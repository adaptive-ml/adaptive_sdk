import httpx
from typing import Any
from httpx import Limits
from jsonschema import validate, ValidationError as JsonSchemaValidationError
from websockets.asyncio.client import connect, ClientConnection
import asyncio
import json
from loguru import logger

from adaptive_sdk.external.reward_types import (
    BatchedMetadataValidationResponse,
    MetadataValidationResponse,
    Request,
    Turn,
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


async def read_task(client: ClientConnection, responses: dict[int, Response | asyncio.Event]):
    while True:
        try:
            msg = await client.recv()
            obj = json.loads(msg)
            response = Response.model_validate(obj)
            response_id: int = response.id  # type: ignore
            event: asyncio.Event = responses.pop(response_id)  # type: ignore
            responses[response_id] = response
            event.set()
        except Exception as e:
            logger.error(f"{e}")
            break


class RewardClient:
    def __init__(self, base_url: str, max_connections: int = 32, timeout: float | None = None):
        headers = dict()  # type: ignore[var-annotated]
        self.base_url = base_url.removeprefix("http://").removeprefix("https://")
        self._client = httpx.AsyncClient(
            headers=dict(),
            base_url=f"http://{self.base_url}",
            timeout=timeout,
            limits=Limits(max_connections=max_connections),
        )
        self._metadata_json_schema: None | dict[str, Any] = None
        self.use_websocket = False

    async def connect_websocket(self):
        self.use_websocket = True
        self.ws_client: ClientConnection = await connect(f"ws://{self.base_url}")
        self.ws_responses: dict[int, Response | asyncio.Event] = dict()
        self.read_task = asyncio.create_task(read_task(self.ws_client, self.ws_responses))
        self.request_id = 0
        return self

    async def _post(self, path: str, data: dict) -> httpx.Response:
        response = await self._client.post(path, json=data)
        response.raise_for_status()
        return response

    async def _ws_post(self, req: Request) -> Response:
        request_id = self.request_id
        self.request_id += 1
        req.id = request_id
        event = asyncio.Event()
        self.ws_responses[request_id] = event
        await self.ws_client.send(req.model_dump_json())
        await event.wait()
        response: Response = self.ws_responses.pop(request_id)  # type: ignore
        assert response.id == request_id
        return response

    async def score(self, req: Request) -> Response:
        if not self.use_websocket:
            response = await self._post(SCORE_PATH, req.model_dump())
            return Response(**response.json())
        else:
            return await self._ws_post(req)

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


# async def main():
#     # client = RewardClient("0.0.0.0:50056")
#     client = await RewardClient("0.0.0.0:50056").connect_websocket()
#     tasks = []
#     for _ in range(1024):
#         task = client.score(Request(turns=[Turn(role="assistant", content="hello")]))
#         tasks.append(task)
#     await asyncio.gather(*tasks)


# if __name__ == "__main__":
#     asyncio.run(main(args.rank))
