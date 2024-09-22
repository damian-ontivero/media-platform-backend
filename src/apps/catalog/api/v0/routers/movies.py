from fastapi import APIRouter
from fastapi import Path
from fastapi import Query
from fastapi import status
from typing_extensions import Annotated

from apps.catalog.api.v0.controllers.movies.movie_get_controller import MovieGetController
from apps.catalog.api.v0.controllers.movies.movies_get_controller import MoviesGetController
from apps.catalog.api.v0.dependecy_injection import container
from apps.catalog.api.v0.schemas.movies import MoviePaginatedResponseSchema
from apps.catalog.api.v0.schemas.movies import MovieReadSchema


router = APIRouter(prefix="/movies", tags=["Movies"])


@router.get("", response_model=MoviePaginatedResponseSchema, status_code=status.HTTP_200_OK, description="Search Movie")
async def search(
    criteria: Annotated[
        str | None,
        Query(
            ...,
            description="""
    The criteria must be a base64 encoded *INLINE* JSON string with the following structure:

    {
        "filter": {
        "conjunction": "AND",
        "conditions": [
            {
                "field": "channel_id",
                "operator": "CONTAINS",
                "value": "1"
            }
            ]
        },
        "sort": [
            {
            "field": "rating",
            "direction": "ASC"
            }
        ],
        "page_size": 15,
        "page_number": 1
    }

            """,
            example="eyJmaWx0ZXIiOnsiY29uanVuY3Rpb24iOiJBTkQiLCJjb25kaXRpb25zIjpbeyJmaWVsZCI6ImNoYW5uZWxfaWQiLCJvcGVyYXRvciI6IkNPTlRBSU5TIiwidmFsdWUiOiIxIn1dfSwic29ydCI6W3siZmllbGQiOiJyYXRpbmciLCJkaXJlY3Rpb24iOiJBU0MifV0sInBhZ2Vfc2l6ZSI6MTUsInBhZ2VfbnVtYmVyIjoxfQ==",
        ),
    ] = None,
):
    controller: MoviesGetController = container.find("MoviesGetController")

    return await controller.run(criteria)


@router.get("/{id}", response_model=MovieReadSchema, status_code=status.HTTP_200_OK, description="Find Movie")
async def find(
    id: Annotated[str, Path(..., description="Id of the Movie", example="123e4567-e89b-12d3-a456-426614174000")],
):
    controller: MovieGetController = container.find("MovieGetController")

    return await controller.run(id)
