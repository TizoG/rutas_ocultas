"""Route DTOs."""

import uuid
from datetime import datetime

from pydantic import BaseModel, ConfigDict

from app.models.route import DifficultyLevel


class RouteCreate(BaseModel):
    title: str
    description: str | None = None
    distance_km: float
    difficulty: DifficultyLevel


class RouteUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    distance_km: float | None = None
    difficulty: DifficultyLevel | None = None


class RouteRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    author_id: uuid.UUID
    title: str
    description: str | None
    distance_km: float
    difficulty: DifficultyLevel
    created_at: datetime
    updated_at: datetime
