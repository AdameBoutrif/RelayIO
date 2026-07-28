from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.app_relay.models.base import Base

class Task_Status(Base):
    __tablename__ = "task_statuses"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(String(50), nullable=False)