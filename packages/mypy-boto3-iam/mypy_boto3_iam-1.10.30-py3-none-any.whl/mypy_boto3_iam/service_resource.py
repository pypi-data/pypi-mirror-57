"Main interface for iam service ServiceResource"
from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List
from boto3.resources.base import ServiceResource as Boto3ServiceResource
from boto3.resources.collection import ResourceCollection
from mypy_boto3.type_defs import Literal

# pylint: disable=import-self
import mypy_boto3_iam.service_resource as service_resource_scope
from mypy_boto3_iam.type_defs import (
    SamlProviderUpdateResponseTypeDef,
    ServiceResourceCreateRoleTagsTypeDef,
    ServiceResourceCreateUserTagsTypeDef,
    UserCreateTagsTypeDef,
)


__all__ = (
    "ServiceResource",
    "AccessKey",
    "AccessKeyPair",
    "AccountPasswordPolicy",
    "AccountSummary",
    "AssumeRolePolicy",
    "CurrentUser",
    "Group",
    "GroupPolicy",
    "InstanceProfile",
    "LoginProfile",
    "MfaDevice",
    "Policy",
    "PolicyVersion",
    "Role",
    "RolePolicy",
    "SamlProvider",
    "ServerCertificate",
    "SigningCertificate",
    "User",
    "UserPolicy",
    "VirtualMfaDevice",
    "ServiceResourceGroupsCollection",
    "ServiceResourceInstanceProfilesCollection",
    "ServiceResourcePoliciesCollection",
    "ServiceResourceRolesCollection",
    "ServiceResourceSamlProvidersCollection",
    "ServiceResourceServerCertificatesCollection",
    "ServiceResourceUsersCollection",
    "ServiceResourceVirtualMfaDevicesCollection",
    "CurrentUserAccessKeysCollection",
    "CurrentUserMfaDevicesCollection",
    "CurrentUserSigningCertificatesCollection",
    "GroupAttachedPoliciesCollection",
    "GroupPoliciesCollection",
    "GroupUsersCollection",
    "PolicyAttachedGroupsCollection",
    "PolicyAttachedRolesCollection",
    "PolicyAttachedUsersCollection",
    "PolicyVersionsCollection",
    "RoleAttachedPoliciesCollection",
    "RoleInstanceProfilesCollection",
    "RolePoliciesCollection",
    "UserAccessKeysCollection",
    "UserAttachedPoliciesCollection",
    "UserGroupsCollection",
    "UserMfaDevicesCollection",
    "UserPoliciesCollection",
    "UserSigningCertificatesCollection",
)


class ServiceResource(Boto3ServiceResource):
    groups: service_resource_scope.ServiceResourceGroupsCollection
    instance_profiles: service_resource_scope.ServiceResourceInstanceProfilesCollection
    policies: service_resource_scope.ServiceResourcePoliciesCollection
    roles: service_resource_scope.ServiceResourceRolesCollection
    saml_providers: service_resource_scope.ServiceResourceSamlProvidersCollection
    server_certificates: service_resource_scope.ServiceResourceServerCertificatesCollection
    users: service_resource_scope.ServiceResourceUsersCollection
    virtual_mfa_devices: service_resource_scope.ServiceResourceVirtualMfaDevicesCollection

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def AccessKey(self, user_name: str, id: str) -> service_resource_scope.AccessKey:
        """
        Creates a AccessKey resource.::

          access_key = iam.AccessKey('user_name','id')

        :type user_name: string
        :param user_name: The AccessKey's user_name identifier. This **must** be set.
        :type id: string
        :param id: The AccessKey's id identifier. This **must** be set.

        :rtype: :py:class:`IAM.AccessKey`
        :returns: A AccessKey resource
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def AccessKeyPair(
        self, user_name: str, id: str, secret: str
    ) -> service_resource_scope.AccessKeyPair:
        """
        Creates a AccessKeyPair resource.::

          access_key_pair = iam.AccessKeyPair('user_name','id','secret')

        :type user_name: string
        :param user_name: The AccessKeyPair's user_name identifier. This **must** be set.
        :type id: string
        :param id: The AccessKeyPair's id identifier. This **must** be set.
        :type secret: string
        :param secret: The AccessKeyPair's secret identifier. This **must** be set.

        :rtype: :py:class:`IAM.AccessKeyPair`
        :returns: A AccessKeyPair resource
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def AccountPasswordPolicy(
        self, *args: Any, **kwargs: Any
    ) -> service_resource_scope.AccountPasswordPolicy:
        """
        Creates a AccountPasswordPolicy resource.::

          account_password_policy = iam.AccountPasswordPolicy()

        :rtype: :py:class:`IAM.AccountPasswordPolicy`
        :returns: A AccountPasswordPolicy resource
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def AccountSummary(self, *args: Any, **kwargs: Any) -> service_resource_scope.AccountSummary:
        """
        Creates a AccountSummary resource.::

          account_summary = iam.AccountSummary()

        :rtype: :py:class:`IAM.AccountSummary`
        :returns: A AccountSummary resource
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def AssumeRolePolicy(self, role_name: str) -> service_resource_scope.AssumeRolePolicy:
        """
        Creates a AssumeRolePolicy resource.::

          assume_role_policy = iam.AssumeRolePolicy('role_name')

        :type role_name: string
        :param role_name: The AssumeRolePolicy's role_name identifier. This **must** be set.

        :rtype: :py:class:`IAM.AssumeRolePolicy`
        :returns: A AssumeRolePolicy resource
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def CurrentUser(self, *args: Any, **kwargs: Any) -> service_resource_scope.CurrentUser:
        """
        Creates a CurrentUser resource.::

          current_user = iam.CurrentUser()

        :rtype: :py:class:`IAM.CurrentUser`
        :returns: A CurrentUser resource
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def Group(self, name: str) -> service_resource_scope.Group:
        """
        Creates a Group resource.::

          group = iam.Group('name')

        :type name: string
        :param name: The Group's name identifier. This **must** be set.

        :rtype: :py:class:`IAM.Group`
        :returns: A Group resource
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def GroupPolicy(self, group_name: str, name: str) -> service_resource_scope.GroupPolicy:
        """
        Creates a GroupPolicy resource.::

          group_policy = iam.GroupPolicy('group_name','name')

        :type group_name: string
        :param group_name: The GroupPolicy's group_name identifier. This **must** be set.
        :type name: string
        :param name: The GroupPolicy's name identifier. This **must** be set.

        :rtype: :py:class:`IAM.GroupPolicy`
        :returns: A GroupPolicy resource
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def InstanceProfile(self, name: str) -> service_resource_scope.InstanceProfile:
        """
        Creates a InstanceProfile resource.::

          instance_profile = iam.InstanceProfile('name')

        :type name: string
        :param name: The InstanceProfile's name identifier. This **must** be set.

        :rtype: :py:class:`IAM.InstanceProfile`
        :returns: A InstanceProfile resource
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def LoginProfile(self, user_name: str) -> service_resource_scope.LoginProfile:
        """
        Creates a LoginProfile resource.::

          login_profile = iam.LoginProfile('user_name')

        :type user_name: string
        :param user_name: The LoginProfile's user_name identifier. This **must** be set.

        :rtype: :py:class:`IAM.LoginProfile`
        :returns: A LoginProfile resource
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def MfaDevice(self, user_name: str, serial_number: str) -> service_resource_scope.MfaDevice:
        """
        Creates a MfaDevice resource.::

          mfa_device = iam.MfaDevice('user_name','serial_number')

        :type user_name: string
        :param user_name: The MfaDevice's user_name identifier. This **must** be set.
        :type serial_number: string
        :param serial_number: The MfaDevice's serial_number identifier. This **must** be set.

        :rtype: :py:class:`IAM.MfaDevice`
        :returns: A MfaDevice resource
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def Policy(self, policy_arn: str) -> service_resource_scope.Policy:
        """
        Creates a Policy resource.::

          policy = iam.Policy('policy_arn')

        :type policy_arn: string
        :param policy_arn: The Policy's policy_arn identifier. This **must** be set.

        :rtype: :py:class:`IAM.Policy`
        :returns: A Policy resource
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def PolicyVersion(self, arn: str, version_id: str) -> service_resource_scope.PolicyVersion:
        """
        Creates a PolicyVersion resource.::

          policy_version = iam.PolicyVersion('arn','version_id')

        :type arn: string
        :param arn: The PolicyVersion's arn identifier. This **must** be set.
        :type version_id: string
        :param version_id: The PolicyVersion's version_id identifier. This **must** be set.

        :rtype: :py:class:`IAM.PolicyVersion`
        :returns: A PolicyVersion resource
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def Role(self, name: str) -> service_resource_scope.Role:
        """
        Creates a Role resource.::

          role = iam.Role('name')

        :type name: string
        :param name: The Role's name identifier. This **must** be set.

        :rtype: :py:class:`IAM.Role`
        :returns: A Role resource
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def RolePolicy(self, role_name: str, name: str) -> service_resource_scope.RolePolicy:
        """
        Creates a RolePolicy resource.::

          role_policy = iam.RolePolicy('role_name','name')

        :type role_name: string
        :param role_name: The RolePolicy's role_name identifier. This **must** be set.
        :type name: string
        :param name: The RolePolicy's name identifier. This **must** be set.

        :rtype: :py:class:`IAM.RolePolicy`
        :returns: A RolePolicy resource
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def SamlProvider(self, arn: str) -> service_resource_scope.SamlProvider:
        """
        Creates a SamlProvider resource.::

          saml_provider = iam.SamlProvider('arn')

        :type arn: string
        :param arn: The SamlProvider's arn identifier. This **must** be set.

        :rtype: :py:class:`IAM.SamlProvider`
        :returns: A SamlProvider resource
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def ServerCertificate(self, name: str) -> service_resource_scope.ServerCertificate:
        """
        Creates a ServerCertificate resource.::

          server_certificate = iam.ServerCertificate('name')

        :type name: string
        :param name: The ServerCertificate's name identifier. This **must** be set.

        :rtype: :py:class:`IAM.ServerCertificate`
        :returns: A ServerCertificate resource
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def SigningCertificate(
        self, user_name: str, id: str
    ) -> service_resource_scope.SigningCertificate:
        """
        Creates a SigningCertificate resource.::

          signing_certificate = iam.SigningCertificate('user_name','id')

        :type user_name: string
        :param user_name: The SigningCertificate's user_name identifier. This **must** be set.
        :type id: string
        :param id: The SigningCertificate's id identifier. This **must** be set.

        :rtype: :py:class:`IAM.SigningCertificate`
        :returns: A SigningCertificate resource
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def User(self, name: str) -> service_resource_scope.User:
        """
        Creates a User resource.::

          user = iam.User('name')

        :type name: string
        :param name: The User's name identifier. This **must** be set.

        :rtype: :py:class:`IAM.User`
        :returns: A User resource
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def UserPolicy(self, user_name: str, name: str) -> service_resource_scope.UserPolicy:
        """
        Creates a UserPolicy resource.::

          user_policy = iam.UserPolicy('user_name','name')

        :type user_name: string
        :param user_name: The UserPolicy's user_name identifier. This **must** be set.
        :type name: string
        :param name: The UserPolicy's name identifier. This **must** be set.

        :rtype: :py:class:`IAM.UserPolicy`
        :returns: A UserPolicy resource
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def VirtualMfaDevice(self, serial_number: str) -> service_resource_scope.VirtualMfaDevice:
        """
        Creates a VirtualMfaDevice resource.::

          virtual_mfa_device = iam.VirtualMfaDevice('serial_number')

        :type serial_number: string
        :param serial_number: The VirtualMfaDevice's serial_number identifier. This **must** be set.

        :rtype: :py:class:`IAM.VirtualMfaDevice`
        :returns: A VirtualMfaDevice resource
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def change_password(self, OldPassword: str, NewPassword: str) -> None:
        """
        Changes the password of the IAM user who is calling this operation. The AWS account root
        user password is not affected by this operation.

        To change the password for a different user, see  UpdateLoginProfile . For more information
        about modifying passwords, see `Managing Passwords
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_ManagingLogins.html>`__ in the *IAM
        User Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ChangePassword>`_

        **Request Syntax**
        ::

          response = iam.change_password(
              OldPassword='string',
              NewPassword='string'
          )
        :type OldPassword: string
        :param OldPassword: **[REQUIRED]**

          The IAM user's current password.

        :type NewPassword: string
        :param NewPassword: **[REQUIRED]**

          The new password. The new password must conform to the AWS account's password policy, if
          one exists.

          The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this
          parameter is a string of characters. That string can include almost any printable ASCII
          character from the space (\\u0020) through the end of the ASCII character range (\\u00FF).
          You can also include the tab (\\u0009), line feed (\\u000A), and carriage return (\\u000D)
          characters. Any of these characters are valid in a password. However, many tools, such as
          the AWS Management Console, might restrict the ability to type certain characters because
          they have special meaning within that tool.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_account_alias(self, AccountAlias: str) -> None:
        """
        Creates an alias for your AWS account. For information about using an AWS account alias, see
        `Using an Alias for Your AWS Account ID
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/AccountAlias.html>`__ in the *IAM User
        Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/CreateAccountAlias>`_

        **Request Syntax**
        ::

          response = iam.create_account_alias(
              AccountAlias='string'
          )
        :type AccountAlias: string
        :param AccountAlias: **[REQUIRED]**

          The account alias to create.

          This parameter allows (through its `regex pattern <http://wikipedia.org/wiki/regex>`__ ) a
          string of characters consisting of lowercase letters, digits, and dashes. You cannot start
          or finish with a dash, nor can you have two dashes in a row.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_account_password_policy(
        self,
        MinimumPasswordLength: int = None,
        RequireSymbols: bool = None,
        RequireNumbers: bool = None,
        RequireUppercaseCharacters: bool = None,
        RequireLowercaseCharacters: bool = None,
        AllowUsersToChangePassword: bool = None,
        MaxPasswordAge: int = None,
        PasswordReusePrevention: int = None,
        HardExpiry: bool = None,
    ) -> service_resource_scope.AccountPasswordPolicy:
        """
        Updates the password policy settings for the AWS account.

        .. note::

          * This operation does not support partial updates. No parameters are required, but if you
          do not specify a parameter, that parameter's value reverts to its default value. See the
          **Request Parameters** section for each parameter's default value. Also note that some
          parameters do not allow the default parameter to be explicitly set. Instead, to invoke the
          default value, do not include that parameter when you invoke the operation.

        For more information about using a password policy, see `Managing an IAM Password Policy
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_ManagingPasswordPolicies.html>`__ in
        the *IAM User Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/UpdateAccountPasswordPolicy>`_

        **Request Syntax**
        ::

          account_password_policy = iam.create_account_password_policy(
              MinimumPasswordLength=123,
              RequireSymbols=True|False,
              RequireNumbers=True|False,
              RequireUppercaseCharacters=True|False,
              RequireLowercaseCharacters=True|False,
              AllowUsersToChangePassword=True|False,
              MaxPasswordAge=123,
              PasswordReusePrevention=123,
              HardExpiry=True|False
          )
        :type MinimumPasswordLength: integer
        :param MinimumPasswordLength:

          The minimum number of characters allowed in an IAM user password.

          If you do not specify a value for this parameter, then the operation uses the default
          value of ``6`` .

        :type RequireSymbols: boolean
        :param RequireSymbols:

          Specifies whether IAM user passwords must contain at least one of the following
          non-alphanumeric characters:

          ! @ # $ % ^ & * ( ) _ + - = [ ] { } | '

          If you do not specify a value for this parameter, then the operation uses the default
          value of ``false`` . The result is that passwords do not require at least one symbol
          character.

        :type RequireNumbers: boolean
        :param RequireNumbers:

          Specifies whether IAM user passwords must contain at least one numeric character (0 to 9).

          If you do not specify a value for this parameter, then the operation uses the default
          value of ``false`` . The result is that passwords do not require at least one numeric
          character.

        :type RequireUppercaseCharacters: boolean
        :param RequireUppercaseCharacters:

          Specifies whether IAM user passwords must contain at least one uppercase character from
          the ISO basic Latin alphabet (A to Z).

          If you do not specify a value for this parameter, then the operation uses the default
          value of ``false`` . The result is that passwords do not require at least one uppercase
          character.

        :type RequireLowercaseCharacters: boolean
        :param RequireLowercaseCharacters:

          Specifies whether IAM user passwords must contain at least one lowercase character from
          the ISO basic Latin alphabet (a to z).

          If you do not specify a value for this parameter, then the operation uses the default
          value of ``false`` . The result is that passwords do not require at least one lowercase
          character.

        :type AllowUsersToChangePassword: boolean
        :param AllowUsersToChangePassword:

          Allows all IAM users in your account to use the AWS Management Console to change their own
          passwords. For more information, see `Letting IAM Users Change Their Own Passwords
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/HowToPwdIAMUser.html>`__ in the *IAM
          User Guide* .

          If you do not specify a value for this parameter, then the operation uses the default
          value of ``false`` . The result is that IAM users in the account do not automatically have
          permissions to change their own password.

        :type MaxPasswordAge: integer
        :param MaxPasswordAge:

          The number of days that an IAM user password is valid.

          If you do not specify a value for this parameter, then the operation uses the default
          value of ``0`` . The result is that IAM user passwords never expire.

        :type PasswordReusePrevention: integer
        :param PasswordReusePrevention:

          Specifies the number of previous passwords that IAM users are prevented from reusing.

          If you do not specify a value for this parameter, then the operation uses the default
          value of ``0`` . The result is that IAM users are not prevented from reusing previous
          passwords.

        :type HardExpiry: boolean
        :param HardExpiry:

          Prevents IAM users from setting a new password after their password has expired. The IAM
          user cannot be accessed until an administrator resets the password.

          If you do not specify a value for this parameter, then the operation uses the default
          value of ``false`` . The result is that IAM users can change their passwords after they
          expire and continue to sign in as the user.

        :rtype: :py:class:`iam.AccountPasswordPolicy`
        :returns: AccountPasswordPolicy resource
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_group(self, GroupName: str, Path: str = None) -> List[service_resource_scope.Group]:
        """
        Creates a new group.

        For information about the number of groups you can create, see `Limitations on IAM Entities
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/LimitationsOnEntities.html>`__ in the *IAM
        User Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/CreateGroup>`_

        **Request Syntax**
        ::

          group = iam.create_group(
              Path='string',
              GroupName='string'
          )
        :type Path: string
        :param Path:

          The path to the group. For more information about paths, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .

          This parameter is optional. If it is not included, it defaults to a slash (/).

          This parameter allows (through its `regex pattern <http://wikipedia.org/wiki/regex>`__ ) a
          string of characters consisting of either a forward slash (/) by itself or a string that
          must begin and end with forward slashes. In addition, it can contain any ASCII character
          from the ! (\\u0021) through the DEL character (\\u007F), including most punctuation
          characters, digits, and upper and lowercased letters.

        :type GroupName: string
        :param GroupName: **[REQUIRED]**

          The name of the group to create. Do not include the path in this value.

          IAM user, group, role, and policy names must be unique within the account. Names are not
          distinguished by case. For example, you cannot create resources named both "MyResource"
          and "myresource".

        :rtype: :py:class:`iam.Group`
        :returns: Group resource
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_instance_profile(
        self, InstanceProfileName: str, Path: str = None
    ) -> service_resource_scope.InstanceProfile:
        """
        Creates a new instance profile. For information about instance profiles, go to `About
        Instance Profiles
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/AboutInstanceProfiles.html>`__ .

        For information about the number of instance profiles you can create, see `Limitations on
        IAM Entities
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/LimitationsOnEntities.html>`__ in the *IAM
        User Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/CreateInstanceProfile>`_

        **Request Syntax**
        ::

          instance_profile = iam.create_instance_profile(
              InstanceProfileName='string',
              Path='string'
          )
        :type InstanceProfileName: string
        :param InstanceProfileName: **[REQUIRED]**

          The name of the instance profile to create.

          This parameter allows (through its `regex pattern <http://wikipedia.org/wiki/regex>`__ ) a
          string of characters consisting of upper and lowercase alphanumeric characters with no
          spaces. You can also include any of the following characters: _+=,.@-

        :type Path: string
        :param Path:

          The path to the instance profile. For more information about paths, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .

          This parameter is optional. If it is not included, it defaults to a slash (/).

          This parameter allows (through its `regex pattern <http://wikipedia.org/wiki/regex>`__ ) a
          string of characters consisting of either a forward slash (/) by itself or a string that
          must begin and end with forward slashes. In addition, it can contain any ASCII character
          from the ! (\\u0021) through the DEL character (\\u007F), including most punctuation
          characters, digits, and upper and lowercased letters.

        :rtype: :py:class:`iam.InstanceProfile`
        :returns: InstanceProfile resource
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_policy(
        self, PolicyName: str, PolicyDocument: str, Path: str = None, Description: str = None
    ) -> service_resource_scope.Policy:
        """
        Creates a new managed policy for your AWS account.

        This operation creates a policy version with a version identifier of ``v1`` and sets v1 as
        the policy's default version. For more information about policy versions, see `Versioning
        for Managed Policies
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-versions.html>`__ in the
        *IAM User Guide* .

        For more information about managed policies in general, see `Managed Policies and Inline
        Policies
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in the
        *IAM User Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/CreatePolicy>`_

        **Request Syntax**
        ::

          policy = iam.create_policy(
              PolicyName='string',
              Path='string',
              PolicyDocument='string',
              Description='string'
          )
        :type PolicyName: string
        :param PolicyName: **[REQUIRED]**

          The friendly name of the policy.

          IAM user, group, role, and policy names must be unique within the account. Names are not
          distinguished by case. For example, you cannot create resources named both "MyResource"
          and "myresource".

        :type Path: string
        :param Path:

          The path for the policy.

          For more information about paths, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .

          This parameter is optional. If it is not included, it defaults to a slash (/).

          This parameter allows (through its `regex pattern <http://wikipedia.org/wiki/regex>`__ ) a
          string of characters consisting of either a forward slash (/) by itself or a string that
          must begin and end with forward slashes. In addition, it can contain any ASCII character
          from the ! (\\u0021) through the DEL character (\\u007F), including most punctuation
          characters, digits, and upper and lowercased letters.

        :type PolicyDocument: string
        :param PolicyDocument: **[REQUIRED]**

          The JSON policy document that you want to use as the content for the new policy.

          You must provide policies in JSON format in IAM. However, for AWS CloudFormation templates
          formatted in YAML, you can provide the policy in JSON or YAML format. AWS CloudFormation
          always converts a YAML policy to JSON format before submitting it to IAM.

          The `regex pattern <http://wikipedia.org/wiki/regex>`__ used to validate this parameter is
          a string of characters consisting of the following:

          * Any printable ASCII character ranging from the space character (\\u0020) through the end
          of the ASCII character range

          * The printable characters in the Basic Latin and Latin-1 Supplement character set
          (through \\u00FF)

          * The special characters tab (\\u0009), line feed (\\u000A), and carriage return (\\u000D)

        :type Description: string
        :param Description:

          A friendly description of the policy.

          Typically used to store information about the permissions defined in the policy. For
          example, "Grants access to production DynamoDB tables."

          The policy description is immutable. After a value is assigned, it cannot be changed.

        :rtype: :py:class:`iam.Policy`
        :returns: Policy resource
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_role(
        self,
        RoleName: str,
        AssumeRolePolicyDocument: str,
        Path: str = None,
        Description: str = None,
        MaxSessionDuration: int = None,
        PermissionsBoundary: str = None,
        Tags: List[ServiceResourceCreateRoleTagsTypeDef] = None,
    ) -> service_resource_scope.Role:
        """
        Creates a new role for your AWS account. For more information about roles, go to `IAM Roles
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/WorkingWithRoles.html>`__ . For
        information about limitations on role names and the number of roles you can create, go to
        `Limitations on IAM Entities
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/LimitationsOnEntities.html>`__ in the *IAM
        User Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/CreateRole>`_

        **Request Syntax**
        ::

          role = iam.create_role(
              Path='string',
              RoleName='string',
              AssumeRolePolicyDocument='string',
              Description='string',
              MaxSessionDuration=123,
              PermissionsBoundary='string',
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ]
          )
        :type Path: string
        :param Path:

          The path to the role. For more information about paths, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .

          This parameter is optional. If it is not included, it defaults to a slash (/).

          This parameter allows (through its `regex pattern <http://wikipedia.org/wiki/regex>`__ ) a
          string of characters consisting of either a forward slash (/) by itself or a string that
          must begin and end with forward slashes. In addition, it can contain any ASCII character
          from the ! (\\u0021) through the DEL character (\\u007F), including most punctuation
          characters, digits, and upper and lowercased letters.

        :type RoleName: string
        :param RoleName: **[REQUIRED]**

          The name of the role to create.

          IAM user, group, role, and policy names must be unique within the account. Names are not
          distinguished by case. For example, you cannot create resources named both "MyResource"
          and "myresource".

        :type AssumeRolePolicyDocument: string
        :param AssumeRolePolicyDocument: **[REQUIRED]**

          The trust relationship policy document that grants an entity permission to assume the
          role.

          In IAM, you must provide a JSON policy that has been converted to a string. However, for
          AWS CloudFormation templates formatted in YAML, you can provide the policy in JSON or YAML
          format. AWS CloudFormation always converts a YAML policy to JSON format before submitting
          it to IAM.

          The `regex pattern <http://wikipedia.org/wiki/regex>`__ used to validate this parameter is
          a string of characters consisting of the following:

          * Any printable ASCII character ranging from the space character (\\u0020) through the end
          of the ASCII character range

          * The printable characters in the Basic Latin and Latin-1 Supplement character set
          (through \\u00FF)

          * The special characters tab (\\u0009), line feed (\\u000A), and carriage return (\\u000D)

          Upon success, the response includes the same trust policy in JSON format.

        :type Description: string
        :param Description:

          A description of the role.

        :type MaxSessionDuration: integer
        :param MaxSessionDuration:

          The maximum session duration (in seconds) that you want to set for the specified role. If
          you do not specify a value for this setting, the default maximum of one hour is applied.
          This setting can have a value from 1 hour to 12 hours.

          Anyone who assumes the role from the AWS CLI or API can use the ``DurationSeconds`` API
          parameter or the ``duration-seconds`` CLI parameter to request a longer session. The
          ``MaxSessionDuration`` setting determines the maximum duration that can be requested using
          the ``DurationSeconds`` parameter. If users don't specify a value for the
          ``DurationSeconds`` parameter, their security credentials are valid for one hour by
          default. This applies when you use the ``AssumeRole*`` API operations or the
          ``assume-role*`` CLI operations but does not apply when you use those operations to create
          a console URL. For more information, see `Using IAM Roles
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use.html>`__ in the *IAM User
          Guide* .

        :type PermissionsBoundary: string
        :param PermissionsBoundary:

          The ARN of the policy that is used to set the permissions boundary for the role.

        :type Tags: list
        :param Tags:

          A list of tags that you want to attach to the newly created role. Each tag consists of a
          key name and an associated value. For more information about tagging, see `Tagging IAM
          Identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM
          User Guide* .

          .. note::

            If any one of the tags is invalid or if you exceed the allowed number of tags per role,
            then the entire request fails and the role is not created.

          - *(dict) --*

            A structure that represents user-provided metadata that can be associated with a
            resource such as an IAM user or role. For more information about tagging, see `Tagging
            IAM Identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the
            *IAM User Guide* .

            - **Key** *(string) --* **[REQUIRED]**

              The key name that can be used to look up or retrieve the associated value. For
              example, ``Department`` or ``Cost Center`` are common choices.

            - **Value** *(string) --* **[REQUIRED]**

              The value associated with this tag. For example, tags with a key name of
              ``Department`` could have values such as ``Human Resources`` , ``Accounting`` , and
              ``Support`` . Tags with a key name of ``Cost Center`` might have values that consist
              of the number associated with the different cost centers in your company. Typically,
              many resources have tags with the same key name but with different values.

              .. note::

                AWS always interprets the tag ``Value`` as a single string. If you need to store an
                array, you can store comma-separated values in the string. However, you must
                interpret the value in your code.

        :rtype: :py:class:`iam.Role`
        :returns: Role resource
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_saml_provider(
        self, SAMLMetadataDocument: str, Name: str
    ) -> service_resource_scope.SamlProvider:
        """
        Creates an IAM resource that describes an identity provider (IdP) that supports SAML 2.0.

        The SAML provider resource that you create with this operation can be used as a principal in
        an IAM role's trust policy. Such a policy can enable federated users who sign in using the
        SAML IdP to assume the role. You can create an IAM role that supports Web-based single
        sign-on (SSO) to the AWS Management Console or one that supports API access to AWS.

        When you create the SAML provider resource, you upload a SAML metadata document that you get
        from your IdP. That document includes the issuer's name, expiration information, and keys
        that can be used to validate the SAML authentication response (assertions) that the IdP
        sends. You must generate the metadata document using the identity management software that
        is used as your organization's IdP.

        .. note::

          This operation requires `Signature Version 4
          <https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html>`__ .

        For more information, see `Enabling SAML 2.0 Federated Users to Access the AWS Management
        Console
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_enable-console-saml.html>`__
        and `About SAML 2.0-based Federation
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_saml.html>`__ in the
        *IAM User Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/CreateSAMLProvider>`_

        **Request Syntax**
        ::

          saml_provider = iam.create_saml_provider(
              SAMLMetadataDocument='string',
              Name='string'
          )
        :type SAMLMetadataDocument: string
        :param SAMLMetadataDocument: **[REQUIRED]**

          An XML document generated by an identity provider (IdP) that supports SAML 2.0. The
          document includes the issuer's name, expiration information, and keys that can be used to
          validate the SAML authentication response (assertions) that are received from the IdP. You
          must generate the metadata document using the identity management software that is used as
          your organization's IdP.

          For more information, see `About SAML 2.0-based Federation
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_saml.html>`__ in the
          *IAM User Guide*

        :type Name: string
        :param Name: **[REQUIRED]**

          The name of the provider to create.

          This parameter allows (through its `regex pattern <http://wikipedia.org/wiki/regex>`__ ) a
          string of characters consisting of upper and lowercase alphanumeric characters with no
          spaces. You can also include any of the following characters: _+=,.@-

        :rtype: :py:class:`iam.SamlProvider`
        :returns: SamlProvider resource
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_server_certificate(
        self,
        ServerCertificateName: str,
        CertificateBody: str,
        PrivateKey: str,
        Path: str = None,
        CertificateChain: str = None,
    ) -> service_resource_scope.ServerCertificate:
        """
        Uploads a server certificate entity for the AWS account. The server certificate entity
        includes a public key certificate, a private key, and an optional certificate chain, which
        should all be PEM-encoded.

        We recommend that you use `AWS Certificate Manager <https://docs.aws.amazon.com/acm/>`__ to
        provision, manage, and deploy your server certificates. With ACM you can request a
        certificate, deploy it to AWS resources, and let ACM handle certificate renewals for you.
        Certificates provided by ACM are free. For more information about using ACM, see the `AWS
        Certificate Manager User Guide <https://docs.aws.amazon.com/acm/latest/userguide/>`__ .

        For more information about working with server certificates, see `Working with Server
        Certificates
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_server-certs.html>`__ in
        the *IAM User Guide* . This topic includes a list of AWS services that can use the server
        certificates that you manage with IAM.

        For information about the number of server certificates you can upload, see `Limitations on
        IAM Entities and Objects
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-limits.html>`__ in the *IAM
        User Guide* .

        .. note::

          Because the body of the public key certificate, private key, and the certificate chain can
          be large, you should use POST rather than GET when calling ``UploadServerCertificate`` .
          For information about setting up signatures and authorization through the API, go to
          `Signing AWS API Requests
          <https://docs.aws.amazon.com/general/latest/gr/signing_aws_api_requests.html>`__ in the
          *AWS General Reference* . For general information about using the Query API with IAM, go
          to `Calling the API by Making HTTP Query Requests
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/programming.html>`__ in the *IAM User
          Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/UploadServerCertificate>`_

        **Request Syntax**
        ::

          server_certificate = iam.create_server_certificate(
              Path='string',
              ServerCertificateName='string',
              CertificateBody='string',
              PrivateKey='string',
              CertificateChain='string'
          )
        :type Path: string
        :param Path:

          The path for the server certificate. For more information about paths, see `IAM
          Identifiers <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__
          in the *IAM User Guide* .

          This parameter is optional. If it is not included, it defaults to a slash (/). This
          parameter allows (through its `regex pattern <http://wikipedia.org/wiki/regex>`__ ) a
          string of characters consisting of either a forward slash (/) by itself or a string that
          must begin and end with forward slashes. In addition, it can contain any ASCII character
          from the ! (\\u0021) through the DEL character (\\u007F), including most punctuation
          characters, digits, and upper and lowercased letters.

          .. note::

            If you are uploading a server certificate specifically for use with Amazon CloudFront
            distributions, you must specify a path using the ``path`` parameter. The path must begin
            with ``/cloudfront`` and must include a trailing slash (for example,
            ``/cloudfront/test/`` ).

        :type ServerCertificateName: string
        :param ServerCertificateName: **[REQUIRED]**

          The name for the server certificate. Do not include the path in this value. The name of
          the certificate cannot contain any spaces.

          This parameter allows (through its `regex pattern <http://wikipedia.org/wiki/regex>`__ ) a
          string of characters consisting of upper and lowercase alphanumeric characters with no
          spaces. You can also include any of the following characters: _+=,.@-

        :type CertificateBody: string
        :param CertificateBody: **[REQUIRED]**

          The contents of the public key certificate in PEM-encoded format.

          The `regex pattern <http://wikipedia.org/wiki/regex>`__ used to validate this parameter is
          a string of characters consisting of the following:

          * Any printable ASCII character ranging from the space character (\\u0020) through the end
          of the ASCII character range

          * The printable characters in the Basic Latin and Latin-1 Supplement character set
          (through \\u00FF)

          * The special characters tab (\\u0009), line feed (\\u000A), and carriage return (\\u000D)

        :type PrivateKey: string
        :param PrivateKey: **[REQUIRED]**

          The contents of the private key in PEM-encoded format.

          The `regex pattern <http://wikipedia.org/wiki/regex>`__ used to validate this parameter is
          a string of characters consisting of the following:

          * Any printable ASCII character ranging from the space character (\\u0020) through the end
          of the ASCII character range

          * The printable characters in the Basic Latin and Latin-1 Supplement character set
          (through \\u00FF)

          * The special characters tab (\\u0009), line feed (\\u000A), and carriage return (\\u000D)

        :type CertificateChain: string
        :param CertificateChain:

          The contents of the certificate chain. This is typically a concatenation of the
          PEM-encoded public key certificates of the chain.

          The `regex pattern <http://wikipedia.org/wiki/regex>`__ used to validate this parameter is
          a string of characters consisting of the following:

          * Any printable ASCII character ranging from the space character (\\u0020) through the end
          of the ASCII character range

          * The printable characters in the Basic Latin and Latin-1 Supplement character set
          (through \\u00FF)

          * The special characters tab (\\u0009), line feed (\\u000A), and carriage return (\\u000D)

        :rtype: :py:class:`iam.ServerCertificate`
        :returns: ServerCertificate resource
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_signing_certificate(
        self, CertificateBody: str, UserName: str = None
    ) -> service_resource_scope.SigningCertificate:
        """
        Uploads an X.509 signing certificate and associates it with the specified IAM user. Some AWS
        services use X.509 signing certificates to validate requests that are signed with a
        corresponding private key. When you upload the certificate, its default status is ``Active``
        .

        If the ``UserName`` is not specified, the IAM user name is determined implicitly based on
        the AWS access key ID used to sign the request. This operation works for access keys under
        the AWS account. Consequently, you can use this operation to manage AWS account root user
        credentials even if the AWS account has no associated users.

        .. note::

          Because the body of an X.509 certificate can be large, you should use POST rather than GET
          when calling ``UploadSigningCertificate`` . For information about setting up signatures
          and authorization through the API, go to `Signing AWS API Requests
          <https://docs.aws.amazon.com/general/latest/gr/signing_aws_api_requests.html>`__ in the
          *AWS General Reference* . For general information about using the Query API with IAM, go
          to `Making Query Requests
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/IAM_UsingQueryAPI.html>`__ in the *IAM
          User Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/UploadSigningCertificate>`_

        **Request Syntax**
        ::

          signing_certificate = iam.create_signing_certificate(
              UserName='string',
              CertificateBody='string'
          )
        :type UserName: string
        :param UserName:

          The name of the user the signing certificate is for.

          This parameter allows (through its `regex pattern <http://wikipedia.org/wiki/regex>`__ ) a
          string of characters consisting of upper and lowercase alphanumeric characters with no
          spaces. You can also include any of the following characters: _+=,.@-

        :type CertificateBody: string
        :param CertificateBody: **[REQUIRED]**

          The contents of the signing certificate.

          The `regex pattern <http://wikipedia.org/wiki/regex>`__ used to validate this parameter is
          a string of characters consisting of the following:

          * Any printable ASCII character ranging from the space character (\\u0020) through the end
          of the ASCII character range

          * The printable characters in the Basic Latin and Latin-1 Supplement character set
          (through \\u00FF)

          * The special characters tab (\\u0009), line feed (\\u000A), and carriage return (\\u000D)

        :rtype: :py:class:`iam.SigningCertificate`
        :returns: SigningCertificate resource
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_user(
        self,
        UserName: str,
        Path: str = None,
        PermissionsBoundary: str = None,
        Tags: List[ServiceResourceCreateUserTagsTypeDef] = None,
    ) -> service_resource_scope.User:
        """
        Creates a new IAM user for your AWS account.

        For information about limitations on the number of IAM users you can create, see
        `Limitations on IAM Entities
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/LimitationsOnEntities.html>`__ in the *IAM
        User Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/CreateUser>`_

        **Request Syntax**
        ::

          user = iam.create_user(
              Path='string',
              UserName='string',
              PermissionsBoundary='string',
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ]
          )
        :type Path: string
        :param Path:

          The path for the user name. For more information about paths, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .

          This parameter is optional. If it is not included, it defaults to a slash (/).

          This parameter allows (through its `regex pattern <http://wikipedia.org/wiki/regex>`__ ) a
          string of characters consisting of either a forward slash (/) by itself or a string that
          must begin and end with forward slashes. In addition, it can contain any ASCII character
          from the ! (\\u0021) through the DEL character (\\u007F), including most punctuation
          characters, digits, and upper and lowercased letters.

        :type UserName: string
        :param UserName: **[REQUIRED]**

          The name of the user to create.

          IAM user, group, role, and policy names must be unique within the account. Names are not
          distinguished by case. For example, you cannot create resources named both "MyResource"
          and "myresource".

        :type PermissionsBoundary: string
        :param PermissionsBoundary:

          The ARN of the policy that is used to set the permissions boundary for the user.

        :type Tags: list
        :param Tags:

          A list of tags that you want to attach to the newly created user. Each tag consists of a
          key name and an associated value. For more information about tagging, see `Tagging IAM
          Identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM
          User Guide* .

          .. note::

            If any one of the tags is invalid or if you exceed the allowed number of tags per user,
            then the entire request fails and the user is not created.

          - *(dict) --*

            A structure that represents user-provided metadata that can be associated with a
            resource such as an IAM user or role. For more information about tagging, see `Tagging
            IAM Identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the
            *IAM User Guide* .

            - **Key** *(string) --* **[REQUIRED]**

              The key name that can be used to look up or retrieve the associated value. For
              example, ``Department`` or ``Cost Center`` are common choices.

            - **Value** *(string) --* **[REQUIRED]**

              The value associated with this tag. For example, tags with a key name of
              ``Department`` could have values such as ``Human Resources`` , ``Accounting`` , and
              ``Support`` . Tags with a key name of ``Cost Center`` might have values that consist
              of the number associated with the different cost centers in your company. Typically,
              many resources have tags with the same key name but with different values.

              .. note::

                AWS always interprets the tag ``Value`` as a single string. If you need to store an
                array, you can store comma-separated values in the string. However, you must
                interpret the value in your code.

        :rtype: :py:class:`iam.User`
        :returns: User resource
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_virtual_mfa_device(
        self, VirtualMFADeviceName: str, Path: str = None
    ) -> service_resource_scope.VirtualMfaDevice:
        """
        Creates a new virtual MFA device for the AWS account. After creating the virtual MFA, use
        EnableMFADevice to attach the MFA device to an IAM user. For more information about creating
        and working with virtual MFA devices, go to `Using a Virtual MFA Device
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_VirtualMFA.html>`__ in the *IAM User
        Guide* .

        For information about limits on the number of MFA devices you can create, see `Limitations
        on Entities <https://docs.aws.amazon.com/IAM/latest/UserGuide/LimitationsOnEntities.html>`__
        in the *IAM User Guide* .

        .. warning::

          The seed information contained in the QR code and the Base32 string should be treated like
          any other secret access information. In other words, protect the seed information as you
          would your AWS access keys or your passwords. After you provision your virtual device, you
          should ensure that the information is destroyed following secure procedures.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/CreateVirtualMFADevice>`_

        **Request Syntax**
        ::

          virtual_mfa_device = iam.create_virtual_mfa_device(
              Path='string',
              VirtualMFADeviceName='string'
          )
        :type Path: string
        :param Path:

          The path for the virtual MFA device. For more information about paths, see `IAM
          Identifiers <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__
          in the *IAM User Guide* .

          This parameter is optional. If it is not included, it defaults to a slash (/).

          This parameter allows (through its `regex pattern <http://wikipedia.org/wiki/regex>`__ ) a
          string of characters consisting of either a forward slash (/) by itself or a string that
          must begin and end with forward slashes. In addition, it can contain any ASCII character
          from the ! (\\u0021) through the DEL character (\\u007F), including most punctuation
          characters, digits, and upper and lowercased letters.

        :type VirtualMFADeviceName: string
        :param VirtualMFADeviceName: **[REQUIRED]**

          The name of the virtual MFA device. Use with path to uniquely identify a virtual MFA
          device.

          This parameter allows (through its `regex pattern <http://wikipedia.org/wiki/regex>`__ ) a
          string of characters consisting of upper and lowercase alphanumeric characters with no
          spaces. You can also include any of the following characters: _+=,.@-

        :rtype: :py:class:`iam.VirtualMfaDevice`
        :returns: VirtualMfaDevice resource
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        Returns a list of all the available sub-resources for this
        Resource.

        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """


class AccessKey(Boto3ServiceResource):
    access_key_id: str
    status: str
    create_date: datetime
    user_name: str
    id: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def activate(self, *args: Any, **kwargs: Any) -> None:
        """
        Changes the status of the specified access key from Active to Inactive, or vice versa. This
        operation can be used to disable a user's key as part of a key rotation workflow.

        If the ``UserName`` is not specified, the user name is determined implicitly based on the
        AWS access key ID used to sign the request. This operation works for access keys under the
        AWS account. Consequently, you can use this operation to manage AWS account root user
        credentials even if the AWS account has no associated users.

        For information about rotating keys, see `Managing Keys and Certificates
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/ManagingCredentials.html>`__ in the *IAM
        User Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/UpdateAccessKey>`_

        **Request Syntax**
        ::

          response = access_key.activate()

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def deactivate(self, *args: Any, **kwargs: Any) -> None:
        """
        Changes the status of the specified access key from Active to Inactive, or vice versa. This
        operation can be used to disable a user's key as part of a key rotation workflow.

        If the ``UserName`` is not specified, the user name is determined implicitly based on the
        AWS access key ID used to sign the request. This operation works for access keys under the
        AWS account. Consequently, you can use this operation to manage AWS account root user
        credentials even if the AWS account has no associated users.

        For information about rotating keys, see `Managing Keys and Certificates
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/ManagingCredentials.html>`__ in the *IAM
        User Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/UpdateAccessKey>`_

        **Request Syntax**
        ::

          response = access_key.deactivate()

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, *args: Any, **kwargs: Any) -> None:
        """
        Deletes the access key pair associated with the specified IAM user.

        If you do not specify a user name, IAM determines the user name implicitly based on the AWS
        access key ID signing the request. This operation works for access keys under the AWS
        account. Consequently, you can use this operation to manage AWS account root user
        credentials even if the AWS account has no associated users.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/DeleteAccessKey>`_

        **Request Syntax**
        ::

          response = access_key.delete()

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        Returns a list of all the available sub-resources for this
        Resource.

        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """


