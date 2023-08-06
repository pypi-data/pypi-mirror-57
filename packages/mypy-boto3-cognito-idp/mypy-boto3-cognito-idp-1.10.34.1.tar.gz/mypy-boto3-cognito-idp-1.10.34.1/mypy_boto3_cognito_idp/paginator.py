"Main interface for cognito-idp service Paginators"
from __future__ import annotations

from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_cognito_idp.type_defs import (
    AdminListGroupsForUserResponseTypeDef,
    AdminListUserAuthEventsResponseTypeDef,
    ListGroupsResponseTypeDef,
    ListIdentityProvidersResponseTypeDef,
    ListResourceServersResponseTypeDef,
    ListUserPoolClientsResponseTypeDef,
    ListUserPoolsResponseTypeDef,
    ListUsersInGroupResponseTypeDef,
    ListUsersResponseTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = (
    "AdminListGroupsForUserPaginator",
    "AdminListUserAuthEventsPaginator",
    "ListGroupsPaginator",
    "ListIdentityProvidersPaginator",
    "ListResourceServersPaginator",
    "ListUserPoolClientsPaginator",
    "ListUserPoolsPaginator",
    "ListUsersPaginator",
    "ListUsersInGroupPaginator",
)


class AdminListGroupsForUserPaginator(Boto3Paginator):
    """
    [Paginator.AdminListGroupsForUser documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.AdminListGroupsForUser)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, Username: str, UserPoolId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> AdminListGroupsForUserResponseTypeDef:
        """
        [AdminListGroupsForUser.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.AdminListGroupsForUser.paginate)
        """


class AdminListUserAuthEventsPaginator(Boto3Paginator):
    """
    [Paginator.AdminListUserAuthEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.AdminListUserAuthEvents)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, UserPoolId: str, Username: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> AdminListUserAuthEventsResponseTypeDef:
        """
        [AdminListUserAuthEvents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.AdminListUserAuthEvents.paginate)
        """


class ListGroupsPaginator(Boto3Paginator):
    """
    [Paginator.ListGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.ListGroups)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, UserPoolId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListGroupsResponseTypeDef:
        """
        [ListGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.ListGroups.paginate)
        """


class ListIdentityProvidersPaginator(Boto3Paginator):
    """
    [Paginator.ListIdentityProviders documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.ListIdentityProviders)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, UserPoolId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListIdentityProvidersResponseTypeDef:
        """
        [ListIdentityProviders.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.ListIdentityProviders.paginate)
        """


class ListResourceServersPaginator(Boto3Paginator):
    """
    [Paginator.ListResourceServers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.ListResourceServers)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, UserPoolId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListResourceServersResponseTypeDef:
        """
        [ListResourceServers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.ListResourceServers.paginate)
        """


class ListUserPoolClientsPaginator(Boto3Paginator):
    """
    [Paginator.ListUserPoolClients documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.ListUserPoolClients)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, UserPoolId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListUserPoolClientsResponseTypeDef:
        """
        [ListUserPoolClients.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.ListUserPoolClients.paginate)
        """


class ListUserPoolsPaginator(Boto3Paginator):
    """
    [Paginator.ListUserPools documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.ListUserPools)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListUserPoolsResponseTypeDef:
        """
        [ListUserPools.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.ListUserPools.paginate)
        """


class ListUsersPaginator(Boto3Paginator):
    """
    [Paginator.ListUsers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.ListUsers)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        UserPoolId: str,
        AttributesToGet: List[str] = None,
        Filter: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> ListUsersResponseTypeDef:
        """
        [ListUsers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.ListUsers.paginate)
        """


class ListUsersInGroupPaginator(Boto3Paginator):
    """
    [Paginator.ListUsersInGroup documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.ListUsersInGroup)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, UserPoolId: str, GroupName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListUsersInGroupResponseTypeDef:
        """
        [ListUsersInGroup.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cognito-idp.html#CognitoIdentityProvider.Paginator.ListUsersInGroup.paginate)
        """
