from __future__ import annotations

from typing import Optional, Dict, List, Any

from dataclasses import dataclass


@dataclass(frozen=True)
class Cover:
    filename: str
    thumbnail: str
    default: str
    md: str


@dataclass(frozen=True)
class AgeRestriction:
    id: int
    label: str


@dataclass(frozen=True)
class Type:
    id: int
    label: str


@dataclass(frozen=True)
class Rating:
    average: str
    averageFormated: str
    votes: int
    votesFormated: str
    user: int


@dataclass(frozen=True)
class Status:
    id: int
    label: str


@dataclass(frozen=True)
class DataItem:
    id: int
    name: str
    rus_name: str
    eng_name: str
    slug: str
    slug_url: str
    cover: _Cover
    ageRestriction: _AgeRestriction
    site: int
    type: _Type
    rating: _Rating
    is_licensed: bool
    model: str
    status: _Status
    releaseDateString: str

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "Data":
        return DataItem(
            cover=Cover(**data.pop("cover")),
            ageRestriction=AgeRestriction(**data.pop("ageRestriction")),
            type=Type(**data.pop("type")),
            rating=Rating(**data.pop("rating")),
            status=Status(**data.pop("status")),
            **data,
        )

    @classmethod
    def from_list(cls, data: List[Dict[str, Any]]) -> List["Data"]:
        return [cls.from_dict(item) for item in data]


@dataclass(frozen=True)
class Links:
    first: Optional[str] = None
    last: Optional[str] = None
    prev: Optional[str] = None
    next: Optional[str] = None


@dataclass(frozen=True)
class Meta:
    current_page: int
    from_: int
    path: str
    per_page: int
    to: int
    page: int
    has_next_page: bool
    seed: str

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "Meta":
        return Meta(from_=data.pop("from"), **data)


@dataclass(frozen=True)
class MangaPageModel:
    data: DataItem
    links: Links
    meta: Meta

    @staticmethod
    def loads(data: List[Dict[str, Any]]) -> "Model":
        return MangaPageModel(
            data=DataItem.from_list(data["data"]),
            links=Links(**data["links"]),
            meta=Meta.from_dict(data["meta"]),
        )
