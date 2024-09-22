from contexts.catalog.media.application.services.media_deleter import MediaDeleter
from tests.contexts.catalog.media.factory.media_factory import MediaFactory


async def test_media_delete__ok(mock_media_repository, mock_event_bus) -> None:
    media = MediaFactory()
    mock_media_repository.search.return_value = media
    deleter = MediaDeleter(mock_media_repository, mock_event_bus)

    await deleter.run(media.id.value)

    mock_media_repository.delete.assert_called_once_with(media.id.value)
    mock_event_bus.publish.assert_called_once()
