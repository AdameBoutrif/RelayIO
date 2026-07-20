from pydantic import BaseModel, ConfigDict

class ShotRead(BaseModel):
    id: int
    shot_code: str
    frame_start: int
    frame_end: int

    model_config = ConfigDict(from_attributes=True)
