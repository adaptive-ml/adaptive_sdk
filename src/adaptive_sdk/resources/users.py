from __future__ import annotations
from typing import TYPE_CHECKING, Sequence, List

from adaptive_sdk.graphql_client import (
    UserData,
    TeamMemberSet,
    UpdateUserSetTeamMember,
    ListTeamsTeams,
)

from .base_resource import SyncAPIResource, AsyncAPIResource, UseCaseResource

if TYPE_CHECKING:
    from adaptive_sdk.client import Adaptive, AsyncAdaptive


class Users(SyncAPIResource, UseCaseResource):  # type: ignore[misc]
    """
    Resource to manage users and permissions.
    """

    def __init__(self, client: Adaptive) -> None:
        SyncAPIResource.__init__(self, client)
        UseCaseResource.__init__(self, client)

    def me(self) -> UserData | None:
        """
        Get details of current user.
        """
        return self._gql_client.me().me

    def list(self) -> Sequence[UserData]:
        """
        List all users registered to Adaptive deployment.
        """
        return self._gql_client.list_users().users

    def update(self, email: str, team: str, role: str) -> UpdateUserSetTeamMember:
        """
        Update team and role for user.

        Args:
            email: User email.
            team: Key of team to which user will be added to.
            role: Assigned role

        """
        input = TeamMemberSet(user=email, team=team, role=role)
        return self._gql_client.update_user(input).set_team_member


class AsyncUsers(AsyncAPIResource, UseCaseResource):  # type: ignore[misc]
    """
    Resource to manage users and permissions.
    """

    def __init__(self, client: AsyncAdaptive) -> None:
        AsyncAPIResource.__init__(self, client)
        UseCaseResource.__init__(self, client)

    async def me(self) -> UserData | None:
        """
        Get details of current user.
        """
        result = await self._gql_client.me()
        return result.me

    async def list(self) -> Sequence[UserData]:
        """
        List all users registered to Adaptive deployment.
        """
        result = await self._gql_client.list_users()
        return result.users

    async def update(self, email: str, team: str, role: str) -> UpdateUserSetTeamMember:
        """
        Update team and role for user.

        Args:
            email: User email.
            team: Key of team to which user will be added to.
            role: Assigned role

        """
        input = TeamMemberSet(user=email, team=team, role=role)
        result = await self._gql_client.update_user(input)
        return result.set_team_member
