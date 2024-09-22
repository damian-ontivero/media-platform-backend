from contexts.shared.domain.domain_event import DomainEvent


class SerieCreatedDomainEvent(DomainEvent):
    EVENT_NAME = "backoffice.event.serie.created"


class SerieUpdatedDomainEvent(DomainEvent):
    EVENT_NAME = "backoffice.event.serie.updated"


class SerieDeletedDomainEvent(DomainEvent):
    EVENT_NAME = "backoffice.event.serie.deleted"
