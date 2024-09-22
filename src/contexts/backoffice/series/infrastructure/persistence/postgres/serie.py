from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship

from contexts.backoffice.series.domain.serie import Serie
from contexts.backoffice.series.infrastructure.persistence.postgres.serie_episode import PostgresSerieEpisode
from contexts.backoffice.series.infrastructure.persistence.postgres.serie_season import PostgresSerieSeason
from contexts.backoffice.shared.infrastructure.persistence.postgres.db import Base


class PostgresSerie(Base):
    __tablename__ = "series"

    id = Column(String(36), primary_key=True)
    title = Column(String(255), index=True)
    synopsis = Column(String(255))
    seasons = relationship("PostgresSerieSeason", cascade="all, delete-orphan")

    @classmethod
    def from_entity(cls, serie: Serie) -> "PostgresSerie":
        return cls(
            id=serie.id.value,
            title=serie.title,
            synopsis=serie.synopsis,
            seasons=[
                PostgresSerieSeason(
                    id=season.id.value,
                    number=season.number,
                    synopsis=season.synopsis,
                    episodes=[
                        PostgresSerieEpisode(
                            id=episode.id.value,
                            number=episode.number,
                            title=episode.title,
                            synopsis=episode.synopsis,
                            media_id=episode.media_id.value,
                        )
                        for episode in season.episodes
                    ],
                )
                for season in serie.seasons
            ],
        )

    def update(self, serie: Serie) -> None:
        self.title = serie.title
        self.seasons = [
            PostgresSerieSeason(
                id=season.id.value,
                number=season.number,
                synopsis=season.synopsis,
                episodes=[
                    PostgresSerieEpisode(
                        id=episode.id.value,
                        number=episode.number,
                        title=episode.title,
                        synopsis=episode.synopsis,
                        media_id=episode.media_id.value,
                        serie_season_id=season.id.value,
                    )
                    for episode in season.episodes
                ],
            )
            for season in serie.seasons
        ]

    def to_primitives(self):
        return {
            "id": self.id,
            "title": self.title,
            "synopsis": self.synopsis,
            "seasons": [season.to_primitives() for season in self.seasons],
        }
