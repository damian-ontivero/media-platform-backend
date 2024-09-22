from contexts.backoffice.series.application.queries.serie_find_by_id_query import SerieFindByIdQuery
from contexts.backoffice.series.application.services.serie_finder import SerieFinder
from contexts.backoffice.series.domain.serie import Serie
from contexts.shared.domain.query_bus.query_handler import QueryHandler


class SerieFindByIdQueryHandler(QueryHandler[Serie, SerieFindByIdQuery]):
    def __init__(self, finder: SerieFinder) -> None:
        self._finder = finder

    @staticmethod
    def subscribed_to() -> type[SerieFindByIdQuery]:
        return SerieFindByIdQuery

    async def handle(self, query: SerieFindByIdQuery) -> Serie:
        return self._finder.run(query.id)
