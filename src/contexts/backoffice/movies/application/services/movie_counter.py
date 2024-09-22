from contexts.backoffice.movies.domain.movie_repository import MovieRepository


class MovieCounter:
    def __init__(self, repository: MovieRepository) -> None:
        self._repository = repository

    def run(self) -> int:
        return self._repository.count()
