from contexts.backoffice.movies.application.queries.movie_count_query import MovieCountQuery
from contexts.backoffice.movies.application.services.movie_counter import MovieCounter
from contexts.backoffice.movies.domain.movie import Movie
from contexts.shared.domain.query_bus.query_handler import QueryHandler


class MovieCountQueryHandler(QueryHandler[Movie, MovieCountQuery]):
    def __init__(self, counter: MovieCounter) -> None:
        self._counter = counter

    @staticmethod
    def subscribed_to() -> type[MovieCountQuery]:
        return MovieCountQuery

    async def handle(self, query: MovieCountQuery) -> int:
        return self._counter.run()
