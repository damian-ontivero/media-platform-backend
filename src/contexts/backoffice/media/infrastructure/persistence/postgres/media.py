from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from contexts.backoffice.media.domain.media import Media
from contexts.backoffice.shared.infrastructure.persistence.postgres.db import Base


class PostgresMedia(Base):
    __tablename__ = "media"

    id = Column(String(36), primary_key=True)
    title = Column(String(255))
    size = Column(Integer)
    duration = Column(Integer)
    path = Column(String(255))

    @classmethod
    def from_entity(cls, media: Media) -> "PostgresMedia":
        return cls(id=media.id.value, title=media.title, size=media.size, duration=media.duration, path=media.path)

    def update(self, media: Media) -> None:
        self.title = media.title
        self.size = media.size
        self.duration = media.duration
        self.path = media.path

    def to_primitives(self) -> dict:
        return {"id": self.id, "title": self.title, "size": self.size, "duration": self.duration, "path": self.path}
