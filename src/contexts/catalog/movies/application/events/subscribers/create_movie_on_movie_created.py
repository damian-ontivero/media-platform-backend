from contexts.catalog.movies.application.services.movie_creator import MovieCreator
from contexts.shared.backoffice.movies.domain.movie_events import MovieCreatedDomainEvent
from contexts.shared.domain.domain_event_subscriber import DomainEventSubscriber


class CreateMovieOnMovieCreated(DomainEventSubscriber[MovieCreatedDomainEvent]):
    def __init__(self, creator: MovieCreator) -> None:
        self._creator = creator

    @staticmethod
    def subscribed_to() -> list[type[MovieCreatedDomainEvent]]:
        return [MovieCreatedDomainEvent]

    async def on(self, event: MovieCreatedDomainEvent) -> None:
        event_data = event.to_primitives()
        attributes = event_data["attributes"]

        await self._creator.run(attributes["id"], attributes["title"], attributes["media_id"])
