from contexts.catalog.movies.application.services.movie_deleter import MovieDeleter
from tests.contexts.catalog.movies.factory.movie_factory import MovieFactory


async def test_movie_delete__ok(mock_movie_repository, mock_event_bus) -> None:
    movie = MovieFactory()
    mock_movie_repository.search.return_value = movie
    deleter = MovieDeleter(mock_movie_repository, mock_event_bus)

    await deleter.run(movie.id.value)

    mock_movie_repository.delete.assert_called_once_with(movie.id.value)
    mock_event_bus.publish.assert_called_once()
