from typing import TYPE_CHECKING

from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.app_relay.models.base import Base

if TYPE_CHECKING:
    from backend.app_relay.models.task import Task

class Artist(Base):
    __tablename__ = "artists"

    id: Mapped[int] = mapped_column(primary_key=True)

    first_name: Mapped[str] = mapped_column(String(100), nullable=False)

    last_name: Mapped[str] = mapped_column(String(100), nullable=False)

    email: Mapped[str] = mapped_column(String(150), nullable=False)

    department_id: Mapped[int] = mapped_column(
        ForeignKey("departments.id"),
        nullable=False,
    )

    tasks: Mapped["Task"] = relationship(
        back_populates="artist"
    )

    @property
    def full_name (self) -> str:
        return f"{self.first_name} {self.last_name}"

    