from fastapi import APIRouter, Request # type: ignore
from src.api.authentication import login_required
# from typing import Annotated

router = APIRouter(
    prefix="/me",
    tags=["me"],
    responses={404: {"description": "Not found"}},
)

@router.get('/')
@login_required
async def my_informations(request: Request):
    return {'logged': 'zz'}

# current_user: Annotated[UserModel, Depends(verify_token)]
