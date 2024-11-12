# from dataclasses import dataclass

from src.api.exception.user import email_already_exists, login_wrong_exception

class UserService:
    def __init__(self):
        pass
    
    async def register(self, name:str, email:str, password:str):
        email_exists = await UserModel.filter(email = email)
        if email_exists:
            raise email_already_exists()
        user = await UserModel.create(
            name = name,
            email = email,
            password = password
        )
        return user
    
    async def login(self, email: str, password:str):
        try: 
            user = await UserModel.get(email=email)
        except Exception:
            raise login_wrong_exception()

        if user.password != password:
            raise login_wrong_exception()