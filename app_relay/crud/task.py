from sqlalchemy.orm import Session

from app_relay.models.task import Task
from app_relay.schemas.task import TaskCreate


def create_task(db: Session, task: TaskCreate) -> Task:
    
    db_task = Task(**task.model_dump())
    
    db.add(db_task)

    db.commit()

    db.refresh(db_task)

    return db_task