from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app_relay.database import get_db
from app_relay.crud.task import create_task
from app_relay.schemas.task import TaskCreate, TaskRead

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"],
)

@router.post(
    "",
    response_model=TaskRead,
    status_code=status.HTTP_201_CREATED
)

def post_task(task_in:TaskCreate, db: Session = Depends(get_db)):
    new_task = create_task(db=db, task=task_in)
    return new_task