from fastapi import FastAPI

from app_relay.routers.movie import router as movies_router
from app_relay.routers.task import router as task_router

app = FastAPI()

app.include_router(movies_router)
app.include_router(task_router)