from contexts.backoffice.media.application.commands.media_delete_command import MediaDeleteCommand
from contexts.backoffice.media.application.services.media_deleter import MediaDeleter
from contexts.shared.domain.command_bus.command_handler import CommandHandler


class MediaDeleteCommandHandler(CommandHandler[MediaDeleteCommand]):
    def __init__(self, deleter: MediaDeleter) -> None:
        self._deleter = deleter

    @staticmethod
    def subscribed_to() -> type[MediaDeleteCommand]:
        return MediaDeleteCommand

    async def handle(self, command: MediaDeleteCommand) -> None:
        await self._deleter.run(command.id)
