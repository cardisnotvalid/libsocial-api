from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class BodyItem:
    insert: str


@dataclass(frozen=True)
class Comment:
    id: int
    post_id: int
    user_id: int
    username: str
    avatar: str
    body: List[BodyItem]
    chatter_discussion_id: int
    created_at: str
    updated_at: str
    deleted_at: str = field(default=None)
    reply_user_id: int = field(default=None)
    reply_username: str = field(default=None)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "BodyItem":
        return cls(body=[BodyItem(**x) for x in data.pop("body").get("ops")], **data)


@dataclass(frozen=True)
class CommentModel:
    current_page: int
    data: List[Comment]
    first_page_url: str
    from_: int
    to: int
    path: str
    per_page: int
    next_page_url: str = field(default=None)
    prev_page_url: str = field(default=None)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "CommentModel":
        return cls(
            from_=data.pop("from"),
            data=[Comment.from_dict(x) for x in data.pop("data")],
            **data,
        )
