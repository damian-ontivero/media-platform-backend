from contexts.backoffice.media.application.queries.media_search_by_criteria_query import MediaSearchByCriteriaQuery
from contexts.backoffice.media.application.queries.media_search_by_criteria_query_handler import (
    MediaSearchByCriteriaQueryHandler,
)
from contexts.backoffice.media.application.services.media_searcher import MediaSearcher
from tests.contexts.backoffice.media.factory.media_factory import MediaFactory


async def test_searcher__ok(mock_media_repository):
    media = MediaFactory.create_batch(10)
    mock_media_repository.matching.return_value = media
    searcher = MediaSearcher(mock_media_repository)
    query = MediaSearchByCriteriaQuery(filter=None, sort=None, page_size=None, page_number=None)
    handler = MediaSearchByCriteriaQueryHandler(searcher)

    found_media = await handler.handle(query)

    assert len(found_media) == 10


async def test_searcher__with_criteria__ok(mock_media_repository):
    media = MediaFactory(title="The Godfather")
    mock_media_repository.matching.return_value = [media]
    searcher = MediaSearcher(mock_media_repository)
    query = MediaSearchByCriteriaQuery(
        filter={
            "conjunction": "AND",
            "conditions": [{"field": "title", "operator": "EQUALS", "value": "The Godfather"}],
        },
        sort=None,
        page_size=None,
        page_number=None,
    )
    handler = MediaSearchByCriteriaQueryHandler(searcher)

    found_media = await handler.handle(query)

    assert found_media == [media]
