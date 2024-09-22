from fastapi import Response
from fastapi import UploadFile
from fastapi import status

from apps.backoffice.api.v0.schemas.media import MediaWriteSchema
from apps.shared.api.v0.controller import Controller
from contexts.backoffice.media.application.commands.media_update_command import MediaUpdateCommand
from contexts.shared.domain.command_bus.command_bus import CommandBus


class MediaPutController(Controller):
    def __init__(self, command_bus: CommandBus) -> None:
        self._command_bus = command_bus

    async def run(self, id: str, media: MediaWriteSchema, file: UploadFile) -> Response:
        command = MediaUpdateCommand(id, media.title, file.filename, await file.read())

        await self._command_bus.dispatch(command)

        return Response(content=None, status_code=status.HTTP_200_OK, media_type=None)
