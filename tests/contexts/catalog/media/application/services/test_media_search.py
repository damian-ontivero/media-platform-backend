from contexts.catalog.media.application.services.media_searcher import MediaSearcher
from tests.contexts.catalog.media.factory.media_factory import MediaFactory


async def test_searcher__ok(mock_media_repository):
    media = MediaFactory.create_batch(10)
    mock_media_repository.matching.return_value = media
    searcher = MediaSearcher(mock_media_repository)

    found_media = searcher.run(filter=None, sort=None, page_size=None, page_number=None)

    assert len(found_media) == 10


async def test_searcher__with_criteria__ok(mock_media_repository):
    media = MediaFactory(title="The Godfather")
    mock_media_repository.matching.return_value = [media]
    searcher = MediaSearcher(mock_media_repository)
    filter = {"conjunction": "AND", "conditions": [{"field": "title", "operator": "EQUALS", "value": "The Godfather"}]}
    sort = None
    page_size = None
    page_number = None

    found_media = searcher.run(filter, sort, page_size, page_number)

    assert found_media == [media]
