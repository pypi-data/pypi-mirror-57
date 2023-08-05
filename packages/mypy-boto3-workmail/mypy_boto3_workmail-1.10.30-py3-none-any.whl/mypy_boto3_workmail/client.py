"Main interface for workmail service Client"
from __future__ import annotations

from typing import Any, Dict, List
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3.type_defs import Literal, overload

# pylint: disable=import-self
import mypy_boto3_workmail.client as client_scope

# pylint: disable=import-self
import mypy_boto3_workmail.paginator as paginator_scope
from mypy_boto3_workmail.type_defs import (
    ClientCreateGroupResponseTypeDef,
    ClientCreateResourceResponseTypeDef,
    ClientCreateUserResponseTypeDef,
    ClientDescribeGroupResponseTypeDef,
    ClientDescribeOrganizationResponseTypeDef,
    ClientDescribeResourceResponseTypeDef,
    ClientDescribeUserResponseTypeDef,
    ClientGetMailboxDetailsResponseTypeDef,
    ClientListAliasesResponseTypeDef,
    ClientListGroupMembersResponseTypeDef,
    ClientListGroupsResponseTypeDef,
    ClientListMailboxPermissionsResponseTypeDef,
    ClientListOrganizationsResponseTypeDef,
    ClientListResourceDelegatesResponseTypeDef,
    ClientListResourcesResponseTypeDef,
    ClientListUsersResponseTypeDef,
    ClientUpdateResourceBookingOptionsTypeDef,
)


__all__ = ("Client",)


