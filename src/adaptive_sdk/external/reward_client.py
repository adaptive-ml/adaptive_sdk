import httpx
from typing import Any
import asyncio
from httpx import Limits
import json


from .types import (
    Request,
    Response,
    ServerInfo,
    Turn,
    BatchedRequest,
    BatchedResponse,
)
from .constants import SCORE_PATH, BATCH_SCORE_PATH, VALIDATE_METADATA, INFO_PATH


class RewardClient:
    def __init__(
        self, base_url, max_connections: int = 32, timeout: float | None = None
    ):
        headers = dict()  # type: ignore[var-annotated]
        self._client = httpx.AsyncClient(
            headers=dict(),
            base_url=base_url,
            timeout=timeout,
            limits=Limits(max_connections=max_connections),
        )

    async def _post(self, path: str, json: str) -> httpx.Response:
        response = await self._client.post(path, json=json)
        response.raise_for_status()
        return response

    async def score(
        self, turns: list[Turn], metadata: dict[Any, Any], policy_tokenizer_key: str
    ) -> Response:
        request = Request(
            turns=turns, metadata=metadata, policy_tokenizer_key=policy_tokenizer_key
        )
        response = await self._post(SCORE_PATH, request.model_dump_json())
        return Response(**response.json())

    async def batch_score(self, requests: list[Request]) -> list[Response]:
        request = BatchedRequest(requests=requests)
        response = await self._post(BATCH_SCORE_PATH, request.model_dump_json())
        batched_response = BatchedResponse(**response.json())
        return batched_response.responses

    async def validate_metadata(self, metadata: dict[Any, Any]):
        response = await self._post(VALIDATE_METADATA, json.dumps(metadata))
        response.raise_for_status()

    async def info(self) -> ServerInfo:
        response = await self._client.get(INFO_PATH)
        response.raise_for_status()
        return ServerInfo(**response.json())


async def main():
    tasks = []
    for _ in range(1024):
        tasks.append(client.info())
    responses = await asyncio.gather(*tasks)


if __name__ == "__main__":

    client = RewardClient("http://0.0.0.0:8000")
    asyncio.run(main())
