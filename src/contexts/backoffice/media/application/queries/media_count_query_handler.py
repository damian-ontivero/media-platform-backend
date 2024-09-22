from contexts.backoffice.media.application.queries.media_count_query import MediaCountQuery
from contexts.backoffice.media.application.services.media_counter import MediaCounter
from contexts.backoffice.media.domain.media import Media
from contexts.shared.domain.query_bus.query_handler import QueryHandler


class MediaCountQueryHandler(QueryHandler[Media, MediaCountQuery]):
    def __init__(self, counter: MediaCounter) -> None:
        self._counter = counter

    @staticmethod
    def subscribed_to() -> type[MediaCountQuery]:
        return MediaCountQuery

    async def handle(self, query: MediaCountQuery) -> int:
        return self._counter.run()
