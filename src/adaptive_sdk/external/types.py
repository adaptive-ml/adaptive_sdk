from typing import Any
from .base_model import BaseModel


class Turn(BaseModel):
    """@public"""

    role: str
    content: str


class Request(BaseModel):
    """@public"""

    turns: list[Turn]
    metadata: dict[Any, Any]
    policy_tokenizer_key: str


class BatchedRequest(BaseModel):
    """@public"""

    requests: list[Request]


class Response(BaseModel):
    """@public"""

    reward: list[float]
    mask: list[bool]


class BatchedResponse(BaseModel):
    """@public"""

    responses: list[Response]


class ServerInfo(BaseModel):
    """@public"""

    version: str
    name: str
    description: str
