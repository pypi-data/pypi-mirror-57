"Main interface for acm service Client"
from __future__ import annotations

from typing import Any, Dict, List
from botocore.client import BaseClient
from botocore.exceptions import ClientError as Boto3ClientError
from botocore.paginate import Paginator as Boto3Paginator
from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3.type_defs import Literal, overload

# pylint: disable=import-self
import mypy_boto3_acm.client as client_scope

# pylint: disable=import-self
import mypy_boto3_acm.paginator as paginator_scope
from mypy_boto3_acm.type_defs import (
    ClientAddTagsToCertificateTagsTypeDef,
    ClientDescribeCertificateResponseTypeDef,
    ClientExportCertificateResponseTypeDef,
    ClientGetCertificateResponseTypeDef,
    ClientImportCertificateResponseTypeDef,
    ClientImportCertificateTagsTypeDef,
    ClientListCertificatesIncludesTypeDef,
    ClientListCertificatesResponseTypeDef,
    ClientListTagsForCertificateResponseTypeDef,
    ClientRemoveTagsFromCertificateTagsTypeDef,
    ClientRequestCertificateDomainValidationOptionsTypeDef,
    ClientRequestCertificateOptionsTypeDef,
    ClientRequestCertificateResponseTypeDef,
    ClientRequestCertificateTagsTypeDef,
    ClientUpdateCertificateOptionsOptionsTypeDef,
)

# pylint: disable=import-self
import mypy_boto3_acm.waiter as waiter_scope


__all__ = ("Client",)


