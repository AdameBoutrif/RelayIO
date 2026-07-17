from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app_relay.config import settings

DATABASE_URL = (
    f"postgresql+psycopg://"
    f"{settings.DB_USER}:{settings.DB_PASSWORD}"
    f"@{settings.DB_HOST}:{settings.DB_PORT}"
    f"/{settings.DB_NAME}"
)

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    expire_on_commit=False,
    autoflush=False,
    autocommit=False,
    bind=engine,
)
