from sqlalchemy.orm import Session
from app_relay.schemas.task import TaskCreate
from app_relay.crud.task import create_task
from app_relay.models.task import Task

def create_task_service(db: Session, task_in:TaskCreate) -> Task:

    new_task = create_task(db=db, task=task_in)

    return new_task