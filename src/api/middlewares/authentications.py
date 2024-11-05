import time
from dev import app
from fastapi import FastAPI, Request


def auth_middleware(app: FastAPI):
    @app.middleware("http")
    async def authentication(request: Request, call_next):
        user_token = response.headers.get('Authorization', False)
        # id 
        response = await call_next(request)
        return response
