from fastapi import Response
from fastapi import status

from apps.catalog.api.v0.schemas.movies import MovieReadSchema
from apps.shared.api.v0.controller import Controller
from contexts.catalog.movies.application.services.movie_finder import MovieFinder


class MovieGetController(Controller):
    def __init__(self, finder: MovieFinder) -> None:
        self._finder = finder

    async def run(self, id: str) -> Response:
        movie = self._finder.run(id)
        response = MovieReadSchema(**movie.to_primitives())

        return Response(
            content=response.model_dump_json(), status_code=status.HTTP_200_OK, media_type="application/json"
        )
