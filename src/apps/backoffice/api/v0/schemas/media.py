import json

from pydantic import BaseModel
from pydantic import Field
from pydantic import model_validator


class MediaReadSchema(BaseModel):
    id: str = Field(..., description="Media ID", examples=["123e4567-e89b-12d3-a456-426614174000"])
    title: str = Field(..., description="Media Title", examples=["Amazing media"])
    size: int = Field(..., description="Media Size", examples=[120])
    duration: int = Field(..., description="Media Duration", examples=[120])
    path: str = Field(..., description="Media Path", examples=["/path/to/media"])


class MediaWriteSchema(BaseModel):
    title: str = Field(..., description="Media Title", examples=["Amazing media"])

    @model_validator(mode="before")
    @classmethod
    def validate_to_json(cls, value):
        if isinstance(value, str):
            return cls(**json.loads(value))

        return value


class MediaPaginatedResponseSchema(BaseModel):
    page_size: int | None = Field(None, description="Number of items per page", examples=[1])
    page_number: int | None = Field(None, description="Current page number", examples=[1])
    total_pages: int | None = Field(None, description="Total number of pages", examples=[1])
    items: list[MediaReadSchema] = Field(..., description="List of Media")
