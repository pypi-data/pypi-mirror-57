"Main interface for dms service Paginators"
from __future__ import annotations

from datetime import datetime
from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_dms.type_defs import (
    DescribeCertificatesPaginateFiltersTypeDef,
    DescribeCertificatesPaginatePaginationConfigTypeDef,
    DescribeCertificatesPaginateResponseTypeDef,
    DescribeConnectionsPaginateFiltersTypeDef,
    DescribeConnectionsPaginatePaginationConfigTypeDef,
    DescribeConnectionsPaginateResponseTypeDef,
    DescribeEndpointTypesPaginateFiltersTypeDef,
    DescribeEndpointTypesPaginatePaginationConfigTypeDef,
    DescribeEndpointTypesPaginateResponseTypeDef,
    DescribeEndpointsPaginateFiltersTypeDef,
    DescribeEndpointsPaginatePaginationConfigTypeDef,
    DescribeEndpointsPaginateResponseTypeDef,
    DescribeEventSubscriptionsPaginateFiltersTypeDef,
    DescribeEventSubscriptionsPaginatePaginationConfigTypeDef,
    DescribeEventSubscriptionsPaginateResponseTypeDef,
    DescribeEventsPaginateFiltersTypeDef,
    DescribeEventsPaginatePaginationConfigTypeDef,
    DescribeEventsPaginateResponseTypeDef,
    DescribeOrderableReplicationInstancesPaginatePaginationConfigTypeDef,
    DescribeOrderableReplicationInstancesPaginateResponseTypeDef,
    DescribeReplicationInstancesPaginateFiltersTypeDef,
    DescribeReplicationInstancesPaginatePaginationConfigTypeDef,
    DescribeReplicationInstancesPaginateResponseTypeDef,
    DescribeReplicationSubnetGroupsPaginateFiltersTypeDef,
    DescribeReplicationSubnetGroupsPaginatePaginationConfigTypeDef,
    DescribeReplicationSubnetGroupsPaginateResponseTypeDef,
    DescribeReplicationTaskAssessmentResultsPaginatePaginationConfigTypeDef,
    DescribeReplicationTaskAssessmentResultsPaginateResponseTypeDef,
    DescribeReplicationTasksPaginateFiltersTypeDef,
    DescribeReplicationTasksPaginatePaginationConfigTypeDef,
    DescribeReplicationTasksPaginateResponseTypeDef,
    DescribeSchemasPaginatePaginationConfigTypeDef,
    DescribeSchemasPaginateResponseTypeDef,
    DescribeTableStatisticsPaginateFiltersTypeDef,
    DescribeTableStatisticsPaginatePaginationConfigTypeDef,
    DescribeTableStatisticsPaginateResponseTypeDef,
)


__all__ = (
    "DescribeCertificatesPaginator",
    "DescribeConnectionsPaginator",
    "DescribeEndpointTypesPaginator",
    "DescribeEndpointsPaginator",
    "DescribeEventSubscriptionsPaginator",
    "DescribeEventsPaginator",
    "DescribeOrderableReplicationInstancesPaginator",
    "DescribeReplicationInstancesPaginator",
    "DescribeReplicationSubnetGroupsPaginator",
    "DescribeReplicationTaskAssessmentResultsPaginator",
    "DescribeReplicationTasksPaginator",
    "DescribeSchemasPaginator",
    "DescribeTableStatisticsPaginator",
)


class DescribeCertificatesPaginator(Boto3Paginator):
    """
    Paginator for `describe_certificates`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[DescribeCertificatesPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeCertificatesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeCertificatesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`DatabaseMigrationService.Client.describe_certificates`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/DescribeCertificates>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type Filters: list
        :param Filters:

          Filters applied to the certificate described in the form of key-value pairs.

          - *(dict) --*

            - **Name** *(string) --* **[REQUIRED]**

              The name of the filter.

            - **Values** *(list) --* **[REQUIRED]**

              The filter value.

              - *(string) --*

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
                'Certificates': [
                    {
                        'CertificateIdentifier': 'string',
                        'CertificateCreationDate': datetime(2015, 1, 1),
                        'CertificatePem': 'string',
                        'CertificateWallet': b'bytes',
                        'CertificateArn': 'string',
                        'CertificateOwner': 'string',
                        'ValidFromDate': datetime(2015, 1, 1),
                        'ValidToDate': datetime(2015, 1, 1),
                        'SigningAlgorithm': 'string',
                        'KeyLength': 123
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Certificates** *(list) --*

              The Secure Sockets Layer (SSL) certificates associated with the replication instance.

              - *(dict) --*

                The SSL certificate that can be used to encrypt connections between the endpoints
                and the replication instance.

                - **CertificateIdentifier** *(string) --*

                  A customer-assigned name for the certificate. Identifiers must begin with a
                  letter; must contain only ASCII letters, digits, and hyphens; and must not end
                  with a hyphen or contain two consecutive hyphens.

                - **CertificateCreationDate** *(datetime) --*

                  The date that the certificate was created.

                - **CertificatePem** *(string) --*

                  The contents of a ``.pem`` file, which contains an X.509 certificate.

                - **CertificateWallet** *(bytes) --*

                  The location of an imported Oracle Wallet certificate for use with SSL.

                - **CertificateArn** *(string) --*

                  The Amazon Resource Name (ARN) for the certificate.

                - **CertificateOwner** *(string) --*

                  The owner of the certificate.

                - **ValidFromDate** *(datetime) --*

                  The beginning date that the certificate is valid.

                - **ValidToDate** *(datetime) --*

                  The final date that the certificate is valid.

                - **SigningAlgorithm** *(string) --*

                  The signing algorithm for the certificate.

                - **KeyLength** *(integer) --*

                  The key length of the cryptographic algorithm being used.

            - **NextToken** *(string) --*

              A token to resume pagination.
        """


class DescribeConnectionsPaginator(Boto3Paginator):
    """
    Paginator for `describe_connections`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[DescribeConnectionsPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeConnectionsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeConnectionsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`DatabaseMigrationService.Client.describe_connections`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/DescribeConnections>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type Filters: list
        :param Filters:

          The filters applied to the connection.

          Valid filter names: endpoint-arn | replication-instance-arn

          - *(dict) --*

            - **Name** *(string) --* **[REQUIRED]**

              The name of the filter.

            - **Values** *(list) --* **[REQUIRED]**

              The filter value.

              - *(string) --*

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
                'Connections': [
                    {
                        'ReplicationInstanceArn': 'string',
                        'EndpointArn': 'string',
                        'Status': 'string',
                        'LastFailureMessage': 'string',
                        'EndpointIdentifier': 'string',
                        'ReplicationInstanceIdentifier': 'string'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Connections** *(list) --*

              A description of the connections.

              - *(dict) --*

                - **ReplicationInstanceArn** *(string) --*

                  The Amazon Resource Name (ARN) of the replication instance.

                - **EndpointArn** *(string) --*

                  The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.

                - **Status** *(string) --*

                  The connection status.

                - **LastFailureMessage** *(string) --*

                  The error message when the connection last failed.

                - **EndpointIdentifier** *(string) --*

                  The identifier of the endpoint. Identifiers must begin with a letter; must contain
                  only ASCII letters, digits, and hyphens; and must not end with a hyphen or contain
                  two consecutive hyphens.

                - **ReplicationInstanceIdentifier** *(string) --*

                  The replication instance identifier. This parameter is stored as a lowercase
                  string.

            - **NextToken** *(string) --*

              A token to resume pagination.
        """


class DescribeEndpointTypesPaginator(Boto3Paginator):
    """
    Paginator for `describe_endpoint_types`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[DescribeEndpointTypesPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeEndpointTypesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeEndpointTypesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`DatabaseMigrationService.Client.describe_endpoint_types`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/DescribeEndpointTypes>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type Filters: list
        :param Filters:

          Filters applied to the describe action.

          Valid filter names: engine-name | endpoint-type

          - *(dict) --*

            - **Name** *(string) --* **[REQUIRED]**

              The name of the filter.

            - **Values** *(list) --* **[REQUIRED]**

              The filter value.

              - *(string) --*

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
                'SupportedEndpointTypes': [
                    {
                        'EngineName': 'string',
                        'SupportsCDC': True|False,
                        'EndpointType': 'source'|'target',
                        'EngineDisplayName': 'string'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **SupportedEndpointTypes** *(list) --*

              The types of endpoints that are supported.

              - *(dict) --*

                - **EngineName** *(string) --*

                  The database engine name. Valid values, depending on the EndpointType, include
                  mysql, oracle, postgres, mariadb, aurora, aurora-postgresql, redshift, s3, db2,
                  azuredb, sybase, dynamodb, mongodb, and sqlserver.

                - **SupportsCDC** *(boolean) --*

                  Indicates if Change Data Capture (CDC) is supported.

                - **EndpointType** *(string) --*

                  The type of endpoint. Valid values are ``source`` and ``target`` .

                - **EngineDisplayName** *(string) --*

                  The expanded name for the engine name. For example, if the ``EngineName``
                  parameter is "aurora," this value would be "Amazon Aurora MySQL."

            - **NextToken** *(string) --*

              A token to resume pagination.
        """


