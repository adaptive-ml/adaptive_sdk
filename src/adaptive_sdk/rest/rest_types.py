from __future__ import annotations
from enum import Enum
from typing import Annotated, Any, Dict, List, Optional, Union
from uuid import UUID
from pydantic import Field, RootModel
from .base_model import BaseModel


class AddInteractionsResponse(BaseModel):
    """@public"""

    completion_id: UUID
    session_id: UUID
    feedback_ids: List[UUID]


class ChatChoiceMessage(BaseModel):
    """@public"""

    id: str
    role: str
    content: str


class ChatMessage(BaseModel):
    """@public"""

    content: str
    role: str
    name: Optional[str] = None
    completion_id: Optional[UUID] = None
    metadata: Optional[Any] = None


class ComparisonOutput(BaseModel):
    """@public"""

    comparison_id: UUID


class ComparisonTie(Enum):
    """@public"""

    good = "good"
    bad = "bad"


class Delta(BaseModel):
    """@public"""

    delta: ChatChoiceMessage
    index: Annotated[int, Field(ge=0)]
    completion_id: str


class EmbeddingsEncodingFormat(Enum):
    """@public"""

    float = "Float"
    base64 = "Base64"


class FeedbackOutput(BaseModel):
    """@public"""

    feedback_id: UUID


class FeedbackReason(Enum):
    """@public"""

    toxicity = "Toxicity"
    factuality = "Factuality"
    style = "Style"
    wrong_answer = "WrongAnswer"


class GenerateChoice(BaseModel):
    """@public"""

    index: Annotated[int, Field(ge=0)]
    text: str
    completion_id: str
    model: str
    finish_reason: Optional[str] = None


class GenerateEmbeddingsInput(BaseModel):
    """@public"""

    input: str
    model: Annotated[
        str,
        Field(
            description="can be of the form '{use_case}/{model}' or '{use_case}'. In the latter it will use the default model"
        ),
    ]
    encoding_format: Optional[EmbeddingsEncodingFormat] = None
    dimensions: Annotated[Optional[int], Field(ge=0)] = None
    user: Optional[UUID] = None
    session_id: Optional[UUID] = None


class GenerateParameters(BaseModel):
    """@public"""

    stop: Optional[List[str]] = None
    max_tokens: Annotated[Optional[int], Field(ge=0)] = None
    temperature: Optional[float] = None
    top_p: Optional[float] = None


class InteractionFeedback(BaseModel):
    """@public"""

    metric: Annotated[
        str, Field(description="id or key of the entity", examples=["76d1fab3-214c-47ef-bb04-16270639bf89"])
    ]
    value: Annotated[
        Any,
        Field(
            description="If the metric is Bool, accepts `0`, `1`, `true` or `false`\nIf the metric is Scalar, accepts number"
        ),
    ]
    reason: Optional[str] = None
    details: Optional[str] = None
    created_at: Optional[str] = None


class OutcomeOutput(BaseModel):
    """@public"""

    outcome_id: UUID


class StreamOptions(BaseModel):
    """@public"""

    include_usage: Optional[bool] = None


class Timestamp(RootModel[float]):
    """@public"""

    root: Annotated[float, Field(description="Unix Timestamp in milliseconds", examples=["1720712536911"])]


class Usage(BaseModel):
    """@public"""

    completion_tokens: Annotated[int, Field(ge=0)]
    prompt_tokens: Annotated[int, Field(ge=0)]
    total_tokens: Annotated[int, Field(ge=0)]


class AddFeedbackRequest(BaseModel):
    """@public"""

    value: Annotated[
        Any,
        Field(
            description="If the metric is Bool, accepts `0`, `1`, `true` or `false`\nIf the metric is Scalar, accepts number"
        ),
    ]
    completion_id: UUID
    metric: Annotated[
        str, Field(description="id or key of the entity", examples=["76d1fab3-214c-47ef-bb04-16270639bf89"])
    ]
    user_id: Optional[UUID] = None
    reason: Optional[FeedbackReason] = None
    details: Optional[str] = None


class AddInteractionsRequest(BaseModel):
    """@public"""

    model_service: Optional[str] = None
    use_case: Annotated[
        str, Field(description="id or key of the entity", examples=["76d1fab3-214c-47ef-bb04-16270639bf89"])
    ]
    prompt: Optional[str] = None
    messages: Optional[List[ChatMessage]] = None
    completion: str
    feedbacks: Optional[List[InteractionFeedback]] = None
    user: Optional[UUID] = None
    session_id: Optional[UUID] = None
    created_at: Optional[str] = None
    ab_campaign: Optional[str] = None
    labels: Optional[Dict[str, str]] = None


