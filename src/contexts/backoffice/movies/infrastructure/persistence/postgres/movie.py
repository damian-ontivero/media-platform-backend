from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String

from contexts.backoffice.movies.domain.movie import Movie
from contexts.backoffice.shared.infrastructure.persistence.postgres.db import Base


class PostgresMovie(Base):
    __tablename__ = "movies"

    id = Column(String(36), primary_key=True)
    title = Column(String(255), index=True)
    synopsis = Column(String(255))
    media_id = Column(ForeignKey("media.id"))

    @classmethod
    def from_entity(cls, movie: Movie) -> "PostgresMovie":
        return cls(id=movie.id.value, title=movie.title, synopsis=movie.synopsis, media_id=movie.media_id.value)

    def update(self, movie: Movie) -> None:
        self.title = movie.title
        self.synopsis = movie.synopsis
        self.media_id = movie.media_id.value

    def to_primitives(self) -> dict:
        return {"id": self.id, "title": self.title, "synopsis": self.synopsis, "media_id": self.media_id}
