from typing import TypeVar, Generic, Union, Dict, Any

import httpx
from httpx import URL, Request, Response


HttpxClientT = TypeVar("HttpxClientT", bound=[httpx.Client, httpx.AsyncClient])


class BaseClient(Generic[HttpxClientT]):
    _client: HttpxClientT

    def _prepare_params(self, params: Dict[str, Any]) -> Dict[str, Any]:
        return {**self.default_category, **params}

    def _build_request(
        self,
        method: str,
        base_url: Union[str, URL],
        path: Union[str, URL],
        **kwargs
    ) -> Request:
        url = URL(base_url).join(path)
        params = self._prepare_params(kwargs.pop("params", {}))
        return self._client.build_request(method=method, url=url, params=params, **kwargs)

    @property
    def default_category(self) -> Dict[str, Any]:
        return {}

    @property
    def default_headers(self) -> Dict[str, str]:
        return {"Accept": "application/json", "Content-Type": "application/json"}


class SyncAPIClient(BaseClient[httpx.Client]):
    _client: httpx.Client

    def __init__(self) -> None:
        super().__init__()

        self._client = httpx.Client()

    def close(self) -> None:
        if hasattr(self, "_client"):
            self._client.close()

    def __enter__(self) -> "SyncAPIClient":
        return self

    def __exit__(self, *args) -> None:
        self.close()

    def _request(
        self,
        method: str,
        base_url: Union[str, URL],
        path: Union[str, URL],
        **kwargs
    ) -> Response:
        request = self._build_request(method, base_url, path, **kwargs)
        return self._client.send(request)

    def get(
        self,
        base_url: Union[str, URL],
        path: Union[str, URL],
        **kwargs
    ) -> Response:
        return self._request("GET", base_url, path, **kwargs)

    def post(
        self,
        base_url: Union[str, URL],
        path: Union[str, URL],
        **kwargs
    ) -> Response:
        return self._request("POST", base_url, path, **kwargs)


class AsyncAPIClient(BaseClient[httpx.AsyncClient]):
    _client: httpx.AsyncClient

    def __init__(self) -> None
        super().__init__()

        self._client = httpx.AsyncClient()

    async def close(self) -> None:
        if hasattr(self, "_client"):
            await self._client.aclose()

    async def __aenter__(self) -> "AsyncAPIClient":
        return self

    async def __aexit__(self, *args) -> None:
        await self.close()

    async def _request(
        self,
        method: str,
        base_url: Union[str, URL],
        path: Union[str, URL],
        **kwargs
    ) -> Response:
        request = self._build_request(method, base_url, path, **kwargs)
        return await self._client.send(request)

    async def get(
        self,
        base_url: Union[str, URL],
        path: Union[str, URL],
        **kwargs
    ) -> Response:
        return await self._request("GET", base_url, path, **kwargs)

    async def post(
        self,
        base_url: Union[str, URL],
        path: Union[str, URL],
        **kwargs
    ) -> Response:
        return await self._request("POST", base_url, path, **kwargs)
