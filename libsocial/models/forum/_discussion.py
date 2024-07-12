from __future__ import annotations

from typing import Dict, Any

from dataclasses import dataclass, field


@dataclass(frozen=True)
class Covers:
    default: str
    thumbnail: str


@dataclass(frozen=True)
class Relation:
    id: int
    value: str
    name: str
    slug: str
    cover: str
    cover_image: str
    cover_thumbnail: str
    covers: Covers
    href: str
    title_status_id: int = field(default=None)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Relation":
        return cls(
            cover_image=data.pop("coverImage"),
            cover_thumbnail=data.pop("coverImageThumbnail"),
            covers=Covers(**data.pop("covers")),
            **data
        ) if data else None


@dataclass(frozen=True)
class Discussion:
    id: int
    user_id: int
    username: str
    avatar: str
    title: str
    views: int
    answered: int
    locked: int
    sticky: int
    yaoi: int
    category_id: int
    category_name: str
    chatter_category_id: int
    category_slug: str
    category_icon: str
    category_color: str
    created_at: str
    updated_at: str
    last_reply_at: str
    relation: Relation = field(default=None)
    deleted_at: str = field(default=None)
    source_id: int = field(default=None)
    source_type: str = field(default=None)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Post":
        return cls(relation=Relation.from_dict(data.pop("relation")), **data)


@dataclass(frozen=True)
class BodyItem:
    insert: str


@dataclass(frozen=True)
class Post:
    id: int
    post_id: int
    user_id: int
    chatter_discussion_id: int
    body: List[BodyItem]
    created_at: str
    updated_at: str
    deleted_at: str = field(default=None)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Post":
        return cls(body=[BodyItem(**x) for x in data.pop("body").get("ops")], **data)


@dataclass(frozen=True)
class DiscussionModel:
    discussion: Discussion
    post: Post

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "DiscussionModel":
        return cls(
            discussion=Discussion.from_dict(data["discussion"]),
            post=Post.from_dict(data["post"]),
        )
