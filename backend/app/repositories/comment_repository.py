"""Persistence operations for comments."""

import uuid

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.comment import Comment
from app.schemas.comment import CommentCreate


class CommentRepository:
    """CRUD repository for comment entities."""

    def create(self, db: Session, payload: CommentCreate, author_id: uuid.UUID) -> Comment:
        comment = Comment(route_id=payload.route_id, content=payload.content, author_id=author_id)
        db.add(comment)
        db.commit()
        db.refresh(comment)
        return comment

    def get_by_id(self, db: Session, comment_id: uuid.UUID) -> Comment | None:
        return db.get(Comment, comment_id)

    def list(self, db: Session, limit: int, offset: int) -> list[Comment]:
        stmt = select(Comment).limit(limit).offset(offset).order_by(Comment.created_at.desc())
        return list(db.scalars(stmt).all())

    def list_by_route(self, db: Session, route_id: uuid.UUID, limit: int, offset: int) -> list[Comment]:
        stmt = (
            select(Comment)
            .where(Comment.route_id == route_id)
            .limit(limit)
            .offset(offset)
            .order_by(Comment.created_at.desc())
        )
        return list(db.scalars(stmt).all())

    def update(self, db: Session, comment: Comment, data: dict) -> Comment:
        for key, value in data.items():
            setattr(comment, key, value)
        db.add(comment)
        db.commit()
        db.refresh(comment)
        return comment

    def delete(self, db: Session, comment: Comment) -> None:
        db.delete(comment)
        db.commit()
