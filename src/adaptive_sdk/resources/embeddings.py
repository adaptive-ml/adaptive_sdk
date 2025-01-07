from typing import Literal
from uuid import UUID

from adaptive_sdk.base_client import BaseAsyncClient, BaseSyncClient
from adaptive_sdk.rest import rest_types
from adaptive_sdk.utils import convert_optional_UUID, _validate_response, get_full_model_path

from .base_resource import SyncAPIResource, AsyncAPIResource

ROUTE = "/embeddings"


class Embeddings(SyncAPIResource):
    """
    Resource to interact with embeddings.
    """

    def __init__(self, client: BaseSyncClient, use_case_key: str) -> None:
        super().__init__(client)
        self._use_case_key = use_case_key

    def create(
        self,
        input: str,
        model: str | None = None,
        encoding_format: Literal["Float", "Base64"] = "Float",
        user: str | UUID | None = None,
    ) -> rest_types.EmbeddingsResponseList:
        """
        Creates embeddings inference request.

        Args:
            input: Input text to embed.
            model: Target model key for inference. If `None`, the requests will be routed to the use case's default model.
                Request will error if default model is not an embedding model.
            encoding_format: Encoding format of response.
            user: ID of user making the requests. If not `None`, will be logged as metadata for the request.
        """

        encoding_format_enum = rest_types.EmbeddingsEncodingFormat(encoding_format)
        emb_input = rest_types.GenerateEmbeddingsInput(
            input=input,
            model=get_full_model_path(self._use_case_key, model),
            encoding_format=encoding_format_enum,
            dimensions=None,
            user=convert_optional_UUID(user),
        )
        r = self._rest_client.post(
            ROUTE, data=emb_input.model_dump_json(exclude_none=True), headers={"Content-Type": "application/json"}  # type: ignore
        )
        _validate_response(r)
        return rest_types.EmbeddingsResponseList.model_validate(r.json())


class AsyncEmbeddings(AsyncAPIResource):
    """
    Resource to interact with embeddings.
    """

    def __init__(self, client: BaseAsyncClient, use_case_key: str) -> None:
        super().__init__(client)
        self._use_case_key = use_case_key

    async def create(
        self,
        input: str,
        model_key: str | None = None,
        encoding_format: Literal["Float", "Base64"] = "Float",
        user: str | UUID | None = None,
    ) -> rest_types.EmbeddingsResponseList:
        """
        Creates embeddings inference request.

        Args:
            input: Input text to embed.
            model: Target model key for inference. If `None`, the requests will be routed to the use case's default model.
                Request will error if default model is not an embedding model.
            encoding_format: Encoding format of response.
            user: ID of user making the requests. If not `None`, will be logged as metadata for the request.
        """
        encoding_format_enum = rest_types.EmbeddingsEncodingFormat(encoding_format)
        emb_input = rest_types.GenerateEmbeddingsInput(
            input=input,
            model=get_full_model_path(self._use_case_key, model_key),
            encoding_format=encoding_format_enum,
            dimensions=None,
            user=convert_optional_UUID(user),
        )
        r = await self._rest_client.post(
            ROUTE, data=emb_input.model_dump_json(exclude_none=True), headers={"Content-Type": "application/json"}  # type: ignore
        )
        _validate_response(r)
        return rest_types.EmbeddingsResponseList.model_validate(r.json())
