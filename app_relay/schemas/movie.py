from pydantic import BaseModel, ConfigDict

from app_relay.schemas.sequence import SequenceRead

class MovieRead(BaseModel):
    id: int
    title: str
    release_year: int

    sequences: list[SequenceRead]

    model_config = ConfigDict(from_attributes=True)