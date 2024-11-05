from pydantic import BaseModel

class UserRegistrations(BaseModel):
    name: str
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str