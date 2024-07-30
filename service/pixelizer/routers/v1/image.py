from typing import Annotated, List, Any
from uuid import UUID
from fastapi import APIRouter, UploadFile, Depends
from .utils.params import Paginator
from ...schemas.image import CertainImage, Image

router = APIRouter()


@router.post('/image')
async def send_image(file: UploadFile) -> Any:
    raise NotImplementedError()


@router.get('/image', response_model=List[Image])
async def get_images(pagination: Annotated[Paginator, Depends()] = ...) -> Any:
    return {"skip": pagination.skip, "limit": pagination.limit}


@router.get('/image/{image_id}', response_model=CertainImage)
async def get_image(image_id: UUID) -> Any:
    raise NotImplementedError()


@router.get('/user/image/{user_id}', response_model=List[Image])
async def get_image_for_user(
        user_id: UUID,
        pagintaion: Annotated[Paginator, Depends()] = ...
        ) -> Any:
    raise NotImplementedError()


@router.delete('/image/{id}')
async def delete_image(id: UUID) -> Any:
    raise NotImplementedError()
