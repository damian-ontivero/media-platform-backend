from contexts.catalog.media.domain.media_events import MediaCreatedDomainEvent
from contexts.catalog.media.domain.media_events import MediaUpdatedDomainEvent
from contexts.shared.domain.aggregate_root import AggregateRoot
from contexts.shared.domain.entity_id import EntityId


class Media(AggregateRoot):
    def __init__(self, id: EntityId, title: str, size: int, duration: int, path: str) -> None:
        super().__init__(id)

        self._title = title
        self._size = size
        self._duration = duration
        self._path = path

    @property
    def title(self) -> str:
        return self._title

    @property
    def size(self) -> int:
        return self._size

    @property
    def duration(self) -> int:
        return self._duration

    @property
    def path(self) -> str:
        return self._path

    def __repr__(self) -> str:
        return "{c}(id={id!r}, title={title!r}, size={size!r}, duration={duration!r}, path={path!r})".format(
            c=self.__class__.__name__,
            id=self._id,
            title=self._title,
            size=self._size,
            duration=self._duration,
            path=self._path,
        )

    @classmethod
    def create(cls, id: str, title: str, size: int, duration: int, path: str) -> "Media":
        media = cls(EntityId.from_string(id), title, size, duration, path)

        media.record(MediaCreatedDomainEvent.create(media.to_primitives()))

        return media

    @classmethod
    def from_primitives(cls, id: str, title: str, size: int, duration: int, path: str) -> "Media":
        return cls(EntityId.from_string(id), title, size, duration, path)

    def update(self, title: str, size: int, duration: int, path: str) -> None:
        self._title = title
        self._size = size
        self._duration = duration
        self._path = path

        self.record(MediaUpdatedDomainEvent.create(self.to_primitives()))

    def to_primitives(self) -> dict:
        return {
            "id": self._id.value,
            "title": self._title,
            "size": self._size,
            "duration": self._duration,
            "path": self._path,
        }
