from __future__ import annotations

from typing import Optional, Dict, List

from dataclasses import dataclass, field


@dataclass(frozen=True)
class CategoryItem:
    id: int
    user_id: int
    username: str
    avatar: str
    title: str
    body: str
    views: int
    answered: int
    locked: int
    sticky: int
    yaoi: int
    category_color: str
    category_id: int
    category_name: str
    category_slug: str
    chatter_category_id: int
    created_at: str
    updated_at: str
    last_reply_at: str
    deleted_at: str = field(default=None)
    source_id: int = field(default=None)
    source_type: str = field(default=None)


@dataclass(frozen=True)
class CategoryModel:
    current_page: int
    data: List[CategoryItem]
    first_page_url: str
    from_: int
    path: str
    per_page: int
    to: int
    prev_page_url: str = field(default=None)
    next_page_url: str = field(default=None)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "DiscussionModel":
        return cls(
            from_=data.pop("from"),
            data=[CategoryItem(**x) for x in data.pop("data")],
            **data,
        )
