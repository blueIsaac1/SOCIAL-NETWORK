from fastapi import FastAPI
from src.api.configuration import configure_routes, configure_db

def create_app():
    app = FastAPI()
    # config db/tortoise
    configure_routes(app)
    configure_db(app)
    return app

app = create_app()
