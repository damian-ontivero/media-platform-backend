from fastapi import Response
from fastapi import status

from apps.backoffice.api.v0.schemas.movies import MovieWriteSchema
from apps.shared.api.v0.controller import Controller
from contexts.backoffice.movies.application.commands.movie_update_command import MovieUpdateCommand
from contexts.shared.domain.command_bus.command_bus import CommandBus


class MoviePutController(Controller):
    def __init__(self, command_bus: CommandBus) -> None:
        self._command_bus = command_bus

    async def run(self, id: str, movie: MovieWriteSchema) -> Response:
        await self._command_bus.dispatch(MovieUpdateCommand(id, **movie.model_dump()))

        return Response(content=None, status_code=status.HTTP_200_OK, media_type=None)
