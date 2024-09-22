from contexts.backoffice.movies.domain.movie import Movie
from contexts.backoffice.movies.domain.movie_exceptions import MovieDoesNotExist
from contexts.backoffice.movies.domain.movie_repository import MovieRepository


class MovieFinder:
    def __init__(self, repository: MovieRepository) -> None:
        self._repository = repository

    def run(self, id: str) -> Movie:
        movie = self._repository.search(id)

        if movie is None:
            raise MovieDoesNotExist(id)

        return movie
