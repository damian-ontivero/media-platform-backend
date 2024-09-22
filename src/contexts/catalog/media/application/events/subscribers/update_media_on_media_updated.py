from contexts.catalog.media.application.services.media_updater import MediaUpdater
from contexts.shared.backoffice.media.domain.media_events import MediaUpdatedDomainEvent
from contexts.shared.domain.domain_event_subscriber import DomainEventSubscriber


class UpdateMediaOnMediaUpdated(DomainEventSubscriber[MediaUpdatedDomainEvent]):
    def __init__(self, updater: MediaUpdater) -> None:
        self._updater = updater

    @staticmethod
    def subscribed_to() -> list[type[MediaUpdatedDomainEvent]]:
        return [MediaUpdatedDomainEvent]

    async def on(self, event: MediaUpdatedDomainEvent) -> None:
        event_data = event.to_primitives()
        attributes = event_data["attributes"]

        await self._updater.run(
            attributes["id"], attributes["title"], attributes["size"], attributes["duration"], attributes["path"]
        )
