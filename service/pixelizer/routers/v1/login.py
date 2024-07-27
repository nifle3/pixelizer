from fastapi import APIRouter


router = APIRouter()


@router.post('/create')
async def create():
    pass


@router.post('/login')
async def login():
    pass


@router.head('/logout')
async def logout():
    pass
