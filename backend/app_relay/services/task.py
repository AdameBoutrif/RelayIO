from datetime import UTC, datetime

from sqlalchemy.orm import Session

from backend.app_relay.crud.task import create_task, delete_task, update_task, get_task
from backend.app_relay.handlers.exceptions import (
    InvalidDateRangeError,
    InvalidDeleteStatusError,
    InvalidDueDateError,
)
from backend.app_relay.models.task import Task
from backend.app_relay.schemas.task import TaskCreate, TaskDelete, TaskUpdate


def create_task_service(db: Session, task_in:TaskCreate) -> Task:

    if task_in.due_date < datetime.now(tz=UTC).today():
        raise InvalidDueDateError(task_in.due_date)

    if task_in.start_date > task_in.due_date:
        raise InvalidDateRangeError(
            task_in.start_date,
            task_in.due_date
        )
    
    new_task = create_task(db=db, task=task_in)

    return new_task

def update_task_service(db:Session, task_id: int, task_in:TaskUpdate):

    if (
        task_in.due_date is not None 
        and task_in.due_date < datetime.now(tz=UTC).today()
    ):
        raise InvalidDueDateError(task_in.due_date)

    return update_task(db= db, task_id=task_id, task_in= task_in)

def delete_task_service(db:Session, task_id: int):

    return delete_task(db=db, task_id=task_id)
        