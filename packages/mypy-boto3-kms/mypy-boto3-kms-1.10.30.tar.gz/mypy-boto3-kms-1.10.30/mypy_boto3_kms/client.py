"Main interface for kms service Client"
from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3.type_defs import Literal, overload

# pylint: disable=import-self
import mypy_boto3_kms.client as client_scope

# pylint: disable=import-self
import mypy_boto3_kms.paginator as paginator_scope
from mypy_boto3_kms.type_defs import (
    ClientCancelKeyDeletionResponseTypeDef,
    ClientCreateCustomKeyStoreResponseTypeDef,
    ClientCreateGrantConstraintsTypeDef,
    ClientCreateGrantResponseTypeDef,
    ClientCreateKeyResponseTypeDef,
    ClientCreateKeyTagsTypeDef,
    ClientDecryptResponseTypeDef,
    ClientDescribeCustomKeyStoresResponseTypeDef,
    ClientDescribeKeyResponseTypeDef,
    ClientEncryptResponseTypeDef,
    ClientGenerateDataKeyPairResponseTypeDef,
    ClientGenerateDataKeyPairWithoutPlaintextResponseTypeDef,
    ClientGenerateDataKeyResponseTypeDef,
    ClientGenerateDataKeyWithoutPlaintextResponseTypeDef,
    ClientGenerateRandomResponseTypeDef,
    ClientGetKeyPolicyResponseTypeDef,
    ClientGetKeyRotationStatusResponseTypeDef,
    ClientGetParametersForImportResponseTypeDef,
    ClientGetPublicKeyResponseTypeDef,
    ClientListAliasesResponseTypeDef,
    ClientListGrantsResponseTypeDef,
    ClientListKeyPoliciesResponseTypeDef,
    ClientListKeysResponseTypeDef,
    ClientListResourceTagsResponseTypeDef,
    ClientListRetirableGrantsResponseTypeDef,
    ClientReEncryptResponseTypeDef,
    ClientScheduleKeyDeletionResponseTypeDef,
    ClientSignResponseTypeDef,
    ClientTagResourceTagsTypeDef,
    ClientVerifyResponseTypeDef,
)


__all__ = ("Client",)


