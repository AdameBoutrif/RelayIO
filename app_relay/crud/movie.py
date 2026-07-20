from sqlalchemy.orm import Session, selectinload

from app_relay.models.movie import Movie
from app_relay.models.sequence import Sequence

def get_movies(db: Session) -> list[Movie]:
    return db.query(Movie).all()

def get_movie(db: Session, movie_id: int) -> Movie | None:
    
    return (
        db.query(Movie).options(selectinload(Movie.sequences).selectinload(Sequence.shots))
        .filter(Movie.id == movie_id)
        .first()
    )
