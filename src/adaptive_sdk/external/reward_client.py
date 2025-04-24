import httpx
from typing import Any
from httpx import Limits
from jsonschema import validate, ValidationError as JsonSchemaValidationError

from adaptive_sdk.external.reward_types import (
    BatchedMetadataValidationResponse,
    MetadataValidationResponse,
    Request,
    Response,
    ServerInfo,
    BatchedRequest,
    BatchedResponse,
)
from adaptive_sdk.external.constants import (
    METADATA_SCHEMA_PATH,
    SCORE_PATH,
    BATCH_SCORE_PATH,
    INFO_PATH,
)


class RewardClient:
    def __init__(self, base_url, max_connections: int = 32, timeout: float | None = None):
        headers = dict()  # type: ignore[var-annotated]
        self._client = httpx.AsyncClient(
            headers=dict(),
            base_url=base_url,
            timeout=timeout,
            limits=Limits(max_connections=max_connections),
        )
        self._metadata_json_schema: None | dict[str, Any] = None

    async def _post(self, path: str, data: dict) -> httpx.Response:
        response = await self._client.post(path, json=data)
        response.raise_for_status()
        return response

    async def score(self, req: Request) -> Response:
        response = await self._post(SCORE_PATH, req.model_dump())
        return Response(**response.json())

    async def batch_score(self, requests: list[Request]) -> list[Response]:
        response = await self._post(BATCH_SCORE_PATH, BatchedRequest(requests=requests).model_dump())
        batched_response = BatchedResponse(**response.json())
        return batched_response.responses

    async def validate_metadata(self, metadata: dict[Any, Any]):
        if self._metadata_json_schema is None:
            response = await self._client.get(METADATA_SCHEMA_PATH)
            self._metadata_json_schema = response.json()

        try:
            validate(instance=metadata, schema=self._metadata_json_schema)  # type: ignore
            return MetadataValidationResponse(is_valid=True)
        except JsonSchemaValidationError as e:
            return MetadataValidationResponse(is_valid=False, error_message=str(e))

    async def batch_validate_metadata(
        self, list_of_metadata: list[dict[Any, Any]]
    ) -> BatchedMetadataValidationResponse:
        return BatchedMetadataValidationResponse(
            responses=[await self.validate_metadata(metadata) for metadata in list_of_metadata]
        )

    async def info(self) -> ServerInfo:
        response = await self._client.get(INFO_PATH)
        response.raise_for_status()
        return ServerInfo(**response.json())

    def blocking_info(self) -> ServerInfo:
        return ServerInfo(**httpx.get(self._client.base_url.join(INFO_PATH), timeout=self._client.timeout).json())

    def blocking_batch_score(self, requests: list[Request]) -> list[Response]:
        request = BatchedRequest(requests=requests)
        response = BatchedResponse(
            **httpx.post(
                self._client.base_url.join(BATCH_SCORE_PATH),
                json=request.model_dump(),
                timeout=self._client.timeout,
            ).json()
        )
        return response.responses
