from copy import deepcopy
import humps
from typing import List, Dict, Literal
from uuid import UUID

from adaptive_sdk import input_types
from adaptive_sdk.base_client import BaseAsyncClient, BaseSyncClient
from adaptive_sdk.graphql_client import (
    CompletionGroupBy,
    CursorPageInput,
    ListCompletionsFilterInput,
    OrderPair,
    ListInteractionsCompletions,
    ListGroupedInteractionsCompletionsGrouped,
    DescribeInteractionCompletion,
)
from adaptive_sdk.graphql_client.base_model import UNSET
from adaptive_sdk.rest import rest_types
from adaptive_sdk.utils import convert_optional_UUID, _validate_response

from .base_resource import SyncAPIResource, AsyncAPIResource

ROUTE = "/interactions"


def _prepare_add_interactions_inputs(
    messages: list[dict[str, str]] | None,
    prompt: str | None,
    feedbacks: list[input_types.InteractionFeedbackDict] | None,
):
    if (messages is None) == (prompt is None):
        raise ValueError("One of prompt or completion must be passed, but not both")

    input_messages = (
        [rest_types.ChatMessage(role=m.get("role"), content=m.get("content")) for m in messages] if messages else None  # type: ignore
    )
    input_feedbacks = (
        [
            rest_types.InteractionFeedback(
                metric=i.get("feedback_key"),
                value=i.get("value"),
                details=i.get("details"),
            )
            for i in feedbacks
        ]
        if feedbacks
        else None
    )
    return input_messages, input_feedbacks


class Interactions(SyncAPIResource):
    """
    Resource to interact with interactions.
    """

    def __init__(self, client: BaseSyncClient, use_case_key: str) -> None:
        super().__init__(client)
        self._use_case_key = use_case_key

    def create(
        self,
        model: str,
        completion: str,
        prompt: str | None = None,
        messages: list[dict[str, str]] | None = None,
        feedbacks: list[input_types.InteractionFeedbackDict] | None = None,
        user: str | UUID | None = None,
        session_id: str | UUID | None = None,
        ab_campaign: str | None = None,
        labels: dict[str, str] | None = None,
        created_at: str | None = None,
    ) -> rest_types.AddInteractionsResponse:
        """
        Create/log an interaction.

        Args:
            model: Model key.
            completion: Model completion.
            prompt: Input text prompt.
            messages: Input chat messages, each dict should have keys `role` and `content`.
            feedbacks: List of feedbacks, each dict should with keys `feedback_key`, `value` and optional(`details`).
            user: ID of user making the request. If not `None`, will be logged as metadata for the interaction.
            ab_campaign: AB test key. If set, provided `feedbacks` will count towards AB test results.
            labels: Key-value pairs of interaction labels.
            created_at: Timestamp of interaction creation or ingestion.
        """

        input_messages, input_feedbacks = _prepare_add_interactions_inputs(messages, prompt, feedbacks)

        input = rest_types.AddInteractionsRequest(
            model_service=model,
            use_case=self._use_case_key,
            completion=completion,
            prompt=prompt,
            messages=input_messages,
            feedbacks=input_feedbacks,
            user=convert_optional_UUID(user),
            session_id=convert_optional_UUID(session_id),
            ab_campaign=ab_campaign,
            labels=labels,
            created_at=created_at,
        )
        r = self._rest_client.post(ROUTE, json=input.model_dump(exclude_none=True))
        _validate_response(r)
        return rest_types.AddInteractionsResponse.model_validate(r.json())

    def list(
        self,
        order: List[input_types.Order] | None = None,
        filters: input_types.ListCompletionsFilterInput | None = None,
        page: input_types.CursorPageInput | None = None,
        group_by: Literal["model", "prompt"] | None = None,
    ) -> ListInteractionsCompletions | ListGroupedInteractionsCompletionsGrouped:
        """
        List interactions in client's use case.

        Args:
            order: Ordering of results.
            filters: List filters.
            page: Paging config.
            group_by: Retrieve interactions grouped by selected dimension.

        """
        new_filters = {} if filters is None else deepcopy(filters)
        order = [] if order is None else order
        new_page = {} if page is None else page

        new_filters = humps.camelize(new_filters)
        new_order = humps.camelize(order)
        new_page = humps.camelize(new_page)

        if new_filters.get("timerange"):
            new_filters["timerange"]["from"] = new_filters["timerange"]["from_"]  # type: ignore
            del new_filters["timerange"]["from_"]  # type: ignore

        new_filters.update({"useCase": self._use_case_key})  # type: ignore
        order_inputs = [OrderPair.model_validate(o) for o in new_order] if new_order else UNSET
        if group_by:
            return self._gql_client.list_grouped_interactions(
                filter=ListCompletionsFilterInput.model_validate(new_filters),
                group_by=CompletionGroupBy(group_by.upper()),
                page=CursorPageInput.model_validate(new_page),
                order=order_inputs,
            ).completions_grouped
        else:
            return self._gql_client.list_interactions(
                filter=ListCompletionsFilterInput.model_validate(new_filters),
                page=CursorPageInput.model_validate(new_page),
                order=order_inputs,
            ).completions

    def get(
        self,
        completion_id: str,
    ) -> DescribeInteractionCompletion | None:
        """
        Get the details for one specific interaction.

        Args:
            completion_id: The ID of the completion.
        """
        return self._gql_client.describe_interaction(use_case=self._use_case_key, id=completion_id).completion


