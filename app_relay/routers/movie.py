from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app_relay.database import get_db
from app_relay.crud.movie import get_movies
from app_relay.schemas import MovieRead

router = APIRouter()

@router.get(
        "/movies",
        response_model=list[MovieRead],
)

def read_movies(db: Session = Depends(get_db)):
    return get_movies(db)