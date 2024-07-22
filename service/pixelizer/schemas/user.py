from uuid import UUID
from pydantic import BaseModel, EmailStr, Base64Str


class AddedUser(BaseModel):
    email: EmailStr
    nickname: str
    password: str
    photo: Base64Str


class GetedShortUser(BaseModel):
    id: UUID
    nickname: str
    photo_link: str


class GetedUser(GetedShortUser):
    email: EmailStr
    description: str
