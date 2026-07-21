from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.app_relay.database import get_db
from backend.app_relay.crud.movie import get_movies, get_movie
from backend.app_relay.schemas import MovieRead

router = APIRouter(
    prefix="/movies",
    tags=["Movies"],
)

@router.get(
        "",
        response_model=list[MovieRead],
)

def read_movies(db: Session = Depends(get_db)):
    return get_movies(db)

@router.get(
        "/{movie_id}",
        response_model=MovieRead,
)

def read_movie(movie_id: int, db: Session = Depends(get_db)):
    movie = get_movie(db=db, movie_id=movie_id)
    if movie is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Movie not found"
        )
    return movie

