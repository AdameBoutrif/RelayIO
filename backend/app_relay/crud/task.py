from sqlalchemy.orm import Session, selectinload

from backend.app_relay.models.task import Task
from backend.app_relay.schemas.task import TaskCreate, TaskSummary

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