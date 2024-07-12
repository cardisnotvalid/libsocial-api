from typing import Union, Dict, Any

import httpx
from httpx import URL

from . import resources
from ._base_client import SyncAPIClient, AsyncAPIClient


class LibSocial(SyncAPIClient):
    manga: resources.Manga
    forum: resources.Forum

    def __init__(self) -> None:
        super().__init__()

        self.manga = resources.Manga(self)
        self.forum = resources.Forum(self)

    @property
    def default_category(self) -> Dict[str, Any]:
        return {"site_id[]": 1}


class AsyncLibSocial(AsyncAPIClient):
    manga: resources.AsyncManga
    forum: resources.AsyncForum

    def __init__(self) -> None:
        super().__init__()

        self.manga = resources.AsyncManga(self)
        self.forum = resources.AsyncForum(self)

    @property
    def default_category(self) -> Dict[str, Any]:
        return {"site_id[]": 1}
