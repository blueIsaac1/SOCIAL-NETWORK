from fastapi import APIRouter, Depends # type: ignore
from src.api.dtos.posts import PostsRegistration
from typing import Annotated
from src.services.post import *
from src.api.authentication import verify_token


router = APIRouter(
    prefix="/posts",
    tags=["posts"],
    responses={404: {"description": "Not found"}},
)

@router.post('/create')
async def create_post(body: PostsRegistration, 
    current_user: Annotated[UserModel, Depends(verify_token)], 
    service: Annotated[PostService, Depends(PostService)]):
    
    post = await service.create_post(user=current_user, message=body.message)

    return {'post': post}

@router.get('/get-posts')
async def get_all_posts(service: Annotated[PostService, Depends(PostService)]):
    return await service.get_all_posts()


@router.get('/{user_id}')
async def get_posts_by_user(user_id: int, service: Annotated[PostService, Depends(PostService)]):
    return await service.get_users_posts(user_id)



