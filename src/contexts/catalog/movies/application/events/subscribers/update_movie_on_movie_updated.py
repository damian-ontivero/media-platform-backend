from contexts.catalog.movies.application.services.movie_updater import MovieUpdater
from contexts.shared.backoffice.movies.domain.movie_events import MovieUpdatedDomainEvent
from contexts.shared.domain.domain_event_subscriber import DomainEventSubscriber


class UpdateMovieOnMovieUpdated(DomainEventSubscriber[MovieUpdatedDomainEvent]):
    def __init__(self, update: MovieUpdater) -> None:
        self._update = update

    @staticmethod
    def subscribed_to() -> list[type[MovieUpdatedDomainEvent]]:
        return [MovieUpdatedDomainEvent]

    async def on(self, event: MovieUpdatedDomainEvent) -> None:
        event_data = event.to_primitives()
        attributes = event_data["attributes"]

        await self._update.run(attributes["id"], attributes["title"], attributes["media_id"])
