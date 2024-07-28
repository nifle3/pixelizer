from typing import Annotated, List, Any
from uuid import UUID
from fastapi import APIRouter, Query
from ...schemas.image import CertainImage, Image

router = APIRouter()


@router.post('/image')
async def send_image() -> Any:
    raise NotImplementedError()


@router.get('/image', response_model=List[Image])
async def get_images(skip: Annotated[int | None, Query(ge=0)] = None,
                     limit: Annotated[int | None, Query(ge=1)] = None) -> Any:
    return {"skip": skip, "limit": limit}


@router.get('/image/{image_id}', response_model=CertainImage)
async def get_image(image_id: UUID) -> Any:
    raise NotImplementedError()


@router.get('/user/image/{user_id}', response_model=List[Image])
async def get_image_for_user(
        user_id: UUID,
        skip: int = Query(0, ge=0),
        limit: int = Query(1, ge=1)
        ) -> Any:
    raise NotImplementedError()


@router.delete('/image/{id}')
async def delete_image(id: UUID) -> Any:
    raise NotImplementedError()
