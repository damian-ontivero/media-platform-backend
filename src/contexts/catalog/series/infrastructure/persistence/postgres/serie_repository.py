from sqlalchemy.orm import Session

from contexts.catalog.series.domain.serie import Serie
from contexts.catalog.series.domain.serie_repository import SerieRepository
from contexts.catalog.series.infrastructure.persistence.postgres.serie import PostgresSerie
from contexts.shared.domain.criteria.criteria import Criteria
from contexts.shared.infrastructure.criteria.criteria_to_sqlalchemy_query import criteria_to_sqlalchemy_query


class PostgresSerieRepository(SerieRepository):
    def __init__(self, session: Session) -> None:
        self._session = session

    def matching(self, criteria: Criteria) -> list[Serie]:
        with self._session() as session:
            query = session.query(PostgresSerie)
            query = criteria_to_sqlalchemy_query(query, PostgresSerie, criteria)

            return [Serie.from_primitives(**serie_db.to_primitives()) for serie_db in query.all()]

    def search(self, id: str) -> Serie | None:
        with self._session() as session:
            serie_db = session.get(PostgresSerie, id)

            if serie_db is None:
                return None

            return Serie.from_primitives(**serie_db.to_primitives())

    def count(self) -> int:
        with self._session() as session:
            return session.query(PostgresSerie).count()

    def save(self, serie: Serie) -> None:
        with self._session() as session:
            serie_db = session.get(PostgresSerie, serie.id.value)

            if serie_db is None:
                serie_db = PostgresSerie.from_entity(serie)

                session.add(serie_db)
            else:
                serie_db.update(serie)

            session.commit()

    def delete(self, id: str) -> None:
        with self._session() as session:
            serie_db = session.get(PostgresSerie, id)

            session.delete(serie_db)
            session.commit()
