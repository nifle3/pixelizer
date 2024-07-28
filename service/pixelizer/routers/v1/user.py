from typing import List, Any
from uuid import UUID
from fastapi import APIRouter
from ...schemas.user import ShortUser, User


router = APIRouter()


@router.get('/v1/user/me', response_model=User)
async def get_me() -> Any:
    raise NotImplementedError()


@router.get('/v1/user/{user_id}', response_model=User)
async def get_another_user(user_id: UUID) -> Any:
    raise NotImplementedError()


@router.patch('/v1/user')
async def update_me() -> Any:
    raise NotImplementedError()


@router.patch('/v1/user/image')
async def update_me_image() -> Any:
    raise NotImplementedError()


@router.delete('/v1/user')
async def delete_me() -> Any:
    raise NotImplementedError()


@router.get('/v1/user/search/{name}', response_model=List[ShortUser])
async def search_user(name: str) -> Any:
    raise NotImplementedError()
