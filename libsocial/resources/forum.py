from typing import Literal, Union

from .._resource import SyncAPIResource, AsyncAPIResource
from ..models.forum import CategoryModel, DiscussionModel, CommentModel
from ..enums import Category


class Forum(SyncAPIResource):
    def get_discussions_category(
        self,
        category: Union[str, int, Category],
        *,
        page: int = 1,
        sort: Literal["newest", "updates", "popular"] = "newest",
    ) -> CategoryModel:
        if isinstance(category, Category):
            category = category.value

        data = self._get(
            "/api/forum/discussion",
            params={"category": category, "page": page, "sort": sort}
        ).json()
        return CategoryModel.from_dict(data)

    def get_discussion(self, discussion_id: int) -> DiscussionModel:
        data = self._get(f"/api/forum/discussion/{discussion_id}").json()
        return DiscussionModel.from_dict(data)

    def get_discussion_comments(
        self,
        discussion_id: int,
        *,
        page: int = 1
    ) -> CommentModel:
        data = self._get(
            "/api/forum/posts",
            params={"discussion_id": discussion_id, "page": page}
        ).json()
        return CommentModel.from_dict(data)


class AsyncForum(AsyncAPIResource):
    async def get_discussions_category(
        self,
        category: Union[str, int, Category],
        *,
        page: int = 1,
        sort: Literal["newest", "updates", "popular"] = "newest",
    ) -> CategoryModel:
        if isinstance(category, Category):
            category = category.value

        data = (await self._get(
            "/api/forum/discussion",
            params={"category": category, "page": page, "sort": sort}
        )).json()
        return CategoryModel.from_dict(data)

    async def get_discussion(self, discussion_id: int) -> DiscussionModel:
        data = (await self._get(f"/api/forum/discussion/{discussion_id}")).json()
        return DiscussionModel.from_dict(data)

    async def get_discussion_comments(
        self,
        discussion_id: int,
        *,
        page: int = 1
    ) -> CommentModel:
        data = (await self._get(
            "/api/forum/posts",
            params={"discussion_id": discussion_id, "page": page}
        )).json()
        return CommentModel.from_dict(data)
