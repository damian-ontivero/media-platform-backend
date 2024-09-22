from contexts.backoffice.media.domain.media import Media
from contexts.backoffice.media.domain.media_exceptions import MediaDoesNotExist
from contexts.backoffice.media.domain.media_repository import MediaRepository


class MediaFinder:
    def __init__(self, repository: MediaRepository) -> None:
        self._repository = repository

    def run(self, id: str) -> Media:
        media = self._repository.search(id)

        if media is None:
            raise MediaDoesNotExist(id)

        return media
