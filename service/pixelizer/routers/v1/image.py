from typing import List
from fastapi import APIRouter
from ...schemas.imgae import Image, CertainImage


router = APIRouter()


@router.post('/image')
async def send_image():
    pass


@router.get('/image')
async def get_images() -> List[Image]:
    pass


@router.get('/image/{imageid}')
async def get_image() -> List[CertainImage]:
    pass


@router.get('/user/image/{userid}')
async def get_image_for_user() -> List[Image]:
    pass


@router.delete('/image/{id}')
async def delete_image():
    pass
