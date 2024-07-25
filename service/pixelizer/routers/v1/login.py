from fastapi import APIRouter


router = APIRouter()


@router.post('/v1/create')
async def create():
    pass


@router.post('/v1/login')
async def login():
    pass


@router.head('/v1/logout')
async def logout():
    pass
