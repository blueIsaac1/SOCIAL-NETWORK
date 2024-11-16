from fastapi import APIRouter, Depends, Request # type: ignore
from src.api.dtos.posts import PostsRegistration
from typing import Annotated
from src.services.post import *
from src.api.authentication import login_required


router = APIRouter(
    prefix="/posts",
    tags=["posts"],
    responses={404: {"description": "Not found"}},
)

@router.post('/create')
@login_required
async def create_post(
    body: PostsRegistration,
    service: Annotated[PostService, Depends(PostService)],
    request: Request
):
    
    post = await service.create_post(user=request.current_user, message=body.message)

    return {'post': post}

@router.get('/get-posts')
async def get_all_posts(service: Annotated[PostService, Depends(PostService)]):
    return await service.get_all_posts()


@router.get('/{user_id}')
async def get_posts_by_user(user_id: int, service: Annotated[PostService, Depends(PostService)]):
    return await service.get_users_posts(user_id)



