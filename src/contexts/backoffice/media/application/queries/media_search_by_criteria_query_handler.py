from contexts.backoffice.media.application.queries.media_search_by_criteria_query import MediaSearchByCriteriaQuery
from contexts.backoffice.media.application.services.media_searcher import MediaSearcher
from contexts.backoffice.media.domain.media import Media
from contexts.shared.domain.query_bus.query_handler import QueryHandler


class MediaSearchByCriteriaQueryHandler(QueryHandler[Media, MediaSearchByCriteriaQuery]):
    def __init__(self, searcher: MediaSearcher) -> None:
        self._searcher = searcher

    @staticmethod
    def subscribed_to() -> type[MediaSearchByCriteriaQuery]:
        return MediaSearchByCriteriaQuery

    async def handle(self, query: MediaSearchByCriteriaQuery) -> list[Media]:
        return self._searcher.run(query.filter, query.sort, query.page_size, query.page_number)
