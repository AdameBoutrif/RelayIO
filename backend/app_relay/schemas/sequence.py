from pydantic import BaseModel, ConfigDict

from backend.app_relay.schemas.shot import ShotRead

class SequenceRead(BaseModel):
    id: int
    sequence_code: str
    shots: list[ShotRead]

    model_config = ConfigDict(from_attributes=True)