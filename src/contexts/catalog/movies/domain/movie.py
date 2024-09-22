from contexts.shared.domain.aggregate_root import AggregateRoot
from contexts.shared.domain.entity_id import EntityId


class Movie(AggregateRoot):
    def __init__(self, id: EntityId, title: str, duration: int) -> None:
        super().__init__(id)

        self._title = title
        self._duration = duration

    @property
    def title(self) -> str:
        return self._title

    @property
    def duration(self) -> int:
        return self._duration

    def __repr__(self) -> str:
        return "{c}(id={id!r}, title={title!r}, duration={duration!r})".format(
            c=self.__class__.__name__, id=self._id, title=self._title, duration=self._duration
        )

    @classmethod
    def create(cls, id: str, title: str, duration: int) -> "Movie":
        return cls(EntityId.from_string(id), title, duration)

    @classmethod
    def from_primitives(cls, id: str, title: str, duration: int) -> "Movie":
        return cls(EntityId.from_string(id), title, duration)

    def update(self, title: str, duration: int) -> None:
        self._title = title
        self._duration = duration

    def to_primitives(self) -> dict:
        return {"id": self._id.value, "title": self._title, "duration": self._duration}
