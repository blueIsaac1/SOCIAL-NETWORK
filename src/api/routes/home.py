from fastapi import APIRouter, Depends
from src.api.dtos.users import *
from src.datalayer.models.user import *
from src.api.exception.user import *
from typing import Annotated
from src.api.authentication import *

router = APIRouter(
    prefix="/me",
    tags=["me"],
    responses={404: {"description": "Not found"}},
)

@router.post('/')
async def my_informations(current_user: Annotated[UserModel, Depends(verify_token)]):
    print('current_user: ', current_user)
    return {'logado': f'Olá {current_user.name} zz'}
