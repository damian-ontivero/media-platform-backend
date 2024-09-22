from fastapi import Request
from fastapi import Response
from fastapi import status

from apps.shared.api.v0.controller import Controller


class HealthCheckController(Controller):
    async def run(self, request: Request | None) -> Response:
        return Response(
            content="The Media Platform API is running.", status_code=status.HTTP_200_OK, media_type="text/plain"
        )
