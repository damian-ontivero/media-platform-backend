from contexts.catalog.media.application.services.media_finder import MediaFinder
from contexts.catalog.movies.domain.movie import Movie
from contexts.catalog.movies.domain.movie_repository import MovieRepository
from contexts.shared.domain.event_bus.event_bus import EventBus


class MovieCreator:
    def __init__(self, repository: MovieRepository, media_finder: MediaFinder, event_bus: EventBus) -> None:
        self._repository = repository
        self._media_finder = media_finder
        self._event_bus = event_bus

    async def run(self, id: str, title: str, media_id: str) -> None:
        media = self._media_finder.run(media_id)
        movie = Movie.create(id, title, media.duration)

        self._repository.save(movie)
        await self._event_bus.publish(movie.pull_events())
