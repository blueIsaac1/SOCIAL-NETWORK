from src.datalayer.models.user import UserModel
from src.datalayer.models.posts import PostModel

class PostService:
    def __init__(self):
        pass

    async def create_post(self, user: UserModel, message:str):
        post = await PostModel.create(
        user = user,
        message = message
        )
        return {'created': post}
    
    async def get_all_posts(self):
        return await PostModel.all().order_by('-created_at')
    
    async def get_users_posts(self, user_id):
        return await PostModel.filter(user_id=user_id)
