from fastapi import FastAPI
from src.api.configuration import configure_routes, configure_db, configure_middlewares

def create_app():
    app = FastAPI()
    
    configure_middlewares(app)
    
    # config db/tortoise
    configure_routes(app)

    configure_db(app)

    return app

app = create_app()

