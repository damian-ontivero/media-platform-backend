from contexts.backoffice.series.application.commands.serie_delete_command import SerieDeleteCommand
from contexts.backoffice.series.application.services.serie_deleter import SerieDeleter
from contexts.shared.domain.command_bus.command_handler import CommandHandler


class SerieDeleteCommandHandler(CommandHandler[SerieDeleteCommand]):
    def __init__(self, deleter: SerieDeleter) -> None:
        self._deleter = deleter

    @staticmethod
    def subscribed_to() -> type[SerieDeleteCommand]:
        return SerieDeleteCommand

    async def handle(self, command: SerieDeleteCommand) -> None:
        await self._deleter.run(command.id)
