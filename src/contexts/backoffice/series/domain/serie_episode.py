from contexts.shared.domain.entity import Entity
from contexts.shared.domain.entity_id import EntityId


class SerieEpisode(Entity):
    def __init__(self, id: EntityId, number: int, title: str, synopsis: str, media_id: EntityId) -> None:
        super().__init__(id)

        self._number = number
        self._title = title
        self._synopsis = synopsis
        self._media_id = media_id

    @property
    def number(self) -> int:
        return self._number

    @property
    def title(self) -> str:
        return self._title

    @property
    def synopsis(self) -> str:
        return self._synopsis

    @property
    def media_id(self) -> EntityId:
        return self._media_id

    def __repr__(self) -> str:
        return (
            "{c}(id={id!r}, number={number!r}, title={title!r}, synopsis={synopsis!r}, media_id={media_id!r})".format(
                c=self.__class__.__name__,
                id=self._id,
                number=self._number,
                title=self._title,
                synopsis=self._synopsis,
                media_id=self._media_id,
            )
        )

    @classmethod
    def create(cls, number: int, title: str, synopsis: str, media_id: str) -> "SerieEpisode":
        return cls(EntityId.generate(), number, title, synopsis, EntityId.from_string(media_id))

    @classmethod
    def from_primitives(cls, id: str, number: int, title: str, synopsis: str, media_id: str) -> "SerieEpisode":
        return cls(EntityId.from_string(id), number, title, synopsis, EntityId.from_string(media_id))

    def to_primitives(self) -> dict:
        return {
            "id": self._id.value,
            "number": self._number,
            "title": self._title,
            "synopsis": self._synopsis,
            "media_id": self._media_id.value,
        }