class DescribeEndpointsPaginator(Boto3Paginator):
    """
    Paginator for `describe_endpoints`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[DescribeEndpointsPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeEndpointsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeEndpointsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`DatabaseMigrationService.Client.describe_endpoints`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/DescribeEndpoints>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type Filters: list
        :param Filters:

          Filters applied to the describe action.

          Valid filter names: endpoint-arn | endpoint-type | endpoint-id | engine-name

          - *(dict) --*

            - **Name** *(string) --* **[REQUIRED]**

              The name of the filter.

            - **Values** *(list) --* **[REQUIRED]**

              The filter value.

              - *(string) --*

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
                'Endpoints': [
                    {
                        'EndpointIdentifier': 'string',
                        'EndpointType': 'source'|'target',
                        'EngineName': 'string',
                        'EngineDisplayName': 'string',
                        'Username': 'string',
                        'ServerName': 'string',
                        'Port': 123,
                        'DatabaseName': 'string',
                        'ExtraConnectionAttributes': 'string',
                        'Status': 'string',
                        'KmsKeyId': 'string',
                        'EndpointArn': 'string',
                        'CertificateArn': 'string',
                        'SslMode': 'none'|'require'|'verify-ca'|'verify-full',
                        'ServiceAccessRoleArn': 'string',
                        'ExternalTableDefinition': 'string',
                        'ExternalId': 'string',
                        'DynamoDbSettings': {
                            'ServiceAccessRoleArn': 'string'
                        },
                        'S3Settings': {
                            'ServiceAccessRoleArn': 'string',
                            'ExternalTableDefinition': 'string',
                            'CsvRowDelimiter': 'string',
                            'CsvDelimiter': 'string',
                            'BucketFolder': 'string',
                            'BucketName': 'string',
                            'CompressionType': 'none'|'gzip',
                            'EncryptionMode': 'sse-s3'|'sse-kms',
                            'ServerSideEncryptionKmsKeyId': 'string',
                            'DataFormat': 'csv'|'parquet',
                            'EncodingType': 'plain'|'plain-dictionary'|'rle-dictionary',
                            'DictPageSizeLimit': 123,
                            'RowGroupLength': 123,
                            'DataPageSize': 123,
                            'ParquetVersion': 'parquet-1-0'|'parquet-2-0',
                            'EnableStatistics': True|False,
                            'IncludeOpForFullLoad': True|False,
                            'CdcInsertsOnly': True|False,
                            'TimestampColumnName': 'string',
                            'ParquetTimestampInMillisecond': True|False
                        },
                        'DmsTransferSettings': {
                            'ServiceAccessRoleArn': 'string',
                            'BucketName': 'string'
                        },
                        'MongoDbSettings': {
                            'Username': 'string',
                            'Password': 'string',
                            'ServerName': 'string',
                            'Port': 123,
                            'DatabaseName': 'string',
                            'AuthType': 'no'|'password',
                            'AuthMechanism': 'default'|'mongodb_cr'|'scram_sha_1',
                            'NestingLevel': 'none'|'one',
                            'ExtractDocId': 'string',
                            'DocsToInvestigate': 'string',
                            'AuthSource': 'string',
                            'KmsKeyId': 'string'
                        },
                        'KinesisSettings': {
                            'StreamArn': 'string',
                            'MessageFormat': 'json',
                            'ServiceAccessRoleArn': 'string'
                        },
                        'ElasticsearchSettings': {
                            'ServiceAccessRoleArn': 'string',
                            'EndpointUri': 'string',
                            'FullLoadErrorPercentage': 123,
                            'ErrorRetryDuration': 123
                        },
                        'RedshiftSettings': {
                            'AcceptAnyDate': True|False,
                            'AfterConnectScript': 'string',
                            'BucketFolder': 'string',
                            'BucketName': 'string',
                            'ConnectionTimeout': 123,
                            'DatabaseName': 'string',
                            'DateFormat': 'string',
                            'EmptyAsNull': True|False,
                            'EncryptionMode': 'sse-s3'|'sse-kms',
                            'FileTransferUploadStreams': 123,
                            'LoadTimeout': 123,
                            'MaxFileSize': 123,
                            'Password': 'string',
                            'Port': 123,
                            'RemoveQuotes': True|False,
                            'ReplaceInvalidChars': 'string',
                            'ReplaceChars': 'string',
                            'ServerName': 'string',
                            'ServiceAccessRoleArn': 'string',
                            'ServerSideEncryptionKmsKeyId': 'string',
                            'TimeFormat': 'string',
                            'TrimBlanks': True|False,
                            'TruncateColumns': True|False,
                            'Username': 'string',
                            'WriteBufferSize': 123
                        }
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Endpoints** *(list) --*

              Endpoint description.

              - *(dict) --*

                - **EndpointIdentifier** *(string) --*

                  The database endpoint identifier. Identifiers must begin with a letter; must
                  contain only ASCII letters, digits, and hyphens; and must not end with a hyphen or
                  contain two consecutive hyphens.

                - **EndpointType** *(string) --*

                  The type of endpoint. Valid values are ``source`` and ``target`` .

                - **EngineName** *(string) --*

                  The database engine name. Valid values, depending on the EndpointType, include
                  mysql, oracle, postgres, mariadb, aurora, aurora-postgresql, redshift, s3, db2,
                  azuredb, sybase, dynamodb, mongodb, and sqlserver.

                - **EngineDisplayName** *(string) --*

                  The expanded name for the engine name. For example, if the ``EngineName``
                  parameter is "aurora," this value would be "Amazon Aurora MySQL."

                - **Username** *(string) --*

                  The user name used to connect to the endpoint.

                - **ServerName** *(string) --*

                  The name of the server at the endpoint.

                - **Port** *(integer) --*

                  The port value used to access the endpoint.

                - **DatabaseName** *(string) --*

                  The name of the database at the endpoint.

                - **ExtraConnectionAttributes** *(string) --*

                  Additional connection attributes used to connect to the endpoint.

                - **Status** *(string) --*

                  The status of the endpoint.

                - **KmsKeyId** *(string) --*

                  An AWS KMS key identifier that is used to encrypt the connection parameters for
                  the endpoint.

                  If you don't specify a value for the ``KmsKeyId`` parameter, then AWS DMS uses
                  your default encryption key.

                  AWS KMS creates the default encryption key for your AWS account. Your AWS account
                  has a different default encryption key for each AWS Region.

                - **EndpointArn** *(string) --*

                  The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.

                - **CertificateArn** *(string) --*

                  The Amazon Resource Name (ARN) used for SSL connection to the endpoint.

                - **SslMode** *(string) --*

                  The SSL mode used to connect to the endpoint. The default value is ``none`` .

                - **ServiceAccessRoleArn** *(string) --*

                  The Amazon Resource Name (ARN) used by the service access IAM role.

                - **ExternalTableDefinition** *(string) --*

                  The external table definition.

                - **ExternalId** *(string) --*

                  Value returned by a call to CreateEndpoint that can be used for cross-account
                  validation. Use it on a subsequent call to CreateEndpoint to create the endpoint
                  with a cross-account.

                - **DynamoDbSettings** *(dict) --*

                  The settings for the target DynamoDB database. For more information, see the
                  ``DynamoDBSettings`` structure.

                  - **ServiceAccessRoleArn** *(string) --*

                    The Amazon Resource Name (ARN) used by the service access IAM role.

                - **S3Settings** *(dict) --*

                  The settings for the S3 target endpoint. For more information, see the
                  ``S3Settings`` structure.

                  - **ServiceAccessRoleArn** *(string) --*

                    The Amazon Resource Name (ARN) used by the service access IAM role.

                  - **ExternalTableDefinition** *(string) --*

                    The external table definition.

                  - **CsvRowDelimiter** *(string) --*

                    The delimiter used to separate rows in the source files. The default is a
                    carriage return (``\\n`` ).

                  - **CsvDelimiter** *(string) --*

                    The delimiter used to separate columns in the source files. The default is a
                    comma.

                  - **BucketFolder** *(string) --*

                    An optional parameter to set a folder name in the S3 bucket. If provided, tables
                    are created in the path `` *bucketFolder* /*schema_name* /*table_name* /`` . If
                    this parameter is not specified, then the path used is `` *schema_name*
                    /*table_name* /`` .

                  - **BucketName** *(string) --*

                    The name of the S3 bucket.

                  - **CompressionType** *(string) --*

                    An optional parameter to use GZIP to compress the target files. Set to GZIP to
                    compress the target files. Set to NONE (the default) or do not use to leave the
                    files uncompressed. Applies to both .csv and .parquet file formats.

                  - **EncryptionMode** *(string) --*

                    The type of server-side encryption that you want to use for your data. This
                    encryption type is part of the endpoint settings or the extra connections
                    attributes for Amazon S3. You can choose either ``SSE_S3`` (the default) or
                    ``SSE_KMS`` . To use ``SSE_S3`` , you need an AWS Identity and Access Management
                    (IAM) role with permission to allow ``"arn:aws:s3:::dms-*"`` to use the
                    following actions:

                    * ``s3:CreateBucket``

                    * ``s3:ListBucket``

                    * ``s3:DeleteBucket``

                    * ``s3:GetBucketLocation``

                    * ``s3:GetObject``

                    * ``s3:PutObject``

                    * ``s3:DeleteObject``

                    * ``s3:GetObjectVersion``

                    * ``s3:GetBucketPolicy``

                    * ``s3:PutBucketPolicy``

                    * ``s3:DeleteBucketPolicy``

                  - **ServerSideEncryptionKmsKeyId** *(string) --*

                    If you are using ``SSE_KMS`` for the ``EncryptionMode`` , provide the AWS KMS
                    key ID. The key that you use needs an attached policy that enables AWS Identity
                    and Access Management (IAM) user permissions and allows use of the key.

                    Here is a CLI example: ``aws dms create-endpoint --endpoint-identifier *value*
                    --endpoint-type target --engine-name s3 --s3-settings
                    ServiceAccessRoleArn=*value* ,BucketFolder=*value* ,BucketName=
                        *value*
                    ,EncryptionMode=SSE_KMS,ServerSideEncryptionKmsKeyId=*value* ``

                  - **DataFormat** *(string) --*

                    The format of the data that you want to use for output. You can choose one of
                    the following:

                    * ``csv`` : This is a row-based file format with comma-separated values (.csv).

                    * ``parquet`` : Apache Parquet (.parquet) is a columnar storage file format that
                    features efficient compression and provides faster query response.

                  - **EncodingType** *(string) --*

                    The type of encoding you are using:

                    * ``RLE_DICTIONARY`` uses a combination of bit-packing and run-length encoding
                    to store repeated values more efficiently. This is the default.

                    * ``PLAIN`` doesn't use encoding at all. Values are stored as they are.

                    * ``PLAIN_DICTIONARY`` builds a dictionary of the values encountered in a given
                    column. The dictionary is stored in a dictionary page for each column chunk.

                  - **DictPageSizeLimit** *(integer) --*

                    The maximum size of an encoded dictionary page of a column. If the dictionary
                    page exceeds this, this column is stored using an encoding type of ``PLAIN`` .
                    This parameter defaults to 1024 * 1024 bytes (1 MiB), the maximum size of a
                    dictionary page before it reverts to ``PLAIN`` encoding. This size is used for
                    .parquet file format only.

                  - **RowGroupLength** *(integer) --*

                    The number of rows in a row group. A smaller row group size provides faster
                    reads. But as the number of row groups grows, the slower writes become. This
                    parameter defaults to 10,000 rows. This number is used for .parquet file format
                    only.

                    If you choose a value larger than the maximum, ``RowGroupLength`` is set to the
                    max row group length in bytes (64 * 1024 * 1024).

                  - **DataPageSize** *(integer) --*

                    The size of one data page in bytes. This parameter defaults to 1024 * 1024 bytes
                    (1 MiB). This number is used for .parquet file format only.

                  - **ParquetVersion** *(string) --*

                    The version of the Apache Parquet format that you want to use: ``parquet_1_0``
                    (the default) or ``parquet_2_0`` .

                  - **EnableStatistics** *(boolean) --*

                    A value that enables statistics for Parquet pages and row groups. Choose
                    ``true`` to enable statistics, ``false`` to disable. Statistics include ``NULL``
                    , ``DISTINCT`` , ``MAX`` , and ``MIN`` values. This parameter defaults to
                    ``true`` . This value is used for .parquet file format only.

                  - **IncludeOpForFullLoad** *(boolean) --*

                    A value that enables a full load to write INSERT operations to the
                    comma-separated value (.csv) output files only to indicate how the rows were
                    added to the source database.

                    .. note::

                      AWS DMS supports the ``IncludeOpForFullLoad`` parameter in versions 3.1.4 and
                      later.

                    For full load, records can only be inserted. By default (the ``false`` setting),
                    no information is recorded in these output files for a full load to indicate
                    that the rows were inserted at the source database. If ``IncludeOpForFullLoad``
                    is set to ``true`` or ``y`` , the INSERT is recorded as an I annotation in the
                    first field of the .csv file. This allows the format of your target records from
                    a full load to be consistent with the target records from a CDC load.

                    .. note::

                      This setting works together with the ``CdcInsertsOnly`` parameter for output
                      to .csv files only. For more information about how these settings work
                      together, see `Indicating Source DB Operations in Migrated S3 Data
                      <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring.InsertOps>`__
                      in the *AWS Database Migration Service User Guide.* .

                  - **CdcInsertsOnly** *(boolean) --*

                    A value that enables a change data capture (CDC) load to write only INSERT
                    operations to .csv or columnar storage (.parquet) output files. By default (the
                    ``false`` setting), the first field in a .csv or .parquet record contains the
                    letter I (INSERT), U (UPDATE), or D (DELETE). These values indicate whether the
                    row was inserted, updated, or deleted at the source database for a CDC load to
                    the target.

                    If ``CdcInsertsOnly`` is set to ``true`` or ``y`` , only INSERTs from the source
                    database are migrated to the .csv or .parquet file. For .csv format only, how
                    these INSERTs are recorded depends on the value of ``IncludeOpForFullLoad`` . If
                    ``IncludeOpForFullLoad`` is set to ``true`` , the first field of every CDC
                    record is set to I to indicate the INSERT operation at the source. If
                    ``IncludeOpForFullLoad`` is set to ``false`` , every CDC record is written
                    without a first field to indicate the INSERT operation at the source. For more
                    information about how these settings work together, see `Indicating Source DB
                    Operations in Migrated S3 Data
                    <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring.InsertOps>`__
                    in the *AWS Database Migration Service User Guide.* .

                    .. note::

                      AWS DMS supports this interaction between the ``CdcInsertsOnly`` and
                      ``IncludeOpForFullLoad`` parameters in versions 3.1.4 and later.

                  - **TimestampColumnName** *(string) --*

                    A value that when nonblank causes AWS DMS to add a column with timestamp
                    information to the endpoint data for an Amazon S3 target.

                    .. note::

                      AWS DMS supports the ``TimestampColumnName`` parameter in versions 3.1.4 and
                      later.

                    DMS includes an additional ``STRING`` column in the .csv or .parquet object
                    files of your migrated data when you set ``TimestampColumnName`` to a nonblank
                    value.

                    For a full load, each row of this timestamp column contains a timestamp for when
                    the data was transferred from the source to the target by DMS.

                    For a change data capture (CDC) load, each row of the timestamp column contains
                    the timestamp for the commit of that row in the source database.

                    The string format for this timestamp column value is ``yyyy-MM-dd
                    HH:mm:ss.SSSSSS`` . By default, the precision of this value is in microseconds.
                    For a CDC load, the rounding of the precision depends on the commit timestamp
                    supported by DMS for the source database.

                    When the ``AddColumnName`` parameter is set to ``true`` , DMS also includes a
                    name for the timestamp column that you set with ``TimestampColumnName`` .

                  - **ParquetTimestampInMillisecond** *(boolean) --*

                    A value that specifies the precision of any ``TIMESTAMP`` column values that are
                    written to an Amazon S3 object file in .parquet format.

                    .. note::

                      AWS DMS supports the ``ParquetTimestampInMillisecond`` parameter in versions
                      3.1.4 and later.

                    When ``ParquetTimestampInMillisecond`` is set to ``true`` or ``y`` , AWS DMS
                    writes all ``TIMESTAMP`` columns in a .parquet formatted file with millisecond
                    precision. Otherwise, DMS writes them with microsecond precision.

                    Currently, Amazon Athena and AWS Glue can handle only millisecond precision for
                    ``TIMESTAMP`` values. Set this parameter to ``true`` for S3 endpoint object
                    files that are .parquet formatted only if you plan to query or process the data
                    with Athena or AWS Glue.

                    .. note::

                      AWS DMS writes any ``TIMESTAMP`` column values written to an S3 file in .csv
                      format with microsecond precision.

                      Setting ``ParquetTimestampInMillisecond`` has no effect on the string format
                      of the timestamp column value that is inserted by setting the
                      ``TimestampColumnName`` parameter.

                - **DmsTransferSettings** *(dict) --*

                  The settings in JSON format for the DMS transfer type of source endpoint.

                  Possible settings include the following:

                  * ``ServiceAccessRoleArn`` - The IAM role that has permission to access the Amazon
                  S3 bucket.

                  * ``BucketName`` - The name of the S3 bucket to use.

                  * ``CompressionType`` - An optional parameter to use GZIP to compress the target
                  files. To use GZIP, set this value to ``NONE`` (the default). To keep the files
                  uncompressed, don't use this value.

                  Shorthand syntax for these settings is as follows:
                  ``ServiceAccessRoleArn=string,BucketName=string,CompressionType=string``

                  JSON syntax for these settings is as follows: ``{ "ServiceAccessRoleArn":
                  "string", "BucketName": "string", "CompressionType": "none"|"gzip" }``

                  - **ServiceAccessRoleArn** *(string) --*

                    The IAM role that has permission to access the Amazon S3 bucket.

                  - **BucketName** *(string) --*

                    The name of the S3 bucket to use.

                - **MongoDbSettings** *(dict) --*

                  The settings for the MongoDB source endpoint. For more information, see the
                  ``MongoDbSettings`` structure.

                  - **Username** *(string) --*

                    The user name you use to access the MongoDB source endpoint.

                  - **Password** *(string) --*

                    The password for the user account you use to access the MongoDB source endpoint.

                  - **ServerName** *(string) --*

                    The name of the server on the MongoDB source endpoint.

                  - **Port** *(integer) --*

                    The port value for the MongoDB source endpoint.

                  - **DatabaseName** *(string) --*

                    The database name on the MongoDB source endpoint.

                  - **AuthType** *(string) --*

                    The authentication type you use to access the MongoDB source endpoint.

                    Valid values: NO, PASSWORD

                    When NO is selected, user name and password parameters are not used and can be
                    empty.

                  - **AuthMechanism** *(string) --*

                    The authentication mechanism you use to access the MongoDB source endpoint.

                    Valid values: DEFAULT, MONGODB_CR, SCRAM_SHA_1

                    DEFAULT – For MongoDB version 2.x, use MONGODB_CR. For MongoDB version 3.x, use
                    SCRAM_SHA_1. This setting is not used when authType=No.

                  - **NestingLevel** *(string) --*

                    Specifies either document or table mode.

                    Valid values: NONE, ONE

                    Default value is NONE. Specify NONE to use document mode. Specify ONE to use
                    table mode.

                  - **ExtractDocId** *(string) --*

                    Specifies the document ID. Use this setting when ``NestingLevel`` is set to
                    NONE.

                    Default value is false.

                  - **DocsToInvestigate** *(string) --*

                    Indicates the number of documents to preview to determine the document
                    organization. Use this setting when ``NestingLevel`` is set to ONE.

                    Must be a positive value greater than 0. Default value is 1000.

                  - **AuthSource** *(string) --*

                    The MongoDB database name. This setting is not used when ``authType=NO`` .

                    The default is admin.

                  - **KmsKeyId** *(string) --*

                    The AWS KMS key identifier that is used to encrypt the content on the
                    replication instance. If you don't specify a value for the ``KmsKeyId``
                    parameter, then AWS DMS uses your default encryption key. AWS KMS creates the
                    default encryption key for your AWS account. Your AWS account has a different
                    default encryption key for each AWS Region.

                - **KinesisSettings** *(dict) --*

                  The settings for the Amazon Kinesis source endpoint. For more information, see the
                  ``KinesisSettings`` structure.

                  - **StreamArn** *(string) --*

                    The Amazon Resource Name (ARN) for the Amazon Kinesis Data Streams endpoint.

                  - **MessageFormat** *(string) --*

                    The output format for the records created on the endpoint. The message format is
                    ``JSON`` .

                  - **ServiceAccessRoleArn** *(string) --*

                    The Amazon Resource Name (ARN) for the IAM role that DMS uses to write to the
                    Amazon Kinesis data stream.

                - **ElasticsearchSettings** *(dict) --*

                  The settings for the Elasticsearch source endpoint. For more information, see the
                  ``ElasticsearchSettings`` structure.

                  - **ServiceAccessRoleArn** *(string) --*

                    The Amazon Resource Name (ARN) used by service to access the IAM role.

                  - **EndpointUri** *(string) --*

                    The endpoint for the Elasticsearch cluster.

                  - **FullLoadErrorPercentage** *(integer) --*

                    The maximum percentage of records that can fail to be written before a full load
                    operation stops.

                  - **ErrorRetryDuration** *(integer) --*

                    The maximum number of seconds that DMS retries failed API requests to the
                    Elasticsearch cluster.

                - **RedshiftSettings** *(dict) --*

                  Settings for the Amazon Redshift endpoint.

                  - **AcceptAnyDate** *(boolean) --*

                    A value that indicates to allow any date format, including invalid formats such
                    as 00/00/00 00:00:00, to be loaded without generating an error. You can choose
                    ``true`` or ``false`` (the default).

                    This parameter applies only to TIMESTAMP and DATE columns. Always use
                    ACCEPTANYDATE with the DATEFORMAT parameter. If the date format for the data
                    doesn't match the DATEFORMAT specification, Amazon Redshift inserts a NULL value
                    into that field.

                  - **AfterConnectScript** *(string) --*

                    Code to run after connecting. This parameter should contain the code itself, not
                    the name of a file containing the code.

                  - **BucketFolder** *(string) --*

                    The location where the comma-separated value (.csv) files are stored before
                    being uploaded to the S3 bucket.

                  - **BucketName** *(string) --*

                    The name of the S3 bucket you want to use

                  - **ConnectionTimeout** *(integer) --*

                    A value that sets the amount of time to wait (in milliseconds) before timing
                    out, beginning from when you initially establish a connection.

                  - **DatabaseName** *(string) --*

                    The name of the Amazon Redshift data warehouse (service) that you are working
                    with.

                  - **DateFormat** *(string) --*

                    The date format that you are using. Valid values are ``auto`` (case-sensitive),
                    your date format string enclosed in quotes, or NULL. If this parameter is left
                    unset (NULL), it defaults to a format of 'YYYY-MM-DD'. Using ``auto`` recognizes
                    most strings, even some that aren't supported when you use a date format string.

                    If your date and time values use formats different from each other, set this to
                    ``auto`` .

                  - **EmptyAsNull** *(boolean) --*

                    A value that specifies whether AWS DMS should migrate empty CHAR and VARCHAR
                    fields as NULL. A value of ``true`` sets empty CHAR and VARCHAR fields to null.
                    The default is ``false`` .

                  - **EncryptionMode** *(string) --*

                    The type of server-side encryption that you want to use for your data. This
                    encryption type is part of the endpoint settings or the extra connections
                    attributes for Amazon S3. You can choose either ``SSE_S3`` (the default) or
                    ``SSE_KMS`` . To use ``SSE_S3`` , create an AWS Identity and Access Management
                    (IAM) role with a policy that allows ``"arn:aws:s3:::*"`` to use the following
                    actions: ``"s3:PutObject", "s3:ListBucket"``

                  - **FileTransferUploadStreams** *(integer) --*

                    The number of threads used to upload a single file. This parameter accepts a
                    value from 1 through 64. It defaults to 10.

                  - **LoadTimeout** *(integer) --*

                    The amount of time to wait (in milliseconds) before timing out, beginning from
                    when you begin loading.

                  - **MaxFileSize** *(integer) --*

                    The maximum size (in KB) of any .csv file used to transfer data to Amazon
                    Redshift. This accepts a value from 1 through 1,048,576. It defaults to 32,768
                    KB (32 MB).

                  - **Password** *(string) --*

                    The password for the user named in the ``username`` property.

                  - **Port** *(integer) --*

                    The port number for Amazon Redshift. The default value is 5439.

                  - **RemoveQuotes** *(boolean) --*

                    A value that specifies to remove surrounding quotation marks from strings in the
                    incoming data. All characters within the quotation marks, including delimiters,
                    are retained. Choose ``true`` to remove quotation marks. The default is
                    ``false`` .

                  - **ReplaceInvalidChars** *(string) --*

                    A list of characters that you want to replace. Use with ``ReplaceChars`` .

                  - **ReplaceChars** *(string) --*

                    A value that specifies to replaces the invalid characters specified in
                    ``ReplaceInvalidChars`` , substituting the specified characters instead. The
                    default is ``"?"`` .

                  - **ServerName** *(string) --*

                    The name of the Amazon Redshift cluster you are using.

                  - **ServiceAccessRoleArn** *(string) --*

                    The Amazon Resource Name (ARN) of the IAM role that has access to the Amazon
                    Redshift service.

                  - **ServerSideEncryptionKmsKeyId** *(string) --*

                    The AWS KMS key ID. If you are using ``SSE_KMS`` for the ``EncryptionMode`` ,
                    provide this key ID. The key that you use needs an attached policy that enables
                    IAM user permissions and allows use of the key.

                  - **TimeFormat** *(string) --*

                    The time format that you want to use. Valid values are ``auto``
                    (case-sensitive), ``'timeformat_string'`` , ``'epochsecs'`` , or
                    ``'epochmillisecs'`` . It defaults to 10. Using ``auto`` recognizes most
                    strings, even some that aren't supported when you use a time format string.

                    If your date and time values use formats different from each other, set this
                    parameter to ``auto`` .

                  - **TrimBlanks** *(boolean) --*

                    A value that specifies to remove the trailing white space characters from a
                    VARCHAR string. This parameter applies only to columns with a VARCHAR data type.
                    Choose ``true`` to remove unneeded white space. The default is ``false`` .

                  - **TruncateColumns** *(boolean) --*

                    A value that specifies to truncate data in columns to the appropriate number of
                    characters, so that the data fits in the column. This parameter applies only to
                    columns with a VARCHAR or CHAR data type, and rows with a size of 4 MB or less.
                    Choose ``true`` to truncate data. The default is ``false`` .

                  - **Username** *(string) --*

                    An Amazon Redshift user name for a registered user.

                  - **WriteBufferSize** *(integer) --*

                    The size of the write buffer to use in rows. Valid values range from 1 through
                    2,048. The default is 1,024. Use this setting to tune performance.

            - **NextToken** *(string) --*

              A token to resume pagination.
        """


