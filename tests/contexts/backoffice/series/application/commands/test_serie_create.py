import faker

from contexts.backoffice.series.application.commands.serie_create_command import SerieCreateCommand
from contexts.backoffice.series.application.commands.serie_create_command_handler import SerieCreateCommandHandler
from contexts.backoffice.series.application.services.serie_creator import SerieCreator
from tests.contexts.backoffice.media.factory.media_factory import MediaFactory
from tests.contexts.backoffice.series.factory.serie_season_factory import SerieSeasonFactory


async def test_serie_create__ok(mock_serie_repository, mock_query_bus, mock_event_bus) -> None:
    media = MediaFactory()
    seasons = SerieSeasonFactory.create_batch(3)
    mock_serie_repository.matching.return_value = None
    mock_query_bus.ask.return_value = media
    creator = SerieCreator(mock_serie_repository, mock_query_bus, mock_event_bus)
    handler = SerieCreateCommandHandler(creator)
    command = SerieCreateCommand(
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

    mock_serie_repository.save.assert_called_once()
    mock_event_bus.publish.assert_called_once()
