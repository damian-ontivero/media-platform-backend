from contexts.catalog.movies.domain.movie_events import MovieDeletedDomainEvent
from contexts.catalog.movies.domain.movie_repository import MovieRepository
from contexts.shared.domain.event_bus.event_bus import EventBus


class MovieDeleter:
    def __init__(self, repository: MovieRepository, event_bus: EventBus) -> None:
        self._repository = repository
        self._event_bus = event_bus

    async def run(self, id: str) -> None:
        self._repository.delete(id)
        await self._event_bus.publish([MovieDeletedDomainEvent.create({"id": id})])