class AsyncInteractions(AsyncAPIResource):
    """
    Resource to interact with interactions.
    """

    def __init__(self, client: BaseAsyncClient, use_case_key: str) -> None:
        super().__init__(client)
        self._use_case_key = use_case_key

    async def create(
        self,
        model: str,
        completion: str,
        prompt: str | None = None,
        messages: list[dict[str, str]] | None = None,
        feedbacks: list[input_types.InteractionFeedbackDict] | None = None,
        user: str | UUID | None = None,
        session_id: str | UUID | None = None,
        ab_campaign: str | None = None,
        labels: dict[str, str] | None = None,
    ) -> rest_types.AddInteractionsResponse:
        """
        Create/log an interaction.

        Args:
            model: Model key.
            completion: Model completion.
            prompt: Input text prompt.
            messages: Input chat messages, each dict should have keys `role` and `content`.
            feedbacks: List of feedbacks, each dict should with keys `feedback_key`, `value` and optional(`details`).
            user: ID of user making the request. If not `None`, will be logged as metadata for the interaction.
            ab_campaign: AB test key. If set, provided `feedbacks` will count towards AB test results.
            labels: Key-value pairs of interaction labels.
            created_at: Timestamp of interaction creation or ingestion.
        """
        input_messages, input_feedbacks = _prepare_add_interactions_inputs(messages, prompt, feedbacks)

        input = rest_types.AddInteractionsRequest(
            model_service=model,
            use_case=self._use_case_key,
            completion=completion,
            prompt=prompt,
            messages=input_messages,
            feedbacks=input_feedbacks,
            user=convert_optional_UUID(user),
            session_id=convert_optional_UUID(session_id),
            ab_campaign=ab_campaign,
            labels=labels,
        )
        r = await self._rest_client.post(ROUTE, json=input.model_dump(exclude_none=True))
        _validate_response(r)
        return rest_types.AddInteractionsResponse.model_validate(r.json())

    async def list(
        self,
        order: List[input_types.Order] | None = None,
        filters: input_types.ListCompletionsFilterInput | None = None,
        page: input_types.CursorPageInput | None = None,
        group_by: Literal["model", "prompt"] | None = None,
    ) -> ListInteractionsCompletions | ListGroupedInteractionsCompletionsGrouped:
        """
        List interactions in client's use case.

        Args:
            order: Ordering of results.
            filters: List filters.
            page: Paging config.
            group_by: Retrieve interactions grouped by selected dimension.

        """
        new_filters = {} if filters is None else deepcopy(filters)
        order = [] if order is None else order
        new_page = {} if page is None else page

        new_filters = humps.camelize(new_filters)
        new_order = humps.camelize(order)
        new_page = humps.camelize(new_page)

        if new_filters.get("timerange"):
            new_filters["timerange"]["from"] = new_filters["timerange"]["from_"]  # type: ignore
            del new_filters["timerange"]["from_"]  # type: ignore

        new_filters.update({"useCase": self._use_case_key})  # type: ignore
        order_inputs = [OrderPair.model_validate(o) for o in new_order] if new_order else UNSET
        if group_by:
            result = await self._gql_client.list_grouped_interactions(
                filter=ListCompletionsFilterInput.model_validate(filters),
                group_by=CompletionGroupBy(group_by.upper()),
                page=CursorPageInput.model_validate(page),
                order=order_inputs,
            )
            return result.completions_grouped
        else:
            result = await self._gql_client.list_interactions(
                filter=ListCompletionsFilterInput.model_validate(filters),
                page=CursorPageInput.model_validate(page),
                order=order_inputs,
            )
            return result.completions

    async def get(
        self,
        completion_id: str,
    ) -> DescribeInteractionCompletion | None:
        """
        Get the details for one specific interaction.

        Args:
            completion_id: The ID of the completion.
        """
        result = await self._gql_client.describe_interaction(use_case=self._use_case_key, id=completion_id)
        return result.completion
