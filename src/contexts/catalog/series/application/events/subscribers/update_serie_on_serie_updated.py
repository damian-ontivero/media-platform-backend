from contexts.catalog.series.application.services.serie_updater import SerieUpdater
from contexts.shared.backoffice.series.domain.serie_events import SerieUpdatedDomainEvent
from contexts.shared.domain.domain_event_subscriber import DomainEventSubscriber


class UpdateSerieOnSerieUpdated(DomainEventSubscriber[SerieUpdatedDomainEvent]):
    def __init__(self, updater: SerieUpdater) -> None:
        self._updater = updater

    @staticmethod
    def subscribed_to() -> list[type[SerieUpdatedDomainEvent]]:
        return [SerieUpdatedDomainEvent]

    async def on(self, event: SerieUpdatedDomainEvent) -> None:
        event_data = event.to_primitives()
        attributes = event_data["attributes"]

        await self._updater.run(attributes["id"], attributes["title"], attributes["seasons"])
