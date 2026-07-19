from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app_relay.models.base import Base

if TYPE_CHECKING: 
    from app_relay.models.movie import Movie

class Sequence(Base):

    __tablename__ = "sequences"

    id: Mapped[int] = mapped_column(primary_key=True)

    movie_id: Mapped[int] = mapped_column(
        ForeignKey("movies.id"),
        nullable=False,
    )

    sequence_code: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    movie: Mapped["Movie"] = relationship(
        back_populates="sequences"
    )

    def __repr__(self) -> str:
        return(
            f"Sequence(id={self.id}, "
            f"sequence_code='{self.sequence_code}')"

        )
