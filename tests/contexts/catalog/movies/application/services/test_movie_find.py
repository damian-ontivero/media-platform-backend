import faker
import pytest

from contexts.catalog.movies.application.services.movie_finder import MovieFinder
from tests.contexts.catalog.movies.factory.movie_factory import MovieFactory


async def test_movie_finder__ok(mock_movie_repository) -> None:
    movie = MovieFactory()
    mock_movie_repository.search.return_value = movie
    finder = MovieFinder(mock_movie_repository)

    found_movie = finder.run(movie.id.value)

    assert found_movie == movie


async def test_movie_finder__not_found(mock_movie_repository) -> None:
    mock_movie_repository.search.return_value = None
    finder = MovieFinder(mock_movie_repository)

    with pytest.raises(Exception):
        finder.run(faker.Faker().uuid4())
