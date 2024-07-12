from __future__ import annotations

from typing import Any, List

from dataclasses import dataclass


@dataclass
class Cover:
    filename: str
    thumbnail: str
    default: str
    md: str


@dataclass
class Background:
    filename: str
    url: str


@dataclass
class AgeRestriction:
    id: int
    label: str


@dataclass
class Type:
    id: int
    label: str


@dataclass
class Views:
    total: int
    short: str
    formatted: str

    @classmethod
    def loads(cls, data: Data[str, Any]) -> Views:
        return cls(formatted=data.pop("formated"), **data)


@dataclass
class Rating:
    average: str
    average_formatted: str
    votes: int
    votes_formatted: str
    user: int

    @classmethod
    def loads(cls, data: Dict[str, Any]) -> Rating:
        return cls(
            average_formatted=data.pop("averageFormated"),
            votes_formatted=data.pop("votesFormated"),
            **data,
        )


@dataclass
class Moderated:
    id: int
    label: str


@dataclass
class Details:
    branch_id: int
    is_active: bool
    subscriptions_count: Optional[int]


@dataclass
class Team:
    id: int
    slug: str
    slug_url: str
    model: str
    name: str
    cover: Cover
    details: Details

    @classmethod
    def loads(cls, data: Dict[str, Any]) -> Team:
        return cls(
            cover=Cover(**data.pop("cover")),
            details=Details(**data.pop("details")),
            **data,
        )


@dataclass
class Genre:
    id: int
    name: str
    adult: bool
    alert: bool


@dataclass
class Tag:
    id: int
    name: str
    adult: bool
    alert: bool


@dataclass
class Subscription:
    is_subscribed: bool
    source_type: str
    source_id: int
    relation: Any


@dataclass
class Publisher:
    id: int
    slug: str
    slug_url: str
    model: str
    name: str
    rus_name: Any
    cover: Cover
    subscription: Subscription

    @classmethod
    def loads(cls, data: Dict[str, Any]) -> Publisher:
        return cls(
            cover=Cover(**data.pop("cover")),
            subscription=Subscription(**data.pop("subscription")),
            **data,
        )


@dataclass
class Franchise:
    id: int
    slug: str
    slug_url: str
    model: str
    name: str


@dataclass
class Author:
    id: int
    slug: str
    slug_url: str
    model: str
    name: str
    rus_name: Any
    alt_name: Any
    cover: Cover
    subscription: Subscription
    confirmed: Any
    user_id: int

    @classmethod
    def loads(cls, data: Dict[str, Any]) -> Author:
        return cls(
            cover=Cover(**data.pop("cover")),
            subscription=Subscription(**data.pop("subscription")),
            **data,
        )


@dataclass
class Characters:
    main: int
    supporting: int

    @classmethod
    def loads(cls, data: Dict[str, int]) -> Characters:
        return cls(main=data["Main"], supporting=data["Supporting"])


@dataclass
class Reviews:
    neutral: int
    positive: int
    negative: int
    all: int


@dataclass
class Count:
    branches: int
    characters: Characters
    reviews: Reviews
    relations: int
    people: int
    covers: int

    @classmethod
    def loads(cls, data: Dict[str, Any]) -> Count:
        return cls(
            characters=Characters.loads(data.pop("characters")),
            reviews=Reviews(**data.pop("reviews")),
            **data,
        )


@dataclass
class Metadata:
    close_comments: int
    count: Count

    @classmethod
    def loads(cls, data: Dict[str, Any]) -> Metadata:
        return cls(count=Count.loads(data.pop("count")), **data)


@dataclass
class Status:
    id: int
    label: str


@dataclass
class ItemsCount:
    uploaded: int
    total: int


@dataclass
class ScanlateStatus:
    id: int
    label: str


@dataclass
class Artist:
    id: int
    slug: str
    slug_url: str
    model: str
    name: str
    rus_name: Any
    alt_name: Any
    cover: Cover
    subscription: Subscription
    confirmed: Any
    user_id: int

    @classmethod
    def loads(cls, data: Dict[str, Any]) -> Artist:
        return cls(
            cover=Cover(**data.pop("cover")),
            subscription=Subscription(**data.pop("subscription")),
            **data,
        )


@dataclass
class Data:
    id: int
    name: str
    rus_name: str
    eng_name: str
    other_names: List[str]
    slug: str
    slug_url: str
    cover: Cover
    background: Background
    age_restriction: AgeRestriction
    site: int
    type: Type
    summary: str
    close_view: int
    release_date: str
    views: Views
    rating: Rating
    is_licensed: bool
    moderated: Moderated
    teams: List[Team]
    genres: List[Genre]
    tags: List[Tag]
    publisher: List[Publisher]
    franchise: List[Franchise]
    authors: List[Author]
    metadata: Metadata
    model: str
    status: Status
    items_count: ItemsCount
    scanlate_status: ScanlateStatus
    artists: List[Artist]
    format: List
    release_date_string: str

    @classmethod
    def loads(cls, data: Dict[str, Any]) -> Data:
        return cls(
            cover=Cover(**data.pop("cover")),
            background=Background(**data.pop("background")),
            age_restriction=AgeRestriction(**data.pop("ageRestriction")),
            type=Type(**data.pop("type")),
            views=Views.loads(data.pop("views")),
            rating=Rating.loads(data.pop("rating")),
            moderated=Moderated(**data.pop("moderated")),
            teams=[Team.loads(item) for item in data.pop("teams")],
            genres=[Genre(**item) for item in data.pop("genres")],
            tags=[Tag(**item) for item in data.pop("tags")],
            publisher=[Publisher.loads(item) for item in data.pop("publisher")],
            franchise=[Franchise(**item) for item in data.pop("franchise")],
            authors=[Author.loads(item) for item in data.pop("authors")],
            metadata=Metadata.loads(data.pop("metadata")),
            status=Status(**data.pop("status")),
            items_count=ItemsCount(**data.pop("items_count")),
            scanlate_status=ScanlateStatus(**data.pop("scanlateStatus")),
            artists=[Artist.loads(item) for item in data.pop("artists")],
            other_names=data.pop("otherNames"),
            release_date=data.pop("releaseDate"),
            release_date_string=data.pop("releaseDateString"),
            **data,
        )


@dataclass
class Meta:
    country: str


@dataclass
class MangaInfoModel:
    data: Data
    meta: Meta

    @classmethod
    def loads(cls, data: Dict[str, Any]) -> MangaInfoModel:
        return cls(data=Data.loads(data["data"]), meta=Meta(**data["meta"]))
