from pydantic import BaseModel

class PostsRegistration(BaseModel):
    message: str