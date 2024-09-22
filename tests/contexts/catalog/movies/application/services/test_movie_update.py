import faker

from contexts.catalog.movies.application.services.movie_updater import MovieUpdater
from tests.contexts.catalog.media.factory.media_factory import MediaFactory
from tests.contexts.catalog.movies.factory.movie_factory import MovieFactory


async def test_movie_update__ok(mock_movie_repository, mock_media_finder, mock_event_bus) -> None:
    movie = MovieFactory()
    media = MediaFactory()
    mock_movie_repository.search.return_value = movie
    mock_movie_repository.matching.return_value = None
    mock_media_finder.run.return_value = media
    updater = MovieUpdater(mock_movie_repository, mock_media_finder, mock_event_bus)

    await updater.run(id=movie.id.value, title=faker.Faker().name(), media_id=media.id.value)

    mock_movie_repository.save.assert_called_once_with(movie)
    mock_event_bus.publish.assert_called_once()
