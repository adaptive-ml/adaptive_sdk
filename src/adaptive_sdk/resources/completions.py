from uuid import UUID

from adaptive_sdk.base_client import BaseAsyncClient, BaseSyncClient
from adaptive_sdk.rest import rest_types
from adaptive_sdk.utils import convert_optional_UUID, _validate_response, get_full_model_path

from .base_resource import SyncAPIResource, AsyncAPIResource

ROUTE = "/completions"


class Completions(SyncAPIResource):
    def __init__(self, client: BaseSyncClient, use_case_key: str) -> None:
        super().__init__(client)
        self._use_case_key = use_case_key

    def create(
        self,
        prompt: str,
        model: str | None = None,
        stream: bool | None = None,
        session_id: str | UUID | None = None,
        user: str | UUID | None = None,
        ab_campaign: str | None = None,
        n: int | None = None,
        labels: dict[str, str] | None = None,
    ) -> rest_types.GenerateResponse:

        input = rest_types.GenerateInput(
            prompt=prompt,
            model=get_full_model_path(self._use_case_key, model),
            stream=stream,
            session_id=convert_optional_UUID(session_id),
            user=convert_optional_UUID(user),
            ab_campaign=ab_campaign,
            n=n,
            labels=labels,
        )
        r = self._rest_client.post(ROUTE, json=input.model_dump(exclude_none=True))
        _validate_response(r)
        return rest_types.GenerateResponse.model_validate(r.json())


class AsyncCompletions(AsyncAPIResource):
    def __init__(self, client: BaseAsyncClient, use_case_key: str) -> None:
        super().__init__(client)
        self._use_case_key = use_case_key

    async def create(
        self,
        prompt: str,
        model: str | None = None,
        stream: bool | None = None,
        session_id: str | UUID | None = None,
        user: str | UUID | None = None,
        ab_campaign: str | None = None,
        n: int | None = None,
        labels: dict[str, str] | None = None,
    ) -> rest_types.GenerateResponse:

        input = rest_types.GenerateInput(
            prompt=prompt,
            model=get_full_model_path(self._use_case_key, model),
            stream=stream,
            session_id=convert_optional_UUID(session_id),
            user=convert_optional_UUID(user),
            ab_campaign=ab_campaign,
            n=n,
            labels=labels,
        )
        r = await self._rest_client.post(ROUTE, json=input.model_dump(exclude_none=True))
        _validate_response(r)
        return rest_types.GenerateResponse.model_validate(r.json())
