"""Business logic for routes."""

import uuid

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.route import Route
from app.models.user import User
from app.repositories.route_repository import RouteRepository
from app.schemas.route import RouteCreate, RouteUpdate


class RouteService:
    """Use-cases for route management."""

    def __init__(self, repository: RouteRepository | None = None) -> None:
        self.repository = repository or RouteRepository()

    def create_route(self, db: Session, payload: RouteCreate, current_user: User) -> Route:
        return self.repository.create(db, payload=payload, author_id=current_user.id)

    def get_route_or_404(self, db: Session, route_id: uuid.UUID) -> Route:
        route = self.repository.get_by_id(db, route_id)
        if route is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Route not found")
        return route

    def list_routes(self, db: Session, limit: int, offset: int) -> list[Route]:
        return self.repository.list(db, limit=limit, offset=offset)

    def update_route(self, db: Session, route_id: uuid.UUID, payload: RouteUpdate, current_user: User) -> Route:
        route = self.get_route_or_404(db, route_id)
        if route.author_id != current_user.id:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You cannot modify this route")
        return self.repository.update(db, route, payload.model_dump(exclude_unset=True))

    def delete_route(self, db: Session, route_id: uuid.UUID, current_user: User) -> None:
        route = self.get_route_or_404(db, route_id)
        if route.author_id != current_user.id:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You cannot delete this route")
        self.repository.delete(db, route)
