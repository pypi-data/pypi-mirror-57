"Main interface for ram service Client"
from __future__ import annotations

from typing import Any, Dict, List
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3.type_defs import Literal, overload

# pylint: disable=import-self
import mypy_boto3_ram.client as client_scope

# pylint: disable=import-self
import mypy_boto3_ram.paginator as paginator_scope
from mypy_boto3_ram.type_defs import (
    ClientAcceptResourceShareInvitationResponseTypeDef,
    ClientAssociateResourceSharePermissionResponseTypeDef,
    ClientAssociateResourceShareResponseTypeDef,
    ClientCreateResourceShareResponseTypeDef,
    ClientCreateResourceShareTagsTypeDef,
    ClientDeleteResourceShareResponseTypeDef,
    ClientDisassociateResourceSharePermissionResponseTypeDef,
    ClientDisassociateResourceShareResponseTypeDef,
    ClientEnableSharingWithAwsOrganizationResponseTypeDef,
    ClientGetPermissionResponseTypeDef,
    ClientGetResourcePoliciesResponseTypeDef,
    ClientGetResourceShareAssociationsResponseTypeDef,
    ClientGetResourceShareInvitationsResponseTypeDef,
    ClientGetResourceSharesResponseTypeDef,
    ClientGetResourceSharesTagFiltersTypeDef,
    ClientListPendingInvitationResourcesResponseTypeDef,
    ClientListPermissionsResponseTypeDef,
    ClientListPrincipalsResponseTypeDef,
    ClientListResourceSharePermissionsResponseTypeDef,
    ClientListResourcesResponseTypeDef,
    ClientPromoteResourceShareCreatedFromPolicyResponseTypeDef,
    ClientRejectResourceShareInvitationResponseTypeDef,
    ClientTagResourceTagsTypeDef,
    ClientUpdateResourceShareResponseTypeDef,
)


__all__ = ("Client",)


