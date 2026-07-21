from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.app_relay.models.base import Base
from backend.app_relay.models.sequence import Sequence

if TYPE_CHECKING:
    from backend.app_relay.models.sequence import Sequence

class Movie(Base):
    __tablename__ = "movies"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    release_year: Mapped[int] = mapped_column(nullable=False)
    sequences: Mapped[list["Sequence"]] = relationship(
        back_populates="movie"
    )

    def __repr__(self) -> str:
        return (
            f"Movie(id={self.id}, "
            f"Title='{self.title}', "
            f"Release Year={self.release_year})"

        )