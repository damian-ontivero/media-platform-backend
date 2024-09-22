from contexts.catalog.media.domain.media import Media
from contexts.catalog.media.domain.media_repository import MediaRepository
from contexts.shared.domain.event_bus.event_bus import EventBus


class MediaCreator:
    def __init__(self, repository: MediaRepository, event_bus: EventBus) -> None:
        self._repository = repository
        self._event_bus = event_bus

    async def run(self, id: str, title: str, size: int, duration: int, path: str) -> None:
        media = Media.create(id, title, size, duration, path)

        self._repository.save(media)
        await self._event_bus.publish(media.pull_events())
