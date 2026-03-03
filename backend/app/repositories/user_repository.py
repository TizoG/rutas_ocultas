"""Persistence operations for users."""

import uuid

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate


class UserRepository:
    """CRUD repository for user entities."""

    def create(self, db: Session, payload: UserCreate) -> User:
        user = User(clerk_id=payload.clerk_id, email=str(payload.email))
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    def get_by_id(self, db: Session, user_id: uuid.UUID) -> User | None:
        return db.get(User, user_id)

    def get_by_clerk_id(self, db: Session, clerk_id: str) -> User | None:
        return db.scalar(select(User).where(User.clerk_id == clerk_id))

    def list(self, db: Session, limit: int, offset: int) -> list[User]:
        stmt = select(User).limit(limit).offset(offset).order_by(User.created_at.desc())
        return list(db.scalars(stmt).all())

    def update(self, db: Session, user: User, data: dict) -> User:
        for key, value in data.items():
            setattr(user, key, value)
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    def delete(self, db: Session, user: User) -> None:
        db.delete(user)
        db.commit()
