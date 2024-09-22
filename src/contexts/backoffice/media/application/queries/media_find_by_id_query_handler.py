from contexts.backoffice.media.application.services.media_finder import MediaFinder
from contexts.backoffice.media.domain.media import Media
from contexts.backoffice.shared.media.application.queries.media_find_by_id_query import MediaFindByIdQuery
from contexts.shared.domain.query_bus.query_handler import QueryHandler


class MediaFindByIdQueryHandler(QueryHandler[Media, MediaFindByIdQuery]):
    def __init__(self, finder: MediaFinder) -> None:
        self._finder = finder

    @staticmethod
    def subscribed_to() -> type[MediaFindByIdQuery]:
        return MediaFindByIdQuery

    async def handle(self, query: MediaFindByIdQuery) -> Media:
        return self._finder.run(query.id)
