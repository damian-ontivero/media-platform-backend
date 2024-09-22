from contexts.catalog.series.domain.serie_events import SerieDeletedDomainEvent
from contexts.catalog.series.domain.serie_repository import SerieRepository
from contexts.shared.domain.event_bus.event_bus import EventBus


class SerieDeleter:
    def __init__(self, repository: SerieRepository, event_bus: EventBus) -> None:
        self._repository = repository
        self._event_bus = event_bus

    async def run(self, id: str) -> None:
        self._repository.delete(id)
        await self._event_bus.publish([SerieDeletedDomainEvent.create({"id": id})])
