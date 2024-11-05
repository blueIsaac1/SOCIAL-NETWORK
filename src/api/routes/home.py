from fastapi import APIRouter
from src.api.dtos.users import *
from src.datalayer.models.user import *
from src.api.exception.user import *

router = APIRouter(
    prefix="/me",
    tags=["me"],
    responses={404: {"description": "Not found"}},
)

@router.post('/')
async def my_informations(n):

    return {'logado': 'zz'}
