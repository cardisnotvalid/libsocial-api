from __future__ import annotations

from typing import Any, List, Optional

from pydantic import BaseModel, Field


class Op(BaseModel):
    insert: str


class Body(BaseModel):
    ops: List[Op]


class Datum(BaseModel):
    id: int
    post_id: int
    chatter_discussion_id: int
    user_id: int
    body: Body
    created_at: str
    updated_at: str
    deleted_at: Any
    username: str
    avatar: str
    reply_username: Optional[str] = None
    reply_user_id: Optional[int] = None


class CommentModel(BaseModel):
    current_page: int
    data: List[Datum]
    first_page_url: str
    from_: Optional[int] = Field(None, alias="from")
    next_page_url: Any
    path: str
    per_page: int
    prev_page_url: Any
    to: Optional[int] = None
