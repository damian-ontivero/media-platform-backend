from contexts.backoffice.series.domain.serie import Serie
from contexts.backoffice.series.domain.serie_exceptions import SerieDoesNotExist
from contexts.backoffice.series.domain.serie_repository import SerieRepository


class SerieFinder:
    def __init__(self, repository: SerieRepository) -> None:
        self._repository = repository

    def run(self, id: str) -> Serie:
        serie = self._repository.search(id)

        if serie is None:
            raise SerieDoesNotExist(id)

        return serie
