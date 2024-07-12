from __future__ import annotations

from typing import Any, List, Optional

from pydantic import BaseModel


class Cover(BaseModel):
    filename: str
    thumbnail: str
    default: str
    md: str


class Team(BaseModel):
    id: int
    slug: str
    slug_url: str
    model: str
    name: str
    cover: Cover


class User(BaseModel):
    username: str
    id: int


class Branch(BaseModel):
    id: int
    branch_id: Any
    created_at: str
    teams: List[Team]
    user: User


class Datum(BaseModel):
    id: int
    index: int
    item_number: int
    volume: str
    number: str
    number_secondary: str
    name: str
    branches_count: int
    branches: List[Branch]


class ChapterModel(BaseModel):
    data: List[Datum]
