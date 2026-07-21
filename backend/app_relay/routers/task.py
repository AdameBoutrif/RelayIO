# from typing import TYPE_CHECKING

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from backend.app_relay.database import get_db
from backend.app_relay.services.task import create_task_service
from backend.app_relay.schemas.task import TaskCreate, TaskRead


router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"],
)

@router.post(
    "",
    response_model=TaskRead,
    status_code=status.HTTP_201_CREATED
)

def post_task(task_in: TaskCreate, db: Session = Depends(get_db)):
    return create_task_service(db=db, task_in=task_in)