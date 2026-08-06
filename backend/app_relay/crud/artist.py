from sqlalchemy.orm import Session

from backend.app_relay.models.artist import Artist
from backend.app_relay.schemas.artist import ArtistSummary

""" Query all artists"""

def get_artist_names(db:Session):
    artists = (
        db.query(Artist).all()
    )

    return [
        ArtistSummary(
            id=artist.id,
            full_name=artist.full_name
        )
        for artist in artists
    ]