class DescribeEventSubscriptionsPaginator(Boto3Paginator):
    """
    Paginator for `describe_event_subscriptions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        SubscriptionName: str = None,
        Filters: List[DescribeEventSubscriptionsPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeEventSubscriptionsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeEventSubscriptionsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`DatabaseMigrationService.Client.describe_event_subscriptions`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/DescribeEventSubscriptions>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              SubscriptionName='string',
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type SubscriptionName: string
        :param SubscriptionName:

          The name of the AWS DMS event subscription to be described.

        :type Filters: list
        :param Filters:

          Filters applied to the action.

          - *(dict) --*

            - **Name** *(string) --* **[REQUIRED]**

              The name of the filter.

            - **Values** *(list) --* **[REQUIRED]**

              The filter value.

              - *(string) --*

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
                'EventSubscriptionsList': [
                    {
                        'CustomerAwsId': 'string',
                        'CustSubscriptionId': 'string',
                        'SnsTopicArn': 'string',
                        'Status': 'string',
                        'SubscriptionCreationTime': 'string',
                        'SourceType': 'string',
                        'SourceIdsList': [
                            'string',
                        ],
                        'EventCategoriesList': [
                            'string',
                        ],
                        'Enabled': True|False
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **EventSubscriptionsList** *(list) --*

              A list of event subscriptions.

              - *(dict) --*

                - **CustomerAwsId** *(string) --*

                  The AWS customer account associated with the AWS DMS event notification
                  subscription.

                - **CustSubscriptionId** *(string) --*

                  The AWS DMS event notification subscription Id.

                - **SnsTopicArn** *(string) --*

                  The topic ARN of the AWS DMS event notification subscription.

                - **Status** *(string) --*

                  The status of the AWS DMS event notification subscription.

                  Constraints:

                  Can be one of the following: creating | modifying | deleting | active |
                  no-permission | topic-not-exist

                  The status "no-permission" indicates that AWS DMS no longer has permission to post
                  to the SNS topic. The status "topic-not-exist" indicates that the topic was
                  deleted after the subscription was created.

                - **SubscriptionCreationTime** *(string) --*

                  The time the RDS event notification subscription was created.

                - **SourceType** *(string) --*

                  The type of AWS DMS resource that generates events.

                  Valid values: replication-instance | replication-server
                  | security-group |
                  replication-task

                - **SourceIdsList** *(list) --*

                  A list of source Ids for the event subscription.

                  - *(string) --*

                - **EventCategoriesList** *(list) --*

                  A lists of event categories.

                  - *(string) --*

                - **Enabled** *(boolean) --*

                  Boolean value that indicates if the event subscription is enabled.

            - **NextToken** *(string) --*

              A token to resume pagination.
        """


