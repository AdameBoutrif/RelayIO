from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.app_relay.crud.task_status import get_task_statuses
from backend.app_relay.database import get_db

router = APIRouter(
    prefix='/task_statuses',
    tags=['Task Statuses'],
)

@router.get(
    "/"
)
def read_task_statuses(db:Session = Depends(get_db)):
    return get_task_statuses(db)