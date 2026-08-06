from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from backend.app_relay.handlers.exceptions import InvalidDueDateError
from backend.app_relay.routers.artist import router as artist_router
from backend.app_relay.routers.movie import router as movies_router
from backend.app_relay.routers.task import router as task_router
from backend.app_relay.routers.task_priority import router as task_priority_router
from backend.app_relay.routers.task_status import router as task_status_router
from backend.app_relay.routers.task_type import router as task_type_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.exception_handler(InvalidDueDateError)
def invalid_due_date_on_task_error(request: Request, exc: InvalidDueDateError):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": "Invalid due date",
            "message": exc.message,
            "path": request.url.path,
        }
    )

app.include_router(movies_router)
app.include_router(task_router)
app.include_router(artist_router)
app.include_router(task_type_router)
app.include_router(task_status_router)
app.include_router(task_priority_router)