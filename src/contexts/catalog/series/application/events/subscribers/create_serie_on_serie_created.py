from contexts.catalog.series.application.services.serie_creator import SerieCreator
from contexts.shared.backoffice.series.domain.serie_events import SerieCreatedDomainEvent
from contexts.shared.domain.domain_event_subscriber import DomainEventSubscriber


class CreateSerieOnSerieCreated(DomainEventSubscriber[SerieCreatedDomainEvent]):
    def __init__(self, creator: SerieCreator) -> None:
        self._creator = creator

    @staticmethod
    def subscribed_to() -> list[type[SerieCreatedDomainEvent]]:
        return [SerieCreatedDomainEvent]

    async def on(self, event: SerieCreatedDomainEvent) -> None:
        event_data = event.to_primitives()
        attributes = event_data["attributes"]

        await self._creator.run(attributes["id"], attributes["title"], attributes["seasons"])
