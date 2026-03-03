"""Comment endpoints."""

import uuid

from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.comment import CommentCreate, CommentRead
from app.security.dependencies import get_current_user
from app.services.comment_service import CommentService

router = APIRouter(prefix="/comments", tags=["comments"])
service = CommentService()


@router.get("", response_model=list[CommentRead])
def list_comments(
    limit: int = Query(10, le=100),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db),
) -> list[CommentRead]:
    return service.list_comments(db, limit=limit, offset=offset)


@router.get("/route/{route_id}", response_model=list[CommentRead])
def list_comments_by_route(
    route_id: uuid.UUID,
    limit: int = Query(10, le=100),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db),
) -> list[CommentRead]:
    return service.list_comments_by_route(db, route_id=route_id, limit=limit, offset=offset)


@router.post("", response_model=CommentRead, status_code=status.HTTP_201_CREATED)
def create_comment(
    payload: CommentCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
) -> CommentRead:
    return service.create_comment(db, payload=payload, current_user=current_user)


@router.delete("/{comment_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_comment(
    comment_id: uuid.UUID,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
) -> None:
    service.delete_comment(db, comment_id=comment_id, current_user=current_user)
