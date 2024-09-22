from contexts.backoffice.movies.application.queries.movie_find_by_id_query import MovieFindByIdQuery
from contexts.backoffice.movies.application.services.movie_finder import MovieFinder
from contexts.backoffice.movies.domain.movie import Movie
from contexts.shared.domain.query_bus.query_handler import QueryHandler


class MovieFindByIdQueryHandler(QueryHandler[Movie, MovieFindByIdQuery]):
    def __init__(self, finder: MovieFinder) -> None:
        self._finder = finder

    @staticmethod
    def subscribed_to() -> type[MovieFindByIdQuery]:
        return MovieFindByIdQuery

    async def handle(self, query: MovieFindByIdQuery) -> Movie:
        return self._finder.run(query.id)
