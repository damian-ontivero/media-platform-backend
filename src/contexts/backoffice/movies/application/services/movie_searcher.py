from contexts.backoffice.movies.domain.movie import Movie
from contexts.backoffice.movies.domain.movie_repository import MovieRepository
from contexts.shared.domain.criteria.criteria import Criteria


class MovieSearcher:
    def __init__(self, repository: MovieRepository) -> None:
        self._repository = repository

    def run(self, filter: dict, sort: list, page_size: int, page_number: int) -> list[Movie]:
        criteria = Criteria.from_primitives(filter, sort, page_size, page_number)

        return self._repository.matching(criteria)
