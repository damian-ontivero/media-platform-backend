from contexts.catalog.series.domain.serie_repository import SerieRepository


class SerieCounter:
    def __init__(self, repository: SerieRepository) -> None:
        self._repository = repository

    def run(self) -> int:
        return self._repository.count()
