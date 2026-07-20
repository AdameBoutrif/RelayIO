from sqlalchemy.orm import Session

from app_relay.models import Movie

def get_movies(db: Session) -> list[Movie]:
    return db.query(Movie).all()

def get_movie(db: Session, movie_id: int) -> Movie | None:
    return (
        db.query(Movie)
        .filter(Movie.id == movie_id)
        .first()
    )
