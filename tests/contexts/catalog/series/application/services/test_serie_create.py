import faker

from contexts.catalog.series.application.services.serie_creator import SerieCreator
from tests.contexts.catalog.media.factory.media_factory import MediaFactory
from tests.contexts.catalog.series.factory.serie_season_factory import SerieSeasonFactory


async def test_serie_create__ok(mock_serie_repository, mock_media_finder, mock_event_bus) -> None:
    media = MediaFactory()
    seasons = SerieSeasonFactory.create_batch(3)
    mock_serie_repository.matching.return_value = None
    mock_media_finder.run.return_value = media
    creator = SerieCreator(mock_serie_repository, mock_media_finder, mock_event_bus)
    title = faker.Faker().name()
    seasons = [
        {
            "id": season.id.value,
            "number": season.number,
            "episodes": [
                {"id": episode.id.value, "number": episode.number, "title": episode.title, "media_id": media.id.value}
                for episode in season.episodes
            ],
        }
        for season in seasons
    ]

    await creator.run(id=faker.Faker().uuid4(), title=title, seasons=seasons)

    mock_serie_repository.save.assert_called_once()
    mock_event_bus.publish.assert_called_once()
