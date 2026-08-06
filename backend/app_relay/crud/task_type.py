from sqlalchemy.orm import Session

from backend.app_relay.models.task_type import Task_Type
from backend.app_relay.schemas.task_type import TaskTypeRead

""" Query all task types"""

def get_task_types(db:Session):
    task_types = (
        db.query(Task_Type).all()
    )

    return [
        TaskTypeRead(
            id=task_type.id,
            name=task_type.name
        )
        for task_type in task_types
    ]