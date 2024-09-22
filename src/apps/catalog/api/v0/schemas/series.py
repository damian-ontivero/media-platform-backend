from pydantic import BaseModel
from pydantic import Field


class SerieEpisodeReadSchema(BaseModel):
    id: str = Field(..., description="Serie Episode ID", examples=["123e4567-e89b-12d3-a456-426614174000"])
    number: int = Field(..., description="Serie Episode Number", examples=[1])
    title: str = Field(..., description="Serie Episode Title", examples=["Amazing episode"])
    media_id: str = Field(..., description="Media ID", examples=["123e4567-e89b-12d3-a456-426614174000"])


class SerieEpisodeWriteSchema(BaseModel):
    number: int = Field(..., description="Serie Episode Number", examples=[1])
    title: str = Field(..., description="Serie Episode Title", examples=["Amazing episode"])
    media_id: str = Field(..., description="Media ID", examples=["123e4567-e89b-12d3-a456-426614174000"])


class SerieSeasonReadSchema(BaseModel):
    id: str = Field(..., description="Serie Season ID", examples=["123e4567-e89b-12d3-a456-426614174000"])
    number: int = Field(..., description="Serie Season Number", examples=[1])
    episodes: list[SerieEpisodeReadSchema] = Field(..., description="List of Serie Episode")


class SerieSeasonWriteSchema(BaseModel):
    number: int = Field(..., description="Serie Season Number", examples=[1])
    episodes: list[SerieEpisodeWriteSchema] = Field(..., description="List of Serie Episode")


class SerieReadSchema(BaseModel):
    id: str = Field(..., description="Serie ID", examples=["123e4567-e89b-12d3-a456-426614174000"])
    title: str = Field(..., description="Serie Title", examples=["Amazing serie"])
    seasons: list[SerieSeasonReadSchema] = Field(..., description="List of Serie Season")


class SerieWriteSchema(BaseModel):
    title: str = Field(..., description="Serie Title", examples=["Amazing serie"])
    seasons: list[SerieSeasonWriteSchema] = Field(..., description="List of Serie Season")


class SeriePaginatedResponseSchema(BaseModel):
    page_size: int | None = Field(None, description="Number of items per page", examples=[1])
    page_number: int | None = Field(None, description="Current page number", examples=[1])
    total_pages: int | None = Field(None, description="Total number of pages", examples=[1])
    items: list[SerieReadSchema] = Field(..., description="List of Serie")
