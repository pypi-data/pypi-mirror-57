"Main interface for sts service Client"
from __future__ import annotations

from typing import Any, Dict, List
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError

# pylint: disable=import-self
import mypy_boto3_sts.client as client_scope
from mypy_boto3_sts.type_defs import (
    ClientAssumeRolePolicyArnsTypeDef,
    ClientAssumeRoleResponseTypeDef,
    ClientAssumeRoleTagsTypeDef,
    ClientAssumeRoleWithSamlPolicyArnsTypeDef,
    ClientAssumeRoleWithSamlResponseTypeDef,
    ClientAssumeRoleWithWebIdentityPolicyArnsTypeDef,
    ClientAssumeRoleWithWebIdentityResponseTypeDef,
    ClientDecodeAuthorizationMessageResponseTypeDef,
    ClientGetAccessKeyInfoResponseTypeDef,
    ClientGetCallerIdentityResponseTypeDef,
    ClientGetFederationTokenPolicyArnsTypeDef,
    ClientGetFederationTokenResponseTypeDef,
    ClientGetFederationTokenTagsTypeDef,
    ClientGetSessionTokenResponseTypeDef,
)


__all__ = ("Client",)


class Client(BaseClient):
    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def assume_role(
        self,
        RoleArn: str,
        RoleSessionName: str,
        PolicyArns: List[ClientAssumeRolePolicyArnsTypeDef] = None,
        Policy: str = None,
        DurationSeconds: int = None,
        Tags: List[ClientAssumeRoleTagsTypeDef] = None,
        TransitiveTagKeys: List[str] = None,
        ExternalId: str = None,
        SerialNumber: str = None,
        TokenCode: str = None,
    ) -> ClientAssumeRoleResponseTypeDef:
        """
        Returns a set of temporary security credentials that you can use to access AWS resources
        that you might not normally have access to. These temporary credentials consist of an access
        key ID, a secret access key, and a security token. Typically, you use ``AssumeRole`` within
        your account or for cross-account access. For a comparison of ``AssumeRole`` with other API
        operations that produce temporary credentials, see `Requesting Temporary Security
        Credentials
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_request.html>`__ and
        `Comparing the AWS STS API operations
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_request.html#stsapi_comparison>`__
        in the *IAM User Guide* .

        .. warning::

          You cannot use AWS account root user credentials to call ``AssumeRole`` . You must use
          credentials for an IAM user or an IAM role to call ``AssumeRole`` .

        For cross-account access, imagine that you own multiple accounts and need to access
        resources in each account. You could create long-term credentials in each account to access
        those resources. However, managing all those credentials and remembering which one can
        access which account can be time consuming. Instead, you can create one set of long-term
        credentials in one account. Then use temporary security credentials to access all the other
        accounts by assuming roles in those accounts. For more information about roles, see `IAM
        Roles <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html>`__ in the *IAM User
        Guide* .

         **Session Duration**

        By default, the temporary security credentials created by ``AssumeRole`` last for one hour.
        However, you can use the optional ``DurationSeconds`` parameter to specify the duration of
        your session. You can provide a value from 900 seconds (15 minutes) up to the maximum
        session duration setting for the role. This setting can have a value from 1 hour to 12
        hours. To learn how to view the maximum value for your role, see `View the Maximum Session
        Duration Setting for a Role
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use.html#id_roles_use_view-role-max-session>`__
        in the *IAM User Guide* . The maximum session duration limit applies when you use the
        ``AssumeRole*`` API operations or the ``assume-role*`` CLI commands. However the limit does
        not apply when you use those operations to create a console URL. For more information, see
        `Using IAM Roles <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use.html>`__ in
        the *IAM User Guide* .

         **Permissions**

        The temporary security credentials created by ``AssumeRole`` can be used to make API calls
        to any AWS service with the following exception: You cannot call the AWS STS
        ``GetFederationToken`` or ``GetSessionToken`` API operations.

        (Optional) You can pass inline or managed `session policies
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_session>`__
        to this operation. You can pass a single JSON policy document to use as an inline session
        policy. You can also specify up to 10 managed policies to use as managed session policies.
        The plain text that you use for both inline and managed session policies can't exceed 2,048
        characters. Passing policies to this operation returns new temporary credentials. The
        resulting session's permissions are the intersection of the role's identity-based policy and
        the session policies. You can use the role's temporary credentials in subsequent AWS API
        calls to access resources in the account that owns the role. You cannot use session policies
        to grant more permissions than those allowed by the identity-based policy of the role that
        is being assumed. For more information, see `Session Policies
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_session>`__
        in the *IAM User Guide* .

        To assume a role from a different account, your AWS account must be trusted by the role. The
        trust relationship is defined in the role's trust policy when the role is created. That
        trust policy states which accounts are allowed to delegate that access to users in the
        account.

        A user who wants to access a role in a different account must also have permissions that are
        delegated from the user account administrator. The administrator must attach a policy that
        allows the user to call ``AssumeRole`` for the ARN of the role in the other account. If the
        user is in the same account as the role, then you can do either of the following:

        * Attach a policy to the user (identical to the previous user in a different account).

        * Add the user as a principal directly in the role's trust policy.

        In this case, the trust policy acts as an IAM resource-based policy. Users in the same
        account as the role do not need explicit permission to assume the role. For more information
        about trust policies and resource-based policies, see `IAM Policies
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html>`__ in the *IAM User
        Guide* .

         **Tags**

        (Optional) You can pass tag key-value pairs to your session. These tags are called session
        tags. For more information about session tags, see `Passing Session Tags in STS
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_session-tags.html>`__ in the *IAM User
        Guide* .

        An administrator must grant you the permissions necessary to pass session tags. The
        administrator can also create granular permissions to allow you to pass only specific
        session tags. For more information, see `Tutorial\\: Using Tags for Attribute-Based Access
        Control
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_attribute-based-access-control.html>`__
        in the *IAM User Guide* .

        You can set the session tags as transitive. Transitive tags persist during role chaining.
        For more information, see `Chaining Roles with Session Tags
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_session-tags.html#id_session-tags_role-chaining>`__
        in the *IAM User Guide* .

         **Using MFA with AssumeRole**

        (Optional) You can include multi-factor authentication (MFA) information when you call
        ``AssumeRole`` . This is useful for cross-account scenarios to ensure that the user that
        assumes the role has been authenticated with an AWS MFA device. In that scenario, the trust
        policy of the role being assumed includes a condition that tests for MFA authentication. If
        the caller does not include valid MFA information, the request to assume the role is denied.
        The condition in a trust policy that tests for MFA authentication might look like the
        following example.

         ``"Condition": {"Bool": {"aws:MultiFactorAuthPresent": true}}``

        For more information, see `Configuring MFA-Protected API Access
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/MFAProtectedAPI.html>`__ in the *IAM User
        Guide* guide.

        To use MFA with ``AssumeRole`` , you pass values for the ``SerialNumber`` and ``TokenCode``
        parameters. The ``SerialNumber`` value identifies the user's hardware or virtual MFA device.
        The ``TokenCode`` is the time-based one-time password (TOTP) that the MFA device produces.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sts-2011-06-15/AssumeRole>`_

        **Request Syntax**
        ::

          response = client.assume_role(
              RoleArn='string',
              RoleSessionName='string',
              PolicyArns=[
                  {
                      'arn': 'string'
                  },
              ],
              Policy='string',
              DurationSeconds=123,
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ],
              TransitiveTagKeys=[
                  'string',
              ],
              ExternalId='string',
              SerialNumber='string',
              TokenCode='string'
          )
        :type RoleArn: string
        :param RoleArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the role to assume.

        :type RoleSessionName: string
        :param RoleSessionName: **[REQUIRED]**

          An identifier for the assumed role session.

          Use the role session name to uniquely identify a session when the same role is assumed by
          different principals or for different reasons. In cross-account scenarios, the role
          session name is visible to, and can be logged by the account that owns the role. The role
          session name is also used in the ARN of the assumed role principal. This means that
          subsequent cross-account API requests that use the temporary security credentials will
          expose the role session name to the external account in their AWS CloudTrail logs.

          The regex used to validate this parameter is a string of characters consisting of upper-
          and lower-case alphanumeric characters with no spaces. You can also include underscores or
          any of the following characters: =,.@-

        :type PolicyArns: list
        :param PolicyArns:

          The Amazon Resource Names (ARNs) of the IAM managed policies that you want to use as
          managed session policies. The policies must exist in the same account as the role.

          This parameter is optional. You can provide up to 10 managed policy ARNs. However, the
          plain text that you use for both inline and managed session policies can't exceed 2,048
          characters. For more information about ARNs, see `Amazon Resource Names (ARNs) and AWS
          Service Namespaces
          <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in the AWS
          General Reference.

          .. note::

            An AWS conversion compresses the passed session policies and session tags into a packed
            binary format that has a separate limit. Your request can fail for this limit even if
            your plain text meets the other requirements. The ``PackedPolicySize`` response element
            indicates by percentage how close the policies and tags for your request are to the
            upper size limit.

          Passing policies to this operation returns new temporary credentials. The resulting
          session's permissions are the intersection of the role's identity-based policy and the
          session policies. You can use the role's temporary credentials in subsequent AWS API calls
          to access resources in the account that owns the role. You cannot use session policies to
          grant more permissions than those allowed by the identity-based policy of the role that is
          being assumed. For more information, see `Session Policies
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_session>`__
          in the *IAM User Guide* .

          - *(dict) --*

            A reference to the IAM managed policy that is passed as a session policy for a role
            session or a federated user session.

            - **arn** *(string) --*

              The Amazon Resource Name (ARN) of the IAM managed policy to use as a session policy
              for the role. For more information about ARNs, see `Amazon Resource Names (ARNs) and
              AWS Service Namespaces
              <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in the
              *AWS General Reference* .

        :type Policy: string
        :param Policy:

          An IAM policy in JSON format that you want to use as an inline session policy.

          This parameter is optional. Passing policies to this operation returns new temporary
          credentials. The resulting session's permissions are the intersection of the role's
          identity-based policy and the session policies. You can use the role's temporary
          credentials in subsequent AWS API calls to access resources in the account that owns the
          role. You cannot use session policies to grant more permissions than those allowed by the
          identity-based policy of the role that is being assumed. For more information, see
          `Session Policies
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_session>`__
          in the *IAM User Guide* .

          The plain text that you use for both inline and managed session policies can't exceed
          2,048 characters. The JSON policy characters can be any ASCII character from the space
          character to the end of the valid character list (\\u0020 through \\u00FF). It can also
          include the tab (\\u0009), linefeed (\\u000A), and carriage return (\\u000D) characters.

          .. note::

            An AWS conversion compresses the passed session policies and session tags into a packed
            binary format that has a separate limit. Your request can fail for this limit even if
            your plain text meets the other requirements. The ``PackedPolicySize`` response element
            indicates by percentage how close the policies and tags for your request are to the
            upper size limit.

        :type DurationSeconds: integer
        :param DurationSeconds:

          The duration, in seconds, of the role session. The value can range from 900 seconds (15
          minutes) up to the maximum session duration setting for the role. This setting can have a
          value from 1 hour to 12 hours. If you specify a value higher than this setting, the
          operation fails. For example, if you specify a session duration of 12 hours, but your
          administrator set the maximum session duration to 6 hours, your operation fails. To learn
          how to view the maximum value for your role, see `View the Maximum Session Duration
          Setting for a Role
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use.html#id_roles_use_view-role-max-session>`__
          in the *IAM User Guide* .

          By default, the value is set to ``3600`` seconds.

          .. note::

            The ``DurationSeconds`` parameter is separate from the duration of a console session
            that you might request using the returned credentials. The request to the federation
            endpoint for a console sign-in token takes a ``SessionDuration`` parameter that
            specifies the maximum length of the console session. For more information, see `Creating
            a URL that Enables Federated Users to Access the AWS Management Console
            <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_enable-console-custom-url.html>`__
            in the *IAM User Guide* .

        :type Tags: list
        :param Tags:

          A list of session tags that you want to pass. Each session tag consists of a key name and
          an associated value. For more information about session tags, see `Tagging AWS STS
          Sessions <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_session-tags.html>`__ in the
          *IAM User Guide* .

          This parameter is optional. You can pass up to 50 session tags. The plain text session tag
          keys can’t exceed 128 characters, and the values can’t exceed 256 characters. For these
          and additional limits, see `IAM and STS Character Limits
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-limits.html#reference_iam-limits-entity-length>`__
          in the *IAM User Guide* .

          .. note::

            An AWS conversion compresses the passed session policies and session tags into a packed
            binary format that has a separate limit. Your request can fail for this limit even if
            your plain text meets the other requirements. The ``PackedPolicySize`` response element
            indicates by percentage how close the policies and tags for your request are to the
            upper size limit.

          You can pass a session tag with the same key as a tag that is already attached to the
          role. When you do, session tags override a role tag with the same key.

          Tag key–value pairs are not case sensitive, but case is preserved. This means that you
          cannot have separate ``Department`` and ``department`` tag keys. Assume that the role has
          the ``Department`` =``Marketing`` tag and you pass the ``department`` =``engineering``
          session tag. ``Department`` and ``department`` are not saved as separate tags, and the
          session tag passed in the request takes precedence over the role tag.

          Additionally, if you used temporary credentials to perform this operation, the new session
          inherits any transitive session tags from the calling session. If you pass a session tag
          with the same key as an inherited tag, the operation fails. To view the inherited tags for
          a session, see the AWS CloudTrail logs. For more information, see `Viewing Session Tags in
          CloudTrail
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/session-tags.html#id_session-tags_ctlogs>`__
          in the *IAM User Guide* .

          - *(dict) --*

            You can pass custom key-value pair attributes when you assume a role or federate a user.
            These are called session tags. You can then use the session tags to control access to
            resources. For more information, see `Tagging AWS STS Sessions
            <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_session-tags.html>`__ in the *IAM
            User Guide* .

            - **Key** *(string) --* **[REQUIRED]**

              The key for a session tag.

              You can pass up to 50 session tags. The plain text session tag keys can’t exceed 128
              characters. For these and additional limits, see `IAM and STS Character Limits
              <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-limits.html#reference_iam-limits-entity-length>`__
              in the *IAM User Guide* .

            - **Value** *(string) --* **[REQUIRED]**

              The value for a session tag.

              You can pass up to 50 session tags. The plain text session tag values can’t exceed 256
              characters. For these and additional limits, see `IAM and STS Character Limits
              <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-limits.html#reference_iam-limits-entity-length>`__
              in the *IAM User Guide* .

        :type TransitiveTagKeys: list
        :param TransitiveTagKeys:

          A list of keys for session tags that you want to set as transitive. If you set a tag key
          as transitive, the corresponding key and value passes to subsequent sessions in a role
          chain. For more information, see `Chaining Roles with Session Tags
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_session-tags.html#id_session-tags_role-chaining>`__
          in the *IAM User Guide* .

          This parameter is optional. When you set session tags as transitive, the session policy
          and session tags packed binary limit is not affected.

          If you choose not to specify a transitive tag key, then no tags are passed from this
          session to any subsequent sessions.

          - *(string) --*

        :type ExternalId: string
        :param ExternalId:

          A unique identifier that might be required when you assume a role in another account. If
          the administrator of the account to which the role belongs provided you with an external
          ID, then provide that value in the ``ExternalId`` parameter. This value can be any string,
          such as a passphrase or account number. A cross-account role is usually set up to trust
          everyone in an account. Therefore, the administrator of the trusting account might send an
          external ID to the administrator of the trusted account. That way, only someone with the
          ID can assume the role, rather than everyone in the account. For more information about
          the external ID, see `How to Use an External ID When Granting Access to Your AWS Resources
          to a Third Party
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user_externalid.html>`__
          in the *IAM User Guide* .

          The regex used to validate this parameter is a string of characters consisting of upper-
          and lower-case alphanumeric characters with no spaces. You can also include underscores or
          any of the following characters: =,.@:/-

        :type SerialNumber: string
        :param SerialNumber:

          The identification number of the MFA device that is associated with the user who is making
          the ``AssumeRole`` call. Specify this value if the trust policy of the role being assumed
          includes a condition that requires MFA authentication. The value is either the serial
          number for a hardware device (such as ``GAHT12345678`` ) or an Amazon Resource Name (ARN)
          for a virtual device (such as ``arn:aws:iam::123456789012:mfa/user`` ).

          The regex used to validate this parameter is a string of characters consisting of upper-
          and lower-case alphanumeric characters with no spaces. You can also include underscores or
          any of the following characters: =,.@-

        :type TokenCode: string
        :param TokenCode:

          The value provided by the MFA device, if the trust policy of the role being assumed
          requires MFA (that is, if the policy includes a condition that tests for MFA). If the role
          being assumed requires MFA and if the ``TokenCode`` value is missing or expired, the
          ``AssumeRole`` call returns an "access denied" error.

          The format for this parameter, as described by its regex pattern, is a sequence of six
          numeric digits.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Credentials': {
                    'AccessKeyId': 'string',
                    'SecretAccessKey': 'string',
                    'SessionToken': 'string',
                    'Expiration': datetime(2015, 1, 1)
                },
                'AssumedRoleUser': {
                    'AssumedRoleId': 'string',
                    'Arn': 'string'
                },
                'PackedPolicySize': 123
            }
          **Response Structure**

          - *(dict) --*

            Contains the response to a successful  AssumeRole request, including temporary AWS
            credentials that can be used to make AWS requests.

            - **Credentials** *(dict) --*

              The temporary security credentials, which include an access key ID, a secret access
              key, and a security (or session) token.

              .. note::

                The size of the security token that STS API operations return is not fixed. We
                strongly recommend that you make no assumptions about the maximum size.

              - **AccessKeyId** *(string) --*

                The access key ID that identifies the temporary security credentials.

              - **SecretAccessKey** *(string) --*

                The secret access key that can be used to sign requests.

              - **SessionToken** *(string) --*

                The token that users must pass to the service API to use the temporary credentials.

              - **Expiration** *(datetime) --*

                The date on which the current credentials expire.

            - **AssumedRoleUser** *(dict) --*

              The Amazon Resource Name (ARN) and the assumed role ID, which are identifiers that you
              can use to refer to the resulting temporary security credentials. For example, you can
              reference these credentials as a principal in a resource-based policy by using the ARN
              or assumed role ID. The ARN and ID include the ``RoleSessionName`` that you specified
              when you called ``AssumeRole`` .

              - **AssumedRoleId** *(string) --*

                A unique identifier that contains the role ID and the role session name of the role
                that is being assumed. The role ID is generated by AWS when the role is created.

              - **Arn** *(string) --*

                The ARN of the temporary security credentials that are returned from the  AssumeRole
                action. For more information about ARNs and how to use them in policies, see `IAM
                Identifiers
                <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html>`__ in
                the *IAM User Guide* .

            - **PackedPolicySize** *(integer) --*

              A percentage value that indicates the packed size of the session policies and session
              tags combined passed in the request. The request fails if the packed size is greater
              than 100 percent, which means the policies and tags exceeded the allowed space.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def assume_role_with_saml(
        self,
        RoleArn: str,
        PrincipalArn: str,
        SAMLAssertion: str,
        PolicyArns: List[ClientAssumeRoleWithSamlPolicyArnsTypeDef] = None,
        Policy: str = None,
        DurationSeconds: int = None,
    ) -> ClientAssumeRoleWithSamlResponseTypeDef:
        """
        Returns a set of temporary security credentials for users who have been authenticated via a
        SAML authentication response. This operation provides a mechanism for tying an enterprise
        identity store or directory to role-based AWS access without user-specific credentials or
        configuration. For a comparison of ``AssumeRoleWithSAML`` with the other API operations that
        produce temporary credentials, see `Requesting Temporary Security Credentials
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_request.html>`__ and
        `Comparing the AWS STS API operations
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_request.html#stsapi_comparison>`__
        in the *IAM User Guide* .

        The temporary security credentials returned by this operation consist of an access key ID, a
        secret access key, and a security token. Applications can use these temporary security
        credentials to sign calls to AWS services.

         **Session Duration**

        By default, the temporary security credentials created by ``AssumeRoleWithSAML`` last for
        one hour. However, you can use the optional ``DurationSeconds`` parameter to specify the
        duration of your session. Your role session lasts for the duration that you specify, or
        until the time specified in the SAML authentication response's ``SessionNotOnOrAfter``
        value, whichever is shorter. You can provide a ``DurationSeconds`` value from 900 seconds
        (15 minutes) up to the maximum session duration setting for the role. This setting can have
        a value from 1 hour to 12 hours. To learn how to view the maximum value for your role, see
        `View the Maximum Session Duration Setting for a Role
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use.html#id_roles_use_view-role-max-session>`__
        in the *IAM User Guide* . The maximum session duration limit applies when you use the
        ``AssumeRole*`` API operations or the ``assume-role*`` CLI commands. However the limit does
        not apply when you use those operations to create a console URL. For more information, see
        `Using IAM Roles <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use.html>`__ in
        the *IAM User Guide* .

         **Permissions**

        The temporary security credentials created by ``AssumeRoleWithSAML`` can be used to make API
        calls to any AWS service with the following exception: you cannot call the STS
        ``GetFederationToken`` or ``GetSessionToken`` API operations.

        (Optional) You can pass inline or managed `session policies
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_session>`__
        to this operation. You can pass a single JSON policy document to use as an inline session
        policy. You can also specify up to 10 managed policies to use as managed session policies.
        The plain text that you use for both inline and managed session policies can't exceed 2,048
        characters. Passing policies to this operation returns new temporary credentials. The
        resulting session's permissions are the intersection of the role's identity-based policy and
        the session policies. You can use the role's temporary credentials in subsequent AWS API
        calls to access resources in the account that owns the role. You cannot use session policies
        to grant more permissions than those allowed by the identity-based policy of the role that
        is being assumed. For more information, see `Session Policies
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_session>`__
        in the *IAM User Guide* .

        Calling ``AssumeRoleWithSAML`` does not require the use of AWS security credentials. The
        identity of the caller is validated by using keys in the metadata document that is uploaded
        for the SAML provider entity for your identity provider.

        .. warning::

          Calling ``AssumeRoleWithSAML`` can result in an entry in your AWS CloudTrail logs. The
          entry includes the value in the ``NameID`` element of the SAML assertion. We recommend
          that you use a ``NameIDType`` that is not associated with any personally identifiable
          information (PII). For example, you could instead use the persistent identifier
          (``urn:oasis:names:tc:SAML:2.0:nameid-format:persistent`` ).

         **Tags**

        (Optional) You can configure your IdP to pass attributes into your SAML assertion as session
        tags. Each session tag consists of a key name and an associated value. For more information
        about session tags, see `Passing Session Tags in STS
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_session-tags.html>`__ in the *IAM User
        Guide* .

        You can pass up to 50 session tags. The plain text session tag keys can’t exceed 128
        characters and the values can’t exceed 256 characters. For these and additional limits, see
        `IAM and STS Character Limits
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-limits.html#reference_iam-limits-entity-length>`__
        in the *IAM User Guide* .

        .. note::

          An AWS conversion compresses the passed session policies and session tags into a packed
          binary format that has a separate limit. Your request can fail for this limit even if your
          plain text meets the other requirements. The ``PackedPolicySize`` response element
          indicates by percentage how close the policies and tags for your request are to the upper
          size limit.

        You can pass a session tag with the same key as a tag that is attached to the role. When you
        do, session tags override the role's tags with the same key.

        An administrator must grant you the permissions necessary to pass session tags. The
        administrator can also create granular permissions to allow you to pass only specific
        session tags. For more information, see `Tutorial\\: Using Tags for Attribute-Based Access
        Control
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_attribute-based-access-control.html>`__
        in the *IAM User Guide* .

        You can set the session tags as transitive. Transitive tags persist during role chaining.
        For more information, see `Chaining Roles with Session Tags
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_session-tags.html#id_session-tags_role-chaining>`__
        in the *IAM User Guide* .

         **SAML Configuration**

        Before your application can call ``AssumeRoleWithSAML`` , you must configure your SAML
        identity provider (IdP) to issue the claims required by AWS. Additionally, you must use AWS
        Identity and Access Management (IAM) to create a SAML provider entity in your AWS account
        that represents your identity provider. You must also create an IAM role that specifies this
        SAML provider in its trust policy.

        For more information, see the following resources:

        * `About SAML 2.0-based Federation
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_saml.html>`__ in the
        *IAM User Guide* .

        * `Creating SAML Identity Providers
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_saml.html>`__ in
        the *IAM User Guide* .

        * `Configuring a Relying Party and Claims
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_saml_relying-party.html>`__
        in the *IAM User Guide* .

        * `Creating a Role for SAML 2.0 Federation
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-idp_saml.html>`__ in
        the *IAM User Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sts-2011-06-15/AssumeRoleWithSAML>`_

        **Request Syntax**
        ::

          response = client.assume_role_with_saml(
              RoleArn='string',
              PrincipalArn='string',
              SAMLAssertion='string',
              PolicyArns=[
                  {
                      'arn': 'string'
                  },
              ],
              Policy='string',
              DurationSeconds=123
          )
        :type RoleArn: string
        :param RoleArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the role that the caller is assuming.

        :type PrincipalArn: string
        :param PrincipalArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the SAML provider in IAM that describes the IdP.

        :type SAMLAssertion: string
        :param SAMLAssertion: **[REQUIRED]**

          The base-64 encoded SAML authentication response provided by the IdP.

          For more information, see `Configuring a Relying Party and Adding Claims
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/create-role-saml-IdP-tasks.html>`__ in
          the *IAM User Guide* .

        :type PolicyArns: list
        :param PolicyArns:

          The Amazon Resource Names (ARNs) of the IAM managed policies that you want to use as
          managed session policies. The policies must exist in the same account as the role.

          This parameter is optional. You can provide up to 10 managed policy ARNs. However, the
          plain text that you use for both inline and managed session policies can't exceed 2,048
          characters. For more information about ARNs, see `Amazon Resource Names (ARNs) and AWS
          Service Namespaces
          <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in the AWS
          General Reference.

          .. note::

            An AWS conversion compresses the passed session policies and session tags into a packed
            binary format that has a separate limit. Your request can fail for this limit even if
            your plain text meets the other requirements. The ``PackedPolicySize`` response element
            indicates by percentage how close the policies and tags for your request are to the
            upper size limit.

          Passing policies to this operation returns new temporary credentials. The resulting
          session's permissions are the intersection of the role's identity-based policy and the
          session policies. You can use the role's temporary credentials in subsequent AWS API calls
          to access resources in the account that owns the role. You cannot use session policies to
          grant more permissions than those allowed by the identity-based policy of the role that is
          being assumed. For more information, see `Session Policies
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_session>`__
          in the *IAM User Guide* .

          - *(dict) --*

            A reference to the IAM managed policy that is passed as a session policy for a role
            session or a federated user session.

            - **arn** *(string) --*

              The Amazon Resource Name (ARN) of the IAM managed policy to use as a session policy
              for the role. For more information about ARNs, see `Amazon Resource Names (ARNs) and
              AWS Service Namespaces
              <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in the
              *AWS General Reference* .

        :type Policy: string
        :param Policy:

          An IAM policy in JSON format that you want to use as an inline session policy.

          This parameter is optional. Passing policies to this operation returns new temporary
          credentials. The resulting session's permissions are the intersection of the role's
          identity-based policy and the session policies. You can use the role's temporary
          credentials in subsequent AWS API calls to access resources in the account that owns the
          role. You cannot use session policies to grant more permissions than those allowed by the
          identity-based policy of the role that is being assumed. For more information, see
          `Session Policies
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_session>`__
          in the *IAM User Guide* .

          The plain text that you use for both inline and managed session policies can't exceed
          2,048 characters. The JSON policy characters can be any ASCII character from the space
          character to the end of the valid character list (\\u0020 through \\u00FF). It can also
          include the tab (\\u0009), linefeed (\\u000A), and carriage return (\\u000D) characters.

          .. note::

            An AWS conversion compresses the passed session policies and session tags into a packed
            binary format that has a separate limit. Your request can fail for this limit even if
            your plain text meets the other requirements. The ``PackedPolicySize`` response element
            indicates by percentage how close the policies and tags for your request are to the
            upper size limit.

        :type DurationSeconds: integer
        :param DurationSeconds:

          The duration, in seconds, of the role session. Your role session lasts for the duration
          that you specify for the ``DurationSeconds`` parameter, or until the time specified in the
          SAML authentication response's ``SessionNotOnOrAfter`` value, whichever is shorter. You
          can provide a ``DurationSeconds`` value from 900 seconds (15 minutes) up to the maximum
          session duration setting for the role. This setting can have a value from 1 hour to 12
          hours. If you specify a value higher than this setting, the operation fails. For example,
          if you specify a session duration of 12 hours, but your administrator set the maximum
          session duration to 6 hours, your operation fails. To learn how to view the maximum value
          for your role, see `View the Maximum Session Duration Setting for a Role
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use.html#id_roles_use_view-role-max-session>`__
          in the *IAM User Guide* .

          By default, the value is set to ``3600`` seconds.

          .. note::

            The ``DurationSeconds`` parameter is separate from the duration of a console session
            that you might request using the returned credentials. The request to the federation
            endpoint for a console sign-in token takes a ``SessionDuration`` parameter that
            specifies the maximum length of the console session. For more information, see `Creating
            a URL that Enables Federated Users to Access the AWS Management Console
            <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_enable-console-custom-url.html>`__
            in the *IAM User Guide* .

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Credentials': {
                    'AccessKeyId': 'string',
                    'SecretAccessKey': 'string',
                    'SessionToken': 'string',
                    'Expiration': datetime(2015, 1, 1)
                },
                'AssumedRoleUser': {
                    'AssumedRoleId': 'string',
                    'Arn': 'string'
                },
                'PackedPolicySize': 123,
                'Subject': 'string',
                'SubjectType': 'string',
                'Issuer': 'string',
                'Audience': 'string',
                'NameQualifier': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Contains the response to a successful  AssumeRoleWithSAML request, including temporary
            AWS credentials that can be used to make AWS requests.

            - **Credentials** *(dict) --*

              The temporary security credentials, which include an access key ID, a secret access
              key, and a security (or session) token.

              .. note::

                The size of the security token that STS API operations return is not fixed. We
                strongly recommend that you make no assumptions about the maximum size.

              - **AccessKeyId** *(string) --*

                The access key ID that identifies the temporary security credentials.

              - **SecretAccessKey** *(string) --*

                The secret access key that can be used to sign requests.

              - **SessionToken** *(string) --*

                The token that users must pass to the service API to use the temporary credentials.

              - **Expiration** *(datetime) --*

                The date on which the current credentials expire.

            - **AssumedRoleUser** *(dict) --*

              The identifiers for the temporary security credentials that the operation returns.

              - **AssumedRoleId** *(string) --*

                A unique identifier that contains the role ID and the role session name of the role
                that is being assumed. The role ID is generated by AWS when the role is created.

              - **Arn** *(string) --*

                The ARN of the temporary security credentials that are returned from the  AssumeRole
                action. For more information about ARNs and how to use them in policies, see `IAM
                Identifiers
                <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html>`__ in
                the *IAM User Guide* .

            - **PackedPolicySize** *(integer) --*

              A percentage value that indicates the packed size of the session policies and session
              tags combined passed in the request. The request fails if the packed size is greater
              than 100 percent, which means the policies and tags exceeded the allowed space.

            - **Subject** *(string) --*

              The value of the ``NameID`` element in the ``Subject`` element of the SAML assertion.

            - **SubjectType** *(string) --*

              The format of the name ID, as defined by the ``Format`` attribute in the ``NameID``
              element of the SAML assertion. Typical examples of the format are ``transient`` or
              ``persistent`` .

              If the format includes the prefix ``urn:oasis:names:tc:SAML:2.0:nameid-format`` , that
              prefix is removed. For example,
              ``urn:oasis:names:tc:SAML:2.0:nameid-format:transient`` is returned as ``transient`` .
              If the format includes any other prefix, the format is returned with no modifications.

            - **Issuer** *(string) --*

              The value of the ``Issuer`` element of the SAML assertion.

            - **Audience** *(string) --*

              The value of the ``Recipient`` attribute of the ``SubjectConfirmationData`` element of
              the SAML assertion.

            - **NameQualifier** *(string) --*

              A hash value based on the concatenation of the ``Issuer`` response value, the AWS
              account ID, and the friendly name (the last part of the ARN) of the SAML provider in
              IAM. The combination of ``NameQualifier`` and ``Subject`` can be used to uniquely
              identify a federated user.

              The following pseudocode shows how the hash value is calculated:

               ``BASE64 ( SHA1 ( "https://example.com/saml" + "123456789012" + "/MySAMLIdP" ) )``
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def assume_role_with_web_identity(
        self,
        RoleArn: str,
        RoleSessionName: str,
        WebIdentityToken: str,
        ProviderId: str = None,
        PolicyArns: List[ClientAssumeRoleWithWebIdentityPolicyArnsTypeDef] = None,
        Policy: str = None,
        DurationSeconds: int = None,
    ) -> ClientAssumeRoleWithWebIdentityResponseTypeDef:
        """
        Returns a set of temporary security credentials for users who have been authenticated in a
        mobile or web application with a web identity provider. Example providers include Amazon
        Cognito, Login with Amazon, Facebook, Google, or any OpenID Connect-compatible identity
        provider.

        .. note::

          For mobile applications, we recommend that you use Amazon Cognito. You can use Amazon
          Cognito with the `AWS SDK for iOS Developer Guide <http://aws.amazon.com/sdkforios/>`__
          and the `AWS SDK for Android Developer Guide <http://aws.amazon.com/sdkforandroid/>`__ to
          uniquely identify a user. You can also supply the user with a consistent identity
          throughout the lifetime of an application.

          To learn more about Amazon Cognito, see `Amazon Cognito Overview
          <https://docs.aws.amazon.com/mobile/sdkforandroid/developerguide/cognito-auth.html#d0e840>`__
          in *AWS SDK for Android Developer Guide* and `Amazon Cognito Overview
          <https://docs.aws.amazon.com/mobile/sdkforios/developerguide/cognito-auth.html#d0e664>`__
          in the *AWS SDK for iOS Developer Guide* .

        Calling ``AssumeRoleWithWebIdentity`` does not require the use of AWS security credentials.
        Therefore, you can distribute an application (for example, on mobile devices) that requests
        temporary security credentials without including long-term AWS credentials in the
        application. You also don't need to deploy server-based proxy services that use long-term
        AWS credentials. Instead, the identity of the caller is validated by using a token from the
        web identity provider. For a comparison of ``AssumeRoleWithWebIdentity`` with the other API
        operations that produce temporary credentials, see `Requesting Temporary Security
        Credentials
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_request.html>`__ and
        `Comparing the AWS STS API operations
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_request.html#stsapi_comparison>`__
        in the *IAM User Guide* .

        The temporary security credentials returned by this API consist of an access key ID, a
        secret access key, and a security token. Applications can use these temporary security
        credentials to sign calls to AWS service API operations.

         **Session Duration**

        By default, the temporary security credentials created by ``AssumeRoleWithWebIdentity`` last
        for one hour. However, you can use the optional ``DurationSeconds`` parameter to specify the
        duration of your session. You can provide a value from 900 seconds (15 minutes) up to the
        maximum session duration setting for the role. This setting can have a value from 1 hour to
        12 hours. To learn how to view the maximum value for your role, see `View the Maximum
        Session Duration Setting for a Role
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use.html#id_roles_use_view-role-max-session>`__
        in the *IAM User Guide* . The maximum session duration limit applies when you use the
        ``AssumeRole*`` API operations or the ``assume-role*`` CLI commands. However the limit does
        not apply when you use those operations to create a console URL. For more information, see
        `Using IAM Roles <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use.html>`__ in
        the *IAM User Guide* .

         **Permissions**

        The temporary security credentials created by ``AssumeRoleWithWebIdentity`` can be used to
        make API calls to any AWS service with the following exception: you cannot call the STS
        ``GetFederationToken`` or ``GetSessionToken`` API operations.

        (Optional) You can pass inline or managed `session policies
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_session>`__
        to this operation. You can pass a single JSON policy document to use as an inline session
        policy. You can also specify up to 10 managed policies to use as managed session policies.
        The plain text that you use for both inline and managed session policies can't exceed 2,048
        characters. Passing policies to this operation returns new temporary credentials. The
        resulting session's permissions are the intersection of the role's identity-based policy and
        the session policies. You can use the role's temporary credentials in subsequent AWS API
        calls to access resources in the account that owns the role. You cannot use session policies
        to grant more permissions than those allowed by the identity-based policy of the role that
        is being assumed. For more information, see `Session Policies
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_session>`__
        in the *IAM User Guide* .

         **Tags**

        (Optional) You can configure your IdP to pass attributes into your web identity token as
        session tags. Each session tag consists of a key name and an associated value. For more
        information about session tags, see `Passing Session Tags in STS
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_session-tags.html>`__ in the *IAM User
        Guide* .

        You can pass up to 50 session tags. The plain text session tag keys can’t exceed 128
        characters and the values can’t exceed 256 characters. For these and additional limits, see
        `IAM and STS Character Limits
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-limits.html#reference_iam-limits-entity-length>`__
        in the *IAM User Guide* .

        .. note::

          An AWS conversion compresses the passed session policies and session tags into a packed
          binary format that has a separate limit. Your request can fail for this limit even if your
          plain text meets the other requirements. The ``PackedPolicySize`` response element
          indicates by percentage how close the policies and tags for your request are to the upper
          size limit.

        You can pass a session tag with the same key as a tag that is attached to the role. When you
        do, the session tag overrides the role tag with the same key.

        An administrator must grant you the permissions necessary to pass session tags. The
        administrator can also create granular permissions to allow you to pass only specific
        session tags. For more information, see `Tutorial\\: Using Tags for Attribute-Based Access
        Control
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_attribute-based-access-control.html>`__
        in the *IAM User Guide* .

        You can set the session tags as transitive. Transitive tags persist during role chaining.
        For more information, see `Chaining Roles with Session Tags
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_session-tags.html#id_session-tags_role-chaining>`__
        in the *IAM User Guide* .

         **Identities**

        Before your application can call ``AssumeRoleWithWebIdentity`` , you must have an identity
        token from a supported identity provider and create a role that the application can assume.
        The role that your application assumes must trust the identity provider that is associated
        with the identity token. In other words, the identity provider must be specified in the
        role's trust policy.

        .. warning::

          Calling ``AssumeRoleWithWebIdentity`` can result in an entry in your AWS CloudTrail logs.
          The entry includes the `Subject
          <http://openid.net/specs/openid-connect-core-1_0.html#Claims>`__ of the provided Web
          Identity Token. We recommend that you avoid using any personally identifiable information
          (PII) in this field. For example, you could instead use a GUID or a pairwise identifier,
          as `suggested in the OIDC specification
          <http://openid.net/specs/openid-connect-core-1_0.html#SubjectIDTypes>`__ .

        For more information about how to use web identity federation and the
        ``AssumeRoleWithWebIdentity`` API, see the following resources:

        * `Using Web Identity Federation API Operations for Mobile Apps
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_oidc_manual.html>`__
        and `Federation Through a Web-based Identity Provider
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_request.html#api_assumerolewithwebidentity>`__
        .

        * `Web Identity Federation Playground
        <https://web-identity-federation-playground.s3.amazonaws.com/index.html>`__ . Walk through
        the process of authenticating through Login with Amazon, Facebook, or Google, getting
        temporary security credentials, and then using those credentials to make a request to AWS.

        * `AWS SDK for iOS Developer Guide <http://aws.amazon.com/sdkforios/>`__ and `AWS SDK for
        Android Developer Guide <http://aws.amazon.com/sdkforandroid/>`__ . These toolkits contain
        sample apps that show how to invoke the identity providers. The toolkits then show how to
        use the information from these providers to get and use temporary security credentials.

        * `Web Identity Federation with Mobile Applications
        <http://aws.amazon.com/articles/web-identity-federation-with-mobile-applications>`__ . This
        article discusses web identity federation and shows an example of how to use web identity
        federation to get access to content in Amazon S3.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sts-2011-06-15/AssumeRoleWithWebIdentity>`_

        **Request Syntax**
        ::

          response = client.assume_role_with_web_identity(
              RoleArn='string',
              RoleSessionName='string',
              WebIdentityToken='string',
              ProviderId='string',
              PolicyArns=[
                  {
                      'arn': 'string'
                  },
              ],
              Policy='string',
              DurationSeconds=123
          )
        :type RoleArn: string
        :param RoleArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the role that the caller is assuming.

        :type RoleSessionName: string
        :param RoleSessionName: **[REQUIRED]**

          An identifier for the assumed role session. Typically, you pass the name or identifier
          that is associated with the user who is using your application. That way, the temporary
          security credentials that your application will use are associated with that user. This
          session name is included as part of the ARN and assumed role ID in the ``AssumedRoleUser``
          response element.

          The regex used to validate this parameter is a string of characters consisting of upper-
          and lower-case alphanumeric characters with no spaces. You can also include underscores or
          any of the following characters: =,.@-

        :type WebIdentityToken: string
        :param WebIdentityToken: **[REQUIRED]**

          The OAuth 2.0 access token or OpenID Connect ID token that is provided by the identity
          provider. Your application must get this token by authenticating the user who is using
          your application with a web identity provider before the application makes an
          ``AssumeRoleWithWebIdentity`` call.

        :type ProviderId: string
        :param ProviderId:

          The fully qualified host component of the domain name of the identity provider.

          Specify this value only for OAuth 2.0 access tokens. Currently ``www.amazon.com`` and
          ``graph.facebook.com`` are the only supported identity providers for OAuth 2.0 access
          tokens. Do not include URL schemes and port numbers.

          Do not specify this value for OpenID Connect ID tokens.

        :type PolicyArns: list
        :param PolicyArns:

          The Amazon Resource Names (ARNs) of the IAM managed policies that you want to use as
          managed session policies. The policies must exist in the same account as the role.

          This parameter is optional. You can provide up to 10 managed policy ARNs. However, the
          plain text that you use for both inline and managed session policies can't exceed 2,048
          characters. For more information about ARNs, see `Amazon Resource Names (ARNs) and AWS
          Service Namespaces
          <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in the AWS
          General Reference.

          .. note::

            An AWS conversion compresses the passed session policies and session tags into a packed
            binary format that has a separate limit. Your request can fail for this limit even if
            your plain text meets the other requirements. The ``PackedPolicySize`` response element
            indicates by percentage how close the policies and tags for your request are to the
            upper size limit.

          Passing policies to this operation returns new temporary credentials. The resulting
          session's permissions are the intersection of the role's identity-based policy and the
          session policies. You can use the role's temporary credentials in subsequent AWS API calls
          to access resources in the account that owns the role. You cannot use session policies to
          grant more permissions than those allowed by the identity-based policy of the role that is
          being assumed. For more information, see `Session Policies
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_session>`__
          in the *IAM User Guide* .

          - *(dict) --*

            A reference to the IAM managed policy that is passed as a session policy for a role
            session or a federated user session.

            - **arn** *(string) --*

              The Amazon Resource Name (ARN) of the IAM managed policy to use as a session policy
              for the role. For more information about ARNs, see `Amazon Resource Names (ARNs) and
              AWS Service Namespaces
              <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in the
              *AWS General Reference* .

        :type Policy: string
        :param Policy:

          An IAM policy in JSON format that you want to use as an inline session policy.

          This parameter is optional. Passing policies to this operation returns new temporary
          credentials. The resulting session's permissions are the intersection of the role's
          identity-based policy and the session policies. You can use the role's temporary
          credentials in subsequent AWS API calls to access resources in the account that owns the
          role. You cannot use session policies to grant more permissions than those allowed by the
          identity-based policy of the role that is being assumed. For more information, see
          `Session Policies
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_session>`__
          in the *IAM User Guide* .

          The plain text that you use for both inline and managed session policies can't exceed
          2,048 characters. The JSON policy characters can be any ASCII character from the space
          character to the end of the valid character list (\\u0020 through \\u00FF). It can also
          include the tab (\\u0009), linefeed (\\u000A), and carriage return (\\u000D) characters.

          .. note::

            An AWS conversion compresses the passed session policies and session tags into a packed
            binary format that has a separate limit. Your request can fail for this limit even if
            your plain text meets the other requirements. The ``PackedPolicySize`` response element
            indicates by percentage how close the policies and tags for your request are to the
            upper size limit.

        :type DurationSeconds: integer
        :param DurationSeconds:

          The duration, in seconds, of the role session. The value can range from 900 seconds (15
          minutes) up to the maximum session duration setting for the role. This setting can have a
          value from 1 hour to 12 hours. If you specify a value higher than this setting, the
          operation fails. For example, if you specify a session duration of 12 hours, but your
          administrator set the maximum session duration to 6 hours, your operation fails. To learn
          how to view the maximum value for your role, see `View the Maximum Session Duration
          Setting for a Role
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use.html#id_roles_use_view-role-max-session>`__
          in the *IAM User Guide* .

          By default, the value is set to ``3600`` seconds.

          .. note::

            The ``DurationSeconds`` parameter is separate from the duration of a console session
            that you might request using the returned credentials. The request to the federation
            endpoint for a console sign-in token takes a ``SessionDuration`` parameter that
            specifies the maximum length of the console session. For more information, see `Creating
            a URL that Enables Federated Users to Access the AWS Management Console
            <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_enable-console-custom-url.html>`__
            in the *IAM User Guide* .

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Credentials': {
                    'AccessKeyId': 'string',
                    'SecretAccessKey': 'string',
                    'SessionToken': 'string',
                    'Expiration': datetime(2015, 1, 1)
                },
                'SubjectFromWebIdentityToken': 'string',
                'AssumedRoleUser': {
                    'AssumedRoleId': 'string',
                    'Arn': 'string'
                },
                'PackedPolicySize': 123,
                'Provider': 'string',
                'Audience': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Contains the response to a successful  AssumeRoleWithWebIdentity request, including
            temporary AWS credentials that can be used to make AWS requests.

            - **Credentials** *(dict) --*

              The temporary security credentials, which include an access key ID, a secret access
              key, and a security token.

              .. note::

                The size of the security token that STS API operations return is not fixed. We
                strongly recommend that you make no assumptions about the maximum size.

              - **AccessKeyId** *(string) --*

                The access key ID that identifies the temporary security credentials.

              - **SecretAccessKey** *(string) --*

                The secret access key that can be used to sign requests.

              - **SessionToken** *(string) --*

                The token that users must pass to the service API to use the temporary credentials.

              - **Expiration** *(datetime) --*

                The date on which the current credentials expire.

            - **SubjectFromWebIdentityToken** *(string) --*

              The unique user identifier that is returned by the identity provider. This identifier
              is associated with the ``WebIdentityToken`` that was submitted with the
              ``AssumeRoleWithWebIdentity`` call. The identifier is typically unique to the user and
              the application that acquired the ``WebIdentityToken`` (pairwise identifier). For
              OpenID Connect ID tokens, this field contains the value returned by the identity
              provider as the token's ``sub`` (Subject) claim.

            - **AssumedRoleUser** *(dict) --*

              The Amazon Resource Name (ARN) and the assumed role ID, which are identifiers that you
              can use to refer to the resulting temporary security credentials. For example, you can
              reference these credentials as a principal in a resource-based policy by using the ARN
              or assumed role ID. The ARN and ID include the ``RoleSessionName`` that you specified
              when you called ``AssumeRole`` .

              - **AssumedRoleId** *(string) --*

                A unique identifier that contains the role ID and the role session name of the role
                that is being assumed. The role ID is generated by AWS when the role is created.

              - **Arn** *(string) --*

                The ARN of the temporary security credentials that are returned from the  AssumeRole
                action. For more information about ARNs and how to use them in policies, see `IAM
                Identifiers
                <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html>`__ in
                the *IAM User Guide* .

            - **PackedPolicySize** *(integer) --*

              A percentage value that indicates the packed size of the session policies and session
              tags combined passed in the request. The request fails if the packed size is greater
              than 100 percent, which means the policies and tags exceeded the allowed space.

            - **Provider** *(string) --*

              The issuing authority of the web identity token presented. For OpenID Connect ID
              tokens, this contains the value of the ``iss`` field. For OAuth 2.0 access tokens,
              this contains the value of the ``ProviderId`` parameter that was passed in the
              ``AssumeRoleWithWebIdentity`` request.

            - **Audience** *(string) --*

              The intended audience (also known as client ID) of the web identity token. This is
              traditionally the client identifier issued to the application that requested the web
              identity token.
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
    def decode_authorization_message(
        self, EncodedMessage: str
    ) -> ClientDecodeAuthorizationMessageResponseTypeDef:
        """
        Decodes additional information about the authorization status of a request from an encoded
        message returned in response to an AWS request.

        For example, if a user is not authorized to perform an operation that he or she has
        requested, the request returns a ``Client.UnauthorizedOperation`` response (an HTTP 403
        response). Some AWS operations additionally return an encoded message that can provide
        details about this authorization failure.

        .. note::

          Only certain AWS operations return an encoded authorization message. The documentation for
          an individual operation indicates whether that operation returns an encoded message in
          addition to returning an HTTP code.

        The message is encoded because the details of the authorization status can constitute
        privileged information that the user who requested the operation should not see. To decode
        an authorization status message, a user must be granted permissions via an IAM policy to
        request the ``DecodeAuthorizationMessage`` (``sts:DecodeAuthorizationMessage`` ) action.

        The decoded message includes the following type of information:

        * Whether the request was denied due to an explicit deny or due to the absence of an
        explicit allow. For more information, see `Determining Whether a Request is Allowed or
        Denied
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic.html#policy-eval-denyallow>`__
        in the *IAM User Guide* .

        * The principal who made the request.

        * The requested action.

        * The requested resource.

        * The values of condition keys in the context of the user's request.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sts-2011-06-15/DecodeAuthorizationMessage>`_

        **Request Syntax**
        ::

          response = client.decode_authorization_message(
              EncodedMessage='string'
          )
        :type EncodedMessage: string
        :param EncodedMessage: **[REQUIRED]**

          The encoded message that was returned with the response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'DecodedMessage': 'string'
            }
          **Response Structure**

          - *(dict) --*

            A document that contains additional information about the authorization status of a
            request from an encoded message that is returned in response to an AWS request.

            - **DecodedMessage** *(string) --*

              An XML document that contains the decoded message.
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
    def get_access_key_info(self, AccessKeyId: str) -> ClientGetAccessKeyInfoResponseTypeDef:
        """
        Returns the account identifier for the specified access key ID.

        Access keys consist of two parts: an access key ID (for example, ``AKIAIOSFODNN7EXAMPLE`` )
        and a secret access key (for example, ``wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY`` ). For
        more information about access keys, see `Managing Access Keys for IAM Users
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html>`__ in the
        *IAM User Guide* .

        When you pass an access key ID to this operation, it returns the ID of the AWS account to
        which the keys belong. Access key IDs beginning with ``AKIA`` are long-term credentials for
        an IAM user or the AWS account root user. Access key IDs beginning with ``ASIA`` are
        temporary credentials that are created using STS operations. If the account in the response
        belongs to you, you can sign in as the root user and review your root user access keys.
        Then, you can pull a `credentials report
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_getting-report.html>`__ to
        learn which IAM user owns the keys. To learn who requested the temporary credentials for an
        ``ASIA`` access key, view the STS events in your `CloudTrail logs
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/cloudtrail-integration.html>`__ in the
        *IAM User Guide* .

        This operation does not indicate the state of the access key. The key might be active,
        inactive, or deleted. Active keys might not have permissions to perform an operation.
        Providing a deleted access key might return an error that the key doesn't exist.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sts-2011-06-15/GetAccessKeyInfo>`_

        **Request Syntax**
        ::

          response = client.get_access_key_info(
              AccessKeyId='string'
          )
        :type AccessKeyId: string
        :param AccessKeyId: **[REQUIRED]**

          The identifier of an access key.

          This parameter allows (through its regex pattern) a string of characters that can consist
          of any upper- or lowercase letter or digit.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Account': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Account** *(string) --*

              The number used to identify the AWS account.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_caller_identity(
        self, *args: Any, **kwargs: Any
    ) -> ClientGetCallerIdentityResponseTypeDef:
        """
        Returns details about the IAM user or role whose credentials are used to call the operation.

        .. note::

          No permissions are required to perform this operation. If an administrator adds a policy
          to your IAM user or role that explicitly denies access to the ``sts:GetCallerIdentity``
          action, you can still perform this operation. Permissions are not required because the
          same information is returned when an IAM user or role is denied access. To view an example
          response, see `I Am Not Authorized to Perform\\: iam\\:DeleteVirtualMFADevice
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_general.html#troubleshoot_general_access-denied-delete-mfa>`__
          in the *IAM User Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sts-2011-06-15/GetCallerIdentity>`_

        **Request Syntax**
        ::

          response = client.get_caller_identity()

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'UserId': 'string',
                'Account': 'string',
                'Arn': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Contains the response to a successful  GetCallerIdentity request, including information
            about the entity making the request.

            - **UserId** *(string) --*

              The unique identifier of the calling entity. The exact value depends on the type of
              entity that is making the call. The values returned are those listed in the
              **aws:userid** column in the `Principal table
              <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_variables.html#principaltable>`__
              found on the **Policy Variables** reference page in the *IAM User Guide* .

            - **Account** *(string) --*

              The AWS account ID number of the account that owns or contains the calling entity.

            - **Arn** *(string) --*

              The AWS ARN associated with the calling entity.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_federation_token(
        self,
        Name: str,
        Policy: str = None,
        PolicyArns: List[ClientGetFederationTokenPolicyArnsTypeDef] = None,
        DurationSeconds: int = None,
        Tags: List[ClientGetFederationTokenTagsTypeDef] = None,
    ) -> ClientGetFederationTokenResponseTypeDef:
        """
        Returns a set of temporary security credentials (consisting of an access key ID, a secret
        access key, and a security token) for a federated user. A typical use is in a proxy
        application that gets temporary security credentials on behalf of distributed applications
        inside a corporate network. You must call the ``GetFederationToken`` operation using the
        long-term security credentials of an IAM user. As a result, this call is appropriate in
        contexts where those credentials can be safely stored, usually in a server-based
        application. For a comparison of ``GetFederationToken`` with the other API operations that
        produce temporary credentials, see `Requesting Temporary Security Credentials
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_request.html>`__ and
        `Comparing the AWS STS API operations
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_request.html#stsapi_comparison>`__
        in the *IAM User Guide* .

        .. note::

          You can create a mobile-based or browser-based app that can authenticate users using a web
          identity provider like Login with Amazon, Facebook, Google, or an OpenID
          Connect-compatible identity provider. In this case, we recommend that you use `Amazon
          Cognito <http://aws.amazon.com/cognito/>`__ or ``AssumeRoleWithWebIdentity`` . For more
          information, see `Federation Through a Web-based Identity Provider
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_request.html#api_assumerolewithwebidentity>`__
          in the *IAM User Guide* .

        You can also call ``GetFederationToken`` using the security credentials of an AWS account
        root user, but we do not recommend it. Instead, we recommend that you create an IAM user for
        the purpose of the proxy application. Then attach a policy to the IAM user that limits
        federated users to only the actions and resources that they need to access. For more
        information, see `IAM Best Practices
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html>`__ in the *IAM User
        Guide* .

         **Session duration**

        The temporary credentials are valid for the specified duration, from 900 seconds (15
        minutes) up to a maximum of 129,600 seconds (36 hours). The default session duration is
        43,200 seconds (12 hours). Temporary credentials that are obtained by using AWS account root
        user credentials have a maximum duration of 3,600 seconds (1 hour).

         **Permissions**

        You can use the temporary credentials created by ``GetFederationToken`` in any AWS service
        except the following:

        * You cannot call any IAM operations using the AWS CLI or the AWS API.

        * You cannot call any STS operations except ``GetCallerIdentity`` .

        You must pass an inline or managed `session policy
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_session>`__
        to this operation. You can pass a single JSON policy document to use as an inline session
        policy. You can also specify up to 10 managed policies to use as managed session policies.
        The plain text that you use for both inline and managed session policies can't exceed 2,048
        characters.

        Though the session policy parameters are optional, if you do not pass a policy, then the
        resulting federated user session has no permissions. When you pass session policies, the
        session permissions are the intersection of the IAM user policies and the session policies
        that you pass. This gives you a way to further restrict the permissions for a federated
        user. You cannot use session policies to grant more permissions than those that are defined
        in the permissions policy of the IAM user. For more information, see `Session Policies
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_session>`__
        in the *IAM User Guide* . For information about using ``GetFederationToken`` to create
        temporary security credentials, see `GetFederationToken—Federation Through a Custom Identity
        Broker
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_request.html#api_getfederationtoken>`__
        .

        You can use the credentials to access a resource that has a resource-based policy. If that
        policy specifically references the federated user session in the ``Principal`` element of
        the policy, the session has the permissions allowed by the policy. These permissions are
        granted in addition to the permissions granted by the session policies.

         **Tags**

        (Optional) You can pass tag key-value pairs to your session. These are called session tags.
        For more information about session tags, see `Passing Session Tags in STS
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_session-tags.html>`__ in the *IAM User
        Guide* .

        An administrator must grant you the permissions necessary to pass session tags. The
        administrator can also create granular permissions to allow you to pass only specific
        session tags. For more information, see `Tutorial\\: Using Tags for Attribute-Based Access
        Control
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_attribute-based-access-control.html>`__
        in the *IAM User Guide* .

        Tag key–value pairs are not case sensitive, but case is preserved. This means that you
        cannot have separate ``Department`` and ``department`` tag keys. Assume that the user that
        you are federating has the ``Department`` =``Marketing`` tag and you pass the ``department``
        =``engineering`` session tag. ``Department`` and ``department`` are not saved as separate
        tags, and the session tag passed in the request takes precedence over the user tag.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sts-2011-06-15/GetFederationToken>`_

        **Request Syntax**
        ::

          response = client.get_federation_token(
              Name='string',
              Policy='string',
              PolicyArns=[
                  {
                      'arn': 'string'
                  },
              ],
              DurationSeconds=123,
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ]
          )
        :type Name: string
        :param Name: **[REQUIRED]**

          The name of the federated user. The name is used as an identifier for the temporary
          security credentials (such as ``Bob`` ). For example, you can reference the federated user
          name in a resource-based policy, such as in an Amazon S3 bucket policy.

          The regex used to validate this parameter is a string of characters consisting of upper-
          and lower-case alphanumeric characters with no spaces. You can also include underscores or
          any of the following characters: =,.@-

        :type Policy: string
        :param Policy:

          An IAM policy in JSON format that you want to use as an inline session policy.

          You must pass an inline or managed `session policy
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_session>`__
          to this operation. You can pass a single JSON policy document to use as an inline session
          policy. You can also specify up to 10 managed policies to use as managed session policies.

          This parameter is optional. However, if you do not pass any session policies, then the
          resulting federated user session has no permissions.

          When you pass session policies, the session permissions are the intersection of the IAM
          user policies and the session policies that you pass. This gives you a way to further
          restrict the permissions for a federated user. You cannot use session policies to grant
          more permissions than those that are defined in the permissions policy of the IAM user.
          For more information, see `Session Policies
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_session>`__
          in the *IAM User Guide* .

          The resulting credentials can be used to access a resource that has a resource-based
          policy. If that policy specifically references the federated user session in the
          ``Principal`` element of the policy, the session has the permissions allowed by the
          policy. These permissions are granted in addition to the permissions that are granted by
          the session policies.

          The plain text that you use for both inline and managed session policies can't exceed
          2,048 characters. The JSON policy characters can be any ASCII character from the space
          character to the end of the valid character list (\\u0020 through \\u00FF). It can also
          include the tab (\\u0009), linefeed (\\u000A), and carriage return (\\u000D) characters.

          .. note::

            An AWS conversion compresses the passed session policies and session tags into a packed
            binary format that has a separate limit. Your request can fail for this limit even if
            your plain text meets the other requirements. The ``PackedPolicySize`` response element
            indicates by percentage how close the policies and tags for your request are to the
            upper size limit.

        :type PolicyArns: list
        :param PolicyArns:

          The Amazon Resource Names (ARNs) of the IAM managed policies that you want to use as a
          managed session policy. The policies must exist in the same account as the IAM user that
          is requesting federated access.

          You must pass an inline or managed `session policy
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_session>`__
          to this operation. You can pass a single JSON policy document to use as an inline session
          policy. You can also specify up to 10 managed policies to use as managed session policies.
          The plain text that you use for both inline and managed session policies can't exceed
          2,048 characters. You can provide up to 10 managed policy ARNs. For more information about
          ARNs, see `Amazon Resource Names (ARNs) and AWS Service Namespaces
          <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in the AWS
          General Reference.

          This parameter is optional. However, if you do not pass any session policies, then the
          resulting federated user session has no permissions.

          When you pass session policies, the session permissions are the intersection of the IAM
          user policies and the session policies that you pass. This gives you a way to further
          restrict the permissions for a federated user. You cannot use session policies to grant
          more permissions than those that are defined in the permissions policy of the IAM user.
          For more information, see `Session Policies
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_session>`__
          in the *IAM User Guide* .

          The resulting credentials can be used to access a resource that has a resource-based
          policy. If that policy specifically references the federated user session in the
          ``Principal`` element of the policy, the session has the permissions allowed by the
          policy. These permissions are granted in addition to the permissions that are granted by
          the session policies.

          .. note::

            An AWS conversion compresses the passed session policies and session tags into a packed
            binary format that has a separate limit. Your request can fail for this limit even if
            your plain text meets the other requirements. The ``PackedPolicySize`` response element
            indicates by percentage how close the policies and tags for your request are to the
            upper size limit.

          - *(dict) --*

            A reference to the IAM managed policy that is passed as a session policy for a role
            session or a federated user session.

            - **arn** *(string) --*

              The Amazon Resource Name (ARN) of the IAM managed policy to use as a session policy
              for the role. For more information about ARNs, see `Amazon Resource Names (ARNs) and
              AWS Service Namespaces
              <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in the
              *AWS General Reference* .

        :type DurationSeconds: integer
        :param DurationSeconds:

          The duration, in seconds, that the session should last. Acceptable durations for
          federation sessions range from 900 seconds (15 minutes) to 129,600 seconds (36 hours),
          with 43,200 seconds (12 hours) as the default. Sessions obtained using AWS account root
          user credentials are restricted to a maximum of 3,600 seconds (one hour). If the specified
          duration is longer than one hour, the session obtained by using root user credentials
          defaults to one hour.

        :type Tags: list
        :param Tags:

          A list of session tags. Each session tag consists of a key name and an associated value.
          For more information about session tags, see `Passing Session Tags in STS
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_session-tags.html>`__ in the *IAM
          User Guide* .

          This parameter is optional. You can pass up to 50 session tags. The plain text session tag
          keys can’t exceed 128 characters and the values can’t exceed 256 characters. For these and
          additional limits, see `IAM and STS Character Limits
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-limits.html#reference_iam-limits-entity-length>`__
          in the *IAM User Guide* .

          .. note::

            An AWS conversion compresses the passed session policies and session tags into a packed
            binary format that has a separate limit. Your request can fail for this limit even if
            your plain text meets the other requirements. The ``PackedPolicySize`` response element
            indicates by percentage how close the policies and tags for your request are to the
            upper size limit.

          You can pass a session tag with the same key as a tag that is already attached to the user
          you are federating. When you do, session tags override a user tag with the same key.

          Tag key–value pairs are not case sensitive, but case is preserved. This means that you
          cannot have separate ``Department`` and ``department`` tag keys. Assume that the role has
          the ``Department`` =``Marketing`` tag and you pass the ``department`` =``engineering``
          session tag. ``Department`` and ``department`` are not saved as separate tags, and the
          session tag passed in the request takes precedence over the role tag.

          - *(dict) --*

            You can pass custom key-value pair attributes when you assume a role or federate a user.
            These are called session tags. You can then use the session tags to control access to
            resources. For more information, see `Tagging AWS STS Sessions
            <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_session-tags.html>`__ in the *IAM
            User Guide* .

            - **Key** *(string) --* **[REQUIRED]**

              The key for a session tag.

              You can pass up to 50 session tags. The plain text session tag keys can’t exceed 128
              characters. For these and additional limits, see `IAM and STS Character Limits
              <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-limits.html#reference_iam-limits-entity-length>`__
              in the *IAM User Guide* .

            - **Value** *(string) --* **[REQUIRED]**

              The value for a session tag.

              You can pass up to 50 session tags. The plain text session tag values can’t exceed 256
              characters. For these and additional limits, see `IAM and STS Character Limits
              <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_iam-limits.html#reference_iam-limits-entity-length>`__
              in the *IAM User Guide* .

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Credentials': {
                    'AccessKeyId': 'string',
                    'SecretAccessKey': 'string',
                    'SessionToken': 'string',
                    'Expiration': datetime(2015, 1, 1)
                },
                'FederatedUser': {
                    'FederatedUserId': 'string',
                    'Arn': 'string'
                },
                'PackedPolicySize': 123
            }
          **Response Structure**

          - *(dict) --*

            Contains the response to a successful  GetFederationToken request, including temporary
            AWS credentials that can be used to make AWS requests.

            - **Credentials** *(dict) --*

              The temporary security credentials, which include an access key ID, a secret access
              key, and a security (or session) token.

              .. note::

                The size of the security token that STS API operations return is not fixed. We
                strongly recommend that you make no assumptions about the maximum size.

              - **AccessKeyId** *(string) --*

                The access key ID that identifies the temporary security credentials.

              - **SecretAccessKey** *(string) --*

                The secret access key that can be used to sign requests.

              - **SessionToken** *(string) --*

                The token that users must pass to the service API to use the temporary credentials.

              - **Expiration** *(datetime) --*

                The date on which the current credentials expire.

            - **FederatedUser** *(dict) --*

              Identifiers for the federated user associated with the credentials (such as
              ``arn:aws:sts::123456789012:federated-user/Bob`` or ``123456789012:Bob`` ). You can
              use the federated user's ARN in your resource-based policies, such as an Amazon S3
              bucket policy.

              - **FederatedUserId** *(string) --*

                The string that identifies the federated user associated with the credentials,
                similar to the unique ID of an IAM user.

              - **Arn** *(string) --*

                The ARN that specifies the federated user that is associated with the credentials.
                For more information about ARNs and how to use them in policies, see `IAM
                Identifiers
                <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html>`__ in
                the *IAM User Guide* .

            - **PackedPolicySize** *(integer) --*

              A percentage value that indicates the packed size of the session policies and session
              tags combined passed in the request. The request fails if the packed size is greater
              than 100 percent, which means the policies and tags exceeded the allowed space.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_session_token(
        self, DurationSeconds: int = None, SerialNumber: str = None, TokenCode: str = None
    ) -> ClientGetSessionTokenResponseTypeDef:
        """
        Returns a set of temporary credentials for an AWS account or IAM user. The credentials
        consist of an access key ID, a secret access key, and a security token. Typically, you use
        ``GetSessionToken`` if you want to use MFA to protect programmatic calls to specific AWS API
        operations like Amazon EC2 ``StopInstances`` . MFA-enabled IAM users would need to call
        ``GetSessionToken`` and submit an MFA code that is associated with their MFA device. Using
        the temporary security credentials that are returned from the call, IAM users can then make
        programmatic calls to API operations that require MFA authentication. If you do not supply a
        correct MFA code, then the API returns an access denied error. For a comparison of
        ``GetSessionToken`` with the other API operations that produce temporary credentials, see
        `Requesting Temporary Security Credentials
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_request.html>`__ and
        `Comparing the AWS STS API operations
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_request.html#stsapi_comparison>`__
        in the *IAM User Guide* .

         **Session Duration**

        The ``GetSessionToken`` operation must be called by using the long-term AWS security
        credentials of the AWS account root user or an IAM user. Credentials that are created by IAM
        users are valid for the duration that you specify. This duration can range from 900 seconds
        (15 minutes) up to a maximum of 129,600 seconds (36 hours), with a default of 43,200 seconds
        (12 hours). Credentials based on account credentials can range from 900 seconds (15 minutes)
        up to 3,600 seconds (1 hour), with a default of 1 hour.

         **Permissions**

        The temporary security credentials created by ``GetSessionToken`` can be used to make API
        calls to any AWS service with the following exceptions:

        * You cannot call any IAM API operations unless MFA authentication information is included
        in the request.

        * You cannot call any STS API *except*  ``AssumeRole`` or ``GetCallerIdentity`` .

        .. note::

          We recommend that you do not call ``GetSessionToken`` with AWS account root user
          credentials. Instead, follow our `best practices
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#create-iam-users>`__
          by creating one or more IAM users, giving them the necessary permissions, and using IAM
          users for everyday interaction with AWS.

        The credentials that are returned by ``GetSessionToken`` are based on permissions associated
        with the user whose credentials were used to call the operation. If ``GetSessionToken`` is
        called using AWS account root user credentials, the temporary credentials have root user
        permissions. Similarly, if ``GetSessionToken`` is called using the credentials of an IAM
        user, the temporary credentials have the same permissions as the IAM user.

        For more information about using ``GetSessionToken`` to create temporary credentials, go to
        `Temporary Credentials for Users in Untrusted Environments
        <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_request.html#api_getsessiontoken>`__
        in the *IAM User Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/sts-2011-06-15/GetSessionToken>`_

        **Request Syntax**
        ::

          response = client.get_session_token(
              DurationSeconds=123,
              SerialNumber='string',
              TokenCode='string'
          )
        :type DurationSeconds: integer
        :param DurationSeconds:

          The duration, in seconds, that the credentials should remain valid. Acceptable durations
          for IAM user sessions range from 900 seconds (15 minutes) to 129,600 seconds (36 hours),
          with 43,200 seconds (12 hours) as the default. Sessions for AWS account owners are
          restricted to a maximum of 3,600 seconds (one hour). If the duration is longer than one
          hour, the session for AWS account owners defaults to one hour.

        :type SerialNumber: string
        :param SerialNumber:

          The identification number of the MFA device that is associated with the IAM user who is
          making the ``GetSessionToken`` call. Specify this value if the IAM user has a policy that
          requires MFA authentication. The value is either the serial number for a hardware device
          (such as ``GAHT12345678`` ) or an Amazon Resource Name (ARN) for a virtual device (such as
          ``arn:aws:iam::123456789012:mfa/user`` ). You can find the device for an IAM user by going
          to the AWS Management Console and viewing the user's security credentials.

          The regex used to validate this parameter is a string of characters consisting of upper-
          and lower-case alphanumeric characters with no spaces. You can also include underscores or
          any of the following characters: =,.@:/-

        :type TokenCode: string
        :param TokenCode:

          The value provided by the MFA device, if MFA is required. If any policy requires the IAM
          user to submit an MFA code, specify this value. If MFA authentication is required, the
          user must provide a code when requesting a set of temporary security credentials. A user
          who fails to provide the code receives an "access denied" response when requesting
          resources that require MFA authentication.

          The format for this parameter, as described by its regex pattern, is a sequence of six
          numeric digits.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Credentials': {
                    'AccessKeyId': 'string',
                    'SecretAccessKey': 'string',
                    'SessionToken': 'string',
                    'Expiration': datetime(2015, 1, 1)
                }
            }
          **Response Structure**

          - *(dict) --*

            Contains the response to a successful  GetSessionToken request, including temporary AWS
            credentials that can be used to make AWS requests.

            - **Credentials** *(dict) --*

              The temporary security credentials, which include an access key ID, a secret access
              key, and a security (or session) token.

              .. note::

                The size of the security token that STS API operations return is not fixed. We
                strongly recommend that you make no assumptions about the maximum size.

              - **AccessKeyId** *(string) --*

                The access key ID that identifies the temporary security credentials.

              - **SecretAccessKey** *(string) --*

                The secret access key that can be used to sign requests.

              - **SessionToken** *(string) --*

                The token that users must pass to the service API to use the temporary credentials.

              - **Expiration** *(datetime) --*

                The date on which the current credentials expire.
        """


class Exceptions:
    ClientError: Boto3ClientError
    ExpiredTokenException: Boto3ClientError
    IDPCommunicationErrorException: Boto3ClientError
    IDPRejectedClaimException: Boto3ClientError
    InvalidAuthorizationMessageException: Boto3ClientError
    InvalidIdentityTokenException: Boto3ClientError
    MalformedPolicyDocumentException: Boto3ClientError
    PackedPolicyTooLargeException: Boto3ClientError
    RegionDisabledException: Boto3ClientError
