from contexts.shared.domain.domain_event import DomainEvent


class MediaCreatedDomainEvent(DomainEvent):
    EVENT_NAME = "catalog.event.media.created"


class MediaUpdatedDomainEvent(DomainEvent):
    EVENT_NAME = "catalog.event.media.updated"


class MediaDeletedDomainEvent(DomainEvent):
    EVENT_NAME = "catalog.event.media.deleted"
