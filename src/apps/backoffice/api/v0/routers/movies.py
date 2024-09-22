from fastapi import APIRouter
from fastapi import Path
from fastapi import Query
from fastapi import status
from typing_extensions import Annotated

from apps.backoffice.api.v0.controllers.movies.movie_delete_controller import MovieDeleteController
from apps.backoffice.api.v0.controllers.movies.movie_get_controller import MovieGetController
from apps.backoffice.api.v0.controllers.movies.movie_post_controller import MoviePostController
from apps.backoffice.api.v0.controllers.movies.movie_put_controller import MoviePutController
from apps.backoffice.api.v0.controllers.movies.movies_get_controller import MoviesGetController
from apps.backoffice.api.v0.dependecy_injection import container
from apps.backoffice.api.v0.schemas.movies import MoviePaginatedResponseSchema
from apps.backoffice.api.v0.schemas.movies import MovieReadSchema
from apps.backoffice.api.v0.schemas.movies import MovieWriteSchema


router = APIRouter(prefix="/movies", tags=["Movies"])


@router.get("", response_model=MoviePaginatedResponseSchema, status_code=status.HTTP_200_OK, description="Search Movie")
async def search(
    criteria: Annotated[
        str | None,
        Query(
            ...,
            description="""
    The criteria must be a base64-encoded JSON string with the following structure:
    {
        "filter": {
            "conjunction": "AND",
            "conditions": [
                {
                    "field": "title",
                    "operator": "CONTAINS",
                    "value": "Amazing"
                }
            ]
        },
        "sort": [
            {
                "field": "title",
                "direction": "ASC"
            }
        ],
        "page_size": 10,
        "page_number": 1
    }
            """,
            example="ewogICAgICAgICJmaWx0ZXIiOiB7CiAgICAgICAgICAgICJjb25qdW5jdGlvbiI6ICJBTkQiLAogICAgICAgICAgICAiY29uZGl0aW9ucyI6IFsKICAgICAgICAgICAgICAgIHsKICAgICAgICAgICAgICAgICAgICAiZmllbGQiOiAidGl0bGUiLAogICAgICAgICAgICAgICAgICAgICJvcGVyYXRvciI6ICJDT05UQUlOUyIsCiAgICAgICAgICAgICAgICAgICAgInZhbHVlIjogIkFtYXppbmciCiAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgIF0KICAgICAgICB9LAogICAgICAgICJzb3J0IjogWwogICAgICAgICAgICB7CiAgICAgICAgICAgICAgICAiZmllbGQiOiAidGl0bGUiLAogICAgICAgICAgICAgICAgImRpcmVjdGlvbiI6ICJBU0MiCiAgICAgICAgICAgIH0KICAgICAgICBdLAogICAgICAgICJwYWdlX3NpemUiOiAxMCwKICAgICAgICAicGFnZV9udW1iZXIiOiAxCiAgICB9",
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


@router.post("", status_code=status.HTTP_201_CREATED, description="Create Movie")
async def create(movie: MovieWriteSchema):
    controller: MoviePostController = container.find("MoviePostController")

    return await controller.run(movie)


@router.put("/{id}", status_code=status.HTTP_200_OK, description="Update Movie")
async def update(
    id: Annotated[str, Path(..., description="Id of the Movie", example="123e4567-e89b-12d3-a456-426614174000")],
    movie: MovieWriteSchema,
):
    controller: MoviePutController = container.find("MoviePutController")

    return await controller.run(id, movie)


@router.delete("/{id}", status_code=status.HTTP_200_OK, description="Delete Movie")
async def delete(
    id: Annotated[str, Path(..., description="Id of the Movie", example="123e4567-e89b-12d3-a456-426614174000")],
):
    controller: MovieDeleteController = container.find("MovieDeleteController")

    return await controller.run(id)
