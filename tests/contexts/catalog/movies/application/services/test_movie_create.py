import faker

from contexts.catalog.movies.application.services.movie_creator import MovieCreator
from tests.contexts.catalog.media.factory.media_factory import MediaFactory


async def test_movie_create__ok(mock_movie_repository, mock_media_finder, mock_event_bus) -> None:
    media = MediaFactory()
    mock_movie_repository.matching.return_value = None
    mock_media_finder.run.return_value = media
    creator = MovieCreator(mock_movie_repository, mock_media_finder, mock_event_bus)

    await creator.run(id=faker.Faker().uuid4(), title=faker.Faker().name(), media_id=media.id.value)

    mock_movie_repository.save.assert_called_once()
    mock_event_bus.publish.assert_called_once()
