from __future__ import annotations

from typing import Any, List, Optional

from pydantic import BaseModel


class Cover(BaseModel):
    filename: str
    thumbnail: str
    default: str
    md: str


class Background(BaseModel):
    filename: Optional[str] = None
    url: str


class AgeRestriction(BaseModel):
    id: int
    label: str


class Type(BaseModel):
    id: int
    label: str


class Views(BaseModel):
    total: int
    short: str
    formated: str


class Rating(BaseModel):
    average: str
    averageFormated: str
    votes: int
    votesFormated: str
    user: int


class Moderated(BaseModel):
    id: int
    label: str


class Cover(BaseModel):
    filename: Optional[str]
    thumbnail: str
    default: str
    md: str


class Details(BaseModel):
    branch_id: Optional[int] = None
    is_active: bool
    subscriptions_count: Any


class Team(BaseModel):
    id: int
    slug: str
    slug_url: str
    model: str
    name: str
    cover: Cover
    details: Details


class Genre(BaseModel):
    id: int
    name: str
    adult: bool
    alert: bool


class Tag(BaseModel):
    id: int
    name: str
    adult: bool
    alert: bool


class Subscription(BaseModel):
    is_subscribed: bool
    source_type: str
    source_id: int
    relation: Any


class PublisherItem(BaseModel):
    id: int
    slug: str
    slug_url: str
    model: str
    name: str
    rus_name: Any
    cover: Cover
    subscription: Subscription


class Author(BaseModel):
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


class Characters(BaseModel):
    Main: int
    Supporting: int


class Reviews(BaseModel):
    neutral: int
    positive: int
    negative: int
    all: int


class Count(BaseModel):
    branches: int
    characters: Characters
    reviews: Reviews
    relations: int
    people: int
    covers: int


class Metadata(BaseModel):
    close_comments: int
    count: Count


class Status(BaseModel):
    id: int
    label: str


class ItemsCount(BaseModel):
    uploaded: int
    total: int


class ScanlateStatus(BaseModel):
    id: int
    label: str


class Artist(BaseModel):
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


class Pivot(BaseModel):
    manga_id: int
    format_id: int


class FormatItem(BaseModel):
    id: int
    name: str
    pivot: Pivot


class Data(BaseModel):
    id: int
    name: str
    rus_name: str
    eng_name: str
    otherNames: List[str]
    slug: str
    slug_url: str
    cover: Cover
    background: Background
    ageRestriction: AgeRestriction
    site: int
    type: Type
    summary: str
    close_view: int
    releaseDate: str
    views: Views
    rating: Rating
    is_licensed: bool
    moderated: Moderated
    teams: List[Team]
    genres: List[Genre]
    tags: List[Tag]
    publisher: List[PublisherItem]
    franchise: List
    authors: List[Author]
    metadata: Metadata
    model: str
    status: Status
    items_count: ItemsCount
    scanlateStatus: ScanlateStatus
    artists: List[Artist]
    format: List[FormatItem]
    releaseDateString: str


class Meta(BaseModel):
    country: str


class InfoModel(BaseModel):
    data: Data
    meta: Meta