class Client(BaseClient):
    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def accept_resource_share_invitation(
        self, resourceShareInvitationArn: str, clientToken: str = None
    ) -> ClientAcceptResourceShareInvitationResponseTypeDef:
        """
        Accepts an invitation to a resource share from another AWS account.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/ram-2018-01-04/AcceptResourceShareInvitation>`_

        **Request Syntax**
        ::

          response = client.accept_resource_share_invitation(
              resourceShareInvitationArn='string',
              clientToken='string'
          )
        :type resourceShareInvitationArn: string
        :param resourceShareInvitationArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the invitation.

        :type clientToken: string
        :param clientToken:

          A unique, case-sensitive identifier that you provide to ensure the idempotency of the
          request.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'resourceShareInvitation': {
                    'resourceShareInvitationArn': 'string',
                    'resourceShareName': 'string',
                    'resourceShareArn': 'string',
                    'senderAccountId': 'string',
                    'receiverAccountId': 'string',
                    'invitationTimestamp': datetime(2015, 1, 1),
                    'status': 'PENDING'|'ACCEPTED'|'REJECTED'|'EXPIRED',
                    'resourceShareAssociations': [
                        {
                            'resourceShareArn': 'string',
                            'resourceShareName': 'string',
                            'associatedEntity': 'string',
                            'associationType': 'PRINCIPAL'|'RESOURCE',
                            'status':
                            'ASSOCIATING'|'ASSOCIATED'|'FAILED'|'DISASSOCIATING'
                            |'DISASSOCIATED',
                            'statusMessage': 'string',
                            'creationTime': datetime(2015, 1, 1),
                            'lastUpdatedTime': datetime(2015, 1, 1),
                            'external': True|False
                        },
                    ]
                },
                'clientToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **resourceShareInvitation** *(dict) --*

              Information about the invitation.

              - **resourceShareInvitationArn** *(string) --*

                The Amazon Resource Name (ARN) of the invitation.

              - **resourceShareName** *(string) --*

                The name of the resource share.

              - **resourceShareArn** *(string) --*

                The Amazon Resource Name (ARN) of the resource share.

              - **senderAccountId** *(string) --*

                The ID of the AWS account that sent the invitation.

              - **receiverAccountId** *(string) --*

                The ID of the AWS account that received the invitation.

              - **invitationTimestamp** *(datetime) --*

                The date and time when the invitation was sent.

              - **status** *(string) --*

                The status of the invitation.

              - **resourceShareAssociations** *(list) --*

                To view the resources associated with a pending resource share invitation, use
                `ListPendingInvitationResources
                <https://docs.aws.amazon.com/ram/latest/APIReference/API_ListPendingInvitationResources.html>`__
                .

                - *(dict) --*

                  Describes an association with a resource share.

                  - **resourceShareArn** *(string) --*

                    The Amazon Resource Name (ARN) of the resource share.

                  - **resourceShareName** *(string) --*

                    The name of the resource share.

                  - **associatedEntity** *(string) --*

                    The associated entity. For resource associations, this is the ARN of the
                    resource. For principal associations, this is the ID of an AWS account or the
                    ARN of an OU or organization from AWS Organizations.

                  - **associationType** *(string) --*

                    The association type.

                  - **status** *(string) --*

                    The status of the association.

                  - **statusMessage** *(string) --*

                    A message about the status of the association.

                  - **creationTime** *(datetime) --*

                    The time when the association was created.

                  - **lastUpdatedTime** *(datetime) --*

                    The time when the association was last updated.

                  - **external** *(boolean) --*

                    Indicates whether the principal belongs to the same AWS organization as the AWS
                    account that owns the resource share.

            - **clientToken** *(string) --*

              A unique, case-sensitive identifier that you provide to ensure the idempotency of the
              request.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def associate_resource_share(
        self,
        resourceShareArn: str,
        resourceArns: List[str] = None,
        principals: List[str] = None,
        clientToken: str = None,
    ) -> ClientAssociateResourceShareResponseTypeDef:
        """
        Associates the specified resource share with the specified principals and resources.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/ram-2018-01-04/AssociateResourceShare>`_

        **Request Syntax**
        ::

          response = client.associate_resource_share(
              resourceShareArn='string',
              resourceArns=[
                  'string',
              ],
              principals=[
                  'string',
              ],
              clientToken='string'
          )
        :type resourceShareArn: string
        :param resourceShareArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the resource share.

        :type resourceArns: list
        :param resourceArns:

          The Amazon Resource Names (ARN) of the resources.

          - *(string) --*

        :type principals: list
        :param principals:

          The principals.

          - *(string) --*

        :type clientToken: string
        :param clientToken:

          A unique, case-sensitive identifier that you provide to ensure the idempotency of the
          request.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'resourceShareAssociations': [
                    {
                        'resourceShareArn': 'string',
                        'resourceShareName': 'string',
                        'associatedEntity': 'string',
                        'associationType': 'PRINCIPAL'|'RESOURCE',
                        'status':
                        'ASSOCIATING'|'ASSOCIATED'|'FAILED'|'DISASSOCIATING'
                        |'DISASSOCIATED',
                        'statusMessage': 'string',
                        'creationTime': datetime(2015, 1, 1),
                        'lastUpdatedTime': datetime(2015, 1, 1),
                        'external': True|False
                    },
                ],
                'clientToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **resourceShareAssociations** *(list) --*

              Information about the associations.

              - *(dict) --*

                Describes an association with a resource share.

                - **resourceShareArn** *(string) --*

                  The Amazon Resource Name (ARN) of the resource share.

                - **resourceShareName** *(string) --*

                  The name of the resource share.

                - **associatedEntity** *(string) --*

                  The associated entity. For resource associations, this is the ARN of the resource.
                  For principal associations, this is the ID of an AWS account or the ARN of an OU
                  or organization from AWS Organizations.

                - **associationType** *(string) --*

                  The association type.

                - **status** *(string) --*

                  The status of the association.

                - **statusMessage** *(string) --*

                  A message about the status of the association.

                - **creationTime** *(datetime) --*

                  The time when the association was created.

                - **lastUpdatedTime** *(datetime) --*

                  The time when the association was last updated.

                - **external** *(boolean) --*

                  Indicates whether the principal belongs to the same AWS organization as the AWS
                  account that owns the resource share.

            - **clientToken** *(string) --*

              A unique, case-sensitive identifier that you provide to ensure the idempotency of the
              request.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def associate_resource_share_permission(
        self,
        resourceShareArn: str,
        permissionArn: str,
        replace: bool = None,
        clientToken: str = None,
    ) -> ClientAssociateResourceSharePermissionResponseTypeDef:
        """
        Associates a permission with a resource share.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/ram-2018-01-04/AssociateResourceSharePermission>`_

        **Request Syntax**
        ::

          response = client.associate_resource_share_permission(
              resourceShareArn='string',
              permissionArn='string',
              replace=True|False,
              clientToken='string'
          )
        :type resourceShareArn: string
        :param resourceShareArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the resource share.

        :type permissionArn: string
        :param permissionArn: **[REQUIRED]**

          The ARN of the AWS RAM permission to associate with the resource share.

        :type replace: boolean
        :param replace:

          Indicates whether the permission should replace the permissions that are currently
          associated with the resource share. Use ``true`` to replace the current permissions. Use
          ``false`` to add the permission to the current permission.

        :type clientToken: string
        :param clientToken:

          A unique, case-sensitive identifier that you provide to ensure the idempotency of the
          request.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'returnValue': True|False,
                'clientToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **returnValue** *(boolean) --*

              Indicates whether the request succeeded.

            - **clientToken** *(string) --*

              A unique, case-sensitive identifier that you provide to ensure the idempotency of the
              request.
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
    def create_resource_share(
        self,
        name: str,
        resourceArns: List[str] = None,
        principals: List[str] = None,
        tags: List[ClientCreateResourceShareTagsTypeDef] = None,
        allowExternalPrincipals: bool = None,
        clientToken: str = None,
        permissionArns: List[str] = None,
    ) -> ClientCreateResourceShareResponseTypeDef:
        """
        Creates a resource share.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/ram-2018-01-04/CreateResourceShare>`_

        **Request Syntax**
        ::

          response = client.create_resource_share(
              name='string',
              resourceArns=[
                  'string',
              ],
              principals=[
                  'string',
              ],
              tags=[
                  {
                      'key': 'string',
                      'value': 'string'
                  },
              ],
              allowExternalPrincipals=True|False,
              clientToken='string',
              permissionArns=[
                  'string',
              ]
          )
        :type name: string
        :param name: **[REQUIRED]**

          The name of the resource share.

        :type resourceArns: list
        :param resourceArns:

          The Amazon Resource Names (ARN) of the resources to associate with the resource share.

          - *(string) --*

        :type principals: list
        :param principals:

          The principals to associate with the resource share. The possible values are IDs of AWS
          accounts, the ARN of an OU or organization from AWS Organizations.

          - *(string) --*

        :type tags: list
        :param tags:

          One or more tags.

          - *(dict) --*

            Information about a tag.

            - **key** *(string) --*

              The key of the tag.

            - **value** *(string) --*

              The value of the tag.

        :type allowExternalPrincipals: boolean
        :param allowExternalPrincipals:

          Indicates whether principals outside your AWS organization can be associated with a
          resource share.

        :type clientToken: string
        :param clientToken:

          A unique, case-sensitive identifier that you provide to ensure the idempotency of the
          request.

        :type permissionArns: list
        :param permissionArns:

          The ARNs of the permissions to associate with the resource share. If you do not specify an
          ARN for the permission, AWS RAM automatically attaches the default version of the
          permission for each resource type.

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'resourceShare': {
                    'resourceShareArn': 'string',
                    'name': 'string',
                    'owningAccountId': 'string',
                    'allowExternalPrincipals': True|False,
                    'status': 'PENDING'|'ACTIVE'|'FAILED'|'DELETING'|'DELETED',
                    'statusMessage': 'string',
                    'tags': [
                        {
                            'key': 'string',
                            'value': 'string'
                        },
                    ],
                    'creationTime': datetime(2015, 1, 1),
                    'lastUpdatedTime': datetime(2015, 1, 1),
                    'featureSet': 'CREATED_FROM_POLICY'|'PROMOTING_TO_STANDARD'|'STANDARD'
                },
                'clientToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **resourceShare** *(dict) --*

              Information about the resource share.

              - **resourceShareArn** *(string) --*

                The Amazon Resource Name (ARN) of the resource share.

              - **name** *(string) --*

                The name of the resource share.

              - **owningAccountId** *(string) --*

                The ID of the AWS account that owns the resource share.

              - **allowExternalPrincipals** *(boolean) --*

                Indicates whether principals outside your AWS organization can be associated with a
                resource share.

              - **status** *(string) --*

                The status of the resource share.

              - **statusMessage** *(string) --*

                A message about the status of the resource share.

              - **tags** *(list) --*

                The tags for the resource share.

                - *(dict) --*

                  Information about a tag.

                  - **key** *(string) --*

                    The key of the tag.

                  - **value** *(string) --*

                    The value of the tag.

              - **creationTime** *(datetime) --*

                The time when the resource share was created.

              - **lastUpdatedTime** *(datetime) --*

                The time when the resource share was last updated.

              - **featureSet** *(string) --*

                Indicates how the resource share was created. Possible values include:

                * ``CREATED_FROM_POLICY`` - Indicates that the resource share was created from an
                AWS Identity and Access Management (AWS IAM) policy attached to a resource. These
                resource shares are visible only to the AWS account that created it. They cannot be
                modified in AWS RAM.

                * ``PROMOTING_TO_STANDARD`` - The resource share is in the process of being
                promoted. For more information, see  PromoteResourceShareCreatedFromPolicy .

                * ``STANDARD`` - Indicates that the resource share was created in AWS RAM using the
                console or APIs. These resource shares are visible to all principals. They can be
                modified in AWS RAM.

            - **clientToken** *(string) --*

              A unique, case-sensitive identifier that you provide to ensure the idempotency of the
              request.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_resource_share(
        self, resourceShareArn: str, clientToken: str = None
    ) -> ClientDeleteResourceShareResponseTypeDef:
        """
        Deletes the specified resource share.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/ram-2018-01-04/DeleteResourceShare>`_

        **Request Syntax**
        ::

          response = client.delete_resource_share(
              resourceShareArn='string',
              clientToken='string'
          )
        :type resourceShareArn: string
        :param resourceShareArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the resource share.

        :type clientToken: string
        :param clientToken:

          A unique, case-sensitive identifier that you provide to ensure the idempotency of the
          request.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'returnValue': True|False,
                'clientToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **returnValue** *(boolean) --*

              Indicates whether the request succeeded.

            - **clientToken** *(string) --*

              A unique, case-sensitive identifier that you provide to ensure the idempotency of the
              request.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disassociate_resource_share(
        self,
        resourceShareArn: str,
        resourceArns: List[str] = None,
        principals: List[str] = None,
        clientToken: str = None,
    ) -> ClientDisassociateResourceShareResponseTypeDef:
        """
        Disassociates the specified principals or resources from the specified resource share.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/ram-2018-01-04/DisassociateResourceShare>`_

        **Request Syntax**
        ::

          response = client.disassociate_resource_share(
              resourceShareArn='string',
              resourceArns=[
                  'string',
              ],
              principals=[
                  'string',
              ],
              clientToken='string'
          )
        :type resourceShareArn: string
        :param resourceShareArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the resource share.

        :type resourceArns: list
        :param resourceArns:

          The Amazon Resource Names (ARNs) of the resources.

          - *(string) --*

        :type principals: list
        :param principals:

          The principals.

          - *(string) --*

        :type clientToken: string
        :param clientToken:

          A unique, case-sensitive identifier that you provide to ensure the idempotency of the
          request.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'resourceShareAssociations': [
                    {
                        'resourceShareArn': 'string',
                        'resourceShareName': 'string',
                        'associatedEntity': 'string',
                        'associationType': 'PRINCIPAL'|'RESOURCE',
                        'status':
                        'ASSOCIATING'|'ASSOCIATED'|'FAILED'|'DISASSOCIATING'
                        |'DISASSOCIATED',
                        'statusMessage': 'string',
                        'creationTime': datetime(2015, 1, 1),
                        'lastUpdatedTime': datetime(2015, 1, 1),
                        'external': True|False
                    },
                ],
                'clientToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **resourceShareAssociations** *(list) --*

              Information about the associations.

              - *(dict) --*

                Describes an association with a resource share.

                - **resourceShareArn** *(string) --*

                  The Amazon Resource Name (ARN) of the resource share.

                - **resourceShareName** *(string) --*

                  The name of the resource share.

                - **associatedEntity** *(string) --*

                  The associated entity. For resource associations, this is the ARN of the resource.
                  For principal associations, this is the ID of an AWS account or the ARN of an OU
                  or organization from AWS Organizations.

                - **associationType** *(string) --*

                  The association type.

                - **status** *(string) --*

                  The status of the association.

                - **statusMessage** *(string) --*

                  A message about the status of the association.

                - **creationTime** *(datetime) --*

                  The time when the association was created.

                - **lastUpdatedTime** *(datetime) --*

                  The time when the association was last updated.

                - **external** *(boolean) --*

                  Indicates whether the principal belongs to the same AWS organization as the AWS
                  account that owns the resource share.

            - **clientToken** *(string) --*

              A unique, case-sensitive identifier that you provide to ensure the idempotency of the
              request.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disassociate_resource_share_permission(
        self, resourceShareArn: str, permissionArn: str, clientToken: str = None
    ) -> ClientDisassociateResourceSharePermissionResponseTypeDef:
        """
        Disassociates an AWS RAM permission from a resource share.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/ram-2018-01-04/DisassociateResourceSharePermission>`_

        **Request Syntax**
        ::

          response = client.disassociate_resource_share_permission(
              resourceShareArn='string',
              permissionArn='string',
              clientToken='string'
          )
        :type resourceShareArn: string
        :param resourceShareArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the resource share.

        :type permissionArn: string
        :param permissionArn: **[REQUIRED]**

          The ARN of the permission to disassociate from the resource share.

        :type clientToken: string
        :param clientToken:

          A unique, case-sensitive identifier that you provide to ensure the idempotency of the
          request.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'returnValue': True|False,
                'clientToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **returnValue** *(boolean) --*

              Indicates whether the request succeeded.

            - **clientToken** *(string) --*

              A unique, case-sensitive identifier that you provide to ensure the idempotency of the
              request.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def enable_sharing_with_aws_organization(
        self, *args: Any, **kwargs: Any
    ) -> ClientEnableSharingWithAwsOrganizationResponseTypeDef:
        """
        Enables resource sharing within your AWS Organization.

        The caller must be the master account for the AWS Organization.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/ram-2018-01-04/EnableSharingWithAwsOrganization>`_

        **Request Syntax**
        ::

          response = client.enable_sharing_with_aws_organization()

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'returnValue': True|False
            }
          **Response Structure**

          - *(dict) --*

            - **returnValue** *(boolean) --*

              Indicates whether the request succeeded.
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
    def get_permission(
        self, permissionArn: str, permissionVersion: int = None
    ) -> ClientGetPermissionResponseTypeDef:
        """
        Gets the contents of an AWS RAM permission in JSON format.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/ram-2018-01-04/GetPermission>`_

        **Request Syntax**
        ::

          response = client.get_permission(
              permissionArn='string',
              permissionVersion=123
          )
        :type permissionArn: string
        :param permissionArn: **[REQUIRED]**

          The ARN of the permission.

        :type permissionVersion: integer
        :param permissionVersion:

          The identifier for the version of the permission.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'permission': {
                    'arn': 'string',
                    'version': 'string',
                    'defaultVersion': True|False,
                    'name': 'string',
                    'resourceType': 'string',
                    'permission': 'string',
                    'creationTime': datetime(2015, 1, 1),
                    'lastUpdatedTime': datetime(2015, 1, 1)
                }
            }
          **Response Structure**

          - *(dict) --*

            - **permission** *(dict) --*

              Information about the permission.

              - **arn** *(string) --*

                The ARN of the permission.

              - **version** *(string) --*

                The identifier for the version of the permission.

              - **defaultVersion** *(boolean) --*

                The identifier for the version of the permission that is set as the default version.

              - **name** *(string) --*

                The name of the permission.

              - **resourceType** *(string) --*

                The resource type to which the permission applies.

              - **permission** *(string) --*

                The permission's effect and actions in JSON format. The ``effect`` indicates whether
                the actions are allowed or denied. The ``actions`` list the API actions to which the
                principal is granted or denied access.

              - **creationTime** *(datetime) --*

                The date and time when the permission was created.

              - **lastUpdatedTime** *(datetime) --*

                The date and time when the permission was last updated.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_resource_policies(
        self,
        resourceArns: List[str],
        principal: str = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ClientGetResourcePoliciesResponseTypeDef:
        """
        Gets the policies for the specified resources that you own and have shared.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/ram-2018-01-04/GetResourcePolicies>`_

        **Request Syntax**
        ::

          response = client.get_resource_policies(
              resourceArns=[
                  'string',
              ],
              principal='string',
              nextToken='string',
              maxResults=123
          )
        :type resourceArns: list
        :param resourceArns: **[REQUIRED]**

          The Amazon Resource Names (ARN) of the resources.

          - *(string) --*

        :type principal: string
        :param principal:

          The principal.

        :type nextToken: string
        :param nextToken:

          The token for the next page of results.

        :type maxResults: integer
        :param maxResults:

          The maximum number of results to return with a single call. To retrieve the remaining
          results, make another call with the returned ``nextToken`` value.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'policies': [
                    'string',
                ],
                'nextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **policies** *(list) --*

              A key policy document, in JSON format.

              - *(string) --*

            - **nextToken** *(string) --*

              The token to use to retrieve the next page of results. This value is ``null`` when
              there are no more results to return.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_resource_share_associations(
        self,
        associationType: Literal["PRINCIPAL", "RESOURCE"],
        resourceShareArns: List[str] = None,
        resourceArn: str = None,
        principal: str = None,
        associationStatus: Literal[
            "ASSOCIATING", "ASSOCIATED", "FAILED", "DISASSOCIATING", "DISASSOCIATED"
        ] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ClientGetResourceShareAssociationsResponseTypeDef:
        """
        Gets the resources or principals for the resource shares that you own.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/ram-2018-01-04/GetResourceShareAssociations>`_

        **Request Syntax**
        ::

          response = client.get_resource_share_associations(
              associationType='PRINCIPAL'|'RESOURCE',
              resourceShareArns=[
                  'string',
              ],
              resourceArn='string',
              principal='string',
              associationStatus=
                  'ASSOCIATING'|'ASSOCIATED'|'FAILED'|'DISASSOCIATING'|'DISASSOCIATED',
              nextToken='string',
              maxResults=123
          )
        :type associationType: string
        :param associationType: **[REQUIRED]**

          The association type. Specify ``PRINCIPAL`` to list the principals that are associated
          with the specified resource share. Specify ``RESOURCE`` to list the resources that are
          associated with the specified resource share.

        :type resourceShareArns: list
        :param resourceShareArns:

          The Amazon Resource Names (ARN) of the resource shares.

          - *(string) --*

        :type resourceArn: string
        :param resourceArn:

          The Amazon Resource Name (ARN) of the resource. You cannot specify this parameter if the
          association type is ``PRINCIPAL`` .

        :type principal: string
        :param principal:

          The principal. You cannot specify this parameter if the association type is ``RESOURCE`` .

        :type associationStatus: string
        :param associationStatus:

          The association status.

        :type nextToken: string
        :param nextToken:

          The token for the next page of results.

        :type maxResults: integer
        :param maxResults:

          The maximum number of results to return with a single call. To retrieve the remaining
          results, make another call with the returned ``nextToken`` value.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'resourceShareAssociations': [
                    {
                        'resourceShareArn': 'string',
                        'resourceShareName': 'string',
                        'associatedEntity': 'string',
                        'associationType': 'PRINCIPAL'|'RESOURCE',
                        'status':
                        'ASSOCIATING'|'ASSOCIATED'|'FAILED'|'DISASSOCIATING'
                        |'DISASSOCIATED',
                        'statusMessage': 'string',
                        'creationTime': datetime(2015, 1, 1),
                        'lastUpdatedTime': datetime(2015, 1, 1),
                        'external': True|False
                    },
                ],
                'nextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **resourceShareAssociations** *(list) --*

              Information about the associations.

              - *(dict) --*

                Describes an association with a resource share.

                - **resourceShareArn** *(string) --*

                  The Amazon Resource Name (ARN) of the resource share.

                - **resourceShareName** *(string) --*

                  The name of the resource share.

                - **associatedEntity** *(string) --*

                  The associated entity. For resource associations, this is the ARN of the resource.
                  For principal associations, this is the ID of an AWS account or the ARN of an OU
                  or organization from AWS Organizations.

                - **associationType** *(string) --*

                  The association type.

                - **status** *(string) --*

                  The status of the association.

                - **statusMessage** *(string) --*

                  A message about the status of the association.

                - **creationTime** *(datetime) --*

                  The time when the association was created.

                - **lastUpdatedTime** *(datetime) --*

                  The time when the association was last updated.

                - **external** *(boolean) --*

                  Indicates whether the principal belongs to the same AWS organization as the AWS
                  account that owns the resource share.

            - **nextToken** *(string) --*

              The token to use to retrieve the next page of results. This value is ``null`` when
              there are no more results to return.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_resource_share_invitations(
        self,
        resourceShareInvitationArns: List[str] = None,
        resourceShareArns: List[str] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ClientGetResourceShareInvitationsResponseTypeDef:
        """
        Gets the invitations for resource sharing that you've received.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/ram-2018-01-04/GetResourceShareInvitations>`_

        **Request Syntax**
        ::

          response = client.get_resource_share_invitations(
              resourceShareInvitationArns=[
                  'string',
              ],
              resourceShareArns=[
                  'string',
              ],
              nextToken='string',
              maxResults=123
          )
        :type resourceShareInvitationArns: list
        :param resourceShareInvitationArns:

          The Amazon Resource Names (ARN) of the invitations.

          - *(string) --*

        :type resourceShareArns: list
        :param resourceShareArns:

          The Amazon Resource Names (ARN) of the resource shares.

          - *(string) --*

        :type nextToken: string
        :param nextToken:

          The token for the next page of results.

        :type maxResults: integer
        :param maxResults:

          The maximum number of results to return with a single call. To retrieve the remaining
          results, make another call with the returned ``nextToken`` value.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'resourceShareInvitations': [
                    {
                        'resourceShareInvitationArn': 'string',
                        'resourceShareName': 'string',
                        'resourceShareArn': 'string',
                        'senderAccountId': 'string',
                        'receiverAccountId': 'string',
                        'invitationTimestamp': datetime(2015, 1, 1),
                        'status': 'PENDING'|'ACCEPTED'|'REJECTED'|'EXPIRED',
                        'resourceShareAssociations': [
                            {
                                'resourceShareArn': 'string',
                                'resourceShareName': 'string',
                                'associatedEntity': 'string',
                                'associationType': 'PRINCIPAL'|'RESOURCE',
                                'status':
                                'ASSOCIATING'|'ASSOCIATED'|'FAILED'
                                |'DISASSOCIATING'|'DISASSOCIATED',
                                'statusMessage': 'string',
                                'creationTime': datetime(2015, 1, 1),
                                'lastUpdatedTime': datetime(2015, 1, 1),
                                'external': True|False
                            },
                        ]
                    },
                ],
                'nextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **resourceShareInvitations** *(list) --*

              Information about the invitations.

              - *(dict) --*

                Describes an invitation to join a resource share.

                - **resourceShareInvitationArn** *(string) --*

                  The Amazon Resource Name (ARN) of the invitation.

                - **resourceShareName** *(string) --*

                  The name of the resource share.

                - **resourceShareArn** *(string) --*

                  The Amazon Resource Name (ARN) of the resource share.

                - **senderAccountId** *(string) --*

                  The ID of the AWS account that sent the invitation.

                - **receiverAccountId** *(string) --*

                  The ID of the AWS account that received the invitation.

                - **invitationTimestamp** *(datetime) --*

                  The date and time when the invitation was sent.

                - **status** *(string) --*

                  The status of the invitation.

                - **resourceShareAssociations** *(list) --*

                  To view the resources associated with a pending resource share invitation, use
                  `ListPendingInvitationResources
                  <https://docs.aws.amazon.com/ram/latest/APIReference/API_ListPendingInvitationResources.html>`__
                  .

                  - *(dict) --*

                    Describes an association with a resource share.

                    - **resourceShareArn** *(string) --*

                      The Amazon Resource Name (ARN) of the resource share.

                    - **resourceShareName** *(string) --*

                      The name of the resource share.

                    - **associatedEntity** *(string) --*

                      The associated entity. For resource associations, this is the ARN of the
                      resource. For principal associations, this is the ID of an AWS account or the
                      ARN of an OU or organization from AWS Organizations.

                    - **associationType** *(string) --*

                      The association type.

                    - **status** *(string) --*

                      The status of the association.

                    - **statusMessage** *(string) --*

                      A message about the status of the association.

                    - **creationTime** *(datetime) --*

                      The time when the association was created.

                    - **lastUpdatedTime** *(datetime) --*

                      The time when the association was last updated.

                    - **external** *(boolean) --*

                      Indicates whether the principal belongs to the same AWS organization as the
                      AWS account that owns the resource share.

            - **nextToken** *(string) --*

              The token to use to retrieve the next page of results. This value is ``null`` when
              there are no more results to return.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_resource_shares(
        self,
        resourceOwner: Literal["SELF", "OTHER-ACCOUNTS"],
        resourceShareArns: List[str] = None,
        resourceShareStatus: Literal["PENDING", "ACTIVE", "FAILED", "DELETING", "DELETED"] = None,
        name: str = None,
        tagFilters: List[ClientGetResourceSharesTagFiltersTypeDef] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ClientGetResourceSharesResponseTypeDef:
        """
        Gets the resource shares that you own or the resource shares that are shared with you.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/ram-2018-01-04/GetResourceShares>`_

        **Request Syntax**
        ::

          response = client.get_resource_shares(
              resourceShareArns=[
                  'string',
              ],
              resourceShareStatus='PENDING'|'ACTIVE'|'FAILED'|'DELETING'|'DELETED',
              resourceOwner='SELF'|'OTHER-ACCOUNTS',
              name='string',
              tagFilters=[
                  {
                      'tagKey': 'string',
                      'tagValues': [
                          'string',
                      ]
                  },
              ],
              nextToken='string',
              maxResults=123
          )
        :type resourceShareArns: list
        :param resourceShareArns:

          The Amazon Resource Names (ARN) of the resource shares.

          - *(string) --*

        :type resourceShareStatus: string
        :param resourceShareStatus:

          The status of the resource share.

        :type resourceOwner: string
        :param resourceOwner: **[REQUIRED]**

          The type of owner.

        :type name: string
        :param name:

          The name of the resource share.

        :type tagFilters: list
        :param tagFilters:

          One or more tag filters.

          - *(dict) --*

            Used to filter information based on tags.

            - **tagKey** *(string) --*

              The tag key.

            - **tagValues** *(list) --*

              The tag values.

              - *(string) --*

        :type nextToken: string
        :param nextToken:

          The token for the next page of results.

        :type maxResults: integer
        :param maxResults:

          The maximum number of results to return with a single call. To retrieve the remaining
          results, make another call with the returned ``nextToken`` value.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'resourceShares': [
                    {
                        'resourceShareArn': 'string',
                        'name': 'string',
                        'owningAccountId': 'string',
                        'allowExternalPrincipals': True|False,
                        'status': 'PENDING'|'ACTIVE'|'FAILED'|'DELETING'|'DELETED',
                        'statusMessage': 'string',
                        'tags': [
                            {
                                'key': 'string',
                                'value': 'string'
                            },
                        ],
                        'creationTime': datetime(2015, 1, 1),
                        'lastUpdatedTime': datetime(2015, 1, 1),
                        'featureSet': 'CREATED_FROM_POLICY'|'PROMOTING_TO_STANDARD'|'STANDARD'
                    },
                ],
                'nextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **resourceShares** *(list) --*

              Information about the resource shares.

              - *(dict) --*

                Describes a resource share.

                - **resourceShareArn** *(string) --*

                  The Amazon Resource Name (ARN) of the resource share.

                - **name** *(string) --*

                  The name of the resource share.

                - **owningAccountId** *(string) --*

                  The ID of the AWS account that owns the resource share.

                - **allowExternalPrincipals** *(boolean) --*

                  Indicates whether principals outside your AWS organization can be associated with
                  a resource share.

                - **status** *(string) --*

                  The status of the resource share.

                - **statusMessage** *(string) --*

                  A message about the status of the resource share.

                - **tags** *(list) --*

                  The tags for the resource share.

                  - *(dict) --*

                    Information about a tag.

                    - **key** *(string) --*

                      The key of the tag.

                    - **value** *(string) --*

                      The value of the tag.

                - **creationTime** *(datetime) --*

                  The time when the resource share was created.

                - **lastUpdatedTime** *(datetime) --*

                  The time when the resource share was last updated.

                - **featureSet** *(string) --*

                  Indicates how the resource share was created. Possible values include:

                  * ``CREATED_FROM_POLICY`` - Indicates that the resource share was created from an
                  AWS Identity and Access Management (AWS IAM) policy attached to a resource. These
                  resource shares are visible only to the AWS account that created it. They cannot
                  be modified in AWS RAM.

                  * ``PROMOTING_TO_STANDARD`` - The resource share is in the process of being
                  promoted. For more information, see  PromoteResourceShareCreatedFromPolicy .

                  * ``STANDARD`` - Indicates that the resource share was created in AWS RAM using
                  the console or APIs. These resource shares are visible to all principals. They can
                  be modified in AWS RAM.

            - **nextToken** *(string) --*

              The token to use to retrieve the next page of results. This value is ``null`` when
              there are no more results to return.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_pending_invitation_resources(
        self, resourceShareInvitationArn: str, nextToken: str = None, maxResults: int = None
    ) -> ClientListPendingInvitationResourcesResponseTypeDef:
        """
        Lists the resources in a resource share that is shared with you but that the invitation is
        still pending for.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/ram-2018-01-04/ListPendingInvitationResources>`_

        **Request Syntax**
        ::

          response = client.list_pending_invitation_resources(
              resourceShareInvitationArn='string',
              nextToken='string',
              maxResults=123
          )
        :type resourceShareInvitationArn: string
        :param resourceShareInvitationArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the invitation.

        :type nextToken: string
        :param nextToken:

          The token for the next page of results.

        :type maxResults: integer
        :param maxResults:

          The maximum number of results to return with a single call. To retrieve the remaining
          results, make another call with the returned ``nextToken`` value.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'resources': [
                    {
                        'arn': 'string',
                        'type': 'string',
                        'resourceShareArn': 'string',
                        'resourceGroupArn': 'string',
                        'status':
                        'AVAILABLE'|'ZONAL_RESOURCE_INACCESSIBLE'|'LIMIT_EXCEEDED'
                        |'UNAVAILABLE'|'PENDING',
                        'statusMessage': 'string',
                        'creationTime': datetime(2015, 1, 1),
                        'lastUpdatedTime': datetime(2015, 1, 1)
                    },
                ],
                'nextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **resources** *(list) --*

              Information about the resources included the resource share.

              - *(dict) --*

                Describes a resource associated with a resource share.

                - **arn** *(string) --*

                  The Amazon Resource Name (ARN) of the resource.

                - **type** *(string) --*

                  The resource type.

                - **resourceShareArn** *(string) --*

                  The Amazon Resource Name (ARN) of the resource share.

                - **resourceGroupArn** *(string) --*

                  The ARN of the resource group. This value is returned only if the resource is a
                  resource group.

                - **status** *(string) --*

                  The status of the resource.

                - **statusMessage** *(string) --*

                  A message about the status of the resource.

                - **creationTime** *(datetime) --*

                  The time when the resource was associated with the resource share.

                - **lastUpdatedTime** *(datetime) --*

                  The time when the association was last updated.

            - **nextToken** *(string) --*

              The token to use to retrieve the next page of results. This value is ``null`` when
              there are no more results to return.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_permissions(
        self, resourceType: str = None, nextToken: str = None, maxResults: int = None
    ) -> ClientListPermissionsResponseTypeDef:
        """
        Lists the AWS RAM permissions.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/ram-2018-01-04/ListPermissions>`_

        **Request Syntax**
        ::

          response = client.list_permissions(
              resourceType='string',
              nextToken='string',
              maxResults=123
          )
        :type resourceType: string
        :param resourceType:

          Specifies the resource type for which to list permissions. For example, to list only
          permissions that apply to EC2 subnets, specify ``ec2:Subnet`` .

        :type nextToken: string
        :param nextToken:

          The token for the next page of results.

        :type maxResults: integer
        :param maxResults:

          The maximum number of results to return with a single call. To retrieve the remaining
          results, make another call with the returned ``nextToken`` value.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'permissions': [
                    {
                        'arn': 'string',
                        'version': 'string',
                        'defaultVersion': True|False,
                        'name': 'string',
                        'resourceType': 'string',
                        'status': 'string',
                        'creationTime': datetime(2015, 1, 1),
                        'lastUpdatedTime': datetime(2015, 1, 1)
                    },
                ],
                'nextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **permissions** *(list) --*

              Information about the permissions.

              - *(dict) --*

                Information about a permission that is associated with a resource share.

                - **arn** *(string) --*

                  The ARN of the permission.

                - **version** *(string) --*

                  The identifier for the version of the permission.

                - **defaultVersion** *(boolean) --*

                  The identifier for the version of the permission that is set as the default
                  version.

                - **name** *(string) --*

                  The name of the permission.

                - **resourceType** *(string) --*

                  The type of resource to which the permission applies.

                - **status** *(string) --*

                  The current status of the permission.

                - **creationTime** *(datetime) --*

                  The date and time when the permission was created.

                - **lastUpdatedTime** *(datetime) --*

                  The date and time when the permission was last updated.

            - **nextToken** *(string) --*

              The token to use to retrieve the next page of results. This value is ``null`` when
              there are no more results to return.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_principals(
        self,
        resourceOwner: Literal["SELF", "OTHER-ACCOUNTS"],
        resourceArn: str = None,
        principals: List[str] = None,
        resourceType: str = None,
        resourceShareArns: List[str] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ClientListPrincipalsResponseTypeDef:
        """
        Lists the principals that you have shared resources with or that have shared resources with
        you.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/ram-2018-01-04/ListPrincipals>`_

        **Request Syntax**
        ::

          response = client.list_principals(
              resourceOwner='SELF'|'OTHER-ACCOUNTS',
              resourceArn='string',
              principals=[
                  'string',
              ],
              resourceType='string',
              resourceShareArns=[
                  'string',
              ],
              nextToken='string',
              maxResults=123
          )
        :type resourceOwner: string
        :param resourceOwner: **[REQUIRED]**

          The type of owner.

        :type resourceArn: string
        :param resourceArn:

          The Amazon Resource Name (ARN) of the resource.

        :type principals: list
        :param principals:

          The principals.

          - *(string) --*

        :type resourceType: string
        :param resourceType:

          The resource type.

          Valid values: ``ec2:CapacityReservation`` | ``ec2:Subnet``
          | ``ec2:TrafficMirrorTarget`` |
          ``ec2:TransitGateway`` | ``license-manager:LicenseConfiguration`` | ``rds:Cluster`` |
          ``route53resolver:ResolverRule`` I ``resource-groups:Group``

        :type resourceShareArns: list
        :param resourceShareArns:

          The Amazon Resource Names (ARN) of the resource shares.

          - *(string) --*

        :type nextToken: string
        :param nextToken:

          The token for the next page of results.

        :type maxResults: integer
        :param maxResults:

          The maximum number of results to return with a single call. To retrieve the remaining
          results, make another call with the returned ``nextToken`` value.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'principals': [
                    {
                        'id': 'string',
                        'resourceShareArn': 'string',
                        'creationTime': datetime(2015, 1, 1),
                        'lastUpdatedTime': datetime(2015, 1, 1),
                        'external': True|False
                    },
                ],
                'nextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **principals** *(list) --*

              The principals.

              - *(dict) --*

                Describes a principal for use with AWS Resource Access Manager.

                - **id** *(string) --*

                  The ID of the principal.

                - **resourceShareArn** *(string) --*

                  The Amazon Resource Name (ARN) of the resource share.

                - **creationTime** *(datetime) --*

                  The time when the principal was associated with the resource share.

                - **lastUpdatedTime** *(datetime) --*

                  The time when the association was last updated.

                - **external** *(boolean) --*

                  Indicates whether the principal belongs to the same AWS organization as the AWS
                  account that owns the resource share.

            - **nextToken** *(string) --*

              The token to use to retrieve the next page of results. This value is ``null`` when
              there are no more results to return.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_resource_share_permissions(
        self, resourceShareArn: str, nextToken: str = None, maxResults: int = None
    ) -> ClientListResourceSharePermissionsResponseTypeDef:
        """
        Lists the AWS RAM permissions that are associated with a resource share.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/ram-2018-01-04/ListResourceSharePermissions>`_

        **Request Syntax**
        ::

          response = client.list_resource_share_permissions(
              resourceShareArn='string',
              nextToken='string',
              maxResults=123
          )
        :type resourceShareArn: string
        :param resourceShareArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the resource share.

        :type nextToken: string
        :param nextToken:

          The token for the next page of results.

        :type maxResults: integer
        :param maxResults:

          The maximum number of results to return with a single call. To retrieve the remaining
          results, make another call with the returned ``nextToken`` value.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'permissions': [
                    {
                        'arn': 'string',
                        'version': 'string',
                        'defaultVersion': True|False,
                        'name': 'string',
                        'resourceType': 'string',
                        'status': 'string',
                        'creationTime': datetime(2015, 1, 1),
                        'lastUpdatedTime': datetime(2015, 1, 1)
                    },
                ],
                'nextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **permissions** *(list) --*

              The permissions associated with the resource share.

              - *(dict) --*

                Information about a permission that is associated with a resource share.

                - **arn** *(string) --*

                  The ARN of the permission.

                - **version** *(string) --*

                  The identifier for the version of the permission.

                - **defaultVersion** *(boolean) --*

                  The identifier for the version of the permission that is set as the default
                  version.

                - **name** *(string) --*

                  The name of the permission.

                - **resourceType** *(string) --*

                  The type of resource to which the permission applies.

                - **status** *(string) --*

                  The current status of the permission.

                - **creationTime** *(datetime) --*

                  The date and time when the permission was created.

                - **lastUpdatedTime** *(datetime) --*

                  The date and time when the permission was last updated.

            - **nextToken** *(string) --*

              The token to use to retrieve the next page of results. This value is ``null`` when
              there are no more results to return.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_resources(
        self,
        resourceOwner: Literal["SELF", "OTHER-ACCOUNTS"],
        principal: str = None,
        resourceType: str = None,
        resourceArns: List[str] = None,
        resourceShareArns: List[str] = None,
        nextToken: str = None,
        maxResults: int = None,
    ) -> ClientListResourcesResponseTypeDef:
        """
        Lists the resources that you added to a resource shares or the resources that are shared
        with you.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/ram-2018-01-04/ListResources>`_

        **Request Syntax**
        ::

          response = client.list_resources(
              resourceOwner='SELF'|'OTHER-ACCOUNTS',
              principal='string',
              resourceType='string',
              resourceArns=[
                  'string',
              ],
              resourceShareArns=[
                  'string',
              ],
              nextToken='string',
              maxResults=123
          )
        :type resourceOwner: string
        :param resourceOwner: **[REQUIRED]**

          The type of owner.

        :type principal: string
        :param principal:

          The principal.

        :type resourceType: string
        :param resourceType:

          The resource type.

          Valid values: ``ec2:CapacityReservation`` | ``ec2:Subnet``
          | ``ec2:TrafficMirrorTarget`` |
          ``ec2:TransitGateway`` | ``license-manager:LicenseConfiguration`` | ``rds:Cluster`` |
          ``route53resolver:ResolverRule`` | ``resource-groups:Group``

        :type resourceArns: list
        :param resourceArns:

          The Amazon Resource Names (ARN) of the resources.

          - *(string) --*

        :type resourceShareArns: list
        :param resourceShareArns:

          The Amazon Resource Names (ARN) of the resource shares.

          - *(string) --*

        :type nextToken: string
        :param nextToken:

          The token for the next page of results.

        :type maxResults: integer
        :param maxResults:

          The maximum number of results to return with a single call. To retrieve the remaining
          results, make another call with the returned ``nextToken`` value.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'resources': [
                    {
                        'arn': 'string',
                        'type': 'string',
                        'resourceShareArn': 'string',
                        'resourceGroupArn': 'string',
                        'status':
                        'AVAILABLE'|'ZONAL_RESOURCE_INACCESSIBLE'|'LIMIT_EXCEEDED'
                        |'UNAVAILABLE'|'PENDING',
                        'statusMessage': 'string',
                        'creationTime': datetime(2015, 1, 1),
                        'lastUpdatedTime': datetime(2015, 1, 1)
                    },
                ],
                'nextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **resources** *(list) --*

              Information about the resources.

              - *(dict) --*

                Describes a resource associated with a resource share.

                - **arn** *(string) --*

                  The Amazon Resource Name (ARN) of the resource.

                - **type** *(string) --*

                  The resource type.

                - **resourceShareArn** *(string) --*

                  The Amazon Resource Name (ARN) of the resource share.

                - **resourceGroupArn** *(string) --*

                  The ARN of the resource group. This value is returned only if the resource is a
                  resource group.

                - **status** *(string) --*

                  The status of the resource.

                - **statusMessage** *(string) --*

                  A message about the status of the resource.

                - **creationTime** *(datetime) --*

                  The time when the resource was associated with the resource share.

                - **lastUpdatedTime** *(datetime) --*

                  The time when the association was last updated.

            - **nextToken** *(string) --*

              The token to use to retrieve the next page of results. This value is ``null`` when
              there are no more results to return.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def promote_resource_share_created_from_policy(
        self, resourceShareArn: str
    ) -> ClientPromoteResourceShareCreatedFromPolicyResponseTypeDef:
        """
        Resource shares that were created by attaching a policy to a resource are visible only to
        the resource share owner, and the resource share cannot be modified in AWS RAM.

        Use this API action to promote the resource share. When you promote the resource share, it
        becomes:

        * Visible to all principals that it is shared with.

        * Modifiable in AWS RAM.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/ram-2018-01-04/PromoteResourceShareCreatedFromPolicy>`_

        **Request Syntax**
        ::

          response = client.promote_resource_share_created_from_policy(
              resourceShareArn='string'
          )
        :type resourceShareArn: string
        :param resourceShareArn: **[REQUIRED]**

          The ARN of the resource share to promote.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'returnValue': True|False
            }
          **Response Structure**

          - *(dict) --*

            - **returnValue** *(boolean) --*

              Indicates whether the request succeeded.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reject_resource_share_invitation(
        self, resourceShareInvitationArn: str, clientToken: str = None
    ) -> ClientRejectResourceShareInvitationResponseTypeDef:
        """
        Rejects an invitation to a resource share from another AWS account.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/ram-2018-01-04/RejectResourceShareInvitation>`_

        **Request Syntax**
        ::

          response = client.reject_resource_share_invitation(
              resourceShareInvitationArn='string',
              clientToken='string'
          )
        :type resourceShareInvitationArn: string
        :param resourceShareInvitationArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the invitation.

        :type clientToken: string
        :param clientToken:

          A unique, case-sensitive identifier that you provide to ensure the idempotency of the
          request.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'resourceShareInvitation': {
                    'resourceShareInvitationArn': 'string',
                    'resourceShareName': 'string',
                    'resourceShareArn': 'string',
                    'senderAccountId': 'string',
                    'receiverAccountId': 'string',
                    'invitationTimestamp': datetime(2015, 1, 1),
                    'status': 'PENDING'|'ACCEPTED'|'REJECTED'|'EXPIRED',
                    'resourceShareAssociations': [
                        {
                            'resourceShareArn': 'string',
                            'resourceShareName': 'string',
                            'associatedEntity': 'string',
                            'associationType': 'PRINCIPAL'|'RESOURCE',
                            'status':
                            'ASSOCIATING'|'ASSOCIATED'|'FAILED'|'DISASSOCIATING'
                            |'DISASSOCIATED',
                            'statusMessage': 'string',
                            'creationTime': datetime(2015, 1, 1),
                            'lastUpdatedTime': datetime(2015, 1, 1),
                            'external': True|False
                        },
                    ]
                },
                'clientToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **resourceShareInvitation** *(dict) --*

              Information about the invitation.

              - **resourceShareInvitationArn** *(string) --*

                The Amazon Resource Name (ARN) of the invitation.

              - **resourceShareName** *(string) --*

                The name of the resource share.

              - **resourceShareArn** *(string) --*

                The Amazon Resource Name (ARN) of the resource share.

              - **senderAccountId** *(string) --*

                The ID of the AWS account that sent the invitation.

              - **receiverAccountId** *(string) --*

                The ID of the AWS account that received the invitation.

              - **invitationTimestamp** *(datetime) --*

                The date and time when the invitation was sent.

              - **status** *(string) --*

                The status of the invitation.

              - **resourceShareAssociations** *(list) --*

                To view the resources associated with a pending resource share invitation, use
                `ListPendingInvitationResources
                <https://docs.aws.amazon.com/ram/latest/APIReference/API_ListPendingInvitationResources.html>`__
                .

                - *(dict) --*

                  Describes an association with a resource share.

                  - **resourceShareArn** *(string) --*

                    The Amazon Resource Name (ARN) of the resource share.

                  - **resourceShareName** *(string) --*

                    The name of the resource share.

                  - **associatedEntity** *(string) --*

                    The associated entity. For resource associations, this is the ARN of the
                    resource. For principal associations, this is the ID of an AWS account or the
                    ARN of an OU or organization from AWS Organizations.

                  - **associationType** *(string) --*

                    The association type.

                  - **status** *(string) --*

                    The status of the association.

                  - **statusMessage** *(string) --*

                    A message about the status of the association.

                  - **creationTime** *(datetime) --*

                    The time when the association was created.

                  - **lastUpdatedTime** *(datetime) --*

                    The time when the association was last updated.

                  - **external** *(boolean) --*

                    Indicates whether the principal belongs to the same AWS organization as the AWS
                    account that owns the resource share.

            - **clientToken** *(string) --*

              A unique, case-sensitive identifier that you provide to ensure the idempotency of the
              request.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resource(
        self, resourceShareArn: str, tags: List[ClientTagResourceTagsTypeDef]
    ) -> Dict[str, Any]:
        """
        Adds the specified tags to the specified resource share that you own.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/ram-2018-01-04/TagResource>`_

        **Request Syntax**
        ::

          response = client.tag_resource(
              resourceShareArn='string',
              tags=[
                  {
                      'key': 'string',
                      'value': 'string'
                  },
              ]
          )
        :type resourceShareArn: string
        :param resourceShareArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the resource share.

        :type tags: list
        :param tags: **[REQUIRED]**

          One or more tags.

          - *(dict) --*

            Information about a tag.

            - **key** *(string) --*

              The key of the tag.

            - **value** *(string) --*

              The value of the tag.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_resource(self, resourceShareArn: str, tagKeys: List[str]) -> Dict[str, Any]:
        """
        Removes the specified tags from the specified resource share that you own.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/ram-2018-01-04/UntagResource>`_

        **Request Syntax**
        ::

          response = client.untag_resource(
              resourceShareArn='string',
              tagKeys=[
                  'string',
              ]
          )
        :type resourceShareArn: string
        :param resourceShareArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the resource share.

        :type tagKeys: list
        :param tagKeys: **[REQUIRED]**

          The tag keys of the tags to remove.

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
    def update_resource_share(
        self,
        resourceShareArn: str,
        name: str = None,
        allowExternalPrincipals: bool = None,
        clientToken: str = None,
    ) -> ClientUpdateResourceShareResponseTypeDef:
        """
        Updates the specified resource share that you own.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/ram-2018-01-04/UpdateResourceShare>`_

        **Request Syntax**
        ::

          response = client.update_resource_share(
              resourceShareArn='string',
              name='string',
              allowExternalPrincipals=True|False,
              clientToken='string'
          )
        :type resourceShareArn: string
        :param resourceShareArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the resource share.

        :type name: string
        :param name:

          The name of the resource share.

        :type allowExternalPrincipals: boolean
        :param allowExternalPrincipals:

          Indicates whether principals outside your AWS organization can be associated with a
          resource share.

        :type clientToken: string
        :param clientToken:

          A unique, case-sensitive identifier that you provide to ensure the idempotency of the
          request.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'resourceShare': {
                    'resourceShareArn': 'string',
                    'name': 'string',
                    'owningAccountId': 'string',
                    'allowExternalPrincipals': True|False,
                    'status': 'PENDING'|'ACTIVE'|'FAILED'|'DELETING'|'DELETED',
                    'statusMessage': 'string',
                    'tags': [
                        {
                            'key': 'string',
                            'value': 'string'
                        },
                    ],
                    'creationTime': datetime(2015, 1, 1),
                    'lastUpdatedTime': datetime(2015, 1, 1),
                    'featureSet': 'CREATED_FROM_POLICY'|'PROMOTING_TO_STANDARD'|'STANDARD'
                },
                'clientToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **resourceShare** *(dict) --*

              Information about the resource share.

              - **resourceShareArn** *(string) --*

                The Amazon Resource Name (ARN) of the resource share.

              - **name** *(string) --*

                The name of the resource share.

              - **owningAccountId** *(string) --*

                The ID of the AWS account that owns the resource share.

              - **allowExternalPrincipals** *(boolean) --*

                Indicates whether principals outside your AWS organization can be associated with a
                resource share.

              - **status** *(string) --*

                The status of the resource share.

              - **statusMessage** *(string) --*

                A message about the status of the resource share.

              - **tags** *(list) --*

                The tags for the resource share.

                - *(dict) --*

                  Information about a tag.

                  - **key** *(string) --*

                    The key of the tag.

                  - **value** *(string) --*

                    The value of the tag.

              - **creationTime** *(datetime) --*

                The time when the resource share was created.

              - **lastUpdatedTime** *(datetime) --*

                The time when the resource share was last updated.

              - **featureSet** *(string) --*

                Indicates how the resource share was created. Possible values include:

                * ``CREATED_FROM_POLICY`` - Indicates that the resource share was created from an
                AWS Identity and Access Management (AWS IAM) policy attached to a resource. These
                resource shares are visible only to the AWS account that created it. They cannot be
                modified in AWS RAM.

                * ``PROMOTING_TO_STANDARD`` - The resource share is in the process of being
                promoted. For more information, see  PromoteResourceShareCreatedFromPolicy .

                * ``STANDARD`` - Indicates that the resource share was created in AWS RAM using the
                console or APIs. These resource shares are visible to all principals. They can be
                modified in AWS RAM.

            - **clientToken** *(string) --*

              A unique, case-sensitive identifier that you provide to ensure the idempotency of the
              request.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_resource_policies"]
    ) -> paginator_scope.GetResourcePoliciesPaginator:
        """
        Get Paginator for `get_resource_policies` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_resource_share_associations"]
    ) -> paginator_scope.GetResourceShareAssociationsPaginator:
        """
        Get Paginator for `get_resource_share_associations` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_resource_share_invitations"]
    ) -> paginator_scope.GetResourceShareInvitationsPaginator:
        """
        Get Paginator for `get_resource_share_invitations` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["get_resource_shares"]
    ) -> paginator_scope.GetResourceSharesPaginator:
        """
        Get Paginator for `get_resource_shares` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_principals"]
    ) -> paginator_scope.ListPrincipalsPaginator:
        """
        Get Paginator for `list_principals` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_resources"]
    ) -> paginator_scope.ListResourcesPaginator:
        """
        Get Paginator for `list_resources` operation.
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
    IdempotentParameterMismatchException: Boto3ClientError
    InvalidClientTokenException: Boto3ClientError
    InvalidMaxResultsException: Boto3ClientError
    InvalidNextTokenException: Boto3ClientError
    InvalidParameterException: Boto3ClientError
    InvalidResourceTypeException: Boto3ClientError
    InvalidStateTransitionException: Boto3ClientError
    MalformedArnException: Boto3ClientError
    MissingRequiredParameterException: Boto3ClientError
    OperationNotPermittedException: Boto3ClientError
    ResourceArnNotFoundException: Boto3ClientError
    ResourceShareInvitationAlreadyAcceptedException: Boto3ClientError
    ResourceShareInvitationAlreadyRejectedException: Boto3ClientError
    ResourceShareInvitationArnNotFoundException: Boto3ClientError
    ResourceShareInvitationExpiredException: Boto3ClientError
    ResourceShareLimitExceededException: Boto3ClientError
    ServerInternalException: Boto3ClientError
    ServiceUnavailableException: Boto3ClientError
    TagLimitExceededException: Boto3ClientError
    TagPolicyViolationException: Boto3ClientError
    UnknownResourceException: Boto3ClientError
