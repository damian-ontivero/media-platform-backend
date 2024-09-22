from contexts.backoffice.movies.application.commands.movie_delete_command import MovieDeleteCommand
from contexts.backoffice.movies.application.services.movie_deleter import MovieDeleter
from contexts.shared.domain.command_bus.command_handler import CommandHandler


class MovieDeleteCommandHandler(CommandHandler[MovieDeleteCommand]):
    def __init__(self, deleter: MovieDeleter) -> None:
        self._deleter = deleter

    @staticmethod
    def subscribed_to() -> type[MovieDeleteCommand]:
        return MovieDeleteCommand

    async def handle(self, command: MovieDeleteCommand) -> None:
        await self._deleter.run(command.id)
