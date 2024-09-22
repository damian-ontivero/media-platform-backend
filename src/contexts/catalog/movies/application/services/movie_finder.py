from contexts.catalog.movies.domain.movie import Movie
from contexts.catalog.movies.domain.movie_exceptions import MovieDoesNotExist
from contexts.catalog.movies.domain.movie_repository import MovieRepository


class MovieFinder:
    def __init__(self, repository: MovieRepository) -> None:
        self._repository = repository

    def run(self, id: str) -> Movie:
        movie = self._repository.search(id)

        if movie is None:
            raise MovieDoesNotExist(f"Movie with id {id!r} does not exist")

        return movie