class AccessKeyPair(Boto3ServiceResource):
    access_key_id: str
    status: str
    secret_access_key: str
    create_date: datetime
    user_name: str
    id: str
    secret: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def activate(self, *args: Any, **kwargs: Any) -> None:
        """
        Changes the status of the specified access key from Active to Inactive, or vice versa. This
        operation can be used to disable a user's key as part of a key rotation workflow.

        If the ``UserName`` is not specified, the user name is determined implicitly based on the
        AWS access key ID used to sign the request. This operation works for access keys under the
        AWS account. Consequently, you can use this operation to manage AWS account root user
        credentials even if the AWS account has no associated users.

        For information about rotating keys, see `Managing Keys and Certificates
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/ManagingCredentials.html>`__ in the *IAM
        User Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/UpdateAccessKey>`_

        **Request Syntax**
        ::

          response = access_key_pair.activate()

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def deactivate(self, *args: Any, **kwargs: Any) -> None:
        """
        Changes the status of the specified access key from Active to Inactive, or vice versa. This
        operation can be used to disable a user's key as part of a key rotation workflow.

        If the ``UserName`` is not specified, the user name is determined implicitly based on the
        AWS access key ID used to sign the request. This operation works for access keys under the
        AWS account. Consequently, you can use this operation to manage AWS account root user
        credentials even if the AWS account has no associated users.

        For information about rotating keys, see `Managing Keys and Certificates
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/ManagingCredentials.html>`__ in the *IAM
        User Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/UpdateAccessKey>`_

        **Request Syntax**
        ::

          response = access_key_pair.deactivate()

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, *args: Any, **kwargs: Any) -> None:
        """
        Deletes the access key pair associated with the specified IAM user.

        If you do not specify a user name, IAM determines the user name implicitly based on the AWS
        access key ID signing the request. This operation works for access keys under the AWS
        account. Consequently, you can use this operation to manage AWS account root user
        credentials even if the AWS account has no associated users.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/DeleteAccessKey>`_

        **Request Syntax**
        ::

          response = access_key_pair.delete()

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        Returns a list of all the available sub-resources for this
        Resource.

        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """


class AccountPasswordPolicy(Boto3ServiceResource):
    minimum_password_length: int
    require_symbols: bool
    require_numbers: bool
    require_uppercase_characters: bool
    require_lowercase_characters: bool
    allow_users_to_change_password: bool
    expire_passwords: bool
    max_password_age: int
    password_reuse_prevention: int
    hard_expiry: bool

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, *args: Any, **kwargs: Any) -> None:
        """
        Deletes the password policy for the AWS account. There are no parameters.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/DeleteAccountPasswordPolicy>`_

        **Request Syntax**

        ::

          response = account_password_policy.delete()
        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        Returns a list of all the available sub-resources for this
        Resource.

        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self, *args: Any, **kwargs: Any) -> None:
        """
        Calls :py:meth:`IAM.Client.get_account_password_policy` to update the attributes of the
        AccountPasswordPolicy resource. Note that the load and reload methods are the same method
        and can be used interchangeably.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/None>`_

        **Request Syntax**

        ::

          account_password_policy.load()
        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self, *args: Any, **kwargs: Any) -> None:
        """
        Calls :py:meth:`IAM.Client.get_account_password_policy` to update the attributes of the
        AccountPasswordPolicy resource. Note that the load and reload methods are the same method
        and can be used interchangeably.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/None>`_

        **Request Syntax**

        ::

          account_password_policy.load()
        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update(
        self,
        MinimumPasswordLength: int = None,
        RequireSymbols: bool = None,
        RequireNumbers: bool = None,
        RequireUppercaseCharacters: bool = None,
        RequireLowercaseCharacters: bool = None,
        AllowUsersToChangePassword: bool = None,
        MaxPasswordAge: int = None,
        PasswordReusePrevention: int = None,
        HardExpiry: bool = None,
    ) -> None:
        """
        Updates the password policy settings for the AWS account.

        .. note::

          * This operation does not support partial updates. No parameters are required, but if you
          do not specify a parameter, that parameter's value reverts to its default value. See the
          **Request Parameters** section for each parameter's default value. Also note that some
          parameters do not allow the default parameter to be explicitly set. Instead, to invoke the
          default value, do not include that parameter when you invoke the operation.

        For more information about using a password policy, see `Managing an IAM Password Policy
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_ManagingPasswordPolicies.html>`__ in
        the *IAM User Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/UpdateAccountPasswordPolicy>`_

        **Request Syntax**
        ::

          response = account_password_policy.update(
              MinimumPasswordLength=123,
              RequireSymbols=True|False,
              RequireNumbers=True|False,
              RequireUppercaseCharacters=True|False,
              RequireLowercaseCharacters=True|False,
              AllowUsersToChangePassword=True|False,
              MaxPasswordAge=123,
              PasswordReusePrevention=123,
              HardExpiry=True|False
          )
        :type MinimumPasswordLength: integer
        :param MinimumPasswordLength:

          The minimum number of characters allowed in an IAM user password.

          If you do not specify a value for this parameter, then the operation uses the default
          value of ``6`` .

        :type RequireSymbols: boolean
        :param RequireSymbols:

          Specifies whether IAM user passwords must contain at least one of the following
          non-alphanumeric characters:

          ! @ # $ % ^ & * ( ) _ + - = [ ] { } | '

          If you do not specify a value for this parameter, then the operation uses the default
          value of ``false`` . The result is that passwords do not require at least one symbol
          character.

        :type RequireNumbers: boolean
        :param RequireNumbers:

          Specifies whether IAM user passwords must contain at least one numeric character (0 to 9).

          If you do not specify a value for this parameter, then the operation uses the default
          value of ``false`` . The result is that passwords do not require at least one numeric
          character.

        :type RequireUppercaseCharacters: boolean
        :param RequireUppercaseCharacters:

          Specifies whether IAM user passwords must contain at least one uppercase character from
          the ISO basic Latin alphabet (A to Z).

          If you do not specify a value for this parameter, then the operation uses the default
          value of ``false`` . The result is that passwords do not require at least one uppercase
          character.

        :type RequireLowercaseCharacters: boolean
        :param RequireLowercaseCharacters:

          Specifies whether IAM user passwords must contain at least one lowercase character from
          the ISO basic Latin alphabet (a to z).

          If you do not specify a value for this parameter, then the operation uses the default
          value of ``false`` . The result is that passwords do not require at least one lowercase
          character.

        :type AllowUsersToChangePassword: boolean
        :param AllowUsersToChangePassword:

          Allows all IAM users in your account to use the AWS Management Console to change their own
          passwords. For more information, see `Letting IAM Users Change Their Own Passwords
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/HowToPwdIAMUser.html>`__ in the *IAM
          User Guide* .

          If you do not specify a value for this parameter, then the operation uses the default
          value of ``false`` . The result is that IAM users in the account do not automatically have
          permissions to change their own password.

        :type MaxPasswordAge: integer
        :param MaxPasswordAge:

          The number of days that an IAM user password is valid.

          If you do not specify a value for this parameter, then the operation uses the default
          value of ``0`` . The result is that IAM user passwords never expire.

        :type PasswordReusePrevention: integer
        :param PasswordReusePrevention:

          Specifies the number of previous passwords that IAM users are prevented from reusing.

          If you do not specify a value for this parameter, then the operation uses the default
          value of ``0`` . The result is that IAM users are not prevented from reusing previous
          passwords.

        :type HardExpiry: boolean
        :param HardExpiry:

          Prevents IAM users from setting a new password after their password has expired. The IAM
          user cannot be accessed until an administrator resets the password.

          If you do not specify a value for this parameter, then the operation uses the default
          value of ``false`` . The result is that IAM users can change their passwords after they
          expire and continue to sign in as the user.

        :returns: None
        """


class AccountSummary(Boto3ServiceResource):
    summary_map: Dict[str, Any]

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        Returns a list of all the available sub-resources for this
        Resource.

        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self, *args: Any, **kwargs: Any) -> None:
        """
        Calls :py:meth:`IAM.Client.get_account_summary` to update the attributes of the
        AccountSummary resource. Note that the load and reload methods are the same method and can
        be used interchangeably.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/None>`_

        **Request Syntax**

        ::

          account_summary.load()
        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self, *args: Any, **kwargs: Any) -> None:
        """
        Calls :py:meth:`IAM.Client.get_account_summary` to update the attributes of the
        AccountSummary resource. Note that the load and reload methods are the same method and can
        be used interchangeably.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/None>`_

        **Request Syntax**

        ::

          account_summary.load()
        :returns: None
        """


class AssumeRolePolicy(Boto3ServiceResource):
    role_name: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        Returns a list of all the available sub-resources for this
        Resource.

        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update(self, PolicyDocument: str) -> None:
        """
        Updates the policy that grants an IAM entity permission to assume a role. This is typically
        referred to as the "role trust policy". For more information about roles, go to `Using Roles
        to Delegate Permissions and Federate Identities
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/roles-toplevel.html>`__ .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/UpdateAssumeRolePolicy>`_

        **Request Syntax**
        ::

          response = assume_role_policy.update(
              PolicyDocument='string'
          )
        :type PolicyDocument: string
        :param PolicyDocument: **[REQUIRED]**

          The policy that grants an entity permission to assume the role.

          You must provide policies in JSON format in IAM. However, for AWS CloudFormation templates
          formatted in YAML, you can provide the policy in JSON or YAML format. AWS CloudFormation
          always converts a YAML policy to JSON format before submitting it to IAM.

          The `regex pattern <http://wikipedia.org/wiki/regex>`__ used to validate this parameter is
          a string of characters consisting of the following:

          * Any printable ASCII character ranging from the space character (\\u0020) through the end
          of the ASCII character range

          * The printable characters in the Basic Latin and Latin-1 Supplement character set
          (through \\u00FF)

          * The special characters tab (\\u0009), line feed (\\u000A), and carriage return (\\u000D)

        :returns: None
        """


