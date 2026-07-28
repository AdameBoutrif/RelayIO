from datetime import date

from pydantic import BaseModel, ConfigDict


class TaskRead(BaseModel):
    id: int
    shot_id: int
    task_type_id: int
    artist_id: int
    status_id: int
    start_date: date
    due_date: date
    priority_id: int
    task_note: str | None = None
    
    
    model_config = ConfigDict(from_attributes=True)

class TaskCreate(BaseModel):
    id: int
    shot_id: int
    task_type_id: int
    artist_id: int
    status_id: int
    start_date: date
    due_date: date
    priority_id: int
    task_note: str | None = None

