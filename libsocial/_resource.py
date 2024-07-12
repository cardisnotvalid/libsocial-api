from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._client import LibSocial, AsyncLibSocial


class SyncAPIResource:
    _client: LibSocial

    def __init__(self, client: LibSocial, base_url: str) -> None:
        self._client = client
        self._client.base_url = base_url

        self._get = client.get
        self._post = client.post


class AsyncAPIResource:
    _client: AsyncLibSocial

    def __init__(self, client: AsyncLibSocial, base_url: str) -> None:
        self._client = client
        self._client.base_url = base_url

        self._get = client.get
        self._post = client.post