class Client(BaseClient):
    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def associate_delegate_to_resource(
        self, OrganizationId: str, ResourceId: str, EntityId: str
    ) -> Dict[str, Any]:
        """
        Adds a member (user or group) to the resource's set of delegates.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/AssociateDelegateToResource>`_

        **Request Syntax**
        ::

          response = client.associate_delegate_to_resource(
              OrganizationId='string',
              ResourceId='string',
              EntityId='string'
          )
        :type OrganizationId: string
        :param OrganizationId: **[REQUIRED]**

          The organization under which the resource exists.

        :type ResourceId: string
        :param ResourceId: **[REQUIRED]**

          The resource for which members (users or groups) are associated.

        :type EntityId: string
        :param EntityId: **[REQUIRED]**

          The member (user or group) to associate to the resource.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def associate_member_to_group(
        self, OrganizationId: str, GroupId: str, MemberId: str
    ) -> Dict[str, Any]:
        """
        Adds a member (user or group) to the group's set.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/AssociateMemberToGroup>`_

        **Request Syntax**
        ::

          response = client.associate_member_to_group(
              OrganizationId='string',
              GroupId='string',
              MemberId='string'
          )
        :type OrganizationId: string
        :param OrganizationId: **[REQUIRED]**

          The organization under which the group exists.

        :type GroupId: string
        :param GroupId: **[REQUIRED]**

          The group to which the member (user or group) is associated.

        :type MemberId: string
        :param MemberId: **[REQUIRED]**

          The member (user or group) to associate to the group.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        :type operation_name: string
        :param operation_name: The operation name.  This is the same name
            as the method name on the client.  For example, if the
            method name is ``create_foo``, and you'd normally invoke the
            operation as ``client.create_foo(**kwargs)``, if the
            ``create_foo`` operation can be paginated, you can use the
            call ``client.get_paginator("create_foo")``.

        :return: ``True`` if the operation can be paginated,
            ``False`` otherwise.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_alias(self, OrganizationId: str, EntityId: str, Alias: str) -> Dict[str, Any]:
        """
        Adds an alias to the set of a given member (user or group) of Amazon WorkMail.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/CreateAlias>`_

        **Request Syntax**
        ::

          response = client.create_alias(
              OrganizationId='string',
              EntityId='string',
              Alias='string'
          )
        :type OrganizationId: string
        :param OrganizationId: **[REQUIRED]**

          The organization under which the member (user or group) exists.

        :type EntityId: string
        :param EntityId: **[REQUIRED]**

          The member (user or group) to which this alias is added.

        :type Alias: string
        :param Alias: **[REQUIRED]**

          The alias to add to the member set.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_group(self, OrganizationId: str, Name: str) -> ClientCreateGroupResponseTypeDef:
        """
        Creates a group that can be used in Amazon WorkMail by calling the  RegisterToWorkMail
        operation.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/CreateGroup>`_

        **Request Syntax**
        ::

          response = client.create_group(
              OrganizationId='string',
              Name='string'
          )
        :type OrganizationId: string
        :param OrganizationId: **[REQUIRED]**

          The organization under which the group is to be created.

        :type Name: string
        :param Name: **[REQUIRED]**

          The name of the group.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'GroupId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **GroupId** *(string) --*

              The identifier of the group.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_resource(
        self, OrganizationId: str, Name: str, Type: Literal["ROOM", "EQUIPMENT"]
    ) -> ClientCreateResourceResponseTypeDef:
        """
        Creates a new Amazon WorkMail resource.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/CreateResource>`_

        **Request Syntax**
        ::

          response = client.create_resource(
              OrganizationId='string',
              Name='string',
              Type='ROOM'|'EQUIPMENT'
          )
        :type OrganizationId: string
        :param OrganizationId: **[REQUIRED]**

          The identifier associated with the organization for which the resource is created.

        :type Name: string
        :param Name: **[REQUIRED]**

          The name of the new resource.

        :type Type: string
        :param Type: **[REQUIRED]**

          The type of the new resource. The available types are ``equipment`` and ``room`` .

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ResourceId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **ResourceId** *(string) --*

              The identifier of the new resource.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_user(
        self, OrganizationId: str, Name: str, DisplayName: str, Password: str
    ) -> ClientCreateUserResponseTypeDef:
        """
        Creates a user who can be used in Amazon WorkMail by calling the  RegisterToWorkMail
        operation.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/CreateUser>`_

        **Request Syntax**
        ::

          response = client.create_user(
              OrganizationId='string',
              Name='string',
              DisplayName='string',
              Password='string'
          )
        :type OrganizationId: string
        :param OrganizationId: **[REQUIRED]**

          The identifier of the organization for which the user is created.

        :type Name: string
        :param Name: **[REQUIRED]**

          The name for the new user. Simple AD or AD Connector user names have a maximum length of
          20. All others have a maximum length of 64.

        :type DisplayName: string
        :param DisplayName: **[REQUIRED]**

          The display name for the new user.

        :type Password: string
        :param Password: **[REQUIRED]**

          The password for the new user.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'UserId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **UserId** *(string) --*

              The identifier for the new user.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_alias(self, OrganizationId: str, EntityId: str, Alias: str) -> Dict[str, Any]:
        """
        Remove one or more specified aliases from a set of aliases for a given user.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/DeleteAlias>`_

        **Request Syntax**
        ::

          response = client.delete_alias(
              OrganizationId='string',
              EntityId='string',
              Alias='string'
          )
        :type OrganizationId: string
        :param OrganizationId: **[REQUIRED]**

          The identifier for the organization under which the user exists.

        :type EntityId: string
        :param EntityId: **[REQUIRED]**

          The identifier for the member (user or group) from which to have the aliases removed.

        :type Alias: string
        :param Alias: **[REQUIRED]**

          The aliases to be removed from the user's set of aliases. Duplicate entries in the list
          are collapsed into single entries (the list is transformed into a set).

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_group(self, OrganizationId: str, GroupId: str) -> Dict[str, Any]:
        """
        Deletes a group from Amazon WorkMail.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/DeleteGroup>`_

        **Request Syntax**
        ::

          response = client.delete_group(
              OrganizationId='string',
              GroupId='string'
          )
        :type OrganizationId: string
        :param OrganizationId: **[REQUIRED]**

          The organization that contains the group.

        :type GroupId: string
        :param GroupId: **[REQUIRED]**

          The identifier of the group to be deleted.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_mailbox_permissions(
        self, OrganizationId: str, EntityId: str, GranteeId: str
    ) -> Dict[str, Any]:
        """
        Deletes permissions granted to a member (user or group).

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/DeleteMailboxPermissions>`_

        **Request Syntax**
        ::

          response = client.delete_mailbox_permissions(
              OrganizationId='string',
              EntityId='string',
              GranteeId='string'
          )
        :type OrganizationId: string
        :param OrganizationId: **[REQUIRED]**

          The identifier of the organization under which the member (user or group) exists.

        :type EntityId: string
        :param EntityId: **[REQUIRED]**

          The identifier of the member (user or group)that owns the mailbox.

        :type GranteeId: string
        :param GranteeId: **[REQUIRED]**

          The identifier of the member (user or group) for which to delete granted permissions.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_resource(self, OrganizationId: str, ResourceId: str) -> Dict[str, Any]:
        """
        Deletes the specified resource.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/DeleteResource>`_

        **Request Syntax**
        ::

          response = client.delete_resource(
              OrganizationId='string',
              ResourceId='string'
          )
        :type OrganizationId: string
        :param OrganizationId: **[REQUIRED]**

          The identifier associated with the organization from which the resource is deleted.

        :type ResourceId: string
        :param ResourceId: **[REQUIRED]**

          The identifier of the resource to be deleted.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_user(self, OrganizationId: str, UserId: str) -> Dict[str, Any]:
        """
        Deletes a user from Amazon WorkMail and all subsequent systems. Before you can delete a
        user, the user state must be ``DISABLED`` . Use the  DescribeUser action to confirm the user
        state.

        Deleting a user is permanent and cannot be undone. WorkMail archives user mailboxes for 30
        days before they are permanently removed.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/DeleteUser>`_

        **Request Syntax**
        ::

          response = client.delete_user(
              OrganizationId='string',
              UserId='string'
          )
        :type OrganizationId: string
        :param OrganizationId: **[REQUIRED]**

          The organization that contains the user to be deleted.

        :type UserId: string
        :param UserId: **[REQUIRED]**

          The identifier of the user to be deleted.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def deregister_from_work_mail(self, OrganizationId: str, EntityId: str) -> Dict[str, Any]:
        """
        Mark a user, group, or resource as no longer used in Amazon WorkMail. This action
        disassociates the mailbox and schedules it for clean-up. WorkMail keeps mailboxes for 30
        days before they are permanently removed. The functionality in the console is *Disable* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/DeregisterFromWorkMail>`_

        **Request Syntax**
        ::

          response = client.deregister_from_work_mail(
              OrganizationId='string',
              EntityId='string'
          )
        :type OrganizationId: string
        :param OrganizationId: **[REQUIRED]**

          The identifier for the organization under which the Amazon WorkMail entity exists.

        :type EntityId: string
        :param EntityId: **[REQUIRED]**

          The identifier for the member (user or group) to be updated.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_group(
        self, OrganizationId: str, GroupId: str
    ) -> ClientDescribeGroupResponseTypeDef:
        """
        Returns the data available for the group.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/DescribeGroup>`_

        **Request Syntax**
        ::

          response = client.describe_group(
              OrganizationId='string',
              GroupId='string'
          )
        :type OrganizationId: string
        :param OrganizationId: **[REQUIRED]**

          The identifier for the organization under which the group exists.

        :type GroupId: string
        :param GroupId: **[REQUIRED]**

          The identifier for the group to be described.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'GroupId': 'string',
                'Name': 'string',
                'Email': 'string',
                'State': 'ENABLED'|'DISABLED'|'DELETED',
                'EnabledDate': datetime(2015, 1, 1),
                'DisabledDate': datetime(2015, 1, 1)
            }
          **Response Structure**

          - *(dict) --*

            - **GroupId** *(string) --*

              The identifier of the described group.

            - **Name** *(string) --*

              The name of the described group.

            - **Email** *(string) --*

              The email of the described group.

            - **State** *(string) --*

              The state of the user: enabled (registered to Amazon WorkMail) or disabled
              (deregistered or never registered to WorkMail).

            - **EnabledDate** *(datetime) --*

              The date and time when a user was registered to WorkMail, in UNIX epoch time format.

            - **DisabledDate** *(datetime) --*

              The date and time when a user was deregistered from WorkMail, in UNIX epoch time
              format.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_organization(
        self, OrganizationId: str
    ) -> ClientDescribeOrganizationResponseTypeDef:
        """
        Provides more information regarding a given organization based on its identifier.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/DescribeOrganization>`_

        **Request Syntax**
        ::

          response = client.describe_organization(
              OrganizationId='string'
          )
        :type OrganizationId: string
        :param OrganizationId: **[REQUIRED]**

          The identifier for the organization to be described.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'OrganizationId': 'string',
                'Alias': 'string',
                'State': 'string',
                'DirectoryId': 'string',
                'DirectoryType': 'string',
                'DefaultMailDomain': 'string',
                'CompletedDate': datetime(2015, 1, 1),
                'ErrorMessage': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **OrganizationId** *(string) --*

              The identifier of an organization.

            - **Alias** *(string) --*

              The alias for an organization.

            - **State** *(string) --*

              The state of an organization.

            - **DirectoryId** *(string) --*

              The identifier for the directory associated with an Amazon WorkMail organization.

            - **DirectoryType** *(string) --*

              The type of directory associated with the WorkMail organization.

            - **DefaultMailDomain** *(string) --*

              The default mail domain associated with the organization.

            - **CompletedDate** *(datetime) --*

              The date at which the organization became usable in the WorkMail context, in UNIX
              epoch time format.

            - **ErrorMessage** *(string) --*

              (Optional) The error message indicating if unexpected behavior was encountered with
              regards to the organization.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_resource(
        self, OrganizationId: str, ResourceId: str
    ) -> ClientDescribeResourceResponseTypeDef:
        """
        Returns the data available for the resource.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/DescribeResource>`_

        **Request Syntax**
        ::

          response = client.describe_resource(
              OrganizationId='string',
              ResourceId='string'
          )
        :type OrganizationId: string
        :param OrganizationId: **[REQUIRED]**

          The identifier associated with the organization for which the resource is described.

        :type ResourceId: string
        :param ResourceId: **[REQUIRED]**

          The identifier of the resource to be described.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'ResourceId': 'string',
                'Email': 'string',
                'Name': 'string',
                'Type': 'ROOM'|'EQUIPMENT',
                'BookingOptions': {
                    'AutoAcceptRequests': True|False,
                    'AutoDeclineRecurringRequests': True|False,
                    'AutoDeclineConflictingRequests': True|False
                },
                'State': 'ENABLED'|'DISABLED'|'DELETED',
                'EnabledDate': datetime(2015, 1, 1),
                'DisabledDate': datetime(2015, 1, 1)
            }
          **Response Structure**

          - *(dict) --*

            - **ResourceId** *(string) --*

              The identifier of the described resource.

            - **Email** *(string) --*

              The email of the described resource.

            - **Name** *(string) --*

              The name of the described resource.

            - **Type** *(string) --*

              The type of the described resource.

            - **BookingOptions** *(dict) --*

              The booking options for the described resource.

              - **AutoAcceptRequests** *(boolean) --*

                The resource's ability to automatically reply to requests. If disabled, delegates
                must be associated to the resource.

              - **AutoDeclineRecurringRequests** *(boolean) --*

                The resource's ability to automatically decline any recurring requests.

              - **AutoDeclineConflictingRequests** *(boolean) --*

                The resource's ability to automatically decline any conflicting requests.

            - **State** *(string) --*

              The state of the resource: enabled (registered to Amazon WorkMail) or disabled
              (deregistered or never registered to WorkMail).

            - **EnabledDate** *(datetime) --*

              The date and time when a resource was enabled for WorkMail, in UNIX epoch time format.

            - **DisabledDate** *(datetime) --*

              The date and time when a resource was disabled from WorkMail, in UNIX epoch time
              format.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_user(self, OrganizationId: str, UserId: str) -> ClientDescribeUserResponseTypeDef:
        """
        Provides information regarding the user.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/DescribeUser>`_

        **Request Syntax**
        ::

          response = client.describe_user(
              OrganizationId='string',
              UserId='string'
          )
        :type OrganizationId: string
        :param OrganizationId: **[REQUIRED]**

          The identifier for the organization under which the user exists.

        :type UserId: string
        :param UserId: **[REQUIRED]**

          The identifier for the user to be described.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'UserId': 'string',
                'Name': 'string',
                'Email': 'string',
                'DisplayName': 'string',
                'State': 'ENABLED'|'DISABLED'|'DELETED',
                'UserRole': 'USER'|'RESOURCE'|'SYSTEM_USER',
                'EnabledDate': datetime(2015, 1, 1),
                'DisabledDate': datetime(2015, 1, 1)
            }
          **Response Structure**

          - *(dict) --*

            - **UserId** *(string) --*

              The identifier for the described user.

            - **Name** *(string) --*

              The name for the user.

            - **Email** *(string) --*

              The email of the user.

            - **DisplayName** *(string) --*

              The display name of the user.

            - **State** *(string) --*

              The state of a user: enabled (registered to Amazon WorkMail) or disabled (deregistered
              or never registered to WorkMail).

            - **UserRole** *(string) --*

              In certain cases, other entities are modeled as users. If interoperability is enabled,
              resources are imported into Amazon WorkMail as users. Because different WorkMail
              organizations rely on different directory types, administrators can distinguish
              between an unregistered user (account is disabled and has a user role) and the
              directory administrators. The values are USER, RESOURCE, and SYSTEM_USER.

            - **EnabledDate** *(datetime) --*

              The date and time at which the user was enabled for Amazon WorkMail usage, in UNIX
              epoch time format.

            - **DisabledDate** *(datetime) --*

              The date and time at which the user was disabled for Amazon WorkMail usage, in UNIX
              epoch time format.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disassociate_delegate_from_resource(
        self, OrganizationId: str, ResourceId: str, EntityId: str
    ) -> Dict[str, Any]:
        """
        Removes a member from the resource's set of delegates.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/DisassociateDelegateFromResource>`_

        **Request Syntax**
        ::

          response = client.disassociate_delegate_from_resource(
              OrganizationId='string',
              ResourceId='string',
              EntityId='string'
          )
        :type OrganizationId: string
        :param OrganizationId: **[REQUIRED]**

          The identifier for the organization under which the resource exists.

        :type ResourceId: string
        :param ResourceId: **[REQUIRED]**

          The identifier of the resource from which delegates' set members are removed.

        :type EntityId: string
        :param EntityId: **[REQUIRED]**

          The identifier for the member (user, group) to be removed from the resource's delegates.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disassociate_member_from_group(
        self, OrganizationId: str, GroupId: str, MemberId: str
    ) -> Dict[str, Any]:
        """
        Removes a member from a group.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/DisassociateMemberFromGroup>`_

        **Request Syntax**
        ::

          response = client.disassociate_member_from_group(
              OrganizationId='string',
              GroupId='string',
              MemberId='string'
          )
        :type OrganizationId: string
        :param OrganizationId: **[REQUIRED]**

          The identifier for the organization under which the group exists.

        :type GroupId: string
        :param GroupId: **[REQUIRED]**

          The identifier for the group from which members are removed.

        :type MemberId: string
        :param MemberId: **[REQUIRED]**

          The identifier for the member to be removed to the group.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> None:
        """
        Generate a presigned url given a client, its method, and arguments

        :type ClientMethod: string
        :param ClientMethod: The client method to presign for

        :type Params: dict
        :param Params: The parameters normally passed to
            ``ClientMethod``.

        :type ExpiresIn: int
        :param ExpiresIn: The number of seconds the presigned url is valid
            for. By default it expires in an hour (3600 seconds)

        :type HttpMethod: string
        :param HttpMethod: The http method to use on the generated url. By
            default, the http method is whatever is used in the method's model.

        :returns: The presigned url
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_mailbox_details(
        self, OrganizationId: str, UserId: str
    ) -> ClientGetMailboxDetailsResponseTypeDef:
        """
        Requests a user's mailbox details for a specified organization and user.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/GetMailboxDetails>`_

        **Request Syntax**
        ::

          response = client.get_mailbox_details(
              OrganizationId='string',
              UserId='string'
          )
        :type OrganizationId: string
        :param OrganizationId: **[REQUIRED]**

          The identifier for the organization that contains the user whose mailbox details are being
          requested.

        :type UserId: string
        :param UserId: **[REQUIRED]**

          The identifier for the user whose mailbox details are being requested.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'MailboxQuota': 123,
                'MailboxSize': 123.0
            }
          **Response Structure**

          - *(dict) --*

            - **MailboxQuota** *(integer) --*

              The maximum allowed mailbox size, in MB, for the specified user.

            - **MailboxSize** *(float) --*

              The current mailbox size, in MB, for the specified user.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_aliases(
        self, OrganizationId: str, EntityId: str, NextToken: str = None, MaxResults: int = None
    ) -> ClientListAliasesResponseTypeDef:
        """
        Creates a paginated call to list the aliases associated with a given entity.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/ListAliases>`_

        **Request Syntax**
        ::

          response = client.list_aliases(
              OrganizationId='string',
              EntityId='string',
              NextToken='string',
              MaxResults=123
          )
        :type OrganizationId: string
        :param OrganizationId: **[REQUIRED]**

          The identifier for the organization under which the entity exists.

        :type EntityId: string
        :param EntityId: **[REQUIRED]**

          The identifier for the entity for which to list the aliases.

        :type NextToken: string
        :param NextToken:

          The token to use to retrieve the next page of results. The first call does not contain any
          tokens.

        :type MaxResults: integer
        :param MaxResults:

          The maximum number of results to return in a single call.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Aliases': [
                    'string',
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Aliases** *(list) --*

              The entity's paginated aliases.

              - *(string) --*

            - **NextToken** *(string) --*

              The token to use to retrieve the next page of results. The value is "null" when there
              are no more results to return.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_group_members(
        self, OrganizationId: str, GroupId: str, NextToken: str = None, MaxResults: int = None
    ) -> ClientListGroupMembersResponseTypeDef:
        """
        Returns an overview of the members of a group. Users and groups can be members of a group.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/ListGroupMembers>`_

        **Request Syntax**
        ::

          response = client.list_group_members(
              OrganizationId='string',
              GroupId='string',
              NextToken='string',
              MaxResults=123
          )
        :type OrganizationId: string
        :param OrganizationId: **[REQUIRED]**

          The identifier for the organization under which the group exists.

        :type GroupId: string
        :param GroupId: **[REQUIRED]**

          The identifier for the group to which the members (users or groups) are associated.

        :type NextToken: string
        :param NextToken:

          The token to use to retrieve the next page of results. The first call does not contain any
          tokens.

        :type MaxResults: integer
        :param MaxResults:

          The maximum number of results to return in a single call.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Members': [
                    {
                        'Id': 'string',
                        'Name': 'string',
                        'Type': 'GROUP'|'USER',
                        'State': 'ENABLED'|'DISABLED'|'DELETED',
                        'EnabledDate': datetime(2015, 1, 1),
                        'DisabledDate': datetime(2015, 1, 1)
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Members** *(list) --*

              The members associated to the group.

              - *(dict) --*

                The representation of a user or group.

                - **Id** *(string) --*

                  The identifier of the member.

                - **Name** *(string) --*

                  The name of the member.

                - **Type** *(string) --*

                  A member can be a user or group.

                - **State** *(string) --*

                  The state of the member, which can be ENABLED, DISABLED, or DELETED.

                - **EnabledDate** *(datetime) --*

                  The date indicating when the member was enabled for Amazon WorkMail use.

                - **DisabledDate** *(datetime) --*

                  The date indicating when the member was disabled from Amazon WorkMail use.

            - **NextToken** *(string) --*

              The token to use to retrieve the next page of results. The first call does not contain
              any tokens.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_groups(
        self, OrganizationId: str, NextToken: str = None, MaxResults: int = None
    ) -> ClientListGroupsResponseTypeDef:
        """
        Returns summaries of the organization's groups.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/ListGroups>`_

        **Request Syntax**
        ::

          response = client.list_groups(
              OrganizationId='string',
              NextToken='string',
              MaxResults=123
          )
        :type OrganizationId: string
        :param OrganizationId: **[REQUIRED]**

          The identifier for the organization under which the groups exist.

        :type NextToken: string
        :param NextToken:

          The token to use to retrieve the next page of results. The first call does not contain any
          tokens.

        :type MaxResults: integer
        :param MaxResults:

          The maximum number of results to return in a single call.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Groups': [
                    {
                        'Id': 'string',
                        'Email': 'string',
                        'Name': 'string',
                        'State': 'ENABLED'|'DISABLED'|'DELETED',
                        'EnabledDate': datetime(2015, 1, 1),
                        'DisabledDate': datetime(2015, 1, 1)
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Groups** *(list) --*

              The overview of groups for an organization.

              - *(dict) --*

                The representation of an Amazon WorkMail group.

                - **Id** *(string) --*

                  The identifier of the group.

                - **Email** *(string) --*

                  The email of the group.

                - **Name** *(string) --*

                  The name of the group.

                - **State** *(string) --*

                  The state of the group, which can be ENABLED, DISABLED, or DELETED.

                - **EnabledDate** *(datetime) --*

                  The date indicating when the group was enabled for Amazon WorkMail use.

                - **DisabledDate** *(datetime) --*

                  The date indicating when the group was disabled from Amazon WorkMail use.

            - **NextToken** *(string) --*

              The token to use to retrieve the next page of results. The value is "null" when there
              are no more results to return.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_mailbox_permissions(
        self, OrganizationId: str, EntityId: str, NextToken: str = None, MaxResults: int = None
    ) -> ClientListMailboxPermissionsResponseTypeDef:
        """
        Lists the mailbox permissions associated with a user, group, or resource mailbox.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/ListMailboxPermissions>`_

        **Request Syntax**
        ::

          response = client.list_mailbox_permissions(
              OrganizationId='string',
              EntityId='string',
              NextToken='string',
              MaxResults=123
          )
        :type OrganizationId: string
        :param OrganizationId: **[REQUIRED]**

          The identifier of the organization under which the user, group, or resource exists.

        :type EntityId: string
        :param EntityId: **[REQUIRED]**

          The identifier of the user, group, or resource for which to list mailbox permissions.

        :type NextToken: string
        :param NextToken:

          The token to use to retrieve the next page of results. The first call does not contain any
          tokens.

        :type MaxResults: integer
        :param MaxResults:

          The maximum number of results to return in a single call.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Permissions': [
                    {
                        'GranteeId': 'string',
                        'GranteeType': 'GROUP'|'USER',
                        'PermissionValues': [
                            'FULL_ACCESS'|'SEND_AS'|'SEND_ON_BEHALF',
                        ]
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Permissions** *(list) --*

              One page of the user, group, or resource mailbox permissions.

              - *(dict) --*

                Permission granted to a user, group, or resource to access a certain aspect of
                another user, group, or resource mailbox.

                - **GranteeId** *(string) --*

                  The identifier of the user, group, or resource to which the permissions are
                  granted.

                - **GranteeType** *(string) --*

                  The type of user, group, or resource referred to in GranteeId.

                - **PermissionValues** *(list) --*

                  The permissions granted to the grantee. SEND_AS allows the grantee to send email
                  as the owner of the mailbox (the grantee is not mentioned on these emails).
                  SEND_ON_BEHALF allows the grantee to send email on behalf of the owner of the
                  mailbox (the grantee is not mentioned as the physical sender of these emails).
                  FULL_ACCESS allows the grantee full access to the mailbox, irrespective of other
                  folder-level permissions set on the mailbox.

                  - *(string) --*

            - **NextToken** *(string) --*

              The token to use to retrieve the next page of results. The value is "null" when there
              are no more results to return.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_organizations(
        self, NextToken: str = None, MaxResults: int = None
    ) -> ClientListOrganizationsResponseTypeDef:
        """
        Returns summaries of the customer's non-deleted organizations.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/ListOrganizations>`_

        **Request Syntax**
        ::

          response = client.list_organizations(
              NextToken='string',
              MaxResults=123
          )
        :type NextToken: string
        :param NextToken:

          The token to use to retrieve the next page of results. The first call does not contain any
          tokens.

        :type MaxResults: integer
        :param MaxResults:

          The maximum number of results to return in a single call.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'OrganizationSummaries': [
                    {
                        'OrganizationId': 'string',
                        'Alias': 'string',
                        'ErrorMessage': 'string',
                        'State': 'string'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **OrganizationSummaries** *(list) --*

              The overview of owned organizations presented as a list of organization summaries.

              - *(dict) --*

                The representation of an organization.

                - **OrganizationId** *(string) --*

                  The identifier associated with the organization.

                - **Alias** *(string) --*

                  The alias associated with the organization.

                - **ErrorMessage** *(string) --*

                  The error message associated with the organization. It is only present if
                  unexpected behavior has occurred with regards to the organization. It provides
                  insight or solutions regarding unexpected behavior.

                - **State** *(string) --*

                  The state associated with the organization.

            - **NextToken** *(string) --*

              The token to use to retrieve the next page of results. The value is "null" when there
              are no more results to return.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_resource_delegates(
        self, OrganizationId: str, ResourceId: str, NextToken: str = None, MaxResults: int = None
    ) -> ClientListResourceDelegatesResponseTypeDef:
        """
        Lists the delegates associated with a resource. Users and groups can be resource delegates
        and answer requests on behalf of the resource.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/ListResourceDelegates>`_

        **Request Syntax**
        ::

          response = client.list_resource_delegates(
              OrganizationId='string',
              ResourceId='string',
              NextToken='string',
              MaxResults=123
          )
        :type OrganizationId: string
        :param OrganizationId: **[REQUIRED]**

          The identifier for the organization that contains the resource for which delegates are
          listed.

        :type ResourceId: string
        :param ResourceId: **[REQUIRED]**

          The identifier for the resource whose delegates are listed.

        :type NextToken: string
        :param NextToken:

          The token used to paginate through the delegates associated with a resource.

        :type MaxResults: integer
        :param MaxResults:

          The number of maximum results in a page.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Delegates': [
                    {
                        'Id': 'string',
                        'Type': 'GROUP'|'USER'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Delegates** *(list) --*

              One page of the resource's delegates.

              - *(dict) --*

                The name of the attribute, which is one of the values defined in the UserAttribute
                enumeration.

                - **Id** *(string) --*

                  The identifier for the user or group associated as the resource's delegate.

                - **Type** *(string) --*

                  The type of the delegate: user or group.

            - **NextToken** *(string) --*

              The token used to paginate through the delegates associated with a resource. While
              results are still available, it has an associated value. When the last page is
              reached, the token is empty.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_resources(
        self, OrganizationId: str, NextToken: str = None, MaxResults: int = None
    ) -> ClientListResourcesResponseTypeDef:
        """
        Returns summaries of the organization's resources.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/ListResources>`_

        **Request Syntax**
        ::

          response = client.list_resources(
              OrganizationId='string',
              NextToken='string',
              MaxResults=123
          )
        :type OrganizationId: string
        :param OrganizationId: **[REQUIRED]**

          The identifier for the organization under which the resources exist.

        :type NextToken: string
        :param NextToken:

          The token to use to retrieve the next page of results. The first call does not contain any
          tokens.

        :type MaxResults: integer
        :param MaxResults:

          The maximum number of results to return in a single call.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Resources': [
                    {
                        'Id': 'string',
                        'Email': 'string',
                        'Name': 'string',
                        'Type': 'ROOM'|'EQUIPMENT',
                        'State': 'ENABLED'|'DISABLED'|'DELETED',
                        'EnabledDate': datetime(2015, 1, 1),
                        'DisabledDate': datetime(2015, 1, 1)
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Resources** *(list) --*

              One page of the organization's resource representation.

              - *(dict) --*

                The representation of a resource.

                - **Id** *(string) --*

                  The identifier of the resource.

                - **Email** *(string) --*

                  The email of the resource.

                - **Name** *(string) --*

                  The name of the resource.

                - **Type** *(string) --*

                  The type of the resource: equipment or room.

                - **State** *(string) --*

                  The state of the resource, which can be ENABLED, DISABLED, or DELETED.

                - **EnabledDate** *(datetime) --*

                  The date indicating when the resource was enabled for Amazon WorkMail use.

                - **DisabledDate** *(datetime) --*

                  The date indicating when the resource was disabled from Amazon WorkMail use.

            - **NextToken** *(string) --*

              The token used to paginate through all the organization's resources. While results are
              still available, it has an associated value. When the last page is reached, the token
              is empty.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_users(
        self, OrganizationId: str, NextToken: str = None, MaxResults: int = None
    ) -> ClientListUsersResponseTypeDef:
        """
        Returns summaries of the organization's users.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/ListUsers>`_

        **Request Syntax**
        ::

          response = client.list_users(
              OrganizationId='string',
              NextToken='string',
              MaxResults=123
          )
        :type OrganizationId: string
        :param OrganizationId: **[REQUIRED]**

          The identifier for the organization under which the users exist.

        :type NextToken: string
        :param NextToken:

          The token to use to retrieve the next page of results. The first call does not contain any
          tokens.

        :type MaxResults: integer
        :param MaxResults:

          The maximum number of results to return in a single call.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Users': [
                    {
                        'Id': 'string',
                        'Email': 'string',
                        'Name': 'string',
                        'DisplayName': 'string',
                        'State': 'ENABLED'|'DISABLED'|'DELETED',
                        'UserRole': 'USER'|'RESOURCE'|'SYSTEM_USER',
                        'EnabledDate': datetime(2015, 1, 1),
                        'DisabledDate': datetime(2015, 1, 1)
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Users** *(list) --*

              The overview of users for an organization.

              - *(dict) --*

                The representation of an Amazon WorkMail user.

                - **Id** *(string) --*

                  The identifier of the user.

                - **Email** *(string) --*

                  The email of the user.

                - **Name** *(string) --*

                  The name of the user.

                - **DisplayName** *(string) --*

                  The display name of the user.

                - **State** *(string) --*

                  The state of the user, which can be ENABLED, DISABLED, or DELETED.

                - **UserRole** *(string) --*

                  The role of the user.

                - **EnabledDate** *(datetime) --*

                  The date indicating when the user was enabled for Amazon WorkMail use.

                - **DisabledDate** *(datetime) --*

                  The date indicating when the user was disabled from Amazon WorkMail use.

            - **NextToken** *(string) --*

              The token to use to retrieve the next page of results. This value is `null` when there
              are no more results to return.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_mailbox_permissions(
        self,
        OrganizationId: str,
        EntityId: str,
        GranteeId: str,
        PermissionValues: List[Literal["FULL_ACCESS", "SEND_AS", "SEND_ON_BEHALF"]],
    ) -> Dict[str, Any]:
        """
        Sets permissions for a user, group, or resource. This replaces any pre-existing permissions.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/PutMailboxPermissions>`_

        **Request Syntax**
        ::

          response = client.put_mailbox_permissions(
              OrganizationId='string',
              EntityId='string',
              GranteeId='string',
              PermissionValues=[
                  'FULL_ACCESS'|'SEND_AS'|'SEND_ON_BEHALF',
              ]
          )
        :type OrganizationId: string
        :param OrganizationId: **[REQUIRED]**

          The identifier of the organization under which the user, group, or resource exists.

        :type EntityId: string
        :param EntityId: **[REQUIRED]**

          The identifier of the user, group, or resource for which to update mailbox permissions.

        :type GranteeId: string
        :param GranteeId: **[REQUIRED]**

          The identifier of the user, group, or resource to which to grant the permissions.

        :type PermissionValues: list
        :param PermissionValues: **[REQUIRED]**

          The permissions granted to the grantee. SEND_AS allows the grantee to send email as the
          owner of the mailbox (the grantee is not mentioned on these emails). SEND_ON_BEHALF allows
          the grantee to send email on behalf of the owner of the mailbox (the grantee is not
          mentioned as the physical sender of these emails). FULL_ACCESS allows the grantee full
          access to the mailbox, irrespective of other folder-level permissions set on the mailbox.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def register_to_work_mail(
        self, OrganizationId: str, EntityId: str, Email: str
    ) -> Dict[str, Any]:
        """
        Registers an existing and disabled user, group, or resource for Amazon WorkMail use by
        associating a mailbox and calendaring capabilities. It performs no change if the user,
        group, or resource is enabled and fails if the user, group, or resource is deleted. This
        operation results in the accumulation of costs. For more information, see `Pricing
        <https://aws.amazon.com//workmail/pricing>`__ . The equivalent console functionality for
        this operation is *Enable* .

        Users can either be created by calling the  CreateUser API operation or they can be
        synchronized from your directory. For more information, see  DeregisterFromWorkMail .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/RegisterToWorkMail>`_

        **Request Syntax**
        ::

          response = client.register_to_work_mail(
              OrganizationId='string',
              EntityId='string',
              Email='string'
          )
        :type OrganizationId: string
        :param OrganizationId: **[REQUIRED]**

          The identifier for the organization under which the user, group, or resource exists.

        :type EntityId: string
        :param EntityId: **[REQUIRED]**

          The identifier for the user, group, or resource to be updated.

        :type Email: string
        :param Email: **[REQUIRED]**

          The email for the user, group, or resource to be updated.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reset_password(self, OrganizationId: str, UserId: str, Password: str) -> Dict[str, Any]:
        """
        Allows the administrator to reset the password for a user.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/ResetPassword>`_

        **Request Syntax**
        ::

          response = client.reset_password(
              OrganizationId='string',
              UserId='string',
              Password='string'
          )
        :type OrganizationId: string
        :param OrganizationId: **[REQUIRED]**

          The identifier of the organization that contains the user for which the password is reset.

        :type UserId: string
        :param UserId: **[REQUIRED]**

          The identifier of the user for whom the password is reset.

        :type Password: string
        :param Password: **[REQUIRED]**

          The new password for the user.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_mailbox_quota(
        self, OrganizationId: str, UserId: str, MailboxQuota: int
    ) -> Dict[str, Any]:
        """
        Updates a user's current mailbox quota for a specified organization and user.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/UpdateMailboxQuota>`_

        **Request Syntax**
        ::

          response = client.update_mailbox_quota(
              OrganizationId='string',
              UserId='string',
              MailboxQuota=123
          )
        :type OrganizationId: string
        :param OrganizationId: **[REQUIRED]**

          The identifier for the organization that contains the user for whom to update the mailbox
          quota.

        :type UserId: string
        :param UserId: **[REQUIRED]**

          The identifer for the user for whom to update the mailbox quota.

        :type MailboxQuota: integer
        :param MailboxQuota: **[REQUIRED]**

          The updated mailbox quota, in MB, for the specified user.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_primary_email_address(
        self, OrganizationId: str, EntityId: str, Email: str
    ) -> Dict[str, Any]:
        """
        Updates the primary email for a user, group, or resource. The current email is moved into
        the list of aliases (or swapped between an existing alias and the current primary email),
        and the email provided in the input is promoted as the primary.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/UpdatePrimaryEmailAddress>`_

        **Request Syntax**
        ::

          response = client.update_primary_email_address(
              OrganizationId='string',
              EntityId='string',
              Email='string'
          )
        :type OrganizationId: string
        :param OrganizationId: **[REQUIRED]**

          The organization that contains the user, group, or resource to update.

        :type EntityId: string
        :param EntityId: **[REQUIRED]**

          The user, group, or resource to update.

        :type Email: string
        :param Email: **[REQUIRED]**

          The value of the email to be updated as primary.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_resource(
        self,
        OrganizationId: str,
        ResourceId: str,
        Name: str = None,
        BookingOptions: ClientUpdateResourceBookingOptionsTypeDef = None,
    ) -> Dict[str, Any]:
        """
        Updates data for the resource. To have the latest information, it must be preceded by a
        DescribeResource call. The dataset in the request should be the one expected when performing
        another ``DescribeResource`` call.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/workmail-2017-10-01/UpdateResource>`_

        **Request Syntax**
        ::

          response = client.update_resource(
              OrganizationId='string',
              ResourceId='string',
              Name='string',
              BookingOptions={
                  'AutoAcceptRequests': True|False,
                  'AutoDeclineRecurringRequests': True|False,
                  'AutoDeclineConflictingRequests': True|False
              }
          )
        :type OrganizationId: string
        :param OrganizationId: **[REQUIRED]**

          The identifier associated with the organization for which the resource is updated.

        :type ResourceId: string
        :param ResourceId: **[REQUIRED]**

          The identifier of the resource to be updated.

        :type Name: string
        :param Name:

          The name of the resource to be updated.

        :type BookingOptions: dict
        :param BookingOptions:

          The resource's booking options to be updated.

          - **AutoAcceptRequests** *(boolean) --*

            The resource's ability to automatically reply to requests. If disabled, delegates must
            be associated to the resource.

          - **AutoDeclineRecurringRequests** *(boolean) --*

            The resource's ability to automatically decline any recurring requests.

          - **AutoDeclineConflictingRequests** *(boolean) --*

            The resource's ability to automatically decline any conflicting requests.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_aliases"]
    ) -> paginator_scope.ListAliasesPaginator:
        """
        Get Paginator for `list_aliases` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_group_members"]
    ) -> paginator_scope.ListGroupMembersPaginator:
        """
        Get Paginator for `list_group_members` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_groups"]
    ) -> paginator_scope.ListGroupsPaginator:
        """
        Get Paginator for `list_groups` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_mailbox_permissions"]
    ) -> paginator_scope.ListMailboxPermissionsPaginator:
        """
        Get Paginator for `list_mailbox_permissions` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_organizations"]
    ) -> paginator_scope.ListOrganizationsPaginator:
        """
        Get Paginator for `list_organizations` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_resource_delegates"]
    ) -> paginator_scope.ListResourceDelegatesPaginator:
        """
        Get Paginator for `list_resource_delegates` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_resources"]
    ) -> paginator_scope.ListResourcesPaginator:
        """
        Get Paginator for `list_resources` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_users"]
    ) -> paginator_scope.ListUsersPaginator:
        """
        Get Paginator for `list_users` operation.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(self, operation_name: str) -> Boto3Paginator:
        """
        Create a paginator for an operation.

        :type operation_name: string
        :param operation_name: The operation name.  This is the same name
            as the method name on the client.  For example, if the
            method name is ``create_foo``, and you'd normally invoke the
            operation as ``client.create_foo(**kwargs)``, if the
            ``create_foo`` operation can be paginated, you can use the
            call ``client.get_paginator("create_foo")``.

        :raise OperationNotPageableError: Raised if the operation is not
            pageable.  You can use the ``client.can_paginate`` method to
            check if an operation is pageable.

        :rtype: L{botocore.paginate.Paginator}
        :return: A paginator object.
        """


class Exceptions:
    ClientError: Boto3ClientError
    DirectoryServiceAuthenticationFailedException: Boto3ClientError
    DirectoryUnavailableException: Boto3ClientError
    EmailAddressInUseException: Boto3ClientError
    EntityAlreadyRegisteredException: Boto3ClientError
    EntityNotFoundException: Boto3ClientError
    EntityStateException: Boto3ClientError
    InvalidConfigurationException: Boto3ClientError
    InvalidParameterException: Boto3ClientError
    InvalidPasswordException: Boto3ClientError
    MailDomainNotFoundException: Boto3ClientError
    MailDomainStateException: Boto3ClientError
    NameAvailabilityException: Boto3ClientError
    OrganizationNotFoundException: Boto3ClientError
    OrganizationStateException: Boto3ClientError
    ReservedNameException: Boto3ClientError
    UnsupportedOperationException: Boto3ClientError
