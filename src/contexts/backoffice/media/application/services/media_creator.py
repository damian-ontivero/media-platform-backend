from contexts.backoffice.media.domain.media import Media
from contexts.backoffice.media.domain.media_exceptions import MediaAlreadyExists
from contexts.backoffice.media.domain.media_repository import MediaRepository
from contexts.shared.domain.criteria.criteria import Criteria
from contexts.shared.domain.event_bus.event_bus import EventBus


class MediaCreator:
    def __init__(self, repository: MediaRepository, event_bus: EventBus) -> None:
        self._repository = repository
        self._event_bus = event_bus

    async def run(self, title: str, size: int, duration: int, path: str) -> None:
        self._ensure_title_is_available(title)

        media = Media.create(title, size, duration, path)

        self._repository.save(media)
        await self._event_bus.publish(media.pull_events())

    def _ensure_title_is_available(self, title: str) -> None:
        criteria = Criteria.from_primitives(
            filter={"conjunction": "AND", "conditions": [{"field": "title", "operator": "EQUALS", "value": title}]},
            sort=None,
            page_size=None,
            page_number=None,
        )
        media = self._repository.matching(criteria)

        if media:
            raise MediaAlreadyExists(title)
