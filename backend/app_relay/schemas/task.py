from datetime import datetime, date

from pydantic import BaseModel, ConfigDict

from backend.app_relay.schemas.artist import ArtistSummary
from backend.app_relay.schemas.shot import ShotSummary
from backend.app_relay.schemas.task_priority import TaskPriorityRead
from backend.app_relay.schemas.task_status import TaskStatusRead
from backend.app_relay.schemas.task_type import TaskTypeRead


class TaskRead(BaseModel):
    id: int
    shot: str
    task_type: str
    artist: str
    status: str
    start_date: date
    due_date: date
    priority: str
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

class TaskSummary(BaseModel):
    id: int
    shot: str
    artist: str
    task_type: str
    status: str
    priority: str
    due_date: date

    model_config = ConfigDict(from_attributes=True)

class TaskDetails(BaseModel):
    id: int
    start_date: date
    due_date: date
    task_note: str

    artist: ArtistSummary
    shot: ShotSummary
    task_type: TaskTypeRead
    task_status: TaskStatusRead
    priority: TaskPriorityRead

class TaskUpdate(BaseModel):
    artist_id: int | None = None
    shot_id: int | None = None
    task_type_id: int | None = None
    status_id: int | None = None
    priority_id: int | None = None

    start_date: date | None = None
    due_date: datetime | None = None
    task_note: str | None = None
