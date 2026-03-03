"""Security dependencies for authenticated endpoints."""

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.models.user import User
from app.security.jwt import verify_clerk_jwt
from app.services.user_service import UserService

bearer_scheme = HTTPBearer(auto_error=True)


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
    db: Session = Depends(get_db),
) -> User:
    """Resolve current authenticated user from Clerk JWT."""
    token = credentials.credentials
    payload = verify_clerk_jwt(token)

    clerk_id = payload.get("sub")
    email = payload.get("email")
    if not clerk_id or not email:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token does not include required user claims",
        )

    return UserService().get_or_create_by_clerk(db, clerk_id=clerk_id, email=email)
