from fastapi import APIRouter
from fastapi import Path
from fastapi import Query
from fastapi import status
from typing_extensions import Annotated

from apps.backoffice.api.v0.controllers.series.serie_delete_controller import SerieDeleteController
from apps.backoffice.api.v0.controllers.series.serie_get_controller import SerieGetController
from apps.backoffice.api.v0.controllers.series.serie_post_controller import SeriePostController
from apps.backoffice.api.v0.controllers.series.serie_put_controller import SeriePutController
from apps.backoffice.api.v0.controllers.series.series_get_controller import SeriesGetController
from apps.backoffice.api.v0.dependecy_injection import container
from apps.backoffice.api.v0.schemas.series import SeriePaginatedResponseSchema
from apps.backoffice.api.v0.schemas.series import SerieReadSchema
from apps.backoffice.api.v0.schemas.series import SerieWriteSchema


router = APIRouter(prefix="/series", tags=["Series"])


@router.get("", response_model=SeriePaginatedResponseSchema, status_code=status.HTTP_200_OK, description="Search Serie")
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
    controller: SeriesGetController = container.find("SeriesGetController")

    return await controller.run(criteria)


@router.get("/{id}", response_model=SerieReadSchema, status_code=status.HTTP_200_OK, description="Find Serie")
async def find(
    id: Annotated[str, Path(..., description="Id of the Serie", example="123e4567-e89b-12d3-a456-426614174000")],
):
    controller: SerieGetController = container.find("SerieGetController")

    return await controller.run(id)


@router.post("", status_code=status.HTTP_201_CREATED, description="Create Serie")
async def create(serie: SerieWriteSchema):
    controller: SeriePostController = container.find("SeriePostController")

    return await controller.run(serie)


@router.put("/{id}", status_code=status.HTTP_200_OK, description="Update Serie")
async def update(
    id: Annotated[str, Path(..., description="Id of the Serie", example="123e4567-e89b-12d3-a456-426614174000")],
    serie: SerieWriteSchema,
):
    controller: SeriePutController = container.find("SeriePutController")

    return await controller.run(id, serie)


@router.delete("/{id}", status_code=status.HTTP_200_OK, description="Delete Serie")
async def delete(
    id: Annotated[str, Path(..., description="Id of the Serie", example="123e4567-e89b-12d3-a456-426614174000")],
):
    controller: SerieDeleteController = container.find("SerieDeleteController")

    return await controller.run(id)
