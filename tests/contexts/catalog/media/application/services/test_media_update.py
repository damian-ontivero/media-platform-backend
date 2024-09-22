import faker

from contexts.catalog.media.application.services.media_updater import MediaUpdater
from tests.contexts.catalog.media.factory.media_factory import MediaFactory


async def test_media_update__ok(mock_media_repository, mock_event_bus) -> None:
    media = MediaFactory()
    mock_media_repository.search.return_value = media
    mock_media_repository.matching.return_value = None
    updater = MediaUpdater(mock_media_repository, mock_event_bus)

    await updater.run(
        id=media.id.value, title=faker.Faker().name(), size=1000, duration=100, path="backend/tests/data/video.mp4"
    )

    mock_media_repository.save.assert_called_once_with(media)
    mock_event_bus.publish.assert_called_once()
