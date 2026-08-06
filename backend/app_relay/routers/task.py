# from typing import TYPE_CHECKING

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.app_relay.crud.task import get_task, get_task_summaries
from backend.app_relay.database import get_db
from backend.app_relay.schemas.task import (
    TaskCreate,
    TaskDetails,
    TaskRead,
    TaskUpdate,
)
from backend.app_relay.services.task import (
    create_task_service,
    delete_task_service,
    update_task_service,
)

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"],
)

@router.get(
        "/"
)

def read_tasks(db: Session = Depends(get_db)):  # noqa: B008
    return get_task_summaries(db)



@router.get(
        "/{task_id}",
        response_model=TaskDetails
)
def read_task(task_id: int, db: Session = Depends(get_db)):  # noqa: B008
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

def create_task(task_in: TaskCreate, db: Session = Depends(get_db)):  # noqa: B008
    return create_task_service(db=db, task_in=task_in)

@router.patch(
    "/{task_id}",
    response_model=TaskDetails
)

def update_task(task_id: int, task_in:TaskUpdate, db:Session = Depends (get_db)):  # noqa: B008

    task = update_task_service(
                        db=db,
                        task_id=task_id, 
                        task_in=task_in
                        )

    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task {task_id} not found.",
        )
    
    return task

@router.delete(
    "/{task_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)

def delete_task(id: int, db:Session = Depends (get_db)):

    task = delete_task_service(
        db=db,
        task_id=id   
    )

    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task {id} not found"
        )