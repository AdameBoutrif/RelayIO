from pydantic import BaseModel, ConfigDict

class MovieRead(BaseModel):
    id: int
    title: str
    release_year: int

    model_config = ConfigDict(from_attributes=True)