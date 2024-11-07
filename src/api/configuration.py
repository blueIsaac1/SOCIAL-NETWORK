from tortoise.contrib.fastapi import register_tortoise
from fastapi import FastAPI
from src.api.routes import users, home

def configure_routes(app: FastAPI):
    app.include_router(users.router)
    app.include_router(home.router)

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
                        "src.datalayer.models.user"
                    ],
                    # If no default_connection specified, defaults to "default"
                    "default_connection": "default",
                }
            }
        },
        generate_schemas=True,
        add_exception_handlers=True
    )