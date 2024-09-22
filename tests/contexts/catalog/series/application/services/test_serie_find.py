import faker
import pytest

from contexts.catalog.series.application.services.serie_finder import SerieFinder
from tests.contexts.catalog.series.factory.serie_factory import SerieFactory


async def test_serie_finder__ok(mock_serie_repository) -> None:
    serie = SerieFactory()
    mock_serie_repository.search.return_value = serie
    finder = SerieFinder(mock_serie_repository)

    found_serie = finder.run(serie.id.value)

    assert found_serie == serie


async def test_serie_finder__not_found(mock_serie_repository) -> None:
    mock_serie_repository.search.return_value = None
    finder = SerieFinder(mock_serie_repository)

    with pytest.raises(Exception):
        finder.run(faker.Faker().uuid4())
