"""Business logic for users."""

import uuid

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate


class UserService:
    """Use-cases for user management."""

    def __init__(self, repository: UserRepository | None = None) -> None:
        self.repository = repository or UserRepository()

    def get_or_create_by_clerk(self, db: Session, clerk_id: str, email: str) -> User:
        user = self.repository.get_by_clerk_id(db, clerk_id)
        if user:
            return user
        return self.repository.create(db, UserCreate(clerk_id=clerk_id, email=email))

    def get_by_id_or_404(self, db: Session, user_id: uuid.UUID) -> User:
        user = self.repository.get_by_id(db, user_id)
        if user is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        return user

    def list_users(self, db: Session, limit: int, offset: int) -> list[User]:
        return self.repository.list(db, limit=limit, offset=offset)
