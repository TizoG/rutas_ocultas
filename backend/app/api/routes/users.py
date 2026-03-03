"""User endpoints."""

import uuid

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.user import UserRead
from app.security.dependencies import get_current_user
from app.services.user_service import UserService

router = APIRouter(prefix="/users", tags=["users"])
service = UserService()


@router.get("", response_model=list[UserRead])
def list_users(
    limit: int = Query(10, le=100),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db),
) -> list[UserRead]:
    return service.list_users(db, limit=limit, offset=offset)


@router.get("/me", response_model=UserRead)
def read_me(current_user=Depends(get_current_user)) -> UserRead:
    return current_user


@router.get("/{user_id}", response_model=UserRead)
def get_user(user_id: uuid.UUID, db: Session = Depends(get_db)) -> UserRead:
    return service.get_by_id_or_404(db, user_id)
