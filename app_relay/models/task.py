from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import date, datetime

from app_relay.models.base import Base

if TYPE_CHECKING:
    from app_relay.models.shot import Shot

class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)

    shot_id: Mapped[int] = mapped_column(
        ForeignKey("shots.id"),
        nullable=False,
    )
    shot: Mapped["Shot"] = relationship(
        back_populates="tasks"
    )

    task_type_id: Mapped[int] = mapped_column(
        ForeignKey("task_types.id"),
        nullable=False,
    )

    artist_id: Mapped[int] = mapped_column(
        ForeignKey("artists.id"),
        nullable=False,
    )

    status_id: Mapped[int] = mapped_column(
        ForeignKey("task_statuses.id"),
        default=1,
    )

    due_date: Mapped[datetime]

    priority_id: Mapped[int] = mapped_column(
        ForeignKey("task_priorities.id"),
        default=1,
    )

    task_note: Mapped[str] = mapped_column(
        String(255),
        nullable=True,
    )

    def __repr__(self):
        return (
            f"Task(id={self.id})"
        )