class CurrentUser(Boto3ServiceResource):
    path: str
    user_name: str
    user_id: str
    arn: str
    create_date: datetime
    password_last_used: datetime
    permissions_boundary: Dict[str, Any]
    tags: List[Any]
    access_keys: service_resource_scope.CurrentUserAccessKeysCollection
    mfa_devices: service_resource_scope.CurrentUserMfaDevicesCollection
    signing_certificates: service_resource_scope.CurrentUserSigningCertificatesCollection

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        Returns a list of all the available sub-resources for this
        Resource.

        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self, *args: Any, **kwargs: Any) -> None:
        """
        Calls :py:meth:`IAM.Client.get_user` to update the attributes of the CurrentUser resource.
        Note that the load and reload methods are the same method and can be used interchangeably.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/None>`_

        **Request Syntax**

        ::

          current_user.load()
        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self, *args: Any, **kwargs: Any) -> None:
        """
        Calls :py:meth:`IAM.Client.get_user` to update the attributes of the CurrentUser resource.
        Note that the load and reload methods are the same method and can be used interchangeably.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/None>`_

        **Request Syntax**

        ::

          current_user.load()
        :returns: None
        """


class Group(Boto3ServiceResource):
    path: str
    group_name: str
    group_id: str
    arn: str
    create_date: datetime
    name: str
    attached_policies: service_resource_scope.GroupAttachedPoliciesCollection
    policies: service_resource_scope.GroupPoliciesCollection
    users: service_resource_scope.GroupUsersCollection

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def add_user(self, UserName: str) -> None:
        """
        Adds the specified user to the specified group.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/AddUserToGroup>`_

        **Request Syntax**
        ::

          response = group.add_user(
              UserName='string'
          )
        :type UserName: string
        :param UserName: **[REQUIRED]**

          The name of the user to add.

          This parameter allows (through its `regex pattern <http://wikipedia.org/wiki/regex>`__ ) a
          string of characters consisting of upper and lowercase alphanumeric characters with no
          spaces. You can also include any of the following characters: _+=,.@-

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def attach_policy(self, PolicyArn: str) -> None:
        """
        Attaches the specified managed policy to the specified IAM group.

        You use this API to attach a managed policy to a group. To embed an inline policy in a
        group, use  PutGroupPolicy .

        For more information about policies, see `Managed Policies and Inline Policies
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in the
        *IAM User Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/AttachGroupPolicy>`_

        **Request Syntax**
        ::

          response = group.attach_policy(
              PolicyArn='string'
          )
        :type PolicyArn: string
        :param PolicyArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the IAM policy you want to attach.

          For more information about ARNs, see `Amazon Resource Names (ARNs) and AWS Service
          Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__
          in the *AWS General Reference* .

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create(self, Path: str = None) -> List[service_resource_scope.Group]:
        """
        Creates a new group.

        For information about the number of groups you can create, see `Limitations on IAM Entities
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/LimitationsOnEntities.html>`__ in the *IAM
        User Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/CreateGroup>`_

        **Request Syntax**
        ::

          group = group.create(
              Path='string',

          )
        :type Path: string
        :param Path:

          The path to the group. For more information about paths, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .

          This parameter is optional. If it is not included, it defaults to a slash (/).

          This parameter allows (through its `regex pattern <http://wikipedia.org/wiki/regex>`__ ) a
          string of characters consisting of either a forward slash (/) by itself or a string that
          must begin and end with forward slashes. In addition, it can contain any ASCII character
          from the ! (\\u0021) through the DEL character (\\u007F), including most punctuation
          characters, digits, and upper and lowercased letters.

        :rtype: :py:class:`iam.Group`
        :returns: Group resource
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_policy(
        self, PolicyName: str, PolicyDocument: str
    ) -> service_resource_scope.GroupPolicy:
        """
        Adds or updates an inline policy document that is embedded in the specified IAM group.

        A user can also have managed policies attached to it. To attach a managed policy to a group,
        use  AttachGroupPolicy . To create a new managed policy, use  CreatePolicy . For information
        about policies, see `Managed Policies and Inline Policies
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in the
        *IAM User Guide* .

        For information about limits on the number of inline policies that you can embed in a group,
        see `Limitations on IAM Entities
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/LimitationsOnEntities.html>`__ in the *IAM
        User Guide* .

        .. note::

          Because policy documents can be large, you should use POST rather than GET when calling
          ``PutGroupPolicy`` . For general information about using the Query API with IAM, go to
          `Making Query Requests
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/IAM_UsingQueryAPI.html>`__ in the *IAM
          User Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/PutGroupPolicy>`_

        **Request Syntax**
        ::

          group_policy = group.create_policy(
              PolicyName='string',
              PolicyDocument='string'
          )
        :type PolicyName: string
        :param PolicyName: **[REQUIRED]**

          The name of the policy document.

          This parameter allows (through its `regex pattern <http://wikipedia.org/wiki/regex>`__ ) a
          string of characters consisting of upper and lowercase alphanumeric characters with no
          spaces. You can also include any of the following characters: _+=,.@-

        :type PolicyDocument: string
        :param PolicyDocument: **[REQUIRED]**

          The policy document.

          You must provide policies in JSON format in IAM. However, for AWS CloudFormation templates
          formatted in YAML, you can provide the policy in JSON or YAML format. AWS CloudFormation
          always converts a YAML policy to JSON format before submitting it to IAM.

          The `regex pattern <http://wikipedia.org/wiki/regex>`__ used to validate this parameter is
          a string of characters consisting of the following:

          * Any printable ASCII character ranging from the space character (\\u0020) through the end
          of the ASCII character range

          * The printable characters in the Basic Latin and Latin-1 Supplement character set
          (through \\u00FF)

          * The special characters tab (\\u0009), line feed (\\u000A), and carriage return (\\u000D)

        :rtype: :py:class:`iam.GroupPolicy`
        :returns: GroupPolicy resource
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, *args: Any, **kwargs: Any) -> None:
        """
        Deletes the specified IAM group. The group must not contain any users or have any attached
        policies.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/DeleteGroup>`_

        **Request Syntax**
        ::

          response = group.delete()

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def detach_policy(self, PolicyArn: str) -> None:
        """
        Removes the specified managed policy from the specified IAM group.

        A group can also have inline policies embedded with it. To delete an inline policy, use the
        DeleteGroupPolicy API. For information about policies, see `Managed Policies and Inline
        Policies
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in the
        *IAM User Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/DetachGroupPolicy>`_

        **Request Syntax**
        ::

          response = group.detach_policy(
              PolicyArn='string'
          )
        :type PolicyArn: string
        :param PolicyArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the IAM policy you want to detach.

          For more information about ARNs, see `Amazon Resource Names (ARNs) and AWS Service
          Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__
          in the *AWS General Reference* .

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        Returns a list of all the available sub-resources for this
        Resource.

        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self, *args: Any, **kwargs: Any) -> None:
        """
        Calls :py:meth:`IAM.Client.get_group` to update the attributes of the Group resource. Note
        that the load and reload methods are the same method and can be used interchangeably.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/None>`_

        **Request Syntax**

        ::

          group.load()
        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self, *args: Any, **kwargs: Any) -> None:
        """
        Calls :py:meth:`IAM.Client.get_group` to update the attributes of the Group resource. Note
        that the load and reload methods are the same method and can be used interchangeably.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/None>`_

        **Request Syntax**

        ::

          group.load()
        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def remove_user(self, UserName: str) -> None:
        """
        Removes the specified user from the specified group.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/RemoveUserFromGroup>`_

        **Request Syntax**
        ::

          response = group.remove_user(
              UserName='string'
          )
        :type UserName: string
        :param UserName: **[REQUIRED]**

          The name of the user to remove.

          This parameter allows (through its `regex pattern <http://wikipedia.org/wiki/regex>`__ ) a
          string of characters consisting of upper and lowercase alphanumeric characters with no
          spaces. You can also include any of the following characters: _+=,.@-

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update(
        self, NewPath: str = None, NewGroupName: str = None
    ) -> List[service_resource_scope.Group]:
        """
        Updates the name and/or the path of the specified IAM group.

        .. warning::

          You should understand the implications of changing a group's path or name. For more
          information, see `Renaming Users and Groups
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_WorkingWithGroupsAndUsers.html>`__
          in the *IAM User Guide* .

        .. note::

          The person making the request (the principal), must have permission to change the role
          group with the old name and the new name. For example, to change the group named
          ``Managers`` to ``MGRs`` , the principal must have a policy that allows them to update
          both groups. If the principal has permission to update the ``Managers`` group, but not the
          ``MGRs`` group, then the update fails. For more information about permissions, see `Access
          Management <https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html>`__ .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/UpdateGroup>`_

        **Request Syntax**
        ::

          group = group.update(
              NewPath='string',
              NewGroupName='string'
          )
        :type NewPath: string
        :param NewPath:

          New path for the IAM group. Only include this if changing the group's path.

          This parameter allows (through its `regex pattern <http://wikipedia.org/wiki/regex>`__ ) a
          string of characters consisting of either a forward slash (/) by itself or a string that
          must begin and end with forward slashes. In addition, it can contain any ASCII character
          from the ! (\\u0021) through the DEL character (\\u007F), including most punctuation
          characters, digits, and upper and lowercased letters.

        :type NewGroupName: string
        :param NewGroupName:

          New name for the IAM group. Only include this if changing the group's name.

          IAM user, group, role, and policy names must be unique within the account. Names are not
          distinguished by case. For example, you cannot create resources named both "MyResource"
          and "myresource".

        :rtype: :py:class:`iam.Group`
        :returns: Group resource
        """


class GroupPolicy(Boto3ServiceResource):
    policy_name: str
    policy_document: str
    group_name: str
    name: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, *args: Any, **kwargs: Any) -> None:
        """
        Deletes the specified inline policy that is embedded in the specified IAM group.

        A group can also have managed policies attached to it. To detach a managed policy from a
        group, use  DetachGroupPolicy . For more information about policies, refer to `Managed
        Policies and Inline Policies
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in the
        *IAM User Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/DeleteGroupPolicy>`_

        **Request Syntax**
        ::

          response = group_policy.delete()

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        Returns a list of all the available sub-resources for this
        Resource.

        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self, *args: Any, **kwargs: Any) -> None:
        """
        Calls :py:meth:`IAM.Client.get_group_policy` to update the attributes of the GroupPolicy
        resource. Note that the load and reload methods are the same method and can be used
        interchangeably.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/None>`_

        **Request Syntax**

        ::

          group_policy.load()
        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put(self, PolicyDocument: str) -> None:
        """
        Adds or updates an inline policy document that is embedded in the specified IAM group.

        A user can also have managed policies attached to it. To attach a managed policy to a group,
        use  AttachGroupPolicy . To create a new managed policy, use  CreatePolicy . For information
        about policies, see `Managed Policies and Inline Policies
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in the
        *IAM User Guide* .

        For information about limits on the number of inline policies that you can embed in a group,
        see `Limitations on IAM Entities
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/LimitationsOnEntities.html>`__ in the *IAM
        User Guide* .

        .. note::

          Because policy documents can be large, you should use POST rather than GET when calling
          ``PutGroupPolicy`` . For general information about using the Query API with IAM, go to
          `Making Query Requests
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/IAM_UsingQueryAPI.html>`__ in the *IAM
          User Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/PutGroupPolicy>`_

        **Request Syntax**
        ::

          response = group_policy.put(
              PolicyDocument='string'
          )
        :type PolicyDocument: string
        :param PolicyDocument: **[REQUIRED]**

          The policy document.

          You must provide policies in JSON format in IAM. However, for AWS CloudFormation templates
          formatted in YAML, you can provide the policy in JSON or YAML format. AWS CloudFormation
          always converts a YAML policy to JSON format before submitting it to IAM.

          The `regex pattern <http://wikipedia.org/wiki/regex>`__ used to validate this parameter is
          a string of characters consisting of the following:

          * Any printable ASCII character ranging from the space character (\\u0020) through the end
          of the ASCII character range

          * The printable characters in the Basic Latin and Latin-1 Supplement character set
          (through \\u00FF)

          * The special characters tab (\\u0009), line feed (\\u000A), and carriage return (\\u000D)

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self, *args: Any, **kwargs: Any) -> None:
        """
        Calls :py:meth:`IAM.Client.get_group_policy` to update the attributes of the GroupPolicy
        resource. Note that the load and reload methods are the same method and can be used
        interchangeably.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/None>`_

        **Request Syntax**

        ::

          group_policy.load()
        :returns: None
        """


class InstanceProfile(Boto3ServiceResource):
    path: str
    instance_profile_name: str
    instance_profile_id: str
    arn: str
    create_date: datetime
    roles_attribute: List[Any]
    name: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def add_role(self, RoleName: str) -> None:
        """
        Adds the specified IAM role to the specified instance profile. An instance profile can
        contain only one role, and this limit cannot be increased. You can remove the existing role
        and then add a different role to an instance profile. You must then wait for the change to
        appear across all of AWS because of `eventual consistency
        <https://en.wikipedia.org/wiki/Eventual_consistency>`__ . To force the change, you must
        `disassociate the instance profile
        <https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisassociateIamInstanceProfile.html>`__
        and then `associate the instance profile
        <https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AssociateIamInstanceProfile.html>`__
        , or you can stop your instance and then restart it.

        .. note::

          The caller of this API must be granted the ``PassRole`` permission on the IAM role by a
          permissions policy.

        For more information about roles, go to `Working with Roles
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/WorkingWithRoles.html>`__ . For more
        information about instance profiles, go to `About Instance Profiles
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/AboutInstanceProfiles.html>`__ .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/AddRoleToInstanceProfile>`_

        **Request Syntax**
        ::

          response = instance_profile.add_role(
              RoleName='string'
          )
        :type RoleName: string
        :param RoleName: **[REQUIRED]**

          The name of the role to add.

          This parameter allows (through its `regex pattern <http://wikipedia.org/wiki/regex>`__ ) a
          string of characters consisting of upper and lowercase alphanumeric characters with no
          spaces. You can also include any of the following characters: _+=,.@-

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, *args: Any, **kwargs: Any) -> None:
        """
        Deletes the specified instance profile. The instance profile must not have an associated
        role.

        .. warning::

          Make sure that you do not have any Amazon EC2 instances running with the instance profile
          you are about to delete. Deleting a role or instance profile that is associated with a
          running instance will break any applications running on the instance.

        For more information about instance profiles, go to `About Instance Profiles
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/AboutInstanceProfiles.html>`__ .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/DeleteInstanceProfile>`_

        **Request Syntax**
        ::

          response = instance_profile.delete()

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        Returns a list of all the available sub-resources for this
        Resource.

        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self, *args: Any, **kwargs: Any) -> None:
        """
        Calls :py:meth:`IAM.Client.get_instance_profile` to update the attributes of the
        InstanceProfile resource. Note that the load and reload methods are the same method and can
        be used interchangeably.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/None>`_

        **Request Syntax**

        ::

          instance_profile.load()
        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self, *args: Any, **kwargs: Any) -> None:
        """
        Calls :py:meth:`IAM.Client.get_instance_profile` to update the attributes of the
        InstanceProfile resource. Note that the load and reload methods are the same method and can
        be used interchangeably.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/None>`_

        **Request Syntax**

        ::

          instance_profile.load()
        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def remove_role(self, RoleName: str) -> None:
        """
        Removes the specified IAM role from the specified EC2 instance profile.

        .. warning::

          Make sure that you do not have any Amazon EC2 instances running with the role you are
          about to remove from the instance profile. Removing a role from an instance profile that
          is associated with a running instance might break any applications running on the
          instance.

        For more information about IAM roles, go to `Working with Roles
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/WorkingWithRoles.html>`__ . For more
        information about instance profiles, go to `About Instance Profiles
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/AboutInstanceProfiles.html>`__ .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/RemoveRoleFromInstanceProfile>`_

        **Request Syntax**
        ::

          response = instance_profile.remove_role(
              RoleName='string'
          )
        :type RoleName: string
        :param RoleName: **[REQUIRED]**

          The name of the role to remove.

          This parameter allows (through its `regex pattern <http://wikipedia.org/wiki/regex>`__ ) a
          string of characters consisting of upper and lowercase alphanumeric characters with no
          spaces. You can also include any of the following characters: _+=,.@-

        :returns: None
        """


class LoginProfile(Boto3ServiceResource):
    create_date: datetime
    password_reset_required: bool
    user_name: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create(
        self, Password: str, PasswordResetRequired: bool = None
    ) -> service_resource_scope.LoginProfile:
        """
        Creates a password for the specified user, giving the user the ability to access AWS
        services through the AWS Management Console. For more information about managing passwords,
        see `Managing Passwords
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_ManagingLogins.html>`__ in the *IAM
        User Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/CreateLoginProfile>`_

        **Request Syntax**
        ::

          login_profile = login_profile.create(
              Password='string',
              PasswordResetRequired=True|False
          )
        :type Password: string
        :param Password: **[REQUIRED]**

          The new password for the user.

          The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this
          parameter is a string of characters. That string can include almost any printable ASCII
          character from the space (\\u0020) through the end of the ASCII character range (\\u00FF).
          You can also include the tab (\\u0009), line feed (\\u000A), and carriage return (\\u000D)
          characters. Any of these characters are valid in a password. However, many tools, such as
          the AWS Management Console, might restrict the ability to type certain characters because
          they have special meaning within that tool.

        :type PasswordResetRequired: boolean
        :param PasswordResetRequired:

          Specifies whether the user is required to set a new password on next sign-in.

        :rtype: :py:class:`iam.LoginProfile`
        :returns: LoginProfile resource
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, *args: Any, **kwargs: Any) -> None:
        """
        Deletes the password for the specified IAM user, which terminates the user's ability to
        access AWS services through the AWS Management Console.

        .. warning::

          Deleting a user's password does not prevent a user from accessing AWS through the command
          line interface or the API. To prevent all user access, you must also either make any
          access keys inactive or delete them. For more information about making keys inactive or
          deleting them, see  UpdateAccessKey and  DeleteAccessKey .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/DeleteLoginProfile>`_

        **Request Syntax**
        ::

          response = login_profile.delete()

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        Returns a list of all the available sub-resources for this
        Resource.

        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self, *args: Any, **kwargs: Any) -> None:
        """
        Calls :py:meth:`IAM.Client.get_login_profile` to update the attributes of the LoginProfile
        resource. Note that the load and reload methods are the same method and can be used
        interchangeably.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/None>`_

        **Request Syntax**

        ::

          login_profile.load()
        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self, *args: Any, **kwargs: Any) -> None:
        """
        Calls :py:meth:`IAM.Client.get_login_profile` to update the attributes of the LoginProfile
        resource. Note that the load and reload methods are the same method and can be used
        interchangeably.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/None>`_

        **Request Syntax**

        ::

          login_profile.load()
        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update(self, Password: str = None, PasswordResetRequired: bool = None) -> None:
        """
        Changes the password for the specified IAM user.

        IAM users can change their own passwords by calling  ChangePassword . For more information
        about modifying passwords, see `Managing Passwords
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_ManagingLogins.html>`__ in the *IAM
        User Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/UpdateLoginProfile>`_

        **Request Syntax**
        ::

          response = login_profile.update(
              Password='string',
              PasswordResetRequired=True|False
          )
        :type Password: string
        :param Password:

          The new password for the specified IAM user.

          The `regex pattern <http://wikipedia.org/wiki/regex>`__ used to validate this parameter is
          a string of characters consisting of the following:

          * Any printable ASCII character ranging from the space character (\\u0020) through the end
          of the ASCII character range

          * The printable characters in the Basic Latin and Latin-1 Supplement character set
          (through \\u00FF)

          * The special characters tab (\\u0009), line feed (\\u000A), and carriage return (\\u000D)

          However, the format can be further restricted by the account administrator by setting a
          password policy on the AWS account. For more information, see  UpdateAccountPasswordPolicy
          .

        :type PasswordResetRequired: boolean
        :param PasswordResetRequired:

          Allows this new password to be used only once by requiring the specified IAM user to set a
          new password on next sign-in.

        :returns: None
        """


class MfaDevice(Boto3ServiceResource):
    enable_date: datetime
    user_name: str
    serial_number: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def associate(self, AuthenticationCode1: str, AuthenticationCode2: str) -> None:
        """
        Enables the specified MFA device and associates it with the specified IAM user. When
        enabled, the MFA device is required for every subsequent login by the IAM user associated
        with the device.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/EnableMFADevice>`_

        **Request Syntax**
        ::

          response = mfa_device.associate(
              AuthenticationCode1='string',
              AuthenticationCode2='string'
          )
        :type AuthenticationCode1: string
        :param AuthenticationCode1: **[REQUIRED]**

          An authentication code emitted by the device.

          The format for this parameter is a string of six digits.

          .. warning::

            Submit your request immediately after generating the authentication codes. If you
            generate the codes and then wait too long to submit the request, the MFA device
            successfully associates with the user but the MFA device becomes out of sync. This
            happens because time-based one-time passwords (TOTP) expire after a short period of
            time. If this happens, you can `resync the device
            <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_sync.html>`__ .

        :type AuthenticationCode2: string
        :param AuthenticationCode2: **[REQUIRED]**

          A subsequent authentication code emitted by the device.

          The format for this parameter is a string of six digits.

          .. warning::

            Submit your request immediately after generating the authentication codes. If you
            generate the codes and then wait too long to submit the request, the MFA device
            successfully associates with the user but the MFA device becomes out of sync. This
            happens because time-based one-time passwords (TOTP) expire after a short period of
            time. If this happens, you can `resync the device
            <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_sync.html>`__ .

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disassociate(self, *args: Any, **kwargs: Any) -> None:
        """
        Deactivates the specified MFA device and removes it from association with the user name for
        which it was originally enabled.

        For more information about creating and working with virtual MFA devices, go to `Enabling a
        Virtual Multi-factor Authentication (MFA) Device
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_VirtualMFA.html>`__ in the *IAM User
        Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/DeactivateMFADevice>`_

        **Request Syntax**
        ::

          response = mfa_device.disassociate()

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        Returns a list of all the available sub-resources for this
        Resource.

        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def resync(self, AuthenticationCode1: str, AuthenticationCode2: str) -> None:
        """
        Synchronizes the specified MFA device with its IAM resource object on the AWS servers.

        For more information about creating and working with virtual MFA devices, go to `Using a
        Virtual MFA Device
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_VirtualMFA.html>`__ in the *IAM User
        Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ResyncMFADevice>`_

        **Request Syntax**
        ::

          response = mfa_device.resync(
              AuthenticationCode1='string',
              AuthenticationCode2='string'
          )
        :type AuthenticationCode1: string
        :param AuthenticationCode1: **[REQUIRED]**

          An authentication code emitted by the device.

          The format for this parameter is a sequence of six digits.

        :type AuthenticationCode2: string
        :param AuthenticationCode2: **[REQUIRED]**

          A subsequent authentication code emitted by the device.

          The format for this parameter is a sequence of six digits.

        :returns: None
        """


