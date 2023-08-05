"Main interface for cognito-idp service Paginators"
from __future__ import annotations

from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_cognito_idp.type_defs import (
    AdminListGroupsForUserPaginatePaginationConfigTypeDef,
    AdminListGroupsForUserPaginateResponseTypeDef,
    AdminListUserAuthEventsPaginatePaginationConfigTypeDef,
    AdminListUserAuthEventsPaginateResponseTypeDef,
    ListGroupsPaginatePaginationConfigTypeDef,
    ListGroupsPaginateResponseTypeDef,
    ListIdentityProvidersPaginatePaginationConfigTypeDef,
    ListIdentityProvidersPaginateResponseTypeDef,
    ListResourceServersPaginatePaginationConfigTypeDef,
    ListResourceServersPaginateResponseTypeDef,
    ListUserPoolClientsPaginatePaginationConfigTypeDef,
    ListUserPoolClientsPaginateResponseTypeDef,
    ListUserPoolsPaginatePaginationConfigTypeDef,
    ListUserPoolsPaginateResponseTypeDef,
    ListUsersInGroupPaginatePaginationConfigTypeDef,
    ListUsersInGroupPaginateResponseTypeDef,
    ListUsersPaginatePaginationConfigTypeDef,
    ListUsersPaginateResponseTypeDef,
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
    Paginator for `admin_list_groups_for_user`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Username: str,
        UserPoolId: str,
        PaginationConfig: AdminListGroupsForUserPaginatePaginationConfigTypeDef = None,
    ) -> AdminListGroupsForUserPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`CognitoIdentityProvider.Client.admin_list_groups_for_user`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/AdminListGroupsForUser>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              Username='string',
              UserPoolId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type Username: string
        :param Username: **[REQUIRED]**

          The username for the user.

        :type UserPoolId: string
        :param UserPoolId: **[REQUIRED]**

          The user pool ID for the user pool.

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than
            the value specified in max-items then a ``NextToken`` will be provided in the output
            that you can use to resume pagination.

          - **PageSize** *(integer) --*

            The size of each page.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Groups': [
                    {
                        'GroupName': 'string',
                        'UserPoolId': 'string',
                        'Description': 'string',
                        'RoleArn': 'string',
                        'Precedence': 123,
                        'LastModifiedDate': datetime(2015, 1, 1),
                        'CreationDate': datetime(2015, 1, 1)
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **Groups** *(list) --*

              The groups that the user belongs to.

              - *(dict) --*

                The group type.

                - **GroupName** *(string) --*

                  The name of the group.

                - **UserPoolId** *(string) --*

                  The user pool ID for the user pool.

                - **Description** *(string) --*

                  A string containing the description of the group.

                - **RoleArn** *(string) --*

                  The role ARN for the group.

                - **Precedence** *(integer) --*

                  A nonnegative integer value that specifies the precedence of this group relative
                  to the other groups that a user can belong to in the user pool. If a user belongs
                  to two or more groups, it is the group with the highest precedence whose role ARN
                  will be used in the ``cognito:roles`` and ``cognito:preferred_role`` claims in the
                  user's tokens. Groups with higher ``Precedence`` values take precedence over
                  groups with lower ``Precedence`` values or with null ``Precedence`` values.

                  Two groups can have the same ``Precedence`` value. If this happens, neither group
                  takes precedence over the other. If two groups with the same ``Precedence`` have
                  the same role ARN, that role is used in the ``cognito:preferred_role`` claim in
                  tokens for users in each group. If the two groups have different role ARNs, the
                  ``cognito:preferred_role`` claim is not set in users' tokens.

                  The default ``Precedence`` value is null.

                - **LastModifiedDate** *(datetime) --*

                  The date the group was last modified.

                - **CreationDate** *(datetime) --*

                  The date the group was created.
        """


class AdminListUserAuthEventsPaginator(Boto3Paginator):
    """
    Paginator for `admin_list_user_auth_events`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        UserPoolId: str,
        Username: str,
        PaginationConfig: AdminListUserAuthEventsPaginatePaginationConfigTypeDef = None,
    ) -> AdminListUserAuthEventsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`CognitoIdentityProvider.Client.admin_list_user_auth_events`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/AdminListUserAuthEvents>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              UserPoolId='string',
              Username='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type UserPoolId: string
        :param UserPoolId: **[REQUIRED]**

          The user pool ID.

        :type Username: string
        :param Username: **[REQUIRED]**

          The user pool username or an alias.

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than
            the value specified in max-items then a ``NextToken`` will be provided in the output
            that you can use to resume pagination.

          - **PageSize** *(integer) --*

            The size of each page.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'AuthEvents': [
                    {
                        'EventId': 'string',
                        'EventType': 'SignIn'|'SignUp'|'ForgotPassword',
                        'CreationDate': datetime(2015, 1, 1),
                        'EventResponse': 'Success'|'Failure',
                        'EventRisk': {
                            'RiskDecision': 'NoRisk'|'AccountTakeover'|'Block',
                            'RiskLevel': 'Low'|'Medium'|'High'
                        },
                        'ChallengeResponses': [
                            {
                                'ChallengeName': 'Password'|'Mfa',
                                'ChallengeResponse': 'Success'|'Failure'
                            },
                        ],
                        'EventContextData': {
                            'IpAddress': 'string',
                            'DeviceName': 'string',
                            'Timezone': 'string',
                            'City': 'string',
                            'Country': 'string'
                        },
                        'EventFeedback': {
                            'FeedbackValue': 'Valid'|'Invalid',
                            'Provider': 'string',
                            'FeedbackDate': datetime(2015, 1, 1)
                        }
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **AuthEvents** *(list) --*

              The response object. It includes the ``EventID`` , ``EventType`` , ``CreationDate`` ,
              ``EventRisk`` , and ``EventResponse`` .

              - *(dict) --*

                The authentication event type.

                - **EventId** *(string) --*

                  The event ID.

                - **EventType** *(string) --*

                  The event type.

                - **CreationDate** *(datetime) --*

                  The creation date

                - **EventResponse** *(string) --*

                  The event response.

                - **EventRisk** *(dict) --*

                  The event risk.

                  - **RiskDecision** *(string) --*

                    The risk decision.

                  - **RiskLevel** *(string) --*

                    The risk level.

                - **ChallengeResponses** *(list) --*

                  The challenge responses.

                  - *(dict) --*

                    The challenge response type.

                    - **ChallengeName** *(string) --*

                      The challenge name

                    - **ChallengeResponse** *(string) --*

                      The challenge response.

                - **EventContextData** *(dict) --*

                  The user context data captured at the time of an event request. It provides
                  additional information about the client from which event the request is received.

                  - **IpAddress** *(string) --*

                    The user's IP address.

                  - **DeviceName** *(string) --*

                    The user's device name.

                  - **Timezone** *(string) --*

                    The user's time zone.

                  - **City** *(string) --*

                    The user's city.

                  - **Country** *(string) --*

                    The user's country.

                - **EventFeedback** *(dict) --*

                  A flag specifying the user feedback captured at the time of an event request is
                  good or bad.

                  - **FeedbackValue** *(string) --*

                    The event feedback value.

                  - **Provider** *(string) --*

                    The provider.

                  - **FeedbackDate** *(datetime) --*

                    The event feedback date.
        """


class ListGroupsPaginator(Boto3Paginator):
    """
    Paginator for `list_groups`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, UserPoolId: str, PaginationConfig: ListGroupsPaginatePaginationConfigTypeDef = None
    ) -> ListGroupsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`CognitoIdentityProvider.Client.list_groups`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/ListGroups>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              UserPoolId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type UserPoolId: string
        :param UserPoolId: **[REQUIRED]**

          The user pool ID for the user pool.

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than
            the value specified in max-items then a ``NextToken`` will be provided in the output
            that you can use to resume pagination.

          - **PageSize** *(integer) --*

            The size of each page.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Groups': [
                    {
                        'GroupName': 'string',
                        'UserPoolId': 'string',
                        'Description': 'string',
                        'RoleArn': 'string',
                        'Precedence': 123,
                        'LastModifiedDate': datetime(2015, 1, 1),
                        'CreationDate': datetime(2015, 1, 1)
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **Groups** *(list) --*

              The group objects for the groups.

              - *(dict) --*

                The group type.

                - **GroupName** *(string) --*

                  The name of the group.

                - **UserPoolId** *(string) --*

                  The user pool ID for the user pool.

                - **Description** *(string) --*

                  A string containing the description of the group.

                - **RoleArn** *(string) --*

                  The role ARN for the group.

                - **Precedence** *(integer) --*

                  A nonnegative integer value that specifies the precedence of this group relative
                  to the other groups that a user can belong to in the user pool. If a user belongs
                  to two or more groups, it is the group with the highest precedence whose role ARN
                  will be used in the ``cognito:roles`` and ``cognito:preferred_role`` claims in the
                  user's tokens. Groups with higher ``Precedence`` values take precedence over
                  groups with lower ``Precedence`` values or with null ``Precedence`` values.

                  Two groups can have the same ``Precedence`` value. If this happens, neither group
                  takes precedence over the other. If two groups with the same ``Precedence`` have
                  the same role ARN, that role is used in the ``cognito:preferred_role`` claim in
                  tokens for users in each group. If the two groups have different role ARNs, the
                  ``cognito:preferred_role`` claim is not set in users' tokens.

                  The default ``Precedence`` value is null.

                - **LastModifiedDate** *(datetime) --*

                  The date the group was last modified.

                - **CreationDate** *(datetime) --*

                  The date the group was created.
        """


class ListIdentityProvidersPaginator(Boto3Paginator):
    """
    Paginator for `list_identity_providers`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        UserPoolId: str,
        PaginationConfig: ListIdentityProvidersPaginatePaginationConfigTypeDef = None,
    ) -> ListIdentityProvidersPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`CognitoIdentityProvider.Client.list_identity_providers`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/ListIdentityProviders>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              UserPoolId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type UserPoolId: string
        :param UserPoolId: **[REQUIRED]**

          The user pool ID.

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than
            the value specified in max-items then a ``NextToken`` will be provided in the output
            that you can use to resume pagination.

          - **PageSize** *(integer) --*

            The size of each page.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Providers': [
                    {
                        'ProviderName': 'string',
                        'ProviderType':
                        'SAML'|'Facebook'|'Google'|'LoginWithAmazon'
                        |'SignInWithApple'|'OIDC',
                        'LastModifiedDate': datetime(2015, 1, 1),
                        'CreationDate': datetime(2015, 1, 1)
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **Providers** *(list) --*

              A list of identity provider objects.

              - *(dict) --*

                A container for identity provider details.

                - **ProviderName** *(string) --*

                  The identity provider name.

                - **ProviderType** *(string) --*

                  The identity provider type.

                - **LastModifiedDate** *(datetime) --*

                  The date the provider was last modified.

                - **CreationDate** *(datetime) --*

                  The date the provider was added to the user pool.
        """


class ListResourceServersPaginator(Boto3Paginator):
    """
    Paginator for `list_resource_servers`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        UserPoolId: str,
        PaginationConfig: ListResourceServersPaginatePaginationConfigTypeDef = None,
    ) -> ListResourceServersPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`CognitoIdentityProvider.Client.list_resource_servers`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/ListResourceServers>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              UserPoolId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type UserPoolId: string
        :param UserPoolId: **[REQUIRED]**

          The user pool ID for the user pool.

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than
            the value specified in max-items then a ``NextToken`` will be provided in the output
            that you can use to resume pagination.

          - **PageSize** *(integer) --*

            The size of each page.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ResourceServers': [
                    {
                        'UserPoolId': 'string',
                        'Identifier': 'string',
                        'Name': 'string',
                        'Scopes': [
                            {
                                'ScopeName': 'string',
                                'ScopeDescription': 'string'
                            },
                        ]
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **ResourceServers** *(list) --*

              The resource servers.

              - *(dict) --*

                A container for information about a resource server for a user pool.

                - **UserPoolId** *(string) --*

                  The user pool ID for the user pool that hosts the resource server.

                - **Identifier** *(string) --*

                  The identifier for the resource server.

                - **Name** *(string) --*

                  The name of the resource server.

                - **Scopes** *(list) --*

                  A list of scopes that are defined for the resource server.

                  - *(dict) --*

                    A resource server scope.

                    - **ScopeName** *(string) --*

                      The name of the scope.

                    - **ScopeDescription** *(string) --*

                      A description of the scope.
        """


class ListUserPoolClientsPaginator(Boto3Paginator):
    """
    Paginator for `list_user_pool_clients`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        UserPoolId: str,
        PaginationConfig: ListUserPoolClientsPaginatePaginationConfigTypeDef = None,
    ) -> ListUserPoolClientsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`CognitoIdentityProvider.Client.list_user_pool_clients`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/ListUserPoolClients>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              UserPoolId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type UserPoolId: string
        :param UserPoolId: **[REQUIRED]**

          The user pool ID for the user pool where you want to list user pool clients.

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than
            the value specified in max-items then a ``NextToken`` will be provided in the output
            that you can use to resume pagination.

          - **PageSize** *(integer) --*

            The size of each page.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'UserPoolClients': [
                    {
                        'ClientId': 'string',
                        'UserPoolId': 'string',
                        'ClientName': 'string'
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            Represents the response from the server that lists user pool clients.

            - **UserPoolClients** *(list) --*

              The user pool clients in the response that lists user pool clients.

              - *(dict) --*

                The description of the user pool client.

                - **ClientId** *(string) --*

                  The ID of the client associated with the user pool.

                - **UserPoolId** *(string) --*

                  The user pool ID for the user pool where you want to describe the user pool
                  client.

                - **ClientName** *(string) --*

                  The client name from the user pool client description.
        """


class ListUserPoolsPaginator(Boto3Paginator):
    """
    Paginator for `list_user_pools`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListUserPoolsPaginatePaginationConfigTypeDef = None
    ) -> ListUserPoolsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`CognitoIdentityProvider.Client.list_user_pools`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/ListUserPools>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than
            the value specified in max-items then a ``NextToken`` will be provided in the output
            that you can use to resume pagination.

          - **PageSize** *(integer) --*

            The size of each page.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'UserPools': [
                    {
                        'Id': 'string',
                        'Name': 'string',
                        'LambdaConfig': {
                            'PreSignUp': 'string',
                            'CustomMessage': 'string',
                            'PostConfirmation': 'string',
                            'PreAuthentication': 'string',
                            'PostAuthentication': 'string',
                            'DefineAuthChallenge': 'string',
                            'CreateAuthChallenge': 'string',
                            'VerifyAuthChallengeResponse': 'string',
                            'PreTokenGeneration': 'string',
                            'UserMigration': 'string'
                        },
                        'Status': 'Enabled'|'Disabled',
                        'LastModifiedDate': datetime(2015, 1, 1),
                        'CreationDate': datetime(2015, 1, 1)
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            Represents the response to list user pools.

            - **UserPools** *(list) --*

              The user pools from the response to list users.

              - *(dict) --*

                A user pool description.

                - **Id** *(string) --*

                  The ID in a user pool description.

                - **Name** *(string) --*

                  The name in a user pool description.

                - **LambdaConfig** *(dict) --*

                  The AWS Lambda configuration information in a user pool description.

                  - **PreSignUp** *(string) --*

                    A pre-registration AWS Lambda trigger.

                  - **CustomMessage** *(string) --*

                    A custom Message AWS Lambda trigger.

                  - **PostConfirmation** *(string) --*

                    A post-confirmation AWS Lambda trigger.

                  - **PreAuthentication** *(string) --*

                    A pre-authentication AWS Lambda trigger.

                  - **PostAuthentication** *(string) --*

                    A post-authentication AWS Lambda trigger.

                  - **DefineAuthChallenge** *(string) --*

                    Defines the authentication challenge.

                  - **CreateAuthChallenge** *(string) --*

                    Creates an authentication challenge.

                  - **VerifyAuthChallengeResponse** *(string) --*

                    Verifies the authentication challenge response.

                  - **PreTokenGeneration** *(string) --*

                    A Lambda trigger that is invoked before token generation.

                  - **UserMigration** *(string) --*

                    The user migration Lambda config type.

                - **Status** *(string) --*

                  The user pool status in a user pool description.

                - **LastModifiedDate** *(datetime) --*

                  The date the user pool description was last modified.

                - **CreationDate** *(datetime) --*

                  The date the user pool description was created.
        """


class ListUsersPaginator(Boto3Paginator):
    """
    Paginator for `list_users`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        UserPoolId: str,
        AttributesToGet: List[str] = None,
        Filter: str = None,
        PaginationConfig: ListUsersPaginatePaginationConfigTypeDef = None,
    ) -> ListUsersPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`CognitoIdentityProvider.Client.list_users`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/ListUsers>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              UserPoolId='string',
              AttributesToGet=[
                  'string',
              ],
              Filter='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type UserPoolId: string
        :param UserPoolId: **[REQUIRED]**

          The user pool ID for the user pool on which the search should be performed.

        :type AttributesToGet: list
        :param AttributesToGet:

          An array of strings, where each string is the name of a user attribute to be returned for
          each user in the search results. If the array is null, all attributes are returned.

          - *(string) --*

        :type Filter: string
        :param Filter:

          A filter string of the form "*AttributeName*  *Filter-Type* "*AttributeValue* "".
          Quotation marks within the filter string must be escaped using the backslash (\\)
          character. For example, "``family_name`` = \\"Reddy\\"".

          * *AttributeName* : The name of the attribute to search for. You can only search for one
          attribute at a time.

          * *Filter-Type* : For an exact match, use =, for example, "``given_name`` = \\"Jon\\"".
          For a prefix ("starts with") match, use ^=, for example, "``given_name`` ^= \\"Jon\\"".

          * *AttributeValue* : The attribute value that must be matched for each user.

          If the filter string is empty, ``ListUsers`` returns all users in the user pool.

          You can only search for the following standard attributes:

          * ``username`` (case-sensitive)

          * ``email``

          * ``phone_number``

          * ``name``

          * ``given_name``

          * ``family_name``

          * ``preferred_username``

          * ``cognito:user_status`` (called **Status** in the Console) (case-insensitive)

          * ``status (called **Enabled** in the Console) (case-sensitive)``

          * ``sub``

          Custom attributes are not searchable.

          For more information, see `Searching for Users Using the ListUsers API
          <https://docs.aws.amazon.com/cognito/latest/developerguide/how-to-manage-user-accounts.html#cognito-user-pools-searching-for-users-using-listusers-api>`__
          and `Examples of Using the ListUsers API
          <https://docs.aws.amazon.com/cognito/latest/developerguide/how-to-manage-user-accounts.html#cognito-user-pools-searching-for-users-listusers-api-examples>`__
          in the *Amazon Cognito Developer Guide* .

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than
            the value specified in max-items then a ``NextToken`` will be provided in the output
            that you can use to resume pagination.

          - **PageSize** *(integer) --*

            The size of each page.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Users': [
                    {
                        'Username': 'string',
                        'Attributes': [
                            {
                                'Name': 'string',
                                'Value': 'string'
                            },
                        ],
                        'UserCreateDate': datetime(2015, 1, 1),
                        'UserLastModifiedDate': datetime(2015, 1, 1),
                        'Enabled': True|False,
                        'UserStatus':
                        'UNCONFIRMED'|'CONFIRMED'|'ARCHIVED'|'COMPROMISED'|'UNKNOWN'
                        |'RESET_REQUIRED'|'FORCE_CHANGE_PASSWORD',
                        'MFAOptions': [
                            {
                                'DeliveryMedium': 'SMS'|'EMAIL',
                                'AttributeName': 'string'
                            },
                        ]
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            The response from the request to list users.

            - **Users** *(list) --*

              The users returned in the request to list users.

              - *(dict) --*

                The user type.

                - **Username** *(string) --*

                  The user name of the user you wish to describe.

                - **Attributes** *(list) --*

                  A container with information about the user type attributes.

                  - *(dict) --*

                    Specifies whether the attribute is standard or custom.

                    - **Name** *(string) --*

                      The name of the attribute.

                    - **Value** *(string) --*

                      The value of the attribute.

                - **UserCreateDate** *(datetime) --*

                  The creation date of the user.

                - **UserLastModifiedDate** *(datetime) --*

                  The last modified date of the user.

                - **Enabled** *(boolean) --*

                  Specifies whether the user is enabled.

                - **UserStatus** *(string) --*

                  The user status. Can be one of the following:

                  * UNCONFIRMED - User has been created but not confirmed.

                  * CONFIRMED - User has been confirmed.

                  * ARCHIVED - User is no longer active.

                  * COMPROMISED - User is disabled due to a potential security threat.

                  * UNKNOWN - User status is not known.

                  * RESET_REQUIRED - User is confirmed, but the user must request a code and reset
                  his or her password before he or she can sign in.

                  * FORCE_CHANGE_PASSWORD - The user is confirmed and the user can sign in using a
                  temporary password, but on first sign-in, the user must change his or her password
                  to a new value before doing anything else.

                - **MFAOptions** *(list) --*

                  The MFA options for the user.

                  - *(dict) --*

                     *This data type is no longer supported.* You can use it only for SMS MFA
                     configurations. You can't use it for TOTP software token MFA configurations.

                    To set either type of MFA configuration, use the  AdminSetUserMFAPreference or
                    SetUserMFAPreference actions.

                    To look up information about either type of MFA configuration, use the
                    AdminGetUserResponse$UserMFASettingList or  GetUserResponse$UserMFASettingList
                    responses.

                    - **DeliveryMedium** *(string) --*

                      The delivery medium to send the MFA code. You can use this parameter to set
                      only the ``SMS`` delivery medium value.

                    - **AttributeName** *(string) --*

                      The attribute name of the MFA option type. The only valid value is
                      ``phone_number`` .

            - **NextToken** *(string) --*

              A token to resume pagination.
        """


class ListUsersInGroupPaginator(Boto3Paginator):
    """
    Paginator for `list_users_in_group`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        UserPoolId: str,
        GroupName: str,
        PaginationConfig: ListUsersInGroupPaginatePaginationConfigTypeDef = None,
    ) -> ListUsersInGroupPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`CognitoIdentityProvider.Client.list_users_in_group`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/cognito-idp-2016-04-18/ListUsersInGroup>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              UserPoolId='string',
              GroupName='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type UserPoolId: string
        :param UserPoolId: **[REQUIRED]**

          The user pool ID for the user pool.

        :type GroupName: string
        :param GroupName: **[REQUIRED]**

          The name of the group.

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than
            the value specified in max-items then a ``NextToken`` will be provided in the output
            that you can use to resume pagination.

          - **PageSize** *(integer) --*

            The size of each page.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Users': [
                    {
                        'Username': 'string',
                        'Attributes': [
                            {
                                'Name': 'string',
                                'Value': 'string'
                            },
                        ],
                        'UserCreateDate': datetime(2015, 1, 1),
                        'UserLastModifiedDate': datetime(2015, 1, 1),
                        'Enabled': True|False,
                        'UserStatus':
                        'UNCONFIRMED'|'CONFIRMED'|'ARCHIVED'|'COMPROMISED'|'UNKNOWN'
                        |'RESET_REQUIRED'|'FORCE_CHANGE_PASSWORD',
                        'MFAOptions': [
                            {
                                'DeliveryMedium': 'SMS'|'EMAIL',
                                'AttributeName': 'string'
                            },
                        ]
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **Users** *(list) --*

              The users returned in the request to list users.

              - *(dict) --*

                The user type.

                - **Username** *(string) --*

                  The user name of the user you wish to describe.

                - **Attributes** *(list) --*

                  A container with information about the user type attributes.

                  - *(dict) --*

                    Specifies whether the attribute is standard or custom.

                    - **Name** *(string) --*

                      The name of the attribute.

                    - **Value** *(string) --*

                      The value of the attribute.

                - **UserCreateDate** *(datetime) --*

                  The creation date of the user.

                - **UserLastModifiedDate** *(datetime) --*

                  The last modified date of the user.

                - **Enabled** *(boolean) --*

                  Specifies whether the user is enabled.

                - **UserStatus** *(string) --*

                  The user status. Can be one of the following:

                  * UNCONFIRMED - User has been created but not confirmed.

                  * CONFIRMED - User has been confirmed.

                  * ARCHIVED - User is no longer active.

                  * COMPROMISED - User is disabled due to a potential security threat.

                  * UNKNOWN - User status is not known.

                  * RESET_REQUIRED - User is confirmed, but the user must request a code and reset
                  his or her password before he or she can sign in.

                  * FORCE_CHANGE_PASSWORD - The user is confirmed and the user can sign in using a
                  temporary password, but on first sign-in, the user must change his or her password
                  to a new value before doing anything else.

                - **MFAOptions** *(list) --*

                  The MFA options for the user.

                  - *(dict) --*

                     *This data type is no longer supported.* You can use it only for SMS MFA
                     configurations. You can't use it for TOTP software token MFA configurations.

                    To set either type of MFA configuration, use the  AdminSetUserMFAPreference or
                    SetUserMFAPreference actions.

                    To look up information about either type of MFA configuration, use the
                    AdminGetUserResponse$UserMFASettingList or  GetUserResponse$UserMFASettingList
                    responses.

                    - **DeliveryMedium** *(string) --*

                      The delivery medium to send the MFA code. You can use this parameter to set
                      only the ``SMS`` delivery medium value.

                    - **AttributeName** *(string) --*

                      The attribute name of the MFA option type. The only valid value is
                      ``phone_number`` .
        """
