from uuid import UUID
from fastapi import APIRouter


router = APIRouter()


@router.get('/v1/user/me')
async def get_me():
    pass


@router.get('/v1/user/{user_id}')
async def get_another_user(user_id: UUID):
    pass


@router.patch('/v1/user')
async def update_me():
    pass


@router.patch('/v1/user/image')
async def update_me_image():
    pass


@router.delete('/v1/user')
async def delete_me():
    pass


@router.get('/v1/user/search/{name}')
async def search_user(name: str):
    pass
