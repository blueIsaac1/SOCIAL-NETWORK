from fastapi import APIRouter, Depends
from src.datalayer.models.user import UserModel
from src.api.authentication import verify_token
from typing import Annotated


router = APIRouter(
    prefix="/me",
    tags=["me"],
    responses={404: {"description": "Not found"}},
)

@router.post('/')
async def my_informations(current_user: Annotated[UserModel, Depends(verify_token)]):
    print('current_user: ', current_user)
    return {'logado': f'Olá {current_user.name} zz'}
