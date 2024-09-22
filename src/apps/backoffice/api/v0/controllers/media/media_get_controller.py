from fastapi import Response
from fastapi import status

from apps.backoffice.api.v0.schemas.media import MediaReadSchema
from apps.shared.api.v0.controller import Controller
from contexts.backoffice.shared.media.application.queries.media_find_by_id_query import MediaFindByIdQuery
from contexts.shared.domain.query_bus.query_bus import QueryBus


class MediaGetController(Controller):
    def __init__(self, query_bus: QueryBus) -> None:
        self._query_bus = query_bus

    async def run(self, id: str) -> Response:
        media = await self._query_bus.ask(MediaFindByIdQuery(id))
        response = MediaReadSchema(**media.to_primitives())

        return Response(
            content=response.model_dump_json(), status_code=status.HTTP_200_OK, media_type="application/json"
        )
