from contexts.shared.domain.domain_event import DomainEvent


class MovieCreatedDomainEvent(DomainEvent):
    EVENT_NAME = "catalog.event.movie.created"


class MovieUpdatedDomainEvent(DomainEvent):
    EVENT_NAME = "catalog.event.movie.updated"


class MovieDeletedDomainEvent(DomainEvent):
    EVENT_NAME = "catalog.event.movie.deleted"
