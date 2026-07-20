from fastapi import FastAPI

from app_relay.routers.movie import router as movies_router

app = FastAPI()

app.include_router(movies_router)