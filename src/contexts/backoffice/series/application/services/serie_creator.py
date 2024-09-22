from contexts.backoffice.series.domain.serie import Serie
from contexts.backoffice.series.domain.serie_exceptions import SerieAlreadyExists
from contexts.backoffice.series.domain.serie_repository import SerieRepository
from contexts.backoffice.shared.media.application.queries.media_find_by_id_query import MediaFindByIdQuery
from contexts.shared.domain.criteria.criteria import Criteria
from contexts.shared.domain.event_bus.event_bus import EventBus
from contexts.shared.domain.query_bus.query_bus import QueryBus


class SerieCreator:
    def __init__(self, repository: SerieRepository, query_bus: QueryBus, event_bus: EventBus) -> None:
        self._repository = repository
        self._query_bus = query_bus
        self._event_bus = event_bus

    async def run(self, title: str, synopsis: str, seasons: list) -> None:
        self._ensure_title_is_available(title)
        await self._ensure_media_is_available(seasons)

        serie = Serie.create(title, synopsis, seasons)

        self._repository.save(serie)
        await self._event_bus.publish(serie.pull_events())

    def _ensure_title_is_available(self, title: str) -> None:
        criteria = Criteria.from_primitives(
            filter={"conjunction": "AND", "conditions": [{"field": "title", "operator": "EQUALS", "value": title}]},
            sort=None,
            page_size=None,
            page_number=None,
        )
        serie = self._repository.matching(criteria)

        if serie:
            raise SerieAlreadyExists(title)

    async def _ensure_media_is_available(self, seasons: list) -> None:
        for season in seasons:
            for episode in season["episodes"]:
                await self._query_bus.ask(MediaFindByIdQuery(episode["media_id"]))
