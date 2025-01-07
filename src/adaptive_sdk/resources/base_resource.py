from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from adaptive_sdk.base_client import BaseAsyncClient, BaseSyncClient


class SyncAPIResource:
    def __init__(self, client: BaseSyncClient) -> None:
        self._client = client
        self._rest_client = client._rest_client
        self._gql_client = client._gql_client


class AsyncAPIResource:
    def __init__(self, client: BaseAsyncClient) -> None:
        self._client = client
        self._rest_client = client._rest_client
        self._gql_client = client._gql_client
