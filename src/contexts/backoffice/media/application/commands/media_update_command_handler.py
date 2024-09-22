import os

from moviepy.editor import VideoFileClip

from contexts.backoffice.media.application.commands.media_update_command import MediaUpdateCommand
from contexts.backoffice.media.application.services.media_updater import MediaUpdater
from contexts.shared.domain.command_bus.command_handler import CommandHandler
from contexts.shared.infrastructure.file_manager.file_manager import FileManager


MEDIA_STORAGE_PATH = os.getenv("MEDIA_STORAGE_PATH", "")


class MediaUpdateCommandHandler(CommandHandler[MediaUpdateCommand]):
    def __init__(self, updater: MediaUpdater) -> None:
        self._updater = updater
        self._file_manager = FileManager(MEDIA_STORAGE_PATH)

    @staticmethod
    def subscribed_to() -> type[MediaUpdateCommand]:
        return MediaUpdateCommand

    async def handle(self, command: MediaUpdateCommand) -> None:
        file_path = self._file_manager.save_file(command.title, command.file_name, command.file)
        size = os.path.getsize(file_path)
        duration = VideoFileClip(file_path).duration

        await self._updater.run(command.id, command.title, size, duration, file_path)
