from tortoise.models import Model
from tortoise import fields
import secrets


def generate_token():
    return secrets.token_urlsafe(20)

class UserModel(Model):
    id = fields.IntField(primary_key=True)
    name = fields.CharField(max_length=100)
    email = fields.CharField(max_length=100, unique=True)
    password = fields.TextField()
    token = fields.TextField(default=generate_token)