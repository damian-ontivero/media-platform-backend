from contexts.backoffice.movies.application.queries.movie_search_by_criteria_query import MovieSearchByCriteriaQuery
from contexts.backoffice.movies.application.services.movie_searcher import MovieSearcher
from contexts.backoffice.movies.domain.movie import Movie
from contexts.shared.domain.query_bus.query_handler import QueryHandler


class MovieSearchByCriteriaQueryHandler(QueryHandler[Movie, MovieSearchByCriteriaQuery]):
    def __init__(self, searcher: MovieSearcher) -> None:
        self._searcher = searcher

    @staticmethod
    def subscribed_to() -> type[MovieSearchByCriteriaQuery]:
        return MovieSearchByCriteriaQuery

    async def handle(self, query: MovieSearchByCriteriaQuery) -> list[Movie]:
        return self._searcher.run(query.filter, query.sort, query.page_size, query.page_number)
