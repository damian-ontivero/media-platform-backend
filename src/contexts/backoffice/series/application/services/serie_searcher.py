from contexts.backoffice.series.domain.serie import Serie
from contexts.backoffice.series.domain.serie_repository import SerieRepository
from contexts.shared.domain.criteria.criteria import Criteria


class SerieSearcher:
    def __init__(self, repository: SerieRepository) -> None:
        self._repository = repository

    def run(self, filter: dict, sort: list, page_size: int, page_number: int) -> list[Serie]:
        criteria = Criteria.from_primitives(filter, sort, page_size, page_number)

        return self._repository.matching(criteria)
