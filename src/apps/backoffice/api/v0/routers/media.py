from fastapi import APIRouter
from fastapi import Body
from fastapi import File
from fastapi import Header
from fastapi import Path
from fastapi import Query
from fastapi import UploadFile
from fastapi import status
from typing_extensions import Annotated

from apps.backoffice.api.v0.controllers.media.media_delete_controller import MediaDeleteController
from apps.backoffice.api.v0.controllers.media.media_file_get_controller import MediaFileGetController
from apps.backoffice.api.v0.controllers.media.media_get_controller import MediaGetController
from apps.backoffice.api.v0.controllers.media.media_post_controller import MediaPostController
from apps.backoffice.api.v0.controllers.media.media_put_controller import MediaPutController
from apps.backoffice.api.v0.controllers.media.medias_get_controller import MediasGetController
from apps.backoffice.api.v0.dependecy_injection import container
from apps.backoffice.api.v0.schemas.media import MediaPaginatedResponseSchema
from apps.backoffice.api.v0.schemas.media import MediaReadSchema
from apps.backoffice.api.v0.schemas.media import MediaWriteSchema


router = APIRouter(prefix="/media", tags=["Media"])


@router.get("", response_model=MediaPaginatedResponseSchema, status_code=status.HTTP_200_OK, description="Search Media")
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
    controller: MediasGetController = container.find("MediasGetController")

    return await controller.run(criteria)


@router.get("/{id}", response_model=MediaReadSchema, status_code=status.HTTP_200_OK, description="Find Media")
async def find(
    id: Annotated[str, Path(..., description="Id of the Media", example="123e4567-e89b-12d3-a456-426614174000")],
):
    controller: MediaGetController = container.find("MediaGetController")

    return await controller.run(id)


@router.post("", status_code=status.HTTP_201_CREATED, description="Create Media")
async def create(media: MediaWriteSchema = Body(...), file: UploadFile = File(...)):
    controller: MediaPostController = container.find("MediaPostController")

    return await controller.run(media, file)


@router.put("/{id}", status_code=status.HTTP_200_OK, description="Update Media")
async def update(
    id: Annotated[str, Path(..., description="Id of the Media", example="123e4567-e89b-12d3-a456-426614174000")],
    media: MediaWriteSchema = Body(...),
    file: UploadFile = File(...),
):
    controller: MediaPutController = container.find("MediaPutController")

    return await controller.run(id, media, file)


@router.delete("/{id}", status_code=status.HTTP_200_OK, description="Delete Media")
async def delete(
    id: Annotated[str, Path(..., description="Id of the Media", example="123e4567-e89b-12d3-a456-426614174000")],
):
    controller: MediaDeleteController = container.find("MediaDeleteController")

    return await controller.run(id)


@router.get("/{id}/file", status_code=status.HTTP_200_OK, description="Find Media File")
async def get_stream(
    id: Annotated[str, Path(..., description="Id of the Media", example="123e4567-e89b-12d3-a456-426614174000")],
    range: Annotated[str, Header(..., description="Range", example="bytes=0-100")],
):
    controller: MediaFileGetController = container.find("MediaFileGetController")

    return await controller.run(id, range)
