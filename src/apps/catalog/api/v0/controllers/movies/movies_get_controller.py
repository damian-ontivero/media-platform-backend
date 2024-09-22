import base64
import json

from fastapi import Response
from fastapi import status

from apps.catalog.api.v0.schemas.movies import MoviePaginatedResponseSchema
from apps.catalog.api.v0.schemas.movies import MovieReadSchema
from apps.shared.api.v0.controller import Controller
from contexts.catalog.movies.application.services.movie_counter import MovieCounter
from contexts.catalog.movies.application.services.movie_searcher import MovieSearcher


class MoviesGetController(Controller):
    def __init__(self, searcher: MovieSearcher, counter: MovieCounter) -> None:
        self._searcher = searcher
        self._counter = counter

    async def run(self, criteria_in: str | None) -> Response:
        criteria = self._get_criteria(criteria_in)
        movies = self._searcher.run(
            criteria["filter"], criteria["sort"], criteria["page_size"], criteria["page_number"]
        )
        total = self._counter.run()
        response = MoviePaginatedResponseSchema(
            page_size=criteria["page_size"],
            page_number=criteria["page_number"],
            total_pages=total // criteria["page_size"],
            items=[MovieReadSchema(**movie.to_primitives()) for movie in movies],
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
