from sqlalchemy.orm import Session

from backend.app_relay.models.task_priority import Task_Priority
from backend.app_relay.schemas.task_priority import TaskPriorityRead

""" Query all task priorities"""

def get_task_priorities(db:Session):
    task_priorities = (
        db.query(Task_Priority).all()
    )

    return [
        TaskPriorityRead(
            id=task_priority.id,
            name=task_priority.name
        )
        for task_priority in task_priorities
    ]