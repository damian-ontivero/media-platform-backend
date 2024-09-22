from fastapi import Response
from fastapi import status

from apps.shared.api.v0.controller import Controller
from contexts.backoffice.media.application.commands.media_delete_command import MediaDeleteCommand
from contexts.shared.domain.command_bus.command_bus import CommandBus


class MediaDeleteController(Controller):
    def __init__(self, command_bus: CommandBus) -> None:
        self._command_bus = command_bus

    async def run(self, id: str) -> Response:
        await self._command_bus.dispatch(MediaDeleteCommand(id))

        return Response(content=None, status_code=status.HTTP_200_OK, media_type=None)
