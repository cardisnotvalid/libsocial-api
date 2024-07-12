from urllib.parse import urlencode

from .._resource import SyncAPIResource, AsyncAPIResource
from ..models.manga import PageModel, InfoModel, RelationModel, SimilarModel, CharacterModel


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

    def search(self, query: str, *, page: int = 1) -> PageModel:
        data = self._get("/api/manga", params={"q": query, "page": page}).json()
        return PageModel(**data)

    def get_page(self, page: int = 1) -> PageModel:
        data = self._get("/api/manga", params={"page": page}).json()
        return PageModel(**data)

    def get_manga(self, slug_url: str) -> InfoModel:
        fields = manga_info_fields()
        data = self._get(f"/api/manga/{slug_url}?{fields}").json()
        return InfoModel(**data)

    def get_relations(self, slug_url: str) -> RelationModel:
        data = self._get(f"/api/manga/{slug_url}/relations").json()
        return RelationModel(**data)

    def get_similar(self, slug_url: str) -> SimilarModel:
        data = self._get(f"/api/manga/{slug_url}/similar").json()
        return SimilarModel(**data)

    def get_characters(self, manga_id: int, *, limit: int = 30, page: int = 1) -> CharacterModel:
        params = {"media_id": manga_id, "page": page, "limit": limit, "media_type": "manga"}
        data = self._get("/api/character", params=params).json()
        return CharacterModel(**data)


class AsyncManga(AsyncAPIResource):
    base_url = "https://api.lib.social"

    async def search(self, query: str, *, page: int = 1) -> PageModel:
        data = (await self._get("/api/manga", params={"q": query, "page": page})).json()
        return PageModel(**data)

    async def get_page(self, page: int = 1) -> PageModel:
        data = (await self._get("/api/manga", params={"page": page})).json()
        return PageModel(**data)

    async def get_manga(self, slug_url: str) -> InfoModel:
        fields = manga_info_fields()
        data = (await self._get(f"/api/manga/{slug_url}?{fields}")).json()
        return InfoModel(**data)

    async def get_relations(self, slug_url: str) -> RelationModel:
        data = (await self._get(f"/api/manga/{slug_url}/relations")).json()
        return RelationModel(**data)

    async def get_similar(self, slug_url: str) -> SimilarModel:
        data = (await self._get(f"/api/manga/{slug_url}/similar")).json()
        return SimilarModel(**data)

    async def get_characters(self, manga_id: int, *, limit: int = 30, page: int = 1) -> CharacterModel:
        params = {"media_id": manga_id, "page": page, "limit": limit, "media_type": "manga"}
        data = (await self._get("/api/character", params=params)).json()
        return CharacterModel(**data)
