from tortoise.models import Model
from tortoise import fields

class UserModel(Model):
    id = fields.IntField(primary_key=True)
    name = fields.CharField(max_length=100)
    email = fields.CharField(max_length=100, unique=True)
    password = fields.TextField()