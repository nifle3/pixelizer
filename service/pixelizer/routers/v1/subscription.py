from typing import Any
from fastapi import APIRouter


router = APIRouter()


@router.post('/subscribtion')
async def subscribtion() -> Any:
    raise NotImplementedError()


@router.get('/subscribtion')
async def get_all_subscribtion() -> Any:
    raise NotImplementedError()


@router.patch('/subscribtion')
async def delete_subscribtion() -> Any:
    raise NotImplementedError()


@router.get('/subscribtion/unconfirmed')
async def get_unconfirmed_subscribtions() -> Any:
    raise NotImplementedError()
