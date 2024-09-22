import faker
import pytest

from contexts.backoffice.movies.application.queries.movie_find_by_id_query import MovieFindByIdQuery
from contexts.backoffice.movies.application.queries.movie_find_by_id_query_handler import MovieFindByIdQueryHandler
from contexts.backoffice.movies.application.services.movie_finder import MovieFinder
from tests.contexts.backoffice.movies.factory.movie_factory import MovieFactory


async def test_movie_finder__ok(mock_movie_repository) -> None:
    movie = MovieFactory()
    mock_movie_repository.search.return_value = movie
    finder = MovieFinder(mock_movie_repository)
    query = MovieFindByIdQuery(movie.id.value)
    handler = MovieFindByIdQueryHandler(finder)

    found_movie = await handler.handle(query)

    assert found_movie == movie


async def test_movie_finder__not_found(mock_movie_repository) -> None:
    mock_movie_repository.search.return_value = None
    finder = MovieFinder(mock_movie_repository)
    query = MovieFindByIdQuery(faker.Faker().uuid4())
    handler = MovieFindByIdQueryHandler(finder)

    with pytest.raises(Exception):
        await handler.handle(query)