class DescribeEventsPaginator(Boto3Paginator):
    """
    Paginator for `describe_events`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        SourceIdentifier: str = None,
        SourceType: str = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        Duration: int = None,
        EventCategories: List[str] = None,
        Filters: List[DescribeEventsPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeEventsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeEventsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`DatabaseMigrationService.Client.describe_events`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/DescribeEvents>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              SourceIdentifier='string',
              SourceType='replication-instance',
              StartTime=datetime(2015, 1, 1),
              EndTime=datetime(2015, 1, 1),
              Duration=123,
              EventCategories=[
                  'string',
              ],
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type SourceIdentifier: string
        :param SourceIdentifier:

          The identifier of an event source.

        :type SourceType: string
        :param SourceType:

          The type of AWS DMS resource that generates events.

          Valid values: replication-instance | replication-task

        :type StartTime: datetime
        :param StartTime:

          The start time for the events to be listed.

        :type EndTime: datetime
        :param EndTime:

          The end time for the events to be listed.

        :type Duration: integer
        :param Duration:

          The duration of the events to be listed.

        :type EventCategories: list
        :param EventCategories:

          A list of event categories for the source type that you've chosen.

          - *(string) --*

        :type Filters: list
        :param Filters:

          Filters applied to the action.

          - *(dict) --*

            - **Name** *(string) --* **[REQUIRED]**

              The name of the filter.

            - **Values** *(list) --* **[REQUIRED]**

              The filter value.

              - *(string) --*

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
                'Events': [
                    {
                        'SourceIdentifier': 'string',
                        'SourceType': 'replication-instance',
                        'Message': 'string',
                        'EventCategories': [
                            'string',
                        ],
                        'Date': datetime(2015, 1, 1)
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Events** *(list) --*

              The events described.

              - *(dict) --*

                - **SourceIdentifier** *(string) --*

                  The identifier of an event source.

                - **SourceType** *(string) --*

                  The type of AWS DMS resource that generates events.

                  Valid values: replication-instance | endpoint | replication-task

                - **Message** *(string) --*

                  The event message.

                - **EventCategories** *(list) --*

                  The event categories available for the specified source type.

                  - *(string) --*

                - **Date** *(datetime) --*

                  The date of the event.

            - **NextToken** *(string) --*

              A token to resume pagination.
        """


