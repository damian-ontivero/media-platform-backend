from contexts.backoffice.movies.application.queries.movie_search_by_criteria_query import MovieSearchByCriteriaQuery
from contexts.backoffice.movies.application.queries.movie_search_by_criteria_query_handler import (
    MovieSearchByCriteriaQueryHandler,
)
from contexts.backoffice.movies.application.services.movie_searcher import MovieSearcher
from tests.contexts.backoffice.movies.factory.movie_factory import MovieFactory


async def test_searcher__ok(mock_movie_repository):
    movies = MovieFactory.create_batch(10)
    mock_movie_repository.matching.return_value = movies
    searcher = MovieSearcher(mock_movie_repository)
    query = MovieSearchByCriteriaQuery(filter=None, sort=None, page_size=None, page_number=None)
    handler = MovieSearchByCriteriaQueryHandler(searcher)

    found_movies = await handler.handle(query)

    assert len(found_movies) == 10


async def test_searcher__with_criteria__ok(mock_movie_repository):
    movie = MovieFactory(title="The Godfather")
    mock_movie_repository.matching.return_value = [movie]
    searcher = MovieSearcher(mock_movie_repository)
    query = MovieSearchByCriteriaQuery(
        filter={
            "conjunction": "AND",
            "conditions": [{"field": "title", "operator": "EQUALS", "value": "The Godfather"}],
        },
        sort=None,
        page_size=None,
        page_number=None,
    )
    handler = MovieSearchByCriteriaQueryHandler(searcher)

    found_movies = await handler.handle(query)

    assert found_movies == [movie]