class Policy(Boto3ServiceResource):
    policy_name: str
    policy_id: str
    path: str
    default_version_id: str
    attachment_count: int
    permissions_boundary_usage_count: int
    is_attachable: bool
    description: str
    create_date: datetime
    update_date: datetime
    arn: str
    attached_groups: service_resource_scope.PolicyAttachedGroupsCollection
    attached_roles: service_resource_scope.PolicyAttachedRolesCollection
    attached_users: service_resource_scope.PolicyAttachedUsersCollection
    versions: service_resource_scope.PolicyVersionsCollection

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def attach_group(self, GroupName: str) -> None:
        """
        Attaches the specified managed policy to the specified IAM group.

        You use this API to attach a managed policy to a group. To embed an inline policy in a
        group, use  PutGroupPolicy .

        For more information about policies, see `Managed Policies and Inline Policies
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in the
        *IAM User Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/AttachGroupPolicy>`_

        **Request Syntax**
        ::

          response = policy.attach_group(
              GroupName='string',

          )
        :type GroupName: string
        :param GroupName: **[REQUIRED]**

          The name (friendly name, not ARN) of the group to attach the policy to.

          This parameter allows (through its `regex pattern <http://wikipedia.org/wiki/regex>`__ ) a
          string of characters consisting of upper and lowercase alphanumeric characters with no
          spaces. You can also include any of the following characters: _+=,.@-

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def attach_role(self, RoleName: str) -> None:
        """
        Attaches the specified managed policy to the specified IAM role. When you attach a managed
        policy to a role, the managed policy becomes part of the role's permission (access) policy.

        .. note::

          You cannot use a managed policy as the role's trust policy. The role's trust policy is
          created at the same time as the role, using  CreateRole . You can update a role's trust
          policy using  UpdateAssumeRolePolicy .

        Use this API to attach a *managed* policy to a role. To embed an inline policy in a role,
        use  PutRolePolicy . For more information about policies, see `Managed Policies and Inline
        Policies
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in the
        *IAM User Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/AttachRolePolicy>`_

        **Request Syntax**
        ::

          response = policy.attach_role(
              RoleName='string',

          )
        :type RoleName: string
        :param RoleName: **[REQUIRED]**

          The name (friendly name, not ARN) of the role to attach the policy to.

          This parameter allows (through its `regex pattern <http://wikipedia.org/wiki/regex>`__ ) a
          string of characters consisting of upper and lowercase alphanumeric characters with no
          spaces. You can also include any of the following characters: _+=,.@-

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def attach_user(self, UserName: str) -> None:
        """
        Attaches the specified managed policy to the specified user.

        You use this API to attach a *managed* policy to a user. To embed an inline policy in a
        user, use  PutUserPolicy .

        For more information about policies, see `Managed Policies and Inline Policies
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in the
        *IAM User Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/AttachUserPolicy>`_

        **Request Syntax**
        ::

          response = policy.attach_user(
              UserName='string',

          )
        :type UserName: string
        :param UserName: **[REQUIRED]**

          The name (friendly name, not ARN) of the IAM user to attach the policy to.

          This parameter allows (through its `regex pattern <http://wikipedia.org/wiki/regex>`__ ) a
          string of characters consisting of upper and lowercase alphanumeric characters with no
          spaces. You can also include any of the following characters: _+=,.@-

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_version(
        self, PolicyDocument: str, SetAsDefault: bool = None
    ) -> service_resource_scope.PolicyVersion:
        """
        Creates a new version of the specified managed policy. To update a managed policy, you
        create a new policy version. A managed policy can have up to five versions. If the policy
        has five versions, you must delete an existing version using  DeletePolicyVersion before you
        create a new version.

        Optionally, you can set the new version as the policy's default version. The default version
        is the version that is in effect for the IAM users, groups, and roles to which the policy is
        attached.

        For more information about managed policy versions, see `Versioning for Managed Policies
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-versions.html>`__ in the
        *IAM User Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/CreatePolicyVersion>`_

        **Request Syntax**
        ::

          policy_version = policy.create_version(
              PolicyDocument='string',
              SetAsDefault=True|False
          )
        :type PolicyDocument: string
        :param PolicyDocument: **[REQUIRED]**

          The JSON policy document that you want to use as the content for this new version of the
          policy.

          You must provide policies in JSON format in IAM. However, for AWS CloudFormation templates
          formatted in YAML, you can provide the policy in JSON or YAML format. AWS CloudFormation
          always converts a YAML policy to JSON format before submitting it to IAM.

          The `regex pattern <http://wikipedia.org/wiki/regex>`__ used to validate this parameter is
          a string of characters consisting of the following:

          * Any printable ASCII character ranging from the space character (\\u0020) through the end
          of the ASCII character range

          * The printable characters in the Basic Latin and Latin-1 Supplement character set
          (through \\u00FF)

          * The special characters tab (\\u0009), line feed (\\u000A), and carriage return (\\u000D)

        :type SetAsDefault: boolean
        :param SetAsDefault:

          Specifies whether to set this version as the policy's default version.

          When this parameter is ``true`` , the new policy version becomes the operative version.
          That is, it becomes the version that is in effect for the IAM users, groups, and roles
          that the policy is attached to.

          For more information about managed policy versions, see `Versioning for Managed Policies
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-versions.html>`__ in
          the *IAM User Guide* .

        :rtype: :py:class:`iam.PolicyVersion`
        :returns: PolicyVersion resource
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, *args: Any, **kwargs: Any) -> None:
        """
        Deletes the specified managed policy.

        Before you can delete a managed policy, you must first detach the policy from all users,
        groups, and roles that it is attached to. In addition, you must delete all the policy's
        versions. The following steps describe the process for deleting a managed policy:

        * Detach the policy from all users, groups, and roles that the policy is attached to, using
        the  DetachUserPolicy ,  DetachGroupPolicy , or  DetachRolePolicy API operations. To list
        all the users, groups, and roles that a policy is attached to, use  ListEntitiesForPolicy .

        * Delete all versions of the policy using  DeletePolicyVersion . To list the policy's
        versions, use  ListPolicyVersions . You cannot use  DeletePolicyVersion to delete the
        version that is marked as the default version. You delete the policy's default version in
        the next step of the process.

        * Delete the policy (this automatically deletes the policy's default version) using this
        API.

        For information about managed policies, see `Managed Policies and Inline Policies
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in the
        *IAM User Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/DeletePolicy>`_

        **Request Syntax**
        ::

          response = policy.delete()

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def detach_group(self, GroupName: str) -> None:
        """
        Removes the specified managed policy from the specified IAM group.

        A group can also have inline policies embedded with it. To delete an inline policy, use the
        DeleteGroupPolicy API. For information about policies, see `Managed Policies and Inline
        Policies
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in the
        *IAM User Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/DetachGroupPolicy>`_

        **Request Syntax**
        ::

          response = policy.detach_group(
              GroupName='string',

          )
        :type GroupName: string
        :param GroupName: **[REQUIRED]**

          The name (friendly name, not ARN) of the IAM group to detach the policy from.

          This parameter allows (through its `regex pattern <http://wikipedia.org/wiki/regex>`__ ) a
          string of characters consisting of upper and lowercase alphanumeric characters with no
          spaces. You can also include any of the following characters: _+=,.@-

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def detach_role(self, RoleName: str) -> None:
        """
        Removes the specified managed policy from the specified role.

        A role can also have inline policies embedded with it. To delete an inline policy, use the
        DeleteRolePolicy API. For information about policies, see `Managed Policies and Inline
        Policies
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in the
        *IAM User Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/DetachRolePolicy>`_

        **Request Syntax**
        ::

          response = policy.detach_role(
              RoleName='string',

          )
        :type RoleName: string
        :param RoleName: **[REQUIRED]**

          The name (friendly name, not ARN) of the IAM role to detach the policy from.

          This parameter allows (through its `regex pattern <http://wikipedia.org/wiki/regex>`__ ) a
          string of characters consisting of upper and lowercase alphanumeric characters with no
          spaces. You can also include any of the following characters: _+=,.@-

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def detach_user(self, UserName: str) -> None:
        """
        Removes the specified managed policy from the specified user.

        A user can also have inline policies embedded with it. To delete an inline policy, use the
        DeleteUserPolicy API. For information about policies, see `Managed Policies and Inline
        Policies
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in the
        *IAM User Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/DetachUserPolicy>`_

        **Request Syntax**
        ::

          response = policy.detach_user(
              UserName='string',

          )
        :type UserName: string
        :param UserName: **[REQUIRED]**

          The name (friendly name, not ARN) of the IAM user to detach the policy from.

          This parameter allows (through its `regex pattern <http://wikipedia.org/wiki/regex>`__ ) a
          string of characters consisting of upper and lowercase alphanumeric characters with no
          spaces. You can also include any of the following characters: _+=,.@-

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        Returns a list of all the available sub-resources for this
        Resource.

        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self, *args: Any, **kwargs: Any) -> None:
        """
        Calls :py:meth:`IAM.Client.get_policy` to update the attributes of the Policy resource. Note
        that the load and reload methods are the same method and can be used interchangeably.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/None>`_

        **Request Syntax**

        ::

          policy.load()
        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self, *args: Any, **kwargs: Any) -> None:
        """
        Calls :py:meth:`IAM.Client.get_policy` to update the attributes of the Policy resource. Note
        that the load and reload methods are the same method and can be used interchangeably.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/None>`_

        **Request Syntax**

        ::

          policy.load()
        :returns: None
        """


class PolicyVersion(Boto3ServiceResource):
    document: str
    is_default_version: bool
    create_date: datetime
    arn: str
    version_id: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, *args: Any, **kwargs: Any) -> None:
        """
        Deletes the specified version from the specified managed policy.

        You cannot delete the default version from a policy using this API. To delete the default
        version from a policy, use  DeletePolicy . To find out which version of a policy is marked
        as the default version, use  ListPolicyVersions .

        For information about versions for managed policies, see `Versioning for Managed Policies
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-versions.html>`__ in the
        *IAM User Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/DeletePolicyVersion>`_

        **Request Syntax**
        ::

          response = policy_version.delete()

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        Returns a list of all the available sub-resources for this
        Resource.

        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self, *args: Any, **kwargs: Any) -> None:
        """
        Calls :py:meth:`IAM.Client.get_policy_version` to update the attributes of the PolicyVersion
        resource. Note that the load and reload methods are the same method and can be used
        interchangeably.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/None>`_

        **Request Syntax**

        ::

          policy_version.load()
        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self, *args: Any, **kwargs: Any) -> None:
        """
        Calls :py:meth:`IAM.Client.get_policy_version` to update the attributes of the PolicyVersion
        resource. Note that the load and reload methods are the same method and can be used
        interchangeably.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/None>`_

        **Request Syntax**

        ::

          policy_version.load()
        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def set_as_default(self, *args: Any, **kwargs: Any) -> None:
        """
        Sets the specified version of the specified policy as the policy's default (operative)
        version.

        This operation affects all users, groups, and roles that the policy is attached to. To list
        the users, groups, and roles that the policy is attached to, use the  ListEntitiesForPolicy
        API.

        For information about managed policies, see `Managed Policies and Inline Policies
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in the
        *IAM User Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/SetDefaultPolicyVersion>`_

        **Request Syntax**
        ::

          response = policy_version.set_as_default()

        :returns: None
        """


class Role(Boto3ServiceResource):
    path: str
    role_name: str
    role_id: str
    arn: str
    create_date: datetime
    assume_role_policy_document: str
    description: str
    max_session_duration: int
    permissions_boundary: Dict[str, Any]
    tags: List[Any]
    role_last_used: Dict[str, Any]
    name: str
    attached_policies: service_resource_scope.RoleAttachedPoliciesCollection
    instance_profiles: service_resource_scope.RoleInstanceProfilesCollection
    policies: service_resource_scope.RolePoliciesCollection

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def attach_policy(self, PolicyArn: str) -> None:
        """
        Attaches the specified managed policy to the specified IAM role. When you attach a managed
        policy to a role, the managed policy becomes part of the role's permission (access) policy.

        .. note::

          You cannot use a managed policy as the role's trust policy. The role's trust policy is
          created at the same time as the role, using  CreateRole . You can update a role's trust
          policy using  UpdateAssumeRolePolicy .

        Use this API to attach a *managed* policy to a role. To embed an inline policy in a role,
        use  PutRolePolicy . For more information about policies, see `Managed Policies and Inline
        Policies
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in the
        *IAM User Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/AttachRolePolicy>`_

        **Request Syntax**
        ::

          response = role.attach_policy(
              PolicyArn='string'
          )
        :type PolicyArn: string
        :param PolicyArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the IAM policy you want to attach.

          For more information about ARNs, see `Amazon Resource Names (ARNs) and AWS Service
          Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__
          in the *AWS General Reference* .

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, *args: Any, **kwargs: Any) -> None:
        """
        Deletes the specified role. The role must not have any policies attached. For more
        information about roles, go to `Working with Roles
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/WorkingWithRoles.html>`__ .

        .. warning::

          Make sure that you do not have any Amazon EC2 instances running with the role you are
          about to delete. Deleting a role or instance profile that is associated with a running
          instance will break any applications running on the instance.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/DeleteRole>`_

        **Request Syntax**
        ::

          response = role.delete()

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def detach_policy(self, PolicyArn: str) -> None:
        """
        Removes the specified managed policy from the specified role.

        A role can also have inline policies embedded with it. To delete an inline policy, use the
        DeleteRolePolicy API. For information about policies, see `Managed Policies and Inline
        Policies
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in the
        *IAM User Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/DetachRolePolicy>`_

        **Request Syntax**
        ::

          response = role.detach_policy(
              PolicyArn='string'
          )
        :type PolicyArn: string
        :param PolicyArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the IAM policy you want to detach.

          For more information about ARNs, see `Amazon Resource Names (ARNs) and AWS Service
          Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__
          in the *AWS General Reference* .

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        Returns a list of all the available sub-resources for this
        Resource.

        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self, *args: Any, **kwargs: Any) -> None:
        """
        Calls :py:meth:`IAM.Client.get_role` to update the attributes of the Role resource. Note
        that the load and reload methods are the same method and can be used interchangeably.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/None>`_

        **Request Syntax**

        ::

          role.load()
        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self, *args: Any, **kwargs: Any) -> None:
        """
        Calls :py:meth:`IAM.Client.get_role` to update the attributes of the Role resource. Note
        that the load and reload methods are the same method and can be used interchangeably.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/None>`_

        **Request Syntax**

        ::

          role.load()
        :returns: None
        """


class RolePolicy(Boto3ServiceResource):
    policy_name: str
    policy_document: str
    role_name: str
    name: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, *args: Any, **kwargs: Any) -> None:
        """
        Deletes the specified inline policy that is embedded in the specified IAM role.

        A role can also have managed policies attached to it. To detach a managed policy from a
        role, use  DetachRolePolicy . For more information about policies, refer to `Managed
        Policies and Inline Policies
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in the
        *IAM User Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/DeleteRolePolicy>`_

        **Request Syntax**
        ::

          response = role_policy.delete()

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        Returns a list of all the available sub-resources for this
        Resource.

        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self, *args: Any, **kwargs: Any) -> None:
        """
        Calls :py:meth:`IAM.Client.get_role_policy` to update the attributes of the RolePolicy
        resource. Note that the load and reload methods are the same method and can be used
        interchangeably.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/None>`_

        **Request Syntax**

        ::

          role_policy.load()
        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put(self, PolicyDocument: str) -> None:
        """
        Adds or updates an inline policy document that is embedded in the specified IAM role.

        When you embed an inline policy in a role, the inline policy is used as part of the role's
        access (permissions) policy. The role's trust policy is created at the same time as the
        role, using  CreateRole . You can update a role's trust policy using  UpdateAssumeRolePolicy
        . For more information about IAM roles, go to `Using Roles to Delegate Permissions and
        Federate Identities
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/roles-toplevel.html>`__ .

        A role can also have a managed policy attached to it. To attach a managed policy to a role,
        use  AttachRolePolicy . To create a new managed policy, use  CreatePolicy . For information
        about policies, see `Managed Policies and Inline Policies
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in the
        *IAM User Guide* .

        For information about limits on the number of inline policies that you can embed with a
        role, see `Limitations on IAM Entities
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/LimitationsOnEntities.html>`__ in the *IAM
        User Guide* .

        .. note::

          Because policy documents can be large, you should use POST rather than GET when calling
          ``PutRolePolicy`` . For general information about using the Query API with IAM, go to
          `Making Query Requests
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/IAM_UsingQueryAPI.html>`__ in the *IAM
          User Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/PutRolePolicy>`_

        **Request Syntax**
        ::

          response = role_policy.put(
              PolicyDocument='string'
          )
        :type PolicyDocument: string
        :param PolicyDocument: **[REQUIRED]**

          The policy document.

          You must provide policies in JSON format in IAM. However, for AWS CloudFormation templates
          formatted in YAML, you can provide the policy in JSON or YAML format. AWS CloudFormation
          always converts a YAML policy to JSON format before submitting it to IAM.

          The `regex pattern <http://wikipedia.org/wiki/regex>`__ used to validate this parameter is
          a string of characters consisting of the following:

          * Any printable ASCII character ranging from the space character (\\u0020) through the end
          of the ASCII character range

          * The printable characters in the Basic Latin and Latin-1 Supplement character set
          (through \\u00FF)

          * The special characters tab (\\u0009), line feed (\\u000A), and carriage return (\\u000D)

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self, *args: Any, **kwargs: Any) -> None:
        """
        Calls :py:meth:`IAM.Client.get_role_policy` to update the attributes of the RolePolicy
        resource. Note that the load and reload methods are the same method and can be used
        interchangeably.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/None>`_

        **Request Syntax**

        ::

          role_policy.load()
        :returns: None
        """


class SamlProvider(Boto3ServiceResource):
    saml_metadata_document: str
    create_date: datetime
    valid_until: datetime
    arn: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, *args: Any, **kwargs: Any) -> None:
        """
        Deletes a SAML provider resource in IAM.

        Deleting the provider resource from IAM does not update any roles that reference the SAML
        provider resource's ARN as a principal in their trust policies. Any attempt to assume a role
        that references a non-existent provider resource ARN fails.

        .. note::

          This operation requires `Signature Version 4
          <https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html>`__ .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/DeleteSAMLProvider>`_

        **Request Syntax**
        ::

          response = saml_provider.delete()

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        Returns a list of all the available sub-resources for this
        Resource.

        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self, *args: Any, **kwargs: Any) -> None:
        """
        Calls :py:meth:`IAM.Client.get_saml_provider` to update the attributes of the SamlProvider
        resource. Note that the load and reload methods are the same method and can be used
        interchangeably.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/None>`_

        **Request Syntax**

        ::

          saml_provider.load()
        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self, *args: Any, **kwargs: Any) -> None:
        """
        Calls :py:meth:`IAM.Client.get_saml_provider` to update the attributes of the SamlProvider
        resource. Note that the load and reload methods are the same method and can be used
        interchangeably.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/None>`_

        **Request Syntax**

        ::

          saml_provider.load()
        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update(self, SAMLMetadataDocument: str) -> SamlProviderUpdateResponseTypeDef:
        """
        Updates the metadata document for an existing SAML provider resource object.

        .. note::

          This operation requires `Signature Version 4
          <https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html>`__ .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/UpdateSAMLProvider>`_

        **Request Syntax**
        ::

          response = saml_provider.update(
              SAMLMetadataDocument='string',

          )
        :type SAMLMetadataDocument: string
        :param SAMLMetadataDocument: **[REQUIRED]**

          An XML document generated by an identity provider (IdP) that supports SAML 2.0. The
          document includes the issuer's name, expiration information, and keys that can be used to
          validate the SAML authentication response (assertions) that are received from the IdP. You
          must generate the metadata document using the identity management software that is used as
          your organization's IdP.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'SAMLProviderArn': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Contains the response to a successful  UpdateSAMLProvider request.

            - **SAMLProviderArn** *(string) --*

              The Amazon Resource Name (ARN) of the SAML provider that was updated.
        """


class ServerCertificate(Boto3ServiceResource):
    server_certificate_metadata: Dict[str, Any]
    certificate_body: str
    certificate_chain: str
    name: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, *args: Any, **kwargs: Any) -> None:
        """
        Deletes the specified server certificate.

        For more information about working with server certificates, see `Working with Server
        Certificates
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_server-certs.html>`__ in
        the *IAM User Guide* . This topic also includes a list of AWS services that can use the
        server certificates that you manage with IAM.

        .. warning::

          If you are using a server certificate with Elastic Load Balancing, deleting the
          certificate could have implications for your application. If Elastic Load Balancing
          doesn't detect the deletion of bound certificates, it may continue to use the
          certificates. This could cause Elastic Load Balancing to stop accepting traffic. We
          recommend that you remove the reference to the certificate from Elastic Load Balancing
          before using this command to delete the certificate. For more information, go to
          `DeleteLoadBalancerListeners
          <https://docs.aws.amazon.com/ElasticLoadBalancing/latest/APIReference/API_DeleteLoadBalancerListeners.html>`__
          in the *Elastic Load Balancing API Reference* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/DeleteServerCertificate>`_

        **Request Syntax**
        ::

          response = server_certificate.delete()

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        Returns a list of all the available sub-resources for this
        Resource.

        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self, *args: Any, **kwargs: Any) -> None:
        """
        Calls :py:meth:`IAM.Client.get_server_certificate` to update the attributes of the
        ServerCertificate resource. Note that the load and reload methods are the same method and
        can be used interchangeably.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/None>`_

        **Request Syntax**

        ::

          server_certificate.load()
        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self, *args: Any, **kwargs: Any) -> None:
        """
        Calls :py:meth:`IAM.Client.get_server_certificate` to update the attributes of the
        ServerCertificate resource. Note that the load and reload methods are the same method and
        can be used interchangeably.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/None>`_

        **Request Syntax**

        ::

          server_certificate.load()
        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update(
        self, NewPath: str = None, NewServerCertificateName: str = None
    ) -> service_resource_scope.ServerCertificate:
        """
        Updates the name and/or the path of the specified server certificate stored in IAM.

        For more information about working with server certificates, see `Working with Server
        Certificates
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_server-certs.html>`__ in
        the *IAM User Guide* . This topic also includes a list of AWS services that can use the
        server certificates that you manage with IAM.

        .. warning::

          You should understand the implications of changing a server certificate's path or name.
          For more information, see `Renaming a Server Certificate
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_server-certs_manage.html#RenamingServerCerts>`__
          in the *IAM User Guide* .

        .. note::

          The person making the request (the principal), must have permission to change the server
          certificate with the old name and the new name. For example, to change the certificate
          named ``ProductionCert`` to ``ProdCert`` , the principal must have a policy that allows
          them to update both certificates. If the principal has permission to update the
          ``ProductionCert`` group, but not the ``ProdCert`` certificate, then the update fails. For
          more information about permissions, see `Access Management
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/access.html>`__ in the *IAM User Guide*
          .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/UpdateServerCertificate>`_

        **Request Syntax**
        ::

          server_certificate = server_certificate.update(
              NewPath='string',
              NewServerCertificateName='string'
          )
        :type NewPath: string
        :param NewPath:

          The new path for the server certificate. Include this only if you are updating the server
          certificate's path.

          This parameter allows (through its `regex pattern <http://wikipedia.org/wiki/regex>`__ ) a
          string of characters consisting of either a forward slash (/) by itself or a string that
          must begin and end with forward slashes. In addition, it can contain any ASCII character
          from the ! (\\u0021) through the DEL character (\\u007F), including most punctuation
          characters, digits, and upper and lowercased letters.

        :type NewServerCertificateName: string
        :param NewServerCertificateName:

          The new name for the server certificate. Include this only if you are updating the server
          certificate's name. The name of the certificate cannot contain any spaces.

          This parameter allows (through its `regex pattern <http://wikipedia.org/wiki/regex>`__ ) a
          string of characters consisting of upper and lowercase alphanumeric characters with no
          spaces. You can also include any of the following characters: _+=,.@-

        :rtype: :py:class:`iam.ServerCertificate`
        :returns: ServerCertificate resource
        """