class DescribeOrderableReplicationInstancesPaginator(Boto3Paginator):
    """
    Paginator for `describe_orderable_replication_instances`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        PaginationConfig: DescribeOrderableReplicationInstancesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeOrderableReplicationInstancesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`DatabaseMigrationService.Client.describe_orderable_replication_instances`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/DescribeOrderableReplicationInstances>`_

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
                'OrderableReplicationInstances': [
                    {
                        'EngineVersion': 'string',
                        'ReplicationInstanceClass': 'string',
                        'StorageType': 'string',
                        'MinAllocatedStorage': 123,
                        'MaxAllocatedStorage': 123,
                        'DefaultAllocatedStorage': 123,
                        'IncludedAllocatedStorage': 123,
                        'AvailabilityZones': [
                            'string',
                        ],
                        'ReleaseStatus': 'beta'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **OrderableReplicationInstances** *(list) --*

              The order-able replication instances available.

              - *(dict) --*

                - **EngineVersion** *(string) --*

                  The version of the replication engine.

                - **ReplicationInstanceClass** *(string) --*

                  The compute and memory capacity of the replication instance.

                  Valid Values: ``dms.t2.micro | dms.t2.small | dms.t2.medium
                  | dms.t2.large |
                  dms.c4.large | dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge``

                - **StorageType** *(string) --*

                  The type of storage used by the replication instance.

                - **MinAllocatedStorage** *(integer) --*

                  The minimum amount of storage (in gigabytes) that can be allocated for the
                  replication instance.

                - **MaxAllocatedStorage** *(integer) --*

                  The minimum amount of storage (in gigabytes) that can be allocated for the
                  replication instance.

                - **DefaultAllocatedStorage** *(integer) --*

                  The default amount of storage (in gigabytes) that is allocated for the replication
                  instance.

                - **IncludedAllocatedStorage** *(integer) --*

                  The amount of storage (in gigabytes) that is allocated for the replication
                  instance.

                - **AvailabilityZones** *(list) --*

                  List of Availability Zones for this replication instance.

                  - *(string) --*

                - **ReleaseStatus** *(string) --*

                  The value returned when the specified ``EngineVersion`` of the replication
                  instance is in Beta or test mode. This indicates some features might not work as
                  expected.

                  .. note::

                    AWS DMS supports the ``ReleaseStatus`` parameter in versions 3.1.4 and later.

            - **NextToken** *(string) --*

              A token to resume pagination.
        """


