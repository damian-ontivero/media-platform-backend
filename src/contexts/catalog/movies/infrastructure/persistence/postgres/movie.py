from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from contexts.catalog.movies.domain.movie import Movie
from contexts.catalog.shared.infrastructure.persistence.postgres.db import Base


class PostgresMovie(Base):
    __tablename__ = "movies"

    id = Column(String(36), primary_key=True)
    title = Column(String, index=True)
    duration = Column(Integer)

    @classmethod
    def from_entity(cls, movie: Movie) -> "PostgresMovie":
        return cls(id=movie.id.value, title=movie.title, duration=movie.duration)

    def update(self, movie: Movie) -> None:
        self.title = movie.title
        self.duration = movie.duration

    def to_primitives(self) -> dict:
        return {"id": self.id, "title": self.title, "duration": self.duration}
