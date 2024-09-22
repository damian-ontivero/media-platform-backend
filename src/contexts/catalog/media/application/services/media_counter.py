from contexts.catalog.media.domain.media_repository import MediaRepository


class MediaCounter:
    def __init__(self, repository: MediaRepository) -> None:
        self._repository = repository

    def run(self) -> int:
        return self._repository.count()
