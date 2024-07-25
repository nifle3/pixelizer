from fastapi import APIRouter


router = APIRouter()


@router.post('/image')
async def send_image():
    pass


@router.get('/image')
async def get_images():
    pass


@router.get('/image/{userid}')
async def get_image_for_user():
    pass


@router.delete('/image/{id}')
async def delete_image():
    pass
