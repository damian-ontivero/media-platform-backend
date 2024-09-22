from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship

from contexts.backoffice.shared.infrastructure.persistence.postgres.db import Base


class PostgresSerieSeason(Base):
    __tablename__ = "serie_seasons"

    id = Column(String(36), primary_key=True)
    number = Column(Integer)
    synopsis = Column(String(255))
    serie_id = Column(ForeignKey("series.id"))
    episodes = relationship("PostgresSerieEpisode", cascade="all, delete-orphan")

    def to_primitives(self) -> dict:
        return {
            "id": self.id,
            "number": self.number,
            "synopsis": self.synopsis,
            "episodes": [episode.to_primitives() for episode in self.episodes],
        }
