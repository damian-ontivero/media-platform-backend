from sqlalchemy.orm import Session

from contexts.catalog.movies.domain.movie import Movie
from contexts.catalog.movies.domain.movie_repository import MovieRepository
from contexts.catalog.movies.infrastructure.persistence.postgres.movie import PostgresMovie
from contexts.shared.infrastructure.criteria.criteria_to_sqlalchemy_query import criteria_to_sqlalchemy_query


class PostgresMovieRepository(MovieRepository):
    def __init__(self, session: Session) -> None:
        self._session = session

    def matching(self, criteria) -> list[Movie]:
        with self._session() as session:
            query = session.query(PostgresMovie)
            query = criteria_to_sqlalchemy_query(query, PostgresMovie, criteria)

            return [Movie.from_primitives(**movie_db.to_primitives()) for movie_db in query.all()]

    def search(self, id: str) -> Movie | None:
        with self._session() as session:
            movie_db = session.get(PostgresMovie, id)

            if movie_db is None:
                return None

            return Movie.from_primitives(**movie_db.to_primitives())

    def count(self) -> int:
        with self._session() as session:
            return session.query(PostgresMovie).count()

    def save(self, movie: Movie) -> None:
        with self._session() as session:
            movie_db = session.get(PostgresMovie, movie.id.value)

            if movie_db is None:
                movie_db = PostgresMovie.from_entity(movie)

                session.add(movie_db)
            else:
                movie_db.update(movie)

            session.commit()

    def delete(self, id: str) -> None:
        with self._session() as session:
            movie_db = session.get(PostgresMovie, id)

            session.delete(movie_db)
            session.commit()
