import base64
import json

from fastapi import Response
from fastapi import status

from apps.catalog.api.v0.schemas.series import SeriePaginatedResponseSchema
from apps.catalog.api.v0.schemas.series import SerieReadSchema
from apps.shared.api.v0.controller import Controller
from contexts.catalog.series.application.services.serie_counter import SerieCounter
from contexts.catalog.series.application.services.serie_searcher import SerieSearcher


class SeriesGetController(Controller):
    def __init__(self, searcher: SerieSearcher, counter: SerieCounter) -> None:
        self._searcher = searcher
        self._counter = counter

    async def run(self, criteria_in: str | None) -> Response:
        criteria = self._get_criteria(criteria_in)
        series = self._searcher.run(
            criteria["filter"], criteria["sort"], criteria["page_size"], criteria["page_number"]
        )
        total = self._counter.run()
        response = SeriePaginatedResponseSchema(
            page_size=criteria["page_size"],
            page_number=criteria["page_number"],
            total_pages=total // criteria["page_size"],
            items=[SerieReadSchema(**serie.to_primitives()) for serie in series],
        )

        return Response(
            content=response.model_dump_json(), status_code=status.HTTP_200_OK, media_type="application/json"
        )

    def _get_criteria(self, criteria_in: str | None) -> dict:
        if criteria_in is None:
            criteria = self._get_default_criteria()

            return json.loads(base64.b64decode(criteria).decode())
        else:
            return json.loads(base64.b64decode(criteria_in).decode())

    def _get_default_criteria(self) -> str:
        criteria = {"filter": {}, "sort": [], "page_size": 10, "page_number": 1}

        return base64.b64encode(json.dumps(criteria).encode()).decode()
