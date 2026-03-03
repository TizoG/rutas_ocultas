"""Route ORM model."""

import enum
import uuid
from datetime import datetime

from sqlalchemy import DateTime, Enum, Float, ForeignKey, Index, String, Text, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class DifficultyLevel(str, enum.Enum):
    """Allowed route difficulty values."""

    easy = "easy"
    medium = "medium"
    hard = "hard"


class Route(Base):
    """Cycling or walking route."""

    __tablename__ = "routes"
    __table_args__ = (Index("ix_routes_author_id", "author_id"),)

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    author_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), index=True, nullable=False
    )
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str | None] = mapped_column(Text)
    distance_km: Mapped[float] = mapped_column(Float, nullable=False)
    difficulty: Mapped[DifficultyLevel] = mapped_column(
        Enum(DifficultyLevel, name="difficulty_level"), nullable=False, default=DifficultyLevel.medium
    )
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False
    )

    author: Mapped["User"] = relationship(back_populates="routes")
    comments: Mapped[list["Comment"]] = relationship(back_populates="route", cascade="all, delete-orphan")
