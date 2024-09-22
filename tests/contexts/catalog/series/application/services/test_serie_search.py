from contexts.catalog.series.application.services.serie_searcher import SerieSearcher
from tests.contexts.catalog.series.factory.serie_factory import SerieFactory


async def test_searcher__ok(mock_serie_repository):
    series = SerieFactory.create_batch(10)
    mock_serie_repository.matching.return_value = series
    searcher = SerieSearcher(mock_serie_repository)

    found_series = searcher.run(filter=None, sort=None, page_size=None, page_number=None)

    assert len(found_series) == 10


async def test_searcher__with_criteria__ok(mock_serie_repository):
    serie = SerieFactory(title="The Godfather")
    mock_serie_repository.matching.return_value = [serie]
    searcher = SerieSearcher(mock_serie_repository)
    filter = {"conjunction": "AND", "conditions": [{"field": "title", "operator": "EQUALS", "value": "The Godfather"}]}
    sort = None
    page_size = None
    page_number = None

    found_series = searcher.run(filter, sort, page_size, page_number)

    assert found_series == [serie]
