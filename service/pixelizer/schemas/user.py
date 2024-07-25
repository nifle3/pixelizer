from uuid import UUID
from typing import Optional, List
from pydantic import BaseModel, EmailStr


class RegistrationUser(BaseModel):
    nickname: str
    email: EmailStr
    password: str


class LoginUser(BaseModel):
    email: EmailStr
    password: str


class ShortUser(BaseModel):
    id: UUID
    nickname: str
    url_image: Optional[str]
    description: str


class User(ShortUser):
    email: Optional[EmailStr]
    friends: Optional[List[ShortUser]]
