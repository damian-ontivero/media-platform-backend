from fastapi import Response
from fastapi import status

from apps.shared.api.v0.controller import Controller
from contexts.backoffice.series.application.commands.serie_delete_command import SerieDeleteCommand
from contexts.shared.domain.command_bus.command_bus import CommandBus


class SerieDeleteController(Controller):
    def __init__(self, command_bus: CommandBus) -> None:
        self._command_bus = command_bus

    async def run(self, id: str) -> Response:
        await self._command_bus.dispatch(SerieDeleteCommand(id))

        return Response(content=None, status_code=status.HTTP_200_OK, media_type=None)
