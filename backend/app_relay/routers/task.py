# from typing import TYPE_CHECKING

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.app_relay.crud.task import get_task, get_task_summaries, get_tasks
from backend.app_relay.database import get_db
from backend.app_relay.schemas.task import TaskCreate, TaskRead
from backend.app_relay.services.task import create_task_service

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"],
)

@router.get(
        "/"
        #response_model=list[TaskRead],
)

def read_tasks(db: Session = Depends(get_db)):
    return get_task_summaries(db)



@router.get(
    "/{id}",
    response_model=TaskRead,
)
def read_task(task_id: int, db: Session = Depends(get_db)):
    task =  get_task(db=db, task_id=task_id)
    if task is None:
        raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Task not found"
                )
    return task

@router.post(
    "",
    response_model=TaskRead,
    status_code=status.HTTP_201_CREATED
)

def post_task(task_in: TaskCreate, db: Session = Depends(get_db)):
    return create_task_service(db=db, task_in=task_in)