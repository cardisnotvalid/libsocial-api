from __future__ import annotations

from typing import Any, List, Optional

from pydantic import BaseModel, Field


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


class Rating(BaseModel):
    average: str
    averageFormated: str
    votes: int
    votesFormated: str
    user: int


class Status(BaseModel):
    id: int
    label: str


class Datum(BaseModel):
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
    rating: Rating
    model: str
    status: Status
    releaseDateString: str


class Links(BaseModel):
    first: str
    last: Any
    prev: Any
    next: Any


class Meta(BaseModel):
    current_page: int
    from_: int = Field(..., alias="from")
    path: str
    per_page: int
    to: int
    page: int
    has_next_page: bool
    seed: str


class MangaPageModel(BaseModel):
    data: List[Datum]
    links: Links
    meta: Meta
