from contexts.backoffice.series.domain.serie_season import SerieSeason
from contexts.shared.backoffice.series.domain.serie_events import SerieCreatedDomainEvent
from contexts.shared.backoffice.series.domain.serie_events import SerieUpdatedDomainEvent
from contexts.shared.domain.aggregate_root import AggregateRoot
from contexts.shared.domain.entity_id import EntityId


class Serie(AggregateRoot):
    def __init__(self, id: EntityId, title: str, synopsis: str, seasons: list[SerieSeason]) -> None:
        super().__init__(id)

        self._title = title
        self._synopsis = synopsis
        self._seasons = seasons

    @property
    def title(self) -> str:
        return self._title

    @property
    def synopsis(self) -> str:
        return self._synopsis

    @property
    def seasons(self) -> list[SerieSeason]:
        return self._seasons

    def __repr__(self) -> str:
        return "{c}(id={id!r}, title={title!r}, synopsis={synopsis!r}, seasons={seasons!r})".format(
            c=self.__class__.__name__, id=self._id, title=self._title, synopsis=self._synopsis, seasons=self._seasons
        )

    @classmethod
    def create(cls, title: str, synopsis: str, seasons: list[dict]) -> "Serie":
        serie = cls(
            EntityId.generate(),
            title,
            synopsis,
            [SerieSeason.create(season["number"], season["synopsis"], season["episodes"]) for season in seasons],
        )

        serie.record(SerieCreatedDomainEvent.create(serie.to_primitives()))

        return serie

    @classmethod
    def from_primitives(cls, id: str, title: str, synopsis: str, seasons: list[dict]) -> "Serie":
        return cls(
            EntityId.from_string(id),
            title,
            synopsis,
            [
                SerieSeason.from_primitives(season["id"], season["number"], season["synopsis"], season["episodes"])
                for season in seasons
            ],
        )

    def update(self, title: str, synopsis: str, seasons: list[dict]) -> None:
        self._title = title
        self._synopsis = synopsis
        self._seasons = [
            SerieSeason.create(season["number"], season["synopsis"], season["episodes"]) for season in seasons
        ]

        self.record(SerieUpdatedDomainEvent.create(self.to_primitives()))

    def to_primitives(self) -> dict:
        return {
            "id": self._id.value,
            "title": self._title,
            "synopsis": self._synopsis,
            "seasons": [season.to_primitives() for season in self._seasons],
        }

    def _ensure_seasons(self) -> None:
        seasons_numbers = [season.number for season in self._seasons]
        duplicated_seasons = set(
            [season_number for season_number in seasons_numbers if seasons_numbers.count(season_number) > 1]
        )

        if duplicated_seasons:
            raise ValueError("Duplicated seasons: {}".format(", ".join(map(str, duplicated_seasons))))
