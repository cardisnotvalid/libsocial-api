from __future__ import annotations

from typing import Any, List, Optional

from pydantic import BaseModel, Field


class Cover(BaseModel):
    filename: str
    thumbnail: str
    default: str
    md: str


class Subscription(BaseModel):
    is_subscribed: bool
    source_type: str
    source_id: int
    relation: Any


class Position(BaseModel):
    id: str
    label: str


class Details(BaseModel):
    order: int
    position: Position


class Datum(BaseModel):
    id: int
    slug: str
    slug_url: str
    model: str
    cover: Cover
    name: str
    rus_name: str
    subscription: Subscription
    details: Details


class Links(BaseModel):
    first: str
    last: Any
    prev: Any
    next: str


class Meta(BaseModel):
    current_page: int
    from_: int = Field(..., alias='from')
    path: str
    per_page: str
    to: int


class CharacterModel(BaseModel):
    data: List[Datum]
    links: Links
    meta: Meta
