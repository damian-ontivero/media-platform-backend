import faker
import pytest

from contexts.backoffice.media.application.commands.media_update_command import MediaUpdateCommand
from contexts.backoffice.media.application.commands.media_update_command_handler import MediaUpdateCommandHandler
from contexts.backoffice.media.application.services.media_updater import MediaUpdater
from contexts.backoffice.media.domain.media_exceptions import MediaDoesNotExist
from tests.contexts.backoffice.media.factory.media_factory import MediaFactory


async def test_media_update__ok(mock_media_repository, mock_event_bus) -> None:
    media = MediaFactory()
    mock_media_repository.search.return_value = media
    mock_media_repository.matching.return_value = None
    updater = MediaUpdater(mock_media_repository, mock_event_bus)

    with open("tests/data/video.mp4", "rb") as file:
        command = MediaUpdateCommand(
            id=media.id.value, title=faker.Faker().name(), file_name="video.mp4", file=file.read()
        )
        handler = MediaUpdateCommandHandler(updater)

        await handler.handle(command)

        mock_media_repository.save.assert_called_once_with(media)
        mock_event_bus.publish.assert_called_once()


async def test_media_update__not_found(mock_media_repository, mock_event_bus) -> None:
    media = MediaFactory()
    mock_media_repository.search.return_value = None
    updater = MediaUpdater(mock_media_repository, mock_event_bus)

    with open("tests/data/video.mp4", "rb") as file:
        command = MediaUpdateCommand(
            id=media.id.value, title=faker.Faker().name(), file_name="video.mp4", file=file.read()
        )
        handler = MediaUpdateCommandHandler(updater)

        with pytest.raises(MediaDoesNotExist):
            await handler.handle(command)
