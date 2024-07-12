from __future__ import annotations

from typing import Any, List, Optional

from pydantic import BaseModel


class Cover(BaseModel):
    filename: str
    thumbnail: str
    default: str
    md: str


class AgeRestriction(BaseModel):
    id: int
    label: str


class Type(BaseModel):
    id: int
    label: str


class Status(BaseModel):
    id: int
    label: str


class Media(BaseModel):
    id: int
    name: str
    rus_name: str
    eng_name: str
    slug: str
    slug_url: str
    cover: Cover
    ageRestriction: AgeRestriction
    site: int
    type: Type
    is_licensed: bool
    model: str
    status: Status
    releaseDateString: str


class Votes(BaseModel):
    up: int
    down: int
    user: Any


class Datum(BaseModel):
    id: int
    similar: str
    user_id: int
    media: Media
    votes: Votes


class SimilarModel(BaseModel):
    data: List[Datum]
