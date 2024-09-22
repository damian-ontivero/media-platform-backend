from contexts.catalog.movies.application.services.movie_deleter import MovieDeleter
from contexts.shared.backoffice.movies.domain.movie_events import MovieDeletedDomainEvent
from contexts.shared.domain.domain_event_subscriber import DomainEventSubscriber


class DeleteMovieOnMovieDeleted(DomainEventSubscriber[MovieDeletedDomainEvent]):
    def __init__(self, deleter: MovieDeleter) -> None:
        self._deleter = deleter

    @staticmethod
    def subscribed_to() -> list[type[MovieDeletedDomainEvent]]:
        return [MovieDeletedDomainEvent]

    async def on(self, event: MovieDeletedDomainEvent) -> None:
        event_data = event.to_primitives()
        attributes = event_data["attributes"]

        await self._deleter.run(attributes["id"])
