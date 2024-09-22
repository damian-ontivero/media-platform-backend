from contexts.backoffice.series.application.queries.serie_search_by_criteria_query import SerieSearchByCriteriaQuery
from contexts.backoffice.series.application.services.serie_searcher import SerieSearcher
from contexts.backoffice.series.domain.serie import Serie
from contexts.shared.domain.query_bus.query_handler import QueryHandler


class SerieSearchByCriteriaQueryHandler(QueryHandler[Serie, SerieSearchByCriteriaQuery]):
    def __init__(self, searcher: SerieSearcher) -> None:
        self._searcher = searcher

    @staticmethod
    def subscribed_to() -> type[SerieSearchByCriteriaQuery]:
        return SerieSearchByCriteriaQuery

    async def handle(self, query: SerieSearchByCriteriaQuery) -> list[Serie]:
        return self._searcher.run(query.filter, query.sort, query.page_size, query.page_number)
