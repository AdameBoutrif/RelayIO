from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.app_relay.crud.task_priority import get_task_priorities
from backend.app_relay.database import get_db

router = APIRouter(
    prefix='/task_priorities',
    tags=['Task Priorities'],
)

@router.get(
    "/"
)
def read_task_priorities(db:Session = Depends(get_db)):
    return get_task_priorities(db)