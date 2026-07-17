from app_relay.database import SessionLocal
from app_relay.models import Movie

db = SessionLocal()

movie = db.query(Movie).filter(Movie.title == 'Project Atlas').first()

print(movie)

db.close()