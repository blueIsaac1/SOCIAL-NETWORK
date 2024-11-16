from fastapi import HTTPException # type: ignore
from src.datalayer.models.user import UserModel
from functools import wraps

async def verify_token(token: str):
    user = await get_user_by_token(token)
    print("User: ", user)
    if not user:
        raise HTTPException(status_code=401, detail="Não Autorizado")
    if not token:
        raise HTTPException(status_code=401, detail="Token não fornecido")
    return user
    
async def get_user_by_token(token):
    try:
        print('token', token)
        user = await UserModel.get(token=token)
        return user
    except Exception as e:
        print('fail: ', e)
        return False
    
def login_required(callback):
    @wraps(callback)
    async def wrapper(*args, **kwargs):
        request = kwargs['request']
        token = request.headers.get('Authorization', False)
        user = await verify_token(token)
        kwargs['request'].current_user = user
        return await callback(*args, **kwargs)
    return wrapper
