from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from backend.app_relay.routers.movie import router as movies_router
from backend.app_relay.routers.task import router as task_router
from backend.app_relay.handlers.exceptions import InvalidDueDateError

app = FastAPI()

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