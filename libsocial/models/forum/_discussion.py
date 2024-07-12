from __future__ import annotations

from typing import Any, List, Optional

from pydantic import BaseModel


class Covers(BaseModel):
    default: str
    thumbnail: str


class Relation(BaseModel):
    id: int
    cover: str
    slug: str
    value: str
    name: Optional[str] = None
    covers: Optional[Covers] = None
    coverImage: Optional[str] = None
    coverImageThumbnail: Optional[str] = None
    href: str
    title_status_id: Optional[int] = None


class Discussion(BaseModel):
    id: int
    chatter_category_id: int
    title: str
    user_id: int
    source_id: Optional[int] = None
    source_type: Optional[str] = None
    sticky: int
    locked: int
    views: int
    answered: int
    last_reply_at: str
    created_at: str
    updated_at: str
    deleted_at: Optional[str] = None
    yaoi: int
    username: str
    avatar: str
    category_id: int
    category_name: str
    category_slug: str
    category_color: str
    category_icon: str
    notification: Optional[bool] = None
    relation: Optional[Relation] = None


class Op(BaseModel):
    insert: str


class Body(BaseModel):
    ops: List[Op]


class Post(BaseModel):
    id: int
    post_id: int
    chatter_discussion_id: int
    user_id: int
    body: Body
    created_at: str
    updated_at: str
    deleted_at: Optional[str] = None


class DiscussionModel(BaseModel):
    discussion: Discussion
    post: Post
