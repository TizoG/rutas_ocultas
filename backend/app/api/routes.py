from __future__ import annotations

import uuid

from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel, ConfigDict
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.core.security import get_current_user
from app.db.session import get_db
from app.models.comment import Comment
from app.models.favorite import Favorite
from app.models.route import Route
from app.models.user import User
from app.models.vote import Vote

router = APIRouter()


class RouteCreate(BaseModel):
    title: str
    description: str | None = None
    start_lat: float
    start_lng: float
    end_lat: float
    end_lng: float
    polyline: str
    distance_km: float
    duration_min: float
    visibility: str = "public"


class RouteUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    visibility: str | None = None


class CommentCreate(BaseModel):
    route_id: uuid.UUID
    content: str


class VoteCreate(BaseModel):
    route_id: uuid.UUID
    value: int


class FavoriteCreate(BaseModel):
    route_id: uuid.UUID


class MessageResponse(BaseModel):
    message: str


class RouteResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: uuid.UUID
    author_id: uuid.UUID
    title: str
    description: str | None
    visibility: str


@router.get("/health", tags=["health"])
def healthcheck() -> dict[str, str]:
    return {"status": "ok"}


@router.post("/routes", response_model=RouteResponse, tags=["routes"])
def create_route(
    payload: RouteCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> Route:
    route = Route(
        author_id=current_user.id,
        title=payload.title,
        description=payload.description,
        start_lat=payload.start_lat,
        start_lng=payload.start_lng,
        end_lat=payload.end_lat,
        end_lng=payload.end_lng,
        polyline=payload.polyline,
        distance_km=payload.distance_km,
        duration_min=payload.duration_min,
        visibility=payload.visibility,
    )
    db.add(route)
    db.commit()
    db.refresh(route)
    return route


@router.put("/routes/{route_id}", response_model=RouteResponse, tags=["routes"])
def update_route(
    route_id: uuid.UUID,
    payload: RouteUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> Route:
    route = db.get(Route, route_id)
    if route is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Route not found")
    if route.author_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden")

    for field, value in payload.model_dump(exclude_unset=True).items():
        setattr(route, field, value)

    db.add(route)
    db.commit()
    db.refresh(route)
    return route


@router.post("/comments", response_model=MessageResponse, tags=["comments"])
def create_comment(
    payload: CommentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> MessageResponse:
    comment = Comment(route_id=payload.route_id, user_id=current_user.id, content=payload.content)
    db.add(comment)
    db.commit()
    return MessageResponse(message="Comment created")


@router.post("/votes", response_model=MessageResponse, tags=["votes"])
def create_or_update_vote(
    payload: VoteCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> MessageResponse:
    if payload.value not in (-1, 1):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Vote must be -1 or 1")

    vote = db.scalar(
        select(Vote).where(Vote.route_id == payload.route_id, Vote.user_id == current_user.id)
    )
    if vote is None:
        vote = Vote(route_id=payload.route_id, user_id=current_user.id, value=payload.value)
    else:
        vote.value = payload.value

    db.add(vote)
    db.commit()
    return MessageResponse(message="Vote saved")


@router.post("/favorites", response_model=MessageResponse, tags=["favorites"])
def create_favorite(
    payload: FavoriteCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
) -> MessageResponse:
    favorite = db.scalar(
        select(Favorite).where(Favorite.route_id == payload.route_id, Favorite.user_id == current_user.id)
    )
    if favorite is None:
        favorite = Favorite(route_id=payload.route_id, user_id=current_user.id)
        db.add(favorite)
        db.commit()

    return MessageResponse(message="Favorite saved")
