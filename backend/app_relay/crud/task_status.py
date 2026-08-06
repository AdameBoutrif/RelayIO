from sqlalchemy.orm import Session

from backend.app_relay.models.task_status import Task_Status
from backend.app_relay.schemas.task_status import TaskStatusRead

""" Query all task statuses """

def get_task_statuses(db:Session):
    task_statuses = (
        db.query(Task_Status).all()
    )

    return [
        TaskStatusRead(
            id=task_status.id,
            name=task_status.name
        )
        for task_status in task_statuses
    ]