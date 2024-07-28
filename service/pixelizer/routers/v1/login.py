from typing import Any
from fastapi import APIRouter
from ...schemas.user import RegistrationUser, LoginUser


router = APIRouter()


@router.post('/create', response_model=Any)
async def create(user: RegistrationUser) -> Any:
    raise NotImplementedError()


@router.post('/login', response_model=Any)
async def login(user: LoginUser) -> Any:
    raise NotImplementedError()


@router.head('/logout', response_model=Any)
async def logout() -> Any:
    raise NotImplementedError()
