"""Persistence operations for routes."""

import uuid

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.route import Route
from app.schemas.route import RouteCreate


class RouteRepository:
    """CRUD repository for route entities."""

    def create(self, db: Session, payload: RouteCreate, author_id: uuid.UUID) -> Route:
        route = Route(**payload.model_dump(), author_id=author_id)
        db.add(route)
        db.commit()
        db.refresh(route)
        return route

    def get_by_id(self, db: Session, route_id: uuid.UUID) -> Route | None:
        return db.get(Route, route_id)

    def list(self, db: Session, limit: int, offset: int) -> list[Route]:
        stmt = select(Route).limit(limit).offset(offset).order_by(Route.created_at.desc())
        return list(db.scalars(stmt).all())

    def update(self, db: Session, route: Route, data: dict) -> Route:
        for key, value in data.items():
            setattr(route, key, value)
        db.add(route)
        db.commit()
        db.refresh(route)
        return route

    def delete(self, db: Session, route: Route) -> None:
        db.delete(route)
        db.commit()
