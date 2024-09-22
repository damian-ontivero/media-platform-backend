import os

from fastapi import Response
from fastapi import status

from apps.shared.api.v0.controller import Controller
from contexts.backoffice.shared.media.application.queries.media_find_by_id_query import MediaFindByIdQuery
from contexts.shared.domain.query_bus.query_bus import QueryBus


class MediaFileGetController(Controller):
    def __init__(self, query_bus: QueryBus) -> None:
        self._query_bus = query_bus

    async def run(self, id: str, range: str) -> Response:
        media = await self._query_bus.ask(MediaFindByIdQuery(id))
        start, _ = range.replace("bytes=", "").split("-")
        end = int(start) + (1024 * 1024)

        with open(media.path, "rb") as f:
            f.seek(int(start))

            data = f.read(end - int(start))

            return Response(
                content=data,
                status_code=status.HTTP_206_PARTIAL_CONTENT,
                headers={
                    "Content-Range": f"bytes {start}-{end}/{os.path.getsize(media.path)}",
                    "Content-Length": str(len(data)),
                },
            )
