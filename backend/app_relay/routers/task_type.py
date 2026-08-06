from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.app_relay.crud.task_type import get_task_types
from backend.app_relay.database import get_db
from backend.app_relay.schemas.task_type import TaskTypeRead

router = APIRouter(
    prefix='/task_types',
    tags=['Task Types'],
)

@router.get(
    "/"
)
def read_task_types(db:Session = Depends(get_db)):
    return get_task_types(db)