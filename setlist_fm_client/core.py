import os
import sys
import typing
from typing import TypeVar

import httpx

if sys.version_info < (3, 8):  # pragma: no cover
    from typing_extensions import Final
else:
    from typing import Final

BASE_URL: Final = "https://api.setlist.fm/rest/1.0"
SETLIST_FM_API_KEY_VAR_NAME: Final = "SETLIST_FM_API_KEY"

SerializedType = TypeVar("SerializedType")


class SetlistFmClient(httpx.Client):
    def __init__(self, *args, api_key: str = None, **kwargs):
        self.api_key = api_key or os.getenv(SETLIST_FM_API_KEY_VAR_NAME)
        super().__init__(*args, base_url=BASE_URL, **kwargs)

    def request(self, *args, **kwargs):
        return super().request(*args, **kwargs)


class AsyncSetlistFmClient(httpx.AsyncClient):
    def __init__(self, *args, api_key: str = None, **kwargs):
        self.api_key = api_key or os.getenv(SETLIST_FM_API_KEY_VAR_NAME)
        super().__init__(*args, base_url=BASE_URL, **kwargs)

    async def request(self, *args, **kwargs):
        response = await super().request(*args, **kwargs)
        return response


def _build_headers(
    accept: str,
    api_key: typing.Optional[str],
    client: typing.Union[AsyncSetlistFmClient, SetlistFmClient],
    **kwargs,
) -> typing.Dict[str, str]:
    if accept is None:
        raise ValueError("'accept' cannot be `None`.  It should be 'application/json' or 'application/xml'.")

    headers = kwargs.pop("headers", dict())
    if headers is None:
        headers = dict()

    if api_key is not None:
        # use api key from func
        headers["x-api-key"] = api_key
    else:
        # use api key from env var
        headers["x-api-key"] = client.api_key

    if headers.get("x-api-key") is None:
        raise ValueError(f"Must pass in api key as 'api_key' kwarg or set {SETLIST_FM_API_KEY_VAR_NAME!r} env var")

    headers["Accept"] = accept

    return headers


def get(
    *args, model: typing.Type[SerializedType] = None, api_key: str = None, accept: str = "application/json", **kwargs
) -> typing.Union[httpx.Response, SerializedType]:
    with SetlistFmClient() as client:
        headers = _build_headers(accept, api_key, client)
        response = client.get(*args, headers=headers, **kwargs)
    if model:
        response.raise_for_status()
        return model(**response.json())
    return response


async def async_get(
    *args, model: typing.Type[SerializedType] = None, api_key: str = None, accept: str = "application/json", **kwargs
) -> typing.Union[httpx.Response, SerializedType]:
    async with AsyncSetlistFmClient() as client:
        headers = _build_headers(accept, api_key, client)
        response = await client.get(*args, headers=headers, **kwargs)
    if model:
        response.raise_for_status()
        return model(**response.json())
    return response


def build_params(**params: typing.Union[int, str, None]) -> typing.Dict[str, typing.Union[int, str]]:
    return {k: v for k, v in params.items() if v is not None}
