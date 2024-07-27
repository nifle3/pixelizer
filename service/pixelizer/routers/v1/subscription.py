from fastapi import APIRouter


router = APIRouter()


@router.post('/subscribtion')
async def subscribtion():
    pass


@router.get('/subscribtion')
async def get_all_subscribtion():
    pass


@router.patch('/subscribtion')
async def delete_subscribtion():
    pass


@router.get('/subscribtion/unconfirmed')
async def get_unconfirmed_subscribtions():
    pass
