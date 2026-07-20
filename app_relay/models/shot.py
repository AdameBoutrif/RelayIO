from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app_relay.models.base import Base

if TYPE_CHECKING:
    from app_relay.models.sequence import Sequence
    from app_relay.models.task import Task

class Shot(Base):
    __tablename__ = "shots"

    id: Mapped[int] = mapped_column(primary_key=True)

    sequence_id: Mapped[int] = mapped_column(
        ForeignKey("sequences.id"),
        nullable=False,
    )

    shot_code: Mapped[str] = mapped_column(
        String(50),
        nullable=False,
    )

    frame_start: Mapped[int]
    frame_end: Mapped[int]

    sequence: Mapped["Sequence"] = relationship(
        back_populates="shots"
    )

    tasks: Mapped[list["Task"]] = relationship(
        back_populates="shot"
    )

    def __repr__(self):
        return (
            f"Shot(id={self.id}, shot_code='{self.shot_code}')"
        )