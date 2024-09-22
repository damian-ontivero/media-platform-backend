from contexts.shared.domain.entity import Entity
from contexts.shared.domain.entity_id import EntityId


class SerieEpisode(Entity):
    def __init__(self, id: EntityId, number: int, title: str, duration: int) -> None:
        super().__init__(id)

        self._number = number
        self._title = title
        self._duration = duration

    @property
    def number(self) -> int:
        return self._number

    @property
    def title(self) -> str:
        return self._title

    @property
    def duration(self) -> int:
        return self._duration

    def __repr__(self) -> str:
        return "{c}(id={id!r}, number={number!r}, title={title!r}, duration={duration!r})".format(
            c=self.__class__.__name__, id=self._id, number=self._number, title=self._title, duration=self._duration
        )

    @classmethod
    def create(cls, id: str, number: int, title: str, duration: int) -> "SerieEpisode":
        return cls(EntityId.from_string(id), number, title, duration)

    @classmethod
    def from_primitives(cls, id: str, number: int, title: str, duration: int) -> "SerieEpisode":
        return cls(EntityId.from_string(id), number, title, duration)

    def to_primitives(self) -> dict:
        return {"id": self._id.value, "number": self._number, "title": self._title, "duration": self._duration}
