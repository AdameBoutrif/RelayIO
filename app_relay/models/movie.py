from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app_relay.models.base import Base

class Movie(Base):
    __tablename__ = "movies"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    release_year: Mapped[int] = mapped_column(nullable=False)

    def __repr__(self) -> str:
        return (
            f"Movie(id={self.id}, "
            f"Title='{self.title}', "
            f"Release Year={self.release_year})"

        )