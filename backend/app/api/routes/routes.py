"""Route endpoints."""

import uuid

from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.route import RouteCreate, RouteRead, RouteUpdate
from app.security.dependencies import get_current_user
from app.services.route_service import RouteService

router = APIRouter(prefix="/routes", tags=["routes"])
service = RouteService()


@router.get("", response_model=list[RouteRead])
def list_routes(
    limit: int = Query(10, le=100),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db),
) -> list[RouteRead]:
    return service.list_routes(db, limit=limit, offset=offset)


@router.get("/{route_id}", response_model=RouteRead)
def get_route(route_id: uuid.UUID, db: Session = Depends(get_db)) -> RouteRead:
    return service.get_route_or_404(db, route_id)


@router.post("", response_model=RouteRead, status_code=status.HTTP_201_CREATED)
def create_route(
    payload: RouteCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
) -> RouteRead:
    return service.create_route(db, payload=payload, current_user=current_user)


@router.put("/{route_id}", response_model=RouteRead)
def update_route(
    route_id: uuid.UUID,
    payload: RouteUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
) -> RouteRead:
    return service.update_route(db, route_id=route_id, payload=payload, current_user=current_user)


@router.delete("/{route_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_route(
    route_id: uuid.UUID,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
) -> None:
    service.delete_route(db, route_id=route_id, current_user=current_user)
