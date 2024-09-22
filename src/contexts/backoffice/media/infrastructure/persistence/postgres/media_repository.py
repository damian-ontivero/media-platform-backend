from sqlalchemy.orm import Session

from contexts.backoffice.media.domain.media import Media
from contexts.backoffice.media.domain.media_repository import MediaRepository
from contexts.backoffice.media.infrastructure.persistence.postgres.media import PostgresMedia
from contexts.shared.infrastructure.criteria.criteria_to_sqlalchemy_query import criteria_to_sqlalchemy_query


class PostgresMediaRepository(MediaRepository):
    def __init__(self, session: Session) -> None:
        self._session = session

    def matching(self, criteria) -> list[Media]:
        with self._session() as session:
            query = session.query(PostgresMedia)
            query = criteria_to_sqlalchemy_query(query, PostgresMedia, criteria)

            return [Media.from_primitives(**media_db.to_primitives()) for media_db in query.all()]

    def search(self, id: str) -> Media | None:
        with self._session() as session:
            media_db = session.get(PostgresMedia, id)

            if media_db is None:
                return None

            return Media.from_primitives(**media_db.to_primitives())

    def count(self) -> int:
        with self._session() as session:
            return session.query(PostgresMedia).count()

    def save(self, media: Media) -> None:
        with self._session() as session:
            media_db = session.get(PostgresMedia, media.id.value)

            if media_db is None:
                media_db = PostgresMedia.from_entity(media)

                session.add(media_db)
            else:
                media_db.update(media)

            session.commit()

    def delete(self, id: str) -> None:
        with self._session() as session:
            media_db = session.get(PostgresMedia, id)

            session.delete(media_db)
            session.commit()