class Client(BaseClient):
    exceptions: client_scope.Exceptions

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
    def cancel_key_deletion(self, KeyId: str) -> ClientCancelKeyDeletionResponseTypeDef:
        """
        Cancels the deletion of a customer master key (CMK). When this operation succeeds, the key
        state of the CMK is ``Disabled`` . To enable the CMK, use  EnableKey . You cannot perform
        this operation on a CMK in a different AWS account.

        For more information about scheduling and canceling deletion of a CMK, see `Deleting
        Customer Master Keys
        <https://docs.aws.amazon.com/kms/latest/developerguide/deleting-keys.html>`__ in the *AWS
        Key Management Service Developer Guide* .

        The CMK that you use for this operation must be in a compatible key state. For details, see
        `How Key State Affects Use of a Customer Master Key
        <https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`__ in the *AWS Key
        Management Service Developer Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/CancelKeyDeletion>`_

        **Request Syntax**
        ::

          response = client.cancel_key_deletion(
              KeyId='string'
          )
        :type KeyId: string
        :param KeyId: **[REQUIRED]**

          The unique identifier for the customer master key (CMK) for which to cancel deletion.

          Specify the key ID or the Amazon Resource Name (ARN) of the CMK.

          For example:

          * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``

          * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``

          To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey .

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'KeyId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **KeyId** *(string) --*

              The unique identifier of the master key for which deletion is canceled.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def connect_custom_key_store(self, CustomKeyStoreId: str) -> Dict[str, Any]:
        """
        Connects or reconnects a `custom key store
        <https://docs.aws.amazon.com/kms/latest/developerguide/custom-key-store-overview.html>`__ to
        its associated AWS CloudHSM cluster.

        The custom key store must be connected before you can create customer master keys (CMKs) in
        the key store or use the CMKs it contains. You can disconnect and reconnect a custom key
        store at any time.

        To connect a custom key store, its associated AWS CloudHSM cluster must have at least one
        active HSM. To get the number of active HSMs in a cluster, use the `DescribeClusters
        <https://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_DescribeClusters.html>`__
        operation. To add HSMs to the cluster, use the `CreateHsm
        <https://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_CreateHsm.html>`__ operation.

        The connection process can take an extended amount of time to complete; up to 20 minutes.
        This operation starts the connection process, but it does not wait for it to complete. When
        it succeeds, this operation quickly returns an HTTP 200 response and a JSON object with no
        properties. However, this response does not indicate that the custom key store is connected.
        To get the connection state of the custom key store, use the  DescribeCustomKeyStores
        operation.

        During the connection process, AWS KMS finds the AWS CloudHSM cluster that is associated
        with the custom key store, creates the connection infrastructure, connects to the cluster,
        logs into the AWS CloudHSM client as the ` ``kmsuser`` crypto user
        <https://docs.aws.amazon.com/kms/latest/developerguide/key-store-concepts.html#concept-kmsuser>`__
        (CU), and rotates its password.

        The ``ConnectCustomKeyStore`` operation might fail for various reasons. To find the reason,
        use the  DescribeCustomKeyStores operation and see the ``ConnectionErrorCode`` in the
        response. For help interpreting the ``ConnectionErrorCode`` , see  CustomKeyStoresListEntry
        .

        To fix the failure, use the  DisconnectCustomKeyStore operation to disconnect the custom key
        store, correct the error, use the  UpdateCustomKeyStore operation if necessary, and then use
        ``ConnectCustomKeyStore`` again.

        If you are having trouble connecting or disconnecting a custom key store, see
        `Troubleshooting a Custom Key Store
        <https://docs.aws.amazon.com/kms/latest/developerguide/fix-keystore.html>`__ in the *AWS Key
        Management Service Developer Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/ConnectCustomKeyStore>`_

        **Request Syntax**
        ::

          response = client.connect_custom_key_store(
              CustomKeyStoreId='string'
          )
        :type CustomKeyStoreId: string
        :param CustomKeyStoreId: **[REQUIRED]**

          Enter the key store ID of the custom key store that you want to connect. To find the ID of
          a custom key store, use the  DescribeCustomKeyStores operation.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_alias(self, AliasName: str, TargetKeyId: str) -> None:
        """
        Creates a display name for a customer managed customer master key (CMK). You can use an
        alias to identify a CMK in cryptographic operations, such as  Encrypt and  GenerateDataKey .
        You can change the CMK associated with the alias at any time.

        Aliases are easier to remember than key IDs. They can also help to simplify your
        applications. For example, if you use an alias in your code, you can change the CMK your
        code uses by associating a given alias with a different CMK.

        To run the same code in multiple AWS regions, use an alias in your code, such as
        ``alias/ApplicationKey`` . Then, in each AWS Region, create an ``alias/ApplicationKey``
        alias that is associated with a CMK in that Region. When you run your code, it uses the
        ``alias/ApplicationKey`` CMK for that AWS Region without any Region-specific code.

        This operation does not return a response. To get the alias that you created, use the
        ListAliases operation.

        To use aliases successfully, be aware of the following information.

        * Each alias points to only one CMK at a time, although a single CMK can have multiple
        aliases. The alias and its associated CMK must be in the same AWS account and Region.

        * You can associate an alias with any customer managed CMK in the same AWS account and
        Region. However, you do not have permission to associate an alias with an `AWS managed CMK
        <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk>`__ or
        an `AWS owned CMK
        <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-owned-cmk>`__ .

        * To change the CMK associated with an alias, use the  UpdateAlias operation. The current
        CMK and the new CMK must be the same type (both symmetric or both asymmetric) and they must
        have the same key usage (``ENCRYPT_DECRYPT`` or ``SIGN_VERIFY`` ). This restriction prevents
        cryptographic errors in code that uses aliases.

        * The alias name must begin with ``alias/`` followed by a name, such as
        ``alias/ExampleAlias`` . It can contain only alphanumeric characters, forward slashes (/),
        underscores (_), and dashes (-). The alias name cannot begin with ``alias/aws/`` . The
        ``alias/aws/`` prefix is reserved for `AWS managed CMKs
        <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk>`__ .

        * The alias name must be unique within an AWS Region. However, you can use the same alias
        name in multiple Regions of the same AWS account. Each instance of the alias is associated
        with a CMK in its Region.

        * After you create an alias, you cannot change its alias name. However, you can use the
        DeleteAlias operation to delete the alias and then create a new alias with the desired name.

        * You can use an alias name or alias ARN to identify a CMK in AWS KMS cryptographic
        operations and in the  DescribeKey operation. However, you cannot use alias names or alias
        ARNs in API operations that manage CMKs, such as  DisableKey or  GetKeyPolicy . For
        information about the valid CMK identifiers for each AWS KMS API operation, see the
        descriptions of the ``KeyId`` parameter in the API operation documentation.

        Because an alias is not a property of a CMK, you can delete and change the aliases of a CMK
        without affecting the CMK. Also, aliases do not appear in the response from the  DescribeKey
        operation. To get the aliases and alias ARNs of CMKs in each AWS account and Region, use the
        ListAliases operation.

        The CMK that you use for this operation must be in a compatible key state. For details, see
        `How Key State Affects Use of a Customer Master Key
        <https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`__ in the *AWS Key
        Management Service Developer Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/CreateAlias>`_

        **Request Syntax**
        ::

          response = client.create_alias(
              AliasName='string',
              TargetKeyId='string'
          )
        :type AliasName: string
        :param AliasName: **[REQUIRED]**

          Specifies the alias name. This value must begin with ``alias/`` followed by a name, such
          as ``alias/ExampleAlias`` . The alias name cannot begin with ``alias/aws/`` . The
          ``alias/aws/`` prefix is reserved for AWS managed CMKs.

        :type TargetKeyId: string
        :param TargetKeyId: **[REQUIRED]**

          Identifies the CMK to which the alias refers. Specify the key ID or the Amazon Resource
          Name (ARN) of the CMK. You cannot specify another alias. For help finding the key ID and
          ARN, see `Finding the Key ID and ARN
          <https://docs.aws.amazon.com/kms/latest/developerguide/viewing-keys.html#find-cmk-id-arn>`__
          in the *AWS Key Management Service Developer Guide* .

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_custom_key_store(
        self,
        CustomKeyStoreName: str,
        CloudHsmClusterId: str,
        TrustAnchorCertificate: str,
        KeyStorePassword: str,
    ) -> ClientCreateCustomKeyStoreResponseTypeDef:
        """
        Creates a `custom key store
        <https://docs.aws.amazon.com/kms/latest/developerguide/custom-key-store-overview.html>`__
        that is associated with an `AWS CloudHSM cluster
        <https://docs.aws.amazon.com/cloudhsm/latest/userguide/clusters.html>`__ that you own and
        manage.

        This operation is part of the `Custom Key Store feature
        <https://docs.aws.amazon.com/kms/latest/developerguide/custom-key-store-overview.html>`__
        feature in AWS KMS, which combines the convenience and extensive integration of AWS KMS with
        the isolation and control of a single-tenant key store.

        Before you create the custom key store, you must assemble the required elements, including
        an AWS CloudHSM cluster that fulfills the requirements for a custom key store. For details
        about the required elements, see `Assemble the Prerequisites
        <https://docs.aws.amazon.com/kms/latest/developerguide/create-keystore.html#before-keystore>`__
        in the *AWS Key Management Service Developer Guide* .

        When the operation completes successfully, it returns the ID of the new custom key store.
        Before you can use your new custom key store, you need to use the  ConnectCustomKeyStore
        operation to connect the new key store to its AWS CloudHSM cluster. Even if you are not
        going to use your custom key store immediately, you might want to connect it to verify that
        all settings are correct and then disconnect it until you are ready to use it.

        For help with failures, see `Troubleshooting a Custom Key Store
        <https://docs.aws.amazon.com/kms/latest/developerguide/fix-keystore.html>`__ in the *AWS Key
        Management Service Developer Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/CreateCustomKeyStore>`_

        **Request Syntax**
        ::

          response = client.create_custom_key_store(
              CustomKeyStoreName='string',
              CloudHsmClusterId='string',
              TrustAnchorCertificate='string',
              KeyStorePassword='string'
          )
        :type CustomKeyStoreName: string
        :param CustomKeyStoreName: **[REQUIRED]**

          Specifies a friendly name for the custom key store. The name must be unique in your AWS
          account.

        :type CloudHsmClusterId: string
        :param CloudHsmClusterId: **[REQUIRED]**

          Identifies the AWS CloudHSM cluster for the custom key store. Enter the cluster ID of any
          active AWS CloudHSM cluster that is not already associated with a custom key store. To
          find the cluster ID, use the `DescribeClusters
          <https://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_DescribeClusters.html>`__
          operation.

        :type TrustAnchorCertificate: string
        :param TrustAnchorCertificate: **[REQUIRED]**

          Enter the content of the trust anchor certificate for the cluster. This is the content of
          the ``customerCA.crt`` file that you created when you `initialized the cluster
          <https://docs.aws.amazon.com/cloudhsm/latest/userguide/initialize-cluster.html>`__ .

        :type KeyStorePassword: string
        :param KeyStorePassword: **[REQUIRED]**

          Enter the password of the ` ``kmsuser`` crypto user (CU) account
          <https://docs.aws.amazon.com/kms/latest/developerguide/key-store-concepts.html#concept-kmsuser>`__
          in the specified AWS CloudHSM cluster. AWS KMS logs into the cluster as this user to
          manage key material on your behalf.

          This parameter tells AWS KMS the ``kmsuser`` account password; it does not change the
          password in the AWS CloudHSM cluster.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'CustomKeyStoreId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **CustomKeyStoreId** *(string) --*

              A unique identifier for the new custom key store.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_grant(
        self,
        KeyId: str,
        GranteePrincipal: str,
        Operations: List[
            Literal[
                "Decrypt",
                "Encrypt",
                "GenerateDataKey",
                "GenerateDataKeyWithoutPlaintext",
                "ReEncryptFrom",
                "ReEncryptTo",
                "Sign",
                "Verify",
                "GetPublicKey",
                "CreateGrant",
                "RetireGrant",
                "DescribeKey",
                "GenerateDataKeyPair",
                "GenerateDataKeyPairWithoutPlaintext",
            ]
        ],
        RetiringPrincipal: str = None,
        Constraints: ClientCreateGrantConstraintsTypeDef = None,
        GrantTokens: List[str] = None,
        Name: str = None,
    ) -> ClientCreateGrantResponseTypeDef:
        """
        Adds a grant to a customer master key (CMK). The grant allows the grantee principal to use
        the CMK when the conditions specified in the grant are met. When setting permissions, grants
        are an alternative to key policies.

        To create a grant that allows a cryptographic operation only when the request includes a
        particular `encryption context
        <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#encrypt_context>`__ ,
        use the ``Constraints`` parameter. For details, see  GrantConstraints .

        You can create grants on symmetric and asymmetric CMKs. However, if the grant allows an
        operation that the CMK does not support, ``CreateGrant`` fails with a
        ``ValidationException`` .

        * Grants for symmetric CMKs cannot allow operations that are not supported for symmetric
        CMKs, including  Sign ,  Verify , and  GetPublicKey . (There are limited exceptions to this
        rule for legacy operations, but you should not create a grant for an operation that AWS KMS
        does not support.)

        * Grants for asymmetric CMKs cannot allow operations that are not supported for asymmetric
        CMKs, including operations that `generate data keys
        <https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKey>`__ or `data key
        pairs <https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKeyPair>`__ , or
        operations related to `automatic key rotation
        <https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html>`__ , `imported key
        material <https://docs.aws.amazon.com/kms/latest/developerguide/importing-keys.html>`__ , or
        CMKs in `custom key stores
        <https://docs.aws.amazon.com/kms/latest/developerguide/custom-key-store-overview.html>`__ .

        * Grants for asymmetric CMKs with a ``KeyUsage`` of ``ENCRYPT_DECRYPT`` cannot allow the
        Sign or  Verify operations. Grants for asymmetric CMKs with a ``KeyUsage`` of
        ``SIGN_VERIFY`` cannot allow the  Encrypt or  Decrypt operations.

        * Grants for asymmetric CMKs cannot include an encryption context grant constraint. An
        encryption context is not supported on asymmetric CMKs.

        For information about symmetric and asymmetric CMKs, see `Using Symmetric and Asymmetric
        CMKs <https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html>`__ in
        the *AWS Key Management Service Developer Guide* .

        To perform this operation on a CMK in a different AWS account, specify the key ARN in the
        value of the ``KeyId`` parameter. For more information about grants, see `Grants
        <https://docs.aws.amazon.com/kms/latest/developerguide/grants.html>`__ in the * *AWS Key
        Management Service Developer Guide* * .

        The CMK that you use for this operation must be in a compatible key state. For details, see
        `How Key State Affects Use of a Customer Master Key
        <https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`__ in the *AWS Key
        Management Service Developer Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/CreateGrant>`_

        **Request Syntax**
        ::

          response = client.create_grant(
              KeyId='string',
              GranteePrincipal='string',
              RetiringPrincipal='string',
              Operations=[
                  'Decrypt'|'Encrypt'|'GenerateDataKey'|'GenerateDataKeyWithoutPlaintext'
                  |'ReEncryptFrom'|'ReEncryptTo'|'Sign'|'Verify'|'GetPublicKey'|'CreateGrant'
                  |'RetireGrant'|'DescribeKey'|'GenerateDataKeyPair'
                  |'GenerateDataKeyPairWithoutPlaintext',
              ],
              Constraints={
                  'EncryptionContextSubset': {
                      'string': 'string'
                  },
                  'EncryptionContextEquals': {
                      'string': 'string'
                  }
              },
              GrantTokens=[
                  'string',
              ],
              Name='string'
          )
        :type KeyId: string
        :param KeyId: **[REQUIRED]**

          The unique identifier for the customer master key (CMK) that the grant applies to.

          Specify the key ID or the Amazon Resource Name (ARN) of the CMK. To specify a CMK in a
          different AWS account, you must use the key ARN.

          For example:

          * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``

          * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``

          To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey .

        :type GranteePrincipal: string
        :param GranteePrincipal: **[REQUIRED]**

          The principal that is given permission to perform the operations that the grant permits.

          To specify the principal, use the `Amazon Resource Name (ARN)
          <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ of an AWS
          principal. Valid AWS principals include AWS accounts (root), IAM users, IAM roles,
          federated users, and assumed role users. For examples of the ARN syntax to use for
          specifying a principal, see `AWS Identity and Access Management (IAM)
          <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-iam>`__
          in the Example ARNs section of the *AWS General Reference* .

        :type RetiringPrincipal: string
        :param RetiringPrincipal:

          The principal that is given permission to retire the grant by using  RetireGrant
          operation.

          To specify the principal, use the `Amazon Resource Name (ARN)
          <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ of an AWS
          principal. Valid AWS principals include AWS accounts (root), IAM users, federated users,
          and assumed role users. For examples of the ARN syntax to use for specifying a principal,
          see `AWS Identity and Access Management (IAM)
          <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-iam>`__
          in the Example ARNs section of the *AWS General Reference* .

        :type Operations: list
        :param Operations: **[REQUIRED]**

          A list of operations that the grant permits.

          - *(string) --*

        :type Constraints: dict
        :param Constraints:

          Allows a cryptographic operation only when the encryption context matches or includes the
          encryption context specified in this structure. For more information about encryption
          context, see `Encryption Context
          <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#encrypt_context>`__
          in the * *AWS Key Management Service Developer Guide* * .

          - **EncryptionContextSubset** *(dict) --*

            A list of key-value pairs that must be included in the encryption context of the
            cryptographic operation request. The grant allows the cryptographic operation only when
            the encryption context in the request includes the key-value pairs specified in this
            constraint, although it can include additional key-value pairs.

            - *(string) --*

              - *(string) --*

          - **EncryptionContextEquals** *(dict) --*

            A list of key-value pairs that must match the encryption context in the cryptographic
            operation request. The grant allows the operation only when the encryption context in
            the request is the same as the encryption context specified in this constraint.

            - *(string) --*

              - *(string) --*

        :type GrantTokens: list
        :param GrantTokens:

          A list of grant tokens.

          For more information, see `Grant Tokens
          <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token>`__ in
          the *AWS Key Management Service Developer Guide* .

          - *(string) --*

        :type Name: string
        :param Name:

          A friendly name for identifying the grant. Use this value to prevent the unintended
          creation of duplicate grants when retrying this request.

          When this value is absent, all ``CreateGrant`` requests result in a new grant with a
          unique ``GrantId`` even if all the supplied parameters are identical. This can result in
          unintended duplicates when you retry the ``CreateGrant`` request.

          When this value is present, you can retry a ``CreateGrant`` request with identical
          parameters; if the grant already exists, the original ``GrantId`` is returned without
          creating a new grant. Note that the returned grant token is unique with every
          ``CreateGrant`` request, even when a duplicate ``GrantId`` is returned. All grant tokens
          obtained in this way can be used interchangeably.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'GrantToken': 'string',
                'GrantId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **GrantToken** *(string) --*

              The grant token.

              For more information, see `Grant Tokens
              <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token>`__
              in the *AWS Key Management Service Developer Guide* .

            - **GrantId** *(string) --*

              The unique identifier for the grant.

              You can use the ``GrantId`` in a subsequent  RetireGrant or  RevokeGrant operation.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def create_key(
        self,
        Policy: str = None,
        Description: str = None,
        KeyUsage: Literal["SIGN_VERIFY", "ENCRYPT_DECRYPT"] = None,
        CustomerMasterKeySpec: Literal[
            "RSA_2048",
            "RSA_3072",
            "RSA_4096",
            "ECC_NIST_P256",
            "ECC_NIST_P384",
            "ECC_NIST_P521",
            "ECC_SECG_P256K1",
            "SYMMETRIC_DEFAULT",
        ] = None,
        Origin: Literal["AWS_KMS", "EXTERNAL", "AWS_CLOUDHSM"] = None,
        CustomKeyStoreId: str = None,
        BypassPolicyLockoutSafetyCheck: bool = None,
        Tags: List[ClientCreateKeyTagsTypeDef] = None,
    ) -> ClientCreateKeyResponseTypeDef:
        """
        Creates a unique customer managed `customer master key
        <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#master-keys>`__ (CMK)
        in your AWS account and Region. You cannot use this operation to create a CMK in a different
        AWS account.

        You can use the ``CreateKey`` operation to create symmetric or asymmetric CMKs.

        * **Symmetric CMKs** contain a 256-bit symmetric key that never leaves AWS KMS unencrypted.
        To use the CMK, you must call AWS KMS. You can use a symmetric CMK to encrypt and decrypt
        small amounts of data, but they are typically used to generate `data keys
        <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#data-keys>`__ or data
        key pairs. For details, see  GenerateDataKey and  GenerateDataKeyPair .

        * **Asymmetric CMKs** can contain an RSA key pair or an Elliptic Curve (ECC) key pair. The
        private key in an asymmetric CMK never leaves AWS KMS unencrypted. However, you can use the
        GetPublicKey operation to download the public key so it can be used outside of AWS KMS. CMKs
        with RSA key pairs can be used to encrypt or decrypt data or sign and verify messages (but
        not both). CMKs with ECC key pairs can be used only to sign and verify messages.

        For information about symmetric and asymmetric CMKs, see `Using Symmetric and Asymmetric
        CMKs <https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html>`__ in
        the *AWS Key Management Service Developer Guide* .

        To create different types of CMKs, use the following guidance:

          Asymmetric CMKs

        To create an asymmetric CMK, use the ``CustomerMasterKeySpec`` parameter to specify the type
        of key material in the CMK. Then, use the ``KeyUsage`` parameter to determine whether the
        CMK will be used to encrypt and decrypt or sign and verify. You can't change these
        properties after the CMK is created.

          Symmetric CMKs

        When creating a symmetric CMK, you don't need to specify the ``CustomerMasterKeySpec`` or
        ``KeyUsage`` parameters. The default value for ``CustomerMasterKeySpec`` ,
        ``SYMMETRIC_DEFAULT`` , and the default value for ``KeyUsage`` , ``ENCRYPT_DECRYPT`` , are
        the only valid values for symmetric CMKs.

          Imported Key Material

        To import your own key material, begin by creating a symmetric CMK with no key material. To
        do this, use the ``Origin`` parameter of ``CreateKey`` with a value of ``EXTERNAL`` . Next,
        use  GetParametersForImport operation to get a public key and import token, and use the
        public key to encrypt your key material. Then, use  ImportKeyMaterial with your import token
        to import the key material. For step-by-step instructions, see `Importing Key Material
        <https://docs.aws.amazon.com/kms/latest/developerguide/importing-keys.html>`__ in the * *AWS
        Key Management Service Developer Guide* * . You cannot import the key material into an
        asymmetric CMK.

          Custom Key Stores

        To create a symmetric CMK in a `custom key store
        <https://docs.aws.amazon.com/kms/latest/developerguide/custom-key-store-overview.html>`__ ,
        use the ``CustomKeyStoreId`` parameter to specify the custom key store. You must also use
        the ``Origin`` parameter with a value of ``AWS_CLOUDHSM`` . The AWS CloudHSM cluster that is
        associated with the custom key store must have at least two active HSMs in different
        Availability Zones in the AWS Region.

        You cannot create an asymmetric CMK in a custom key store. For information about custom key
        stores in AWS KMS see `Using Custom Key Stores
        <https://docs.aws.amazon.com/kms/latest/developerguide/custom-key-store-overview.html>`__ in
        the * *AWS Key Management Service Developer Guide* * .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/CreateKey>`_

        **Request Syntax**
        ::

          response = client.create_key(
              Policy='string',
              Description='string',
              KeyUsage='SIGN_VERIFY'|'ENCRYPT_DECRYPT',
              CustomerMasterKeySpec=
                  'RSA_2048'|'RSA_3072'|'RSA_4096'|'ECC_NIST_P256'|'ECC_NIST_P384'|'ECC_NIST_P521'
                  |'ECC_SECG_P256K1'|'SYMMETRIC_DEFAULT',
              Origin='AWS_KMS'|'EXTERNAL'|'AWS_CLOUDHSM',
              CustomKeyStoreId='string',
              BypassPolicyLockoutSafetyCheck=True|False,
              Tags=[
                  {
                      'TagKey': 'string',
                      'TagValue': 'string'
                  },
              ]
          )
        :type Policy: string
        :param Policy:

          The key policy to attach to the CMK.

          If you provide a key policy, it must meet the following criteria:

          * If you don't set ``BypassPolicyLockoutSafetyCheck`` to true, the key policy must allow
          the principal that is making the ``CreateKey`` request to make a subsequent  PutKeyPolicy
          request on the CMK. This reduces the risk that the CMK becomes unmanageable. For more
          information, refer to the scenario in the `Default Key Policy
          <https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html#key-policy-default-allow-root-enable-iam>`__
          section of the * *AWS Key Management Service Developer Guide* * .

          * Each statement in the key policy must contain one or more principals. The principals in
          the key policy must exist and be visible to AWS KMS. When you create a new AWS principal
          (for example, an IAM user or role), you might need to enforce a delay before including the
          new principal in a key policy because the new principal might not be immediately visible
          to AWS KMS. For more information, see `Changes that I make are not always immediately
          visible
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_general.html#troubleshoot_general_eventual-consistency>`__
          in the *AWS Identity and Access Management User Guide* .

          If you do not provide a key policy, AWS KMS attaches a default key policy to the CMK. For
          more information, see `Default Key Policy
          <https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html#key-policy-default>`__
          in the *AWS Key Management Service Developer Guide* .

          The key policy size limit is 32 kilobytes (32768 bytes).

        :type Description: string
        :param Description:

          A description of the CMK.

          Use a description that helps you decide whether the CMK is appropriate for a task.

        :type KeyUsage: string
        :param KeyUsage:

          Determines the cryptographic operations for which you can use the CMK. The default value
          is ``ENCRYPT_DECRYPT`` . This parameter is required only for asymmetric CMKs. You can't
          change the ``KeyUsage`` value after the CMK is created.

          Select only one valid value.

          * For symmetric CMKs, omit the parameter or specify ``ENCRYPT_DECRYPT`` .

          * For asymmetric CMKs with RSA key material, specify ``ENCRYPT_DECRYPT`` or
          ``SIGN_VERIFY`` .

          * For asymmetric CMKs with ECC key material, specify ``SIGN_VERIFY`` .

        :type CustomerMasterKeySpec: string
        :param CustomerMasterKeySpec:

          Specifies the type of CMK to create. The ``CustomerMasterKeySpec`` determines whether the
          CMK contains a symmetric key or an asymmetric key pair. It also determines the encryption
          algorithms or signing algorithms that the CMK supports. You can't change the
          ``CustomerMasterKeySpec`` after the CMK is created. To further restrict the algorithms
          that can be used with the CMK, use its key policy or IAM policy.

          For help with choosing a key spec for your CMK, see `Selecting a Customer Master Key Spec
          <https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html#cmk-key-spec>`__
          in the *AWS Key Management Service Developer Guide* .

          The default value, ``SYMMETRIC_DEFAULT`` , creates a CMK with a 256-bit symmetric key.

          AWS KMS supports the following key specs for CMKs:

          * Symmetric key (default)

            * ``SYMMETRIC_DEFAULT`` (AES-256-GCM)

          * Asymmetric RSA key pairs

            * ``RSA_2048``

            * ``RSA_3072``

            * ``RSA_4096``

          * Asymmetric NIST-recommended elliptic curve key pairs

            * ``ECC_NIST_P256`` (secp256r1)

            * ``ECC_NIST_P384`` (secp384r1)

            * ``ECC_NIST_P521`` (secp521r1)

          * Other asymmetric elliptic curve key pairs

            * ``ECC_SECG_P256K1`` (secp256k1), commonly used for cryptocurrencies.

        :type Origin: string
        :param Origin:

          The source of the key material for the CMK. You cannot change the origin after you create
          the CMK. The default is ``AWS_KMS`` , which means AWS KMS creates the key material.

          When the parameter value is ``EXTERNAL`` , AWS KMS creates a CMK without key material so
          that you can import key material from your existing key management infrastructure. For
          more information about importing key material into AWS KMS, see `Importing Key Material
          <https://docs.aws.amazon.com/kms/latest/developerguide/importing-keys.html>`__ in the *AWS
          Key Management Service Developer Guide* . This value is valid only for symmetric CMKs.

          When the parameter value is ``AWS_CLOUDHSM`` , AWS KMS creates the CMK in an AWS KMS
          `custom key store
          <https://docs.aws.amazon.com/kms/latest/developerguide/custom-key-store-overview.html>`__
          and creates its key material in the associated AWS CloudHSM cluster. You must also use the
          ``CustomKeyStoreId`` parameter to identify the custom key store. This value is valid only
          for symmetric CMKs.

        :type CustomKeyStoreId: string
        :param CustomKeyStoreId:

          Creates the CMK in the specified `custom key store
          <https://docs.aws.amazon.com/kms/latest/developerguide/custom-key-store-overview.html>`__
          and the key material in its associated AWS CloudHSM cluster. To create a CMK in a custom
          key store, you must also specify the ``Origin`` parameter with a value of ``AWS_CLOUDHSM``
          . The AWS CloudHSM cluster that is associated with the custom key store must have at least
          two active HSMs, each in a different Availability Zone in the Region.

          This parameter is valid only for symmetric CMKs. You cannot create an asymmetric CMK in a
          custom key store.

          To find the ID of a custom key store, use the  DescribeCustomKeyStores operation.

          The response includes the custom key store ID and the ID of the AWS CloudHSM cluster.

          This operation is part of the `Custom Key Store feature
          <https://docs.aws.amazon.com/kms/latest/developerguide/custom-key-store-overview.html>`__
          feature in AWS KMS, which combines the convenience and extensive integration of AWS KMS
          with the isolation and control of a single-tenant key store.

        :type BypassPolicyLockoutSafetyCheck: boolean
        :param BypassPolicyLockoutSafetyCheck:

          A flag to indicate whether to bypass the key policy lockout safety check.

          .. warning::

            Setting this value to true increases the risk that the CMK becomes unmanageable. Do not
            set this value to true indiscriminately.

            For more information, refer to the scenario in the `Default Key Policy
            <https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html#key-policy-default-allow-root-enable-iam>`__
            section in the * *AWS Key Management Service Developer Guide* * .

          Use this parameter only when you include a policy in the request and you intend to prevent
          the principal that is making the request from making a subsequent  PutKeyPolicy request on
          the CMK.

          The default value is false.

        :type Tags: list
        :param Tags:

          One or more tags. Each tag consists of a tag key and a tag value. Both the tag key and the
          tag value are required, but the tag value can be an empty (null) string.

          When you add tags to an AWS resource, AWS generates a cost allocation report with usage
          and costs aggregated by tags. For information about adding, changing, deleting and listing
          tags for CMKs, see `Tagging Keys
          <https://docs.aws.amazon.com/kms/latest/developerguide/tagging-keys.html>`__ .

          Use this parameter to tag the CMK when it is created. To add tags to an existing CMK, use
          the  TagResource operation.

          - *(dict) --*

            A key-value pair. A tag consists of a tag key and a tag value. Tag keys and tag values
            are both required, but tag values can be empty (null) strings.

            For information about the rules that apply to tag keys and tag values, see `User-Defined
            Tag Restrictions
            <https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/allocation-tag-restrictions.html>`__
            in the *AWS Billing and Cost Management User Guide* .

            - **TagKey** *(string) --* **[REQUIRED]**

              The key of the tag.

            - **TagValue** *(string) --* **[REQUIRED]**

              The value of the tag.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'KeyMetadata': {
                    'AWSAccountId': 'string',
                    'KeyId': 'string',
                    'Arn': 'string',
                    'CreationDate': datetime(2015, 1, 1),
                    'Enabled': True|False,
                    'Description': 'string',
                    'KeyUsage': 'SIGN_VERIFY'|'ENCRYPT_DECRYPT',
                    'KeyState':
                    'Enabled'|'Disabled'|'PendingDeletion'|'PendingImport'
                    |'Unavailable',
                    'DeletionDate': datetime(2015, 1, 1),
                    'ValidTo': datetime(2015, 1, 1),
                    'Origin': 'AWS_KMS'|'EXTERNAL'|'AWS_CLOUDHSM',
                    'CustomKeyStoreId': 'string',
                    'CloudHsmClusterId': 'string',
                    'ExpirationModel': 'KEY_MATERIAL_EXPIRES'|'KEY_MATERIAL_DOES_NOT_EXPIRE',
                    'KeyManager': 'AWS'|'CUSTOMER',
                    'CustomerMasterKeySpec':
                    'RSA_2048'|'RSA_3072'|'RSA_4096'|'ECC_NIST_P256'|'ECC_NIST_P384'
                    |'ECC_NIST_P521'|'ECC_SECG_P256K1'|'SYMMETRIC_DEFAULT',
                    'EncryptionAlgorithms': [
                        'SYMMETRIC_DEFAULT'|'RSAES_OAEP_SHA_1'|'RSAES_OAEP_SHA_256',
                    ],
                    'SigningAlgorithms': [
                        'RSASSA_PSS_SHA_256'|'RSASSA_PSS_SHA_384'|'RSASSA_PSS_SHA_512'
                        |'RSASSA_PKCS1_V1_5_SHA_256'|'RSASSA_PKCS1_V1_5_SHA_384'
                        |'RSASSA_PKCS1_V1_5_SHA_512'|'ECDSA_SHA_256'|'ECDSA_SHA_384'
                        |'ECDSA_SHA_512',
                    ]
                }
            }
          **Response Structure**

          - *(dict) --*

            - **KeyMetadata** *(dict) --*

              Metadata associated with the CMK.

              - **AWSAccountId** *(string) --*

                The twelve-digit account ID of the AWS account that owns the CMK.

              - **KeyId** *(string) --*

                The globally unique identifier for the CMK.

              - **Arn** *(string) --*

                The Amazon Resource Name (ARN) of the CMK. For examples, see `AWS Key Management
                Service (AWS KMS)
                <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-kms>`__
                in the Example ARNs section of the *AWS General Reference* .

              - **CreationDate** *(datetime) --*

                The date and time when the CMK was created.

              - **Enabled** *(boolean) --*

                Specifies whether the CMK is enabled. When ``KeyState`` is ``Enabled`` this value is
                true, otherwise it is false.

              - **Description** *(string) --*

                The description of the CMK.

              - **KeyUsage** *(string) --*

                The cryptographic operations for which you can use the CMK.

              - **KeyState** *(string) --*

                The state of the CMK.

                For more information about how key state affects the use of a CMK, see `How Key
                State Affects the Use of a Customer Master Key
                <https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`__ in the
                *AWS Key Management Service Developer Guide* .

              - **DeletionDate** *(datetime) --*

                The date and time after which AWS KMS deletes the CMK. This value is present only
                when ``KeyState`` is ``PendingDeletion`` .

              - **ValidTo** *(datetime) --*

                The time at which the imported key material expires. When the key material expires,
                AWS KMS deletes the key material and the CMK becomes unusable. This value is present
                only for CMKs whose ``Origin`` is ``EXTERNAL`` and whose ``ExpirationModel`` is
                ``KEY_MATERIAL_EXPIRES`` , otherwise this value is omitted.

              - **Origin** *(string) --*

                The source of the CMK's key material. When this value is ``AWS_KMS`` , AWS KMS
                created the key material. When this value is ``EXTERNAL`` , the key material was
                imported from your existing key management infrastructure or the CMK lacks key
                material. When this value is ``AWS_CLOUDHSM`` , the key material was created in the
                AWS CloudHSM cluster associated with a custom key store.

              - **CustomKeyStoreId** *(string) --*

                A unique identifier for the `custom key store
                <https://docs.aws.amazon.com/kms/latest/developerguide/custom-key-store-overview.html>`__
                that contains the CMK. This value is present only when the CMK is created in a
                custom key store.

              - **CloudHsmClusterId** *(string) --*

                The cluster ID of the AWS CloudHSM cluster that contains the key material for the
                CMK. When you create a CMK in a `custom key store
                <https://docs.aws.amazon.com/kms/latest/developerguide/custom-key-store-overview.html>`__
                , AWS KMS creates the key material for the CMK in the associated AWS CloudHSM
                cluster. This value is present only when the CMK is created in a custom key store.

              - **ExpirationModel** *(string) --*

                Specifies whether the CMK's key material expires. This value is present only when
                ``Origin`` is ``EXTERNAL`` , otherwise this value is omitted.

              - **KeyManager** *(string) --*

                The manager of the CMK. CMKs in your AWS account are either customer managed or AWS
                managed. For more information about the difference, see `Customer Master Keys
                <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#master_keys>`__
                in the *AWS Key Management Service Developer Guide* .

              - **CustomerMasterKeySpec** *(string) --*

                Describes the type of key material in the CMK.

              - **EncryptionAlgorithms** *(list) --*

                A list of encryption algorithms that the CMK supports. You cannot use the CMK with
                other encryption algorithms within AWS KMS.

                This field appears only when the ``KeyUsage`` of the CMK is ``ENCRYPT_DECRYPT`` .

                - *(string) --*

              - **SigningAlgorithms** *(list) --*

                A list of signing algorithms that the CMK supports. You cannot use the CMK with
                other signing algorithms within AWS KMS.

                This field appears only when the ``KeyUsage`` of the CMK is ``SIGN_VERIFY`` .

                - *(string) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def decrypt(
        self,
        CiphertextBlob: bytes,
        EncryptionContext: Dict[str, str] = None,
        GrantTokens: List[str] = None,
        KeyId: str = None,
        EncryptionAlgorithm: Literal[
            "SYMMETRIC_DEFAULT", "RSAES_OAEP_SHA_1", "RSAES_OAEP_SHA_256"
        ] = None,
    ) -> ClientDecryptResponseTypeDef:
        """
        Decrypts ciphertext that was encrypted by a AWS KMS customer master key (CMK) using any of
        the following operations:

        *  Encrypt

        *  GenerateDataKey

        *  GenerateDataKeyPair

        *  GenerateDataKeyWithoutPlaintext

        *  GenerateDataKeyPairWithoutPlaintext

        You can use this operation to decrypt ciphertext that was encrypted under a symmetric or
        asymmetric CMK. When the CMK is asymmetric, you must specify the CMK and the encryption
        algorithm that was used to encrypt the ciphertext. For information about symmetric and
        asymmetric CMKs, see `Using Symmetric and Asymmetric CMKs
        <https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html>`__ in the
        *AWS Key Management Service Developer Guide* .

        The Decrypt operation also decrypts ciphertext that was encrypted outside of AWS KMS by the
        public key in an AWS KMS asymmetric CMK. However, it cannot decrypt ciphertext produced by
        other libraries, such as the `AWS Encryption SDK
        <https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/>`__ or `Amazon S3
        client-side encryption
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingClientSideEncryption.html>`__ . These
        libraries return a ciphertext format that is incompatible with AWS KMS.

        If the ciphertext was encrypted under a symmetric CMK, you do not need to specify the CMK or
        the encryption algorithm. AWS KMS can get this information from metadata that it adds to the
        symmetric ciphertext blob. However, if you prefer, you can specify the ``KeyId`` to ensure
        that a particular CMK is used to decrypt the ciphertext. If you specify a different CMK than
        the one used to encrypt the ciphertext, the ``Decrypt`` operation fails.

        Whenever possible, use key policies to give users permission to call the Decrypt operation
        on a particular CMK, instead of using IAM policies. Otherwise, you might create an IAM user
        policy that gives the user Decrypt permission on all CMKs. This user could decrypt
        ciphertext that was encrypted by CMKs in other accounts if the key policy for the
        cross-account CMK permits it. If you must use an IAM policy for ``Decrypt`` permissions,
        limit the user to particular CMKs or particular trusted accounts.

        The CMK that you use for this operation must be in a compatible key state. For details, see
        `How Key State Affects Use of a Customer Master Key
        <https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`__ in the *AWS Key
        Management Service Developer Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/Decrypt>`_

        **Request Syntax**
        ::

          response = client.decrypt(
              CiphertextBlob=b'bytes',
              EncryptionContext={
                  'string': 'string'
              },
              GrantTokens=[
                  'string',
              ],
              KeyId='string',
              EncryptionAlgorithm='SYMMETRIC_DEFAULT'|'RSAES_OAEP_SHA_1'|'RSAES_OAEP_SHA_256'
          )
        :type CiphertextBlob: bytes
        :param CiphertextBlob: **[REQUIRED]**

          Ciphertext to be decrypted. The blob includes metadata.

        :type EncryptionContext: dict
        :param EncryptionContext:

          Specifies the encryption context to use when decrypting the data. An encryption context is
          valid only for cryptographic operations with a symmetric CMK. The standard asymmetric
          encryption algorithms that AWS KMS uses do not support an encryption context.

          An *encryption context* is a collection of non-secret key-value pairs that represents
          additional authenticated data. When you use an encryption context to encrypt data, you
          must specify the same (an exact case-sensitive match) encryption context to decrypt the
          data. An encryption context is optional when encrypting with a symmetric CMK, but it is
          highly recommended.

          For more information, see `Encryption Context
          <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#encrypt_context>`__
          in the *AWS Key Management Service Developer Guide* .

          - *(string) --*

            - *(string) --*

        :type GrantTokens: list
        :param GrantTokens:

          A list of grant tokens.

          For more information, see `Grant Tokens
          <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token>`__ in
          the *AWS Key Management Service Developer Guide* .

          - *(string) --*

        :type KeyId: string
        :param KeyId:

          Specifies the customer master key (CMK) that AWS KMS will use to decrypt the ciphertext.
          Enter a key ID of the CMK that was used to encrypt the ciphertext.

          If you specify a ``KeyId`` value, the ``Decrypt`` operation succeeds only if the specified
          CMK was used to encrypt the ciphertext.

          This parameter is required only when the ciphertext was encrypted under an asymmetric CMK.
          Otherwise, AWS KMS uses the metadata that it adds to the ciphertext blob to determine
          which CMK was used to encrypt the ciphertext. However, you can use this parameter to
          ensure that a particular CMK (of any kind) is used to decrypt the ciphertext.

          To specify a CMK, use its key ID, Amazon Resource Name (ARN), alias name, or alias ARN.
          When using an alias name, prefix it with ``"alias/"`` .

          For example:

          * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``

          * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``

          * Alias name: ``alias/ExampleAlias``

          * Alias ARN: ``arn:aws:kms:us-east-2:111122223333:alias/ExampleAlias``

          To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey . To get the alias
          name and alias ARN, use  ListAliases .

        :type EncryptionAlgorithm: string
        :param EncryptionAlgorithm:

          Specifies the encryption algorithm that will be used to decrypt the ciphertext. Specify
          the same algorithm that was used to encrypt the data. If you specify a different
          algorithm, the ``Decrypt`` operation fails.

          This parameter is required only when the ciphertext was encrypted under an asymmetric CMK.
          The default value, ``SYMMETRIC_DEFAULT`` , represents the only supported algorithm that is
          valid for symmetric CMKs.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'KeyId': 'string',
                'Plaintext': b'bytes',
                'EncryptionAlgorithm': 'SYMMETRIC_DEFAULT'|'RSAES_OAEP_SHA_1'|'RSAES_OAEP_SHA_256'
            }
          **Response Structure**

          - *(dict) --*

            - **KeyId** *(string) --*

              The ARN of the customer master key that was used to perform the decryption.

            - **Plaintext** *(bytes) --*

              Decrypted plaintext data. When you use the HTTP API or the AWS CLI, the value is
              Base64-encoded. Otherwise, it is not Base64-encoded.

            - **EncryptionAlgorithm** *(string) --*

              The encryption algorithm that was used to decrypt the ciphertext.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_alias(self, AliasName: str) -> None:
        """
        Deletes the specified alias. You cannot perform this operation on an alias in a different
        AWS account.

        Because an alias is not a property of a CMK, you can delete and change the aliases of a CMK
        without affecting the CMK. Also, aliases do not appear in the response from the  DescribeKey
        operation. To get the aliases of all CMKs, use the  ListAliases operation.

        Each CMK can have multiple aliases. To change the alias of a CMK, use  DeleteAlias to delete
        the current alias and  CreateAlias to create a new alias. To associate an existing alias
        with a different customer master key (CMK), call  UpdateAlias .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/DeleteAlias>`_

        **Request Syntax**
        ::

          response = client.delete_alias(
              AliasName='string'
          )
        :type AliasName: string
        :param AliasName: **[REQUIRED]**

          The alias to be deleted. The alias name must begin with ``alias/`` followed by the alias
          name, such as ``alias/ExampleAlias`` .

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_custom_key_store(self, CustomKeyStoreId: str) -> Dict[str, Any]:
        """
        Deletes a `custom key store
        <https://docs.aws.amazon.com/kms/latest/developerguide/custom-key-store-overview.html>`__ .
        This operation does not delete the AWS CloudHSM cluster that is associated with the custom
        key store, or affect any users or keys in the cluster.

        The custom key store that you delete cannot contain any AWS KMS `customer master keys (CMKs)
        <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#master_keys>`__ .
        Before deleting the key store, verify that you will never need to use any of the CMKs in the
        key store for any cryptographic operations. Then, use  ScheduleKeyDeletion to delete the AWS
        KMS customer master keys (CMKs) from the key store. When the scheduled waiting period
        expires, the ``ScheduleKeyDeletion`` operation deletes the CMKs. Then it makes a best effort
        to delete the key material from the associated cluster. However, you might need to manually
        `delete the orphaned key material
        <https://docs.aws.amazon.com/kms/latest/developerguide/fix-keystore.html#fix-keystore-orphaned-key>`__
        from the cluster and its backups.

        After all CMKs are deleted from AWS KMS, use  DisconnectCustomKeyStore to disconnect the key
        store from AWS KMS. Then, you can delete the custom key store.

        Instead of deleting the custom key store, consider using  DisconnectCustomKeyStore to
        disconnect it from AWS KMS. While the key store is disconnected, you cannot create or use
        the CMKs in the key store. But, you do not need to delete CMKs and you can reconnect a
        disconnected custom key store at any time.

        If the operation succeeds, it returns a JSON object with no properties.

        This operation is part of the `Custom Key Store feature
        <https://docs.aws.amazon.com/kms/latest/developerguide/custom-key-store-overview.html>`__
        feature in AWS KMS, which combines the convenience and extensive integration of AWS KMS with
        the isolation and control of a single-tenant key store.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/DeleteCustomKeyStore>`_

        **Request Syntax**
        ::

          response = client.delete_custom_key_store(
              CustomKeyStoreId='string'
          )
        :type CustomKeyStoreId: string
        :param CustomKeyStoreId: **[REQUIRED]**

          Enter the ID of the custom key store you want to delete. To find the ID of a custom key
          store, use the  DescribeCustomKeyStores operation.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def delete_imported_key_material(self, KeyId: str) -> None:
        """
        Deletes key material that you previously imported. This operation makes the specified
        customer master key (CMK) unusable. For more information about importing key material into
        AWS KMS, see `Importing Key Material
        <https://docs.aws.amazon.com/kms/latest/developerguide/importing-keys.html>`__ in the *AWS
        Key Management Service Developer Guide* . You cannot perform this operation on a CMK in a
        different AWS account.

        When the specified CMK is in the ``PendingDeletion`` state, this operation does not change
        the CMK's state. Otherwise, it changes the CMK's state to ``PendingImport`` .

        After you delete key material, you can use  ImportKeyMaterial to reimport the same key
        material into the CMK.

        The CMK that you use for this operation must be in a compatible key state. For details, see
        `How Key State Affects Use of a Customer Master Key
        <https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`__ in the *AWS Key
        Management Service Developer Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/DeleteImportedKeyMaterial>`_

        **Request Syntax**
        ::

          response = client.delete_imported_key_material(
              KeyId='string'
          )
        :type KeyId: string
        :param KeyId: **[REQUIRED]**

          Identifies the CMK from which you are deleting imported key material. The ``Origin`` of
          the CMK must be ``EXTERNAL`` .

          Specify the key ID or the Amazon Resource Name (ARN) of the CMK.

          For example:

          * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``

          * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``

          To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey .

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_custom_key_stores(
        self,
        CustomKeyStoreId: str = None,
        CustomKeyStoreName: str = None,
        Limit: int = None,
        Marker: str = None,
    ) -> ClientDescribeCustomKeyStoresResponseTypeDef:
        """
        Gets information about `custom key stores
        <https://docs.aws.amazon.com/kms/latest/developerguide/custom-key-store-overview.html>`__ in
        the account and region.

        This operation is part of the `Custom Key Store feature
        <https://docs.aws.amazon.com/kms/latest/developerguide/custom-key-store-overview.html>`__
        feature in AWS KMS, which combines the convenience and extensive integration of AWS KMS with
        the isolation and control of a single-tenant key store.

        By default, this operation returns information about all custom key stores in the account
        and region. To get only information about a particular custom key store, use either the
        ``CustomKeyStoreName`` or ``CustomKeyStoreId`` parameter (but not both).

        To determine whether the custom key store is connected to its AWS CloudHSM cluster, use the
        ``ConnectionState`` element in the response. If an attempt to connect the custom key store
        failed, the ``ConnectionState`` value is ``FAILED`` and the ``ConnectionErrorCode`` element
        in the response indicates the cause of the failure. For help interpreting the
        ``ConnectionErrorCode`` , see  CustomKeyStoresListEntry .

        Custom key stores have a ``DISCONNECTED`` connection state if the key store has never been
        connected or you use the  DisconnectCustomKeyStore operation to disconnect it. If your
        custom key store state is ``CONNECTED`` but you are having trouble using it, make sure that
        its associated AWS CloudHSM cluster is active and contains the minimum number of HSMs
        required for the operation, if any.

        For help repairing your custom key store, see the `Troubleshooting Custom Key Stores
        <https://docs.aws.amazon.com/kms/latest/developerguide/fix-keystore.html>`__ topic in the
        *AWS Key Management Service Developer Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/DescribeCustomKeyStores>`_

        **Request Syntax**
        ::

          response = client.describe_custom_key_stores(
              CustomKeyStoreId='string',
              CustomKeyStoreName='string',
              Limit=123,
              Marker='string'
          )
        :type CustomKeyStoreId: string
        :param CustomKeyStoreId:

          Gets only information about the specified custom key store. Enter the key store ID.

          By default, this operation gets information about all custom key stores in the account and
          region. To limit the output to a particular custom key store, you can use either the
          ``CustomKeyStoreId`` or ``CustomKeyStoreName`` parameter, but not both.

        :type CustomKeyStoreName: string
        :param CustomKeyStoreName:

          Gets only information about the specified custom key store. Enter the friendly name of the
          custom key store.

          By default, this operation gets information about all custom key stores in the account and
          region. To limit the output to a particular custom key store, you can use either the
          ``CustomKeyStoreId`` or ``CustomKeyStoreName`` parameter, but not both.

        :type Limit: integer
        :param Limit:

          Use this parameter to specify the maximum number of items to return. When this value is
          present, AWS KMS does not return more than the specified number of items, but it might
          return fewer.

        :type Marker: string
        :param Marker:

          Use this parameter in a subsequent request after you receive a response with truncated
          results. Set it to the value of ``NextMarker`` from the truncated response you just
          received.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'CustomKeyStores': [
                    {
                        'CustomKeyStoreId': 'string',
                        'CustomKeyStoreName': 'string',
                        'CloudHsmClusterId': 'string',
                        'TrustAnchorCertificate': 'string',
                        'ConnectionState':
                        'CONNECTED'|'CONNECTING'|'FAILED'|'DISCONNECTED'
                        |'DISCONNECTING',
                        'ConnectionErrorCode':
                        'INVALID_CREDENTIALS'|'CLUSTER_NOT_FOUND'|'NETWORK_ERRORS'
                        |'INTERNAL_ERROR'|'INSUFFICIENT_CLOUDHSM_HSMS'
                        |'USER_LOCKED_OUT',
                        'CreationDate': datetime(2015, 1, 1)
                    },
                ],
                'NextMarker': 'string',
                'Truncated': True|False
            }
          **Response Structure**

          - *(dict) --*

            - **CustomKeyStores** *(list) --*

              Contains metadata about each custom key store.

              - *(dict) --*

                Contains information about each custom key store in the custom key store list.

                - **CustomKeyStoreId** *(string) --*

                  A unique identifier for the custom key store.

                - **CustomKeyStoreName** *(string) --*

                  The user-specified friendly name for the custom key store.

                - **CloudHsmClusterId** *(string) --*

                  A unique identifier for the AWS CloudHSM cluster that is associated with the
                  custom key store.

                - **TrustAnchorCertificate** *(string) --*

                  The trust anchor certificate of the associated AWS CloudHSM cluster. When you
                  `initialize the cluster
                  <https://docs.aws.amazon.com/cloudhsm/latest/userguide/initialize-cluster.html#sign-csr>`__
                  , you create this certificate and save it in the ``customerCA.crt`` file.

                - **ConnectionState** *(string) --*

                  Indicates whether the custom key store is connected to its AWS CloudHSM cluster.

                  You can create and use CMKs in your custom key stores only when its connection
                  state is ``CONNECTED`` .

                  The value is ``DISCONNECTED`` if the key store has never been connected or you use
                  the  DisconnectCustomKeyStore operation to disconnect it. If the value is
                  ``CONNECTED`` but you are having trouble using the custom key store, make sure
                  that its associated AWS CloudHSM cluster is active and contains at least one
                  active HSM.

                  A value of ``FAILED`` indicates that an attempt to connect was unsuccessful. For
                  help resolving a connection failure, see `Troubleshooting a Custom Key Store
                  <https://docs.aws.amazon.com/kms/latest/developerguide/fix-keystore.html>`__ in
                  the *AWS Key Management Service Developer Guide* .

                - **ConnectionErrorCode** *(string) --*

                  Describes the connection error. Valid values are:

                  * ``CLUSTER_NOT_FOUND`` - AWS KMS cannot find the AWS CloudHSM cluster with the
                  specified cluster ID.

                  * ``INSUFFICIENT_CLOUDHSM_HSMS`` - The associated AWS CloudHSM cluster does not
                  contain any active HSMs. To connect a custom key store to its AWS CloudHSM
                  cluster, the cluster must contain at least one active HSM.

                  * ``INTERNAL_ERROR`` - AWS KMS could not complete the request due to an internal
                  error. Retry the request. For ``ConnectCustomKeyStore`` requests, disconnect the
                  custom key store before trying to connect again.

                  * ``INVALID_CREDENTIALS`` - AWS KMS does not have the correct password for the
                  ``kmsuser`` crypto user in the AWS CloudHSM cluster.

                  * ``NETWORK_ERRORS`` - Network errors are preventing AWS KMS from connecting to
                  the custom key store.

                  * ``USER_LOCKED_OUT`` - The ``kmsuser`` CU account is locked out of the associated
                  AWS CloudHSM cluster due to too many failed password attempts. Before you can
                  connect your custom key store to its AWS CloudHSM cluster, you must change the
                  ``kmsuser`` account password and update the password value for the custom key
                  store.

                  For help with connection failures, see `Troubleshooting Custom Key Stores
                  <https://docs.aws.amazon.com/kms/latest/developerguide/fix-keystore.html>`__ in
                  the *AWS Key Management Service Developer Guide* .

                - **CreationDate** *(datetime) --*

                  The date and time when the custom key store was created.

            - **NextMarker** *(string) --*

              When ``Truncated`` is true, this element is present and contains the value to use for
              the ``Marker`` parameter in a subsequent request.

            - **Truncated** *(boolean) --*

              A flag that indicates whether there are more items in the list. When this value is
              true, the list in this response is truncated. To get more items, pass the value of the
              ``NextMarker`` element in thisresponse to the ``Marker`` parameter in a subsequent
              request.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_key(
        self, KeyId: str, GrantTokens: List[str] = None
    ) -> ClientDescribeKeyResponseTypeDef:
        """
        Provides detailed information about a customer master key (CMK). You can run ``DescribeKey``
        on a `customer managed CMK
        <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk>`__ or an
        `AWS managed CMK
        <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk>`__ .

        This detailed information includes the key ARN, creation date (and deletion date, if
        applicable), the key state, and the origin and expiration date (if any) of the key material.
        For CMKs in custom key stores, it includes information about the custom key store, such as
        the key store ID and the AWS CloudHSM cluster ID. It includes fields, like ``KeySpec`` ,
        that help you distinguish symmetric from asymmetric CMKs. It also provides information that
        is particularly important to asymmetric CMKs, such as the key usage (encryption or signing)
        and the encryption algorithms or signing algorithms that the CMK supports.

         ``DescribeKey`` does not return the following information:

        * Aliases associated with the CMK. To get this information, use  ListAliases .

        * Whether automatic key rotation is enabled on the CMK. To get this information, use
        GetKeyRotationStatus . Also, some key states prevent a CMK from being automatically rotated.
        For details, see `How Automatic Key Rotation Works
        <https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html#rotate-keys-how-it-works>`__
        in *AWS Key Management Service Developer Guide* .

        * Tags on the CMK. To get this information, use  ListResourceTags .

        * Key policies and grants on the CMK. To get this information, use  GetKeyPolicy and
        ListGrants .

        If you call the ``DescribeKey`` operation on a *predefined AWS alias* , that is, an AWS
        alias with no key ID, AWS KMS creates an `AWS managed CMK
        <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#master_keys>`__ . Then,
        it associates the alias with the new CMK, and returns the ``KeyId`` and ``Arn`` of the new
        CMK in the response.

        To perform this operation on a CMK in a different AWS account, specify the key ARN or alias
        ARN in the value of the KeyId parameter.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/DescribeKey>`_

        **Request Syntax**
        ::

          response = client.describe_key(
              KeyId='string',
              GrantTokens=[
                  'string',
              ]
          )
        :type KeyId: string
        :param KeyId: **[REQUIRED]**

          Describes the specified customer master key (CMK).

          If you specify a predefined AWS alias (an AWS alias with no key ID), KMS associates the
          alias with an `AWS managed CMK
          <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#master_keys>`__ and
          returns its ``KeyId`` and ``Arn`` in the response.

          To specify a CMK, use its key ID, Amazon Resource Name (ARN), alias name, or alias ARN.
          When using an alias name, prefix it with ``"alias/"`` . To specify a CMK in a different
          AWS account, you must use the key ARN or alias ARN.

          For example:

          * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``

          * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``

          * Alias name: ``alias/ExampleAlias``

          * Alias ARN: ``arn:aws:kms:us-east-2:111122223333:alias/ExampleAlias``

          To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey . To get the alias
          name and alias ARN, use  ListAliases .

        :type GrantTokens: list
        :param GrantTokens:

          A list of grant tokens.

          For more information, see `Grant Tokens
          <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token>`__ in
          the *AWS Key Management Service Developer Guide* .

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'KeyMetadata': {
                    'AWSAccountId': 'string',
                    'KeyId': 'string',
                    'Arn': 'string',
                    'CreationDate': datetime(2015, 1, 1),
                    'Enabled': True|False,
                    'Description': 'string',
                    'KeyUsage': 'SIGN_VERIFY'|'ENCRYPT_DECRYPT',
                    'KeyState':
                    'Enabled'|'Disabled'|'PendingDeletion'|'PendingImport'
                    |'Unavailable',
                    'DeletionDate': datetime(2015, 1, 1),
                    'ValidTo': datetime(2015, 1, 1),
                    'Origin': 'AWS_KMS'|'EXTERNAL'|'AWS_CLOUDHSM',
                    'CustomKeyStoreId': 'string',
                    'CloudHsmClusterId': 'string',
                    'ExpirationModel': 'KEY_MATERIAL_EXPIRES'|'KEY_MATERIAL_DOES_NOT_EXPIRE',
                    'KeyManager': 'AWS'|'CUSTOMER',
                    'CustomerMasterKeySpec':
                    'RSA_2048'|'RSA_3072'|'RSA_4096'|'ECC_NIST_P256'|'ECC_NIST_P384'
                    |'ECC_NIST_P521'|'ECC_SECG_P256K1'|'SYMMETRIC_DEFAULT',
                    'EncryptionAlgorithms': [
                        'SYMMETRIC_DEFAULT'|'RSAES_OAEP_SHA_1'|'RSAES_OAEP_SHA_256',
                    ],
                    'SigningAlgorithms': [
                        'RSASSA_PSS_SHA_256'|'RSASSA_PSS_SHA_384'|'RSASSA_PSS_SHA_512'
                        |'RSASSA_PKCS1_V1_5_SHA_256'|'RSASSA_PKCS1_V1_5_SHA_384'
                        |'RSASSA_PKCS1_V1_5_SHA_512'|'ECDSA_SHA_256'|'ECDSA_SHA_384'
                        |'ECDSA_SHA_512',
                    ]
                }
            }
          **Response Structure**

          - *(dict) --*

            - **KeyMetadata** *(dict) --*

              Metadata associated with the key.

              - **AWSAccountId** *(string) --*

                The twelve-digit account ID of the AWS account that owns the CMK.

              - **KeyId** *(string) --*

                The globally unique identifier for the CMK.

              - **Arn** *(string) --*

                The Amazon Resource Name (ARN) of the CMK. For examples, see `AWS Key Management
                Service (AWS KMS)
                <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-kms>`__
                in the Example ARNs section of the *AWS General Reference* .

              - **CreationDate** *(datetime) --*

                The date and time when the CMK was created.

              - **Enabled** *(boolean) --*

                Specifies whether the CMK is enabled. When ``KeyState`` is ``Enabled`` this value is
                true, otherwise it is false.

              - **Description** *(string) --*

                The description of the CMK.

              - **KeyUsage** *(string) --*

                The cryptographic operations for which you can use the CMK.

              - **KeyState** *(string) --*

                The state of the CMK.

                For more information about how key state affects the use of a CMK, see `How Key
                State Affects the Use of a Customer Master Key
                <https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`__ in the
                *AWS Key Management Service Developer Guide* .

              - **DeletionDate** *(datetime) --*

                The date and time after which AWS KMS deletes the CMK. This value is present only
                when ``KeyState`` is ``PendingDeletion`` .

              - **ValidTo** *(datetime) --*

                The time at which the imported key material expires. When the key material expires,
                AWS KMS deletes the key material and the CMK becomes unusable. This value is present
                only for CMKs whose ``Origin`` is ``EXTERNAL`` and whose ``ExpirationModel`` is
                ``KEY_MATERIAL_EXPIRES`` , otherwise this value is omitted.

              - **Origin** *(string) --*

                The source of the CMK's key material. When this value is ``AWS_KMS`` , AWS KMS
                created the key material. When this value is ``EXTERNAL`` , the key material was
                imported from your existing key management infrastructure or the CMK lacks key
                material. When this value is ``AWS_CLOUDHSM`` , the key material was created in the
                AWS CloudHSM cluster associated with a custom key store.

              - **CustomKeyStoreId** *(string) --*

                A unique identifier for the `custom key store
                <https://docs.aws.amazon.com/kms/latest/developerguide/custom-key-store-overview.html>`__
                that contains the CMK. This value is present only when the CMK is created in a
                custom key store.

              - **CloudHsmClusterId** *(string) --*

                The cluster ID of the AWS CloudHSM cluster that contains the key material for the
                CMK. When you create a CMK in a `custom key store
                <https://docs.aws.amazon.com/kms/latest/developerguide/custom-key-store-overview.html>`__
                , AWS KMS creates the key material for the CMK in the associated AWS CloudHSM
                cluster. This value is present only when the CMK is created in a custom key store.

              - **ExpirationModel** *(string) --*

                Specifies whether the CMK's key material expires. This value is present only when
                ``Origin`` is ``EXTERNAL`` , otherwise this value is omitted.

              - **KeyManager** *(string) --*

                The manager of the CMK. CMKs in your AWS account are either customer managed or AWS
                managed. For more information about the difference, see `Customer Master Keys
                <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#master_keys>`__
                in the *AWS Key Management Service Developer Guide* .

              - **CustomerMasterKeySpec** *(string) --*

                Describes the type of key material in the CMK.

              - **EncryptionAlgorithms** *(list) --*

                A list of encryption algorithms that the CMK supports. You cannot use the CMK with
                other encryption algorithms within AWS KMS.

                This field appears only when the ``KeyUsage`` of the CMK is ``ENCRYPT_DECRYPT`` .

                - *(string) --*

              - **SigningAlgorithms** *(list) --*

                A list of signing algorithms that the CMK supports. You cannot use the CMK with
                other signing algorithms within AWS KMS.

                This field appears only when the ``KeyUsage`` of the CMK is ``SIGN_VERIFY`` .

                - *(string) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disable_key(self, KeyId: str) -> None:
        """
        Sets the state of a customer master key (CMK) to disabled, thereby preventing its use for
        cryptographic operations. You cannot perform this operation on a CMK in a different AWS
        account.

        For more information about how key state affects the use of a CMK, see `How Key State
        Affects the Use of a Customer Master Key
        <https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`__ in the * *AWS Key
        Management Service Developer Guide* * .

        The CMK that you use for this operation must be in a compatible key state. For details, see
        `How Key State Affects Use of a Customer Master Key
        <https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`__ in the *AWS Key
        Management Service Developer Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/DisableKey>`_

        **Request Syntax**
        ::

          response = client.disable_key(
              KeyId='string'
          )
        :type KeyId: string
        :param KeyId: **[REQUIRED]**

          A unique identifier for the customer master key (CMK).

          Specify the key ID or the Amazon Resource Name (ARN) of the CMK.

          For example:

          * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``

          * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``

          To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey .

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disable_key_rotation(self, KeyId: str) -> None:
        """
        Disables `automatic rotation of the key material
        <https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html>`__ for the
        specified symmetric customer master key (CMK).

        You cannot enable automatic rotation of asymmetric CMKs, CMKs with imported key material, or
        CMKs in a `custom key store
        <https://docs.aws.amazon.com/kms/latest/developerguide/custom-key-store-overview.html>`__ .
        You cannot perform this operation on a CMK in a different AWS account.

        The CMK that you use for this operation must be in a compatible key state. For details, see
        `How Key State Affects Use of a Customer Master Key
        <https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`__ in the *AWS Key
        Management Service Developer Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/DisableKeyRotation>`_

        **Request Syntax**
        ::

          response = client.disable_key_rotation(
              KeyId='string'
          )
        :type KeyId: string
        :param KeyId: **[REQUIRED]**

          Identifies a symmetric customer master key (CMK). You cannot enable automatic rotation of
          `asymmetric CMKs
          <https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html#asymmetric-cmks>`__
          , CMKs with `imported key material
          <https://docs.aws.amazon.com/kms/latest/developerguide/importing-keys.html>`__ , or CMKs
          in a `custom key store
          <https://docs.aws.amazon.com/kms/latest/developerguide/custom-key-store-overview.html>`__
          .

          Specify the key ID or the Amazon Resource Name (ARN) of the CMK.

          For example:

          * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``

          * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``

          To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey .

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def disconnect_custom_key_store(self, CustomKeyStoreId: str) -> Dict[str, Any]:
        """
        Disconnects the `custom key store
        <https://docs.aws.amazon.com/kms/latest/developerguide/custom-key-store-overview.html>`__
        from its associated AWS CloudHSM cluster. While a custom key store is disconnected, you can
        manage the custom key store and its customer master keys (CMKs), but you cannot create or
        use CMKs in the custom key store. You can reconnect the custom key store at any time.

        .. note::

          While a custom key store is disconnected, all attempts to create customer master keys
          (CMKs) in the custom key store or to use existing CMKs in cryptographic operations will
          fail. This action can prevent users from storing and accessing sensitive data.

        To find the connection state of a custom key store, use the  DescribeCustomKeyStores
        operation. To reconnect a custom key store, use the  ConnectCustomKeyStore operation.

        If the operation succeeds, it returns a JSON object with no properties.

        This operation is part of the `Custom Key Store feature
        <https://docs.aws.amazon.com/kms/latest/developerguide/custom-key-store-overview.html>`__
        feature in AWS KMS, which combines the convenience and extensive integration of AWS KMS with
        the isolation and control of a single-tenant key store.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/DisconnectCustomKeyStore>`_

        **Request Syntax**
        ::

          response = client.disconnect_custom_key_store(
              CustomKeyStoreId='string'
          )
        :type CustomKeyStoreId: string
        :param CustomKeyStoreId: **[REQUIRED]**

          Enter the ID of the custom key store you want to disconnect. To find the ID of a custom
          key store, use the  DescribeCustomKeyStores operation.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def enable_key(self, KeyId: str) -> None:
        """
        Sets the key state of a customer master key (CMK) to enabled. This allows you to use the CMK
        for cryptographic operations. You cannot perform this operation on a CMK in a different AWS
        account.

        The CMK that you use for this operation must be in a compatible key state. For details, see
        `How Key State Affects Use of a Customer Master Key
        <https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`__ in the *AWS Key
        Management Service Developer Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/EnableKey>`_

        **Request Syntax**
        ::

          response = client.enable_key(
              KeyId='string'
          )
        :type KeyId: string
        :param KeyId: **[REQUIRED]**

          A unique identifier for the customer master key (CMK).

          Specify the key ID or the Amazon Resource Name (ARN) of the CMK.

          For example:

          * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``

          * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``

          To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey .

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def enable_key_rotation(self, KeyId: str) -> None:
        """
        Enables `automatic rotation of the key material
        <https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html>`__ for the
        specified symmetric customer master key (CMK). You cannot perform this operation on a CMK in
        a different AWS account.

        You cannot enable automatic rotation of asymmetric CMKs, CMKs with imported key material, or
        CMKs in a `custom key store
        <https://docs.aws.amazon.com/kms/latest/developerguide/custom-key-store-overview.html>`__ .

        The CMK that you use for this operation must be in a compatible key state. For details, see
        `How Key State Affects Use of a Customer Master Key
        <https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`__ in the *AWS Key
        Management Service Developer Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/EnableKeyRotation>`_

        **Request Syntax**
        ::

          response = client.enable_key_rotation(
              KeyId='string'
          )
        :type KeyId: string
        :param KeyId: **[REQUIRED]**

          Identifies a symmetric customer master key (CMK). You cannot enable automatic rotation of
          asymmetric CMKs, CMKs with imported key material, or CMKs in a `custom key store
          <https://docs.aws.amazon.com/kms/latest/developerguide/custom-key-store-overview.html>`__
          .

          Specify the key ID or the Amazon Resource Name (ARN) of the CMK.

          For example:

          * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``

          * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``

          To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey .

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def encrypt(
        self,
        KeyId: str,
        Plaintext: bytes,
        EncryptionContext: Dict[str, str] = None,
        GrantTokens: List[str] = None,
        EncryptionAlgorithm: Literal[
            "SYMMETRIC_DEFAULT", "RSAES_OAEP_SHA_1", "RSAES_OAEP_SHA_256"
        ] = None,
    ) -> ClientEncryptResponseTypeDef:
        """
        Encrypts plaintext into ciphertext by using a customer master key (CMK). The ``Encrypt``
        operation has two primary use cases:

        * You can encrypt small amounts of arbitrary data, such as a personal identifier or database
        password, or other sensitive information.

        * You can use the ``Encrypt`` operation to move encrypted data from one AWS region to
        another. In the first region, generate a data key and use the plaintext key to encrypt the
        data. Then, in the new region, call the ``Encrypt`` method on same plaintext data key. Now,
        you can safely move the encrypted data and encrypted data key to the new region, and decrypt
        in the new region when necessary.

        You don't need to use the ``Encrypt`` operation to encrypt a data key. The  GenerateDataKey
        and  GenerateDataKeyPair operations return a plaintext data key and an encrypted copy of
        that data key.

        When you encrypt data, you must specify a symmetric or asymmetric CMK to use in the
        encryption operation. The CMK must have a ``KeyUsage`` value of ``ENCRYPT_DECRYPT.`` To find
        the ``KeyUsage`` of a CMK, use the  DescribeKey operation.

        If you use a symmetric CMK, you can use an encryption context to add additional security to
        your encryption operation. If you specify an ``EncryptionContext`` when encrypting data, you
        must specify the same encryption context (a case-sensitive exact match) when decrypting the
        data. Otherwise, the request to decrypt fails with an ``InvalidCiphertextException`` . For
        more information, see `Encryption Context
        <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#encrypt_context>`__ in
        the *AWS Key Management Service Developer Guide* .

        If you specify an asymmetric CMK, you must also specify the encryption algorithm. The
        algorithm must be compatible with the CMK type.

        .. warning::

          When you use an asymmetric CMK to encrypt or reencrypt data, be sure to record the CMK and
          encryption algorithm that you choose. You will be required to provide the same CMK and
          encryption algorithm when you decrypt the data. If the CMK and algorithm do not match the
          values used to encrypt the data, the decrypt operation fails.

          You are not required to supply the CMK ID and encryption algorithm when you decrypt with
          symmetric CMKs because AWS KMS stores this information in the ciphertext blob. AWS KMS
          cannot store metadata in ciphertext generated with asymmetric keys. The standard format
          for asymmetric key ciphertext does not include configurable fields.

        The maximum size of the data that you can encrypt varies with the type of CMK and the
        encryption algorithm that you choose.

        * Symmetric CMKs

          * ``SYMMETRIC_DEFAULT`` : 4096 bytes

        * ``RSA_2048``

          * ``RSAES_OAEP_SHA_1`` : 214 bytes

          * ``RSAES_OAEP_SHA_256`` : 190 bytes

        * ``RSA_3072``

          * ``RSAES_OAEP_SHA_1`` : 342 bytes

          * ``RSAES_OAEP_SHA_256`` : 318 bytes

        * ``RSA_4096``

          * ``RSAES_OAEP_SHA_1`` : 470 bytes

          * ``RSAES_OAEP_SHA_256`` : 446 bytes

        The CMK that you use for this operation must be in a compatible key state. For details, see
        `How Key State Affects Use of a Customer Master Key
        <https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`__ in the *AWS Key
        Management Service Developer Guide* .

        To perform this operation on a CMK in a different AWS account, specify the key ARN or alias
        ARN in the value of the KeyId parameter.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/Encrypt>`_

        **Request Syntax**
        ::

          response = client.encrypt(
              KeyId='string',
              Plaintext=b'bytes',
              EncryptionContext={
                  'string': 'string'
              },
              GrantTokens=[
                  'string',
              ],
              EncryptionAlgorithm='SYMMETRIC_DEFAULT'|'RSAES_OAEP_SHA_1'|'RSAES_OAEP_SHA_256'
          )
        :type KeyId: string
        :param KeyId: **[REQUIRED]**

          A unique identifier for the customer master key (CMK).

          To specify a CMK, use its key ID, Amazon Resource Name (ARN), alias name, or alias ARN.
          When using an alias name, prefix it with ``"alias/"`` . To specify a CMK in a different
          AWS account, you must use the key ARN or alias ARN.

          For example:

          * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``

          * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``

          * Alias name: ``alias/ExampleAlias``

          * Alias ARN: ``arn:aws:kms:us-east-2:111122223333:alias/ExampleAlias``

          To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey . To get the alias
          name and alias ARN, use  ListAliases .

        :type Plaintext: bytes
        :param Plaintext: **[REQUIRED]**

          Data to be encrypted.

        :type EncryptionContext: dict
        :param EncryptionContext:

          Specifies the encryption context that will be used to encrypt the data. An encryption
          context is valid only for cryptographic operations with a symmetric CMK. The standard
          asymmetric encryption algorithms that AWS KMS uses do not support an encryption context.

          An *encryption context* is a collection of non-secret key-value pairs that represents
          additional authenticated data. When you use an encryption context to encrypt data, you
          must specify the same (an exact case-sensitive match) encryption context to decrypt the
          data. An encryption context is optional when encrypting with a symmetric CMK, but it is
          highly recommended.

          For more information, see `Encryption Context
          <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#encrypt_context>`__
          in the *AWS Key Management Service Developer Guide* .

          - *(string) --*

            - *(string) --*

        :type GrantTokens: list
        :param GrantTokens:

          A list of grant tokens.

          For more information, see `Grant Tokens
          <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token>`__ in
          the *AWS Key Management Service Developer Guide* .

          - *(string) --*

        :type EncryptionAlgorithm: string
        :param EncryptionAlgorithm:

          Specifies the encryption algorithm that AWS KMS will use to encrypt the plaintext message.
          The algorithm must be compatible with the CMK that you specify.

          This parameter is required only for asymmetric CMKs. The default value,
          ``SYMMETRIC_DEFAULT`` , is the algorithm used for symmetric CMKs. If you are using an
          asymmetric CMK, we recommend RSAES_OAEP_SHA_256.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'CiphertextBlob': b'bytes',
                'KeyId': 'string',
                'EncryptionAlgorithm': 'SYMMETRIC_DEFAULT'|'RSAES_OAEP_SHA_1'|'RSAES_OAEP_SHA_256'
            }
          **Response Structure**

          - *(dict) --*

            - **CiphertextBlob** *(bytes) --*

              The encrypted plaintext. When you use the HTTP API or the AWS CLI, the value is
              Base64-encoded. Otherwise, it is not Base64-encoded.

            - **KeyId** *(string) --*

              The ID of the key used during encryption.

            - **EncryptionAlgorithm** *(string) --*

              The encryption algorithm that was used to encrypt the plaintext.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def generate_data_key(
        self,
        KeyId: str,
        EncryptionContext: Dict[str, str] = None,
        NumberOfBytes: int = None,
        KeySpec: Literal["AES_256", "AES_128"] = None,
        GrantTokens: List[str] = None,
    ) -> ClientGenerateDataKeyResponseTypeDef:
        """
        Generates a unique symmetric data key. This operation returns a plaintext copy of the data
        key and a copy that is encrypted under a customer master key (CMK) that you specify. You can
        use the plaintext key to encrypt your data outside of AWS KMS and store the encrypted data
        key with the encrypted data.

         ``GenerateDataKey`` returns a unique data key for each request. The bytes in the key are
         not related to the caller or CMK that is used to encrypt the data key.

        To generate a data key, specify the symmetric CMK that will be used to encrypt the data key.
        You cannot use an asymmetric CMK to generate data keys.

        You must also specify the length of the data key. Use either the ``KeySpec`` or
        ``NumberOfBytes`` parameters (but not both). For 128-bit and 256-bit data keys, use the
        ``KeySpec`` parameter.

        If the operation succeeds, the plaintext copy of the data key is in the ``Plaintext`` field
        of the response, and the encrypted copy of the data key in the ``CiphertextBlob`` field.

        To get only an encrypted copy of the data key, use  GenerateDataKeyWithoutPlaintext . To
        generate an asymmetric data key pair, use the  GenerateDataKeyPair or
        GenerateDataKeyPairWithoutPlaintext operation. To get a cryptographically secure random byte
        string, use  GenerateRandom .

        You can use the optional encryption context to add additional security to the encryption
        operation. If you specify an ``EncryptionContext`` , you must specify the same encryption
        context (a case-sensitive exact match) when decrypting the encrypted data key. Otherwise,
        the request to decrypt fails with an InvalidCiphertextException. For more information, see
        `Encryption Context
        <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#encrypt_context>`__ in
        the *AWS Key Management Service Developer Guide* .

        The CMK that you use for this operation must be in a compatible key state. For details, see
        `How Key State Affects Use of a Customer Master Key
        <https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`__ in the *AWS Key
        Management Service Developer Guide* .

        We recommend that you use the following pattern to encrypt data locally in your application:

        * Use the ``GenerateDataKey`` operation to get a data encryption key.

        * Use the plaintext data key (returned in the ``Plaintext`` field of the response) to
        encrypt data locally, then erase the plaintext data key from memory.

        * Store the encrypted data key (returned in the ``CiphertextBlob`` field of the response)
        alongside the locally encrypted data.

        To decrypt data locally:

        * Use the  Decrypt operation to decrypt the encrypted data key. The operation returns a
        plaintext copy of the data key.

        * Use the plaintext data key to decrypt data locally, then erase the plaintext data key from
        memory.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/GenerateDataKey>`_

        **Request Syntax**
        ::

          response = client.generate_data_key(
              KeyId='string',
              EncryptionContext={
                  'string': 'string'
              },
              NumberOfBytes=123,
              KeySpec='AES_256'|'AES_128',
              GrantTokens=[
                  'string',
              ]
          )
        :type KeyId: string
        :param KeyId: **[REQUIRED]**

          Identifies the symmetric CMK that encrypts the data key.

          To specify a CMK, use its key ID, Amazon Resource Name (ARN), alias name, or alias ARN.
          When using an alias name, prefix it with ``"alias/"`` . To specify a CMK in a different
          AWS account, you must use the key ARN or alias ARN.

          For example:

          * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``

          * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``

          * Alias name: ``alias/ExampleAlias``

          * Alias ARN: ``arn:aws:kms:us-east-2:111122223333:alias/ExampleAlias``

          To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey . To get the alias
          name and alias ARN, use  ListAliases .

        :type EncryptionContext: dict
        :param EncryptionContext:

          Specifies the encryption context that will be used when encrypting the data key.

          An *encryption context* is a collection of non-secret key-value pairs that represents
          additional authenticated data. When you use an encryption context to encrypt data, you
          must specify the same (an exact case-sensitive match) encryption context to decrypt the
          data. An encryption context is optional when encrypting with a symmetric CMK, but it is
          highly recommended.

          For more information, see `Encryption Context
          <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#encrypt_context>`__
          in the *AWS Key Management Service Developer Guide* .

          - *(string) --*

            - *(string) --*

        :type NumberOfBytes: integer
        :param NumberOfBytes:

          Specifies the length of the data key in bytes. For example, use the value 64 to generate a
          512-bit data key (64 bytes is 512 bits). For 128-bit (16-byte) and 256-bit (32-byte) data
          keys, use the ``KeySpec`` parameter.

          You must specify either the ``KeySpec`` or the ``NumberOfBytes`` parameter (but not both)
          in every ``GenerateDataKey`` request.

        :type KeySpec: string
        :param KeySpec:

          Specifies the length of the data key. Use ``AES_128`` to generate a 128-bit symmetric key,
          or ``AES_256`` to generate a 256-bit symmetric key.

          You must specify either the ``KeySpec`` or the ``NumberOfBytes`` parameter (but not both)
          in every ``GenerateDataKey`` request.

        :type GrantTokens: list
        :param GrantTokens:

          A list of grant tokens.

          For more information, see `Grant Tokens
          <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token>`__ in
          the *AWS Key Management Service Developer Guide* .

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'CiphertextBlob': b'bytes',
                'Plaintext': b'bytes',
                'KeyId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **CiphertextBlob** *(bytes) --*

              The encrypted copy of the data key. When you use the HTTP API or the AWS CLI, the
              value is Base64-encoded. Otherwise, it is not Base64-encoded.

            - **Plaintext** *(bytes) --*

              The plaintext data key. When you use the HTTP API or the AWS CLI, the value is
              Base64-encoded. Otherwise, it is not Base64-encoded. Use this data key to encrypt your
              data outside of KMS. Then, remove it from memory as soon as possible.

            - **KeyId** *(string) --*

              The identifier of the CMK that encrypted the data key.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def generate_data_key_pair(
        self,
        KeyId: str,
        KeyPairSpec: Literal[
            "RSA_2048",
            "RSA_3072",
            "RSA_4096",
            "ECC_NIST_P256",
            "ECC_NIST_P384",
            "ECC_NIST_P521",
            "ECC_SECG_P256K1",
        ],
        EncryptionContext: Dict[str, str] = None,
        GrantTokens: List[str] = None,
    ) -> ClientGenerateDataKeyPairResponseTypeDef:
        """
        Generates a unique asymmetric data key pair. The ``GenerateDataKeyPair`` operation returns a
        plaintext public key, a plaintext private key, and a copy of the private key that is
        encrypted under the symmetric CMK you specify. You can use the data key pair to perform
        asymmetric cryptography outside of AWS KMS.

         ``GenerateDataKeyPair`` returns a unique data key pair for each request. The bytes in the
         keys are not related to the caller or the CMK that is used to encrypt the private key.

        You can use the public key that ``GenerateDataKeyPair`` returns to encrypt data or verify a
        signature outside of AWS KMS. Then, store the encrypted private key with the data. When you
        are ready to decrypt data or sign a message, you can use the  Decrypt operation to decrypt
        the encrypted private key.

        To generate a data key pair, you must specify a symmetric customer master key (CMK) to
        encrypt the private key in a data key pair. You cannot use an asymmetric CMK. To get the
        type of your CMK, use the  DescribeKey operation.

        If you are using the data key pair to encrypt data, or for any operation where you don't
        immediately need a private key, consider using the  GenerateDataKeyPairWithoutPlaintext
        operation. ``GenerateDataKeyPairWithoutPlaintext`` returns a plaintext public key and an
        encrypted private key, but omits the plaintext private key that you need only to decrypt
        ciphertext or sign a message. Later, when you need to decrypt the data or sign a message,
        use the  Decrypt operation to decrypt the encrypted private key in the data key pair.

        You can use the optional encryption context to add additional security to the encryption
        operation. If you specify an ``EncryptionContext`` , you must specify the same encryption
        context (a case-sensitive exact match) when decrypting the encrypted data key. Otherwise,
        the request to decrypt fails with an InvalidCiphertextException. For more information, see
        `Encryption Context
        <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#encrypt_context>`__ in
        the *AWS Key Management Service Developer Guide* .

        The CMK that you use for this operation must be in a compatible key state. For details, see
        `How Key State Affects Use of a Customer Master Key
        <https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`__ in the *AWS Key
        Management Service Developer Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/GenerateDataKeyPair>`_

        **Request Syntax**
        ::

          response = client.generate_data_key_pair(
              EncryptionContext={
                  'string': 'string'
              },
              KeyId='string',
              KeyPairSpec=
                  'RSA_2048'|'RSA_3072'|'RSA_4096'|'ECC_NIST_P256'|'ECC_NIST_P384'|'ECC_NIST_P521'
                  |'ECC_SECG_P256K1',
              GrantTokens=[
                  'string',
              ]
          )
        :type EncryptionContext: dict
        :param EncryptionContext:

          Specifies the encryption context that will be used when encrypting the private key in the
          data key pair.

          An *encryption context* is a collection of non-secret key-value pairs that represents
          additional authenticated data. When you use an encryption context to encrypt data, you
          must specify the same (an exact case-sensitive match) encryption context to decrypt the
          data. An encryption context is optional when encrypting with a symmetric CMK, but it is
          highly recommended.

          For more information, see `Encryption Context
          <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#encrypt_context>`__
          in the *AWS Key Management Service Developer Guide* .

          - *(string) --*

            - *(string) --*

        :type KeyId: string
        :param KeyId: **[REQUIRED]**

          Specifies the symmetric CMK that encrypts the private key in the data key pair. You cannot
          specify an asymmetric CMKs.

          To specify a CMK, use its key ID, Amazon Resource Name (ARN), alias name, or alias ARN.
          When using an alias name, prefix it with ``"alias/"`` . To specify a CMK in a different
          AWS account, you must use the key ARN or alias ARN.

          For example:

          * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``

          * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``

          * Alias name: ``alias/ExampleAlias``

          * Alias ARN: ``arn:aws:kms:us-east-2:111122223333:alias/ExampleAlias``

          To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey . To get the alias
          name and alias ARN, use  ListAliases .

        :type KeyPairSpec: string
        :param KeyPairSpec: **[REQUIRED]**

          Determines the type of data key pair that is generated.

          The AWS KMS rule that restricts the use of asymmetric RSA CMKs to encrypt and decrypt or
          to sign and verify (but not both), and the rule that permits you to use ECC CMKs only to
          sign and verify, are not effective outside of AWS KMS.

        :type GrantTokens: list
        :param GrantTokens:

          A list of grant tokens.

          For more information, see `Grant Tokens
          <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token>`__ in
          the *AWS Key Management Service Developer Guide* .

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'PrivateKeyCiphertextBlob': b'bytes',
                'PrivateKeyPlaintext': b'bytes',
                'PublicKey': b'bytes',
                'KeyId': 'string',
                'KeyPairSpec':
                'RSA_2048'|'RSA_3072'|'RSA_4096'|'ECC_NIST_P256'|'ECC_NIST_P384'
                |'ECC_NIST_P521'|'ECC_SECG_P256K1'
            }
          **Response Structure**

          - *(dict) --*

            - **PrivateKeyCiphertextBlob** *(bytes) --*

              The encrypted copy of the private key. When you use the HTTP API or the AWS CLI, the
              value is Base64-encoded. Otherwise, it is not Base64-encoded.

            - **PrivateKeyPlaintext** *(bytes) --*

              The plaintext copy of the private key. When you use the HTTP API or the AWS CLI, the
              value is Base64-encoded. Otherwise, it is not Base64-encoded.

            - **PublicKey** *(bytes) --*

              The public key (in plaintext).

            - **KeyId** *(string) --*

              The identifier of the CMK that encrypted the private key.

            - **KeyPairSpec** *(string) --*

              The type of data key pair that was generated.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def generate_data_key_pair_without_plaintext(
        self,
        KeyId: str,
        KeyPairSpec: Literal[
            "RSA_2048",
            "RSA_3072",
            "RSA_4096",
            "ECC_NIST_P256",
            "ECC_NIST_P384",
            "ECC_NIST_P521",
            "ECC_SECG_P256K1",
        ],
        EncryptionContext: Dict[str, str] = None,
        GrantTokens: List[str] = None,
    ) -> ClientGenerateDataKeyPairWithoutPlaintextResponseTypeDef:
        """
        Generates a unique asymmetric data key pair. The ``GenerateDataKeyPairWithoutPlaintext``
        operation returns a plaintext public key and a copy of the private key that is encrypted
        under the symmetric CMK you specify. Unlike  GenerateDataKeyPair , this operation does not
        return a plaintext private key.

        To generate a data key pair, you must specify a symmetric customer master key (CMK) to
        encrypt the private key in the data key pair. You cannot use an asymmetric CMK. To get the
        type of your CMK, use the ``KeySpec`` field in the  DescribeKey response.

        You can use the public key that ``GenerateDataKeyPairWithoutPlaintext`` returns to encrypt
        data or verify a signature outside of AWS KMS. Then, store the encrypted private key with
        the data. When you are ready to decrypt data or sign a message, you can use the  Decrypt
        operation to decrypt the encrypted private key.

         ``GenerateDataKeyPairWithoutPlaintext`` returns a unique data key pair for each request.
         The bytes in the key are not related to the caller or CMK that is used to encrypt the
         private key.

        You can use the optional encryption context to add additional security to the encryption
        operation. If you specify an ``EncryptionContext`` , you must specify the same encryption
        context (a case-sensitive exact match) when decrypting the encrypted data key. Otherwise,
        the request to decrypt fails with an InvalidCiphertextException. For more information, see
        `Encryption Context
        <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#encrypt_context>`__ in
        the *AWS Key Management Service Developer Guide* .

        The CMK that you use for this operation must be in a compatible key state. For details, see
        `How Key State Affects Use of a Customer Master Key
        <https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`__ in the *AWS Key
        Management Service Developer Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/GenerateDataKeyPairWithoutPlaintext>`_

        **Request Syntax**
        ::

          response = client.generate_data_key_pair_without_plaintext(
              EncryptionContext={
                  'string': 'string'
              },
              KeyId='string',
              KeyPairSpec=
                  'RSA_2048'|'RSA_3072'|'RSA_4096'|'ECC_NIST_P256'|'ECC_NIST_P384'|'ECC_NIST_P521'
                  |'ECC_SECG_P256K1',
              GrantTokens=[
                  'string',
              ]
          )
        :type EncryptionContext: dict
        :param EncryptionContext:

          Specifies the encryption context that will be used when encrypting the private key in the
          data key pair.

          An *encryption context* is a collection of non-secret key-value pairs that represents
          additional authenticated data. When you use an encryption context to encrypt data, you
          must specify the same (an exact case-sensitive match) encryption context to decrypt the
          data. An encryption context is optional when encrypting with a symmetric CMK, but it is
          highly recommended.

          For more information, see `Encryption Context
          <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#encrypt_context>`__
          in the *AWS Key Management Service Developer Guide* .

          - *(string) --*

            - *(string) --*

        :type KeyId: string
        :param KeyId: **[REQUIRED]**

          Specifies the CMK that encrypts the private key in the data key pair. You must specify a
          symmetric CMK. You cannot use an asymmetric CMK.

          To specify a CMK, use its key ID, Amazon Resource Name (ARN), alias name, or alias ARN.
          When using an alias name, prefix it with ``"alias/"`` .

          For example:

          * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``

          * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``

          * Alias name: ``alias/ExampleAlias``

          * Alias ARN: ``arn:aws:kms:us-east-2:111122223333:alias/ExampleAlias``

          To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey . To get the alias
          name and alias ARN, use  ListAliases .

        :type KeyPairSpec: string
        :param KeyPairSpec: **[REQUIRED]**

          Determines the type of data key pair that is generated.

          The AWS KMS rule that restricts the use of asymmetric RSA CMKs to encrypt and decrypt or
          to sign and verify (but not both), and the rule that permits you to use ECC CMKs only to
          sign and verify, are not effective outside of AWS KMS.

        :type GrantTokens: list
        :param GrantTokens:

          A list of grant tokens.

          For more information, see `Grant Tokens
          <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token>`__ in
          the *AWS Key Management Service Developer Guide* .

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'PrivateKeyCiphertextBlob': b'bytes',
                'PublicKey': b'bytes',
                'KeyId': 'string',
                'KeyPairSpec':
                'RSA_2048'|'RSA_3072'|'RSA_4096'|'ECC_NIST_P256'|'ECC_NIST_P384'
                |'ECC_NIST_P521'|'ECC_SECG_P256K1'
            }
          **Response Structure**

          - *(dict) --*

            - **PrivateKeyCiphertextBlob** *(bytes) --*

              The encrypted copy of the private key. When you use the HTTP API or the AWS CLI, the
              value is Base64-encoded. Otherwise, it is not Base64-encoded.

            - **PublicKey** *(bytes) --*

              The public key (in plaintext).

            - **KeyId** *(string) --*

              Specifies the CMK that encrypted the private key in the data key pair. You must
              specify a symmetric CMK. You cannot use an asymmetric CMK.

              To specify a CMK, use its key ID, Amazon Resource Name (ARN), alias name, or alias
              ARN. When using an alias name, prefix it with ``"alias/"`` .

              For example:

              * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``

              * Key ARN:
              ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``

              * Alias name: ``alias/ExampleAlias``

              * Alias ARN: ``arn:aws:kms:us-east-2:111122223333:alias/ExampleAlias``

              To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey . To get the
              alias name and alias ARN, use  ListAliases .

            - **KeyPairSpec** *(string) --*

              The type of data key pair that was generated.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def generate_data_key_without_plaintext(
        self,
        KeyId: str,
        EncryptionContext: Dict[str, str] = None,
        KeySpec: Literal["AES_256", "AES_128"] = None,
        NumberOfBytes: int = None,
        GrantTokens: List[str] = None,
    ) -> ClientGenerateDataKeyWithoutPlaintextResponseTypeDef:
        """
        Generates a unique symmetric data key. This operation returns a data key that is encrypted
        under a customer master key (CMK) that you specify. To request an asymmetric data key pair,
        use the  GenerateDataKeyPair or  GenerateDataKeyPairWithoutPlaintext operations.

         ``GenerateDataKeyWithoutPlaintext`` is identical to the  GenerateDataKey operation except
         that returns only the encrypted copy of the data key. This operation is useful for systems
         that need to encrypt data at some point, but not immediately. When you need to encrypt the
         data, you call the  Decrypt operation on the encrypted copy of the key.

        It's also useful in distributed systems with different levels of trust. For example, you
        might store encrypted data in containers. One component of your system creates new
        containers and stores an encrypted data key with each container. Then, a different component
        puts the data into the containers. That component first decrypts the data key, uses the
        plaintext data key to encrypt data, puts the encrypted data into the container, and then
        destroys the plaintext data key. In this system, the component that creates the containers
        never sees the plaintext data key.

         ``GenerateDataKeyWithoutPlaintext`` returns a unique data key for each request. The bytes
         in the keys are not related to the caller or CMK that is used to encrypt the private key.

        To generate a data key, you must specify the symmetric customer master key (CMK) that is
        used to encrypt the data key. You cannot use an asymmetric CMK to generate a data key. To
        get the type of your CMK, use the ``KeySpec`` field in the  DescribeKey response. You must
        also specify the length of the data key using either the ``KeySpec`` or ``NumberOfBytes``
        field (but not both). For common key lengths (128-bit and 256-bit symmetric keys), use the
        ``KeySpec`` parameter.

        If the operation succeeds, you will find the plaintext copy of the data key in the
        ``Plaintext`` field of the response, and the encrypted copy of the data key in the
        ``CiphertextBlob`` field.

        You can use the optional encryption context to add additional security to the encryption
        operation. If you specify an ``EncryptionContext`` , you must specify the same encryption
        context (a case-sensitive exact match) when decrypting the encrypted data key. Otherwise,
        the request to decrypt fails with an InvalidCiphertextException. For more information, see
        `Encryption Context
        <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#encrypt_context>`__ in
        the *AWS Key Management Service Developer Guide* .

        The CMK that you use for this operation must be in a compatible key state. For details, see
        `How Key State Affects Use of a Customer Master Key
        <https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`__ in the *AWS Key
        Management Service Developer Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/GenerateDataKeyWithoutPlaintext>`_

        **Request Syntax**
        ::

          response = client.generate_data_key_without_plaintext(
              KeyId='string',
              EncryptionContext={
                  'string': 'string'
              },
              KeySpec='AES_256'|'AES_128',
              NumberOfBytes=123,
              GrantTokens=[
                  'string',
              ]
          )
        :type KeyId: string
        :param KeyId: **[REQUIRED]**

          The identifier of the symmetric customer master key (CMK) that encrypts the data key.

          To specify a CMK, use its key ID, Amazon Resource Name (ARN), alias name, or alias ARN.
          When using an alias name, prefix it with ``"alias/"`` . To specify a CMK in a different
          AWS account, you must use the key ARN or alias ARN.

          For example:

          * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``

          * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``

          * Alias name: ``alias/ExampleAlias``

          * Alias ARN: ``arn:aws:kms:us-east-2:111122223333:alias/ExampleAlias``

          To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey . To get the alias
          name and alias ARN, use  ListAliases .

        :type EncryptionContext: dict
        :param EncryptionContext:

          Specifies the encryption context that will be used when encrypting the data key.

          An *encryption context* is a collection of non-secret key-value pairs that represents
          additional authenticated data. When you use an encryption context to encrypt data, you
          must specify the same (an exact case-sensitive match) encryption context to decrypt the
          data. An encryption context is optional when encrypting with a symmetric CMK, but it is
          highly recommended.

          For more information, see `Encryption Context
          <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#encrypt_context>`__
          in the *AWS Key Management Service Developer Guide* .

          - *(string) --*

            - *(string) --*

        :type KeySpec: string
        :param KeySpec:

          The length of the data key. Use ``AES_128`` to generate a 128-bit symmetric key, or
          ``AES_256`` to generate a 256-bit symmetric key.

        :type NumberOfBytes: integer
        :param NumberOfBytes:

          The length of the data key in bytes. For example, use the value 64 to generate a 512-bit
          data key (64 bytes is 512 bits). For common key lengths (128-bit and 256-bit symmetric
          keys), we recommend that you use the ``KeySpec`` field instead of this one.

        :type GrantTokens: list
        :param GrantTokens:

          A list of grant tokens.

          For more information, see `Grant Tokens
          <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token>`__ in
          the *AWS Key Management Service Developer Guide* .

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'CiphertextBlob': b'bytes',
                'KeyId': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **CiphertextBlob** *(bytes) --*

              The encrypted data key. When you use the HTTP API or the AWS CLI, the value is
              Base64-encoded. Otherwise, it is not Base64-encoded.

            - **KeyId** *(string) --*

              The identifier of the CMK that encrypted the data key.
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
    def generate_random(
        self, NumberOfBytes: int = None, CustomKeyStoreId: str = None
    ) -> ClientGenerateRandomResponseTypeDef:
        """
        Returns a random byte string that is cryptographically secure.

        By default, the random byte string is generated in AWS KMS. To generate the byte string in
        the AWS CloudHSM cluster that is associated with a `custom key store
        <https://docs.aws.amazon.com/kms/latest/developerguide/custom-key-store-overview.html>`__ ,
        specify the custom key store ID.

        For more information about entropy and random number generation, see the `AWS Key Management
        Service Cryptographic Details
        <https://d0.awsstatic.com/whitepapers/KMS-Cryptographic-Details.pdf>`__ whitepaper.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/GenerateRandom>`_

        **Request Syntax**
        ::

          response = client.generate_random(
              NumberOfBytes=123,
              CustomKeyStoreId='string'
          )
        :type NumberOfBytes: integer
        :param NumberOfBytes:

          The length of the byte string.

        :type CustomKeyStoreId: string
        :param CustomKeyStoreId:

          Generates the random byte string in the AWS CloudHSM cluster that is associated with the
          specified `custom key store
          <https://docs.aws.amazon.com/kms/latest/developerguide/custom-key-store-overview.html>`__
          . To find the ID of a custom key store, use the  DescribeCustomKeyStores operation.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Plaintext': b'bytes'
            }
          **Response Structure**

          - *(dict) --*

            - **Plaintext** *(bytes) --*

              The random byte string. When you use the HTTP API or the AWS CLI, the value is
              Base64-encoded. Otherwise, it is not Base64-encoded.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_key_policy(self, KeyId: str, PolicyName: str) -> ClientGetKeyPolicyResponseTypeDef:
        """
        Gets a key policy attached to the specified customer master key (CMK). You cannot perform
        this operation on a CMK in a different AWS account.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/GetKeyPolicy>`_

        **Request Syntax**
        ::

          response = client.get_key_policy(
              KeyId='string',
              PolicyName='string'
          )
        :type KeyId: string
        :param KeyId: **[REQUIRED]**

          A unique identifier for the customer master key (CMK).

          Specify the key ID or the Amazon Resource Name (ARN) of the CMK.

          For example:

          * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``

          * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``

          To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey .

        :type PolicyName: string
        :param PolicyName: **[REQUIRED]**

          Specifies the name of the key policy. The only valid name is ``default`` . To get the
          names of key policies, use  ListKeyPolicies .

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Policy': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Policy** *(string) --*

              A key policy document in JSON format.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_key_rotation_status(self, KeyId: str) -> ClientGetKeyRotationStatusResponseTypeDef:
        """
        Gets a Boolean value that indicates whether `automatic rotation of the key material
        <https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html>`__ is enabled for
        the specified customer master key (CMK).

        You cannot enable automatic rotation of asymmetric CMKs, CMKs with imported key material, or
        CMKs in a `custom key store
        <https://docs.aws.amazon.com/kms/latest/developerguide/custom-key-store-overview.html>`__ .
        The key rotation status for these CMKs is always ``false`` .

        The CMK that you use for this operation must be in a compatible key state. For details, see
        `How Key State Affects Use of a Customer Master Key
        <https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`__ in the *AWS Key
        Management Service Developer Guide* .

        * Disabled: The key rotation status does not change when you disable a CMK. However, while
        the CMK is disabled, AWS KMS does not rotate the backing key.

        * Pending deletion: While a CMK is pending deletion, its key rotation status is ``false``
        and AWS KMS does not rotate the backing key. If you cancel the deletion, the original key
        rotation status is restored.

        To perform this operation on a CMK in a different AWS account, specify the key ARN in the
        value of the ``KeyId`` parameter.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/GetKeyRotationStatus>`_

        **Request Syntax**
        ::

          response = client.get_key_rotation_status(
              KeyId='string'
          )
        :type KeyId: string
        :param KeyId: **[REQUIRED]**

          A unique identifier for the customer master key (CMK).

          Specify the key ID or the Amazon Resource Name (ARN) of the CMK. To specify a CMK in a
          different AWS account, you must use the key ARN.

          For example:

          * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``

          * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``

          To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey .

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'KeyRotationEnabled': True|False
            }
          **Response Structure**

          - *(dict) --*

            - **KeyRotationEnabled** *(boolean) --*

              A Boolean value that specifies whether key rotation is enabled.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_parameters_for_import(
        self,
        KeyId: str,
        WrappingAlgorithm: Literal["RSAES_PKCS1_V1_5", "RSAES_OAEP_SHA_1", "RSAES_OAEP_SHA_256"],
        WrappingKeySpec: str,
    ) -> ClientGetParametersForImportResponseTypeDef:
        """
        Returns the items you need to import key material into a symmetric, customer managed
        customer master key (CMK). For more information about importing key material into AWS KMS,
        see `Importing Key Material
        <https://docs.aws.amazon.com/kms/latest/developerguide/importing-keys.html>`__ in the *AWS
        Key Management Service Developer Guide* .

        This operation returns a public key and an import token. Use the public key to encrypt the
        symmetric key material. Store the import token to send with a subsequent  ImportKeyMaterial
        request.

        You must specify the key ID of the symmetric CMK into which you will import key material.
        This CMK's ``Origin`` must be ``EXTERNAL`` . You must also specify the wrapping algorithm
        and type of wrapping key (public key) that you will use to encrypt the key material. You
        cannot perform this operation on an asymmetric CMK or on any CMK in a different AWS account.

        To import key material, you must use the public key and import token from the same response.
        These items are valid for 24 hours. The expiration date and time appear in the
        ``GetParametersForImport`` response. You cannot use an expired token in an
        ImportKeyMaterial request. If your key and token expire, send another
        ``GetParametersForImport`` request.

        The CMK that you use for this operation must be in a compatible key state. For details, see
        `How Key State Affects Use of a Customer Master Key
        <https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`__ in the *AWS Key
        Management Service Developer Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/GetParametersForImport>`_

        **Request Syntax**
        ::

          response = client.get_parameters_for_import(
              KeyId='string',
              WrappingAlgorithm='RSAES_PKCS1_V1_5'|'RSAES_OAEP_SHA_1'|'RSAES_OAEP_SHA_256',
              WrappingKeySpec='RSA_2048'
          )
        :type KeyId: string
        :param KeyId: **[REQUIRED]**

          The identifier of the symmetric CMK into which you will import key material. The
          ``Origin`` of the CMK must be ``EXTERNAL`` .

          Specify the key ID or the Amazon Resource Name (ARN) of the CMK.

          For example:

          * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``

          * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``

          To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey .

        :type WrappingAlgorithm: string
        :param WrappingAlgorithm: **[REQUIRED]**

          The algorithm you will use to encrypt the key material before importing it with
          ImportKeyMaterial . For more information, see `Encrypt the Key Material
          <https://docs.aws.amazon.com/kms/latest/developerguide/importing-keys-encrypt-key-material.html>`__
          in the *AWS Key Management Service Developer Guide* .

        :type WrappingKeySpec: string
        :param WrappingKeySpec: **[REQUIRED]**

          The type of wrapping key (public key) to return in the response. Only 2048-bit RSA public
          keys are supported.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'KeyId': 'string',
                'ImportToken': b'bytes',
                'PublicKey': b'bytes',
                'ParametersValidTo': datetime(2015, 1, 1)
            }
          **Response Structure**

          - *(dict) --*

            - **KeyId** *(string) --*

              The identifier of the CMK to use in a subsequent  ImportKeyMaterial request. This is
              the same CMK specified in the ``GetParametersForImport`` request.

            - **ImportToken** *(bytes) --*

              The import token to send in a subsequent  ImportKeyMaterial request.

            - **PublicKey** *(bytes) --*

              The public key to use to encrypt the key material before importing it with
              ImportKeyMaterial .

            - **ParametersValidTo** *(datetime) --*

              The time at which the import token and public key are no longer valid. After this
              time, you cannot use them to make an  ImportKeyMaterial request and you must send
              another ``GetParametersForImport`` request to get new ones.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_public_key(
        self, KeyId: str, GrantTokens: List[str] = None
    ) -> ClientGetPublicKeyResponseTypeDef:
        """
        Returns the public key of an asymmetric CMK. Unlike the private key of a asymmetric CMK,
        which never leaves AWS KMS unencrypted, callers with ``kms:GetPublicKey`` permission can
        download the public key of an asymmetric CMK. You can share the public key to allow others
        to encrypt messages and verify signatures outside of AWS KMS. For information about
        symmetric and asymmetric CMKs, see `Using Symmetric and Asymmetric CMKs
        <https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html>`__ in the
        *AWS Key Management Service Developer Guide* .

        You do not need to download the public key. Instead, you can use the public key within AWS
        KMS by calling the  Encrypt ,  ReEncrypt , or  Verify operations with the identifier of an
        asymmetric CMK. When you use the public key within AWS KMS, you benefit from the
        authentication, authorization, and logging that are part of every AWS KMS operation. You
        also reduce of risk of encrypting data that cannot be decrypted. These features are not
        effective outside of AWS KMS. For details, see `Special Considerations for Downloading
        Public Keys <kms/latest/developerguide/get-public-key.html#get-public-key-considerations>`__
        .

        To help you use the public key safely outside of AWS KMS, ``GetPublicKey`` returns important
        information about the public key in the response, including:

        * `CustomerMasterKeySpec
        <https://docs.aws.amazon.com/kms/latest/APIReference/API_GetPublicKey.html#KMS-GetPublicKey-response-CustomerMasterKeySpec>`__
        : The type of key material in the public key, such as ``RSA_4096`` or ``ECC_NIST_P521`` .

        * `KeyUsage
        <https://docs.aws.amazon.com/kms/latest/APIReference/API_GetPublicKey.html#KMS-GetPublicKey-response-KeyUsage>`__
        : Whether the key is used for encryption or signing.

        * `EncryptionAlgorithms
        <https://docs.aws.amazon.com/kms/latest/APIReference/API_GetPublicKey.html#KMS-GetPublicKey-response-EncryptionAlgorithms>`__
        or `SigningAlgorithms
        <https://docs.aws.amazon.com/kms/latest/APIReference/API_GetPublicKey.html#KMS-GetPublicKey-response-SigningAlgorithms>`__
        : A list of the encryption algorithms or the signing algorithms for the key.

        Although AWS KMS cannot enforce these restrictions on external operations, it is crucial
        that you use this information to prevent the public key from being used improperly. For
        example, you can prevent a public signing key from being used encrypt data, or prevent a
        public key from being used with an encryption algorithm that is not supported by AWS KMS.
        You can also avoid errors, such as using the wrong signing algorithm in a verification
        operation.

        The CMK that you use for this operation must be in a compatible key state. For details, see
        `How Key State Affects Use of a Customer Master Key
        <https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`__ in the *AWS Key
        Management Service Developer Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/GetPublicKey>`_

        **Request Syntax**
        ::

          response = client.get_public_key(
              KeyId='string',
              GrantTokens=[
                  'string',
              ]
          )
        :type KeyId: string
        :param KeyId: **[REQUIRED]**

          Identifies the asymmetric CMK that includes the public key.

          To specify a CMK, use its key ID, Amazon Resource Name (ARN), alias name, or alias ARN.
          When using an alias name, prefix it with ``"alias/"`` . To specify a CMK in a different
          AWS account, you must use the key ARN or alias ARN.

          For example:

          * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``

          * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``

          * Alias name: ``alias/ExampleAlias``

          * Alias ARN: ``arn:aws:kms:us-east-2:111122223333:alias/ExampleAlias``

          To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey . To get the alias
          name and alias ARN, use  ListAliases .

        :type GrantTokens: list
        :param GrantTokens:

          A list of grant tokens.

          For more information, see `Grant Tokens
          <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token>`__ in
          the *AWS Key Management Service Developer Guide* .

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'KeyId': 'string',
                'PublicKey': b'bytes',
                'CustomerMasterKeySpec':
                'RSA_2048'|'RSA_3072'|'RSA_4096'|'ECC_NIST_P256'|'ECC_NIST_P384'
                |'ECC_NIST_P521'|'ECC_SECG_P256K1'|'SYMMETRIC_DEFAULT',
                'KeyUsage': 'SIGN_VERIFY'|'ENCRYPT_DECRYPT',
                'EncryptionAlgorithms': [
                    'SYMMETRIC_DEFAULT'|'RSAES_OAEP_SHA_1'|'RSAES_OAEP_SHA_256',
                ],
                'SigningAlgorithms': [
                    'RSASSA_PSS_SHA_256'|'RSASSA_PSS_SHA_384'|'RSASSA_PSS_SHA_512'
                    |'RSASSA_PKCS1_V1_5_SHA_256'|'RSASSA_PKCS1_V1_5_SHA_384'
                    |'RSASSA_PKCS1_V1_5_SHA_512'|'ECDSA_SHA_256'|'ECDSA_SHA_384'|'ECDSA_SHA_512',
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **KeyId** *(string) --*

              The identifier of the asymmetric CMK from which the public key was downloaded.

            - **PublicKey** *(bytes) --*

              The exported public key.

              This value is returned as a binary `Distinguished Encoding Rules
              <https://www.itu.int/ITU-T/studygroups/com17/languages/X.690-0207.pdf>`__
              (DER)-encoded object. To decode it, use an ASN.1 parsing tool, such as `OpenSSL
              asn1parse <https://www.openssl.org/docs/man1.0.2/man1/asn1parse.html>`__ .

            - **CustomerMasterKeySpec** *(string) --*

              The type of the of the public key that was downloaded.

            - **KeyUsage** *(string) --*

              The permitted use of the public key. Valid values are ``ENCRYPT_DECRYPT`` or
              ``SIGN_VERIFY`` .

              This information is critical. If a public key with ``SIGN_VERIFY`` key usage encrypts
              data outside of AWS KMS, the ciphertext cannot be decrypted.

            - **EncryptionAlgorithms** *(list) --*

              The encryption algorithms that AWS KMS supports for this key.

              This information is critical. If a public key encrypts data outside of AWS KMS by
              using an unsupported encryption algorithm, the ciphertext cannot be decrypted.

              This field appears in the response only when the ``KeyUsage`` of the public key is
              ``ENCRYPT_DECRYPT`` .

              - *(string) --*

            - **SigningAlgorithms** *(list) --*

              The signing algorithms that AWS KMS supports for this key.

              This field appears in the response only when the ``KeyUsage`` of the public key is
              ``SIGN_VERIFY`` .

              - *(string) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def import_key_material(
        self,
        KeyId: str,
        ImportToken: bytes,
        EncryptedKeyMaterial: bytes,
        ValidTo: datetime = None,
        ExpirationModel: Literal["KEY_MATERIAL_EXPIRES", "KEY_MATERIAL_DOES_NOT_EXPIRE"] = None,
    ) -> Dict[str, Any]:
        """
        Imports key material into an existing symmetric AWS KMS customer master key (CMK) that was
        created without key material. After you successfully import key material into a CMK, you can
        `reimport the same key material
        <https://docs.aws.amazon.com/kms/latest/developerguide/importing-keys.html#reimport-key-material>`__
        into that CMK, but you cannot import different key material.

        You cannot perform this operation on an asymmetric CMK or on any CMK in a different AWS
        account. For more information about creating CMKs with no key material and then importing
        key material, see `Importing Key Material
        <https://docs.aws.amazon.com/kms/latest/developerguide/importing-keys.html>`__ in the *AWS
        Key Management Service Developer Guide* .

        Before using this operation, call  GetParametersForImport . Its response includes a public
        key and an import token. Use the public key to encrypt the key material. Then, submit the
        import token from the same ``GetParametersForImport`` response.

        When calling this operation, you must specify the following values:

        * The key ID or key ARN of a CMK with no key material. Its ``Origin`` must be ``EXTERNAL`` .
        To create a CMK with no key material, call  CreateKey and set the value of its ``Origin``
        parameter to ``EXTERNAL`` . To get the ``Origin`` of a CMK, call  DescribeKey .)

        * The encrypted key material. To get the public key to encrypt the key material, call
        GetParametersForImport .

        * The import token that  GetParametersForImport returned. You must use a public key and
        token from the same ``GetParametersForImport`` response.

        * Whether the key material expires and if so, when. If you set an expiration date, AWS KMS
        deletes the key material from the CMK on the specified date, and the CMK becomes unusable.
        To use the CMK again, you must reimport the same key material. The only way to change an
        expiration date is by reimporting the same key material and specifying a new expiration
        date.

        When this operation is successful, the key state of the CMK changes from ``PendingImport``
        to ``Enabled`` , and you can use the CMK.

        If this operation fails, use the exception to help determine the problem. If the error is
        related to the key material, the import token, or wrapping key, use  GetParametersForImport
        to get a new public key and import token for the CMK and repeat the import procedure. For
        help, see `How To Import Key Material
        <https://docs.aws.amazon.com/kms/latest/developerguide/importing-keys.html#importing-keys-overview>`__
        in the *AWS Key Management Service Developer Guide* .

        The CMK that you use for this operation must be in a compatible key state. For details, see
        `How Key State Affects Use of a Customer Master Key
        <https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`__ in the *AWS Key
        Management Service Developer Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/ImportKeyMaterial>`_

        **Request Syntax**
        ::

          response = client.import_key_material(
              KeyId='string',
              ImportToken=b'bytes',
              EncryptedKeyMaterial=b'bytes',
              ValidTo=datetime(2015, 1, 1),
              ExpirationModel='KEY_MATERIAL_EXPIRES'|'KEY_MATERIAL_DOES_NOT_EXPIRE'
          )
        :type KeyId: string
        :param KeyId: **[REQUIRED]**

          The identifier of the symmetric CMK that receives the imported key material. The CMK's
          ``Origin`` must be ``EXTERNAL`` . This must be the same CMK specified in the ``KeyID``
          parameter of the corresponding  GetParametersForImport request.

          Specify the key ID or the Amazon Resource Name (ARN) of the CMK.

          For example:

          * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``

          * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``

          To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey .

        :type ImportToken: bytes
        :param ImportToken: **[REQUIRED]**

          The import token that you received in the response to a previous  GetParametersForImport
          request. It must be from the same response that contained the public key that you used to
          encrypt the key material.

        :type EncryptedKeyMaterial: bytes
        :param EncryptedKeyMaterial: **[REQUIRED]**

          The encrypted key material to import. The key material must be encrypted with the public
          wrapping key that  GetParametersForImport returned, using the wrapping algorithm that you
          specified in the same ``GetParametersForImport`` request.

        :type ValidTo: datetime
        :param ValidTo:

          The time at which the imported key material expires. When the key material expires, AWS
          KMS deletes the key material and the CMK becomes unusable. You must omit this parameter
          when the ``ExpirationModel`` parameter is set to ``KEY_MATERIAL_DOES_NOT_EXPIRE`` .
          Otherwise it is required.

        :type ExpirationModel: string
        :param ExpirationModel:

          Specifies whether the key material expires. The default is ``KEY_MATERIAL_EXPIRES`` , in
          which case you must include the ``ValidTo`` parameter. When this parameter is set to
          ``KEY_MATERIAL_DOES_NOT_EXPIRE`` , you must omit the ``ValidTo`` parameter.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_aliases(
        self, KeyId: str = None, Limit: int = None, Marker: str = None
    ) -> ClientListAliasesResponseTypeDef:
        """
        Gets a list of aliases in the caller's AWS account and region. You cannot list aliases in
        other accounts. For more information about aliases, see  CreateAlias .

        By default, the ListAliases command returns all aliases in the account and region. To get
        only the aliases that point to a particular customer master key (CMK), use the ``KeyId``
        parameter.

        The ``ListAliases`` response can include aliases that you created and associated with your
        customer managed CMKs, and aliases that AWS created and associated with AWS managed CMKs in
        your account. You can recognize AWS aliases because their names have the format
        ``aws/<service-name>`` , such as ``aws/dynamodb`` .

        The response might also include aliases that have no ``TargetKeyId`` field. These are
        predefined aliases that AWS has created but has not yet associated with a CMK. Aliases that
        AWS creates in your account, including predefined aliases, do not count against your `AWS
        KMS aliases limit
        <https://docs.aws.amazon.com/kms/latest/developerguide/limits.html#aliases-limit>`__ .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/ListAliases>`_

        **Request Syntax**
        ::

          response = client.list_aliases(
              KeyId='string',
              Limit=123,
              Marker='string'
          )
        :type KeyId: string
        :param KeyId:

          Lists only aliases that refer to the specified CMK. The value of this parameter can be the
          ID or Amazon Resource Name (ARN) of a CMK in the caller's account and region. You cannot
          use an alias name or alias ARN in this value.

          This parameter is optional. If you omit it, ``ListAliases`` returns all aliases in the
          account and region.

        :type Limit: integer
        :param Limit:

          Use this parameter to specify the maximum number of items to return. When this value is
          present, AWS KMS does not return more than the specified number of items, but it might
          return fewer.

          This value is optional. If you include a value, it must be between 1 and 100, inclusive.
          If you do not include a value, it defaults to 50.

        :type Marker: string
        :param Marker:

          Use this parameter in a subsequent request after you receive a response with truncated
          results. Set it to the value of ``NextMarker`` from the truncated response you just
          received.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Aliases': [
                    {
                        'AliasName': 'string',
                        'AliasArn': 'string',
                        'TargetKeyId': 'string'
                    },
                ],
                'NextMarker': 'string',
                'Truncated': True|False
            }
          **Response Structure**

          - *(dict) --*

            - **Aliases** *(list) --*

              A list of aliases.

              - *(dict) --*

                Contains information about an alias.

                - **AliasName** *(string) --*

                  String that contains the alias. This value begins with ``alias/`` .

                - **AliasArn** *(string) --*

                  String that contains the key ARN.

                - **TargetKeyId** *(string) --*

                  String that contains the key identifier referred to by the alias.

            - **NextMarker** *(string) --*

              When ``Truncated`` is true, this element is present and contains the value to use for
              the ``Marker`` parameter in a subsequent request.

            - **Truncated** *(boolean) --*

              A flag that indicates whether there are more items in the list. When this value is
              true, the list in this response is truncated. To get more items, pass the value of the
              ``NextMarker`` element in thisresponse to the ``Marker`` parameter in a subsequent
              request.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_grants(
        self, KeyId: str, Limit: int = None, Marker: str = None
    ) -> ClientListGrantsResponseTypeDef:
        """
        Gets a list of all grants for the specified customer master key (CMK).

        To perform this operation on a CMK in a different AWS account, specify the key ARN in the
        value of the ``KeyId`` parameter.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/ListGrants>`_

        **Request Syntax**
        ::

          response = client.list_grants(
              Limit=123,
              Marker='string',
              KeyId='string'
          )
        :type Limit: integer
        :param Limit:

          Use this parameter to specify the maximum number of items to return. When this value is
          present, AWS KMS does not return more than the specified number of items, but it might
          return fewer.

          This value is optional. If you include a value, it must be between 1 and 100, inclusive.
          If you do not include a value, it defaults to 50.

        :type Marker: string
        :param Marker:

          Use this parameter in a subsequent request after you receive a response with truncated
          results. Set it to the value of ``NextMarker`` from the truncated response you just
          received.

        :type KeyId: string
        :param KeyId: **[REQUIRED]**

          A unique identifier for the customer master key (CMK).

          Specify the key ID or the Amazon Resource Name (ARN) of the CMK. To specify a CMK in a
          different AWS account, you must use the key ARN.

          For example:

          * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``

          * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``

          To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey .

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Grants': [
                    {
                        'KeyId': 'string',
                        'GrantId': 'string',
                        'Name': 'string',
                        'CreationDate': datetime(2015, 1, 1),
                        'GranteePrincipal': 'string',
                        'RetiringPrincipal': 'string',
                        'IssuingAccount': 'string',
                        'Operations': [
                            'Decrypt'|'Encrypt'|'GenerateDataKey'|'GenerateDataKeyWithoutPlaintext'
                            |'ReEncryptFrom'|'ReEncryptTo'|'Sign'|'Verify'|'GetPublicKey'
                            |'CreateGrant'|'RetireGrant'|'DescribeKey'|'GenerateDataKeyPair'
                            |'GenerateDataKeyPairWithoutPlaintext',
                        ],
                        'Constraints': {
                            'EncryptionContextSubset': {
                                'string': 'string'
                            },
                            'EncryptionContextEquals': {
                                'string': 'string'
                            }
                        }
                    },
                ],
                'NextMarker': 'string',
                'Truncated': True|False
            }
          **Response Structure**

          - *(dict) --*

            - **Grants** *(list) --*

              A list of grants.

              - *(dict) --*

                Contains information about an entry in a list of grants.

                - **KeyId** *(string) --*

                  The unique identifier for the customer master key (CMK) to which the grant
                  applies.

                - **GrantId** *(string) --*

                  The unique identifier for the grant.

                - **Name** *(string) --*

                  The friendly name that identifies the grant. If a name was provided in the
                  CreateGrant request, that name is returned. Otherwise this value is null.

                - **CreationDate** *(datetime) --*

                  The date and time when the grant was created.

                - **GranteePrincipal** *(string) --*

                  The principal that receives the grant's permissions.

                - **RetiringPrincipal** *(string) --*

                  The principal that can retire the grant.

                - **IssuingAccount** *(string) --*

                  The AWS account under which the grant was issued.

                - **Operations** *(list) --*

                  The list of operations permitted by the grant.

                  - *(string) --*

                - **Constraints** *(dict) --*

                  A list of key-value pairs that must be present in the encryption context of
                  certain subsequent operations that the grant allows.

                  - **EncryptionContextSubset** *(dict) --*

                    A list of key-value pairs that must be included in the encryption context of the
                    cryptographic operation request. The grant allows the cryptographic operation
                    only when the encryption context in the request includes the key-value pairs
                    specified in this constraint, although it can include additional key-value
                    pairs.

                    - *(string) --*

                      - *(string) --*

                  - **EncryptionContextEquals** *(dict) --*

                    A list of key-value pairs that must match the encryption context in the
                    cryptographic operation request. The grant allows the operation only when the
                    encryption context in the request is the same as the encryption context
                    specified in this constraint.

                    - *(string) --*

                      - *(string) --*

            - **NextMarker** *(string) --*

              When ``Truncated`` is true, this element is present and contains the value to use for
              the ``Marker`` parameter in a subsequent request.

            - **Truncated** *(boolean) --*

              A flag that indicates whether there are more items in the list. When this value is
              true, the list in this response is truncated. To get more items, pass the value of the
              ``NextMarker`` element in thisresponse to the ``Marker`` parameter in a subsequent
              request.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_key_policies(
        self, KeyId: str, Limit: int = None, Marker: str = None
    ) -> ClientListKeyPoliciesResponseTypeDef:
        """
        Gets the names of the key policies that are attached to a customer master key (CMK). This
        operation is designed to get policy names that you can use in a  GetKeyPolicy operation.
        However, the only valid policy name is ``default`` . You cannot perform this operation on a
        CMK in a different AWS account.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/ListKeyPolicies>`_

        **Request Syntax**
        ::

          response = client.list_key_policies(
              KeyId='string',
              Limit=123,
              Marker='string'
          )
        :type KeyId: string
        :param KeyId: **[REQUIRED]**

          A unique identifier for the customer master key (CMK).

          Specify the key ID or the Amazon Resource Name (ARN) of the CMK.

          For example:

          * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``

          * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``

          To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey .

        :type Limit: integer
        :param Limit:

          Use this parameter to specify the maximum number of items to return. When this value is
          present, AWS KMS does not return more than the specified number of items, but it might
          return fewer.

          This value is optional. If you include a value, it must be between 1 and 1000, inclusive.
          If you do not include a value, it defaults to 100.

          Only one policy can be attached to a key.

        :type Marker: string
        :param Marker:

          Use this parameter in a subsequent request after you receive a response with truncated
          results. Set it to the value of ``NextMarker`` from the truncated response you just
          received.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'PolicyNames': [
                    'string',
                ],
                'NextMarker': 'string',
                'Truncated': True|False
            }
          **Response Structure**

          - *(dict) --*

            - **PolicyNames** *(list) --*

              A list of key policy names. The only valid value is ``default`` .

              - *(string) --*

            - **NextMarker** *(string) --*

              When ``Truncated`` is true, this element is present and contains the value to use for
              the ``Marker`` parameter in a subsequent request.

            - **Truncated** *(boolean) --*

              A flag that indicates whether there are more items in the list. When this value is
              true, the list in this response is truncated. To get more items, pass the value of the
              ``NextMarker`` element in thisresponse to the ``Marker`` parameter in a subsequent
              request.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_keys(self, Limit: int = None, Marker: str = None) -> ClientListKeysResponseTypeDef:
        """
        Gets a list of all customer master keys (CMKs) in the caller's AWS account and Region.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/ListKeys>`_

        **Request Syntax**
        ::

          response = client.list_keys(
              Limit=123,
              Marker='string'
          )
        :type Limit: integer
        :param Limit:

          Use this parameter to specify the maximum number of items to return. When this value is
          present, AWS KMS does not return more than the specified number of items, but it might
          return fewer.

          This value is optional. If you include a value, it must be between 1 and 1000, inclusive.
          If you do not include a value, it defaults to 100.

        :type Marker: string
        :param Marker:

          Use this parameter in a subsequent request after you receive a response with truncated
          results. Set it to the value of ``NextMarker`` from the truncated response you just
          received.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Keys': [
                    {
                        'KeyId': 'string',
                        'KeyArn': 'string'
                    },
                ],
                'NextMarker': 'string',
                'Truncated': True|False
            }
          **Response Structure**

          - *(dict) --*

            - **Keys** *(list) --*

              A list of customer master keys (CMKs).

              - *(dict) --*

                Contains information about each entry in the key list.

                - **KeyId** *(string) --*

                  Unique identifier of the key.

                - **KeyArn** *(string) --*

                  ARN of the key.

            - **NextMarker** *(string) --*

              When ``Truncated`` is true, this element is present and contains the value to use for
              the ``Marker`` parameter in a subsequent request.

            - **Truncated** *(boolean) --*

              A flag that indicates whether there are more items in the list. When this value is
              true, the list in this response is truncated. To get more items, pass the value of the
              ``NextMarker`` element in thisresponse to the ``Marker`` parameter in a subsequent
              request.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_resource_tags(
        self, KeyId: str, Limit: int = None, Marker: str = None
    ) -> ClientListResourceTagsResponseTypeDef:
        """
        Returns a list of all tags for the specified customer master key (CMK).

        You cannot perform this operation on a CMK in a different AWS account.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/ListResourceTags>`_

        **Request Syntax**
        ::

          response = client.list_resource_tags(
              KeyId='string',
              Limit=123,
              Marker='string'
          )
        :type KeyId: string
        :param KeyId: **[REQUIRED]**

          A unique identifier for the customer master key (CMK).

          Specify the key ID or the Amazon Resource Name (ARN) of the CMK.

          For example:

          * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``

          * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``

          To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey .

        :type Limit: integer
        :param Limit:

          Use this parameter to specify the maximum number of items to return. When this value is
          present, AWS KMS does not return more than the specified number of items, but it might
          return fewer.

          This value is optional. If you include a value, it must be between 1 and 50, inclusive. If
          you do not include a value, it defaults to 50.

        :type Marker: string
        :param Marker:

          Use this parameter in a subsequent request after you receive a response with truncated
          results. Set it to the value of ``NextMarker`` from the truncated response you just
          received.

          Do not attempt to construct this value. Use only the value of ``NextMarker`` from the
          truncated response you just received.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Tags': [
                    {
                        'TagKey': 'string',
                        'TagValue': 'string'
                    },
                ],
                'NextMarker': 'string',
                'Truncated': True|False
            }
          **Response Structure**

          - *(dict) --*

            - **Tags** *(list) --*

              A list of tags. Each tag consists of a tag key and a tag value.

              - *(dict) --*

                A key-value pair. A tag consists of a tag key and a tag value. Tag keys and tag
                values are both required, but tag values can be empty (null) strings.

                For information about the rules that apply to tag keys and tag values, see
                `User-Defined Tag Restrictions
                <https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/allocation-tag-restrictions.html>`__
                in the *AWS Billing and Cost Management User Guide* .

                - **TagKey** *(string) --*

                  The key of the tag.

                - **TagValue** *(string) --*

                  The value of the tag.

            - **NextMarker** *(string) --*

              When ``Truncated`` is true, this element is present and contains the value to use for
              the ``Marker`` parameter in a subsequent request.

              Do not assume or infer any information from this value.

            - **Truncated** *(boolean) --*

              A flag that indicates whether there are more items in the list. When this value is
              true, the list in this response is truncated. To get more items, pass the value of the
              ``NextMarker`` element in thisresponse to the ``Marker`` parameter in a subsequent
              request.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_retirable_grants(
        self, RetiringPrincipal: str, Limit: int = None, Marker: str = None
    ) -> ClientListRetirableGrantsResponseTypeDef:
        """
        Returns a list of all grants for which the grant's ``RetiringPrincipal`` matches the one
        specified.

        A typical use is to list all grants that you are able to retire. To retire a grant, use
        RetireGrant .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/ListRetirableGrants>`_

        **Request Syntax**
        ::

          response = client.list_retirable_grants(
              Limit=123,
              Marker='string',
              RetiringPrincipal='string'
          )
        :type Limit: integer
        :param Limit:

          Use this parameter to specify the maximum number of items to return. When this value is
          present, AWS KMS does not return more than the specified number of items, but it might
          return fewer.

          This value is optional. If you include a value, it must be between 1 and 100, inclusive.
          If you do not include a value, it defaults to 50.

        :type Marker: string
        :param Marker:

          Use this parameter in a subsequent request after you receive a response with truncated
          results. Set it to the value of ``NextMarker`` from the truncated response you just
          received.

        :type RetiringPrincipal: string
        :param RetiringPrincipal: **[REQUIRED]**

          The retiring principal for which to list grants.

          To specify the retiring principal, use the `Amazon Resource Name (ARN)
          <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ of an AWS
          principal. Valid AWS principals include AWS accounts (root), IAM users, federated users,
          and assumed role users. For examples of the ARN syntax for specifying a principal, see
          `AWS Identity and Access Management (IAM)
          <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-iam>`__
          in the Example ARNs section of the *Amazon Web Services General Reference* .

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Grants': [
                    {
                        'KeyId': 'string',
                        'GrantId': 'string',
                        'Name': 'string',
                        'CreationDate': datetime(2015, 1, 1),
                        'GranteePrincipal': 'string',
                        'RetiringPrincipal': 'string',
                        'IssuingAccount': 'string',
                        'Operations': [
                            'Decrypt'|'Encrypt'|'GenerateDataKey'|'GenerateDataKeyWithoutPlaintext'
                            |'ReEncryptFrom'|'ReEncryptTo'|'Sign'|'Verify'|'GetPublicKey'
                            |'CreateGrant'|'RetireGrant'|'DescribeKey'|'GenerateDataKeyPair'
                            |'GenerateDataKeyPairWithoutPlaintext',
                        ],
                        'Constraints': {
                            'EncryptionContextSubset': {
                                'string': 'string'
                            },
                            'EncryptionContextEquals': {
                                'string': 'string'
                            }
                        }
                    },
                ],
                'NextMarker': 'string',
                'Truncated': True|False
            }
          **Response Structure**

          - *(dict) --*

            - **Grants** *(list) --*

              A list of grants.

              - *(dict) --*

                Contains information about an entry in a list of grants.

                - **KeyId** *(string) --*

                  The unique identifier for the customer master key (CMK) to which the grant
                  applies.

                - **GrantId** *(string) --*

                  The unique identifier for the grant.

                - **Name** *(string) --*

                  The friendly name that identifies the grant. If a name was provided in the
                  CreateGrant request, that name is returned. Otherwise this value is null.

                - **CreationDate** *(datetime) --*

                  The date and time when the grant was created.

                - **GranteePrincipal** *(string) --*

                  The principal that receives the grant's permissions.

                - **RetiringPrincipal** *(string) --*

                  The principal that can retire the grant.

                - **IssuingAccount** *(string) --*

                  The AWS account under which the grant was issued.

                - **Operations** *(list) --*

                  The list of operations permitted by the grant.

                  - *(string) --*

                - **Constraints** *(dict) --*

                  A list of key-value pairs that must be present in the encryption context of
                  certain subsequent operations that the grant allows.

                  - **EncryptionContextSubset** *(dict) --*

                    A list of key-value pairs that must be included in the encryption context of the
                    cryptographic operation request. The grant allows the cryptographic operation
                    only when the encryption context in the request includes the key-value pairs
                    specified in this constraint, although it can include additional key-value
                    pairs.

                    - *(string) --*

                      - *(string) --*

                  - **EncryptionContextEquals** *(dict) --*

                    A list of key-value pairs that must match the encryption context in the
                    cryptographic operation request. The grant allows the operation only when the
                    encryption context in the request is the same as the encryption context
                    specified in this constraint.

                    - *(string) --*

                      - *(string) --*

            - **NextMarker** *(string) --*

              When ``Truncated`` is true, this element is present and contains the value to use for
              the ``Marker`` parameter in a subsequent request.

            - **Truncated** *(boolean) --*

              A flag that indicates whether there are more items in the list. When this value is
              true, the list in this response is truncated. To get more items, pass the value of the
              ``NextMarker`` element in thisresponse to the ``Marker`` parameter in a subsequent
              request.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def put_key_policy(
        self, KeyId: str, PolicyName: str, Policy: str, BypassPolicyLockoutSafetyCheck: bool = None
    ) -> None:
        """
        Attaches a key policy to the specified customer master key (CMK). You cannot perform this
        operation on a CMK in a different AWS account.

        For more information about key policies, see `Key Policies
        <https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html>`__ in the *AWS Key
        Management Service Developer Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/PutKeyPolicy>`_

        **Request Syntax**
        ::

          response = client.put_key_policy(
              KeyId='string',
              PolicyName='string',
              Policy='string',
              BypassPolicyLockoutSafetyCheck=True|False
          )
        :type KeyId: string
        :param KeyId: **[REQUIRED]**

          A unique identifier for the customer master key (CMK).

          Specify the key ID or the Amazon Resource Name (ARN) of the CMK.

          For example:

          * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``

          * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``

          To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey .

        :type PolicyName: string
        :param PolicyName: **[REQUIRED]**

          The name of the key policy. The only valid value is ``default`` .

        :type Policy: string
        :param Policy: **[REQUIRED]**

          The key policy to attach to the CMK.

          The key policy must meet the following criteria:

          * If you don't set ``BypassPolicyLockoutSafetyCheck`` to true, the key policy must allow
          the principal that is making the ``PutKeyPolicy`` request to make a subsequent
          ``PutKeyPolicy`` request on the CMK. This reduces the risk that the CMK becomes
          unmanageable. For more information, refer to the scenario in the `Default Key Policy
          <https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html#key-policy-default-allow-root-enable-iam>`__
          section of the *AWS Key Management Service Developer Guide* .

          * Each statement in the key policy must contain one or more principals. The principals in
          the key policy must exist and be visible to AWS KMS. When you create a new AWS principal
          (for example, an IAM user or role), you might need to enforce a delay before including the
          new principal in a key policy because the new principal might not be immediately visible
          to AWS KMS. For more information, see `Changes that I make are not always immediately
          visible
          <https://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_general.html#troubleshoot_general_eventual-consistency>`__
          in the *AWS Identity and Access Management User Guide* .

          The key policy size limit is 32 kilobytes (32768 bytes).

        :type BypassPolicyLockoutSafetyCheck: boolean
        :param BypassPolicyLockoutSafetyCheck:

          A flag to indicate whether to bypass the key policy lockout safety check.

          .. warning::

            Setting this value to true increases the risk that the CMK becomes unmanageable. Do not
            set this value to true indiscriminately.

            For more information, refer to the scenario in the `Default Key Policy
            <https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html#key-policy-default-allow-root-enable-iam>`__
            section in the *AWS Key Management Service Developer Guide* .

          Use this parameter only when you intend to prevent the principal that is making the
          request from making a subsequent ``PutKeyPolicy`` request on the CMK.

          The default value is false.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def re_encrypt(
        self,
        CiphertextBlob: bytes,
        DestinationKeyId: str,
        SourceEncryptionContext: Dict[str, str] = None,
        SourceKeyId: str = None,
        DestinationEncryptionContext: Dict[str, str] = None,
        SourceEncryptionAlgorithm: Literal[
            "SYMMETRIC_DEFAULT", "RSAES_OAEP_SHA_1", "RSAES_OAEP_SHA_256"
        ] = None,
        DestinationEncryptionAlgorithm: Literal[
            "SYMMETRIC_DEFAULT", "RSAES_OAEP_SHA_1", "RSAES_OAEP_SHA_256"
        ] = None,
        GrantTokens: List[str] = None,
    ) -> ClientReEncryptResponseTypeDef:
        """
        Decrypts ciphertext and then reencrypts it entirely within AWS KMS. You can use this
        operation to change the customer master key (CMK) under which data is encrypted, such as
        when you `manually rotate
        <kms/latest/developerguide/rotate-keys.html#rotate-keys-manually>`__ a CMK or change the CMK
        that protects a ciphertext. You can also use it to reencrypt ciphertext under the same CMK,
        such as to change the encryption context of a ciphertext.

        The ``ReEncrypt`` operation can decrypt ciphertext that was encrypted by using an AWS KMS
        CMK in an AWS KMS operation, such as  Encrypt or  GenerateDataKey . It can also decrypt
        ciphertext that was encrypted by using the public key of an asymmetric CMK outside of AWS
        KMS. However, it cannot decrypt ciphertext produced by other libraries, such as the `AWS
        Encryption SDK <https://docs.aws.amazon.com/encryption-sdk/latest/developer-guide/>`__ or
        `Amazon S3 client-side encryption
        <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingClientSideEncryption.html>`__ . These
        libraries return a ciphertext format that is incompatible with AWS KMS.

        When you use the ``ReEncrypt`` operation, you need to provide information for the decrypt
        operation and the subsequent encrypt operation.

        * If your ciphertext was encrypted under an asymmetric CMK, you must identify the *source
        CMK* , that is, the CMK that encrypted the ciphertext. You must also supply the encryption
        algorithm that was used. This information is required to decrypt the data.

        * It is optional, but you can specify a source CMK even when the ciphertext was encrypted
        under a symmetric CMK. This ensures that the ciphertext is decrypted only by using a
        particular CMK. If the CMK that you specify cannot decrypt the ciphertext, the ``ReEncrypt``
        operation fails.

        * To reencrypt the data, you must specify the *destination CMK* , that is, the CMK that
        re-encrypts the data after it is decrypted. You can select a symmetric or asymmetric CMK. If
        the destination CMK is an asymmetric CMK, you must also provide the encryption algorithm.
        The algorithm that you choose must be compatible with the CMK.

        .. warning::

           When you use an asymmetric CMK to encrypt or reencrypt data, be sure to record the CMK
           and encryption algorithm that you choose. You will be required to provide the same CMK
           and encryption algorithm when you decrypt the data. If the CMK and algorithm do not match
           the values used to encrypt the data, the decrypt operation fails. You are not required to
           supply the CMK ID and encryption algorithm when you decrypt with symmetric CMKs because
           AWS KMS stores this information in the ciphertext blob. AWS KMS cannot store metadata in
           ciphertext generated with asymmetric keys. The standard format for asymmetric key
           ciphertext does not include configurable fields.

        Unlike other AWS KMS API operations, ``ReEncrypt`` callers must have two permissions:

        * ``kms:EncryptFrom`` permission on the source CMK

        * ``kms:EncryptTo`` permission on the destination CMK

        To permit reencryption from

        or to a CMK, include the ``"kms:ReEncrypt*"`` permission in your `key policy
        <https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html>`__ . This
        permission is automatically included in the key policy when you use the console to create a
        CMK. But you must include it manually when you create a CMK programmatically or when you use
        the  PutKeyPolicy operation set a key policy.

        The CMK that you use for this operation must be in a compatible key state. For details, see
        `How Key State Affects Use of a Customer Master Key
        <https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`__ in the *AWS Key
        Management Service Developer Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/ReEncrypt>`_

        **Request Syntax**
        ::

          response = client.re_encrypt(
              CiphertextBlob=b'bytes',
              SourceEncryptionContext={
                  'string': 'string'
              },
              SourceKeyId='string',
              DestinationKeyId='string',
              DestinationEncryptionContext={
                  'string': 'string'
              },
              SourceEncryptionAlgorithm='SYMMETRIC_DEFAULT'|'RSAES_OAEP_SHA_1'|'RSAES_OAEP_SHA_256',
              DestinationEncryptionAlgorithm=
                  'SYMMETRIC_DEFAULT'|'RSAES_OAEP_SHA_1'|'RSAES_OAEP_SHA_256',
              GrantTokens=[
                  'string',
              ]
          )
        :type CiphertextBlob: bytes
        :param CiphertextBlob: **[REQUIRED]**

          Ciphertext of the data to reencrypt.

        :type SourceEncryptionContext: dict
        :param SourceEncryptionContext:

          Specifies the encryption context to use to decrypt the ciphertext. Enter the same
          encryption context that was used to encrypt the ciphertext.

          An *encryption context* is a collection of non-secret key-value pairs that represents
          additional authenticated data. When you use an encryption context to encrypt data, you
          must specify the same (an exact case-sensitive match) encryption context to decrypt the
          data. An encryption context is optional when encrypting with a symmetric CMK, but it is
          highly recommended.

          For more information, see `Encryption Context
          <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#encrypt_context>`__
          in the *AWS Key Management Service Developer Guide* .

          - *(string) --*

            - *(string) --*

        :type SourceKeyId: string
        :param SourceKeyId:

          A unique identifier for the CMK that is used to decrypt the ciphertext before it
          reencrypts it using the destination CMK.

          This parameter is required only when the ciphertext was encrypted under an asymmetric CMK.
          Otherwise, AWS KMS uses the metadata that it adds to the ciphertext blob to determine
          which CMK was used to encrypt the ciphertext. However, you can use this parameter to
          ensure that a particular CMK (of any kind) is used to decrypt the ciphertext before it is
          reencrypted.

          If you specify a ``KeyId`` value, the decrypt part of the ``ReEncrypt`` operation succeeds
          only if the specified CMK was used to encrypt the ciphertext.

          To specify a CMK, use its key ID, Amazon Resource Name (ARN), alias name, or alias ARN.
          When using an alias name, prefix it with ``"alias/"`` .

          For example:

          * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``

          * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``

          * Alias name: ``alias/ExampleAlias``

          * Alias ARN: ``arn:aws:kms:us-east-2:111122223333:alias/ExampleAlias``

          To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey . To get the alias
          name and alias ARN, use  ListAliases .

        :type DestinationKeyId: string
        :param DestinationKeyId: **[REQUIRED]**

          A unique identifier for the CMK that is used to reencrypt the data. Specify a symmetric or
          asymmetric CMK with a ``KeyUsage`` value of ``ENCRYPT_DECRYPT`` . To find the ``KeyUsage``
          value of a CMK, use the  DescribeKey operation.

          To specify a CMK, use its key ID, Amazon Resource Name (ARN), alias name, or alias ARN.
          When using an alias name, prefix it with ``"alias/"`` . To specify a CMK in a different
          AWS account, you must use the key ARN or alias ARN.

          For example:

          * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``

          * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``

          * Alias name: ``alias/ExampleAlias``

          * Alias ARN: ``arn:aws:kms:us-east-2:111122223333:alias/ExampleAlias``

          To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey . To get the alias
          name and alias ARN, use  ListAliases .

        :type DestinationEncryptionContext: dict
        :param DestinationEncryptionContext:

          Specifies that encryption context to use when the reencrypting the data.

          A destination encryption context is valid only when the destination CMK is a symmetric
          CMK. The standard ciphertext format for asymmetric CMKs does not include fields for
          metadata.

          An *encryption context* is a collection of non-secret key-value pairs that represents
          additional authenticated data. When you use an encryption context to encrypt data, you
          must specify the same (an exact case-sensitive match) encryption context to decrypt the
          data. An encryption context is optional when encrypting with a symmetric CMK, but it is
          highly recommended.

          For more information, see `Encryption Context
          <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#encrypt_context>`__
          in the *AWS Key Management Service Developer Guide* .

          - *(string) --*

            - *(string) --*

        :type SourceEncryptionAlgorithm: string
        :param SourceEncryptionAlgorithm:

          Specifies the encryption algorithm that AWS KMS will use to decrypt the ciphertext before
          it is reencrypted. The default value, ``SYMMETRIC_DEFAULT`` , represents the algorithm
          used for symmetric CMKs.

          Specify the same algorithm that was used to encrypt the ciphertext. If you specify a
          different algorithm, the decrypt attempt fails.

          This parameter is required only when the ciphertext was encrypted under an asymmetric CMK.

        :type DestinationEncryptionAlgorithm: string
        :param DestinationEncryptionAlgorithm:

          Specifies the encryption algorithm that AWS KMS will use to reecrypt the data after it has
          decrypted it. The default value, ``SYMMETRIC_DEFAULT`` , represents the encryption
          algorithm used for symmetric CMKs.

          This parameter is required only when the destination CMK is an asymmetric CMK.

        :type GrantTokens: list
        :param GrantTokens:

          A list of grant tokens.

          For more information, see `Grant Tokens
          <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token>`__ in
          the *AWS Key Management Service Developer Guide* .

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'CiphertextBlob': b'bytes',
                'SourceKeyId': 'string',
                'KeyId': 'string',
                'SourceEncryptionAlgorithm':
                'SYMMETRIC_DEFAULT'|'RSAES_OAEP_SHA_1'|'RSAES_OAEP_SHA_256',
                'DestinationEncryptionAlgorithm':
                'SYMMETRIC_DEFAULT'|'RSAES_OAEP_SHA_1'|'RSAES_OAEP_SHA_256'
            }
          **Response Structure**

          - *(dict) --*

            - **CiphertextBlob** *(bytes) --*

              The reencrypted data. When you use the HTTP API or the AWS CLI, the value is
              Base64-encoded. Otherwise, it is not Base64-encoded.

            - **SourceKeyId** *(string) --*

              Unique identifier of the CMK used to originally encrypt the data.

            - **KeyId** *(string) --*

              Unique identifier of the CMK used to reencrypt the data.

            - **SourceEncryptionAlgorithm** *(string) --*

              The encryption algorithm that was used to decrypt the ciphertext before it was
              reencrypted.

            - **DestinationEncryptionAlgorithm** *(string) --*

              The encryption algorithm that was used to reencrypt the data.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def retire_grant(self, GrantToken: str = None, KeyId: str = None, GrantId: str = None) -> None:
        """
        Retires a grant. To clean up, you can retire a grant when you're done using it. You should
        revoke a grant when you intend to actively deny operations that depend on it. The following
        are permitted to call this API:

        * The AWS account (root user) under which the grant was created

        * The ``RetiringPrincipal`` , if present in the grant

        * The ``GranteePrincipal`` , if ``RetireGrant`` is an operation specified in the grant

        You must identify the grant to retire by its grant token or by a combination of the grant ID
        and the Amazon Resource Name (ARN) of the customer master key (CMK). A grant token is a
        unique variable-length base64-encoded string. A grant ID is a 64 character unique identifier
        of a grant. The  CreateGrant operation returns both.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/RetireGrant>`_

        **Request Syntax**
        ::

          response = client.retire_grant(
              GrantToken='string',
              KeyId='string',
              GrantId='string'
          )
        :type GrantToken: string
        :param GrantToken:

          Token that identifies the grant to be retired.

        :type KeyId: string
        :param KeyId:

          The Amazon Resource Name (ARN) of the CMK associated with the grant.

          For example:
          ``arn:aws:kms:us-east-2:444455556666:key/1234abcd-12ab-34cd-56ef-1234567890ab``

        :type GrantId: string
        :param GrantId:

          Unique identifier of the grant to retire. The grant ID is returned in the response to a
          ``CreateGrant`` operation.

          * Grant ID Example - 0123456789012345678901234567890123456789012345678901234567890123

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def revoke_grant(self, KeyId: str, GrantId: str) -> None:
        """
        Revokes the specified grant for the specified customer master key (CMK). You can revoke a
        grant to actively deny operations that depend on it.

        To perform this operation on a CMK in a different AWS account, specify the key ARN in the
        value of the ``KeyId`` parameter.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/RevokeGrant>`_

        **Request Syntax**
        ::

          response = client.revoke_grant(
              KeyId='string',
              GrantId='string'
          )
        :type KeyId: string
        :param KeyId: **[REQUIRED]**

          A unique identifier for the customer master key associated with the grant.

          Specify the key ID or the Amazon Resource Name (ARN) of the CMK. To specify a CMK in a
          different AWS account, you must use the key ARN.

          For example:

          * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``

          * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``

          To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey .

        :type GrantId: string
        :param GrantId: **[REQUIRED]**

          Identifier of the grant to be revoked.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def schedule_key_deletion(
        self, KeyId: str, PendingWindowInDays: int = None
    ) -> ClientScheduleKeyDeletionResponseTypeDef:
        """
        Schedules the deletion of a customer master key (CMK). You may provide a waiting period,
        specified in days, before deletion occurs. If you do not provide a waiting period, the
        default period of 30 days is used. When this operation is successful, the key state of the
        CMK changes to ``PendingDeletion`` . Before the waiting period ends, you can use
        CancelKeyDeletion to cancel the deletion of the CMK. After the waiting period ends, AWS KMS
        deletes the CMK and all AWS KMS data associated with it, including all aliases that refer to
        it.

        .. warning::

          Deleting a CMK is a destructive and potentially dangerous operation. When a CMK is
          deleted, all data that was encrypted under the CMK is unrecoverable. To prevent the use of
          a CMK without deleting it, use  DisableKey .

        If you schedule deletion of a CMK from a `custom key store
        <https://docs.aws.amazon.com/kms/latest/developerguide/custom-key-store-overview.html>`__ ,
        when the waiting period expires, ``ScheduleKeyDeletion`` deletes the CMK from AWS KMS. Then
        AWS KMS makes a best effort to delete the key material from the associated AWS CloudHSM
        cluster. However, you might need to manually `delete the orphaned key material
        <https://docs.aws.amazon.com/kms/latest/developerguide/fix-keystore.html#fix-keystore-orphaned-key>`__
        from the cluster and its backups.

        You cannot perform this operation on a CMK in a different AWS account.

        For more information about scheduling a CMK for deletion, see `Deleting Customer Master Keys
        <https://docs.aws.amazon.com/kms/latest/developerguide/deleting-keys.html>`__ in the *AWS
        Key Management Service Developer Guide* .

        The CMK that you use for this operation must be in a compatible key state. For details, see
        `How Key State Affects Use of a Customer Master Key
        <https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`__ in the *AWS Key
        Management Service Developer Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/ScheduleKeyDeletion>`_

        **Request Syntax**
        ::

          response = client.schedule_key_deletion(
              KeyId='string',
              PendingWindowInDays=123
          )
        :type KeyId: string
        :param KeyId: **[REQUIRED]**

          The unique identifier of the customer master key (CMK) to delete.

          Specify the key ID or the Amazon Resource Name (ARN) of the CMK.

          For example:

          * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``

          * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``

          To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey .

        :type PendingWindowInDays: integer
        :param PendingWindowInDays:

          The waiting period, specified in number of days. After the waiting period ends, AWS KMS
          deletes the customer master key (CMK).

          This value is optional. If you include a value, it must be between 7 and 30, inclusive. If
          you do not include a value, it defaults to 30.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'KeyId': 'string',
                'DeletionDate': datetime(2015, 1, 1)
            }
          **Response Structure**

          - *(dict) --*

            - **KeyId** *(string) --*

              The unique identifier of the customer master key (CMK) for which deletion is
              scheduled.

            - **DeletionDate** *(datetime) --*

              The date and time after which AWS KMS deletes the customer master key (CMK).
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def sign(
        self,
        KeyId: str,
        Message: bytes,
        SigningAlgorithm: Literal[
            "RSASSA_PSS_SHA_256",
            "RSASSA_PSS_SHA_384",
            "RSASSA_PSS_SHA_512",
            "RSASSA_PKCS1_V1_5_SHA_256",
            "RSASSA_PKCS1_V1_5_SHA_384",
            "RSASSA_PKCS1_V1_5_SHA_512",
            "ECDSA_SHA_256",
            "ECDSA_SHA_384",
            "ECDSA_SHA_512",
        ],
        MessageType: Literal["RAW", "DIGEST"] = None,
        GrantTokens: List[str] = None,
    ) -> ClientSignResponseTypeDef:
        """
        Creates a `digital signature <https://en.wikipedia.org/wiki/Digital_signature>`__ for a
        message or message digest by using the private key in an asymmetric CMK. To verify the
        signature, use the  Verify operation, or use the public key in the same asymmetric CMK
        outside of AWS KMS. For information about symmetric and asymmetric CMKs, see `Using
        Symmetric and Asymmetric CMKs
        <https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html>`__ in the
        *AWS Key Management Service Developer Guide* .

        Digital signatures are generated and verified by using asymmetric key pair, such as an RSA
        or ECC pair that is represented by an asymmetric customer master key (CMK). The key owner
        (or an authorized user) uses their private key to sign a message. Anyone with the public key
        can verify that the message was signed with that particular private key and that the message
        hasn't changed since it was signed.

        To use the ``Sign`` operation, provide the following information:

        * Use the ``KeyId`` parameter to identify an asymmetric CMK with a ``KeyUsage`` value of
        ``SIGN_VERIFY`` . To get the ``KeyUsage`` value of a CMK, use the  DescribeKey operation.
        The caller must have ``kms:Sign`` permission on the CMK.

        * Use the ``Message`` parameter to specify the message or message digest to sign. You can
        submit messages of up to 4096 bytes. To sign a larger message, generate a hash digest of the
        message, and then provide the hash digest in the ``Message`` parameter. To indicate whether
        the message is a full message or a digest, use the ``MessageType`` parameter.

        * Choose a signing algorithm that is compatible with the CMK.

        .. warning::

          When signing a message, be sure to record the CMK and the signing algorithm. This
          information is required to verify the signature.

        To verify the signature that this operation generates, use the  Verify operation. Or use the
        GetPublicKey operation to download the public key and then use the public key to verify the
        signature outside of AWS KMS.

        The CMK that you use for this operation must be in a compatible key state. For details, see
        `How Key State Affects Use of a Customer Master Key
        <https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`__ in the *AWS Key
        Management Service Developer Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/Sign>`_

        **Request Syntax**
        ::

          response = client.sign(
              KeyId='string',
              Message=b'bytes',
              MessageType='RAW'|'DIGEST',
              GrantTokens=[
                  'string',
              ],
              SigningAlgorithm=
                  'RSASSA_PSS_SHA_256'|'RSASSA_PSS_SHA_384'|'RSASSA_PSS_SHA_512'
                  |'RSASSA_PKCS1_V1_5_SHA_256'|'RSASSA_PKCS1_V1_5_SHA_384'
                  |'RSASSA_PKCS1_V1_5_SHA_512'|'ECDSA_SHA_256'|'ECDSA_SHA_384'|'ECDSA_SHA_512'
          )
        :type KeyId: string
        :param KeyId: **[REQUIRED]**

          Identifies an asymmetric CMK. AWS KMS uses the private key in the asymmetric CMK to sign
          the message. The ``KeyUsage`` type of the CMK must be ``SIGN_VERIFY`` . To find the
          ``KeyUsage`` of a CMK, use the  DescribeKey operation.

          To specify a CMK, use its key ID, Amazon Resource Name (ARN), alias name, or alias ARN.
          When using an alias name, prefix it with ``"alias/"`` . To specify a CMK in a different
          AWS account, you must use the key ARN or alias ARN.

          For example:

          * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``

          * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``

          * Alias name: ``alias/ExampleAlias``

          * Alias ARN: ``arn:aws:kms:us-east-2:111122223333:alias/ExampleAlias``

          To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey . To get the alias
          name and alias ARN, use  ListAliases .

        :type Message: bytes
        :param Message: **[REQUIRED]**

          Specifies the message or message digest to sign. Messages can be 0-4096 bytes. To sign a
          larger message, provide the message digest.

          If you provide a message, AWS KMS generates a hash digest of the message and then signs
          it.

        :type MessageType: string
        :param MessageType:

          Tells AWS KMS whether the value of the ``Message`` parameter is a message or message
          digest. To indicate a message, enter ``RAW`` . To indicate a message digest, enter
          ``DIGEST`` .

        :type GrantTokens: list
        :param GrantTokens:

          A list of grant tokens.

          For more information, see `Grant Tokens
          <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token>`__ in
          the *AWS Key Management Service Developer Guide* .

          - *(string) --*

        :type SigningAlgorithm: string
        :param SigningAlgorithm: **[REQUIRED]**

          Specifies the signing algorithm to use when signing the message.

          Choose an algorithm that is compatible with the type and size of the specified asymmetric
          CMK.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'KeyId': 'string',
                'Signature': b'bytes',
                'SigningAlgorithm':
                'RSASSA_PSS_SHA_256'|'RSASSA_PSS_SHA_384'|'RSASSA_PSS_SHA_512'
                |'RSASSA_PKCS1_V1_5_SHA_256'|'RSASSA_PKCS1_V1_5_SHA_384'
                |'RSASSA_PKCS1_V1_5_SHA_512'|'ECDSA_SHA_256'|'ECDSA_SHA_384'|'ECDSA_SHA_512'
            }
          **Response Structure**

          - *(dict) --*

            - **KeyId** *(string) --*

              The Amazon Resource Name (ARN) of the asymmetric CMK that was used to sign the
              message.

            - **Signature** *(bytes) --*

              The cryptographic signature that was generated for the message.

            - **SigningAlgorithm** *(string) --*

              The signing algorithm that was used to sign the message.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def tag_resource(self, KeyId: str, Tags: List[ClientTagResourceTagsTypeDef]) -> None:
        """
        Adds or edits tags for a customer master key (CMK). You cannot perform this operation on a
        CMK in a different AWS account.

        Each tag consists of a tag key and a tag value. Tag keys and tag values are both required,
        but tag values can be empty (null) strings.

        You can only use a tag key once for each CMK. If you use the tag key again, AWS KMS replaces
        the current tag value with the specified value.

        For information about the rules that apply to tag keys and tag values, see `User-Defined Tag
        Restrictions
        <https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/allocation-tag-restrictions.html>`__
        in the *AWS Billing and Cost Management User Guide* .

        The CMK that you use for this operation must be in a compatible key state. For details, see
        `How Key State Affects Use of a Customer Master Key
        <https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`__ in the *AWS Key
        Management Service Developer Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/TagResource>`_

        **Request Syntax**
        ::

          response = client.tag_resource(
              KeyId='string',
              Tags=[
                  {
                      'TagKey': 'string',
                      'TagValue': 'string'
                  },
              ]
          )
        :type KeyId: string
        :param KeyId: **[REQUIRED]**

          A unique identifier for the CMK you are tagging.

          Specify the key ID or the Amazon Resource Name (ARN) of the CMK.

          For example:

          * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``

          * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``

          To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey .

        :type Tags: list
        :param Tags: **[REQUIRED]**

          One or more tags. Each tag consists of a tag key and a tag value.

          - *(dict) --*

            A key-value pair. A tag consists of a tag key and a tag value. Tag keys and tag values
            are both required, but tag values can be empty (null) strings.

            For information about the rules that apply to tag keys and tag values, see `User-Defined
            Tag Restrictions
            <https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/allocation-tag-restrictions.html>`__
            in the *AWS Billing and Cost Management User Guide* .

            - **TagKey** *(string) --* **[REQUIRED]**

              The key of the tag.

            - **TagValue** *(string) --* **[REQUIRED]**

              The value of the tag.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def untag_resource(self, KeyId: str, TagKeys: List[str]) -> None:
        """
        Removes the specified tags from the specified customer master key (CMK). You cannot perform
        this operation on a CMK in a different AWS account.

        To remove a tag, specify the tag key. To change the tag value of an existing tag key, use
        TagResource .

        The CMK that you use for this operation must be in a compatible key state. For details, see
        `How Key State Affects Use of a Customer Master Key
        <https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`__ in the *AWS Key
        Management Service Developer Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/UntagResource>`_

        **Request Syntax**
        ::

          response = client.untag_resource(
              KeyId='string',
              TagKeys=[
                  'string',
              ]
          )
        :type KeyId: string
        :param KeyId: **[REQUIRED]**

          A unique identifier for the CMK from which you are removing tags.

          Specify the key ID or the Amazon Resource Name (ARN) of the CMK.

          For example:

          * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``

          * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``

          To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey .

        :type TagKeys: list
        :param TagKeys: **[REQUIRED]**

          One or more tag keys. Specify only the tag keys, not the tag values.

          - *(string) --*

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_alias(self, AliasName: str, TargetKeyId: str) -> None:
        """
        Associates an existing AWS KMS alias with a different customer master key (CMK). Each alias
        is associated with only one CMK at a time, although a CMK can have multiple aliases. The
        alias and the CMK must be in the same AWS account and region. You cannot perform this
        operation on an alias in a different AWS account.

        The current and new CMK must be the same type (both symmetric or both asymmetric), and they
        must have the same key usage (``ENCRYPT_DECRYPT`` or ``SIGN_VERIFY`` ). This restriction
        prevents errors in code that uses aliases. If you must assign an alias to a different type
        of CMK, use  DeleteAlias to delete the old alias and  CreateAlias to create a new alias.

        You cannot use ``UpdateAlias`` to change an alias name. To change an alias name, use
        DeleteAlias to delete the old alias and  CreateAlias to create a new alias.

        Because an alias is not a property of a CMK, you can create, update, and delete the aliases
        of a CMK without affecting the CMK. Also, aliases do not appear in the response from the
        DescribeKey operation. To get the aliases of all CMKs in the account, use the  ListAliases
        operation.

        The CMK that you use for this operation must be in a compatible key state. For details, see
        `How Key State Affects Use of a Customer Master Key
        <https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`__ in the *AWS Key
        Management Service Developer Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/UpdateAlias>`_

        **Request Syntax**
        ::

          response = client.update_alias(
              AliasName='string',
              TargetKeyId='string'
          )
        :type AliasName: string
        :param AliasName: **[REQUIRED]**

          Identifies the alias that is changing its CMK. This value must begin with ``alias/``
          followed by the alias name, such as ``alias/ExampleAlias`` . You cannot use UpdateAlias to
          change the alias name.

        :type TargetKeyId: string
        :param TargetKeyId: **[REQUIRED]**

          Identifies the CMK to associate with the alias. When the update operation completes, the
          alias will point to this CMK.

          The CMK must be in the same AWS account and Region as the alias. Also, the new target CMK
          must be the same type as the current target CMK (both symmetric or both asymmetric) and
          they must have the same key usage.

          Specify the key ID or the Amazon Resource Name (ARN) of the CMK.

          For example:

          * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``

          * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``

          To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey .

          To verify that the alias is mapped to the correct CMK, use  ListAliases .

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_custom_key_store(
        self,
        CustomKeyStoreId: str,
        NewCustomKeyStoreName: str = None,
        KeyStorePassword: str = None,
        CloudHsmClusterId: str = None,
    ) -> Dict[str, Any]:
        """
        Changes the properties of a custom key store. Use the ``CustomKeyStoreId`` parameter to
        identify the custom key store you want to edit. Use the remaining parameters to change the
        properties of the custom key store.

        You can only update a custom key store that is disconnected. To disconnect the custom key
        store, use  DisconnectCustomKeyStore . To reconnect the custom key store after the update
        completes, use  ConnectCustomKeyStore . To find the connection state of a custom key store,
        use the  DescribeCustomKeyStores operation.

        Use the parameters of ``UpdateCustomKeyStore`` to edit your keystore settings.

        * Use the **NewCustomKeyStoreName** parameter to change the friendly name of the custom key
        store to the value that you specify.

        * Use the **KeyStorePassword** parameter tell AWS KMS the current password of the `
        ``kmsuser`` crypto user (CU)
        <https://docs.aws.amazon.com/kms/latest/developerguide/key-store-concepts.html#concept-kmsuser>`__
        in the associated AWS CloudHSM cluster. You can use this parameter to `fix connection
        failures
        <https://docs.aws.amazon.com/kms/latest/developerguide/fix-keystore.html#fix-keystore-password>`__
        that occur when AWS KMS cannot log into the associated cluster because the ``kmsuser``
        password has changed. This value does not change the password in the AWS CloudHSM cluster.

        * Use the **CloudHsmClusterId** parameter to associate the custom key store with a
        different, but related, AWS CloudHSM cluster. You can use this parameter to repair a custom
        key store if its AWS CloudHSM cluster becomes corrupted or is deleted, or when you need to
        create or restore a cluster from a backup.

        If the operation succeeds, it returns a JSON object with no properties.

        This operation is part of the `Custom Key Store feature
        <https://docs.aws.amazon.com/kms/latest/developerguide/custom-key-store-overview.html>`__
        feature in AWS KMS, which combines the convenience and extensive integration of AWS KMS with
        the isolation and control of a single-tenant key store.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/UpdateCustomKeyStore>`_

        **Request Syntax**
        ::

          response = client.update_custom_key_store(
              CustomKeyStoreId='string',
              NewCustomKeyStoreName='string',
              KeyStorePassword='string',
              CloudHsmClusterId='string'
          )
        :type CustomKeyStoreId: string
        :param CustomKeyStoreId: **[REQUIRED]**

          Identifies the custom key store that you want to update. Enter the ID of the custom key
          store. To find the ID of a custom key store, use the  DescribeCustomKeyStores operation.

        :type NewCustomKeyStoreName: string
        :param NewCustomKeyStoreName:

          Changes the friendly name of the custom key store to the value that you specify. The
          custom key store name must be unique in the AWS account.

        :type KeyStorePassword: string
        :param KeyStorePassword:

          Enter the current password of the ``kmsuser`` crypto user (CU) in the AWS CloudHSM cluster
          that is associated with the custom key store.

          This parameter tells AWS KMS the current password of the ``kmsuser`` crypto user (CU). It
          does not set or change the password of any users in the AWS CloudHSM cluster.

        :type CloudHsmClusterId: string
        :param CloudHsmClusterId:

          Associates the custom key store with a related AWS CloudHSM cluster.

          Enter the cluster ID of the cluster that you used to create the custom key store or a
          cluster that shares a backup history and has the same cluster certificate as the original
          cluster. You cannot use this parameter to associate a custom key store with an unrelated
          cluster. In addition, the replacement cluster must `fulfill the requirements
          <https://docs.aws.amazon.com/kms/latest/developerguide/create-keystore.html#before-keystore>`__
          for a cluster associated with a custom key store. To view the cluster certificate of a
          cluster, use the `DescribeClusters
          <https://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_DescribeClusters.html>`__
          operation.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {}
          **Response Structure**

          - *(dict) --*
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_key_description(self, KeyId: str, Description: str) -> None:
        """
        Updates the description of a customer master key (CMK). To see the description of a CMK, use
        DescribeKey .

        You cannot perform this operation on a CMK in a different AWS account.

        The CMK that you use for this operation must be in a compatible key state. For details, see
        `How Key State Affects Use of a Customer Master Key
        <https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`__ in the *AWS Key
        Management Service Developer Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/UpdateKeyDescription>`_

        **Request Syntax**
        ::

          response = client.update_key_description(
              KeyId='string',
              Description='string'
          )
        :type KeyId: string
        :param KeyId: **[REQUIRED]**

          A unique identifier for the customer master key (CMK).

          Specify the key ID or the Amazon Resource Name (ARN) of the CMK.

          For example:

          * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``

          * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``

          To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey .

        :type Description: string
        :param Description: **[REQUIRED]**

          New description for the CMK.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def verify(
        self,
        KeyId: str,
        Message: bytes,
        Signature: bytes,
        SigningAlgorithm: Literal[
            "RSASSA_PSS_SHA_256",
            "RSASSA_PSS_SHA_384",
            "RSASSA_PSS_SHA_512",
            "RSASSA_PKCS1_V1_5_SHA_256",
            "RSASSA_PKCS1_V1_5_SHA_384",
            "RSASSA_PKCS1_V1_5_SHA_512",
            "ECDSA_SHA_256",
            "ECDSA_SHA_384",
            "ECDSA_SHA_512",
        ],
        MessageType: Literal["RAW", "DIGEST"] = None,
        GrantTokens: List[str] = None,
    ) -> ClientVerifyResponseTypeDef:
        """
        Verifies a digital signature that was generated by the  Sign operation. This operation
        requires an asymmetric CMK with a ``KeyUsage`` value of ``SIGN_VERIFY`` .

        Verification confirms that an authorized user signed the message with the specified key and
        signing algorithm, and the message hasn't changed since it was signed. A digital signature
        is generated by using the private key in an asymmetric CMK. The signature is verified by
        using the public key in the same asymmetric CMK. For information about symmetric and
        asymmetric CMKs, see `Using Symmetric and Asymmetric CMKs
        <https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html>`__ in the
        *AWS Key Management Service Developer Guide* .

        To verify a digital signature, you can use the ``Verify`` operation. Specify the same
        asymmetric CMK that was used by the ``Sign`` operation to generate the digital signature.

        You can also verify the digital signature by using the public key of the CMK outside of AWS
        KMS. Use the  GetPublicKey operation to download the public key in the asymmetric CMK and
        then use the public key to verify the signature outside of AWS KMS.

        The advantage of using the ``Verify`` operation is that it is performed within AWS KMS. As a
        result, it's easy to call, the operation is performed within the FIPS boundary, it is logged
        in AWS CloudTrail, and you can use key policy and IAM policy to determine who is authorized
        to use the CMK to verify signatures.

        .. warning::

          The result of the ``Verify`` operation, which is represented by its HTTP status code, does
          not indicate whether the signature verification succeeded or failed. To determine whether
          the signature was verified, see the ``SignatureValid`` field in the response.

        The CMK that you use for this operation must be in a compatible key state. For details, see
        `How Key State Affects Use of a Customer Master Key
        <https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html>`__ in the *AWS Key
        Management Service Developer Guide* .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/Verify>`_

        **Request Syntax**
        ::

          response = client.verify(
              KeyId='string',
              Message=b'bytes',
              MessageType='RAW'|'DIGEST',
              Signature=b'bytes',
              SigningAlgorithm=
                  'RSASSA_PSS_SHA_256'|'RSASSA_PSS_SHA_384'|'RSASSA_PSS_SHA_512'
                  |'RSASSA_PKCS1_V1_5_SHA_256'|'RSASSA_PKCS1_V1_5_SHA_384'
                  |'RSASSA_PKCS1_V1_5_SHA_512'|'ECDSA_SHA_256'|'ECDSA_SHA_384'|'ECDSA_SHA_512',
              GrantTokens=[
                  'string',
              ]
          )
        :type KeyId: string
        :param KeyId: **[REQUIRED]**

          Identifies the asymmetric CMK that will be used to verify the signature. This must be the
          same CMK that was used to generate the signature. If you specify a different CMK, the
          value of the ``SignatureValid`` field in the response will be ``False`` .

          To specify a CMK, use its key ID, Amazon Resource Name (ARN), alias name, or alias ARN.
          When using an alias name, prefix it with ``"alias/"`` . To specify a CMK in a different
          AWS account, you must use the key ARN or alias ARN.

          For example:

          * Key ID: ``1234abcd-12ab-34cd-56ef-1234567890ab``

          * Key ARN: ``arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab``

          * Alias name: ``alias/ExampleAlias``

          * Alias ARN: ``arn:aws:kms:us-east-2:111122223333:alias/ExampleAlias``

          To get the key ID and key ARN for a CMK, use  ListKeys or  DescribeKey . To get the alias
          name and alias ARN, use  ListAliases .

        :type Message: bytes
        :param Message: **[REQUIRED]**

          Specifies the message that was signed, or a hash digest of that message. Messages can be
          0-4096 bytes. To verify a larger message, provide a hash digest of the message.

          If the digest of the message specified here is different from the message digest that was
          signed, the ``SignatureValid`` value in the response will be ``False`` .

        :type MessageType: string
        :param MessageType:

          Tells AWS KMS whether the value of the ``Message`` parameter is a message or message
          digest. To indicate a message, enter ``RAW`` . To indicate a message digest, enter
          ``DIGEST`` .

        :type Signature: bytes
        :param Signature: **[REQUIRED]**

          The signature that the ``Sign`` operation generated.

        :type SigningAlgorithm: string
        :param SigningAlgorithm: **[REQUIRED]**

          The signing algorithm that was used to sign the message. If you submit a different
          algorithm, the value of the ``SignatureValid`` field in the response will be ``False`` .

        :type GrantTokens: list
        :param GrantTokens:

          A list of grant tokens.

          For more information, see `Grant Tokens
          <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#grant_token>`__ in
          the *AWS Key Management Service Developer Guide* .

          - *(string) --*

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'KeyId': 'string',
                'SignatureValid': True|False,
                'SigningAlgorithm':
                'RSASSA_PSS_SHA_256'|'RSASSA_PSS_SHA_384'|'RSASSA_PSS_SHA_512'
                |'RSASSA_PKCS1_V1_5_SHA_256'|'RSASSA_PKCS1_V1_5_SHA_384'
                |'RSASSA_PKCS1_V1_5_SHA_512'|'ECDSA_SHA_256'|'ECDSA_SHA_384'|'ECDSA_SHA_512'
            }
          **Response Structure**

          - *(dict) --*

            - **KeyId** *(string) --*

              The unique identifier for the asymmetric CMK that was used to verify the signature.

            - **SignatureValid** *(boolean) --*

              A Boolean value that indicates whether the signature was verified. A value of True
              indicates that the ``Signature`` was produced by signing the ``Message`` with the
              specified KeyID and ``SigningAlgorithm.`` A value of False indicates that the message,
              the algorithm, or the key changed since the message was signed.

            - **SigningAlgorithm** *(string) --*

              The signing algorithm that was used to verify the signature.
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
        self, operation_name: Literal["list_grants"]
    ) -> paginator_scope.ListGrantsPaginator:
        """
        Get Paginator for `list_grants` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_key_policies"]
    ) -> paginator_scope.ListKeyPoliciesPaginator:
        """
        Get Paginator for `list_key_policies` operation.
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_keys"]
    ) -> paginator_scope.ListKeysPaginator:
        """
        Get Paginator for `list_keys` operation.
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
    AlreadyExistsException: Boto3ClientError
    ClientError: Boto3ClientError
    CloudHsmClusterInUseException: Boto3ClientError
    CloudHsmClusterInvalidConfigurationException: Boto3ClientError
    CloudHsmClusterNotActiveException: Boto3ClientError
    CloudHsmClusterNotFoundException: Boto3ClientError
    CloudHsmClusterNotRelatedException: Boto3ClientError
    CustomKeyStoreHasCMKsException: Boto3ClientError
    CustomKeyStoreInvalidStateException: Boto3ClientError
    CustomKeyStoreNameInUseException: Boto3ClientError
    CustomKeyStoreNotFoundException: Boto3ClientError
    DependencyTimeoutException: Boto3ClientError
    DisabledException: Boto3ClientError
    ExpiredImportTokenException: Boto3ClientError
    IncorrectKeyException: Boto3ClientError
    IncorrectKeyMaterialException: Boto3ClientError
    IncorrectTrustAnchorException: Boto3ClientError
    InvalidAliasNameException: Boto3ClientError
    InvalidArnException: Boto3ClientError
    InvalidCiphertextException: Boto3ClientError
    InvalidGrantIdException: Boto3ClientError
    InvalidGrantTokenException: Boto3ClientError
    InvalidImportTokenException: Boto3ClientError
    InvalidKeyUsageException: Boto3ClientError
    InvalidMarkerException: Boto3ClientError
    KMSInternalException: Boto3ClientError
    KMSInvalidStateException: Boto3ClientError
    KeyUnavailableException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    MalformedPolicyDocumentException: Boto3ClientError
    NotFoundException: Boto3ClientError
    TagException: Boto3ClientError
    UnsupportedOperationException: Boto3ClientError
