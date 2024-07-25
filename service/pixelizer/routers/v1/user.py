from fastapi import APIRouter


router = APIRouter()


@router.get('/user')
async def get_me():
    pass


@router.get('/v1/user/{userid}')
async def get_another_user():
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


@router.get('/v1/user/search')
async def search_user():
    pass