class Client(BaseClient):
    exceptions: client_scope.Exceptions

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def add_tags_to_certificate(
        self, CertificateArn: str, Tags: List[ClientAddTagsToCertificateTagsTypeDef]
    ) -> None:
        """
        Adds one or more tags to an ACM certificate. Tags are labels that you can use to identify
        and organize your AWS resources. Each tag consists of a ``key`` and an optional ``value`` .
        You specify the certificate on input by its Amazon Resource Name (ARN). You specify the tag
        by using a key-value pair.

        You can apply a tag to just one certificate if you want to identify a specific
        characteristic of that certificate, or you can apply the same tag to multiple certificates
        if you want to filter for a common relationship among those certificates. Similarly, you can
        apply the same tag to multiple resources if you want to specify a relationship among those
        resources. For example, you can add the same tag to an ACM certificate and an Elastic Load
        Balancing load balancer to indicate that they are both used by the same website. For more
        information, see `Tagging ACM certificates
        <https://docs.aws.amazon.com/acm/latest/userguide/tags.html>`__ .

        To remove one or more tags, use the  RemoveTagsFromCertificate action. To view all of the
        tags that have been applied to the certificate, use the  ListTagsForCertificate action.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/acm-2015-12-08/AddTagsToCertificate>`_

        **Request Syntax**
        ::

          response = client.add_tags_to_certificate(
              CertificateArn='string',
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ]
          )
        :type CertificateArn: string
        :param CertificateArn: **[REQUIRED]**

          String that contains the ARN of the ACM certificate to which the tag is to be applied.
          This must be of the form:

           ``arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012``

          For more information about ARNs, see `Amazon Resource Names (ARNs) and AWS Service
          Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__
          .

        :type Tags: list
        :param Tags: **[REQUIRED]**

          The key-value pair that defines the tag. The tag value is optional.

          - *(dict) --*

            A key-value pair that identifies or specifies metadata about an ACM resource.

            - **Key** *(string) --* **[REQUIRED]**

              The key of the tag.

            - **Value** *(string) --*

              The value of the tag.

        :returns: None
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
    def delete_certificate(self, CertificateArn: str) -> None:
        """
        Deletes a certificate and its associated private key. If this action succeeds, the
        certificate no longer appears in the list that can be displayed by calling the
        ListCertificates action or be retrieved by calling the  GetCertificate action. The
        certificate will not be available for use by AWS services integrated with ACM.

        .. note::

          You cannot delete an ACM certificate that is being used by another AWS service. To delete
          a certificate that is in use, the certificate association must first be removed.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/acm-2015-12-08/DeleteCertificate>`_

        **Request Syntax**
        ::

          response = client.delete_certificate(
              CertificateArn='string'
          )
        :type CertificateArn: string
        :param CertificateArn: **[REQUIRED]**

          String that contains the ARN of the ACM certificate to be deleted. This must be of the
          form:

           ``arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012``

          For more information about ARNs, see `Amazon Resource Names (ARNs) and AWS Service
          Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__
          .

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def describe_certificate(self, CertificateArn: str) -> ClientDescribeCertificateResponseTypeDef:
        """
        Returns detailed metadata about the specified ACM certificate.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/acm-2015-12-08/DescribeCertificate>`_

        **Request Syntax**
        ::

          response = client.describe_certificate(
              CertificateArn='string'
          )
        :type CertificateArn: string
        :param CertificateArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the ACM certificate. The ARN must have the following
          form:

           ``arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012``

          For more information about ARNs, see `Amazon Resource Names (ARNs) and AWS Service
          Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__
          .

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Certificate': {
                    'CertificateArn': 'string',
                    'DomainName': 'string',
                    'SubjectAlternativeNames': [
                        'string',
                    ],
                    'DomainValidationOptions': [
                        {
                            'DomainName': 'string',
                            'ValidationEmails': [
                                'string',
                            ],
                            'ValidationDomain': 'string',
                            'ValidationStatus': 'PENDING_VALIDATION'|'SUCCESS'|'FAILED',
                            'ResourceRecord': {
                                'Name': 'string',
                                'Type': 'CNAME',
                                'Value': 'string'
                            },
                            'ValidationMethod': 'EMAIL'|'DNS'
                        },
                    ],
                    'Serial': 'string',
                    'Subject': 'string',
                    'Issuer': 'string',
                    'CreatedAt': datetime(2015, 1, 1),
                    'IssuedAt': datetime(2015, 1, 1),
                    'ImportedAt': datetime(2015, 1, 1),
                    'Status':
                    'PENDING_VALIDATION'|'ISSUED'|'INACTIVE'|'EXPIRED'
                    |'VALIDATION_TIMED_OUT'|'REVOKED'|'FAILED',
                    'RevokedAt': datetime(2015, 1, 1),
                    'RevocationReason':
                    'UNSPECIFIED'|'KEY_COMPROMISE'|'CA_COMPROMISE'|'AFFILIATION_CHANGED'
                    |'SUPERCEDED'|'CESSATION_OF_OPERATION'|'CERTIFICATE_HOLD'
                    |'REMOVE_FROM_CRL'|'PRIVILEGE_WITHDRAWN'|'A_A_COMPROMISE',
                    'NotBefore': datetime(2015, 1, 1),
                    'NotAfter': datetime(2015, 1, 1),
                    'KeyAlgorithm':
                    'RSA_2048'|'RSA_1024'|'RSA_4096'|'EC_prime256v1'|'EC_secp384r1'
                    |'EC_secp521r1',
                    'SignatureAlgorithm': 'string',
                    'InUseBy': [
                        'string',
                    ],
                    'FailureReason':
                    'NO_AVAILABLE_CONTACTS'|'ADDITIONAL_VERIFICATION_REQUIRED'
                    |'DOMAIN_NOT_ALLOWED'|'INVALID_PUBLIC_DOMAIN'
                    |'DOMAIN_VALIDATION_DENIED'|'CAA_ERROR'|'PCA_LIMIT_EXCEEDED'
                    |'PCA_INVALID_ARN'|'PCA_INVALID_STATE'|'PCA_REQUEST_FAILED'
                    |'PCA_NAME_CONSTRAINTS_VALIDATION'|'PCA_RESOURCE_NOT_FOUND'
                    |'PCA_INVALID_ARGS'|'PCA_INVALID_DURATION'|'PCA_ACCESS_DENIED'
                    |'OTHER',
                    'Type': 'IMPORTED'|'AMAZON_ISSUED'|'PRIVATE',
                    'RenewalSummary': {
                        'RenewalStatus':
                        'PENDING_AUTO_RENEWAL'|'PENDING_VALIDATION'|'SUCCESS'
                        |'FAILED',
                        'DomainValidationOptions': [
                            {
                                'DomainName': 'string',
                                'ValidationEmails': [
                                    'string',
                                ],
                                'ValidationDomain': 'string',
                                'ValidationStatus': 'PENDING_VALIDATION'|'SUCCESS'|'FAILED',
                                'ResourceRecord': {
                                    'Name': 'string',
                                    'Type': 'CNAME',
                                    'Value': 'string'
                                },
                                'ValidationMethod': 'EMAIL'|'DNS'
                            },
                        ],
                        'RenewalStatusReason':
                        'NO_AVAILABLE_CONTACTS'|'ADDITIONAL_VERIFICATION_REQUIRED'
                        |'DOMAIN_NOT_ALLOWED'|'INVALID_PUBLIC_DOMAIN'
                        |'DOMAIN_VALIDATION_DENIED'|'CAA_ERROR'|'PCA_LIMIT_EXCEEDED'
                        |'PCA_INVALID_ARN'|'PCA_INVALID_STATE'|'PCA_REQUEST_FAILED'
                        |'PCA_NAME_CONSTRAINTS_VALIDATION'|'PCA_RESOURCE_NOT_FOUND'
                        |'PCA_INVALID_ARGS'|'PCA_INVALID_DURATION'
                        |'PCA_ACCESS_DENIED'|'OTHER',
                        'UpdatedAt': datetime(2015, 1, 1)
                    },
                    'KeyUsages': [
                        {
                            'Name':
                            'DIGITAL_SIGNATURE'|'NON_REPUDIATION'
                            |'KEY_ENCIPHERMENT'|'DATA_ENCIPHERMENT'
                            |'KEY_AGREEMENT'|'CERTIFICATE_SIGNING'|'CRL_SIGNING'
                            |'ENCIPHER_ONLY'|'DECIPHER_ONLY'|'ANY'|'CUSTOM'
                        },
                    ],
                    'ExtendedKeyUsages': [
                        {
                            'Name':
                            'TLS_WEB_SERVER_AUTHENTICATION'
                            |'TLS_WEB_CLIENT_AUTHENTICATION'|'CODE_SIGNING'
                            |'EMAIL_PROTECTION'|'TIME_STAMPING'|'OCSP_SIGNING'
                            |'IPSEC_END_SYSTEM'|'IPSEC_TUNNEL'|'IPSEC_USER'
                            |'ANY'|'NONE'|'CUSTOM',
                            'OID': 'string'
                        },
                    ],
                    'CertificateAuthorityArn': 'string',
                    'RenewalEligibility': 'ELIGIBLE'|'INELIGIBLE',
                    'Options': {
                        'CertificateTransparencyLoggingPreference': 'ENABLED'|'DISABLED'
                    }
                }
            }
          **Response Structure**

          - *(dict) --*

            - **Certificate** *(dict) --*

              Metadata about an ACM certificate.

              - **CertificateArn** *(string) --*

                The Amazon Resource Name (ARN) of the certificate. For more information about ARNs,
                see `Amazon Resource Names (ARNs) and AWS Service Namespaces
                <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ in
                the *AWS General Reference* .

              - **DomainName** *(string) --*

                The fully qualified domain name for the certificate, such as www.example.com or
                example.com.

              - **SubjectAlternativeNames** *(list) --*

                One or more domain names (subject alternative names) included in the certificate.
                This list contains the domain names that are bound to the public key that is
                contained in the certificate. The subject alternative names include the canonical
                domain name (CN) of the certificate and additional domain names that can be used to
                connect to the website.

                - *(string) --*

              - **DomainValidationOptions** *(list) --*

                Contains information about the initial validation of each domain name that occurs as
                a result of the  RequestCertificate request. This field exists only when the
                certificate type is ``AMAZON_ISSUED`` .

                - *(dict) --*

                  Contains information about the validation of each domain name in the certificate.

                  - **DomainName** *(string) --*

                    A fully qualified domain name (FQDN) in the certificate. For example,
                    ``www.example.com`` or ``example.com`` .

                  - **ValidationEmails** *(list) --*

                    A list of email addresses that ACM used to send domain validation emails.

                    - *(string) --*

                  - **ValidationDomain** *(string) --*

                    The domain name that ACM used to send domain validation emails.

                  - **ValidationStatus** *(string) --*

                    The validation status of the domain name. This can be one of the following
                    values:

                    * ``PENDING_VALIDATION``

                    * SUCCESS

                    * FAILED

                  - **ResourceRecord** *(dict) --*

                    Contains the CNAME record that you add to your DNS database for domain
                    validation. For more information, see `Use DNS to Validate Domain Ownership
                    <https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-validate-dns.html>`__ .

                    - **Name** *(string) --*

                      The name of the DNS record to create in your domain. This is supplied by ACM.

                    - **Type** *(string) --*

                      The type of DNS record. Currently this can be ``CNAME`` .

                    - **Value** *(string) --*

                      The value of the CNAME record to add to your DNS database. This is supplied by
                      ACM.

                  - **ValidationMethod** *(string) --*

                    Specifies the domain validation method.

              - **Serial** *(string) --*

                The serial number of the certificate.

              - **Subject** *(string) --*

                The name of the entity that is associated with the public key contained in the
                certificate.

              - **Issuer** *(string) --*

                The name of the certificate authority that issued and signed the certificate.

              - **CreatedAt** *(datetime) --*

                The time at which the certificate was requested. This value exists only when the
                certificate type is ``AMAZON_ISSUED`` .

              - **IssuedAt** *(datetime) --*

                The time at which the certificate was issued. This value exists only when the
                certificate type is ``AMAZON_ISSUED`` .

              - **ImportedAt** *(datetime) --*

                The date and time at which the certificate was imported. This value exists only when
                the certificate type is ``IMPORTED`` .

              - **Status** *(string) --*

                The status of the certificate.

              - **RevokedAt** *(datetime) --*

                The time at which the certificate was revoked. This value exists only when the
                certificate status is ``REVOKED`` .

              - **RevocationReason** *(string) --*

                The reason the certificate was revoked. This value exists only when the certificate
                status is ``REVOKED`` .

              - **NotBefore** *(datetime) --*

                The time before which the certificate is not valid.

              - **NotAfter** *(datetime) --*

                The time after which the certificate is not valid.

              - **KeyAlgorithm** *(string) --*

                The algorithm that was used to generate the public-private key pair.

              - **SignatureAlgorithm** *(string) --*

                The algorithm that was used to sign the certificate.

              - **InUseBy** *(list) --*

                A list of ARNs for the AWS resources that are using the certificate. A certificate
                can be used by multiple AWS resources.

                - *(string) --*

              - **FailureReason** *(string) --*

                The reason the certificate request failed. This value exists only when the
                certificate status is ``FAILED`` . For more information, see `Certificate Request
                Failed
                <https://docs.aws.amazon.com/acm/latest/userguide/troubleshooting.html#troubleshooting-failed>`__
                in the *AWS Certificate Manager User Guide* .

              - **Type** *(string) --*

                The source of the certificate. For certificates provided by ACM, this value is
                ``AMAZON_ISSUED`` . For certificates that you imported with  ImportCertificate ,
                this value is ``IMPORTED`` . ACM does not provide `managed renewal
                <https://docs.aws.amazon.com/acm/latest/userguide/acm-renewal.html>`__ for imported
                certificates. For more information about the differences between certificates that
                you import and those that ACM provides, see `Importing Certificates
                <https://docs.aws.amazon.com/acm/latest/userguide/import-certificate.html>`__ in the
                *AWS Certificate Manager User Guide* .

              - **RenewalSummary** *(dict) --*

                Contains information about the status of ACM's `managed renewal
                <https://docs.aws.amazon.com/acm/latest/userguide/acm-renewal.html>`__ for the
                certificate. This field exists only when the certificate type is ``AMAZON_ISSUED`` .

                - **RenewalStatus** *(string) --*

                  The status of ACM's `managed renewal
                  <https://docs.aws.amazon.com/acm/latest/userguide/acm-renewal.html>`__ of the
                  certificate.

                - **DomainValidationOptions** *(list) --*

                  Contains information about the validation of each domain name in the certificate,
                  as it pertains to ACM's `managed renewal
                  <https://docs.aws.amazon.com/acm/latest/userguide/acm-renewal.html>`__ . This is
                  different from the initial validation that occurs as a result of the
                  RequestCertificate request. This field exists only when the certificate type is
                  ``AMAZON_ISSUED`` .

                  - *(dict) --*

                    Contains information about the validation of each domain name in the
                    certificate.

                    - **DomainName** *(string) --*

                      A fully qualified domain name (FQDN) in the certificate. For example,
                      ``www.example.com`` or ``example.com`` .

                    - **ValidationEmails** *(list) --*

                      A list of email addresses that ACM used to send domain validation emails.

                      - *(string) --*

                    - **ValidationDomain** *(string) --*

                      The domain name that ACM used to send domain validation emails.

                    - **ValidationStatus** *(string) --*

                      The validation status of the domain name. This can be one of the following
                      values:

                      * ``PENDING_VALIDATION``

                      * SUCCESS

                      * FAILED

                    - **ResourceRecord** *(dict) --*

                      Contains the CNAME record that you add to your DNS database for domain
                      validation. For more information, see `Use DNS to Validate Domain Ownership
                      <https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-validate-dns.html>`__
                      .

                      - **Name** *(string) --*

                        The name of the DNS record to create in your domain. This is supplied by
                        ACM.

                      - **Type** *(string) --*

                        The type of DNS record. Currently this can be ``CNAME`` .

                      - **Value** *(string) --*

                        The value of the CNAME record to add to your DNS database. This is supplied
                        by ACM.

                    - **ValidationMethod** *(string) --*

                      Specifies the domain validation method.

                - **RenewalStatusReason** *(string) --*

                  The reason that a renewal request was unsuccessful.

                - **UpdatedAt** *(datetime) --*

                  The time at which the renewal summary was last updated.

              - **KeyUsages** *(list) --*

                A list of Key Usage X.509 v3 extension objects. Each object is a string value that
                identifies the purpose of the public key contained in the certificate. Possible
                extension values include DIGITAL_SIGNATURE, KEY_ENCHIPHERMENT, NON_REPUDIATION, and
                more.

                - *(dict) --*

                  The Key Usage X.509 v3 extension defines the purpose of the public key contained
                  in the certificate.

                  - **Name** *(string) --*

                    A string value that contains a Key Usage extension name.

              - **ExtendedKeyUsages** *(list) --*

                Contains a list of Extended Key Usage X.509 v3 extension objects. Each object
                specifies a purpose for which the certificate public key can be used and consists of
                a name and an object identifier (OID).

                - *(dict) --*

                  The Extended Key Usage X.509 v3 extension defines one or more purposes for which
                  the public key can be used. This is in addition to or in place of the basic
                  purposes specified by the Key Usage extension.

                  - **Name** *(string) --*

                    The name of an Extended Key Usage value.

                  - **OID** *(string) --*

                    An object identifier (OID) for the extension value. OIDs are strings of numbers
                    separated by periods. The following OIDs are defined in RFC 3280 and RFC 5280.

                    * ``1.3.6.1.5.5.7.3.1 (TLS_WEB_SERVER_AUTHENTICATION)``

                    * ``1.3.6.1.5.5.7.3.2 (TLS_WEB_CLIENT_AUTHENTICATION)``

                    * ``1.3.6.1.5.5.7.3.3 (CODE_SIGNING)``

                    * ``1.3.6.1.5.5.7.3.4 (EMAIL_PROTECTION)``

                    * ``1.3.6.1.5.5.7.3.8 (TIME_STAMPING)``

                    * ``1.3.6.1.5.5.7.3.9 (OCSP_SIGNING)``

                    * ``1.3.6.1.5.5.7.3.5 (IPSEC_END_SYSTEM)``

                    * ``1.3.6.1.5.5.7.3.6 (IPSEC_TUNNEL)``

                    * ``1.3.6.1.5.5.7.3.7 (IPSEC_USER)``

              - **CertificateAuthorityArn** *(string) --*

                The Amazon Resource Name (ARN) of the ACM PCA private certificate authority (CA)
                that issued the certificate. This has the following format:

                 ``arn:aws:acm-pca:region:account:certificate-authority/12345678-1234-1234-1234-123456789012``

              - **RenewalEligibility** *(string) --*

                Specifies whether the certificate is eligible for renewal. At this time, only
                exported private certificates can be renewed with the  RenewCertificate command.

              - **Options** *(dict) --*

                Value that specifies whether to add the certificate to a transparency log.
                Certificate transparency makes it possible to detect SSL certificates that have been
                mistakenly or maliciously issued. A browser might respond to certificate that has
                not been logged by showing an error message. The logs are cryptographically secure.

                - **CertificateTransparencyLoggingPreference** *(string) --*

                  You can opt out of certificate transparency logging by specifying the ``DISABLED``
                  option. Opt in by specifying ``ENABLED`` .
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def export_certificate(
        self, CertificateArn: str, Passphrase: bytes
    ) -> ClientExportCertificateResponseTypeDef:
        """
        Exports a private certificate issued by a private certificate authority (CA) for use
        anywhere. The exported file contains the certificate, the certificate chain, and the
        encrypted private 2048-bit RSA key associated with the public key that is embedded in the
        certificate. For security, you must assign a passphrase for the private key when exporting
        it.

        For information about exporting and formatting a certificate using the ACM console or CLI,
        see `Export a Private Certificate
        <https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-export-private.html>`__ .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/acm-2015-12-08/ExportCertificate>`_

        **Request Syntax**
        ::

          response = client.export_certificate(
              CertificateArn='string',
              Passphrase=b'bytes'
          )
        :type CertificateArn: string
        :param CertificateArn: **[REQUIRED]**

          An Amazon Resource Name (ARN) of the issued certificate. This must be of the form:

           ``arn:aws:acm:region:account:certificate/12345678-1234-1234-1234-123456789012``

        :type Passphrase: bytes
        :param Passphrase: **[REQUIRED]**

          Passphrase to associate with the encrypted exported private key. If you want to later
          decrypt the private key, you must have the passphrase. You can use the following OpenSSL
          command to decrypt a private key:

           ``openssl rsa -in encrypted_key.pem -out decrypted_key.pem``

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Certificate': 'string',
                'CertificateChain': 'string',
                'PrivateKey': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Certificate** *(string) --*

              The base64 PEM-encoded certificate.

            - **CertificateChain** *(string) --*

              The base64 PEM-encoded certificate chain. This does not include the certificate that
              you are exporting.

            - **PrivateKey** *(string) --*

              The encrypted private key associated with the public key in the certificate. The key
              is output in PKCS #8 format and is base64 PEM-encoded.
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
    def get_certificate(self, CertificateArn: str) -> ClientGetCertificateResponseTypeDef:
        """
        Retrieves a certificate specified by an ARN and its certificate chain . The chain is an
        ordered list of certificates that contains the end entity certificate, intermediate
        certificates of subordinate CAs, and the root certificate in that order. The certificate and
        certificate chain are base64 encoded. If you want to decode the certificate to see the
        individual fields, you can use OpenSSL.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/acm-2015-12-08/GetCertificate>`_

        **Request Syntax**
        ::

          response = client.get_certificate(
              CertificateArn='string'
          )
        :type CertificateArn: string
        :param CertificateArn: **[REQUIRED]**

          String that contains a certificate ARN in the following format:

           ``arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012``

          For more information about ARNs, see `Amazon Resource Names (ARNs) and AWS Service
          Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__
          .

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Certificate': 'string',
                'CertificateChain': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Certificate** *(string) --*

              String that contains the ACM certificate represented by the ARN specified at input.

            - **CertificateChain** *(string) --*

              The certificate chain that contains the root certificate issued by the certificate
              authority (CA).
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def import_certificate(
        self,
        Certificate: bytes,
        PrivateKey: bytes,
        CertificateArn: str = None,
        CertificateChain: bytes = None,
        Tags: List[ClientImportCertificateTagsTypeDef] = None,
    ) -> ClientImportCertificateResponseTypeDef:
        """
        Imports a certificate into AWS Certificate Manager (ACM) to use with services that are
        integrated with ACM. Note that `integrated services
        <https://docs.aws.amazon.com/acm/latest/userguide/acm-services.html>`__ allow only
        certificate types and keys they support to be associated with their resources. Further,
        their support differs depending on whether the certificate is imported into IAM or into ACM.
        For more information, see the documentation for each service. For more information about
        importing certificates into ACM, see `Importing Certificates
        <https://docs.aws.amazon.com/acm/latest/userguide/import-certificate.html>`__ in the *AWS
        Certificate Manager User Guide* .

        .. note::

          ACM does not provide `managed renewal
          <https://docs.aws.amazon.com/acm/latest/userguide/acm-renewal.html>`__ for certificates
          that you import.

        Note the following guidelines when importing third party certificates:

        * You must enter the private key that matches the certificate you are importing.

        * The private key must be unencrypted. You cannot import a private key that is protected by
        a password or a passphrase.

        * If the certificate you are importing is not self-signed, you must enter its certificate
        chain.

        * If a certificate chain is included, the issuer must be the subject of one of the
        certificates in the chain.

        * The certificate, private key, and certificate chain must be PEM-encoded.

        * The current time must be between the ``Not Before`` and ``Not After`` certificate fields.

        * The ``Issuer`` field must not be empty.

        * The OCSP authority URL, if present, must not exceed 1000 characters.

        * To import a new certificate, omit the ``CertificateArn`` argument. Include this argument
        only when you want to replace a previously imported certifica

        * When you import a certificate by using the CLI, you must specify the certificate, the
        certificate chain, and the private key by their file names preceded by ``file://`` . For
        example, you can specify a certificate saved in the ``C:\\temp`` folder as
        ``file://C:\\temp\\certificate_to_import.pem`` . If you are making an HTTP or HTTPS Query
        request, include these arguments as BLOBs.

        * When you import a certificate by using an SDK, you must specify the certificate, the
        certificate chain, and the private key files in the manner required by the programming
        language you're using.

        * The cryptographic algorithm of an imported certificate must match the algorithm of the
        signing CA. For example, if the signing CA key type is RSA, then the certificate key type
        must also be RSA.

        This operation returns the `Amazon Resource Name (ARN)
        <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ of the
        imported certificate.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/acm-2015-12-08/ImportCertificate>`_

        **Request Syntax**
        ::

          response = client.import_certificate(
              CertificateArn='string',
              Certificate=b'bytes',
              PrivateKey=b'bytes',
              CertificateChain=b'bytes',
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ]
          )
        :type CertificateArn: string
        :param CertificateArn:

          The `Amazon Resource Name (ARN)
          <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ of an
          imported certificate to replace. To import a new certificate, omit this field.

        :type Certificate: bytes
        :param Certificate: **[REQUIRED]**

          The certificate to import.

        :type PrivateKey: bytes
        :param PrivateKey: **[REQUIRED]**

          The private key that matches the public key in the certificate.

        :type CertificateChain: bytes
        :param CertificateChain:

          The PEM encoded certificate chain.

        :type Tags: list
        :param Tags:

          One or more resource tags to associate with the imported certificate.

          Note: You cannot apply tags when reimporting a certificate.

          - *(dict) --*

            A key-value pair that identifies or specifies metadata about an ACM resource.

            - **Key** *(string) --* **[REQUIRED]**

              The key of the tag.

            - **Value** *(string) --*

              The value of the tag.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'CertificateArn': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **CertificateArn** *(string) --*

              The `Amazon Resource Name (ARN)
              <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ of the
              imported certificate.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_certificates(
        self,
        CertificateStatuses: List[
            Literal[
                "PENDING_VALIDATION",
                "ISSUED",
                "INACTIVE",
                "EXPIRED",
                "VALIDATION_TIMED_OUT",
                "REVOKED",
                "FAILED",
            ]
        ] = None,
        Includes: ClientListCertificatesIncludesTypeDef = None,
        NextToken: str = None,
        MaxItems: int = None,
    ) -> ClientListCertificatesResponseTypeDef:
        """
        Retrieves a list of certificate ARNs and domain names. You can request that only
        certificates that match a specific status be listed. You can also filter by specific
        attributes of the certificate. Default filtering returns only ``RSA_2048`` certificates. For
        more information, see  Filters .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/acm-2015-12-08/ListCertificates>`_

        **Request Syntax**
        ::

          response = client.list_certificates(
              CertificateStatuses=[
                  'PENDING_VALIDATION'|'ISSUED'|'INACTIVE'|'EXPIRED'|'VALIDATION_TIMED_OUT'
                  |'REVOKED'|'FAILED',
              ],
              Includes={
                  'extendedKeyUsage': [
                      'TLS_WEB_SERVER_AUTHENTICATION'|'TLS_WEB_CLIENT_AUTHENTICATION'|'CODE_SIGNING'
                      |'EMAIL_PROTECTION'|'TIME_STAMPING'|'OCSP_SIGNING'|'IPSEC_END_SYSTEM'
                      |'IPSEC_TUNNEL'|'IPSEC_USER'|'ANY'|'NONE'|'CUSTOM',
                  ],
                  'keyUsage': [
                      'DIGITAL_SIGNATURE'|'NON_REPUDIATION'|'KEY_ENCIPHERMENT'|'DATA_ENCIPHERMENT'
                      |'KEY_AGREEMENT'|'CERTIFICATE_SIGNING'|'CRL_SIGNING'|'ENCIPHER_ONLY'
                      |'DECIPHER_ONLY'|'ANY'|'CUSTOM',
                  ],
                  'keyTypes': [
                      'RSA_2048'|'RSA_1024'|'RSA_4096'|'EC_prime256v1'|'EC_secp384r1'
                      |'EC_secp521r1',
                  ]
              },
              NextToken='string',
              MaxItems=123
          )
        :type CertificateStatuses: list
        :param CertificateStatuses:

          Filter the certificate list by status value.

          - *(string) --*

        :type Includes: dict
        :param Includes:

          Filter the certificate list. For more information, see the  Filters structure.

          - **extendedKeyUsage** *(list) --*

            Specify one or more  ExtendedKeyUsage extension values.

            - *(string) --*

          - **keyUsage** *(list) --*

            Specify one or more  KeyUsage extension values.

            - *(string) --*

          - **keyTypes** *(list) --*

            Specify one or more algorithms that can be used to generate key pairs.

            Default filtering returns only ``RSA_2048`` certificates. To return other certificate
            types, provide the desired type signatures in a comma-separated list. For example,
            ``"keyTypes": ["RSA_2048,RSA_4096"]`` returns both ``RSA_2048`` and ``RSA_4096``
            certificates.

            - *(string) --*

        :type NextToken: string
        :param NextToken:

          Use this parameter only when paginating results and only in a subsequent request after you
          receive a response with truncated results. Set it to the value of ``NextToken`` from the
          response you just received.

        :type MaxItems: integer
        :param MaxItems:

          Use this parameter when paginating results to specify the maximum number of items to
          return in the response. If additional items exist beyond the number you specify, the
          ``NextToken`` element is sent in the response. Use this ``NextToken`` value in a
          subsequent request to retrieve additional items.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'NextToken': 'string',
                'CertificateSummaryList': [
                    {
                        'CertificateArn': 'string',
                        'DomainName': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **NextToken** *(string) --*

              When the list is truncated, this value is present and contains the value to use for
              the ``NextToken`` parameter in a subsequent pagination request.

            - **CertificateSummaryList** *(list) --*

              A list of ACM certificates.

              - *(dict) --*

                This structure is returned in the response object of  ListCertificates action.

                - **CertificateArn** *(string) --*

                  Amazon Resource Name (ARN) of the certificate. This is of the form:

                   ``arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012``

                  For more information about ARNs, see `Amazon Resource Names (ARNs) and AWS Service
                  Namespaces
                  <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__ .

                - **DomainName** *(string) --*

                  Fully qualified domain name (FQDN), such as www.example.com or example.com, for
                  the certificate.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def list_tags_for_certificate(
        self, CertificateArn: str
    ) -> ClientListTagsForCertificateResponseTypeDef:
        """
        Lists the tags that have been applied to the ACM certificate. Use the certificate's Amazon
        Resource Name (ARN) to specify the certificate. To add a tag to an ACM certificate, use the
        AddTagsToCertificate action. To delete a tag, use the  RemoveTagsFromCertificate action.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/acm-2015-12-08/ListTagsForCertificate>`_

        **Request Syntax**
        ::

          response = client.list_tags_for_certificate(
              CertificateArn='string'
          )
        :type CertificateArn: string
        :param CertificateArn: **[REQUIRED]**

          String that contains the ARN of the ACM certificate for which you want to list the tags.
          This must have the following form:

           ``arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012``

          For more information about ARNs, see `Amazon Resource Names (ARNs) and AWS Service
          Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__
          .

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'Tags': [
                    {
                        'Key': 'string',
                        'Value': 'string'
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **Tags** *(list) --*

              The key-value pairs that define the applied tags.

              - *(dict) --*

                A key-value pair that identifies or specifies metadata about an ACM resource.

                - **Key** *(string) --*

                  The key of the tag.

                - **Value** *(string) --*

                  The value of the tag.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def remove_tags_from_certificate(
        self, CertificateArn: str, Tags: List[ClientRemoveTagsFromCertificateTagsTypeDef]
    ) -> None:
        """
        Remove one or more tags from an ACM certificate. A tag consists of a key-value pair. If you
        do not specify the value portion of the tag when calling this function, the tag will be
        removed regardless of value. If you specify a value, the tag is removed only if it is
        associated with the specified value.

        To add tags to a certificate, use the  AddTagsToCertificate action. To view all of the tags
        that have been applied to a specific ACM certificate, use the  ListTagsForCertificate
        action.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/acm-2015-12-08/RemoveTagsFromCertificate>`_

        **Request Syntax**
        ::

          response = client.remove_tags_from_certificate(
              CertificateArn='string',
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ]
          )
        :type CertificateArn: string
        :param CertificateArn: **[REQUIRED]**

          String that contains the ARN of the ACM Certificate with one or more tags that you want to
          remove. This must be of the form:

           ``arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012``

          For more information about ARNs, see `Amazon Resource Names (ARNs) and AWS Service
          Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__
          .

        :type Tags: list
        :param Tags: **[REQUIRED]**

          The key-value pair that defines the tag to remove.

          - *(dict) --*

            A key-value pair that identifies or specifies metadata about an ACM resource.

            - **Key** *(string) --* **[REQUIRED]**

              The key of the tag.

            - **Value** *(string) --*

              The value of the tag.

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def renew_certificate(self, CertificateArn: str) -> None:
        """
        Renews an eligable ACM certificate. At this time, only exported private certificates can be
        renewed with this operation. In order to renew your ACM PCA certificates with ACM, you must
        first `grant the ACM service principal permission to do so
        <https://docs.aws.amazon.com/acm-pca/latest/userguide/PcaPermissions.html>`__ . For more
        information, see `Testing Managed Renewal
        <https://docs.aws.amazon.com/acm/latest/userguide/manual-renewal.html>`__ in the ACM User
        Guide.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/acm-2015-12-08/RenewCertificate>`_

        **Request Syntax**
        ::

          response = client.renew_certificate(
              CertificateArn='string'
          )
        :type CertificateArn: string
        :param CertificateArn: **[REQUIRED]**

          String that contains the ARN of the ACM certificate to be renewed. This must be of the
          form:

           ``arn:aws:acm:region:123456789012:certificate/12345678-1234-1234-1234-123456789012``

          For more information about ARNs, see `Amazon Resource Names (ARNs) and AWS Service
          Namespaces <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`__
          .

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def request_certificate(
        self,
        DomainName: str,
        ValidationMethod: Literal["EMAIL", "DNS"] = None,
        SubjectAlternativeNames: List[str] = None,
        IdempotencyToken: str = None,
        DomainValidationOptions: List[
            ClientRequestCertificateDomainValidationOptionsTypeDef
        ] = None,
        Options: ClientRequestCertificateOptionsTypeDef = None,
        CertificateAuthorityArn: str = None,
        Tags: List[ClientRequestCertificateTagsTypeDef] = None,
    ) -> ClientRequestCertificateResponseTypeDef:
        """
        Requests an ACM certificate for use with other AWS services. To request an ACM certificate,
        you must specify a fully qualified domain name (FQDN) in the ``DomainName`` parameter. You
        can also specify additional FQDNs in the ``SubjectAlternativeNames`` parameter.

        If you are requesting a private certificate, domain validation is not required. If you are
        requesting a public certificate, each domain name that you specify must be validated to
        verify that you own or control the domain. You can use `DNS validation
        <https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-validate-dns.html>`__ or `email
        validation <https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-validate-email.html>`__
        . We recommend that you use DNS validation. ACM issues public certificates after receiving
        approval from the domain owner.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/acm-2015-12-08/RequestCertificate>`_

        **Request Syntax**
        ::

          response = client.request_certificate(
              DomainName='string',
              ValidationMethod='EMAIL'|'DNS',
              SubjectAlternativeNames=[
                  'string',
              ],
              IdempotencyToken='string',
              DomainValidationOptions=[
                  {
                      'DomainName': 'string',
                      'ValidationDomain': 'string'
                  },
              ],
              Options={
                  'CertificateTransparencyLoggingPreference': 'ENABLED'|'DISABLED'
              },
              CertificateAuthorityArn='string',
              Tags=[
                  {
                      'Key': 'string',
                      'Value': 'string'
                  },
              ]
          )
        :type DomainName: string
        :param DomainName: **[REQUIRED]**

          Fully qualified domain name (FQDN), such as www.example.com, that you want to secure with
          an ACM certificate. Use an asterisk (*) to create a wildcard certificate that protects
          several sites in the same domain. For example, *.example.com protects www.example.com,
          site.example.com, and images.example.com.

          The first domain name you enter cannot exceed 64 octets, including periods. Each
          subsequent Subject Alternative Name (SAN), however, can be up to 253 octets in length.

        :type ValidationMethod: string
        :param ValidationMethod:

          The method you want to use if you are requesting a public certificate to validate that you
          own or control domain. You can `validate with DNS
          <https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-validate-dns.html>`__ or
          `validate with email
          <https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-validate-email.html>`__ . We
          recommend that you use DNS validation.

        :type SubjectAlternativeNames: list
        :param SubjectAlternativeNames:

          Additional FQDNs to be included in the Subject Alternative Name extension of the ACM
          certificate. For example, add the name www.example.net to a certificate for which the
          ``DomainName`` field is www.example.com if users can reach your site by using either name.
          The maximum number of domain names that you can add to an ACM certificate is 100. However,
          the initial limit is 10 domain names. If you need more than 10 names, you must request a
          limit increase. For more information, see `Limits
          <https://docs.aws.amazon.com/acm/latest/userguide/acm-limits.html>`__ .

          The maximum length of a SAN DNS name is 253 octets. The name is made up of multiple labels
          separated by periods. No label can be longer than 63 octets. Consider the following
          examples:

          * ``(63 octets).(63 octets).(63 octets).(61 octets)`` is legal because the total length is
          253 octets (63+1+63+1+63+1+61) and no label exceeds 63 octets.

          * ``(64 octets).(63 octets).(63 octets).(61 octets)`` is not legal because the total
          length exceeds 253 octets (64+1+63+1+63+1+61) and the first label exceeds 63 octets.

          * ``(63 octets).(63 octets).(63 octets).(62 octets)`` is not legal because the total
          length of the DNS name (63+1+63+1+63+1+62) exceeds 253 octets.

          - *(string) --*

        :type IdempotencyToken: string
        :param IdempotencyToken:

          Customer chosen string that can be used to distinguish between calls to
          ``RequestCertificate`` . Idempotency tokens time out after one hour. Therefore, if you
          call ``RequestCertificate`` multiple times with the same idempotency token within one
          hour, ACM recognizes that you are requesting only one certificate and will issue only one.
          If you change the idempotency token for each call, ACM recognizes that you are requesting
          multiple certificates.

        :type DomainValidationOptions: list
        :param DomainValidationOptions:

          The domain name that you want ACM to use to send you emails so that you can validate
          domain ownership.

          - *(dict) --*

            Contains information about the domain names that you want ACM to use to send you emails
            that enable you to validate domain ownership.

            - **DomainName** *(string) --* **[REQUIRED]**

              A fully qualified domain name (FQDN) in the certificate request.

            - **ValidationDomain** *(string) --* **[REQUIRED]**

              The domain name that you want ACM to use to send you validation emails. This domain
              name is the suffix of the email addresses that you want ACM to use. This must be the
              same as the ``DomainName`` value or a superdomain of the ``DomainName`` value. For
              example, if you request a certificate for ``testing.example.com`` , you can specify
              ``example.com`` for this value. In that case, ACM sends domain validation emails to
              the following five addresses:

              * admin@example.com

              * administrator@example.com

              * hostmaster@example.com

              * postmaster@example.com

              * webmaster@example.com

        :type Options: dict
        :param Options:

          Currently, you can use this parameter to specify whether to add the certificate to a
          certificate transparency log. Certificate transparency makes it possible to detect SSL/TLS
          certificates that have been mistakenly or maliciously issued. Certificates that have not
          been logged typically produce an error message in a browser. For more information, see
          `Opting Out of Certificate Transparency Logging
          <https://docs.aws.amazon.com/acm/latest/userguide/acm-bestpractices.html#best-practices-transparency>`__
          .

          - **CertificateTransparencyLoggingPreference** *(string) --*

            You can opt out of certificate transparency logging by specifying the ``DISABLED``
            option. Opt in by specifying ``ENABLED`` .

        :type CertificateAuthorityArn: string
        :param CertificateAuthorityArn:

          The Amazon Resource Name (ARN) of the private certificate authority (CA) that will be used
          to issue the certificate. If you do not provide an ARN and you are trying to request a
          private certificate, ACM will attempt to issue a public certificate. For more information
          about private CAs, see the `AWS Certificate Manager Private Certificate Authority (PCA)
          <https://docs.aws.amazon.com/acm-pca/latest/userguide/PcaWelcome.html>`__ user guide. The
          ARN must have the following form:

           ``arn:aws:acm-pca:region:account:certificate-authority/12345678-1234-1234-1234-123456789012``

        :type Tags: list
        :param Tags:

          One or more resource tags to associate with the certificate.

          - *(dict) --*

            A key-value pair that identifies or specifies metadata about an ACM resource.

            - **Key** *(string) --* **[REQUIRED]**

              The key of the tag.

            - **Value** *(string) --*

              The value of the tag.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'CertificateArn': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **CertificateArn** *(string) --*

              String that contains the ARN of the issued certificate. This must be of the form:

               ``arn:aws:acm:us-east-1:123456789012:certificate/12345678-1234-1234-1234-123456789012``
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def resend_validation_email(
        self, CertificateArn: str, Domain: str, ValidationDomain: str
    ) -> None:
        """
        Resends the email that requests domain ownership validation. The domain owner or an
        authorized representative must approve the ACM certificate before it can be issued. The
        certificate can be approved by clicking a link in the mail to navigate to the Amazon
        certificate approval website and then clicking **I Approve** . However, the validation email
        can be blocked by spam filters. Therefore, if you do not receive the original mail, you can
        request that the mail be resent within 72 hours of requesting the ACM certificate. If more
        than 72 hours have elapsed since your original request or since your last attempt to resend
        validation mail, you must request a new certificate. For more information about setting up
        your contact email addresses, see `Configure Email for your Domain
        <https://docs.aws.amazon.com/acm/latest/userguide/setup-email.html>`__ .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/acm-2015-12-08/ResendValidationEmail>`_

        **Request Syntax**
        ::

          response = client.resend_validation_email(
              CertificateArn='string',
              Domain='string',
              ValidationDomain='string'
          )
        :type CertificateArn: string
        :param CertificateArn: **[REQUIRED]**

          String that contains the ARN of the requested certificate. The certificate ARN is
          generated and returned by the  RequestCertificate action as soon as the request is made.
          By default, using this parameter causes email to be sent to all top-level domains you
          specified in the certificate request. The ARN must be of the form:

           ``arn:aws:acm:us-east-1:123456789012:certificate/12345678-1234-1234-1234-123456789012``

        :type Domain: string
        :param Domain: **[REQUIRED]**

          The fully qualified domain name (FQDN) of the certificate that needs to be validated.

        :type ValidationDomain: string
        :param ValidationDomain: **[REQUIRED]**

          The base validation domain that will act as the suffix of the email addresses that are
          used to send the emails. This must be the same as the ``Domain`` value or a superdomain of
          the ``Domain`` value. For example, if you requested a certificate for
          ``site.subdomain.example.com`` and specify a **ValidationDomain** of
          ``subdomain.example.com`` , ACM sends email to the domain registrant, technical contact,
          and administrative contact in WHOIS and the following five addresses:

          * admin@subdomain.example.com

          * administrator@subdomain.example.com

          * hostmaster@subdomain.example.com

          * postmaster@subdomain.example.com

          * webmaster@subdomain.example.com

        :returns: None
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def update_certificate_options(
        self, CertificateArn: str, Options: ClientUpdateCertificateOptionsOptionsTypeDef
    ) -> None:
        """
        Updates a certificate. Currently, you can use this function to specify whether to opt in to
        or out of recording your certificate in a certificate transparency log. For more
        information, see `Opting Out of Certificate Transparency Logging
        <https://docs.aws.amazon.com/acm/latest/userguide/acm-bestpractices.html#best-practices-transparency>`__
        .

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/acm-2015-12-08/UpdateCertificateOptions>`_

        **Request Syntax**
        ::

          response = client.update_certificate_options(
              CertificateArn='string',
              Options={
                  'CertificateTransparencyLoggingPreference': 'ENABLED'|'DISABLED'
              }
          )
        :type CertificateArn: string
        :param CertificateArn: **[REQUIRED]**

          ARN of the requested certificate to update. This must be of the form:

           ``arn:aws:acm:us-east-1:*account* :certificate/*12345678-1234-1234-1234-123456789012* ``

        :type Options: dict
        :param Options: **[REQUIRED]**

          Use to update the options for your certificate. Currently, you can specify whether to add
          your certificate to a transparency log. Certificate transparency makes it possible to
          detect SSL/TLS certificates that have been mistakenly or maliciously issued. Certificates
          that have not been logged typically produce an error message in a browser.

          - **CertificateTransparencyLoggingPreference** *(string) --*

            You can opt out of certificate transparency logging by specifying the ``DISABLED``
            option. Opt in by specifying ``ENABLED`` .

        :returns: None
        """

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_paginator(
        self, operation_name: Literal["list_certificates"]
    ) -> paginator_scope.ListCertificatesPaginator:
        """
        Get Paginator for `list_certificates` operation.
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

    @overload
    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(
        self, waiter_name: Literal["certificate_validated"]
    ) -> waiter_scope.CertificateValidatedWaiter:
        """
        Get Waiter `certificate_validated`.
        """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def get_waiter(self, waiter_name: str) -> Boto3Waiter:
        """
        Returns an object that can wait for some condition.

        :type waiter_name: str
        :param waiter_name: The name of the waiter to get. See the waiters
            section of the service docs for a list of available waiters.

        :returns: The specified waiter object.
        :rtype: botocore.waiter.Waiter
        """


class Exceptions:
    ClientError: Boto3ClientError
    InvalidArgsException: Boto3ClientError
    InvalidArnException: Boto3ClientError
    InvalidDomainValidationOptionsException: Boto3ClientError
    InvalidParameterException: Boto3ClientError
    InvalidStateException: Boto3ClientError
    InvalidTagException: Boto3ClientError
    LimitExceededException: Boto3ClientError
    RequestInProgressException: Boto3ClientError
    ResourceInUseException: Boto3ClientError
    ResourceNotFoundException: Boto3ClientError
    TagPolicyException: Boto3ClientError
    TooManyTagsException: Boto3ClientError
