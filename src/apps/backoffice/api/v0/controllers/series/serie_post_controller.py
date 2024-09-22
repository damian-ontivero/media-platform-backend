from fastapi import Response
from fastapi import status

from apps.backoffice.api.v0.schemas.series import SerieWriteSchema
from apps.shared.api.v0.controller import Controller
from contexts.backoffice.series.application.commands.serie_create_command import SerieCreateCommand
from contexts.shared.domain.command_bus.command_bus import CommandBus


class SeriePostController(Controller):
    def __init__(self, command_bus: CommandBus) -> None:
        self._command_bus = command_bus

    async def run(self, serie: SerieWriteSchema) -> Response:
        await self._command_bus.dispatch(SerieCreateCommand(**serie.model_dump()))

        return Response(content=None, status_code=status.HTTP_201_CREATED, media_type=None)
