from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from backend.app_relay.models.base import Base

class Artist(Base):
    __tablename__ = "artists"

    id: Mapped[int] = mapped_column(primary_key=True)

    first_name: Mapped[str] = mapped_column(String(100), nullable=False)

    last_name: Mapped[str] = mapped_column(String(100), nullable=False)

    email: Mapped[str] = mapped_column(String(150), nullable=False)

    department: Mapped[int] = mapped_column(
        ForeignKey("departments.id"),
        nullable=False,
    )

    