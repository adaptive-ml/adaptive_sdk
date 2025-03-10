from abc import ABC, abstractmethod
from fastapi import FastAPI, APIRouter
from fastapi.responses import JSONResponse
from fastapi import status
from typing import Callable, Any
from dataclasses import dataclass
import threading
import uvicorn
import time
import asyncio

from .types import Request, Response, ServerInfo, BatchedRequest, BatchedResponse
from .constants import SCORE_PATH, BATCH_SCORE_PATH, VALIDATE_METADATA, INFO_PATH


@dataclass
class Route:
    path: str
    endpoint: Callable[..., Any]
    methods: list[str]


class RewardServer(ABC):
    def __init__(
        self, port: int, blocking: bool = True, request_timeout_s: int = 3_600
    ):
        self.request_timeout_s = request_timeout_s
        self._setup_server(port, blocking)

    async def score_timeout(self, request: Request) -> Response:
        try:
            start_time = time.time()
            return await asyncio.wait_for(
                self.score(request), timeout=self.request_timeout_s
            )

        except asyncio.TimeoutError:
            process_time = time.time() - start_time
            return JSONResponse(  # type: ignore[return-value]
                {
                    "detail": "Request processing time excedeed limit",
                    "processing_time": process_time,
                    "timeout": self.request_timeout_s,
                },
                status_code=status.HTTP_504_GATEWAY_TIMEOUT,
            )

    @abstractmethod
    async def score(self, request: Request) -> Response: ...

    async def batch_score(self, requests: BatchedRequest) -> BatchedResponse:
        tasks = []
        for request in requests.requests:
            tasks.append(self.score_timeout(request))

        responses = await asyncio.gather(*tasks)
        return BatchedResponse(responses=responses)

    @abstractmethod
    async def validate_metadata(self, metadata: dict[Any, Any]): ...

    @abstractmethod
    async def info(self) -> ServerInfo: ...

    def _setup_server(self, port: int, blocking: bool):
        class ThreadServer(uvicorn.Server):
            """ "Easy to kill uvicorn server"""

            def run_in_thread(self):
                self.thread = threading.Thread(target=self.run, daemon=True)
                self.thread.start()

            def stop(self):
                self.should_exit = True
                self.thread.join()

        def get_routes() -> list[Route]:
            routes: list[Route] = []
            routes.append(Route(SCORE_PATH, self.score_timeout, methods=["POST"]))
            routes.append(Route(BATCH_SCORE_PATH, self.batch_score, methods=["POST"]))
            routes.append(Route(INFO_PATH, self.info, methods=["GET"]))
            routes.append(
                Route(VALIDATE_METADATA, self.validate_metadata, methods=["POST"])
            )
            return routes

        router = APIRouter()
        routes = get_routes()

        for route in routes:
            router.add_api_route(route.path, route.endpoint, methods=route.methods)

        app = FastAPI()
        app.include_router(router)

        config = uvicorn.Config(
            app,
            host="0.0.0.0",
            port=port,
            log_level="info",
            workers=8,
        )
        self.server = ThreadServer(config=config)

        if blocking:
            self.server.run()
        else:
            self.server.run_in_thread()


class MyRewardServer(RewardServer):
    def __init__(self, port=8000, blocking=True):
        super().__init__(port, blocking)

    async def score(self, request: Request) -> Response:
        raise NotImplementedError()

    async def validate_metadata(self, metadata: dict[Any, Any]):
        raise NotImplementedError()

    async def info(self) -> ServerInfo:
        return ServerInfo(
            version="1.0", name="My sevice", description="This is a nice description"
        )


if __name__ == "__main__":
    server = MyRewardServer()
