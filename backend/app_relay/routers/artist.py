from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.app_relay.crud.artist import get_artist_names
from backend.app_relay.database import get_db
from backend.app_relay.schemas.artist import ArtistSummary
from backend.app_relay.models.artist import Artist

router = APIRouter(
    prefix='/artists',
    tags=['Artists'],
)

@router.get(
    "/"
)
def read_artists(db:Session = Depends(get_db)):
    return get_artist_names(db)