class SigningCertificate(Boto3ServiceResource):
    certificate_id: str
    certificate_body: str
    status: str
    upload_date: datetime
    user_name: str
    id: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def activate(self, *args: Any, **kwargs: Any) -> None:
        """
        Changes the status of the specified user signing certificate from active to disabled, or
        vice versa. This operation can be used to disable an IAM user's signing certificate as part
        of a certificate rotation work flow.

        If the ``UserName`` field is not specified, the user name is determined implicitly based on
        the AWS access key ID used to sign the request. This operation works for access keys under
        the AWS account. Consequently, you can use this operation to manage AWS account root user
        credentials even if the AWS account has no associated users.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/UpdateSigningCertificate>`_

        **Request Syntax**
        ::

          response = signing_certificate.activate()

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def deactivate(self, *args: Any, **kwargs: Any) -> None:
        """
        Changes the status of the specified user signing certificate from active to disabled, or
        vice versa. This operation can be used to disable an IAM user's signing certificate as part
        of a certificate rotation work flow.

        If the ``UserName`` field is not specified, the user name is determined implicitly based on
        the AWS access key ID used to sign the request. This operation works for access keys under
        the AWS account. Consequently, you can use this operation to manage AWS account root user
        credentials even if the AWS account has no associated users.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/UpdateSigningCertificate>`_

        **Request Syntax**
        ::

          response = signing_certificate.deactivate()

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, *args: Any, **kwargs: Any) -> None:
        """
        Deletes a signing certificate associated with the specified IAM user.

        If you do not specify a user name, IAM determines the user name implicitly based on the AWS
        access key ID signing the request. This operation works for access keys under the AWS
        account. Consequently, you can use this operation to manage AWS account root user
        credentials even if the AWS account has no associated IAM users.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/DeleteSigningCertificate>`_

        **Request Syntax**
        ::

          response = signing_certificate.delete()

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        Returns a list of all the available sub-resources for this
        Resource.

        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """


class User(Boto3ServiceResource):
    path: str
    user_name: str
    user_id: str
    arn: str
    create_date: datetime
    password_last_used: datetime
    permissions_boundary: Dict[str, Any]
    tags: List[Any]
    name: str
    access_keys: service_resource_scope.UserAccessKeysCollection
    attached_policies: service_resource_scope.UserAttachedPoliciesCollection
    groups: service_resource_scope.UserGroupsCollection
    mfa_devices: service_resource_scope.UserMfaDevicesCollection
    policies: service_resource_scope.UserPoliciesCollection
    signing_certificates: service_resource_scope.UserSigningCertificatesCollection

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def add_group(self, GroupName: str) -> None:
        """
        Adds the specified user to the specified group.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/AddUserToGroup>`_

        **Request Syntax**
        ::

          response = user.add_group(
              GroupName='string',

          )
        :type GroupName: string
        :param GroupName: **[REQUIRED]**

          The name of the group to update.

          This parameter allows (through its `regex pattern <http://wikipedia.org/wiki/regex>`__ ) a
          string of characters consisting of upper and lowercase alphanumeric characters with no
          spaces. You can also include any of the following characters: _+=,.@-

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def attach_policy(self, PolicyArn: str) -> None:
        """
        Attaches the specified managed policy to the specified user.

        You use this API to attach a *managed* policy to a user. To embed an inline policy in a
        user, use  PutUserPolicy .

        For more information about policies, see `Managed Policies and Inline Policies
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in the
        *IAM User Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/AttachUserPolicy>`_

        **Request Syntax**
        ::

          response = user.attach_policy(
              PolicyArn='string'
          )
        :type PolicyArn: string
        :param PolicyArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the IAM policy you want to attach.

          For more information about ARNs, see `Amazon Resource Names (ARNs) and AWS Service
          Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__
          in the *AWS General Reference* .

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create(
        self,
        Path: str = None,
        PermissionsBoundary: str = None,
        Tags: List[UserCreateTagsTypeDef] = None,
    ) -> service_resource_scope.User:
        """
        Creates a new IAM user for your AWS account.

        For information about limitations on the number of IAM users you can create, see
        `Limitations on IAM Entities
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/LimitationsOnEntities.html>`__ in the *IAM
        User Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/CreateUser>`_

        **Request Syntax**
        ::

          user = user.create(
              Path='string',
              PermissionsBoundary='string',
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ]
          )
        :type Path: string
        :param Path:

          The path for the user name. For more information about paths, see `IAM Identifiers
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_Identifiers.html>`__ in the *IAM
          User Guide* .

          This parameter is optional. If it is not included, it defaults to a slash (/).

          This parameter allows (through its `regex pattern <http://wikipedia.org/wiki/regex>`__ ) a
          string of characters consisting of either a forward slash (/) by itself or a string that
          must begin and end with forward slashes. In addition, it can contain any ASCII character
          from the ! (\\u0021) through the DEL character (\\u007F), including most punctuation
          characters, digits, and upper and lowercased letters.

        :type PermissionsBoundary: string
        :param PermissionsBoundary:

          The ARN of the policy that is used to set the permissions boundary for the user.

        :type Tags: list
        :param Tags:

          A list of tags that you want to attach to the newly created user. Each tag consists of a
          key name and an associated value. For more information about tagging, see `Tagging IAM
          Identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the *IAM
          User Guide* .

          .. note::

            If any one of the tags is invalid or if you exceed the allowed number of tags per user,
            then the entire request fails and the user is not created.

          - *(dict) --*

            A structure that represents user-provided metadata that can be associated with a
            resource such as an IAM user or role. For more information about tagging, see `Tagging
            IAM Identities <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_tags.html>`__ in the
            *IAM User Guide* .

            - **Key** *(string) --* **[REQUIRED]**

              The key name that can be used to look up or retrieve the associated value. For
              example, ``Department`` or ``Cost Center`` are common choices.

            - **Value** *(string) --* **[REQUIRED]**

              The value associated with this tag. For example, tags with a key name of
              ``Department`` could have values such as ``Human Resources`` , ``Accounting`` , and
              ``Support`` . Tags with a key name of ``Cost Center`` might have values that consist
              of the number associated with the different cost centers in your company. Typically,
              many resources have tags with the same key name but with different values.

              .. note::

                AWS always interprets the tag ``Value`` as a single string. If you need to store an
                array, you can store comma-separated values in the string. However, you must
                interpret the value in your code.

        :rtype: :py:class:`iam.User`
        :returns: User resource
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_access_key_pair(
        self, *args: Any, **kwargs: Any
    ) -> service_resource_scope.AccessKeyPair:
        """
        Creates a new AWS secret access key and corresponding AWS access key ID for the specified
        user. The default status for new keys is ``Active`` .

        If you do not specify a user name, IAM determines the user name implicitly based on the AWS
        access key ID signing the request. This operation works for access keys under the AWS
        account. Consequently, you can use this operation to manage AWS account root user
        credentials. This is true even if the AWS account has no associated users.

        For information about limits on the number of keys you can create, see `Limitations on IAM
        Entities <https://docs.aws.amazon.com/IAM/latest/UserGuide/LimitationsOnEntities.html>`__ in
        the *IAM User Guide* .

        .. warning::

          To ensure the security of your AWS account, the secret access key is accessible only
          during key and user creation. You must save the key (for example, in a text file) if you
          want to be able to access it again. If a secret key is lost, you can delete the access
          keys for the associated user and then create new keys.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/CreateAccessKey>`_

        **Request Syntax**
        ::

          access_key_pair = user.create_access_key_pair()

        :rtype: :py:class:`iam.AccessKeyPair`
        :returns: AccessKeyPair resource
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_login_profile(
        self, Password: str, PasswordResetRequired: bool = None
    ) -> service_resource_scope.LoginProfile:
        """
        Creates a password for the specified user, giving the user the ability to access AWS
        services through the AWS Management Console. For more information about managing passwords,
        see `Managing Passwords
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/Using_ManagingLogins.html>`__ in the *IAM
        User Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/CreateLoginProfile>`_

        **Request Syntax**
        ::

          login_profile = user.create_login_profile(
              Password='string',
              PasswordResetRequired=True|False
          )
        :type Password: string
        :param Password: **[REQUIRED]**

          The new password for the user.

          The `regex pattern <http://wikipedia.org/wiki/regex>`__ that is used to validate this
          parameter is a string of characters. That string can include almost any printable ASCII
          character from the space (\\u0020) through the end of the ASCII character range (\\u00FF).
          You can also include the tab (\\u0009), line feed (\\u000A), and carriage return (\\u000D)
          characters. Any of these characters are valid in a password. However, many tools, such as
          the AWS Management Console, might restrict the ability to type certain characters because
          they have special meaning within that tool.

        :type PasswordResetRequired: boolean
        :param PasswordResetRequired:

          Specifies whether the user is required to set a new password on next sign-in.

        :rtype: :py:class:`iam.LoginProfile`
        :returns: LoginProfile resource
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_policy(
        self, PolicyName: str, PolicyDocument: str
    ) -> service_resource_scope.UserPolicy:
        """
        Adds or updates an inline policy document that is embedded in the specified IAM user.

        An IAM user can also have a managed policy attached to it. To attach a managed policy to a
        user, use  AttachUserPolicy . To create a new managed policy, use  CreatePolicy . For
        information about policies, see `Managed Policies and Inline Policies
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in the
        *IAM User Guide* .

        For information about limits on the number of inline policies that you can embed in a user,
        see `Limitations on IAM Entities
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/LimitationsOnEntities.html>`__ in the *IAM
        User Guide* .

        .. note::

          Because policy documents can be large, you should use POST rather than GET when calling
          ``PutUserPolicy`` . For general information about using the Query API with IAM, go to
          `Making Query Requests
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/IAM_UsingQueryAPI.html>`__ in the *IAM
          User Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/PutUserPolicy>`_

        **Request Syntax**
        ::

          user_policy = user.create_policy(
              PolicyName='string',
              PolicyDocument='string'
          )
        :type PolicyName: string
        :param PolicyName: **[REQUIRED]**

          The name of the policy document.

          This parameter allows (through its `regex pattern <http://wikipedia.org/wiki/regex>`__ ) a
          string of characters consisting of upper and lowercase alphanumeric characters with no
          spaces. You can also include any of the following characters: _+=,.@-

        :type PolicyDocument: string
        :param PolicyDocument: **[REQUIRED]**

          The policy document.

          You must provide policies in JSON format in IAM. However, for AWS CloudFormation templates
          formatted in YAML, you can provide the policy in JSON or YAML format. AWS CloudFormation
          always converts a YAML policy to JSON format before submitting it to IAM.

          The `regex pattern <http://wikipedia.org/wiki/regex>`__ used to validate this parameter is
          a string of characters consisting of the following:

          * Any printable ASCII character ranging from the space character (\\u0020) through the end
          of the ASCII character range

          * The printable characters in the Basic Latin and Latin-1 Supplement character set
          (through \\u00FF)

          * The special characters tab (\\u0009), line feed (\\u000A), and carriage return (\\u000D)

        :rtype: :py:class:`iam.UserPolicy`
        :returns: UserPolicy resource
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, *args: Any, **kwargs: Any) -> None:
        """
        Deletes the specified IAM user. Unlike the AWS Management Console, when you delete a user
        programmatically, you must delete the items attached to the user manually, or the deletion
        fails. For more information, see `Deleting an IAM User
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_manage.html#id_users_deleting_cli>`__
        . Before attempting to delete a user, remove the following items:

        * Password ( DeleteLoginProfile )

        * Access keys ( DeleteAccessKey )

        * Signing certificate ( DeleteSigningCertificate )

        * SSH public key ( DeleteSSHPublicKey )

        * Git credentials ( DeleteServiceSpecificCredential )

        * Multi-factor authentication (MFA) device ( DeactivateMFADevice ,  DeleteVirtualMFADevice )

        * Inline policies ( DeleteUserPolicy )

        * Attached managed policies ( DetachUserPolicy )

        * Group memberships ( RemoveUserFromGroup )

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/DeleteUser>`_

        **Request Syntax**
        ::

          response = user.delete()

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def detach_policy(self, PolicyArn: str) -> None:
        """
        Removes the specified managed policy from the specified user.

        A user can also have inline policies embedded with it. To delete an inline policy, use the
        DeleteUserPolicy API. For information about policies, see `Managed Policies and Inline
        Policies
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in the
        *IAM User Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/DetachUserPolicy>`_

        **Request Syntax**
        ::

          response = user.detach_policy(
              PolicyArn='string'
          )
        :type PolicyArn: string
        :param PolicyArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the IAM policy you want to detach.

          For more information about ARNs, see `Amazon Resource Names (ARNs) and AWS Service
          Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__
          in the *AWS General Reference* .

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def enable_mfa(
        self, SerialNumber: str, AuthenticationCode1: str, AuthenticationCode2: str
    ) -> service_resource_scope.MfaDevice:
        """
        Enables the specified MFA device and associates it with the specified IAM user. When
        enabled, the MFA device is required for every subsequent login by the IAM user associated
        with the device.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/EnableMFADevice>`_

        **Request Syntax**
        ::

          mfa_device = user.enable_mfa(
              SerialNumber='string',
              AuthenticationCode1='string',
              AuthenticationCode2='string'
          )
        :type SerialNumber: string
        :param SerialNumber: **[REQUIRED]**

          The serial number that uniquely identifies the MFA device. For virtual MFA devices, the
          serial number is the device ARN.

          This parameter allows (through its `regex pattern <http://wikipedia.org/wiki/regex>`__ ) a
          string of characters consisting of upper and lowercase alphanumeric characters with no
          spaces. You can also include any of the following characters: =,.@:/-

        :type AuthenticationCode1: string
        :param AuthenticationCode1: **[REQUIRED]**

          An authentication code emitted by the device.

          The format for this parameter is a string of six digits.

          .. warning::

            Submit your request immediately after generating the authentication codes. If you
            generate the codes and then wait too long to submit the request, the MFA device
            successfully associates with the user but the MFA device becomes out of sync. This
            happens because time-based one-time passwords (TOTP) expire after a short period of
            time. If this happens, you can `resync the device
            <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_sync.html>`__ .

        :type AuthenticationCode2: string
        :param AuthenticationCode2: **[REQUIRED]**

          A subsequent authentication code emitted by the device.

          The format for this parameter is a string of six digits.

          .. warning::

            Submit your request immediately after generating the authentication codes. If you
            generate the codes and then wait too long to submit the request, the MFA device
            successfully associates with the user but the MFA device becomes out of sync. This
            happens because time-based one-time passwords (TOTP) expire after a short period of
            time. If this happens, you can `resync the device
            <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_sync.html>`__ .

        :rtype: :py:class:`iam.MfaDevice`
        :returns: MfaDevice resource
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        Returns a list of all the available sub-resources for this
        Resource.

        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self, *args: Any, **kwargs: Any) -> None:
        """
        Calls :py:meth:`IAM.Client.get_user` to update the attributes of the User resource. Note
        that the load and reload methods are the same method and can be used interchangeably.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/None>`_

        **Request Syntax**

        ::

          user.load()
        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self, *args: Any, **kwargs: Any) -> None:
        """
        Calls :py:meth:`IAM.Client.get_user` to update the attributes of the User resource. Note
        that the load and reload methods are the same method and can be used interchangeably.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/None>`_

        **Request Syntax**

        ::

          user.load()
        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def remove_group(self, GroupName: str) -> None:
        """
        Removes the specified user from the specified group.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/RemoveUserFromGroup>`_

        **Request Syntax**
        ::

          response = user.remove_group(
              GroupName='string',

          )
        :type GroupName: string
        :param GroupName: **[REQUIRED]**

          The name of the group to update.

          This parameter allows (through its `regex pattern <http://wikipedia.org/wiki/regex>`__ ) a
          string of characters consisting of upper and lowercase alphanumeric characters with no
          spaces. You can also include any of the following characters: _+=,.@-

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update(self, NewPath: str = None, NewUserName: str = None) -> service_resource_scope.User:
        """
        Updates the name and/or the path of the specified IAM user.

        .. warning::

          You should understand the implications of changing an IAM user's path or name. For more
          information, see `Renaming an IAM User
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_manage.html#id_users_renaming>`__
          and `Renaming an IAM Group
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups_manage_rename.html>`__ in the
          *IAM User Guide* .

        .. note::

          To change a user name, the requester must have appropriate permissions on both the source
          object and the target object. For example, to change Bob to Robert, the entity making the
          request must have permission on Bob and Robert, or must have permission on all (*). For
          more information about permissions, see `Permissions and Policies
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/PermissionsAndPolicies.html>`__ .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/UpdateUser>`_

        **Request Syntax**
        ::

          user = user.update(
              NewPath='string',
              NewUserName='string'
          )
        :type NewPath: string
        :param NewPath:

          New path for the IAM user. Include this parameter only if you're changing the user's path.

          This parameter allows (through its `regex pattern <http://wikipedia.org/wiki/regex>`__ ) a
          string of characters consisting of either a forward slash (/) by itself or a string that
          must begin and end with forward slashes. In addition, it can contain any ASCII character
          from the ! (\\u0021) through the DEL character (\\u007F), including most punctuation
          characters, digits, and upper and lowercased letters.

        :type NewUserName: string
        :param NewUserName:

          New name for the user. Include this parameter only if you're changing the user's name.

          IAM user, group, role, and policy names must be unique within the account. Names are not
          distinguished by case. For example, you cannot create resources named both "MyResource"
          and "myresource".

        :rtype: :py:class:`iam.User`
        :returns: User resource
        """


class UserPolicy(Boto3ServiceResource):
    policy_name: str
    policy_document: str
    user_name: str
    name: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, *args: Any, **kwargs: Any) -> None:
        """
        Deletes the specified inline policy that is embedded in the specified IAM user.

        A user can also have managed policies attached to it. To detach a managed policy from a
        user, use  DetachUserPolicy . For more information about policies, refer to `Managed
        Policies and Inline Policies
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in the
        *IAM User Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/DeleteUserPolicy>`_

        **Request Syntax**
        ::

          response = user_policy.delete()

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        Returns a list of all the available sub-resources for this
        Resource.

        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def load(self, *args: Any, **kwargs: Any) -> None:
        """
        Calls :py:meth:`IAM.Client.get_user_policy` to update the attributes of the UserPolicy
        resource. Note that the load and reload methods are the same method and can be used
        interchangeably.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/None>`_

        **Request Syntax**

        ::

          user_policy.load()
        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put(self, PolicyDocument: str) -> None:
        """
        Adds or updates an inline policy document that is embedded in the specified IAM user.

        An IAM user can also have a managed policy attached to it. To attach a managed policy to a
        user, use  AttachUserPolicy . To create a new managed policy, use  CreatePolicy . For
        information about policies, see `Managed Policies and Inline Policies
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/policies-managed-vs-inline.html>`__ in the
        *IAM User Guide* .

        For information about limits on the number of inline policies that you can embed in a user,
        see `Limitations on IAM Entities
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/LimitationsOnEntities.html>`__ in the *IAM
        User Guide* .

        .. note::

          Because policy documents can be large, you should use POST rather than GET when calling
          ``PutUserPolicy`` . For general information about using the Query API with IAM, go to
          `Making Query Requests
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/IAM_UsingQueryAPI.html>`__ in the *IAM
          User Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/PutUserPolicy>`_

        **Request Syntax**
        ::

          response = user_policy.put(
              PolicyDocument='string'
          )
        :type PolicyDocument: string
        :param PolicyDocument: **[REQUIRED]**

          The policy document.

          You must provide policies in JSON format in IAM. However, for AWS CloudFormation templates
          formatted in YAML, you can provide the policy in JSON or YAML format. AWS CloudFormation
          always converts a YAML policy to JSON format before submitting it to IAM.

          The `regex pattern <http://wikipedia.org/wiki/regex>`__ used to validate this parameter is
          a string of characters consisting of the following:

          * Any printable ASCII character ranging from the space character (\\u0020) through the end
          of the ASCII character range

          * The printable characters in the Basic Latin and Latin-1 Supplement character set
          (through \\u00FF)

          * The special characters tab (\\u0009), line feed (\\u000A), and carriage return (\\u000D)

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def reload(self, *args: Any, **kwargs: Any) -> None:
        """
        Calls :py:meth:`IAM.Client.get_user_policy` to update the attributes of the UserPolicy
        resource. Note that the load and reload methods are the same method and can be used
        interchangeably.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/None>`_

        **Request Syntax**

        ::

          user_policy.load()
        :returns: None
        """


class VirtualMfaDevice(Boto3ServiceResource):
    base32_string_seed: bytes
    qr_code_png: bytes
    user_attribute: Dict[str, Any]
    enable_date: datetime
    serial_number: str

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete(self, *args: Any, **kwargs: Any) -> None:
        """
        Deletes a virtual MFA device.

        .. note::

          You must deactivate a user's virtual MFA device before you can delete it. For information
          about deactivating MFA devices, see  DeactivateMFADevice .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/DeleteVirtualMFADevice>`_

        **Request Syntax**
        ::

          response = virtual_mfa_device.delete()

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_available_subresources(self) -> List[str]:
        """
        Returns a list of all the available sub-resources for this
        Resource.

        :returns: A list containing the name of each sub-resource for this
            resource
        :rtype: list of str
        """


class ServiceResourceGroupsCollection(ResourceCollection):
    """
    A group of resources. See :py:class:`Action`.

    :type name: string
    :param name: The name of the collection
    :type definition: dict
    :param definition: The JSON definition
    :type resource_defs: dict
    :param resource_defs: All resources defined in the service
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.Group]:
        """
        Creates an iterable of all Group resources in the collection.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListGroups>`_

        **Request Syntax**
        ::

          group_iterator = iam.groups.all()

        :rtype: list(:py:class:`iam.Group`)
        :returns: A list of Group resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self, PathPrefix: str = None, Marker: str = None, MaxItems: int = None
    ) -> List[service_resource_scope.Group]:
        """
        Creates an iterable of all Group resources in the collection filtered by kwargs passed to
        method.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListGroups>`_

        **Request Syntax**
        ::

          group_iterator = iam.groups.filter(
              PathPrefix='string',
              Marker='string',
              MaxItems=123
          )
        :type PathPrefix: string
        :param PathPrefix:

          The path prefix for filtering the results. For example, the prefix
          ``/division_abc/subdivision_xyz/`` gets all groups whose path starts with
          ``/division_abc/subdivision_xyz/`` .

          This parameter is optional. If it is not included, it defaults to a slash (/), listing all
          groups. This parameter allows (through its `regex pattern
          <http://wikipedia.org/wiki/regex>`__ ) a string of characters consisting of either a
          forward slash (/) by itself or a string that must begin and end with forward slashes. In
          addition, it can contain any ASCII character from the ! (\\u0021) through the DEL
          character (\\u007F), including most punctuation characters, digits, and upper and
          lowercased letters.

        :type Marker: string
        :param Marker:

          Use this parameter only when paginating results and only after you receive a response
          indicating that the results are truncated. Set it to the value of the ``Marker`` element
          in the response that you received to indicate where the next call should start.

        :type MaxItems: integer
        :param MaxItems:

          Use this only when paginating results to indicate the maximum number of items you want in
          the response. If additional items exist beyond the maximum you specify, the
          ``IsTruncated`` response element is ``true`` .

          If you do not include this parameter, the number of items defaults to 100. Note that IAM
          might return fewer results, even when there are more results available. In that case, the
          ``IsTruncated`` response element returns ``true`` , and ``Marker`` contains a value to
          include in the subsequent call that tells the service where to continue from.

        :rtype: list(:py:class:`iam.Group`)
        :returns: A list of Group resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        """
        Get a resource collection iterator from this manager.

        :rtype: :py:class:`ResourceCollection`
        :return: An iterable representing the collection of resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.Group]:
        """
        Creates an iterable up to a specified amount of Group resources in the collection.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListGroups>`_

        **Request Syntax**
        ::

          group_iterator = iam.groups.limit(
              count=123
          )
        :type count: integer
        :param count: The limit to the number of resources in the iterable.

        :rtype: list(:py:class:`iam.Group`)
        :returns: A list of Group resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.Group]:
        """
        Creates an iterable of all Group resources in the collection, but limits the number of items
        returned by each service call by the specified amount.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListGroups>`_

        **Request Syntax**
        ::

          group_iterator = iam.groups.page_size(
              count=123
          )
        :type count: integer
        :param count: The number of items returned by each service call

        :rtype: list(:py:class:`iam.Group`)
        :returns: A list of Group resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        """
        A generator which yields pages of resource instances after
        doing the appropriate service operation calls and handling
        any pagination on your behalf. Non-paginated calls will
        return a single page of items.

        Page size, item limit, and filter parameters are applied
        if they have previously been set.

            >>> bucket = s3.Bucket('boto3')
            >>> for page in bucket.objects.pages():
            ...     for obj in page:
            ...         print(obj.key)
            'key1'
            'key2'

        :rtype: list(:py:class:`~boto3.resources.base.ServiceResource`)
        :return: List of resource instances
        """


class ServiceResourceInstanceProfilesCollection(ResourceCollection):
    """
    A group of resources. See :py:class:`Action`.

    :type name: string
    :param name: The name of the collection
    :type definition: dict
    :param definition: The JSON definition
    :type resource_defs: dict
    :param resource_defs: All resources defined in the service
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.InstanceProfile]:
        """
        Creates an iterable of all InstanceProfile resources in the collection.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListInstanceProfiles>`_

        **Request Syntax**
        ::

          instance_profile_iterator = iam.instance_profiles.all()

        :rtype: list(:py:class:`iam.InstanceProfile`)
        :returns: A list of InstanceProfile resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self, PathPrefix: str = None, Marker: str = None, MaxItems: int = None
    ) -> List[service_resource_scope.InstanceProfile]:
        """
        Creates an iterable of all InstanceProfile resources in the collection filtered by kwargs
        passed to method.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListInstanceProfiles>`_

        **Request Syntax**
        ::

          instance_profile_iterator = iam.instance_profiles.filter(
              PathPrefix='string',
              Marker='string',
              MaxItems=123
          )
        :type PathPrefix: string
        :param PathPrefix:

          The path prefix for filtering the results. For example, the prefix
          ``/application_abc/component_xyz/`` gets all instance profiles whose path starts with
          ``/application_abc/component_xyz/`` .

          This parameter is optional. If it is not included, it defaults to a slash (/), listing all
          instance profiles. This parameter allows (through its `regex pattern
          <http://wikipedia.org/wiki/regex>`__ ) a string of characters consisting of either a
          forward slash (/) by itself or a string that must begin and end with forward slashes. In
          addition, it can contain any ASCII character from the ! (\\u0021) through the DEL
          character (\\u007F), including most punctuation characters, digits, and upper and
          lowercased letters.

        :type Marker: string
        :param Marker:

          Use this parameter only when paginating results and only after you receive a response
          indicating that the results are truncated. Set it to the value of the ``Marker`` element
          in the response that you received to indicate where the next call should start.

        :type MaxItems: integer
        :param MaxItems:

          Use this only when paginating results to indicate the maximum number of items you want in
          the response. If additional items exist beyond the maximum you specify, the
          ``IsTruncated`` response element is ``true`` .

          If you do not include this parameter, the number of items defaults to 100. Note that IAM
          might return fewer results, even when there are more results available. In that case, the
          ``IsTruncated`` response element returns ``true`` , and ``Marker`` contains a value to
          include in the subsequent call that tells the service where to continue from.

        :rtype: list(:py:class:`iam.InstanceProfile`)
        :returns: A list of InstanceProfile resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        """
        Get a resource collection iterator from this manager.

        :rtype: :py:class:`ResourceCollection`
        :return: An iterable representing the collection of resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.InstanceProfile]:
        """
        Creates an iterable up to a specified amount of InstanceProfile resources in the collection.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListInstanceProfiles>`_

        **Request Syntax**
        ::

          instance_profile_iterator = iam.instance_profiles.limit(
              count=123
          )
        :type count: integer
        :param count: The limit to the number of resources in the iterable.

        :rtype: list(:py:class:`iam.InstanceProfile`)
        :returns: A list of InstanceProfile resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.InstanceProfile]:
        """
        Creates an iterable of all InstanceProfile resources in the collection, but limits the
        number of items returned by each service call by the specified amount.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListInstanceProfiles>`_

        **Request Syntax**
        ::

          instance_profile_iterator = iam.instance_profiles.page_size(
              count=123
          )
        :type count: integer
        :param count: The number of items returned by each service call

        :rtype: list(:py:class:`iam.InstanceProfile`)
        :returns: A list of InstanceProfile resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        """
        A generator which yields pages of resource instances after
        doing the appropriate service operation calls and handling
        any pagination on your behalf. Non-paginated calls will
        return a single page of items.

        Page size, item limit, and filter parameters are applied
        if they have previously been set.

            >>> bucket = s3.Bucket('boto3')
            >>> for page in bucket.objects.pages():
            ...     for obj in page:
            ...         print(obj.key)
            'key1'
            'key2'

        :rtype: list(:py:class:`~boto3.resources.base.ServiceResource`)
        :return: List of resource instances
        """


class ServiceResourcePoliciesCollection(ResourceCollection):
    """
    A group of resources. See :py:class:`Action`.

    :type name: string
    :param name: The name of the collection
    :type definition: dict
    :param definition: The JSON definition
    :type resource_defs: dict
    :param resource_defs: All resources defined in the service
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.Policy]:
        """
        Creates an iterable of all Policy resources in the collection.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListPolicies>`_

        **Request Syntax**
        ::

          policy_iterator = iam.policies.all()

        :rtype: list(:py:class:`iam.Policy`)
        :returns: A list of Policy resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self,
        Scope: Literal["All", "AWS", "Local"] = None,
        OnlyAttached: bool = None,
        PathPrefix: str = None,
        PolicyUsageFilter: Literal["PermissionsPolicy", "PermissionsBoundary"] = None,
        Marker: str = None,
        MaxItems: int = None,
    ) -> List[service_resource_scope.Policy]:
        """
        Creates an iterable of all Policy resources in the collection filtered by kwargs passed to
        method.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListPolicies>`_

        **Request Syntax**
        ::

          policy_iterator = iam.policies.filter(
              Scope='All'|'AWS'|'Local',
              OnlyAttached=True|False,
              PathPrefix='string',
              PolicyUsageFilter='PermissionsPolicy'|'PermissionsBoundary',
              Marker='string',
              MaxItems=123
          )
        :type Scope: string
        :param Scope:

          The scope to use for filtering the results.

          To list only AWS managed policies, set ``Scope`` to ``AWS`` . To list only the customer
          managed policies in your AWS account, set ``Scope`` to ``Local`` .

          This parameter is optional. If it is not included, or if it is set to ``All`` , all
          policies are returned.

        :type OnlyAttached: boolean
        :param OnlyAttached:

          A flag to filter the results to only the attached policies.

          When ``OnlyAttached`` is ``true`` , the returned list contains only the policies that are
          attached to an IAM user, group, or role. When ``OnlyAttached`` is ``false`` , or when the
          parameter is not included, all policies are returned.

        :type PathPrefix: string
        :param PathPrefix:

          The path prefix for filtering the results. This parameter is optional. If it is not
          included, it defaults to a slash (/), listing all policies. This parameter allows (through
          its `regex pattern <http://wikipedia.org/wiki/regex>`__ ) a string of characters
          consisting of either a forward slash (/) by itself or a string that must begin and end
          with forward slashes. In addition, it can contain any ASCII character from the ! (\\u0021)
          through the DEL character (\\u007F), including most punctuation characters, digits, and
          upper and lowercased letters.

        :type PolicyUsageFilter: string
        :param PolicyUsageFilter:

          The policy usage method to use for filtering the results.

          To list only permissions policies, set ``PolicyUsageFilter`` to ``PermissionsPolicy`` . To
          list only the policies used to set permissions boundaries, set the value to
          ``PermissionsBoundary`` .

          This parameter is optional. If it is not included, all policies are returned.

        :type Marker: string
        :param Marker:

          Use this parameter only when paginating results and only after you receive a response
          indicating that the results are truncated. Set it to the value of the ``Marker`` element
          in the response that you received to indicate where the next call should start.

        :type MaxItems: integer
        :param MaxItems:

          Use this only when paginating results to indicate the maximum number of items you want in
          the response. If additional items exist beyond the maximum you specify, the
          ``IsTruncated`` response element is ``true`` .

          If you do not include this parameter, the number of items defaults to 100. Note that IAM
          might return fewer results, even when there are more results available. In that case, the
          ``IsTruncated`` response element returns ``true`` , and ``Marker`` contains a value to
          include in the subsequent call that tells the service where to continue from.

        :rtype: list(:py:class:`iam.Policy`)
        :returns: A list of Policy resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        """
        Get a resource collection iterator from this manager.

        :rtype: :py:class:`ResourceCollection`
        :return: An iterable representing the collection of resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.Policy]:
        """
        Creates an iterable up to a specified amount of Policy resources in the collection.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListPolicies>`_

        **Request Syntax**
        ::

          policy_iterator = iam.policies.limit(
              count=123
          )
        :type count: integer
        :param count: The limit to the number of resources in the iterable.

        :rtype: list(:py:class:`iam.Policy`)
        :returns: A list of Policy resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.Policy]:
        """
        Creates an iterable of all Policy resources in the collection, but limits the number of
        items returned by each service call by the specified amount.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListPolicies>`_

        **Request Syntax**
        ::

          policy_iterator = iam.policies.page_size(
              count=123
          )
        :type count: integer
        :param count: The number of items returned by each service call

        :rtype: list(:py:class:`iam.Policy`)
        :returns: A list of Policy resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        """
        A generator which yields pages of resource instances after
        doing the appropriate service operation calls and handling
        any pagination on your behalf. Non-paginated calls will
        return a single page of items.

        Page size, item limit, and filter parameters are applied
        if they have previously been set.

            >>> bucket = s3.Bucket('boto3')
            >>> for page in bucket.objects.pages():
            ...     for obj in page:
            ...         print(obj.key)
            'key1'
            'key2'

        :rtype: list(:py:class:`~boto3.resources.base.ServiceResource`)
        :return: List of resource instances
        """


class ServiceResourceRolesCollection(ResourceCollection):
    """
    A group of resources. See :py:class:`Action`.

    :type name: string
    :param name: The name of the collection
    :type definition: dict
    :param definition: The JSON definition
    :type resource_defs: dict
    :param resource_defs: All resources defined in the service
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.Role]:
        """
        Creates an iterable of all Role resources in the collection.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListRoles>`_

        **Request Syntax**
        ::

          role_iterator = iam.roles.all()

        :rtype: list(:py:class:`iam.Role`)
        :returns: A list of Role resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self, PathPrefix: str = None, Marker: str = None, MaxItems: int = None
    ) -> List[service_resource_scope.Role]:
        """
        Creates an iterable of all Role resources in the collection filtered by kwargs passed to
        method.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListRoles>`_

        **Request Syntax**
        ::

          role_iterator = iam.roles.filter(
              PathPrefix='string',
              Marker='string',
              MaxItems=123
          )
        :type PathPrefix: string
        :param PathPrefix:

          The path prefix for filtering the results. For example, the prefix
          ``/application_abc/component_xyz/`` gets all roles whose path starts with
          ``/application_abc/component_xyz/`` .

          This parameter is optional. If it is not included, it defaults to a slash (/), listing all
          roles. This parameter allows (through its `regex pattern
          <http://wikipedia.org/wiki/regex>`__ ) a string of characters consisting of either a
          forward slash (/) by itself or a string that must begin and end with forward slashes. In
          addition, it can contain any ASCII character from the ! (\\u0021) through the DEL
          character (\\u007F), including most punctuation characters, digits, and upper and
          lowercased letters.

        :type Marker: string
        :param Marker:

          Use this parameter only when paginating results and only after you receive a response
          indicating that the results are truncated. Set it to the value of the ``Marker`` element
          in the response that you received to indicate where the next call should start.

        :type MaxItems: integer
        :param MaxItems:

          Use this only when paginating results to indicate the maximum number of items you want in
          the response. If additional items exist beyond the maximum you specify, the
          ``IsTruncated`` response element is ``true`` .

          If you do not include this parameter, the number of items defaults to 100. Note that IAM
          might return fewer results, even when there are more results available. In that case, the
          ``IsTruncated`` response element returns ``true`` , and ``Marker`` contains a value to
          include in the subsequent call that tells the service where to continue from.

        :rtype: list(:py:class:`iam.Role`)
        :returns: A list of Role resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        """
        Get a resource collection iterator from this manager.

        :rtype: :py:class:`ResourceCollection`
        :return: An iterable representing the collection of resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.Role]:
        """
        Creates an iterable up to a specified amount of Role resources in the collection.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListRoles>`_

        **Request Syntax**
        ::

          role_iterator = iam.roles.limit(
              count=123
          )
        :type count: integer
        :param count: The limit to the number of resources in the iterable.

        :rtype: list(:py:class:`iam.Role`)
        :returns: A list of Role resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.Role]:
        """
        Creates an iterable of all Role resources in the collection, but limits the number of items
        returned by each service call by the specified amount.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListRoles>`_

        **Request Syntax**
        ::

          role_iterator = iam.roles.page_size(
              count=123
          )
        :type count: integer
        :param count: The number of items returned by each service call

        :rtype: list(:py:class:`iam.Role`)
        :returns: A list of Role resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        """
        A generator which yields pages of resource instances after
        doing the appropriate service operation calls and handling
        any pagination on your behalf. Non-paginated calls will
        return a single page of items.

        Page size, item limit, and filter parameters are applied
        if they have previously been set.

            >>> bucket = s3.Bucket('boto3')
            >>> for page in bucket.objects.pages():
            ...     for obj in page:
            ...         print(obj.key)
            'key1'
            'key2'

        :rtype: list(:py:class:`~boto3.resources.base.ServiceResource`)
        :return: List of resource instances
        """


