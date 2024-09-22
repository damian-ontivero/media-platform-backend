from contexts.backoffice.movies.application.commands.movie_update_command import MovieUpdateCommand
from contexts.backoffice.movies.application.services.movie_updater import MovieUpdater
from contexts.shared.domain.command_bus.command_handler import CommandHandler


class MovieUpdateCommandHandler(CommandHandler[MovieUpdateCommand]):
    def __init__(self, updater: MovieUpdater) -> None:
        self._updater = updater

    @staticmethod
    def subscribed_to() -> type[MovieUpdateCommand]:
        return MovieUpdateCommand

    async def handle(self, command: MovieUpdateCommand) -> None:
        await self._updater.run(command.id, command.title, command.synopsis, command.media_id)
