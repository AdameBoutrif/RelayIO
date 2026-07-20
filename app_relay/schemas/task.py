from pydantic import BaseModel, ConfigDict
from datetime import date

class TaskRead(BaseModel):
    id: int
    shot_id: int
    artist_id: int
    task_type_id: int
    priority_id: int
    due_date: date
    task_note: str | None = None
    start_date: date
    
    model_config = ConfigDict(from_attributes=True)

class TaskCreate(BaseModel):
    shot_id: int
    artist_id: int
    task_type_id: int
    priority_id: int
    due_date: date
    
    task_note: str | None = None

