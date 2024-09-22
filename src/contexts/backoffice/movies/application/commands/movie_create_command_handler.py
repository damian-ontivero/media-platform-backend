from contexts.backoffice.movies.application.commands.movie_create_command import MovieCreateCommand
from contexts.backoffice.movies.application.services.movie_creator import MovieCreator
from contexts.shared.domain.command_bus.command_handler import CommandHandler


class MovieCreateCommandHandler(CommandHandler[MovieCreateCommand]):
    def __init__(self, creator: MovieCreator) -> None:
        self._creator = creator

    @staticmethod
    def subscribed_to() -> type[MovieCreateCommand]:
        return MovieCreateCommand

    async def handle(self, command: MovieCreateCommand) -> None:
        await self._creator.run(command.title, command.synopsis, command.media_id)
