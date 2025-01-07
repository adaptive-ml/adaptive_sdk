from typing import Sequence

from adaptive_sdk.base_client import BaseAsyncClient, BaseSyncClient
from adaptive_sdk.graphql_client import UseCaseCreate, UseCaseSettingsInput, UseCaseData

from .base_resource import SyncAPIResource, AsyncAPIResource


class UseCasesAdmin(SyncAPIResource):
    """
    Resource to administrate use cases.
    """

    def create(
        self,
        key: str,
        name: str | None = None,
        description: str | None = None,
        team: str | None = None,
    ) -> UseCaseData:
        """
        Create new use case.

        Args:
            key: Use case key.
            name: Human-readable use case name which will be rendered in the UI.
                If not set, will be the same as `key`.
            description: Description of model which will be rendered in the UI.
        """

        input = UseCaseCreate(
            name=name if name else key,
            key=key,
            description=description,
            team=team,
            settings=UseCaseSettingsInput(defaultMetric=None),
        )
        return self._gql_client.create_use_case(input).create_use_case

    def list(self) -> Sequence[UseCaseData]:
        """
        List all use cases.
        """
        return self._gql_client.list_use_cases().use_cases

    def get(self, use_case: str) -> UseCaseData | None:
        """
        Get details for a use case.

        Args:
            use_case: Use case key.
        """
        return self._gql_client.describe_use_case(use_case).use_case


class UseCase(SyncAPIResource):
    """
    Resource to interact with use cases.
    """

    def __init__(self, client: BaseSyncClient, use_case_key: str) -> None:
        super().__init__(client)
        self._use_case_key = use_case_key

    def get(self) -> UseCaseData | None:
        """
        Get details for the client's use case.
        """
        return self._gql_client.describe_use_case(self._use_case_key).use_case


class AsyncUseCasesAdmin(AsyncAPIResource):
    """
    Resource to administrate use cases.
    """

    async def create(
        self,
        key: str,
        name: str | None = None,
        description: str | None = None,
        team: str | None = None,
        default_feedback_key: str | None = None,
    ) -> UseCaseData:
        """
        Create new use case.

        Args:
            key: Use case key.
            name: Human-readable use case name which will be rendered in the UI.
                If not set, will be the same as `key`.
            description: Description of model which will be rendered in the UI.
        """
        input = UseCaseCreate(
            name=name if name else key,
            key=key,
            description=description,
            team=team,
            settings=UseCaseSettingsInput(defaultMetric=default_feedback_key),
        )
        result = await self._gql_client.create_use_case(input)
        return result.create_use_case

    async def list(self) -> Sequence[UseCaseData]:
        """
        List all use cases.
        """
        result = await self._gql_client.list_use_cases()
        return result.use_cases

    async def get(self, use_case: str) -> UseCaseData | None:
        """
        Get details for a use case.

        Args:
            use_case: Use case key.
        """
        result = await self._gql_client.describe_use_case(use_case)
        return result.use_case


class AsyncUseCase(AsyncAPIResource):
    """
    Resource to interact with use cases.
    """

    def __init__(self, client: BaseAsyncClient, use_case_key: str) -> None:
        super().__init__(client)
        self._use_case_key = use_case_key

    async def get(self) -> UseCaseData | None:
        """
        Get details for the client's use case.
        """
        result = await self._gql_client.describe_use_case(self._use_case_key)
        return result.use_case
