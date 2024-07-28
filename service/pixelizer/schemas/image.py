from uuid import UUID
from pydantic import BaseModel


class Image(BaseModel):
    id: UUID
    url: str
    user_nickname: str
    user_image_url: str


class CertainImage(Image):
    original_url: str
