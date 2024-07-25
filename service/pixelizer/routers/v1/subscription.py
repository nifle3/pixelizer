from fastapi import APIRouter


router = APIRouter()


@router.post('/v1/subscribtion')
async def subscribtion():
    pass


@router.get('/v1/subscribtion')
async def get_all_subscribtion():
    pass


@router.patch('/v1/subscribtion')
async def delete_subscribtion():
    pass


@router.get('/v1/subscribtion/unconfirmed')
async def get_unconfirmed_subscribtions():
    pass
