import base64
import json

from fastapi import Response
from fastapi import status

from apps.backoffice.api.v0.schemas.movies import MoviePaginatedResponseSchema
from apps.shared.api.v0.controller import Controller
from contexts.backoffice.movies.application.queries.movie_count_query import MovieCountQuery
from contexts.backoffice.movies.application.queries.movie_search_by_criteria_query import MovieSearchByCriteriaQuery
from contexts.shared.domain.query_bus.query_bus import QueryBus


class MoviesGetController(Controller):
    def __init__(self, query_bus: QueryBus) -> None:
        self._query_bus = query_bus

    async def run(self, criteria_in: str | None) -> Response:
        criteria = self._get_criteria(criteria_in)
        movies = await self._query_bus.ask(MovieSearchByCriteriaQuery(**criteria))
        total = await self._query_bus.ask(MovieCountQuery())
        response = MoviePaginatedResponseSchema(
            page_size=criteria["page_size"],
            page_number=criteria["page_number"],
            total_pages=total // criteria["page_size"],
            items=[movie.to_primitives() for movie in movies],
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
