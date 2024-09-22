from contexts.catalog.media.application.services.media_deleter import MediaDeleter
from contexts.shared.backoffice.media.domain.media_events import MediaDeletedDomainEvent
from contexts.shared.domain.domain_event_subscriber import DomainEventSubscriber


class DeleteMediaOnMediaDeleted(DomainEventSubscriber[MediaDeletedDomainEvent]):
    def __init__(self, deleter: MediaDeleter) -> None:
        self._deleter = deleter

    @staticmethod
    def subscribed_to() -> list[type[MediaDeletedDomainEvent]]:
        return [MediaDeletedDomainEvent]

    async def on(self, event: MediaDeletedDomainEvent) -> None:
        event_data = event.to_primitives()
        attributes = event_data["attributes"]

        await self._deleter.run(attributes["id"])
