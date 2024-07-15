from uuid import UUID
from pydantic import BaseModel


class AddedUser(BaseModel):
    email: str
    password: str
    nickname: str


class GetedUser(AddedUser):
    id: UUID
    link_to_profile_picture: str