class DescribeReplicationInstancesPaginator(Boto3Paginator):
    """
    Paginator for `describe_replication_instances`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[DescribeReplicationInstancesPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeReplicationInstancesPaginatePaginationConfigTypeDef = None,
    ) -> DescribeReplicationInstancesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`DatabaseMigrationService.Client.describe_replication_instances`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/DescribeReplicationInstances>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type Filters: list
        :param Filters:

          Filters applied to the describe action.

          Valid filter names: replication-instance-arn | replication-instance-id |
          replication-instance-class | engine-version

          - *(dict) --*

            - **Name** *(string) --* **[REQUIRED]**

              The name of the filter.

            - **Values** *(list) --* **[REQUIRED]**

              The filter value.

              - *(string) --*

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
                'ReplicationInstances': [
                    {
                        'ReplicationInstanceIdentifier': 'string',
                        'ReplicationInstanceClass': 'string',
                        'ReplicationInstanceStatus': 'string',
                        'AllocatedStorage': 123,
                        'InstanceCreateTime': datetime(2015, 1, 1),
                        'VpcSecurityGroups': [
                            {
                                'VpcSecurityGroupId': 'string',
                                'Status': 'string'
                            },
                        ],
                        'AvailabilityZone': 'string',
                        'ReplicationSubnetGroup': {
                            'ReplicationSubnetGroupIdentifier': 'string',
                            'ReplicationSubnetGroupDescription': 'string',
                            'VpcId': 'string',
                            'SubnetGroupStatus': 'string',
                            'Subnets': [
                                {
                                    'SubnetIdentifier': 'string',
                                    'SubnetAvailabilityZone': {
                                        'Name': 'string'
                                    },
                                    'SubnetStatus': 'string'
                                },
                            ]
                        },
                        'PreferredMaintenanceWindow': 'string',
                        'PendingModifiedValues': {
                            'ReplicationInstanceClass': 'string',
                            'AllocatedStorage': 123,
                            'MultiAZ': True|False,
                            'EngineVersion': 'string'
                        },
                        'MultiAZ': True|False,
                        'EngineVersion': 'string',
                        'AutoMinorVersionUpgrade': True|False,
                        'KmsKeyId': 'string',
                        'ReplicationInstanceArn': 'string',
                        'ReplicationInstancePublicIpAddress': 'string',
                        'ReplicationInstancePrivateIpAddress': 'string',
                        'ReplicationInstancePublicIpAddresses': [
                            'string',
                        ],
                        'ReplicationInstancePrivateIpAddresses': [
                            'string',
                        ],
                        'PubliclyAccessible': True|False,
                        'SecondaryAvailabilityZone': 'string',
                        'FreeUntil': datetime(2015, 1, 1),
                        'DnsNameServers': 'string'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **ReplicationInstances** *(list) --*

              The replication instances described.

              - *(dict) --*

                - **ReplicationInstanceIdentifier** *(string) --*

                  The replication instance identifier. This parameter is stored as a lowercase
                  string.

                  Constraints:

                  * Must contain from 1 to 63 alphanumeric characters or hyphens.

                  * First character must be a letter.

                  * Cannot end with a hyphen or contain two consecutive hyphens.

                  Example: ``myrepinstance``

                - **ReplicationInstanceClass** *(string) --*

                  The compute and memory capacity of the replication instance.

                  Valid Values: ``dms.t2.micro | dms.t2.small | dms.t2.medium
                  | dms.t2.large |
                  dms.c4.large | dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge``

                - **ReplicationInstanceStatus** *(string) --*

                  The status of the replication instance.

                - **AllocatedStorage** *(integer) --*

                  The amount of storage (in gigabytes) that is allocated for the replication
                  instance.

                - **InstanceCreateTime** *(datetime) --*

                  The time the replication instance was created.

                - **VpcSecurityGroups** *(list) --*

                  The VPC security group for the instance.

                  - *(dict) --*

                    - **VpcSecurityGroupId** *(string) --*

                      The VPC security group Id.

                    - **Status** *(string) --*

                      The status of the VPC security group.

                - **AvailabilityZone** *(string) --*

                  The Availability Zone for the instance.

                - **ReplicationSubnetGroup** *(dict) --*

                  The subnet group for the replication instance.

                  - **ReplicationSubnetGroupIdentifier** *(string) --*

                    The identifier of the replication instance subnet group.

                  - **ReplicationSubnetGroupDescription** *(string) --*

                    A description for the replication subnet group.

                  - **VpcId** *(string) --*

                    The ID of the VPC.

                  - **SubnetGroupStatus** *(string) --*

                    The status of the subnet group.

                  - **Subnets** *(list) --*

                    The subnets that are in the subnet group.

                    - *(dict) --*

                      - **SubnetIdentifier** *(string) --*

                        The subnet identifier.

                      - **SubnetAvailabilityZone** *(dict) --*

                        The Availability Zone of the subnet.

                        - **Name** *(string) --*

                          The name of the availability zone.

                      - **SubnetStatus** *(string) --*

                        The status of the subnet.

                - **PreferredMaintenanceWindow** *(string) --*

                  The maintenance window times for the replication instance.

                - **PendingModifiedValues** *(dict) --*

                  The pending modification values.

                  - **ReplicationInstanceClass** *(string) --*

                    The compute and memory capacity of the replication instance.

                    Valid Values: ``dms.t2.micro | dms.t2.small | dms.t2.medium
                    | dms.t2.large |
                    dms.c4.large | dms.c4.xlarge | dms.c4.2xlarge | dms.c4.4xlarge``

                  - **AllocatedStorage** *(integer) --*

                    The amount of storage (in gigabytes) that is allocated for the replication
                    instance.

                  - **MultiAZ** *(boolean) --*

                    Specifies whether the replication instance is a Multi-AZ deployment. You cannot
                    set the ``AvailabilityZone`` parameter if the Multi-AZ parameter is set to
                    ``true`` .

                  - **EngineVersion** *(string) --*

                    The engine version number of the replication instance.

                - **MultiAZ** *(boolean) --*

                  Specifies whether the replication instance is a Multi-AZ deployment. You cannot
                  set the ``AvailabilityZone`` parameter if the Multi-AZ parameter is set to
                  ``true`` .

                - **EngineVersion** *(string) --*

                  The engine version number of the replication instance.

                - **AutoMinorVersionUpgrade** *(boolean) --*

                  Boolean value indicating if minor version upgrades will be automatically applied
                  to the instance.

                - **KmsKeyId** *(string) --*

                  An AWS KMS key identifier that is used to encrypt the data on the replication
                  instance.

                  If you don't specify a value for the ``KmsKeyId`` parameter, then AWS DMS uses
                  your default encryption key.

                  AWS KMS creates the default encryption key for your AWS account. Your AWS account
                  has a different default encryption key for each AWS Region.

                - **ReplicationInstanceArn** *(string) --*

                  The Amazon Resource Name (ARN) of the replication instance.

                - **ReplicationInstancePublicIpAddress** *(string) --*

                  The public IP address of the replication instance.

                - **ReplicationInstancePrivateIpAddress** *(string) --*

                  The private IP address of the replication instance.

                - **ReplicationInstancePublicIpAddresses** *(list) --*

                  One or more public IP addresses for the replication instance.

                  - *(string) --*

                - **ReplicationInstancePrivateIpAddresses** *(list) --*

                  One or more private IP addresses for the replication instance.

                  - *(string) --*

                - **PubliclyAccessible** *(boolean) --*

                  Specifies the accessibility options for the replication instance. A value of
                  ``true`` represents an instance with a public IP address. A value of ``false``
                  represents an instance with a private IP address. The default value is ``true`` .

                - **SecondaryAvailabilityZone** *(string) --*

                  The availability zone of the standby replication instance in a Multi-AZ
                  deployment.

                - **FreeUntil** *(datetime) --*

                  The expiration date of the free replication instance that is part of the Free DMS
                  program.

                - **DnsNameServers** *(string) --*

                  The DNS name servers for the replication instance.

            - **NextToken** *(string) --*

              A token to resume pagination.
        """


