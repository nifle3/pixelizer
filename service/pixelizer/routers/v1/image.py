from uuid import UUID
from fastapi import APIRouter


router = APIRouter()


@router.post('/image')
async def send_image():
    pass


@router.get('/image')
async def get_images(start: int, end: int):
    pass


@router.get('/image/{image_id}')
async def get_image(image_id: int):
    pass


@router.get('/user/image/{user_id}')
async def get_image_for_user(user_id: UUID, starat: int, end: int):
    pass


@router.delete('/image/{id}')
async def delete_image(id: UUID):
    pass
