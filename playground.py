from app_relay.database import SessionLocal
from app_relay.models import Movie

db = SessionLocal()

movie = (
    db.query(Movie)
    .filter(Movie.title == 'Project Atlas')
    .first()
)

if movie is not None:
    # print(movie)
    print(movie.title)
    for sequence in movie.sequences:
        print(sequence.sequence_code)
        for shot in sequence.shots:
            print("     ", shot.shot_code)

db.close()