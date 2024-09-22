from contexts.catalog.series.application.services.serie_deleter import SerieDeleter
from contexts.shared.backoffice.series.domain.serie_events import SerieDeletedDomainEvent
from contexts.shared.domain.domain_event_subscriber import DomainEventSubscriber


class DeleteSerieOnSerieDeleted(DomainEventSubscriber[SerieDeletedDomainEvent]):
    def __init__(self, deleter: SerieDeleter) -> None:
        self._deleter = deleter

    @staticmethod
    def subscribed_to() -> list[type[SerieDeletedDomainEvent]]:
        return [SerieDeletedDomainEvent]

    async def on(self, event: SerieDeletedDomainEvent) -> None:
        event_data = event.to_primitives()
        attributes = event_data["attributes"]

        await self._deleter.run(attributes["id"])
