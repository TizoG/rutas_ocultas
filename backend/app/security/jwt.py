"""JWT verification utilities for Clerk tokens."""

import json
import time
from urllib.request import urlopen

import jwt
from fastapi import HTTPException, status
from jwt.algorithms import RSAAlgorithm

from app.core.config import settings

_JWKS_CACHE: dict[str, object] = {"expires_at": 0.0, "keys": {}}
_JWKS_TTL_SECONDS = 300


def _load_jwks_keys() -> dict[str, object]:
    now = time.time()
    if _JWKS_CACHE["keys"] and now < float(_JWKS_CACHE["expires_at"]):
        return _JWKS_CACHE["keys"]  # type: ignore[return-value]

    with urlopen(settings.clerk_jwks_url, timeout=5) as response:
        jwks_payload = json.loads(response.read().decode("utf-8"))

    keys = {key["kid"]: key for key in jwks_payload.get("keys", []) if key.get("kid")}
    if not keys:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Unable to load Clerk JWKS keys",
        )

    _JWKS_CACHE["keys"] = keys
    _JWKS_CACHE["expires_at"] = now + _JWKS_TTL_SECONDS
    return keys


def verify_clerk_jwt(token: str) -> dict:
    """Validate Clerk JWT signature and claims, returning decoded payload."""
    try:
        unverified_header = jwt.get_unverified_header(token)
        kid = unverified_header.get("kid")
        if not kid:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token missing key id")

        keys = _load_jwks_keys()
        jwk = keys.get(kid)
        if not jwk:
            _JWKS_CACHE["expires_at"] = 0
            keys = _load_jwks_keys()
            jwk = keys.get(kid)
            if not jwk:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Signing key not found")

        public_key = RSAAlgorithm.from_jwk(json.dumps(jwk))
        payload = jwt.decode(
            token,
            key=public_key,
            algorithms=["RS256"],
            issuer=settings.clerk_issuer,
            options={"require": ["exp", "iss", "sub"]},
        )
    except HTTPException:
        raise
    except jwt.ExpiredSignatureError as exc:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token has expired") from exc
    except jwt.InvalidTokenError as exc:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication token") from exc

    clerk_id = payload.get("sub")
    if not clerk_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token missing subject")
    return payload
