from tortoise.contrib.fastapi import register_tortoise
from fastapi import FastAPI
from src.api.routes import users, home, posts
from fastapi.middleware.cors import CORSMiddleware

def configure_routes(app: FastAPI):
    app.include_router(users.router)
    app.include_router(home.router),
    app.include_router(posts.router)

def configure_db(app: FastAPI):
    register_tortoise(
        app = app,
        # db_url = "sqlite://db.sqlite3",
        modules = {"models": [
            "src.datalayer.models.user",
            
            ]},
        # db_url = "postgres://postgres:qwerty123@localhost:5432/events"
        config = {
            "connections": {
                # "default": "postgres://postgres:qwerty123@localhost:5432/events"
                "default": "sqlite://db.sqlite3"
            },
            "apps": {
                "models": {
                    "models": [
                        "src.datalayer.models.user",
                        "src.datalayer.models.posts"
                    ],
                    # If no default_connection specified, defaults to "default"
                    "default_connection": "default",
                }
            }
        },
        generate_schemas=True,
        add_exception_handlers=True
    )

def configure_middlewares(app):

    origins = [
    "http://127.0.0.1:5500"
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

