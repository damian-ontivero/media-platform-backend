from contexts.backoffice.series.domain.serie_episode import SerieEpisode
from contexts.shared.domain.entity import Entity
from contexts.shared.domain.entity_id import EntityId


class SerieSeason(Entity):
    def __init__(self, id: EntityId, number: int, synopsis: str, episodes: list[SerieEpisode]) -> None:
        super().__init__(id)

        self._number = number
        self._synopsis = synopsis
        self._episodes = episodes

        self._ensure_episodes()

    @property
    def number(self) -> int:
        return self._number

    @property
    def synopsis(self) -> str:
        return self._synopsis

    @property
    def episodes(self) -> list[SerieEpisode]:
        return self._episodes

    def __repr__(self) -> str:
        return "{c}(id={id!r}, number={number!r}, synopsis={synopsis!r}, episodes={episodes!r})".format(
            c=self.__class__.__name__,
            id=self._id,
            number=self._number,
            synopsis=self._synopsis,
            episodes=self._episodes,
        )

    @classmethod
    def create(cls, number: int, synopsis: str, episodes: list[dict]) -> "SerieSeason":
        return cls(
            EntityId.generate(),
            number,
            synopsis,
            [
                SerieEpisode.create(episode["number"], episode["title"], episode["synopsis"], episode["media_id"])
                for episode in episodes
            ],
        )

    @classmethod
    def from_primitives(cls, id: str, number: int, synopsis: str, episodes: list[dict]) -> "SerieSeason":
        return cls(
            EntityId.from_string(id),
            number,
            synopsis,
            [
                SerieEpisode.from_primitives(
                    episode["id"], episode["number"], episode["title"], episode["synopsis"], episode["media_id"]
                )
                for episode in episodes
            ],
        )

    def to_primitives(self) -> dict:
        return {
            "id": self._id.value,
            "number": self._number,
            "synopsis": self._synopsis,
            "episodes": [episode.to_primitives() for episode in self._episodes],
        }

    def _ensure_episodes(self) -> None:
        episodes_numbers = [episode.number for episode in self._episodes]
        duplicated_episodes = set(
            [episode_number for episode_number in episodes_numbers if episodes_numbers.count(episode_number) > 1]
        )

        if duplicated_episodes:
            raise ValueError("Duplicated episodes: {}".format(", ".join(map(str, duplicated_episodes))))