class AddOutcomeRequest(BaseModel):
    """@public"""

    value: Annotated[
        Any,
        Field(
            description="If the metric is Bool, accepts `0`, `1`, `true` or `false`\nIf the metric is Scalar, accepts number"
        ),
    ]
    metric: Annotated[
        str, Field(description="id or key of the entity", examples=["76d1fab3-214c-47ef-bb04-16270639bf89"])
    ]
    session_id: UUID
    user_id: Optional[UUID] = None


class ChatChoice(BaseModel):
    """@public"""

    index: Annotated[int, Field(ge=0)]
    message: ChatChoiceMessage
    finish_reason: Optional[str] = None
    completion_id: str
    model: str


class ChatInput(GenerateParameters):
    """@public"""

    messages: List[ChatMessage]
    model: Annotated[
        str,
        Field(
            description="can be of the form `{use_case}/{model}` or `{use_case}`. In the latter it will use the default model"
        ),
    ]
    stream: Optional[bool] = None
    stream_options: Optional[StreamOptions] = None
    session_id: Optional[UUID] = None
    user: Optional[UUID] = None
    ab_campaign: Optional[str] = None
    n: Annotated[Optional[int], Field(ge=0)] = None
    labels: Optional[Dict[str, str]] = None
    metadata: Optional[Dict[str, str]] = None
    system_prompt_args: Annotated[
        Optional[Dict[str, Any]], Field(description="Will be used to render system prompt template")
    ] = None
    tags: Optional[List[str]] = None


class ChatResponse(BaseModel):
    """@public"""

    id: str
    created: Annotated[float, Field(description="Unix Timestamp in seconds", examples=["1720712536"])]
    choices: List[ChatChoice]
    session_id: UUID
    usage: Usage


class ChatResponseChunk(BaseModel):
    """@public"""

    id: str
    choices: List[Delta]
    created: Annotated[float, Field(description="Unix Timestamp in seconds", examples=["1720712536"])]
    session_id: UUID
    usage: Optional[Usage] = None


class CompletionIdOrText1(BaseModel):
    """@public"""

    text: str
    model: Annotated[
        str, Field(description="id or key of the entity", examples=["76d1fab3-214c-47ef-bb04-16270639bf89"])
    ]


class EmbeddingResponse(BaseModel):
    """@public"""

    index: Annotated[int, Field(ge=0)]
    embedding: Union[List[float], str]


class EmbeddingsResponseList(BaseModel):
    """@public"""

    data: List[EmbeddingResponse]
    usage: Optional[Usage] = None


class GenerateInput(GenerateParameters):
    """@public"""

    prompt: str
    model: Annotated[
        str,
        Field(
            description="can be of the form `{use_case}/{model}` or `{use_case}`. In the latter it will use the default model"
        ),
    ]
    stream: Optional[bool] = None
    session_id: Optional[UUID] = None
    user: Optional[UUID] = None
    ab_campaign: Optional[str] = None
    n: Annotated[Optional[int], Field(ge=0)] = None
    metadata: Optional[Dict[str, str]] = None
    labels: Optional[Dict[str, str]] = None
    tags: Optional[List[str]] = None


class GenerateResponse(BaseModel):
    """@public"""

    id: str
    created: Annotated[float, Field(description="Unix Timestamp in seconds", examples=["1720712536"])]
    choices: List[GenerateChoice]
    usage: Usage


class AddComparisonRequest(BaseModel):
    """@public"""

    metric: Annotated[
        str, Field(description="id or key of the entity", examples=["76d1fab3-214c-47ef-bb04-16270639bf89"])
    ]
    prompt: Annotated[
        Optional[str],
        Field(description="Required (or messages) when using raw text for completion, ignored if using ids"),
    ] = None
    messages: Annotated[
        Optional[List[ChatMessage]],
        Field(description="Required (or prompt) when using raw text for completion, ignored if using ids"),
    ] = None
    preferred_completion: Union[UUID, CompletionIdOrText1]
    other_completion: Union[UUID, CompletionIdOrText1]
    tied: Optional[ComparisonTie] = None
    use_case: Optional[str] = None
    user_id: Optional[UUID] = None
