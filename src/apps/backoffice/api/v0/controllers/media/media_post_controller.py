from fastapi import Response
from fastapi import UploadFile
from fastapi import status

from apps.backoffice.api.v0.schemas.media import MediaWriteSchema
from apps.shared.api.v0.controller import Controller
from contexts.backoffice.media.application.commands.media_create_command import MediaCreateCommand
from contexts.shared.domain.command_bus.command_bus import CommandBus


class MediaPostController(Controller):
    def __init__(self, command_bus: CommandBus) -> None:
        self._command_bus = command_bus

    async def run(self, media: MediaWriteSchema, file: UploadFile) -> Response:
        command = MediaCreateCommand(media.title, file.filename, await file.read())

        await self._command_bus.dispatch(command)

        return Response(content=None, status_code=status.HTTP_201_CREATED, media_type=None)
