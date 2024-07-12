from __future__ import annotations

from typing import Any, List, Optional

from pydantic import BaseModel, Field


class Datum(BaseModel):
    id: int
    chatter_category_id: int
    title: str
    user_id: int
    source_id: Optional[int]
    source_type: Optional[str]
    sticky: int
    locked: int
    views: int
    answered: int
    last_reply_at: str
    created_at: str
    updated_at: str
    deleted_at: Any
    yaoi: int
    category_id: int
    category_name: str
    category_slug: str
    category_color: str
    username: str
    avatar: str
    body: str


class CategoryModel(BaseModel):
    current_page: int
    data: List[Datum]
    first_page_url: str
    from_: int = Field(..., alias="from")
    next_page_url: str
    path: str
    per_page: int
    prev_page_url: Any
    to: int
