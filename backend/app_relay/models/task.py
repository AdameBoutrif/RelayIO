from datetime import date
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.app_relay.models.base import Base

if TYPE_CHECKING:
    from backend.app_relay.models.artist import Artist
    from backend.app_relay.models.shot import Shot
    from backend.app_relay.models.task_priority import Task_Priority
    from backend.app_relay.models.task_status import Task_Status
    from backend.app_relay.models.task_type import Task_Type


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

    start_date: Mapped[date]

    due_date: Mapped[date]

    priority_id: Mapped[int] = mapped_column(
        ForeignKey("task_priorities.id"),
        default=1,
    )

    task_note: Mapped[str] = mapped_column(
        String(255),
        nullable=True,
    )

    artist: Mapped["Artist"] = relationship(
        back_populates="tasks"
    )

    task_status: Mapped["Task_Status"] = relationship(
        back_populates="tasks"
    )

    priority: Mapped["Task_Priority"] = relationship(
        back_populates="tasks"
    )

    task_type: Mapped["Task_Type"] = relationship(
        back_populates="tasks"
    )

    def __repr__(self):
        return (
            f"Task(id={self.id})"
        )