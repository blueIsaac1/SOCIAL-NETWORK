from fastapi import APIRouter, Depends
from src.api.dtos.posts import PostsRegistration
from src.datalayer.models.posts import PostModel
from src.datalayer.models.user import UserModel
from typing import Annotated
from src.api.authentication import verify_token

router = APIRouter(
    prefix="/posts",
    tags=["posts"],
    responses={404: {"description": "Not found"}},
)

@router.post('/create')
async def create_post(body: PostsRegistration, current_user: Annotated[UserModel, Depends(verify_token)]):

    post = await PostModel.create(
        user = current_user,
        message = body.message
    )
    return {'created': post}

@router.get('/get-posts')
async def get_posts():
    posts = await PostModel.all()
    return {'posts': posts}


@router.get('/{user_id}')
async def get_posts_by_user(user_id: int):
    post_by_user = await PostModel.filter(user_id=user_id)
    return {'posts by this user': post_by_user}



