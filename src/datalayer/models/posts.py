from tortoise.models import Model
from tortoise import fields
from src.datalayer.models.user import UserModel

class PostModel(Model):
    id = fields.IntField(primary_key=True)
    message = fields.TextField()
    user = fields.ForeignKeyField('models.UserModel', related_name='posts')
    
    