from contexts.catalog.media.domain.media_events import MediaDeletedDomainEvent
from contexts.catalog.media.domain.media_repository import MediaRepository
from contexts.shared.domain.event_bus.event_bus import EventBus


class MediaDeleter:
    def __init__(self, repository: MediaRepository, event_bus: EventBus) -> None:
        self._repository = repository
        self._event_bus = event_bus

    async def run(self, id: str) -> None:
        self._repository.delete(id)
        await self._event_bus.publish([MediaDeletedDomainEvent.create({"id": id})])
