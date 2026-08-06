from pydantic import BaseModel, ConfigDict

from backend.app_relay.schemas.department import DepartmentRead


class ArtistRead(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    department: int

    model_config = ConfigDict(from_attributes=True)

class ArtistSummary(BaseModel):
    id: int
    full_name: str

