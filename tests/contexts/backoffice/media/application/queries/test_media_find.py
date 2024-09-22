import faker
import pytest

from contexts.backoffice.media.application.queries.media_find_by_id_query_handler import MediaFindByIdQueryHandler
from contexts.backoffice.media.application.services.media_finder import MediaFinder
from contexts.backoffice.shared.media.application.queries.media_find_by_id_query import MediaFindByIdQuery
from tests.contexts.backoffice.media.factory.media_factory import MediaFactory


async def test_media_finder__ok(mock_media_repository) -> None:
    media = MediaFactory()
    mock_media_repository.search.return_value = media
    finder = MediaFinder(mock_media_repository)
    query = MediaFindByIdQuery(media.id.value)
    handler = MediaFindByIdQueryHandler(finder)

    found_media = await handler.handle(query)

    assert found_media == media


async def test_media_finder__not_found(mock_media_repository) -> None:
    mock_media_repository.search.return_value = None
    finder = MediaFinder(mock_media_repository)
    query = MediaFindByIdQuery(faker.Faker().uuid4())
    handler = MediaFindByIdQueryHandler(finder)

    with pytest.raises(Exception):
        await handler.handle(query)
