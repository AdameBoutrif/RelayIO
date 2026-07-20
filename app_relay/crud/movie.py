from sqlalchemy.orm import Session

from app_relay.models import Movie

def get_movies(db: Session):
    return db.query(Movie).all()
