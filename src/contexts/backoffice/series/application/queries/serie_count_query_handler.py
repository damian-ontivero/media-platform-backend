from contexts.backoffice.series.application.queries.serie_count_query import SerieCountQuery
from contexts.backoffice.series.application.services.serie_counter import SerieCounter
from contexts.backoffice.series.domain.serie import Serie
from contexts.shared.domain.query_bus.query_handler import QueryHandler


class SerieCountQueryHandler(QueryHandler[Serie, SerieCountQuery]):
    def __init__(self, counter: SerieCounter) -> None:
        self._counter = counter

    @staticmethod
    def subscribed_to() -> type[SerieCountQuery]:
        return SerieCountQuery

    async def handle(self, query: SerieCountQuery) -> int:
        return self._counter.run()
