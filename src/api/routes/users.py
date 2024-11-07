from fastapi import APIRouter
from src.api.dtos.users import *
from src.datalayer.models.user import *
from src.api.exception.user import *

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)

@router.post('/register')
async def register(body: UserRegistrations):

    email_exists = await UserModel.filter(email=body.email)
    if email_exists:
        raise email_already_exists()

    user = await UserModel.create(
        name = body.name,
        email = body.email,
        password = body.password
    )
    return {'created': user}

@router.post('/login')
async def login(body: UserLogin):
    user = None

    try: 
        user = await UserModel.get(email=body.email)
    except Exception as e:
        raise login_wrong_exception()

    if user.password != body.password:
        raise login_wrong_exception()
    
    return {'sucess': user}

@router.get('/get-users')
async def get_users():
    user = await UserModel.all()
    return {'users': user}

