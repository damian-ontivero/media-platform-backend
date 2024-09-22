import faker
import pytest

from contexts.backoffice.series.application.commands.serie_update_command import SerieUpdateCommand
from contexts.backoffice.series.application.commands.serie_update_command_handler import SerieUpdateCommandHandler
from contexts.backoffice.series.application.services.serie_updater import SerieUpdater
from contexts.backoffice.series.domain.serie_exceptions import SerieDoesNotExist
from tests.contexts.backoffice.series.factory.serie_factory import SerieFactory
from tests.contexts.backoffice.series.factory.serie_season_factory import SerieSeasonFactory


async def test_serie_update__ok(mock_serie_repository, mock_query_bus, mock_event_bus) -> None:
    serie = SerieFactory()
    seasons = SerieSeasonFactory.create_batch(3)
    mock_serie_repository.search.return_value = serie
    mock_serie_repository.matching.return_value = None
    updater = SerieUpdater(mock_serie_repository, mock_query_bus, mock_event_bus)
    handler = SerieUpdateCommandHandler(updater)
    command = SerieUpdateCommand(
        id=serie.id.value,
        title=faker.Faker().name(),
        synopsis=faker.Faker().text(),
        seasons=[
            {
                "number": season.number,
                "synopsis": season.synopsis,
                "episodes": [
                    {
                        "number": episode.number,
                        "title": episode.title,
                        "synopsis": episode.synopsis,
                        "media_id": episode.media_id,
                    }
                    for episode in season.episodes
                ],
            }
            for season in seasons
        ],
    )

    await handler.handle(command)

    mock_serie_repository.save.assert_called_once_with(serie)
    mock_event_bus.publish.assert_called_once()


async def test_serie_update__not_found(mock_serie_repository, mock_query_bus, mock_event_bus) -> None:
    mock_serie_repository.search.return_value = None
    updater = SerieUpdater(mock_serie_repository, mock_query_bus, mock_event_bus)
    handler = SerieUpdateCommandHandler(updater)
    command = SerieUpdateCommand(
        id=faker.Faker().uuid4(), title=faker.Faker().name(), synopsis=faker.Faker().text(), seasons=[]
    )

    with pytest.raises(SerieDoesNotExist):
        await handler.handle(command)
