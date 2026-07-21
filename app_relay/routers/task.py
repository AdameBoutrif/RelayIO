# from typing import TYPE_CHECKING

from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session

from app_relay.database import get_db
from app_relay.services.task import create_task_service
from app_relay.schemas.task import TaskCreate, TaskRead
from app_relay.exceptions.task import InvalidDueDateError

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
    try:
        return create_task_service(db=db, task_in=task_in)
    except InvalidDueDateError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc)
        )
        