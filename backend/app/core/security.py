from __future__ import annotations

from functools import lru_cache

import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.config import settings
from app.db.session import get_db
from app.models.user import User

http_bearer = HTTPBearer(auto_error=False)


@lru_cache(maxsize=1)
def get_jwk_client() -> jwt.PyJWKClient:
    return jwt.PyJWKClient(settings.clerk_jwks_url)


def _decode_clerk_token(token: str) -> dict:
    try:
        signing_key = get_jwk_client().get_signing_key_from_jwt(token)
        decode_kwargs: dict[str, object] = {
            "algorithms": ["RS256"],
            "issuer": settings.clerk_issuer,
        }
        if settings.clerk_audience:
            decode_kwargs["audience"] = settings.clerk_audience
        else:
            decode_kwargs["options"] = {"verify_aud": False}

        return jwt.decode(token, signing_key.key, **decode_kwargs)
    except jwt.InvalidTokenError as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication token",
        ) from exc


def get_current_user(
    credentials: HTTPAuthorizationCredentials | None = Depends(http_bearer),
    db: Session = Depends(get_db),
) -> User:
    if credentials is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Authentication required",
        )

    payload = _decode_clerk_token(credentials.credentials)
    clerk_user_id = payload.get("sub")
    if not clerk_user_id:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token missing subject",
        )

    user = db.scalar(select(User).where(User.clerk_user_id == clerk_user_id))

    email = payload.get("email") or f"{clerk_user_id}@clerk.local"
    name = payload.get("name")
    avatar_url = payload.get("picture")

    if user is None:
        user = User(
            clerk_user_id=clerk_user_id,
            email=email,
            name=name,
            avatar_url=avatar_url,
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    changed = False
    if email and user.email != email:
        user.email = email
        changed = True
    if user.name != name:
        user.name = name
        changed = True
    if user.avatar_url != avatar_url:
        user.avatar_url = avatar_url
        changed = True

    if changed:
        db.add(user)
        db.commit()
        db.refresh(user)

    return user
