from contexts.backoffice.series.application.commands.serie_create_command import SerieCreateCommand
from contexts.backoffice.series.application.services.serie_creator import SerieCreator
from contexts.shared.domain.command_bus.command_handler import CommandHandler


class SerieCreateCommandHandler(CommandHandler[SerieCreateCommand]):
    def __init__(self, creator: SerieCreator) -> None:
        self._creator = creator

    @staticmethod
    def subscribed_to() -> type[SerieCreateCommand]:
        return SerieCreateCommand

    async def handle(self, command: SerieCreateCommand) -> None:
        await self._creator.run(command.title, command.synopsis, command.seasons)
