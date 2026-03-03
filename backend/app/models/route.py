import uuid
from datetime import datetime

from sqlalchemy import DateTime, Float, ForeignKey, Index, String, Text, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class Route(Base):
    __tablename__ = "routes"
    __table_args__ = (
        Index("ix_routes_author_created_at", "author_id", "created_at"),
        Index("ix_routes_created_at", "created_at"),
        Index("ix_routes_author_id", "author_id"),
    )

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    author_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
    )
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    start_lat: Mapped[float] = mapped_column(Float, nullable=False)
    start_lng: Mapped[float] = mapped_column(Float, nullable=False)
    end_lat: Mapped[float] = mapped_column(Float, nullable=False)
    end_lng: Mapped[float] = mapped_column(Float, nullable=False)
    polyline: Mapped[str] = mapped_column(Text, nullable=False)
    distance_km: Mapped[float] = mapped_column(Float, nullable=False)
    duration_min: Mapped[float] = mapped_column(Float, nullable=False)
    visibility: Mapped[str] = mapped_column(String(50), nullable=False, default="public", index=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())

    author = relationship("User", back_populates="routes")
    comments = relationship("Comment", back_populates="route", cascade="all, delete-orphan")
    favorites = relationship("Favorite", back_populates="route", cascade="all, delete-orphan")
    votes = relationship("Vote", back_populates="route", cascade="all, delete-orphan")