class ServiceResourceSamlProvidersCollection(ResourceCollection):
    """
    A group of resources. See :py:class:`Action`.

    :type name: string
    :param name: The name of the collection
    :type definition: dict
    :param definition: The JSON definition
    :type resource_defs: dict
    :param resource_defs: All resources defined in the service
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.SamlProvider]:
        """
        Creates an iterable of all SamlProvider resources in the collection.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListSAMLProviders>`_

        **Request Syntax**
        ::

          saml_provider_iterator = iam.saml_providers.all()

        :rtype: list(:py:class:`iam.SamlProvider`)
        :returns: A list of SamlProvider resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(self, **kwargs: Any) -> List[service_resource_scope.SamlProvider]:
        """
        Creates an iterable of all SamlProvider resources in the collection filtered by kwargs
        passed to method.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListSAMLProviders>`_

        **Request Syntax**
        ::

          saml_provider_iterator = iam.saml_providers.filter()

        :rtype: list(:py:class:`iam.SamlProvider`)
        :returns: A list of SamlProvider resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        """
        Get a resource collection iterator from this manager.

        :rtype: :py:class:`ResourceCollection`
        :return: An iterable representing the collection of resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.SamlProvider]:
        """
        Creates an iterable up to a specified amount of SamlProvider resources in the collection.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListSAMLProviders>`_

        **Request Syntax**
        ::

          saml_provider_iterator = iam.saml_providers.limit(
              count=123
          )
        :type count: integer
        :param count: The limit to the number of resources in the iterable.

        :rtype: list(:py:class:`iam.SamlProvider`)
        :returns: A list of SamlProvider resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.SamlProvider]:
        """
        Creates an iterable of all SamlProvider resources in the collection, but limits the number
        of items returned by each service call by the specified amount.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListSAMLProviders>`_

        **Request Syntax**
        ::

          saml_provider_iterator = iam.saml_providers.page_size(
              count=123
          )
        :type count: integer
        :param count: The number of items returned by each service call

        :rtype: list(:py:class:`iam.SamlProvider`)
        :returns: A list of SamlProvider resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        """
        A generator which yields pages of resource instances after
        doing the appropriate service operation calls and handling
        any pagination on your behalf. Non-paginated calls will
        return a single page of items.

        Page size, item limit, and filter parameters are applied
        if they have previously been set.

            >>> bucket = s3.Bucket('boto3')
            >>> for page in bucket.objects.pages():
            ...     for obj in page:
            ...         print(obj.key)
            'key1'
            'key2'

        :rtype: list(:py:class:`~boto3.resources.base.ServiceResource`)
        :return: List of resource instances
        """


class ServiceResourceServerCertificatesCollection(ResourceCollection):
    """
    A group of resources. See :py:class:`Action`.

    :type name: string
    :param name: The name of the collection
    :type definition: dict
    :param definition: The JSON definition
    :type resource_defs: dict
    :param resource_defs: All resources defined in the service
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.ServerCertificate]:
        """
        Creates an iterable of all ServerCertificate resources in the collection.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListServerCertificates>`_

        **Request Syntax**
        ::

          server_certificate_iterator = iam.server_certificates.all()

        :rtype: list(:py:class:`iam.ServerCertificate`)
        :returns: A list of ServerCertificate resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self, PathPrefix: str = None, Marker: str = None, MaxItems: int = None
    ) -> List[service_resource_scope.ServerCertificate]:
        """
        Creates an iterable of all ServerCertificate resources in the collection filtered by kwargs
        passed to method.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListServerCertificates>`_

        **Request Syntax**
        ::

          server_certificate_iterator = iam.server_certificates.filter(
              PathPrefix='string',
              Marker='string',
              MaxItems=123
          )
        :type PathPrefix: string
        :param PathPrefix:

          The path prefix for filtering the results. For example: ``/company/servercerts`` would get
          all server certificates for which the path starts with ``/company/servercerts`` .

          This parameter is optional. If it is not included, it defaults to a slash (/), listing all
          server certificates. This parameter allows (through its `regex pattern
          <http://wikipedia.org/wiki/regex>`__ ) a string of characters consisting of either a
          forward slash (/) by itself or a string that must begin and end with forward slashes. In
          addition, it can contain any ASCII character from the ! (\\u0021) through the DEL
          character (\\u007F), including most punctuation characters, digits, and upper and
          lowercased letters.

        :type Marker: string
        :param Marker:

          Use this parameter only when paginating results and only after you receive a response
          indicating that the results are truncated. Set it to the value of the ``Marker`` element
          in the response that you received to indicate where the next call should start.

        :type MaxItems: integer
        :param MaxItems:

          Use this only when paginating results to indicate the maximum number of items you want in
          the response. If additional items exist beyond the maximum you specify, the
          ``IsTruncated`` response element is ``true`` .

          If you do not include this parameter, the number of items defaults to 100. Note that IAM
          might return fewer results, even when there are more results available. In that case, the
          ``IsTruncated`` response element returns ``true`` , and ``Marker`` contains a value to
          include in the subsequent call that tells the service where to continue from.

        :rtype: list(:py:class:`iam.ServerCertificate`)
        :returns: A list of ServerCertificate resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        """
        Get a resource collection iterator from this manager.

        :rtype: :py:class:`ResourceCollection`
        :return: An iterable representing the collection of resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.ServerCertificate]:
        """
        Creates an iterable up to a specified amount of ServerCertificate resources in the
        collection.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListServerCertificates>`_

        **Request Syntax**
        ::

          server_certificate_iterator = iam.server_certificates.limit(
              count=123
          )
        :type count: integer
        :param count: The limit to the number of resources in the iterable.

        :rtype: list(:py:class:`iam.ServerCertificate`)
        :returns: A list of ServerCertificate resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.ServerCertificate]:
        """
        Creates an iterable of all ServerCertificate resources in the collection, but limits the
        number of items returned by each service call by the specified amount.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListServerCertificates>`_

        **Request Syntax**
        ::

          server_certificate_iterator = iam.server_certificates.page_size(
              count=123
          )
        :type count: integer
        :param count: The number of items returned by each service call

        :rtype: list(:py:class:`iam.ServerCertificate`)
        :returns: A list of ServerCertificate resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        """
        A generator which yields pages of resource instances after
        doing the appropriate service operation calls and handling
        any pagination on your behalf. Non-paginated calls will
        return a single page of items.

        Page size, item limit, and filter parameters are applied
        if they have previously been set.

            >>> bucket = s3.Bucket('boto3')
            >>> for page in bucket.objects.pages():
            ...     for obj in page:
            ...         print(obj.key)
            'key1'
            'key2'

        :rtype: list(:py:class:`~boto3.resources.base.ServiceResource`)
        :return: List of resource instances
        """


class ServiceResourceUsersCollection(ResourceCollection):
    """
    A group of resources. See :py:class:`Action`.

    :type name: string
    :param name: The name of the collection
    :type definition: dict
    :param definition: The JSON definition
    :type resource_defs: dict
    :param resource_defs: All resources defined in the service
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.User]:
        """
        Creates an iterable of all User resources in the collection.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListUsers>`_

        **Request Syntax**
        ::

          user_iterator = iam.users.all()

        :rtype: list(:py:class:`iam.User`)
        :returns: A list of User resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self, PathPrefix: str = None, Marker: str = None, MaxItems: int = None
    ) -> List[service_resource_scope.User]:
        """
        Creates an iterable of all User resources in the collection filtered by kwargs passed to
        method.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListUsers>`_

        **Request Syntax**
        ::

          user_iterator = iam.users.filter(
              PathPrefix='string',
              Marker='string',
              MaxItems=123
          )
        :type PathPrefix: string
        :param PathPrefix:

          The path prefix for filtering the results. For example: ``/division_abc/subdivision_xyz/``
          , which would get all user names whose path starts with ``/division_abc/subdivision_xyz/``
          .

          This parameter is optional. If it is not included, it defaults to a slash (/), listing all
          user names. This parameter allows (through its `regex pattern
          <http://wikipedia.org/wiki/regex>`__ ) a string of characters consisting of either a
          forward slash (/) by itself or a string that must begin and end with forward slashes. In
          addition, it can contain any ASCII character from the ! (\\u0021) through the DEL
          character (\\u007F), including most punctuation characters, digits, and upper and
          lowercased letters.

        :type Marker: string
        :param Marker:

          Use this parameter only when paginating results and only after you receive a response
          indicating that the results are truncated. Set it to the value of the ``Marker`` element
          in the response that you received to indicate where the next call should start.

        :type MaxItems: integer
        :param MaxItems:

          Use this only when paginating results to indicate the maximum number of items you want in
          the response. If additional items exist beyond the maximum you specify, the
          ``IsTruncated`` response element is ``true`` .

          If you do not include this parameter, the number of items defaults to 100. Note that IAM
          might return fewer results, even when there are more results available. In that case, the
          ``IsTruncated`` response element returns ``true`` , and ``Marker`` contains a value to
          include in the subsequent call that tells the service where to continue from.

        :rtype: list(:py:class:`iam.User`)
        :returns: A list of User resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        """
        Get a resource collection iterator from this manager.

        :rtype: :py:class:`ResourceCollection`
        :return: An iterable representing the collection of resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.User]:
        """
        Creates an iterable up to a specified amount of User resources in the collection.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListUsers>`_

        **Request Syntax**
        ::

          user_iterator = iam.users.limit(
              count=123
          )
        :type count: integer
        :param count: The limit to the number of resources in the iterable.

        :rtype: list(:py:class:`iam.User`)
        :returns: A list of User resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.User]:
        """
        Creates an iterable of all User resources in the collection, but limits the number of items
        returned by each service call by the specified amount.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListUsers>`_

        **Request Syntax**
        ::

          user_iterator = iam.users.page_size(
              count=123
          )
        :type count: integer
        :param count: The number of items returned by each service call

        :rtype: list(:py:class:`iam.User`)
        :returns: A list of User resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        """
        A generator which yields pages of resource instances after
        doing the appropriate service operation calls and handling
        any pagination on your behalf. Non-paginated calls will
        return a single page of items.

        Page size, item limit, and filter parameters are applied
        if they have previously been set.

            >>> bucket = s3.Bucket('boto3')
            >>> for page in bucket.objects.pages():
            ...     for obj in page:
            ...         print(obj.key)
            'key1'
            'key2'

        :rtype: list(:py:class:`~boto3.resources.base.ServiceResource`)
        :return: List of resource instances
        """


class ServiceResourceVirtualMfaDevicesCollection(ResourceCollection):
    """
    A group of resources. See :py:class:`Action`.

    :type name: string
    :param name: The name of the collection
    :type definition: dict
    :param definition: The JSON definition
    :type resource_defs: dict
    :param resource_defs: All resources defined in the service
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.VirtualMfaDevice]:
        """
        Creates an iterable of all VirtualMfaDevice resources in the collection.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListVirtualMFADevices>`_

        **Request Syntax**
        ::

          virtual_mfa_device_iterator = iam.virtual_mfa_devices.all()

        :rtype: list(:py:class:`iam.VirtualMfaDevice`)
        :returns: A list of VirtualMfaDevice resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self,
        AssignmentStatus: Literal["Assigned", "Unassigned", "Any"] = None,
        Marker: str = None,
        MaxItems: int = None,
    ) -> List[service_resource_scope.VirtualMfaDevice]:
        """
        Creates an iterable of all VirtualMfaDevice resources in the collection filtered by kwargs
        passed to method.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListVirtualMFADevices>`_

        **Request Syntax**
        ::

          virtual_mfa_device_iterator = iam.virtual_mfa_devices.filter(
              AssignmentStatus='Assigned'|'Unassigned'|'Any',
              Marker='string',
              MaxItems=123
          )
        :type AssignmentStatus: string
        :param AssignmentStatus:

          The status (``Unassigned`` or ``Assigned`` ) of the devices to list. If you do not specify
          an ``AssignmentStatus`` , the operation defaults to ``Any`` , which lists both assigned
          and unassigned virtual MFA devices.,

        :type Marker: string
        :param Marker:

          Use this parameter only when paginating results and only after you receive a response
          indicating that the results are truncated. Set it to the value of the ``Marker`` element
          in the response that you received to indicate where the next call should start.

        :type MaxItems: integer
        :param MaxItems:

          Use this only when paginating results to indicate the maximum number of items you want in
          the response. If additional items exist beyond the maximum you specify, the
          ``IsTruncated`` response element is ``true`` .

          If you do not include this parameter, the number of items defaults to 100. Note that IAM
          might return fewer results, even when there are more results available. In that case, the
          ``IsTruncated`` response element returns ``true`` , and ``Marker`` contains a value to
          include in the subsequent call that tells the service where to continue from.

        :rtype: list(:py:class:`iam.VirtualMfaDevice`)
        :returns: A list of VirtualMfaDevice resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        """
        Get a resource collection iterator from this manager.

        :rtype: :py:class:`ResourceCollection`
        :return: An iterable representing the collection of resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.VirtualMfaDevice]:
        """
        Creates an iterable up to a specified amount of VirtualMfaDevice resources in the
        collection.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListVirtualMFADevices>`_

        **Request Syntax**
        ::

          virtual_mfa_device_iterator = iam.virtual_mfa_devices.limit(
              count=123
          )
        :type count: integer
        :param count: The limit to the number of resources in the iterable.

        :rtype: list(:py:class:`iam.VirtualMfaDevice`)
        :returns: A list of VirtualMfaDevice resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.VirtualMfaDevice]:
        """
        Creates an iterable of all VirtualMfaDevice resources in the collection, but limits the
        number of items returned by each service call by the specified amount.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListVirtualMFADevices>`_

        **Request Syntax**
        ::

          virtual_mfa_device_iterator = iam.virtual_mfa_devices.page_size(
              count=123
          )
        :type count: integer
        :param count: The number of items returned by each service call

        :rtype: list(:py:class:`iam.VirtualMfaDevice`)
        :returns: A list of VirtualMfaDevice resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        """
        A generator which yields pages of resource instances after
        doing the appropriate service operation calls and handling
        any pagination on your behalf. Non-paginated calls will
        return a single page of items.

        Page size, item limit, and filter parameters are applied
        if they have previously been set.

            >>> bucket = s3.Bucket('boto3')
            >>> for page in bucket.objects.pages():
            ...     for obj in page:
            ...         print(obj.key)
            'key1'
            'key2'

        :rtype: list(:py:class:`~boto3.resources.base.ServiceResource`)
        :return: List of resource instances
        """


class CurrentUserAccessKeysCollection(ResourceCollection):
    """
    A group of resources. See :py:class:`Action`.

    :type name: string
    :param name: The name of the collection
    :type definition: dict
    :param definition: The JSON definition
    :type resource_defs: dict
    :param resource_defs: All resources defined in the service
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.AccessKey]:
        """
        Creates an iterable of all AccessKey resources in the collection.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListAccessKeys>`_

        **Request Syntax**
        ::

          access_key_iterator = current_user.access_keys.all()

        :rtype: list(:py:class:`iam.AccessKey`)
        :returns: A list of AccessKey resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self, UserName: str = None, Marker: str = None, MaxItems: int = None
    ) -> List[service_resource_scope.AccessKey]:
        """
        Creates an iterable of all AccessKey resources in the collection filtered by kwargs passed
        to method.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListAccessKeys>`_

        **Request Syntax**
        ::

          access_key_iterator = current_user.access_keys.filter(
              UserName='string',
              Marker='string',
              MaxItems=123
          )
        :type UserName: string
        :param UserName:

          The name of the user.

          This parameter allows (through its `regex pattern <http://wikipedia.org/wiki/regex>`__ ) a
          string of characters consisting of upper and lowercase alphanumeric characters with no
          spaces. You can also include any of the following characters: _+=,.@-

        :type Marker: string
        :param Marker:

          Use this parameter only when paginating results and only after you receive a response
          indicating that the results are truncated. Set it to the value of the ``Marker`` element
          in the response that you received to indicate where the next call should start.

        :type MaxItems: integer
        :param MaxItems:

          Use this only when paginating results to indicate the maximum number of items you want in
          the response. If additional items exist beyond the maximum you specify, the
          ``IsTruncated`` response element is ``true`` .

          If you do not include this parameter, the number of items defaults to 100. Note that IAM
          might return fewer results, even when there are more results available. In that case, the
          ``IsTruncated`` response element returns ``true`` , and ``Marker`` contains a value to
          include in the subsequent call that tells the service where to continue from.

        :rtype: list(:py:class:`iam.AccessKey`)
        :returns: A list of AccessKey resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        """
        Get a resource collection iterator from this manager.

        :rtype: :py:class:`ResourceCollection`
        :return: An iterable representing the collection of resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.AccessKey]:
        """
        Creates an iterable up to a specified amount of AccessKey resources in the collection.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListAccessKeys>`_

        **Request Syntax**
        ::

          access_key_iterator = current_user.access_keys.limit(
              count=123
          )
        :type count: integer
        :param count: The limit to the number of resources in the iterable.

        :rtype: list(:py:class:`iam.AccessKey`)
        :returns: A list of AccessKey resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.AccessKey]:
        """
        Creates an iterable of all AccessKey resources in the collection, but limits the number of
        items returned by each service call by the specified amount.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListAccessKeys>`_

        **Request Syntax**
        ::

          access_key_iterator = current_user.access_keys.page_size(
              count=123
          )
        :type count: integer
        :param count: The number of items returned by each service call

        :rtype: list(:py:class:`iam.AccessKey`)
        :returns: A list of AccessKey resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        """
        A generator which yields pages of resource instances after
        doing the appropriate service operation calls and handling
        any pagination on your behalf. Non-paginated calls will
        return a single page of items.

        Page size, item limit, and filter parameters are applied
        if they have previously been set.

            >>> bucket = s3.Bucket('boto3')
            >>> for page in bucket.objects.pages():
            ...     for obj in page:
            ...         print(obj.key)
            'key1'
            'key2'

        :rtype: list(:py:class:`~boto3.resources.base.ServiceResource`)
        :return: List of resource instances
        """


class CurrentUserMfaDevicesCollection(ResourceCollection):
    """
    A group of resources. See :py:class:`Action`.

    :type name: string
    :param name: The name of the collection
    :type definition: dict
    :param definition: The JSON definition
    :type resource_defs: dict
    :param resource_defs: All resources defined in the service
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.MfaDevice]:
        """
        Creates an iterable of all MfaDevice resources in the collection.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListMFADevices>`_

        **Request Syntax**
        ::

          mfa_device_iterator = current_user.mfa_devices.all()

        :rtype: list(:py:class:`iam.MfaDevice`)
        :returns: A list of MfaDevice resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self, UserName: str = None, Marker: str = None, MaxItems: int = None
    ) -> List[service_resource_scope.MfaDevice]:
        """
        Creates an iterable of all MfaDevice resources in the collection filtered by kwargs passed
        to method.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListMFADevices>`_

        **Request Syntax**
        ::

          mfa_device_iterator = current_user.mfa_devices.filter(
              UserName='string',
              Marker='string',
              MaxItems=123
          )
        :type UserName: string
        :param UserName:

          The name of the user whose MFA devices you want to list.

          This parameter allows (through its `regex pattern <http://wikipedia.org/wiki/regex>`__ ) a
          string of characters consisting of upper and lowercase alphanumeric characters with no
          spaces. You can also include any of the following characters: _+=,.@-

        :type Marker: string
        :param Marker:

          Use this parameter only when paginating results and only after you receive a response
          indicating that the results are truncated. Set it to the value of the ``Marker`` element
          in the response that you received to indicate where the next call should start.

        :type MaxItems: integer
        :param MaxItems:

          Use this only when paginating results to indicate the maximum number of items you want in
          the response. If additional items exist beyond the maximum you specify, the
          ``IsTruncated`` response element is ``true`` .

          If you do not include this parameter, the number of items defaults to 100. Note that IAM
          might return fewer results, even when there are more results available. In that case, the
          ``IsTruncated`` response element returns ``true`` , and ``Marker`` contains a value to
          include in the subsequent call that tells the service where to continue from.

        :rtype: list(:py:class:`iam.MfaDevice`)
        :returns: A list of MfaDevice resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        """
        Get a resource collection iterator from this manager.

        :rtype: :py:class:`ResourceCollection`
        :return: An iterable representing the collection of resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.MfaDevice]:
        """
        Creates an iterable up to a specified amount of MfaDevice resources in the collection.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListMFADevices>`_

        **Request Syntax**
        ::

          mfa_device_iterator = current_user.mfa_devices.limit(
              count=123
          )
        :type count: integer
        :param count: The limit to the number of resources in the iterable.

        :rtype: list(:py:class:`iam.MfaDevice`)
        :returns: A list of MfaDevice resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.MfaDevice]:
        """
        Creates an iterable of all MfaDevice resources in the collection, but limits the number of
        items returned by each service call by the specified amount.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListMFADevices>`_

        **Request Syntax**
        ::

          mfa_device_iterator = current_user.mfa_devices.page_size(
              count=123
          )
        :type count: integer
        :param count: The number of items returned by each service call

        :rtype: list(:py:class:`iam.MfaDevice`)
        :returns: A list of MfaDevice resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        """
        A generator which yields pages of resource instances after
        doing the appropriate service operation calls and handling
        any pagination on your behalf. Non-paginated calls will
        return a single page of items.

        Page size, item limit, and filter parameters are applied
        if they have previously been set.

            >>> bucket = s3.Bucket('boto3')
            >>> for page in bucket.objects.pages():
            ...     for obj in page:
            ...         print(obj.key)
            'key1'
            'key2'

        :rtype: list(:py:class:`~boto3.resources.base.ServiceResource`)
        :return: List of resource instances
        """


class CurrentUserSigningCertificatesCollection(ResourceCollection):
    """
    A group of resources. See :py:class:`Action`.

    :type name: string
    :param name: The name of the collection
    :type definition: dict
    :param definition: The JSON definition
    :type resource_defs: dict
    :param resource_defs: All resources defined in the service
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.SigningCertificate]:
        """
        Creates an iterable of all SigningCertificate resources in the collection.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListSigningCertificates>`_

        **Request Syntax**
        ::

          signing_certificate_iterator = current_user.signing_certificates.all()

        :rtype: list(:py:class:`iam.SigningCertificate`)
        :returns: A list of SigningCertificate resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self, UserName: str = None, Marker: str = None, MaxItems: int = None
    ) -> List[service_resource_scope.SigningCertificate]:
        """
        Creates an iterable of all SigningCertificate resources in the collection filtered by kwargs
        passed to method.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListSigningCertificates>`_

        **Request Syntax**
        ::

          signing_certificate_iterator = current_user.signing_certificates.filter(
              UserName='string',
              Marker='string',
              MaxItems=123
          )
        :type UserName: string
        :param UserName:

          The name of the IAM user whose signing certificates you want to examine.

          This parameter allows (through its `regex pattern <http://wikipedia.org/wiki/regex>`__ ) a
          string of characters consisting of upper and lowercase alphanumeric characters with no
          spaces. You can also include any of the following characters: _+=,.@-

        :type Marker: string
        :param Marker:

          Use this parameter only when paginating results and only after you receive a response
          indicating that the results are truncated. Set it to the value of the ``Marker`` element
          in the response that you received to indicate where the next call should start.

        :type MaxItems: integer
        :param MaxItems:

          Use this only when paginating results to indicate the maximum number of items you want in
          the response. If additional items exist beyond the maximum you specify, the
          ``IsTruncated`` response element is ``true`` .

          If you do not include this parameter, the number of items defaults to 100. Note that IAM
          might return fewer results, even when there are more results available. In that case, the
          ``IsTruncated`` response element returns ``true`` , and ``Marker`` contains a value to
          include in the subsequent call that tells the service where to continue from.

        :rtype: list(:py:class:`iam.SigningCertificate`)
        :returns: A list of SigningCertificate resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        """
        Get a resource collection iterator from this manager.

        :rtype: :py:class:`ResourceCollection`
        :return: An iterable representing the collection of resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.SigningCertificate]:
        """
        Creates an iterable up to a specified amount of SigningCertificate resources in the
        collection.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListSigningCertificates>`_

        **Request Syntax**
        ::

          signing_certificate_iterator = current_user.signing_certificates.limit(
              count=123
          )
        :type count: integer
        :param count: The limit to the number of resources in the iterable.

        :rtype: list(:py:class:`iam.SigningCertificate`)
        :returns: A list of SigningCertificate resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.SigningCertificate]:
        """
        Creates an iterable of all SigningCertificate resources in the collection, but limits the
        number of items returned by each service call by the specified amount.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListSigningCertificates>`_

        **Request Syntax**
        ::

          signing_certificate_iterator = current_user.signing_certificates.page_size(
              count=123
          )
        :type count: integer
        :param count: The number of items returned by each service call

        :rtype: list(:py:class:`iam.SigningCertificate`)
        :returns: A list of SigningCertificate resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        """
        A generator which yields pages of resource instances after
        doing the appropriate service operation calls and handling
        any pagination on your behalf. Non-paginated calls will
        return a single page of items.

        Page size, item limit, and filter parameters are applied
        if they have previously been set.

            >>> bucket = s3.Bucket('boto3')
            >>> for page in bucket.objects.pages():
            ...     for obj in page:
            ...         print(obj.key)
            'key1'
            'key2'

        :rtype: list(:py:class:`~boto3.resources.base.ServiceResource`)
        :return: List of resource instances
        """


