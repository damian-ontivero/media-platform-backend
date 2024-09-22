from contexts.backoffice.media.domain.media import Media
from contexts.backoffice.media.domain.media_repository import MediaRepository
from contexts.shared.domain.criteria.criteria import Criteria


class MediaSearcher:
    def __init__(self, repository: MediaRepository) -> None:
        self._repository = repository

    def run(self, filter: dict, sort: list, page_size: int, page_number: int) -> list[Media]:
        criteria = Criteria.from_primitives(filter, sort, page_size, page_number)

        return self._repository.matching(criteria)
