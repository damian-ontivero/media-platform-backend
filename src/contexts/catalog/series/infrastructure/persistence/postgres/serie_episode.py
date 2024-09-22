from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String

from contexts.catalog.shared.infrastructure.persistence.postgres.db import Base


class PostgresSerieEpisode(Base):
    __tablename__ = "serie_episodes"

    id = Column(String(36), primary_key=True)
    number = Column(Integer)
    title = Column(String(255))
    duration = Column(Integer)
    serie_season_id = Column(String(36), ForeignKey("serie_seasons.id"))

    def to_primitives(self) -> dict:
        return {"id": self.id, "number": self.number, "title": self.title, "duration": self.duration}
