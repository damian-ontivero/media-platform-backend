from contexts.catalog.media.application.services.media_finder import MediaFinder
from contexts.catalog.series.domain.serie_repository import SerieRepository
from contexts.shared.domain.event_bus.event_bus import EventBus


class SerieUpdater:
    def __init__(self, repository: SerieRepository, media_finder: MediaFinder, event_bus: EventBus) -> None:
        self._repository = repository
        self._media_finder = media_finder
        self._event_bus = event_bus

    async def run(self, id: str, title: str, seasons: list) -> None:
        await self._ensure_media_is_available(seasons)

        serie = self._repository.search(id)

        if serie:
            serie.update(title, seasons)
            self._repository.save(serie)
            await self._event_bus.publish(serie.pull_events())

    async def _ensure_media_is_available(self, seasons: list) -> None:
        for season in seasons:
            for episode in season["episodes"]:
                episode["duration"] = self._media_finder.run(episode["media_id"])

                del episode["media_id"]
