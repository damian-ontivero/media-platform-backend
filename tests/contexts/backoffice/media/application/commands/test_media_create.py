import faker

from contexts.backoffice.media.application.commands.media_create_command import MediaCreateCommand
from contexts.backoffice.media.application.commands.media_create_command_handler import MediaCreateCommandHandler
from contexts.backoffice.media.application.services.media_creator import MediaCreator


async def test_media_create__ok(mock_media_repository, mock_event_bus) -> None:
    mock_media_repository.matching.return_value = None
    creator = MediaCreator(mock_media_repository, mock_event_bus)

    with open("tests/data/video.mp4", "rb") as file:
        command = MediaCreateCommand(title=faker.Faker().name(), file_name="video.mp4", file=file.read())
        handler = MediaCreateCommandHandler(creator)

        await handler.handle(command)

        mock_media_repository.save.assert_called_once()
        mock_event_bus.publish.assert_called_once()
