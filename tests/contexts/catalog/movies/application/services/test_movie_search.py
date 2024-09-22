from contexts.catalog.movies.application.services.movie_searcher import MovieSearcher
from tests.contexts.catalog.movies.factory.movie_factory import MovieFactory


async def test_searcher__ok(mock_movie_repository):
    movies = MovieFactory.create_batch(10)
    mock_movie_repository.matching.return_value = movies
    searcher = MovieSearcher(mock_movie_repository)

    found_movies = searcher.run(filter=None, sort=None, page_size=None, page_number=None)

    assert len(found_movies) == 10


async def test_searcher__with_criteria__ok(mock_movie_repository):
    movie = MovieFactory(title="The Godfather")
    mock_movie_repository.matching.return_value = [movie]
    searcher = MovieSearcher(mock_movie_repository)
    filter = {"conjunction": "AND", "conditions": [{"field": "title", "operator": "EQUALS", "value": "The Godfather"}]}
    sort = None
    page_size = None
    page_number = None

    found_movies = searcher.run(filter, sort, page_size, page_number)

    assert found_movies == [movie]
