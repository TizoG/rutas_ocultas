"""Business logic for comments."""

import uuid

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.comment import Comment
from app.models.user import User
from app.repositories.comment_repository import CommentRepository
from app.repositories.route_repository import RouteRepository
from app.schemas.comment import CommentCreate


class CommentService:
    """Use-cases for comment management."""

    def __init__(
        self,
        comment_repository: CommentRepository | None = None,
        route_repository: RouteRepository | None = None,
    ) -> None:
        self.comment_repository = comment_repository or CommentRepository()
        self.route_repository = route_repository or RouteRepository()

    def create_comment(self, db: Session, payload: CommentCreate, current_user: User) -> Comment:
        route = self.route_repository.get_by_id(db, payload.route_id)
        if route is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Route not found")
        return self.comment_repository.create(db, payload=payload, author_id=current_user.id)

    def get_comment_or_404(self, db: Session, comment_id: uuid.UUID) -> Comment:
        comment = self.comment_repository.get_by_id(db, comment_id)
        if comment is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Comment not found")
        return comment

    def list_comments(self, db: Session, limit: int, offset: int) -> list[Comment]:
        return self.comment_repository.list(db, limit=limit, offset=offset)

    def list_comments_by_route(self, db: Session, route_id: uuid.UUID, limit: int, offset: int) -> list[Comment]:
        route = self.route_repository.get_by_id(db, route_id)
        if route is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Route not found")
        return self.comment_repository.list_by_route(db, route_id=route_id, limit=limit, offset=offset)

    def delete_comment(self, db: Session, comment_id: uuid.UUID, current_user: User) -> None:
        comment = self.get_comment_or_404(db, comment_id)
        if comment.author_id != current_user.id:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="You cannot delete this comment")
        self.comment_repository.delete(db, comment)
