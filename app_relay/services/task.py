from typing import TYPE_CHECKING

from sqlalchemy.orm import Session


from app_relay.schemas.task import TaskCreate
from app_relay.crud.task import create_task
from app_relay.models.task import Task
from app_relay.handlers.exceptions import InvalidDueDateError

from datetime import date

if TYPE_CHECKING:
    from app_relay.models.task import Task

def create_task_service(db: Session, task_in:TaskCreate) -> Task:

    if task_in.due_date < date.today():
        raise InvalidDueDateError(task_in.due_date)
    
    new_task = create_task(db=db, task=task_in)

    return new_task