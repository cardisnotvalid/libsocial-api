from __future__ import annotations

from typing import TYPE_CHECKING, Union

from httpx import URL, Response

if TYPE_CHECKING:
    from ._client import LibSocial, AsyncLibSocial


class SyncAPIResource:
    _client: LibSocial
    base_url: str

    def __init__(self, client: LibSocial) -> None:
        self._client = client

    def _get(self, path: Union[str, URL], **kwargs) -> Response:
        return self._client.get(self.base_url, path, **kwargs)

    def _post(self, path: Union[str, URL], **kwargs) -> Response:
        return self._client.post(self.base_url, path, **kwargs)


class AsyncAPIResource:
    _client: AsyncLibSocial
    base_url: str

    def __init__(self, client: AsyncLibSocial) -> None:
        self._client = client

    async def _get(self, path: Union[str, URL], **kwargs) -> Response:
        return await self._client.get(self.base_url, path, **kwargs)

    async def _post(self, path: Union[str, URL], **kwargs) -> Response:
        return await self._client.post(self.base_url, path, **kwargs)
