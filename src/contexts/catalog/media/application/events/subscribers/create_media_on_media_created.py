from contexts.catalog.media.application.services.media_creator import MediaCreator
from contexts.shared.backoffice.media.domain.media_events import MediaCreatedDomainEvent
from contexts.shared.domain.domain_event_subscriber import DomainEventSubscriber


class CreateMediaOnMediaCreated(DomainEventSubscriber[MediaCreatedDomainEvent]):
    def __init__(self, creator: MediaCreator) -> None:
        self._creator = creator

    @staticmethod
    def subscribed_to() -> list[type[MediaCreatedDomainEvent]]:
        return [MediaCreatedDomainEvent]

    async def on(self, event: MediaCreatedDomainEvent) -> None:
        event_data = event.to_primitives()
        attributes = event_data["attributes"]

        await self._creator.run(
            attributes["id"], attributes["title"], attributes["size"], attributes["duration"], attributes["path"]
        )