class DescribeReplicationSubnetGroupsPaginator(Boto3Paginator):
    """
    Paginator for `describe_replication_subnet_groups`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[DescribeReplicationSubnetGroupsPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeReplicationSubnetGroupsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeReplicationSubnetGroupsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`DatabaseMigrationService.Client.describe_replication_subnet_groups`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/DescribeReplicationSubnetGroups>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type Filters: list
        :param Filters:

          Filters applied to the describe action.

          - *(dict) --*

            - **Name** *(string) --* **[REQUIRED]**

              The name of the filter.

            - **Values** *(list) --* **[REQUIRED]**

              The filter value.

              - *(string) --*

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
                'ReplicationSubnetGroups': [
                    {
                        'ReplicationSubnetGroupIdentifier': 'string',
                        'ReplicationSubnetGroupDescription': 'string',
                        'VpcId': 'string',
                        'SubnetGroupStatus': 'string',
                        'Subnets': [
                            {
                                'SubnetIdentifier': 'string',
                                'SubnetAvailabilityZone': {
                                    'Name': 'string'
                                },
                                'SubnetStatus': 'string'
                            },
                        ]
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **ReplicationSubnetGroups** *(list) --*

              A description of the replication subnet groups.

              - *(dict) --*

                - **ReplicationSubnetGroupIdentifier** *(string) --*

                  The identifier of the replication instance subnet group.

                - **ReplicationSubnetGroupDescription** *(string) --*

                  A description for the replication subnet group.

                - **VpcId** *(string) --*

                  The ID of the VPC.

                - **SubnetGroupStatus** *(string) --*

                  The status of the subnet group.

                - **Subnets** *(list) --*

                  The subnets that are in the subnet group.

                  - *(dict) --*

                    - **SubnetIdentifier** *(string) --*

                      The subnet identifier.

                    - **SubnetAvailabilityZone** *(dict) --*

                      The Availability Zone of the subnet.

                      - **Name** *(string) --*

                        The name of the availability zone.

                    - **SubnetStatus** *(string) --*

                      The status of the subnet.

            - **NextToken** *(string) --*

              A token to resume pagination.
        """


class DescribeReplicationTaskAssessmentResultsPaginator(Boto3Paginator):
    """
    Paginator for `describe_replication_task_assessment_results`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ReplicationTaskArn: str = None,
        PaginationConfig: DescribeReplicationTaskAssessmentResultsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeReplicationTaskAssessmentResultsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`DatabaseMigrationService.Client.describe_replication_task_assessment_results`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/DescribeReplicationTaskAssessmentResults>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              ReplicationTaskArn='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type ReplicationTaskArn: string
        :param ReplicationTaskArn:

          - The Amazon Resource Name (ARN) string that uniquely identifies the task. When this input
          parameter is specified the API will return only one result and ignore the values of the
          max-records and marker parameters.

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
                'BucketName': 'string',
                'ReplicationTaskAssessmentResults': [
                    {
                        'ReplicationTaskIdentifier': 'string',
                        'ReplicationTaskArn': 'string',
                        'ReplicationTaskLastAssessmentDate': datetime(2015, 1, 1),
                        'AssessmentStatus': 'string',
                        'AssessmentResultsFile': 'string',
                        'AssessmentResults': 'string',
                        'S3ObjectUrl': 'string'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **BucketName** *(string) --*

              - The Amazon S3 bucket where the task assessment report is located.

            - **ReplicationTaskAssessmentResults** *(list) --*

              The task assessment report.

              - *(dict) --*

                The task assessment report in JSON format.

                - **ReplicationTaskIdentifier** *(string) --*

                  The replication task identifier of the task on which the task assessment was run.

                - **ReplicationTaskArn** *(string) --*

                  The Amazon Resource Name (ARN) of the replication task.

                - **ReplicationTaskLastAssessmentDate** *(datetime) --*

                  The date the task assessment was completed.

                - **AssessmentStatus** *(string) --*

                  The status of the task assessment.

                - **AssessmentResultsFile** *(string) --*

                  The file containing the results of the task assessment.

                - **AssessmentResults** *(string) --*

                  The task assessment results in JSON format.

                - **S3ObjectUrl** *(string) --*

                  The URL of the S3 object containing the task assessment results.

            - **NextToken** *(string) --*

              A token to resume pagination.
        """


