from __future__ import annotations

from typing import Any, List, Optional

from pydantic import BaseModel


class RelatedType(BaseModel):
    id: int
    label: str


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
    model: str
    status: Status
    releaseDateString: str
    shiki_rate: Optional[Any] = None


class Datum(BaseModel):
    order: int
    related_type: RelatedType
    media: Media


class RelationModel(BaseModel):
    data: List[Datum]
