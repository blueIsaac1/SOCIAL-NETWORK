from fastapi import FastAPI
from src.api.configuration import configure_routes, configure_db
from fastapi.middleware.cors import CORSMiddleware

def create_app():
    app = FastAPI()
    origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://127.0.0.1:5500",
    "file:///C:/Users/Shunppo/Desktop/SOCIAL-NETWORK/sn-public/public/index.html"
    ]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    # config db/tortoise
    configure_routes(app)
    configure_db(app)
    return app

app = create_app()

