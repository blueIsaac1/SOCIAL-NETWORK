from fastapi import APIRouter, Depends # type: ignore
from src.api.dtos.users import UserRegistrations, UserLogin
from src.services.user import UserService
from typing import Annotated

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)

@router.post('/register')
async def register(body: UserRegistrations, service: Annotated[UserService, Depends(UserService)]):
    
    register_user = await service.register(
        name = body.name, 
        email = body.email, 
        password = body.password)
    
    return {'created': register_user}

@router.post('/login')
async def login(body: UserLogin, service: Annotated[UserService, Depends(UserService)]):

    login_user = await service.login(
        email = body.email,
        password = body.password
    )
    print(body.email, body.password)

    return {'zz': login_user}

@router.get('/get-users')
async def get_all_users(service: Annotated[UserService, Depends(UserService)]):
    return await service.get_all_users()