class DescribeReplicationTasksPaginator(Boto3Paginator):
    """
    Paginator for `describe_replication_tasks`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[DescribeReplicationTasksPaginateFiltersTypeDef] = None,
        WithoutSettings: bool = None,
        PaginationConfig: DescribeReplicationTasksPaginatePaginationConfigTypeDef = None,
    ) -> DescribeReplicationTasksPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`DatabaseMigrationService.Client.describe_replication_tasks`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/DescribeReplicationTasks>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              WithoutSettings=True|False,
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type Filters: list
        :param Filters:

          Filters applied to the describe action.

          Valid filter names: replication-task-arn | replication-task-id | migration-type |
          endpoint-arn | replication-instance-arn

          - *(dict) --*

            - **Name** *(string) --* **[REQUIRED]**

              The name of the filter.

            - **Values** *(list) --* **[REQUIRED]**

              The filter value.

              - *(string) --*

        :type WithoutSettings: boolean
        :param WithoutSettings:

          An option to set to avoid returning information about settings. Use this to reduce
          overhead when setting information is too large. To use this option, choose ``true`` ;
          otherwise, choose ``false`` (the default).

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
                'ReplicationTasks': [
                    {
                        'ReplicationTaskIdentifier': 'string',
                        'SourceEndpointArn': 'string',
                        'TargetEndpointArn': 'string',
                        'ReplicationInstanceArn': 'string',
                        'MigrationType': 'full-load'|'cdc'|'full-load-and-cdc',
                        'TableMappings': 'string',
                        'ReplicationTaskSettings': 'string',
                        'Status': 'string',
                        'LastFailureMessage': 'string',
                        'StopReason': 'string',
                        'ReplicationTaskCreationDate': datetime(2015, 1, 1),
                        'ReplicationTaskStartDate': datetime(2015, 1, 1),
                        'CdcStartPosition': 'string',
                        'CdcStopPosition': 'string',
                        'RecoveryCheckpoint': 'string',
                        'ReplicationTaskArn': 'string',
                        'ReplicationTaskStats': {
                            'FullLoadProgressPercent': 123,
                            'ElapsedTimeMillis': 123,
                            'TablesLoaded': 123,
                            'TablesLoading': 123,
                            'TablesQueued': 123,
                            'TablesErrored': 123,
                            'FreshStartDate': datetime(2015, 1, 1),
                            'StartDate': datetime(2015, 1, 1),
                            'StopDate': datetime(2015, 1, 1),
                            'FullLoadStartDate': datetime(2015, 1, 1),
                            'FullLoadFinishDate': datetime(2015, 1, 1)
                        }
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **ReplicationTasks** *(list) --*

              A description of the replication tasks.

              - *(dict) --*

                - **ReplicationTaskIdentifier** *(string) --*

                  The user-assigned replication task identifier or name.

                  Constraints:

                  * Must contain from 1 to 255 alphanumeric characters or hyphens.

                  * First character must be a letter.

                  * Cannot end with a hyphen or contain two consecutive hyphens.

                - **SourceEndpointArn** *(string) --*

                  The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.

                - **TargetEndpointArn** *(string) --*

                  The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.

                - **ReplicationInstanceArn** *(string) --*

                  The Amazon Resource Name (ARN) of the replication instance.

                - **MigrationType** *(string) --*

                  The type of migration.

                - **TableMappings** *(string) --*

                  Table mappings specified in the task.

                - **ReplicationTaskSettings** *(string) --*

                  The settings for the replication task.

                - **Status** *(string) --*

                  The status of the replication task.

                - **LastFailureMessage** *(string) --*

                  The last error (failure) message generated for the replication instance.

                - **StopReason** *(string) --*

                  The reason the replication task was stopped.

                - **ReplicationTaskCreationDate** *(datetime) --*

                  The date the replication task was created.

                - **ReplicationTaskStartDate** *(datetime) --*

                  The date the replication task is scheduled to start.

                - **CdcStartPosition** *(string) --*

                  Indicates when you want a change data capture (CDC) operation to start. Use either
                  ``CdcStartPosition`` or ``CdcStartTime`` to specify when you want the CDC
                  operation to start. Specifying both values results in an error.

                  The value can be in date, checkpoint, or LSN/SCN format.

                  Date Example: --cdc-start-position “2018-03-08T12:12:12”

                  Checkpoint Example: --cdc-start-position
                  "checkpoint:V1#27#mysql-bin-changelog.157832:1975:-1:2002:677883278264080:mysql-bin-changelog.157832:1876#0#0#*#0#93"

                  LSN Example: --cdc-start-position “mysql-bin-changelog.000024:373”

                - **CdcStopPosition** *(string) --*

                  Indicates when you want a change data capture (CDC) operation to stop. The value
                  can be either server time or commit time.

                  Server time example: --cdc-stop-position “server_time:3018-02-09T12:12:12”

                  Commit time example: --cdc-stop-position “commit_time: 3018-02-09T12:12:12 “

                - **RecoveryCheckpoint** *(string) --*

                  Indicates the last checkpoint that occurred during a change data capture (CDC)
                  operation. You can provide this value to the ``CdcStartPosition`` parameter to
                  start a CDC operation that begins at that checkpoint.

                - **ReplicationTaskArn** *(string) --*

                  The Amazon Resource Name (ARN) of the replication task.

                - **ReplicationTaskStats** *(dict) --*

                  The statistics for the task, including elapsed time, tables loaded, and table
                  errors.

                  - **FullLoadProgressPercent** *(integer) --*

                    The percent complete for the full load migration task.

                  - **ElapsedTimeMillis** *(integer) --*

                    The elapsed time of the task, in milliseconds.

                  - **TablesLoaded** *(integer) --*

                    The number of tables loaded for this task.

                  - **TablesLoading** *(integer) --*

                    The number of tables currently loading for this task.

                  - **TablesQueued** *(integer) --*

                    The number of tables queued for this task.

                  - **TablesErrored** *(integer) --*

                    The number of errors that have occurred during this task.

                  - **FreshStartDate** *(datetime) --*

                    The date the replication task was started either with a fresh start or a target
                    reload.

                  - **StartDate** *(datetime) --*

                    The date the replication task was started either with a fresh start or a resume.
                    For more information, see `StartReplicationTaskType
                    <https://docs.aws.amazon.com/dms/latest/APIReference/API_StartReplicationTask.html#DMS-StartReplicationTask-request-StartReplicationTaskType>`__
                    .

                  - **StopDate** *(datetime) --*

                    The date the replication task was stopped.

                  - **FullLoadStartDate** *(datetime) --*

                    The date the the replication task full load was started.

                  - **FullLoadFinishDate** *(datetime) --*

                    The date the replication task full load was completed.

            - **NextToken** *(string) --*

              A token to resume pagination.
        """


class DescribeSchemasPaginator(Boto3Paginator):
    """
    Paginator for `describe_schemas`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        EndpointArn: str,
        PaginationConfig: DescribeSchemasPaginatePaginationConfigTypeDef = None,
    ) -> DescribeSchemasPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`DatabaseMigrationService.Client.describe_schemas`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/DescribeSchemas>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              EndpointArn='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type EndpointArn: string
        :param EndpointArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.

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
                'Schemas': [
                    'string',
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **Schemas** *(list) --*

              The described schema.

              - *(string) --*

            - **NextToken** *(string) --*

              A token to resume pagination.
        """


class DescribeTableStatisticsPaginator(Boto3Paginator):
    """
    Paginator for `describe_table_statistics`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ReplicationTaskArn: str,
        Filters: List[DescribeTableStatisticsPaginateFiltersTypeDef] = None,
        PaginationConfig: DescribeTableStatisticsPaginatePaginationConfigTypeDef = None,
    ) -> DescribeTableStatisticsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`DatabaseMigrationService.Client.describe_table_statistics`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/DescribeTableStatistics>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              ReplicationTaskArn='string',
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type ReplicationTaskArn: string
        :param ReplicationTaskArn: **[REQUIRED]**

          The Amazon Resource Name (ARN) of the replication task.

        :type Filters: list
        :param Filters:

          Filters applied to the describe table statistics action.

          Valid filter names: schema-name | table-name | table-state

          A combination of filters creates an AND condition where each record matches all specified
          filters.

          - *(dict) --*

            - **Name** *(string) --* **[REQUIRED]**

              The name of the filter.

            - **Values** *(list) --* **[REQUIRED]**

              The filter value.

              - *(string) --*

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
                'ReplicationTaskArn': 'string',
                'TableStatistics': [
                    {
                        'SchemaName': 'string',
                        'TableName': 'string',
                        'Inserts': 123,
                        'Deletes': 123,
                        'Updates': 123,
                        'Ddls': 123,
                        'FullLoadRows': 123,
                        'FullLoadCondtnlChkFailedRows': 123,
                        'FullLoadErrorRows': 123,
                        'LastUpdateTime': datetime(2015, 1, 1),
                        'TableState': 'string',
                        'ValidationPendingRecords': 123,
                        'ValidationFailedRecords': 123,
                        'ValidationSuspendedRecords': 123,
                        'ValidationState': 'string',
                        'ValidationStateDetails': 'string'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **ReplicationTaskArn** *(string) --*

              The Amazon Resource Name (ARN) of the replication task.

            - **TableStatistics** *(list) --*

              The table statistics.

              - *(dict) --*

                - **SchemaName** *(string) --*

                  The schema name.

                - **TableName** *(string) --*

                  The name of the table.

                - **Inserts** *(integer) --*

                  The number of insert actions performed on a table.

                - **Deletes** *(integer) --*

                  The number of delete actions performed on a table.

                - **Updates** *(integer) --*

                  The number of update actions performed on a table.

                - **Ddls** *(integer) --*

                  The Data Definition Language (DDL) used to build and modify the structure of your
                  tables.

                - **FullLoadRows** *(integer) --*

                  The number of rows added during the Full Load operation.

                - **FullLoadCondtnlChkFailedRows** *(integer) --*

                  The number of rows that failed conditional checks during the Full Load operation
                  (valid only for DynamoDB as a target migrations).

                - **FullLoadErrorRows** *(integer) --*

                  The number of rows that failed to load during the Full Load operation (valid only
                  for DynamoDB as a target migrations).

                - **LastUpdateTime** *(datetime) --*

                  The last time the table was updated.

                - **TableState** *(string) --*

                  The state of the tables described.

                  Valid states: Table does not exist | Before load | Full load
                  | Table completed |
                  Table cancelled | Table error | Table all | Table updates
                  | Table is being
                  reloaded

                - **ValidationPendingRecords** *(integer) --*

                  The number of records that have yet to be validated.

                - **ValidationFailedRecords** *(integer) --*

                  The number of records that failed validation.

                - **ValidationSuspendedRecords** *(integer) --*

                  The number of records that could not be validated.

                - **ValidationState** *(string) --*

                  The validation state of the table.

                  The parameter can have the following values

                  * Not enabled—Validation is not enabled for the table in the migration task.

                  * Pending records—Some records in the table are waiting for validation.

                  * Mismatched records—Some records in the table do not match between the source and
                  target.

                  * Suspended records—Some records in the table could not be validated.

                  * No primary key—The table could not be validated because it had no primary key.

                  * Table error—The table was not validated because it was in an error state and
                  some data was not migrated.

                  * Validated—All rows in the table were validated. If the table is updated, the
                  status can change from Validated.

                  * Error—The table could not be validated because of an unexpected error.

                - **ValidationStateDetails** *(string) --*

                  Additional details about the state of validation.

            - **NextToken** *(string) --*

              A token to resume pagination.
        """
