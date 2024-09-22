import faker
import pytest

from contexts.catalog.media.application.services.media_finder import MediaFinder
from tests.contexts.catalog.media.factory.media_factory import MediaFactory


async def test_media_finder__ok(mock_media_repository) -> None:
    media = MediaFactory()
    mock_media_repository.search.return_value = media
    finder = MediaFinder(mock_media_repository)

    found_media = finder.run(media.id.value)

    assert found_media == media


async def test_media_finder__not_found(mock_media_repository) -> None:
    mock_media_repository.search.return_value = None
    finder = MediaFinder(mock_media_repository)

    with pytest.raises(Exception):
        finder.run(faker.Faker().uuid4())
