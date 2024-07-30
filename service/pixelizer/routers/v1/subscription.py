from typing import Any, Annotated
from fastapi import APIRouter, status, Depends
from .utils.params import Paginator


router = APIRouter()


@router.post('/subscribtion', status_code=status.HTTP_201_CREATED)
async def subscribtion() -> Any:
    raise NotImplementedError()


@router.get('/subscribtion')
async def get_all_subscribtion(pagintaion: Annotated[
                                                    Paginator,
                                                    Depends()
                                                     ] = ...) -> Any:
    raise NotImplementedError()


@router.delete('/subscribtion', status_code=status.HTTP_204_NO_CONTENT)
async def delete_subscribtion() -> Any:
    raise NotImplementedError()