class GroupAttachedPoliciesCollection(ResourceCollection):
    """
    A group of resources. See :py:class:`Action`.

    :type name: string
    :param name: The name of the collection
    :type definition: dict
    :param definition: The JSON definition
    :type resource_defs: dict
    :param resource_defs: All resources defined in the service
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.Policy]:
        """
        Creates an iterable of all Policy resources in the collection.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListAttachedGroupPolicies>`_

        **Request Syntax**
        ::

          policy_iterator = group.attached_policies.all()

        :rtype: list(:py:class:`iam.Policy`)
        :returns: A list of Policy resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self, PathPrefix: str = None, Marker: str = None, MaxItems: int = None
    ) -> List[service_resource_scope.Policy]:
        """
        Creates an iterable of all Policy resources in the collection filtered by kwargs passed to
        method.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListAttachedGroupPolicies>`_

        **Request Syntax**
        ::

          policy_iterator = group.attached_policies.filter(
              PathPrefix='string',
              Marker='string',
              MaxItems=123
          )
        :type PathPrefix: string
        :param PathPrefix:

          The path prefix for filtering the results. This parameter is optional. If it is not
          included, it defaults to a slash (/), listing all policies.

          This parameter allows (through its `regex pattern <http://wikipedia.org/wiki/regex>`__ ) a
          string of characters consisting of either a forward slash (/) by itself or a string that
          must begin and end with forward slashes. In addition, it can contain any ASCII character
          from the ! (\\u0021) through the DEL character (\\u007F), including most punctuation
          characters, digits, and upper and lowercased letters.

        :type Marker: string
        :param Marker:

          Use this parameter only when paginating results and only after you receive a response
          indicating that the results are truncated. Set it to the value of the ``Marker`` element
          in the response that you received to indicate where the next call should start.

        :type MaxItems: integer
        :param MaxItems:

          Use this only when paginating results to indicate the maximum number of items you want in
          the response. If additional items exist beyond the maximum you specify, the
          ``IsTruncated`` response element is ``true`` .

          If you do not include this parameter, the number of items defaults to 100. Note that IAM
          might return fewer results, even when there are more results available. In that case, the
          ``IsTruncated`` response element returns ``true`` , and ``Marker`` contains a value to
          include in the subsequent call that tells the service where to continue from.

        :rtype: list(:py:class:`iam.Policy`)
        :returns: A list of Policy resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        """
        Get a resource collection iterator from this manager.

        :rtype: :py:class:`ResourceCollection`
        :return: An iterable representing the collection of resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.Policy]:
        """
        Creates an iterable up to a specified amount of Policy resources in the collection.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListAttachedGroupPolicies>`_

        **Request Syntax**
        ::

          policy_iterator = group.attached_policies.limit(
              count=123
          )
        :type count: integer
        :param count: The limit to the number of resources in the iterable.

        :rtype: list(:py:class:`iam.Policy`)
        :returns: A list of Policy resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.Policy]:
        """
        Creates an iterable of all Policy resources in the collection, but limits the number of
        items returned by each service call by the specified amount.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListAttachedGroupPolicies>`_

        **Request Syntax**
        ::

          policy_iterator = group.attached_policies.page_size(
              count=123
          )
        :type count: integer
        :param count: The number of items returned by each service call

        :rtype: list(:py:class:`iam.Policy`)
        :returns: A list of Policy resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        """
        A generator which yields pages of resource instances after
        doing the appropriate service operation calls and handling
        any pagination on your behalf. Non-paginated calls will
        return a single page of items.

        Page size, item limit, and filter parameters are applied
        if they have previously been set.

            >>> bucket = s3.Bucket('boto3')
            >>> for page in bucket.objects.pages():
            ...     for obj in page:
            ...         print(obj.key)
            'key1'
            'key2'

        :rtype: list(:py:class:`~boto3.resources.base.ServiceResource`)
        :return: List of resource instances
        """


class GroupPoliciesCollection(ResourceCollection):
    """
    A group of resources. See :py:class:`Action`.

    :type name: string
    :param name: The name of the collection
    :type definition: dict
    :param definition: The JSON definition
    :type resource_defs: dict
    :param resource_defs: All resources defined in the service
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.GroupPolicy]:
        """
        Creates an iterable of all GroupPolicy resources in the collection.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListGroupPolicies>`_

        **Request Syntax**
        ::

          group_policy_iterator = group.policies.all()

        :rtype: list(:py:class:`iam.GroupPolicy`)
        :returns: A list of GroupPolicy resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self, Marker: str = None, MaxItems: int = None
    ) -> List[service_resource_scope.GroupPolicy]:
        """
        Creates an iterable of all GroupPolicy resources in the collection filtered by kwargs passed
        to method.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListGroupPolicies>`_

        **Request Syntax**
        ::

          group_policy_iterator = group.policies.filter(
              Marker='string',
              MaxItems=123
          )
        :type Marker: string
        :param Marker:

          Use this parameter only when paginating results and only after you receive a response
          indicating that the results are truncated. Set it to the value of the ``Marker`` element
          in the response that you received to indicate where the next call should start.

        :type MaxItems: integer
        :param MaxItems:

          Use this only when paginating results to indicate the maximum number of items you want in
          the response. If additional items exist beyond the maximum you specify, the
          ``IsTruncated`` response element is ``true`` .

          If you do not include this parameter, the number of items defaults to 100. Note that IAM
          might return fewer results, even when there are more results available. In that case, the
          ``IsTruncated`` response element returns ``true`` , and ``Marker`` contains a value to
          include in the subsequent call that tells the service where to continue from.

        :rtype: list(:py:class:`iam.GroupPolicy`)
        :returns: A list of GroupPolicy resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        """
        Get a resource collection iterator from this manager.

        :rtype: :py:class:`ResourceCollection`
        :return: An iterable representing the collection of resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.GroupPolicy]:
        """
        Creates an iterable up to a specified amount of GroupPolicy resources in the collection.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListGroupPolicies>`_

        **Request Syntax**
        ::

          group_policy_iterator = group.policies.limit(
              count=123
          )
        :type count: integer
        :param count: The limit to the number of resources in the iterable.

        :rtype: list(:py:class:`iam.GroupPolicy`)
        :returns: A list of GroupPolicy resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.GroupPolicy]:
        """
        Creates an iterable of all GroupPolicy resources in the collection, but limits the number of
        items returned by each service call by the specified amount.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListGroupPolicies>`_

        **Request Syntax**
        ::

          group_policy_iterator = group.policies.page_size(
              count=123
          )
        :type count: integer
        :param count: The number of items returned by each service call

        :rtype: list(:py:class:`iam.GroupPolicy`)
        :returns: A list of GroupPolicy resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        """
        A generator which yields pages of resource instances after
        doing the appropriate service operation calls and handling
        any pagination on your behalf. Non-paginated calls will
        return a single page of items.

        Page size, item limit, and filter parameters are applied
        if they have previously been set.

            >>> bucket = s3.Bucket('boto3')
            >>> for page in bucket.objects.pages():
            ...     for obj in page:
            ...         print(obj.key)
            'key1'
            'key2'

        :rtype: list(:py:class:`~boto3.resources.base.ServiceResource`)
        :return: List of resource instances
        """


class GroupUsersCollection(ResourceCollection):
    """
    A group of resources. See :py:class:`Action`.

    :type name: string
    :param name: The name of the collection
    :type definition: dict
    :param definition: The JSON definition
    :type resource_defs: dict
    :param resource_defs: All resources defined in the service
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.User]:
        """
        Creates an iterable of all User resources in the collection.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/GetGroup>`_

        **Request Syntax**
        ::

          user_iterator = group.users.all()

        :rtype: list(:py:class:`iam.User`)
        :returns: A list of User resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(self, Marker: str = None, MaxItems: int = None) -> List[service_resource_scope.User]:
        """
        Creates an iterable of all User resources in the collection filtered by kwargs passed to
        method.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/GetGroup>`_

        **Request Syntax**
        ::

          user_iterator = group.users.filter(
              Marker='string',
              MaxItems=123
          )
        :type Marker: string
        :param Marker:

          Use this parameter only when paginating results and only after you receive a response
          indicating that the results are truncated. Set it to the value of the ``Marker`` element
          in the response that you received to indicate where the next call should start.

        :type MaxItems: integer
        :param MaxItems:

          Use this only when paginating results to indicate the maximum number of items you want in
          the response. If additional items exist beyond the maximum you specify, the
          ``IsTruncated`` response element is ``true`` .

          If you do not include this parameter, the number of items defaults to 100. Note that IAM
          might return fewer results, even when there are more results available. In that case, the
          ``IsTruncated`` response element returns ``true`` , and ``Marker`` contains a value to
          include in the subsequent call that tells the service where to continue from.

        :rtype: list(:py:class:`iam.User`)
        :returns: A list of User resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        """
        Get a resource collection iterator from this manager.

        :rtype: :py:class:`ResourceCollection`
        :return: An iterable representing the collection of resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.User]:
        """
        Creates an iterable up to a specified amount of User resources in the collection.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/GetGroup>`_

        **Request Syntax**
        ::

          user_iterator = group.users.limit(
              count=123
          )
        :type count: integer
        :param count: The limit to the number of resources in the iterable.

        :rtype: list(:py:class:`iam.User`)
        :returns: A list of User resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.User]:
        """
        Creates an iterable of all User resources in the collection, but limits the number of items
        returned by each service call by the specified amount.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/GetGroup>`_

        **Request Syntax**
        ::

          user_iterator = group.users.page_size(
              count=123
          )
        :type count: integer
        :param count: The number of items returned by each service call

        :rtype: list(:py:class:`iam.User`)
        :returns: A list of User resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        """
        A generator which yields pages of resource instances after
        doing the appropriate service operation calls and handling
        any pagination on your behalf. Non-paginated calls will
        return a single page of items.

        Page size, item limit, and filter parameters are applied
        if they have previously been set.

            >>> bucket = s3.Bucket('boto3')
            >>> for page in bucket.objects.pages():
            ...     for obj in page:
            ...         print(obj.key)
            'key1'
            'key2'

        :rtype: list(:py:class:`~boto3.resources.base.ServiceResource`)
        :return: List of resource instances
        """


class PolicyAttachedGroupsCollection(ResourceCollection):
    """
    A group of resources. See :py:class:`Action`.

    :type name: string
    :param name: The name of the collection
    :type definition: dict
    :param definition: The JSON definition
    :type resource_defs: dict
    :param resource_defs: All resources defined in the service
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.Group]:
        """
        Creates an iterable of all Group resources in the collection.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListEntitiesForPolicy>`_

        **Request Syntax**
        ::

          group_iterator = policy.attached_groups.all()

        :rtype: list(:py:class:`iam.Group`)
        :returns: A list of Group resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self,
        PathPrefix: str = None,
        PolicyUsageFilter: Literal["PermissionsPolicy", "PermissionsBoundary"] = None,
        Marker: str = None,
        MaxItems: int = None,
    ) -> List[service_resource_scope.Group]:
        """
        Creates an iterable of all Group resources in the collection filtered by kwargs passed to
        method.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListEntitiesForPolicy>`_

        **Request Syntax**
        ::

          group_iterator = policy.attached_groups.filter(
              PathPrefix='string',
              PolicyUsageFilter='PermissionsPolicy'|'PermissionsBoundary',
              Marker='string',
              MaxItems=123
          )
        :type PathPrefix: string
        :param PathPrefix:

          The path prefix for filtering the results. This parameter is optional. If it is not
          included, it defaults to a slash (/), listing all entities.

          This parameter allows (through its `regex pattern <http://wikipedia.org/wiki/regex>`__ ) a
          string of characters consisting of either a forward slash (/) by itself or a string that
          must begin and end with forward slashes. In addition, it can contain any ASCII character
          from the ! (\\u0021) through the DEL character (\\u007F), including most punctuation
          characters, digits, and upper and lowercased letters.

        :type PolicyUsageFilter: string
        :param PolicyUsageFilter:

          The policy usage method to use for filtering the results.

          To list only permissions policies, set ``PolicyUsageFilter`` to ``PermissionsPolicy`` . To
          list only the policies used to set permissions boundaries, set the value to
          ``PermissionsBoundary`` .

          This parameter is optional. If it is not included, all policies are returned.

        :type Marker: string
        :param Marker:

          Use this parameter only when paginating results and only after you receive a response
          indicating that the results are truncated. Set it to the value of the ``Marker`` element
          in the response that you received to indicate where the next call should start.

        :type MaxItems: integer
        :param MaxItems:

          Use this only when paginating results to indicate the maximum number of items you want in
          the response. If additional items exist beyond the maximum you specify, the
          ``IsTruncated`` response element is ``true`` .

          If you do not include this parameter, the number of items defaults to 100. Note that IAM
          might return fewer results, even when there are more results available. In that case, the
          ``IsTruncated`` response element returns ``true`` , and ``Marker`` contains a value to
          include in the subsequent call that tells the service where to continue from.

        :rtype: list(:py:class:`iam.Group`)
        :returns: A list of Group resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        """
        Get a resource collection iterator from this manager.

        :rtype: :py:class:`ResourceCollection`
        :return: An iterable representing the collection of resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.Group]:
        """
        Creates an iterable up to a specified amount of Group resources in the collection.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListEntitiesForPolicy>`_

        **Request Syntax**
        ::

          group_iterator = policy.attached_groups.limit(
              count=123
          )
        :type count: integer
        :param count: The limit to the number of resources in the iterable.

        :rtype: list(:py:class:`iam.Group`)
        :returns: A list of Group resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.Group]:
        """
        Creates an iterable of all Group resources in the collection, but limits the number of items
        returned by each service call by the specified amount.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListEntitiesForPolicy>`_

        **Request Syntax**
        ::

          group_iterator = policy.attached_groups.page_size(
              count=123
          )
        :type count: integer
        :param count: The number of items returned by each service call

        :rtype: list(:py:class:`iam.Group`)
        :returns: A list of Group resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        """
        A generator which yields pages of resource instances after
        doing the appropriate service operation calls and handling
        any pagination on your behalf. Non-paginated calls will
        return a single page of items.

        Page size, item limit, and filter parameters are applied
        if they have previously been set.

            >>> bucket = s3.Bucket('boto3')
            >>> for page in bucket.objects.pages():
            ...     for obj in page:
            ...         print(obj.key)
            'key1'
            'key2'

        :rtype: list(:py:class:`~boto3.resources.base.ServiceResource`)
        :return: List of resource instances
        """


class PolicyAttachedRolesCollection(ResourceCollection):
    """
    A group of resources. See :py:class:`Action`.

    :type name: string
    :param name: The name of the collection
    :type definition: dict
    :param definition: The JSON definition
    :type resource_defs: dict
    :param resource_defs: All resources defined in the service
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.Role]:
        """
        Creates an iterable of all Role resources in the collection.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListEntitiesForPolicy>`_

        **Request Syntax**
        ::

          role_iterator = policy.attached_roles.all()

        :rtype: list(:py:class:`iam.Role`)
        :returns: A list of Role resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self,
        PathPrefix: str = None,
        PolicyUsageFilter: Literal["PermissionsPolicy", "PermissionsBoundary"] = None,
        Marker: str = None,
        MaxItems: int = None,
    ) -> List[service_resource_scope.Role]:
        """
        Creates an iterable of all Role resources in the collection filtered by kwargs passed to
        method.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListEntitiesForPolicy>`_

        **Request Syntax**
        ::

          role_iterator = policy.attached_roles.filter(
              PathPrefix='string',
              PolicyUsageFilter='PermissionsPolicy'|'PermissionsBoundary',
              Marker='string',
              MaxItems=123
          )
        :type PathPrefix: string
        :param PathPrefix:

          The path prefix for filtering the results. This parameter is optional. If it is not
          included, it defaults to a slash (/), listing all entities.

          This parameter allows (through its `regex pattern <http://wikipedia.org/wiki/regex>`__ ) a
          string of characters consisting of either a forward slash (/) by itself or a string that
          must begin and end with forward slashes. In addition, it can contain any ASCII character
          from the ! (\\u0021) through the DEL character (\\u007F), including most punctuation
          characters, digits, and upper and lowercased letters.

        :type PolicyUsageFilter: string
        :param PolicyUsageFilter:

          The policy usage method to use for filtering the results.

          To list only permissions policies, set ``PolicyUsageFilter`` to ``PermissionsPolicy`` . To
          list only the policies used to set permissions boundaries, set the value to
          ``PermissionsBoundary`` .

          This parameter is optional. If it is not included, all policies are returned.

        :type Marker: string
        :param Marker:

          Use this parameter only when paginating results and only after you receive a response
          indicating that the results are truncated. Set it to the value of the ``Marker`` element
          in the response that you received to indicate where the next call should start.

        :type MaxItems: integer
        :param MaxItems:

          Use this only when paginating results to indicate the maximum number of items you want in
          the response. If additional items exist beyond the maximum you specify, the
          ``IsTruncated`` response element is ``true`` .

          If you do not include this parameter, the number of items defaults to 100. Note that IAM
          might return fewer results, even when there are more results available. In that case, the
          ``IsTruncated`` response element returns ``true`` , and ``Marker`` contains a value to
          include in the subsequent call that tells the service where to continue from.

        :rtype: list(:py:class:`iam.Role`)
        :returns: A list of Role resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        """
        Get a resource collection iterator from this manager.

        :rtype: :py:class:`ResourceCollection`
        :return: An iterable representing the collection of resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.Role]:
        """
        Creates an iterable up to a specified amount of Role resources in the collection.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListEntitiesForPolicy>`_

        **Request Syntax**
        ::

          role_iterator = policy.attached_roles.limit(
              count=123
          )
        :type count: integer
        :param count: The limit to the number of resources in the iterable.

        :rtype: list(:py:class:`iam.Role`)
        :returns: A list of Role resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.Role]:
        """
        Creates an iterable of all Role resources in the collection, but limits the number of items
        returned by each service call by the specified amount.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListEntitiesForPolicy>`_

        **Request Syntax**
        ::

          role_iterator = policy.attached_roles.page_size(
              count=123
          )
        :type count: integer
        :param count: The number of items returned by each service call

        :rtype: list(:py:class:`iam.Role`)
        :returns: A list of Role resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        """
        A generator which yields pages of resource instances after
        doing the appropriate service operation calls and handling
        any pagination on your behalf. Non-paginated calls will
        return a single page of items.

        Page size, item limit, and filter parameters are applied
        if they have previously been set.

            >>> bucket = s3.Bucket('boto3')
            >>> for page in bucket.objects.pages():
            ...     for obj in page:
            ...         print(obj.key)
            'key1'
            'key2'

        :rtype: list(:py:class:`~boto3.resources.base.ServiceResource`)
        :return: List of resource instances
        """


class PolicyAttachedUsersCollection(ResourceCollection):
    """
    A group of resources. See :py:class:`Action`.

    :type name: string
    :param name: The name of the collection
    :type definition: dict
    :param definition: The JSON definition
    :type resource_defs: dict
    :param resource_defs: All resources defined in the service
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.User]:
        """
        Creates an iterable of all User resources in the collection.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListEntitiesForPolicy>`_

        **Request Syntax**
        ::

          user_iterator = policy.attached_users.all()

        :rtype: list(:py:class:`iam.User`)
        :returns: A list of User resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self,
        PathPrefix: str = None,
        PolicyUsageFilter: Literal["PermissionsPolicy", "PermissionsBoundary"] = None,
        Marker: str = None,
        MaxItems: int = None,
    ) -> List[service_resource_scope.User]:
        """
        Creates an iterable of all User resources in the collection filtered by kwargs passed to
        method.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListEntitiesForPolicy>`_

        **Request Syntax**
        ::

          user_iterator = policy.attached_users.filter(
              PathPrefix='string',
              PolicyUsageFilter='PermissionsPolicy'|'PermissionsBoundary',
              Marker='string',
              MaxItems=123
          )
        :type PathPrefix: string
        :param PathPrefix:

          The path prefix for filtering the results. This parameter is optional. If it is not
          included, it defaults to a slash (/), listing all entities.

          This parameter allows (through its `regex pattern <http://wikipedia.org/wiki/regex>`__ ) a
          string of characters consisting of either a forward slash (/) by itself or a string that
          must begin and end with forward slashes. In addition, it can contain any ASCII character
          from the ! (\\u0021) through the DEL character (\\u007F), including most punctuation
          characters, digits, and upper and lowercased letters.

        :type PolicyUsageFilter: string
        :param PolicyUsageFilter:

          The policy usage method to use for filtering the results.

          To list only permissions policies, set ``PolicyUsageFilter`` to ``PermissionsPolicy`` . To
          list only the policies used to set permissions boundaries, set the value to
          ``PermissionsBoundary`` .

          This parameter is optional. If it is not included, all policies are returned.

        :type Marker: string
        :param Marker:

          Use this parameter only when paginating results and only after you receive a response
          indicating that the results are truncated. Set it to the value of the ``Marker`` element
          in the response that you received to indicate where the next call should start.

        :type MaxItems: integer
        :param MaxItems:

          Use this only when paginating results to indicate the maximum number of items you want in
          the response. If additional items exist beyond the maximum you specify, the
          ``IsTruncated`` response element is ``true`` .

          If you do not include this parameter, the number of items defaults to 100. Note that IAM
          might return fewer results, even when there are more results available. In that case, the
          ``IsTruncated`` response element returns ``true`` , and ``Marker`` contains a value to
          include in the subsequent call that tells the service where to continue from.

        :rtype: list(:py:class:`iam.User`)
        :returns: A list of User resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        """
        Get a resource collection iterator from this manager.

        :rtype: :py:class:`ResourceCollection`
        :return: An iterable representing the collection of resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.User]:
        """
        Creates an iterable up to a specified amount of User resources in the collection.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListEntitiesForPolicy>`_

        **Request Syntax**
        ::

          user_iterator = policy.attached_users.limit(
              count=123
          )
        :type count: integer
        :param count: The limit to the number of resources in the iterable.

        :rtype: list(:py:class:`iam.User`)
        :returns: A list of User resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.User]:
        """
        Creates an iterable of all User resources in the collection, but limits the number of items
        returned by each service call by the specified amount.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListEntitiesForPolicy>`_

        **Request Syntax**
        ::

          user_iterator = policy.attached_users.page_size(
              count=123
          )
        :type count: integer
        :param count: The number of items returned by each service call

        :rtype: list(:py:class:`iam.User`)
        :returns: A list of User resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        """
        A generator which yields pages of resource instances after
        doing the appropriate service operation calls and handling
        any pagination on your behalf. Non-paginated calls will
        return a single page of items.

        Page size, item limit, and filter parameters are applied
        if they have previously been set.

            >>> bucket = s3.Bucket('boto3')
            >>> for page in bucket.objects.pages():
            ...     for obj in page:
            ...         print(obj.key)
            'key1'
            'key2'

        :rtype: list(:py:class:`~boto3.resources.base.ServiceResource`)
        :return: List of resource instances
        """


class PolicyVersionsCollection(ResourceCollection):
    """
    A group of resources. See :py:class:`Action`.

    :type name: string
    :param name: The name of the collection
    :type definition: dict
    :param definition: The JSON definition
    :type resource_defs: dict
    :param resource_defs: All resources defined in the service
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.PolicyVersion]:
        """
        Creates an iterable of all PolicyVersion resources in the collection.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListPolicyVersions>`_

        **Request Syntax**
        ::

          policy_version_iterator = policy.versions.all()

        :rtype: list(:py:class:`iam.PolicyVersion`)
        :returns: A list of PolicyVersion resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self, Marker: str = None, MaxItems: int = None
    ) -> List[service_resource_scope.PolicyVersion]:
        """
        Creates an iterable of all PolicyVersion resources in the collection filtered by kwargs
        passed to method.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListPolicyVersions>`_

        **Request Syntax**
        ::

          policy_version_iterator = policy.versions.filter(
              Marker='string',
              MaxItems=123
          )
        :type Marker: string
        :param Marker:

          Use this parameter only when paginating results and only after you receive a response
          indicating that the results are truncated. Set it to the value of the ``Marker`` element
          in the response that you received to indicate where the next call should start.

        :type MaxItems: integer
        :param MaxItems:

          Use this only when paginating results to indicate the maximum number of items you want in
          the response. If additional items exist beyond the maximum you specify, the
          ``IsTruncated`` response element is ``true`` .

          If you do not include this parameter, the number of items defaults to 100. Note that IAM
          might return fewer results, even when there are more results available. In that case, the
          ``IsTruncated`` response element returns ``true`` , and ``Marker`` contains a value to
          include in the subsequent call that tells the service where to continue from.

        :rtype: list(:py:class:`iam.PolicyVersion`)
        :returns: A list of PolicyVersion resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        """
        Get a resource collection iterator from this manager.

        :rtype: :py:class:`ResourceCollection`
        :return: An iterable representing the collection of resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.PolicyVersion]:
        """
        Creates an iterable up to a specified amount of PolicyVersion resources in the collection.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListPolicyVersions>`_

        **Request Syntax**
        ::

          policy_version_iterator = policy.versions.limit(
              count=123
          )
        :type count: integer
        :param count: The limit to the number of resources in the iterable.

        :rtype: list(:py:class:`iam.PolicyVersion`)
        :returns: A list of PolicyVersion resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.PolicyVersion]:
        """
        Creates an iterable of all PolicyVersion resources in the collection, but limits the number
        of items returned by each service call by the specified amount.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListPolicyVersions>`_

        **Request Syntax**
        ::

          policy_version_iterator = policy.versions.page_size(
              count=123
          )
        :type count: integer
        :param count: The number of items returned by each service call

        :rtype: list(:py:class:`iam.PolicyVersion`)
        :returns: A list of PolicyVersion resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        """
        A generator which yields pages of resource instances after
        doing the appropriate service operation calls and handling
        any pagination on your behalf. Non-paginated calls will
        return a single page of items.

        Page size, item limit, and filter parameters are applied
        if they have previously been set.

            >>> bucket = s3.Bucket('boto3')
            >>> for page in bucket.objects.pages():
            ...     for obj in page:
            ...         print(obj.key)
            'key1'
            'key2'

        :rtype: list(:py:class:`~boto3.resources.base.ServiceResource`)
        :return: List of resource instances
        """


class RoleAttachedPoliciesCollection(ResourceCollection):
    """
    A group of resources. See :py:class:`Action`.

    :type name: string
    :param name: The name of the collection
    :type definition: dict
    :param definition: The JSON definition
    :type resource_defs: dict
    :param resource_defs: All resources defined in the service
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.Policy]:
        """
        Creates an iterable of all Policy resources in the collection.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListAttachedRolePolicies>`_

        **Request Syntax**
        ::

          policy_iterator = role.attached_policies.all()

        :rtype: list(:py:class:`iam.Policy`)
        :returns: A list of Policy resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self, PathPrefix: str = None, Marker: str = None, MaxItems: int = None
    ) -> List[service_resource_scope.Policy]:
        """
        Creates an iterable of all Policy resources in the collection filtered by kwargs passed to
        method.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListAttachedRolePolicies>`_

        **Request Syntax**
        ::

          policy_iterator = role.attached_policies.filter(
              PathPrefix='string',
              Marker='string',
              MaxItems=123
          )
        :type PathPrefix: string
        :param PathPrefix:

          The path prefix for filtering the results. This parameter is optional. If it is not
          included, it defaults to a slash (/), listing all policies.

          This parameter allows (through its `regex pattern <http://wikipedia.org/wiki/regex>`__ ) a
          string of characters consisting of either a forward slash (/) by itself or a string that
          must begin and end with forward slashes. In addition, it can contain any ASCII character
          from the ! (\\u0021) through the DEL character (\\u007F), including most punctuation
          characters, digits, and upper and lowercased letters.

        :type Marker: string
        :param Marker:

          Use this parameter only when paginating results and only after you receive a response
          indicating that the results are truncated. Set it to the value of the ``Marker`` element
          in the response that you received to indicate where the next call should start.

        :type MaxItems: integer
        :param MaxItems:

          Use this only when paginating results to indicate the maximum number of items you want in
          the response. If additional items exist beyond the maximum you specify, the
          ``IsTruncated`` response element is ``true`` .

          If you do not include this parameter, the number of items defaults to 100. Note that IAM
          might return fewer results, even when there are more results available. In that case, the
          ``IsTruncated`` response element returns ``true`` , and ``Marker`` contains a value to
          include in the subsequent call that tells the service where to continue from.

        :rtype: list(:py:class:`iam.Policy`)
        :returns: A list of Policy resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        """
        Get a resource collection iterator from this manager.

        :rtype: :py:class:`ResourceCollection`
        :return: An iterable representing the collection of resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.Policy]:
        """
        Creates an iterable up to a specified amount of Policy resources in the collection.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListAttachedRolePolicies>`_

        **Request Syntax**
        ::

          policy_iterator = role.attached_policies.limit(
              count=123
          )
        :type count: integer
        :param count: The limit to the number of resources in the iterable.

        :rtype: list(:py:class:`iam.Policy`)
        :returns: A list of Policy resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.Policy]:
        """
        Creates an iterable of all Policy resources in the collection, but limits the number of
        items returned by each service call by the specified amount.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListAttachedRolePolicies>`_

        **Request Syntax**
        ::

          policy_iterator = role.attached_policies.page_size(
              count=123
          )
        :type count: integer
        :param count: The number of items returned by each service call

        :rtype: list(:py:class:`iam.Policy`)
        :returns: A list of Policy resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        """
        A generator which yields pages of resource instances after
        doing the appropriate service operation calls and handling
        any pagination on your behalf. Non-paginated calls will
        return a single page of items.

        Page size, item limit, and filter parameters are applied
        if they have previously been set.

            >>> bucket = s3.Bucket('boto3')
            >>> for page in bucket.objects.pages():
            ...     for obj in page:
            ...         print(obj.key)
            'key1'
            'key2'

        :rtype: list(:py:class:`~boto3.resources.base.ServiceResource`)
        :return: List of resource instances
        """


