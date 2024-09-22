from fastapi import Response
from fastapi import status

from apps.catalog.api.v0.schemas.series import SerieReadSchema
from apps.shared.api.v0.controller import Controller
from contexts.catalog.series.application.services.serie_finder import SerieFinder


class SerieGetController(Controller):
    def __init__(self, finder: SerieFinder) -> None:
        self._finder = finder

    async def run(self, id: str) -> Response:
        serie = self._finder.run(id)
        response = SerieReadSchema(**serie.to_primitives())

        return Response(
            content=response.model_dump_json(), status_code=status.HTTP_200_OK, media_type="application/json"
        )
