from sqlalchemy.orm import Session, selectinload

from backend.app_relay.models.task import Task
from backend.app_relay.schemas.task import TaskCreate, TaskRead

"""Query all tasks available"""

def get_tasks(db:Session) -> list[Task]:
    return db.query(Task).all()

"""Query task by id"""

def get_task(db: Session, task_id: int) -> Task | None:
    
    return (
        db.query(Task)
        .filter(Task.id == task_id)
        .first()
    )

"""Create Task"""

def create_task(db: Session, task: TaskCreate) -> Task:
    
    db_task = Task(**task.model_dump())
    
    db.add(db_task)

    db.commit()

    db.refresh(db_task)

    return db_task