class RoleInstanceProfilesCollection(ResourceCollection):
    """
    A group of resources. See :py:class:`Action`.

    :type name: string
    :param name: The name of the collection
    :type definition: dict
    :param definition: The JSON definition
    :type resource_defs: dict
    :param resource_defs: All resources defined in the service
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.InstanceProfile]:
        """
        Creates an iterable of all InstanceProfile resources in the collection.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListInstanceProfilesForRole>`_

        **Request Syntax**
        ::

          instance_profile_iterator = role.instance_profiles.all()

        :rtype: list(:py:class:`iam.InstanceProfile`)
        :returns: A list of InstanceProfile resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self, Marker: str = None, MaxItems: int = None
    ) -> List[service_resource_scope.InstanceProfile]:
        """
        Creates an iterable of all InstanceProfile resources in the collection filtered by kwargs
        passed to method.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListInstanceProfilesForRole>`_

        **Request Syntax**
        ::

          instance_profile_iterator = role.instance_profiles.filter(
              Marker='string',
              MaxItems=123
          )
        :type Marker: string
        :param Marker:

          Use this parameter only when paginating results and only after you receive a response
          indicating that the results are truncated. Set it to the value of the ``Marker`` element
          in the response that you received to indicate where the next call should start.

        :type MaxItems: integer
        :param MaxItems:

          Use this only when paginating results to indicate the maximum number of items you want in
          the response. If additional items exist beyond the maximum you specify, the
          ``IsTruncated`` response element is ``true`` .

          If you do not include this parameter, the number of items defaults to 100. Note that IAM
          might return fewer results, even when there are more results available. In that case, the
          ``IsTruncated`` response element returns ``true`` , and ``Marker`` contains a value to
          include in the subsequent call that tells the service where to continue from.

        :rtype: list(:py:class:`iam.InstanceProfile`)
        :returns: A list of InstanceProfile resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        """
        Get a resource collection iterator from this manager.

        :rtype: :py:class:`ResourceCollection`
        :return: An iterable representing the collection of resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.InstanceProfile]:
        """
        Creates an iterable up to a specified amount of InstanceProfile resources in the collection.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListInstanceProfilesForRole>`_

        **Request Syntax**
        ::

          instance_profile_iterator = role.instance_profiles.limit(
              count=123
          )
        :type count: integer
        :param count: The limit to the number of resources in the iterable.

        :rtype: list(:py:class:`iam.InstanceProfile`)
        :returns: A list of InstanceProfile resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.InstanceProfile]:
        """
        Creates an iterable of all InstanceProfile resources in the collection, but limits the
        number of items returned by each service call by the specified amount.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListInstanceProfilesForRole>`_

        **Request Syntax**
        ::

          instance_profile_iterator = role.instance_profiles.page_size(
              count=123
          )
        :type count: integer
        :param count: The number of items returned by each service call

        :rtype: list(:py:class:`iam.InstanceProfile`)
        :returns: A list of InstanceProfile resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        """
        A generator which yields pages of resource instances after
        doing the appropriate service operation calls and handling
        any pagination on your behalf. Non-paginated calls will
        return a single page of items.

        Page size, item limit, and filter parameters are applied
        if they have previously been set.

            >>> bucket = s3.Bucket('boto3')
            >>> for page in bucket.objects.pages():
            ...     for obj in page:
            ...         print(obj.key)
            'key1'
            'key2'

        :rtype: list(:py:class:`~boto3.resources.base.ServiceResource`)
        :return: List of resource instances
        """


class RolePoliciesCollection(ResourceCollection):
    """
    A group of resources. See :py:class:`Action`.

    :type name: string
    :param name: The name of the collection
    :type definition: dict
    :param definition: The JSON definition
    :type resource_defs: dict
    :param resource_defs: All resources defined in the service
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.RolePolicy]:
        """
        Creates an iterable of all RolePolicy resources in the collection.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListRolePolicies>`_

        **Request Syntax**
        ::

          role_policy_iterator = role.policies.all()

        :rtype: list(:py:class:`iam.RolePolicy`)
        :returns: A list of RolePolicy resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self, Marker: str = None, MaxItems: int = None
    ) -> List[service_resource_scope.RolePolicy]:
        """
        Creates an iterable of all RolePolicy resources in the collection filtered by kwargs passed
        to method.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListRolePolicies>`_

        **Request Syntax**
        ::

          role_policy_iterator = role.policies.filter(
              Marker='string',
              MaxItems=123
          )
        :type Marker: string
        :param Marker:

          Use this parameter only when paginating results and only after you receive a response
          indicating that the results are truncated. Set it to the value of the ``Marker`` element
          in the response that you received to indicate where the next call should start.

        :type MaxItems: integer
        :param MaxItems:

          Use this only when paginating results to indicate the maximum number of items you want in
          the response. If additional items exist beyond the maximum you specify, the
          ``IsTruncated`` response element is ``true`` .

          If you do not include this parameter, the number of items defaults to 100. Note that IAM
          might return fewer results, even when there are more results available. In that case, the
          ``IsTruncated`` response element returns ``true`` , and ``Marker`` contains a value to
          include in the subsequent call that tells the service where to continue from.

        :rtype: list(:py:class:`iam.RolePolicy`)
        :returns: A list of RolePolicy resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        """
        Get a resource collection iterator from this manager.

        :rtype: :py:class:`ResourceCollection`
        :return: An iterable representing the collection of resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.RolePolicy]:
        """
        Creates an iterable up to a specified amount of RolePolicy resources in the collection.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListRolePolicies>`_

        **Request Syntax**
        ::

          role_policy_iterator = role.policies.limit(
              count=123
          )
        :type count: integer
        :param count: The limit to the number of resources in the iterable.

        :rtype: list(:py:class:`iam.RolePolicy`)
        :returns: A list of RolePolicy resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.RolePolicy]:
        """
        Creates an iterable of all RolePolicy resources in the collection, but limits the number of
        items returned by each service call by the specified amount.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListRolePolicies>`_

        **Request Syntax**
        ::

          role_policy_iterator = role.policies.page_size(
              count=123
          )
        :type count: integer
        :param count: The number of items returned by each service call

        :rtype: list(:py:class:`iam.RolePolicy`)
        :returns: A list of RolePolicy resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        """
        A generator which yields pages of resource instances after
        doing the appropriate service operation calls and handling
        any pagination on your behalf. Non-paginated calls will
        return a single page of items.

        Page size, item limit, and filter parameters are applied
        if they have previously been set.

            >>> bucket = s3.Bucket('boto3')
            >>> for page in bucket.objects.pages():
            ...     for obj in page:
            ...         print(obj.key)
            'key1'
            'key2'

        :rtype: list(:py:class:`~boto3.resources.base.ServiceResource`)
        :return: List of resource instances
        """


class UserAccessKeysCollection(ResourceCollection):
    """
    A group of resources. See :py:class:`Action`.

    :type name: string
    :param name: The name of the collection
    :type definition: dict
    :param definition: The JSON definition
    :type resource_defs: dict
    :param resource_defs: All resources defined in the service
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.AccessKey]:
        """
        Creates an iterable of all AccessKey resources in the collection.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListAccessKeys>`_

        **Request Syntax**
        ::

          access_key_iterator = user.access_keys.all()

        :rtype: list(:py:class:`iam.AccessKey`)
        :returns: A list of AccessKey resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self, Marker: str = None, MaxItems: int = None
    ) -> List[service_resource_scope.AccessKey]:
        """
        Creates an iterable of all AccessKey resources in the collection filtered by kwargs passed
        to method.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListAccessKeys>`_

        **Request Syntax**
        ::

          access_key_iterator = user.access_keys.filter(
              Marker='string',
              MaxItems=123
          )
        :type Marker: string
        :param Marker:

          Use this parameter only when paginating results and only after you receive a response
          indicating that the results are truncated. Set it to the value of the ``Marker`` element
          in the response that you received to indicate where the next call should start.

        :type MaxItems: integer
        :param MaxItems:

          Use this only when paginating results to indicate the maximum number of items you want in
          the response. If additional items exist beyond the maximum you specify, the
          ``IsTruncated`` response element is ``true`` .

          If you do not include this parameter, the number of items defaults to 100. Note that IAM
          might return fewer results, even when there are more results available. In that case, the
          ``IsTruncated`` response element returns ``true`` , and ``Marker`` contains a value to
          include in the subsequent call that tells the service where to continue from.

        :rtype: list(:py:class:`iam.AccessKey`)
        :returns: A list of AccessKey resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        """
        Get a resource collection iterator from this manager.

        :rtype: :py:class:`ResourceCollection`
        :return: An iterable representing the collection of resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.AccessKey]:
        """
        Creates an iterable up to a specified amount of AccessKey resources in the collection.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListAccessKeys>`_

        **Request Syntax**
        ::

          access_key_iterator = user.access_keys.limit(
              count=123
          )
        :type count: integer
        :param count: The limit to the number of resources in the iterable.

        :rtype: list(:py:class:`iam.AccessKey`)
        :returns: A list of AccessKey resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.AccessKey]:
        """
        Creates an iterable of all AccessKey resources in the collection, but limits the number of
        items returned by each service call by the specified amount.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListAccessKeys>`_

        **Request Syntax**
        ::

          access_key_iterator = user.access_keys.page_size(
              count=123
          )
        :type count: integer
        :param count: The number of items returned by each service call

        :rtype: list(:py:class:`iam.AccessKey`)
        :returns: A list of AccessKey resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        """
        A generator which yields pages of resource instances after
        doing the appropriate service operation calls and handling
        any pagination on your behalf. Non-paginated calls will
        return a single page of items.

        Page size, item limit, and filter parameters are applied
        if they have previously been set.

            >>> bucket = s3.Bucket('boto3')
            >>> for page in bucket.objects.pages():
            ...     for obj in page:
            ...         print(obj.key)
            'key1'
            'key2'

        :rtype: list(:py:class:`~boto3.resources.base.ServiceResource`)
        :return: List of resource instances
        """


class UserAttachedPoliciesCollection(ResourceCollection):
    """
    A group of resources. See :py:class:`Action`.

    :type name: string
    :param name: The name of the collection
    :type definition: dict
    :param definition: The JSON definition
    :type resource_defs: dict
    :param resource_defs: All resources defined in the service
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.Policy]:
        """
        Creates an iterable of all Policy resources in the collection.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListAttachedUserPolicies>`_

        **Request Syntax**
        ::

          policy_iterator = user.attached_policies.all()

        :rtype: list(:py:class:`iam.Policy`)
        :returns: A list of Policy resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self, PathPrefix: str = None, Marker: str = None, MaxItems: int = None
    ) -> List[service_resource_scope.Policy]:
        """
        Creates an iterable of all Policy resources in the collection filtered by kwargs passed to
        method.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListAttachedUserPolicies>`_

        **Request Syntax**
        ::

          policy_iterator = user.attached_policies.filter(
              PathPrefix='string',
              Marker='string',
              MaxItems=123
          )
        :type PathPrefix: string
        :param PathPrefix:

          The path prefix for filtering the results. This parameter is optional. If it is not
          included, it defaults to a slash (/), listing all policies.

          This parameter allows (through its `regex pattern <http://wikipedia.org/wiki/regex>`__ ) a
          string of characters consisting of either a forward slash (/) by itself or a string that
          must begin and end with forward slashes. In addition, it can contain any ASCII character
          from the ! (\\u0021) through the DEL character (\\u007F), including most punctuation
          characters, digits, and upper and lowercased letters.

        :type Marker: string
        :param Marker:

          Use this parameter only when paginating results and only after you receive a response
          indicating that the results are truncated. Set it to the value of the ``Marker`` element
          in the response that you received to indicate where the next call should start.

        :type MaxItems: integer
        :param MaxItems:

          Use this only when paginating results to indicate the maximum number of items you want in
          the response. If additional items exist beyond the maximum you specify, the
          ``IsTruncated`` response element is ``true`` .

          If you do not include this parameter, the number of items defaults to 100. Note that IAM
          might return fewer results, even when there are more results available. In that case, the
          ``IsTruncated`` response element returns ``true`` , and ``Marker`` contains a value to
          include in the subsequent call that tells the service where to continue from.

        :rtype: list(:py:class:`iam.Policy`)
        :returns: A list of Policy resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        """
        Get a resource collection iterator from this manager.

        :rtype: :py:class:`ResourceCollection`
        :return: An iterable representing the collection of resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.Policy]:
        """
        Creates an iterable up to a specified amount of Policy resources in the collection.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListAttachedUserPolicies>`_

        **Request Syntax**
        ::

          policy_iterator = user.attached_policies.limit(
              count=123
          )
        :type count: integer
        :param count: The limit to the number of resources in the iterable.

        :rtype: list(:py:class:`iam.Policy`)
        :returns: A list of Policy resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.Policy]:
        """
        Creates an iterable of all Policy resources in the collection, but limits the number of
        items returned by each service call by the specified amount.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListAttachedUserPolicies>`_

        **Request Syntax**
        ::

          policy_iterator = user.attached_policies.page_size(
              count=123
          )
        :type count: integer
        :param count: The number of items returned by each service call

        :rtype: list(:py:class:`iam.Policy`)
        :returns: A list of Policy resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        """
        A generator which yields pages of resource instances after
        doing the appropriate service operation calls and handling
        any pagination on your behalf. Non-paginated calls will
        return a single page of items.

        Page size, item limit, and filter parameters are applied
        if they have previously been set.

            >>> bucket = s3.Bucket('boto3')
            >>> for page in bucket.objects.pages():
            ...     for obj in page:
            ...         print(obj.key)
            'key1'
            'key2'

        :rtype: list(:py:class:`~boto3.resources.base.ServiceResource`)
        :return: List of resource instances
        """


class UserGroupsCollection(ResourceCollection):
    """
    A group of resources. See :py:class:`Action`.

    :type name: string
    :param name: The name of the collection
    :type definition: dict
    :param definition: The JSON definition
    :type resource_defs: dict
    :param resource_defs: All resources defined in the service
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.Group]:
        """
        Creates an iterable of all Group resources in the collection.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListGroupsForUser>`_

        **Request Syntax**
        ::

          group_iterator = user.groups.all()

        :rtype: list(:py:class:`iam.Group`)
        :returns: A list of Group resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self, Marker: str = None, MaxItems: int = None
    ) -> List[service_resource_scope.Group]:
        """
        Creates an iterable of all Group resources in the collection filtered by kwargs passed to
        method.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListGroupsForUser>`_

        **Request Syntax**
        ::

          group_iterator = user.groups.filter(
              Marker='string',
              MaxItems=123
          )
        :type Marker: string
        :param Marker:

          Use this parameter only when paginating results and only after you receive a response
          indicating that the results are truncated. Set it to the value of the ``Marker`` element
          in the response that you received to indicate where the next call should start.

        :type MaxItems: integer
        :param MaxItems:

          Use this only when paginating results to indicate the maximum number of items you want in
          the response. If additional items exist beyond the maximum you specify, the
          ``IsTruncated`` response element is ``true`` .

          If you do not include this parameter, the number of items defaults to 100. Note that IAM
          might return fewer results, even when there are more results available. In that case, the
          ``IsTruncated`` response element returns ``true`` , and ``Marker`` contains a value to
          include in the subsequent call that tells the service where to continue from.

        :rtype: list(:py:class:`iam.Group`)
        :returns: A list of Group resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        """
        Get a resource collection iterator from this manager.

        :rtype: :py:class:`ResourceCollection`
        :return: An iterable representing the collection of resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.Group]:
        """
        Creates an iterable up to a specified amount of Group resources in the collection.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListGroupsForUser>`_

        **Request Syntax**
        ::

          group_iterator = user.groups.limit(
              count=123
          )
        :type count: integer
        :param count: The limit to the number of resources in the iterable.

        :rtype: list(:py:class:`iam.Group`)
        :returns: A list of Group resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.Group]:
        """
        Creates an iterable of all Group resources in the collection, but limits the number of items
        returned by each service call by the specified amount.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListGroupsForUser>`_

        **Request Syntax**
        ::

          group_iterator = user.groups.page_size(
              count=123
          )
        :type count: integer
        :param count: The number of items returned by each service call

        :rtype: list(:py:class:`iam.Group`)
        :returns: A list of Group resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        """
        A generator which yields pages of resource instances after
        doing the appropriate service operation calls and handling
        any pagination on your behalf. Non-paginated calls will
        return a single page of items.

        Page size, item limit, and filter parameters are applied
        if they have previously been set.

            >>> bucket = s3.Bucket('boto3')
            >>> for page in bucket.objects.pages():
            ...     for obj in page:
            ...         print(obj.key)
            'key1'
            'key2'

        :rtype: list(:py:class:`~boto3.resources.base.ServiceResource`)
        :return: List of resource instances
        """


class UserMfaDevicesCollection(ResourceCollection):
    """
    A group of resources. See :py:class:`Action`.

    :type name: string
    :param name: The name of the collection
    :type definition: dict
    :param definition: The JSON definition
    :type resource_defs: dict
    :param resource_defs: All resources defined in the service
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.MfaDevice]:
        """
        Creates an iterable of all MfaDevice resources in the collection.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListMFADevices>`_

        **Request Syntax**
        ::

          mfa_device_iterator = user.mfa_devices.all()

        :rtype: list(:py:class:`iam.MfaDevice`)
        :returns: A list of MfaDevice resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self, Marker: str = None, MaxItems: int = None
    ) -> List[service_resource_scope.MfaDevice]:
        """
        Creates an iterable of all MfaDevice resources in the collection filtered by kwargs passed
        to method.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListMFADevices>`_

        **Request Syntax**
        ::

          mfa_device_iterator = user.mfa_devices.filter(
              Marker='string',
              MaxItems=123
          )
        :type Marker: string
        :param Marker:

          Use this parameter only when paginating results and only after you receive a response
          indicating that the results are truncated. Set it to the value of the ``Marker`` element
          in the response that you received to indicate where the next call should start.

        :type MaxItems: integer
        :param MaxItems:

          Use this only when paginating results to indicate the maximum number of items you want in
          the response. If additional items exist beyond the maximum you specify, the
          ``IsTruncated`` response element is ``true`` .

          If you do not include this parameter, the number of items defaults to 100. Note that IAM
          might return fewer results, even when there are more results available. In that case, the
          ``IsTruncated`` response element returns ``true`` , and ``Marker`` contains a value to
          include in the subsequent call that tells the service where to continue from.

        :rtype: list(:py:class:`iam.MfaDevice`)
        :returns: A list of MfaDevice resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        """
        Get a resource collection iterator from this manager.

        :rtype: :py:class:`ResourceCollection`
        :return: An iterable representing the collection of resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.MfaDevice]:
        """
        Creates an iterable up to a specified amount of MfaDevice resources in the collection.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListMFADevices>`_

        **Request Syntax**
        ::

          mfa_device_iterator = user.mfa_devices.limit(
              count=123
          )
        :type count: integer
        :param count: The limit to the number of resources in the iterable.

        :rtype: list(:py:class:`iam.MfaDevice`)
        :returns: A list of MfaDevice resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.MfaDevice]:
        """
        Creates an iterable of all MfaDevice resources in the collection, but limits the number of
        items returned by each service call by the specified amount.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListMFADevices>`_

        **Request Syntax**
        ::

          mfa_device_iterator = user.mfa_devices.page_size(
              count=123
          )
        :type count: integer
        :param count: The number of items returned by each service call

        :rtype: list(:py:class:`iam.MfaDevice`)
        :returns: A list of MfaDevice resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        """
        A generator which yields pages of resource instances after
        doing the appropriate service operation calls and handling
        any pagination on your behalf. Non-paginated calls will
        return a single page of items.

        Page size, item limit, and filter parameters are applied
        if they have previously been set.

            >>> bucket = s3.Bucket('boto3')
            >>> for page in bucket.objects.pages():
            ...     for obj in page:
            ...         print(obj.key)
            'key1'
            'key2'

        :rtype: list(:py:class:`~boto3.resources.base.ServiceResource`)
        :return: List of resource instances
        """


class UserPoliciesCollection(ResourceCollection):
    """
    A group of resources. See :py:class:`Action`.

    :type name: string
    :param name: The name of the collection
    :type definition: dict
    :param definition: The JSON definition
    :type resource_defs: dict
    :param resource_defs: All resources defined in the service
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.UserPolicy]:
        """
        Creates an iterable of all UserPolicy resources in the collection.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListUserPolicies>`_

        **Request Syntax**
        ::

          user_policy_iterator = user.policies.all()

        :rtype: list(:py:class:`iam.UserPolicy`)
        :returns: A list of UserPolicy resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self, Marker: str = None, MaxItems: int = None
    ) -> List[service_resource_scope.UserPolicy]:
        """
        Creates an iterable of all UserPolicy resources in the collection filtered by kwargs passed
        to method.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListUserPolicies>`_

        **Request Syntax**
        ::

          user_policy_iterator = user.policies.filter(
              Marker='string',
              MaxItems=123
          )
        :type Marker: string
        :param Marker:

          Use this parameter only when paginating results and only after you receive a response
          indicating that the results are truncated. Set it to the value of the ``Marker`` element
          in the response that you received to indicate where the next call should start.

        :type MaxItems: integer
        :param MaxItems:

          Use this only when paginating results to indicate the maximum number of items you want in
          the response. If additional items exist beyond the maximum you specify, the
          ``IsTruncated`` response element is ``true`` .

          If you do not include this parameter, the number of items defaults to 100. Note that IAM
          might return fewer results, even when there are more results available. In that case, the
          ``IsTruncated`` response element returns ``true`` , and ``Marker`` contains a value to
          include in the subsequent call that tells the service where to continue from.

        :rtype: list(:py:class:`iam.UserPolicy`)
        :returns: A list of UserPolicy resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        """
        Get a resource collection iterator from this manager.

        :rtype: :py:class:`ResourceCollection`
        :return: An iterable representing the collection of resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.UserPolicy]:
        """
        Creates an iterable up to a specified amount of UserPolicy resources in the collection.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListUserPolicies>`_

        **Request Syntax**
        ::

          user_policy_iterator = user.policies.limit(
              count=123
          )
        :type count: integer
        :param count: The limit to the number of resources in the iterable.

        :rtype: list(:py:class:`iam.UserPolicy`)
        :returns: A list of UserPolicy resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.UserPolicy]:
        """
        Creates an iterable of all UserPolicy resources in the collection, but limits the number of
        items returned by each service call by the specified amount.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListUserPolicies>`_

        **Request Syntax**
        ::

          user_policy_iterator = user.policies.page_size(
              count=123
          )
        :type count: integer
        :param count: The number of items returned by each service call

        :rtype: list(:py:class:`iam.UserPolicy`)
        :returns: A list of UserPolicy resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        """
        A generator which yields pages of resource instances after
        doing the appropriate service operation calls and handling
        any pagination on your behalf. Non-paginated calls will
        return a single page of items.

        Page size, item limit, and filter parameters are applied
        if they have previously been set.

            >>> bucket = s3.Bucket('boto3')
            >>> for page in bucket.objects.pages():
            ...     for obj in page:
            ...         print(obj.key)
            'key1'
            'key2'

        :rtype: list(:py:class:`~boto3.resources.base.ServiceResource`)
        :return: List of resource instances
        """


class UserSigningCertificatesCollection(ResourceCollection):
    """
    A group of resources. See :py:class:`Action`.

    :type name: string
    :param name: The name of the collection
    :type definition: dict
    :param definition: The JSON definition
    :type resource_defs: dict
    :param resource_defs: All resources defined in the service
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def all(self) -> List[service_resource_scope.SigningCertificate]:
        """
        Creates an iterable of all SigningCertificate resources in the collection.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListSigningCertificates>`_

        **Request Syntax**
        ::

          signing_certificate_iterator = user.signing_certificates.all()

        :rtype: list(:py:class:`iam.SigningCertificate`)
        :returns: A list of SigningCertificate resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def filter(
        self, Marker: str = None, MaxItems: int = None
    ) -> List[service_resource_scope.SigningCertificate]:
        """
        Creates an iterable of all SigningCertificate resources in the collection filtered by kwargs
        passed to method.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListSigningCertificates>`_

        **Request Syntax**
        ::

          signing_certificate_iterator = user.signing_certificates.filter(
              Marker='string',
              MaxItems=123
          )
        :type Marker: string
        :param Marker:

          Use this parameter only when paginating results and only after you receive a response
          indicating that the results are truncated. Set it to the value of the ``Marker`` element
          in the response that you received to indicate where the next call should start.

        :type MaxItems: integer
        :param MaxItems:

          Use this only when paginating results to indicate the maximum number of items you want in
          the response. If additional items exist beyond the maximum you specify, the
          ``IsTruncated`` response element is ``true`` .

          If you do not include this parameter, the number of items defaults to 100. Note that IAM
          might return fewer results, even when there are more results available. In that case, the
          ``IsTruncated`` response element returns ``true`` , and ``Marker`` contains a value to
          include in the subsequent call that tells the service where to continue from.

        :rtype: list(:py:class:`iam.SigningCertificate`)
        :returns: A list of SigningCertificate resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def iterator(self, **kwargs: Any) -> ResourceCollection:
        """
        Get a resource collection iterator from this manager.

        :rtype: :py:class:`ResourceCollection`
        :return: An iterable representing the collection of resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def limit(self, count: int) -> List[service_resource_scope.SigningCertificate]:
        """
        Creates an iterable up to a specified amount of SigningCertificate resources in the
        collection.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListSigningCertificates>`_

        **Request Syntax**
        ::

          signing_certificate_iterator = user.signing_certificates.limit(
              count=123
          )
        :type count: integer
        :param count: The limit to the number of resources in the iterable.

        :rtype: list(:py:class:`iam.SigningCertificate`)
        :returns: A list of SigningCertificate resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def page_size(self, count: int) -> List[service_resource_scope.SigningCertificate]:
        """
        Creates an iterable of all SigningCertificate resources in the collection, but limits the
        number of items returned by each service call by the specified amount.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/iam-2010-05-08/ListSigningCertificates>`_

        **Request Syntax**
        ::

          signing_certificate_iterator = user.signing_certificates.page_size(
              count=123
          )
        :type count: integer
        :param count: The number of items returned by each service call

        :rtype: list(:py:class:`iam.SigningCertificate`)
        :returns: A list of SigningCertificate resources
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def pages(self) -> List[Boto3ServiceResource]:
        """
        A generator which yields pages of resource instances after
        doing the appropriate service operation calls and handling
        any pagination on your behalf. Non-paginated calls will
        return a single page of items.

        Page size, item limit, and filter parameters are applied
        if they have previously been set.

            >>> bucket = s3.Bucket('boto3')
            >>> for page in bucket.objects.pages():
            ...     for obj in page:
            ...         print(obj.key)
            'key1'
            'key2'

        :rtype: list(:py:class:`~boto3.resources.base.ServiceResource`)
        :return: List of resource instances
        """
