from sqlalchemy.orm import Session, selectinload

from backend.app_relay.models.task import Task
from backend.app_relay.schemas.task import (
    TaskCreate,
    TaskDelete,
    TaskSummary,
    TaskUpdate,
)

"""Query all tasks available"""

def get_tasks(db:Session) -> list[Task]:
    return (
        db.query(Task)
        .options(
            selectinload(Task.artist),
            selectinload(Task.shot),
            selectinload(Task.task_status),
            selectinload(Task.priority),
            selectinload(Task.task_type),
        )
        .all()
    )

"""Query task by id"""

def get_task(db: Session, task_id: int) -> Task | None:
    
        return (
             db.query(Task)
                .options(
                    selectinload(Task.shot),
                    selectinload(Task.task_type),
                    selectinload(Task.artist),
                    selectinload(Task.task_status),
                    selectinload(Task.priority)
                )
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

"""Query tasks with rich data"""

def get_task_summaries(db: Session):
    tasks = (
        db.query(Task)
        .options(
            selectinload(Task.shot),
            selectinload(Task.artist),
            selectinload(Task.task_status),
            selectinload(Task.priority),
            selectinload(Task.task_type),
        )
        .all()
    )

    return [
        TaskSummary(
            id=task.id,
            shot=task.shot.shot_code,
            artist=task.artist.full_name,
            task_type=task.task_type.name,
            status=task.task_status.name,
            priority=task.priority.name,
            due_date=task.due_date
        )
        for task in tasks
    ]

"""Update Task"""

def update_task(db: Session, task_id: int, task_in: TaskUpdate ) -> Task | None:
    
    db_task = (
        db.query(Task)
        .filter(Task.id == task_id)
        .first()
        )
    if db_task is None:
         return None

    update_data = task_in.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(db_task, field, value)

    db.commit()

    db.refresh(db_task)

    return db_task

"""Delete Task"""

def delete_task(db:Session, task_id: int) -> Task | None:
    db_task = (
         db.query(Task)
         .filter(Task.id == task_id)
         .first()
    )
    if db_task is None:
         return None

    db.delete(db_task)

    db.commit()

    return db_task
