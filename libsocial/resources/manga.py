from urllib.parse import urlencode

from .._resource import SyncAPIResource, AsyncAPIResource
from ..models.manga import MangaPageModel, MangaInfoModel


def manga_info_fields() -> str:
    fields = [
        "background", "eng_name", "otherNames", "summary", "releaseDate",
        "type_id", "caution", "views", "close_view", "rate_avg", "rate",
        "genres", "tags", "teams", "franchise", "authors", "publisher",
        "userRating", "moderated", "metadata", "metadata.count",
        "metadata.close_comments", "manga_status_id", "chap_count",
        "status_id", "artists", "format"
    ]
    return urlencode([("fields[]", field) for field in fields])


class Manga(SyncAPIResource):
    base_url = "https://api.lib.social"

    def search(self, query: str, *, page: int = 1) -> MangaPageModel:
        data = self._get("/api/manga", params={"q": query, "page": page}).json()
        return MangaPageModel(**data)

    def get_page(self, page: int = 1) -> MangaPageModel:
        data = self._get("/api/manga", params={"page": page}).json()
        return MangaPageModel(**data)

    def get_manga(self, slug_url: str) -> MangaInfoModel:
        fields = manga_info_fields()
        data = self._get(f"/api/manga/{slug_url}?{fields}").json()
        return MangaInfoModel(**data)


class AsyncManga(AsyncAPIResource):
    base_url = "https://api.lib.social"

    async def search(self, query: str, *, page: int = 1) -> MangaPageModel:
        data = (await self._get("/api/manga", params={"q": query, "page": page})).json()
        return MangaPageModel(**data)

    async def get_page(self, page: int = 1) -> MangaPageModel:
        data = (await self._get("/api/manga", params={"page": page})).json()
        return MangaPageModel(**data)

    async def get_manga(self, slug_url: str) -> MangaInfoModel:
        fields = manga_info_fields()
        data = (await self._get(f"/api/manga/{slug_url}?{fields}")).json()
        return MangaInfoModel(**data)
