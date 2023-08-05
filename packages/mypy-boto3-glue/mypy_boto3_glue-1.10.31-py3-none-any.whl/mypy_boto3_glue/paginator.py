"Main interface for glue service Paginators"
from __future__ import annotations

from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_glue.type_defs import (
    GetClassifiersPaginatePaginationConfigTypeDef,
    GetClassifiersPaginateResponseTypeDef,
    GetConnectionsPaginateFilterTypeDef,
    GetConnectionsPaginatePaginationConfigTypeDef,
    GetConnectionsPaginateResponseTypeDef,
    GetCrawlerMetricsPaginatePaginationConfigTypeDef,
    GetCrawlerMetricsPaginateResponseTypeDef,
    GetCrawlersPaginatePaginationConfigTypeDef,
    GetCrawlersPaginateResponseTypeDef,
    GetDatabasesPaginatePaginationConfigTypeDef,
    GetDatabasesPaginateResponseTypeDef,
    GetDevEndpointsPaginatePaginationConfigTypeDef,
    GetDevEndpointsPaginateResponseTypeDef,
    GetJobRunsPaginatePaginationConfigTypeDef,
    GetJobRunsPaginateResponseTypeDef,
    GetJobsPaginatePaginationConfigTypeDef,
    GetJobsPaginateResponseTypeDef,
    GetPartitionsPaginatePaginationConfigTypeDef,
    GetPartitionsPaginateResponseTypeDef,
    GetPartitionsPaginateSegmentTypeDef,
    GetSecurityConfigurationsPaginatePaginationConfigTypeDef,
    GetSecurityConfigurationsPaginateResponseTypeDef,
    GetTableVersionsPaginatePaginationConfigTypeDef,
    GetTableVersionsPaginateResponseTypeDef,
    GetTablesPaginatePaginationConfigTypeDef,
    GetTablesPaginateResponseTypeDef,
    GetTriggersPaginatePaginationConfigTypeDef,
    GetTriggersPaginateResponseTypeDef,
    GetUserDefinedFunctionsPaginatePaginationConfigTypeDef,
    GetUserDefinedFunctionsPaginateResponseTypeDef,
)


__all__ = (
    "GetClassifiersPaginator",
    "GetConnectionsPaginator",
    "GetCrawlerMetricsPaginator",
    "GetCrawlersPaginator",
    "GetDatabasesPaginator",
    "GetDevEndpointsPaginator",
    "GetJobRunsPaginator",
    "GetJobsPaginator",
    "GetPartitionsPaginator",
    "GetSecurityConfigurationsPaginator",
    "GetTableVersionsPaginator",
    "GetTablesPaginator",
    "GetTriggersPaginator",
    "GetUserDefinedFunctionsPaginator",
)


class GetClassifiersPaginator(Boto3Paginator):
    """
    Paginator for `get_classifiers`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: GetClassifiersPaginatePaginationConfigTypeDef = None
    ) -> GetClassifiersPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`Glue.Client.get_classifiers`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetClassifiers>`_

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
                'Classifiers': [
                    {
                        'GrokClassifier': {
                            'Name': 'string',
                            'Classification': 'string',
                            'CreationTime': datetime(2015, 1, 1),
                            'LastUpdated': datetime(2015, 1, 1),
                            'Version': 123,
                            'GrokPattern': 'string',
                            'CustomPatterns': 'string'
                        },
                        'XMLClassifier': {
                            'Name': 'string',
                            'Classification': 'string',
                            'CreationTime': datetime(2015, 1, 1),
                            'LastUpdated': datetime(2015, 1, 1),
                            'Version': 123,
                            'RowTag': 'string'
                        },
                        'JsonClassifier': {
                            'Name': 'string',
                            'CreationTime': datetime(2015, 1, 1),
                            'LastUpdated': datetime(2015, 1, 1),
                            'Version': 123,
                            'JsonPath': 'string'
                        },
                        'CsvClassifier': {
                            'Name': 'string',
                            'CreationTime': datetime(2015, 1, 1),
                            'LastUpdated': datetime(2015, 1, 1),
                            'Version': 123,
                            'Delimiter': 'string',
                            'QuoteSymbol': 'string',
                            'ContainsHeader': 'UNKNOWN'|'PRESENT'|'ABSENT',
                            'Header': [
                                'string',
                            ],
                            'DisableValueTrimming': True|False,
                            'AllowSingleColumn': True|False
                        }
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **Classifiers** *(list) --*

              The requested list of classifier objects.

              - *(dict) --*

                Classifiers are triggered during a crawl task. A classifier checks whether a given
                file is in a format it can handle. If it is, the classifier creates a schema in the
                form of a ``StructType`` object that matches that data format.

                You can use the standard classifiers that AWS Glue provides, or you can write your
                own classifiers to best categorize your data sources and specify the appropriate
                schemas to use for them. A classifier can be a ``grok`` classifier, an ``XML``
                classifier, a ``JSON`` classifier, or a custom ``CSV`` classifier, as specified in
                one of the fields in the ``Classifier`` object.

                - **GrokClassifier** *(dict) --*

                  A classifier that uses ``grok`` .

                  - **Name** *(string) --*

                    The name of the classifier.

                  - **Classification** *(string) --*

                    An identifier of the data format that the classifier matches, such as Twitter,
                    JSON, Omniture logs, and so on.

                  - **CreationTime** *(datetime) --*

                    The time that this classifier was registered.

                  - **LastUpdated** *(datetime) --*

                    The time that this classifier was last updated.

                  - **Version** *(integer) --*

                    The version of this classifier.

                  - **GrokPattern** *(string) --*

                    The grok pattern applied to a data store by this classifier. For more
                    information, see built-in patterns in `Writing Custom Classifiers
                    <http://docs.aws.amazon.com/glue/latest/dg/custom-classifier.html>`__ .

                  - **CustomPatterns** *(string) --*

                    Optional custom grok patterns defined by this classifier. For more information,
                    see custom patterns in `Writing Custom Classifiers
                    <http://docs.aws.amazon.com/glue/latest/dg/custom-classifier.html>`__ .

                - **XMLClassifier** *(dict) --*

                  A classifier for XML content.

                  - **Name** *(string) --*

                    The name of the classifier.

                  - **Classification** *(string) --*

                    An identifier of the data format that the classifier matches.

                  - **CreationTime** *(datetime) --*

                    The time that this classifier was registered.

                  - **LastUpdated** *(datetime) --*

                    The time that this classifier was last updated.

                  - **Version** *(integer) --*

                    The version of this classifier.

                  - **RowTag** *(string) --*

                    The XML tag designating the element that contains each record in an XML document
                    being parsed. This can't identify a self-closing element (closed by ``/>`` ). An
                    empty row element that contains only attributes can be parsed as long as it ends
                    with a closing tag (for example, ``<row item_a="A" item_b=
                        "B"></row>`` is okay,
                    but ``<row item_a="A" item_b="B" />`` is not).

                - **JsonClassifier** *(dict) --*

                  A classifier for JSON content.

                  - **Name** *(string) --*

                    The name of the classifier.

                  - **CreationTime** *(datetime) --*

                    The time that this classifier was registered.

                  - **LastUpdated** *(datetime) --*

                    The time that this classifier was last updated.

                  - **Version** *(integer) --*

                    The version of this classifier.

                  - **JsonPath** *(string) --*

                    A ``JsonPath`` string defining the JSON data for the classifier to classify. AWS
                    Glue supports a subset of ``JsonPath`` , as described in `Writing JsonPath
                    Custom Classifiers
                    <https://docs.aws.amazon.com/glue/latest/dg/custom-classifier.html#custom-classifier-json>`__
                    .

                - **CsvClassifier** *(dict) --*

                  A classifier for comma-separated values (CSV).

                  - **Name** *(string) --*

                    The name of the classifier.

                  - **CreationTime** *(datetime) --*

                    The time that this classifier was registered.

                  - **LastUpdated** *(datetime) --*

                    The time that this classifier was last updated.

                  - **Version** *(integer) --*

                    The version of this classifier.

                  - **Delimiter** *(string) --*

                    A custom symbol to denote what separates each column entry in the row.

                  - **QuoteSymbol** *(string) --*

                    A custom symbol to denote what combines content into a single column value. It
                    must be different from the column delimiter.

                  - **ContainsHeader** *(string) --*

                    Indicates whether the CSV file contains a header.

                  - **Header** *(list) --*

                    A list of strings representing column names.

                    - *(string) --*

                  - **DisableValueTrimming** *(boolean) --*

                    Specifies not to trim values before identifying the type of column values. The
                    default value is ``true`` .

                  - **AllowSingleColumn** *(boolean) --*

                    Enables the processing of files that contain only one column.
        """


class GetConnectionsPaginator(Boto3Paginator):
    """
    Paginator for `get_connections`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        CatalogId: str = None,
        Filter: GetConnectionsPaginateFilterTypeDef = None,
        HidePassword: bool = None,
        PaginationConfig: GetConnectionsPaginatePaginationConfigTypeDef = None,
    ) -> GetConnectionsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`Glue.Client.get_connections`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetConnections>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              CatalogId='string',
              Filter={
                  'MatchCriteria': [
                      'string',
                  ],
                  'ConnectionType': 'JDBC'|'SFTP'
              },
              HidePassword=True|False,
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type CatalogId: string
        :param CatalogId:

          The ID of the Data Catalog in which the connections reside. If none is provided, the AWS
          account ID is used by default.

        :type Filter: dict
        :param Filter:

          A filter that controls which connections are returned.

          - **MatchCriteria** *(list) --*

            A criteria string that must match the criteria recorded in the connection definition for
            that connection definition to be returned.

            - *(string) --*

          - **ConnectionType** *(string) --*

            The type of connections to return. Currently, only JDBC is supported; SFTP is not
            supported.

        :type HidePassword: boolean
        :param HidePassword:

          Allows you to retrieve the connection metadata without returning the password. For
          instance, the AWS Glue console uses this flag to retrieve the connection, and does not
          display the password. Set this parameter when the caller might not have permission to use
          the AWS KMS key to decrypt the password, but it does have permission to access the rest of
          the connection properties.

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
                'ConnectionList': [
                    {
                        'Name': 'string',
                        'Description': 'string',
                        'ConnectionType': 'JDBC'|'SFTP',
                        'MatchCriteria': [
                            'string',
                        ],
                        'ConnectionProperties': {
                            'string': 'string'
                        },
                        'PhysicalConnectionRequirements': {
                            'SubnetId': 'string',
                            'SecurityGroupIdList': [
                                'string',
                            ],
                            'AvailabilityZone': 'string'
                        },
                        'CreationTime': datetime(2015, 1, 1),
                        'LastUpdatedTime': datetime(2015, 1, 1),
                        'LastUpdatedBy': 'string'
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **ConnectionList** *(list) --*

              A list of requested connection definitions.

              - *(dict) --*

                Defines a connection to a data source.

                - **Name** *(string) --*

                  The name of the connection definition.

                - **Description** *(string) --*

                  The description of the connection.

                - **ConnectionType** *(string) --*

                  The type of the connection. Currently, only JDBC is supported; SFTP is not
                  supported.

                - **MatchCriteria** *(list) --*

                  A list of criteria that can be used in selecting this connection.

                  - *(string) --*

                - **ConnectionProperties** *(dict) --*

                  These key-value pairs define parameters for the connection:

                  * ``HOST`` - The host URI: either the fully qualified domain name (FQDN) or the
                  IPv4 address of the database host.

                  * ``PORT`` - The port number, between 1024 and 65535, of the port on which the
                  database host is listening for database connections.

                  * ``USER_NAME`` - The name under which to log in to the database. The value string
                  for ``USER_NAME`` is "``USERNAME`` ".

                  * ``PASSWORD`` - A password, if one is used, for the user name.

                  * ``ENCRYPTED_PASSWORD`` - When you enable connection password protection by
                  setting ``ConnectionPasswordEncryption`` in the Data Catalog encryption settings,
                  this field stores the encrypted password.

                  * ``JDBC_DRIVER_JAR_URI`` - The Amazon Simple Storage Service (Amazon S3) path of
                  the JAR file that contains the JDBC driver to use.

                  * ``JDBC_DRIVER_CLASS_NAME`` - The class name of the JDBC driver to use.

                  * ``JDBC_ENGINE`` - The name of the JDBC engine to use.

                  * ``JDBC_ENGINE_VERSION`` - The version of the JDBC engine to use.

                  * ``CONFIG_FILES`` - (Reserved for future use.)

                  * ``INSTANCE_ID`` - The instance ID to use.

                  * ``JDBC_CONNECTION_URL`` - The URL for the JDBC connection.

                  * ``JDBC_ENFORCE_SSL`` - A Boolean string (true, false) specifying whether Secure
                  Sockets Layer (SSL) with hostname matching is enforced for the JDBC connection on
                  the client. The default is false.

                  * ``CUSTOM_JDBC_CERT`` - An Amazon S3 location specifying the customer's root
                  certificate. AWS Glue uses this root certificate to validate the customer’s
                  certificate when connecting to the customer database. AWS Glue only handles X.509
                  certificates. The certificate provided must be DER-encoded and supplied in Base64
                  encoding PEM format.

                  * ``SKIP_CUSTOM_JDBC_CERT_VALIDATION`` - By default, this is ``false`` . AWS Glue
                  validates the Signature algorithm and Subject Public Key Algorithm for the
                  customer certificate. The only permitted algorithms for the Signature algorithm
                  are SHA256withRSA, SHA384withRSA or SHA512withRSA. For the Subject Public Key
                  Algorithm, the key length must be at least 2048. You can set the value of this
                  property to ``true`` to skip AWS Glue’s validation of the customer certificate.

                  * ``CUSTOM_JDBC_CERT_STRING`` - A custom JDBC certificate string which is used for
                  domain match or distinguished name match to prevent a man-in-the-middle attack. In
                  Oracle database, this is used as the ``SSL_SERVER_CERT_DN`` ; in Microsoft SQL
                  Server, this is used as the ``hostNameInCertificate`` .

                  - *(string) --*

                    - *(string) --*

                - **PhysicalConnectionRequirements** *(dict) --*

                  A map of physical connection requirements, such as virtual private cloud (VPC) and
                  ``SecurityGroup`` , that are needed to make this connection successfully.

                  - **SubnetId** *(string) --*

                    The subnet ID used by the connection.

                  - **SecurityGroupIdList** *(list) --*

                    The security group ID list used by the connection.

                    - *(string) --*

                  - **AvailabilityZone** *(string) --*

                    The connection's Availability Zone. This field is redundant because the
                    specified subnet implies the Availability Zone to be used. Currently the field
                    must be populated, but it will be deprecated in the future.

                - **CreationTime** *(datetime) --*

                  The time that this connection definition was created.

                - **LastUpdatedTime** *(datetime) --*

                  The last time that this connection definition was updated.

                - **LastUpdatedBy** *(string) --*

                  The user, group, or role that last updated this connection definition.
        """


class GetCrawlerMetricsPaginator(Boto3Paginator):
    """
    Paginator for `get_crawler_metrics`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        CrawlerNameList: List[str] = None,
        PaginationConfig: GetCrawlerMetricsPaginatePaginationConfigTypeDef = None,
    ) -> GetCrawlerMetricsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`Glue.Client.get_crawler_metrics`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetCrawlerMetrics>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              CrawlerNameList=[
                  'string',
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type CrawlerNameList: list
        :param CrawlerNameList:

          A list of the names of crawlers about which to retrieve metrics.

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
                'CrawlerMetricsList': [
                    {
                        'CrawlerName': 'string',
                        'TimeLeftSeconds': 123.0,
                        'StillEstimating': True|False,
                        'LastRuntimeSeconds': 123.0,
                        'MedianRuntimeSeconds': 123.0,
                        'TablesCreated': 123,
                        'TablesUpdated': 123,
                        'TablesDeleted': 123
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **CrawlerMetricsList** *(list) --*

              A list of metrics for the specified crawler.

              - *(dict) --*

                Metrics for a specified crawler.

                - **CrawlerName** *(string) --*

                  The name of the crawler.

                - **TimeLeftSeconds** *(float) --*

                  The estimated time left to complete a running crawl.

                - **StillEstimating** *(boolean) --*

                  True if the crawler is still estimating how long it will take to complete this
                  run.

                - **LastRuntimeSeconds** *(float) --*

                  The duration of the crawler's most recent run, in seconds.

                - **MedianRuntimeSeconds** *(float) --*

                  The median duration of this crawler's runs, in seconds.

                - **TablesCreated** *(integer) --*

                  The number of tables created by this crawler.

                - **TablesUpdated** *(integer) --*

                  The number of tables updated by this crawler.

                - **TablesDeleted** *(integer) --*

                  The number of tables deleted by this crawler.
        """


class GetCrawlersPaginator(Boto3Paginator):
    """
    Paginator for `get_crawlers`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: GetCrawlersPaginatePaginationConfigTypeDef = None
    ) -> GetCrawlersPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`Glue.Client.get_crawlers`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetCrawlers>`_

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
                'Crawlers': [
                    {
                        'Name': 'string',
                        'Role': 'string',
                        'Targets': {
                            'S3Targets': [
                                {
                                    'Path': 'string',
                                    'Exclusions': [
                                        'string',
                                    ]
                                },
                            ],
                            'JdbcTargets': [
                                {
                                    'ConnectionName': 'string',
                                    'Path': 'string',
                                    'Exclusions': [
                                        'string',
                                    ]
                                },
                            ],
                            'DynamoDBTargets': [
                                {
                                    'Path': 'string'
                                },
                            ],
                            'CatalogTargets': [
                                {
                                    'DatabaseName': 'string',
                                    'Tables': [
                                        'string',
                                    ]
                                },
                            ]
                        },
                        'DatabaseName': 'string',
                        'Description': 'string',
                        'Classifiers': [
                            'string',
                        ],
                        'SchemaChangePolicy': {
                            'UpdateBehavior': 'LOG'|'UPDATE_IN_DATABASE',
                            'DeleteBehavior': 'LOG'|'DELETE_FROM_DATABASE'|'DEPRECATE_IN_DATABASE'
                        },
                        'State': 'READY'|'RUNNING'|'STOPPING',
                        'TablePrefix': 'string',
                        'Schedule': {
                            'ScheduleExpression': 'string',
                            'State': 'SCHEDULED'|'NOT_SCHEDULED'|'TRANSITIONING'
                        },
                        'CrawlElapsedTime': 123,
                        'CreationTime': datetime(2015, 1, 1),
                        'LastUpdated': datetime(2015, 1, 1),
                        'LastCrawl': {
                            'Status': 'SUCCEEDED'|'CANCELLED'|'FAILED',
                            'ErrorMessage': 'string',
                            'LogGroup': 'string',
                            'LogStream': 'string',
                            'MessagePrefix': 'string',
                            'StartTime': datetime(2015, 1, 1)
                        },
                        'Version': 123,
                        'Configuration': 'string',
                        'CrawlerSecurityConfiguration': 'string'
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **Crawlers** *(list) --*

              A list of crawler metadata.

              - *(dict) --*

                Specifies a crawler program that examines a data source and uses classifiers to try
                to determine its schema. If successful, the crawler records metadata concerning the
                data source in the AWS Glue Data Catalog.

                - **Name** *(string) --*

                  The name of the crawler.

                - **Role** *(string) --*

                  The Amazon Resource Name (ARN) of an IAM role that's used to access customer
                  resources, such as Amazon Simple Storage Service (Amazon S3) data.

                - **Targets** *(dict) --*

                  A collection of targets to crawl.

                  - **S3Targets** *(list) --*

                    Specifies Amazon Simple Storage Service (Amazon S3) targets.

                    - *(dict) --*

                      Specifies a data store in Amazon Simple Storage Service (Amazon S3).

                      - **Path** *(string) --*

                        The path to the Amazon S3 target.

                      - **Exclusions** *(list) --*

                        A list of glob patterns used to exclude from the crawl. For more
                        information, see `Catalog Tables with a Crawler
                        <http://docs.aws.amazon.com/glue/latest/dg/add-crawler.html>`__ .

                        - *(string) --*

                  - **JdbcTargets** *(list) --*

                    Specifies JDBC targets.

                    - *(dict) --*

                      Specifies a JDBC data store to crawl.

                      - **ConnectionName** *(string) --*

                        The name of the connection to use to connect to the JDBC target.

                      - **Path** *(string) --*

                        The path of the JDBC target.

                      - **Exclusions** *(list) --*

                        A list of glob patterns used to exclude from the crawl. For more
                        information, see `Catalog Tables with a Crawler
                        <http://docs.aws.amazon.com/glue/latest/dg/add-crawler.html>`__ .

                        - *(string) --*

                  - **DynamoDBTargets** *(list) --*

                    Specifies Amazon DynamoDB targets.

                    - *(dict) --*

                      Specifies an Amazon DynamoDB table to crawl.

                      - **Path** *(string) --*

                        The name of the DynamoDB table to crawl.

                  - **CatalogTargets** *(list) --*

                    Specifies AWS Glue Data Catalog targets.

                    - *(dict) --*

                      Specifies an AWS Glue Data Catalog target.

                      - **DatabaseName** *(string) --*

                        The name of the database to be synchronized.

                      - **Tables** *(list) --*

                        A list of the tables to be synchronized.

                        - *(string) --*

                - **DatabaseName** *(string) --*

                  The name of the database in which the crawler's output is stored.

                - **Description** *(string) --*

                  A description of the crawler.

                - **Classifiers** *(list) --*

                  A list of UTF-8 strings that specify the custom classifiers that are associated
                  with the crawler.

                  - *(string) --*

                - **SchemaChangePolicy** *(dict) --*

                  The policy that specifies update and delete behaviors for the crawler.

                  - **UpdateBehavior** *(string) --*

                    The update behavior when the crawler finds a changed schema.

                  - **DeleteBehavior** *(string) --*

                    The deletion behavior when the crawler finds a deleted object.

                - **State** *(string) --*

                  Indicates whether the crawler is running, or whether a run is pending.

                - **TablePrefix** *(string) --*

                  The prefix added to the names of tables that are created.

                - **Schedule** *(dict) --*

                  For scheduled crawlers, the schedule when the crawler runs.

                  - **ScheduleExpression** *(string) --*

                    A ``cron`` expression used to specify the schedule. For more information, see
                    `Time-Based Schedules for Jobs and Crawlers
                    <http://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html>`__
                    . For example, to run something every day at 12:15 UTC, specify ``cron(15 12 * *
                    ? *)`` .

                  - **State** *(string) --*

                    The state of the schedule.

                - **CrawlElapsedTime** *(integer) --*

                  If the crawler is running, contains the total time elapsed since the last crawl
                  began.

                - **CreationTime** *(datetime) --*

                  The time that the crawler was created.

                - **LastUpdated** *(datetime) --*

                  The time that the crawler was last updated.

                - **LastCrawl** *(dict) --*

                  The status of the last crawl, and potentially error information if an error
                  occurred.

                  - **Status** *(string) --*

                    Status of the last crawl.

                  - **ErrorMessage** *(string) --*

                    If an error occurred, the error information about the last crawl.

                  - **LogGroup** *(string) --*

                    The log group for the last crawl.

                  - **LogStream** *(string) --*

                    The log stream for the last crawl.

                  - **MessagePrefix** *(string) --*

                    The prefix for a message about this crawl.

                  - **StartTime** *(datetime) --*

                    The time at which the crawl started.

                - **Version** *(integer) --*

                  The version of the crawler.

                - **Configuration** *(string) --*

                  Crawler configuration information. This versioned JSON string allows users to
                  specify aspects of a crawler's behavior. For more information, see `Configuring a
                  Crawler <http://docs.aws.amazon.com/glue/latest/dg/crawler-configuration.html>`__
                  .

                - **CrawlerSecurityConfiguration** *(string) --*

                  The name of the ``SecurityConfiguration`` structure to be used by this crawler.
        """


class GetDatabasesPaginator(Boto3Paginator):
    """
    Paginator for `get_databases`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        CatalogId: str = None,
        PaginationConfig: GetDatabasesPaginatePaginationConfigTypeDef = None,
    ) -> GetDatabasesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`Glue.Client.get_databases`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetDatabases>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              CatalogId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type CatalogId: string
        :param CatalogId:

          The ID of the Data Catalog from which to retrieve ``Databases`` . If none is provided, the
          AWS account ID is used by default.

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
                'DatabaseList': [
                    {
                        'Name': 'string',
                        'Description': 'string',
                        'LocationUri': 'string',
                        'Parameters': {
                            'string': 'string'
                        },
                        'CreateTime': datetime(2015, 1, 1),
                        'CreateTableDefaultPermissions': [
                            {
                                'Principal': {
                                    'DataLakePrincipalIdentifier': 'string'
                                },
                                'Permissions': [
                                    'ALL'|'SELECT'|'ALTER'|'DROP'|'DELETE'|'INSERT'
                                    |'CREATE_DATABASE'|'CREATE_TABLE'|'DATA_LOCATION_ACCESS',
                                ]
                            },
                        ]
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **DatabaseList** *(list) --*

              A list of ``Database`` objects from the specified catalog.

              - *(dict) --*

                The ``Database`` object represents a logical grouping of tables that might reside in
                a Hive metastore or an RDBMS.

                - **Name** *(string) --*

                  The name of the database. For Hive compatibility, this is folded to lowercase when
                  it is stored.

                - **Description** *(string) --*

                  A description of the database.

                - **LocationUri** *(string) --*

                  The location of the database (for example, an HDFS path).

                - **Parameters** *(dict) --*

                  These key-value pairs define parameters and properties of the database.

                  - *(string) --*

                    - *(string) --*

                - **CreateTime** *(datetime) --*

                  The time at which the metadata database was created in the catalog.

                - **CreateTableDefaultPermissions** *(list) --*

                  Creates a set of default permissions on the table for principals.

                  - *(dict) --*

                    Permissions granted to a principal.

                    - **Principal** *(dict) --*

                      The principal who is granted permissions.

                      - **DataLakePrincipalIdentifier** *(string) --*

                        An identifier for the AWS Lake Formation principal.

                    - **Permissions** *(list) --*

                      The permissions that are granted to the principal.

                      - *(string) --*
        """


class GetDevEndpointsPaginator(Boto3Paginator):
    """
    Paginator for `get_dev_endpoints`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: GetDevEndpointsPaginatePaginationConfigTypeDef = None
    ) -> GetDevEndpointsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`Glue.Client.get_dev_endpoints`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetDevEndpoints>`_

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
                'DevEndpoints': [
                    {
                        'EndpointName': 'string',
                        'RoleArn': 'string',
                        'SecurityGroupIds': [
                            'string',
                        ],
                        'SubnetId': 'string',
                        'YarnEndpointAddress': 'string',
                        'PrivateAddress': 'string',
                        'ZeppelinRemoteSparkInterpreterPort': 123,
                        'PublicAddress': 'string',
                        'Status': 'string',
                        'WorkerType': 'Standard'|'G.1X'|'G.2X',
                        'GlueVersion': 'string',
                        'NumberOfWorkers': 123,
                        'NumberOfNodes': 123,
                        'AvailabilityZone': 'string',
                        'VpcId': 'string',
                        'ExtraPythonLibsS3Path': 'string',
                        'ExtraJarsS3Path': 'string',
                        'FailureReason': 'string',
                        'LastUpdateStatus': 'string',
                        'CreatedTimestamp': datetime(2015, 1, 1),
                        'LastModifiedTimestamp': datetime(2015, 1, 1),
                        'PublicKey': 'string',
                        'PublicKeys': [
                            'string',
                        ],
                        'SecurityConfiguration': 'string',
                        'Arguments': {
                            'string': 'string'
                        }
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **DevEndpoints** *(list) --*

              A list of ``DevEndpoint`` definitions.

              - *(dict) --*

                A development endpoint where a developer can remotely debug extract, transform, and
                load (ETL) scripts.

                - **EndpointName** *(string) --*

                  The name of the ``DevEndpoint`` .

                - **RoleArn** *(string) --*

                  The Amazon Resource Name (ARN) of the IAM role used in this ``DevEndpoint`` .

                - **SecurityGroupIds** *(list) --*

                  A list of security group identifiers used in this ``DevEndpoint`` .

                  - *(string) --*

                - **SubnetId** *(string) --*

                  The subnet ID for this ``DevEndpoint`` .

                - **YarnEndpointAddress** *(string) --*

                  The YARN endpoint address used by this ``DevEndpoint`` .

                - **PrivateAddress** *(string) --*

                  A private IP address to access the ``DevEndpoint`` within a VPC if the
                  ``DevEndpoint`` is created within one. The ``PrivateAddress`` field is present
                  only when you create the ``DevEndpoint`` within your VPC.

                - **ZeppelinRemoteSparkInterpreterPort** *(integer) --*

                  The Apache Zeppelin port for the remote Apache Spark interpreter.

                - **PublicAddress** *(string) --*

                  The public IP address used by this ``DevEndpoint`` . The ``PublicAddress`` field
                  is present only when you create a non-virtual private cloud (VPC) ``DevEndpoint``
                  .

                - **Status** *(string) --*

                  The current status of this ``DevEndpoint`` .

                - **WorkerType** *(string) --*

                  The type of predefined worker that is allocated to the development endpoint.
                  Accepts a value of Standard, G.1X, or G.2X.

                  * For the ``Standard`` worker type, each worker provides 4 vCPU, 16 GB of memory
                  and a 50GB disk, and 2 executors per worker.

                  * For the ``G.1X`` worker type, each worker maps to 1 DPU (4 vCPU, 16 GB of
                  memory, 64 GB disk), and provides 1 executor per worker. We recommend this worker
                  type for memory-intensive jobs.

                  * For the ``G.2X`` worker type, each worker maps to 2 DPU (8 vCPU, 32 GB of
                  memory, 128 GB disk), and provides 1 executor per worker. We recommend this worker
                  type for memory-intensive jobs.

                  Known issue: when a development endpoint is created with the ``G.2X``
                  ``WorkerType`` configuration, the Spark drivers for the development endpoint will
                  run on 4 vCPU, 16 GB of memory, and a 64 GB disk.

                - **GlueVersion** *(string) --*

                  Glue version determines the versions of Apache Spark and Python that AWS Glue
                  supports. The Python version indicates the version supported for running your ETL
                  scripts on development endpoints.

                  For more information about the available AWS Glue versions and corresponding Spark
                  and Python versions, see `Glue version
                  <https://docs.aws.amazon.com/glue/latest/dg/add-job.html>`__ in the developer
                  guide.

                  Development endpoints that are created without specifying a Glue version default
                  to Glue 0.9.

                  You can specify a version of Python support for development endpoints by using the
                  ``Arguments`` parameter in the ``CreateDevEndpoint`` or ``UpdateDevEndpoint``
                  APIs. If no arguments are provided, the version defaults to Python 2.

                - **NumberOfWorkers** *(integer) --*

                  The number of workers of a defined ``workerType`` that are allocated to the
                  development endpoint.

                  The maximum number of workers you can define are 299 for ``G.1X`` , and 149 for
                  ``G.2X`` .

                - **NumberOfNodes** *(integer) --*

                  The number of AWS Glue Data Processing Units (DPUs) allocated to this
                  ``DevEndpoint`` .

                - **AvailabilityZone** *(string) --*

                  The AWS Availability Zone where this ``DevEndpoint`` is located.

                - **VpcId** *(string) --*

                  The ID of the virtual private cloud (VPC) used by this ``DevEndpoint`` .

                - **ExtraPythonLibsS3Path** *(string) --*

                  The paths to one or more Python libraries in an Amazon S3 bucket that should be
                  loaded in your ``DevEndpoint`` . Multiple values must be complete paths separated
                  by a comma.

                  .. note::

                    You can only use pure Python libraries with a ``DevEndpoint`` . Libraries that
                    rely on C extensions, such as the `pandas <http://pandas.pydata.org/>`__ Python
                    data analysis library, are not currently supported.

                - **ExtraJarsS3Path** *(string) --*

                  The path to one or more Java ``.jar`` files in an S3 bucket that should be loaded
                  in your ``DevEndpoint`` .

                  .. note::

                    You can only use pure Java/Scala libraries with a ``DevEndpoint`` .

                - **FailureReason** *(string) --*

                  The reason for a current failure in this ``DevEndpoint`` .

                - **LastUpdateStatus** *(string) --*

                  The status of the last update.

                - **CreatedTimestamp** *(datetime) --*

                  The point in time at which this DevEndpoint was created.

                - **LastModifiedTimestamp** *(datetime) --*

                  The point in time at which this ``DevEndpoint`` was last modified.

                - **PublicKey** *(string) --*

                  The public key to be used by this ``DevEndpoint`` for authentication. This
                  attribute is provided for backward compatibility because the recommended attribute
                  to use is public keys.

                - **PublicKeys** *(list) --*

                  A list of public keys to be used by the ``DevEndpoints`` for authentication. Using
                  this attribute is preferred over a single public key because the public keys allow
                  you to have a different private key per client.

                  .. note::

                    If you previously created an endpoint with a public key, you must remove that
                    key to be able to set a list of public keys. Call the ``UpdateDevEndpoint`` API
                    operation with the public key content in the ``deletePublicKeys`` attribute, and
                    the list of new keys in the ``addPublicKeys`` attribute.

                  - *(string) --*

                - **SecurityConfiguration** *(string) --*

                  The name of the ``SecurityConfiguration`` structure to be used with this
                  ``DevEndpoint`` .

                - **Arguments** *(dict) --*

                  A map of arguments used to configure the ``DevEndpoint`` .

                  Valid arguments are:

                  * ``"--enable-glue-datacatalog": ""``

                  * ``"GLUE_PYTHON_VERSION": "3"``

                  * ``"GLUE_PYTHON_VERSION": "2"``

                  You can specify a version of Python support for development endpoints by using the
                  ``Arguments`` parameter in the ``CreateDevEndpoint`` or ``UpdateDevEndpoint``
                  APIs. If no arguments are provided, the version defaults to Python 2.

                  - *(string) --*

                    - *(string) --*
        """


class GetJobRunsPaginator(Boto3Paginator):
    """
    Paginator for `get_job_runs`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, JobName: str, PaginationConfig: GetJobRunsPaginatePaginationConfigTypeDef = None
    ) -> GetJobRunsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`Glue.Client.get_job_runs`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetJobRuns>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              JobName='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type JobName: string
        :param JobName: **[REQUIRED]**

          The name of the job definition for which to retrieve all job runs.

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
                'JobRuns': [
                    {
                        'Id': 'string',
                        'Attempt': 123,
                        'PreviousRunId': 'string',
                        'TriggerName': 'string',
                        'JobName': 'string',
                        'StartedOn': datetime(2015, 1, 1),
                        'LastModifiedOn': datetime(2015, 1, 1),
                        'CompletedOn': datetime(2015, 1, 1),
                        'JobRunState':
                        'STARTING'|'RUNNING'|'STOPPING'|'STOPPED'|'SUCCEEDED'
                        |'FAILED'|'TIMEOUT',
                        'Arguments': {
                            'string': 'string'
                        },
                        'ErrorMessage': 'string',
                        'PredecessorRuns': [
                            {
                                'JobName': 'string',
                                'RunId': 'string'
                            },
                        ],
                        'AllocatedCapacity': 123,
                        'ExecutionTime': 123,
                        'Timeout': 123,
                        'MaxCapacity': 123.0,
                        'WorkerType': 'Standard'|'G.1X'|'G.2X',
                        'NumberOfWorkers': 123,
                        'SecurityConfiguration': 'string',
                        'LogGroupName': 'string',
                        'NotificationProperty': {
                            'NotifyDelayAfter': 123
                        },
                        'GlueVersion': 'string'
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **JobRuns** *(list) --*

              A list of job-run metadata objects.

              - *(dict) --*

                Contains information about a job run.

                - **Id** *(string) --*

                  The ID of this job run.

                - **Attempt** *(integer) --*

                  The number of the attempt to run this job.

                - **PreviousRunId** *(string) --*

                  The ID of the previous run of this job. For example, the ``JobRunId`` specified in
                  the ``StartJobRun`` action.

                - **TriggerName** *(string) --*

                  The name of the trigger that started this job run.

                - **JobName** *(string) --*

                  The name of the job definition being used in this run.

                - **StartedOn** *(datetime) --*

                  The date and time at which this job run was started.

                - **LastModifiedOn** *(datetime) --*

                  The last time that this job run was modified.

                - **CompletedOn** *(datetime) --*

                  The date and time that this job run completed.

                - **JobRunState** *(string) --*

                  The current state of the job run.

                - **Arguments** *(dict) --*

                  The job arguments associated with this run. For this job run, they replace the
                  default arguments set in the job definition itself.

                  You can specify arguments here that your own job-execution script consumes, as
                  well as arguments that AWS Glue itself consumes.

                  For information about how to specify and consume your own job arguments, see the
                  `Calling AWS Glue APIs in Python
                  <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-calling.html>`__
                  topic in the developer guide.

                  For information about the key-value pairs that AWS Glue consumes to set up your
                  job, see the `Special Parameters Used by AWS Glue
                  <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-glue-arguments.html>`__
                  topic in the developer guide.

                  - *(string) --*

                    - *(string) --*

                - **ErrorMessage** *(string) --*

                  An error message associated with this job run.

                - **PredecessorRuns** *(list) --*

                  A list of predecessors to this job run.

                  - *(dict) --*

                    A job run that was used in the predicate of a conditional trigger that triggered
                    this job run.

                    - **JobName** *(string) --*

                      The name of the job definition used by the predecessor job run.

                    - **RunId** *(string) --*

                      The job-run ID of the predecessor job run.

                - **AllocatedCapacity** *(integer) --*

                  This field is deprecated. Use ``MaxCapacity`` instead.

                  The number of AWS Glue data processing units (DPUs) allocated to this JobRun. From
                  2 to 100 DPUs can be allocated; the default is 10. A DPU is a relative measure of
                  processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory.
                  For more information, see the `AWS Glue pricing page
                  <https://aws.amazon.com/glue/pricing/>`__ .

                - **ExecutionTime** *(integer) --*

                  The amount of time (in seconds) that the job run consumed resources.

                - **Timeout** *(integer) --*

                  The ``JobRun`` timeout in minutes. This is the maximum time that a job run can
                  consume resources before it is terminated and enters ``TIMEOUT`` status. The
                  default is 2,880 minutes (48 hours). This overrides the timeout value set in the
                  parent job.

                - **MaxCapacity** *(float) --*

                  The number of AWS Glue data processing units (DPUs) that can be allocated when
                  this job runs. A DPU is a relative measure of processing power that consists of 4
                  vCPUs of compute capacity and 16 GB of memory. For more information, see the `AWS
                  Glue pricing page
                  <https://docs.aws.amazon.com/https:/aws.amazon.com/glue/pricing/>`__ .

                  Do not set ``Max Capacity`` if using ``WorkerType`` and ``NumberOfWorkers`` .

                  The value that can be allocated for ``MaxCapacity`` depends on whether you are
                  running a Python shell job or an Apache Spark ETL job:

                  * When you specify a Python shell job (``JobCommand.Name`` =
                      "pythonshell"), you
                  can allocate either 0.0625 or 1 DPU. The default is 0.0625 DPU.

                  * When you specify an Apache Spark ETL job (``JobCommand.Name`` =
                      "glueetl"), you
                  can allocate from 2 to 100 DPUs. The default is 10 DPUs. This job type cannot have
                  a fractional DPU allocation.

                - **WorkerType** *(string) --*

                  The type of predefined worker that is allocated when a job runs. Accepts a value
                  of Standard, G.1X, or G.2X.

                  * For the ``Standard`` worker type, each worker provides 4 vCPU, 16 GB of memory
                  and a 50GB disk, and 2 executors per worker.

                  * For the ``G.1X`` worker type, each worker provides 4 vCPU, 16 GB of memory and a
                  64GB disk, and 1 executor per worker.

                  * For the ``G.2X`` worker type, each worker provides 8 vCPU, 32 GB of memory and a
                  128GB disk, and 1 executor per worker.

                - **NumberOfWorkers** *(integer) --*

                  The number of workers of a defined ``workerType`` that are allocated when a job
                  runs.

                  The maximum number of workers you can define are 299 for ``G.1X`` , and 149 for
                  ``G.2X`` .

                - **SecurityConfiguration** *(string) --*

                  The name of the ``SecurityConfiguration`` structure to be used with this job run.

                - **LogGroupName** *(string) --*

                  The name of the log group for secure logging that can be server-side encrypted in
                  Amazon CloudWatch using AWS KMS. This name can be ``/aws-glue/jobs/`` , in which
                  case the default encryption is ``NONE`` . If you add a role name and
                  ``SecurityConfiguration`` name (in other words,
                  ``/aws-glue/jobs-yourRoleName-yourSecurityConfigurationName/`` ), then that
                  security configuration is used to encrypt the log group.

                - **NotificationProperty** *(dict) --*

                  Specifies configuration properties of a job run notification.

                  - **NotifyDelayAfter** *(integer) --*

                    After a job run starts, the number of minutes to wait before sending a job run
                    delay notification.

                - **GlueVersion** *(string) --*

                  Glue version determines the versions of Apache Spark and Python that AWS Glue
                  supports. The Python version indicates the version supported for jobs of type
                  Spark.

                  For more information about the available AWS Glue versions and corresponding Spark
                  and Python versions, see `Glue version
                  <https://docs.aws.amazon.com/glue/latest/dg/add-job.html>`__ in the developer
                  guide.

                  Jobs that are created without specifying a Glue version default to Glue 0.9.
        """


class GetJobsPaginator(Boto3Paginator):
    """
    Paginator for `get_jobs`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: GetJobsPaginatePaginationConfigTypeDef = None
    ) -> GetJobsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`Glue.Client.get_jobs`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetJobs>`_

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
                'Jobs': [
                    {
                        'Name': 'string',
                        'Description': 'string',
                        'LogUri': 'string',
                        'Role': 'string',
                        'CreatedOn': datetime(2015, 1, 1),
                        'LastModifiedOn': datetime(2015, 1, 1),
                        'ExecutionProperty': {
                            'MaxConcurrentRuns': 123
                        },
                        'Command': {
                            'Name': 'string',
                            'ScriptLocation': 'string',
                            'PythonVersion': 'string'
                        },
                        'DefaultArguments': {
                            'string': 'string'
                        },
                        'Connections': {
                            'Connections': [
                                'string',
                            ]
                        },
                        'MaxRetries': 123,
                        'AllocatedCapacity': 123,
                        'Timeout': 123,
                        'MaxCapacity': 123.0,
                        'WorkerType': 'Standard'|'G.1X'|'G.2X',
                        'NumberOfWorkers': 123,
                        'SecurityConfiguration': 'string',
                        'NotificationProperty': {
                            'NotifyDelayAfter': 123
                        },
                        'GlueVersion': 'string'
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **Jobs** *(list) --*

              A list of job definitions.

              - *(dict) --*

                Specifies a job definition.

                - **Name** *(string) --*

                  The name you assign to this job definition.

                - **Description** *(string) --*

                  A description of the job.

                - **LogUri** *(string) --*

                  This field is reserved for future use.

                - **Role** *(string) --*

                  The name or Amazon Resource Name (ARN) of the IAM role associated with this job.

                - **CreatedOn** *(datetime) --*

                  The time and date that this job definition was created.

                - **LastModifiedOn** *(datetime) --*

                  The last point in time when this job definition was modified.

                - **ExecutionProperty** *(dict) --*

                  An ``ExecutionProperty`` specifying the maximum number of concurrent runs allowed
                  for this job.

                  - **MaxConcurrentRuns** *(integer) --*

                    The maximum number of concurrent runs allowed for the job. The default is 1. An
                    error is returned when this threshold is reached. The maximum value you can
                    specify is controlled by a service limit.

                - **Command** *(dict) --*

                  The ``JobCommand`` that executes this job.

                  - **Name** *(string) --*

                    The name of the job command. For an Apache Spark ETL job, this must be
                    ``glueetl`` . For a Python shell job, it must be ``pythonshell`` .

                  - **ScriptLocation** *(string) --*

                    Specifies the Amazon Simple Storage Service (Amazon S3) path to a script that
                    executes a job.

                  - **PythonVersion** *(string) --*

                    The Python version being used to execute a Python shell job. Allowed values are
                    2 or 3.

                - **DefaultArguments** *(dict) --*

                  The default arguments for this job, specified as name-value pairs.

                  You can specify arguments here that your own job-execution script consumes, as
                  well as arguments that AWS Glue itself consumes.

                  For information about how to specify and consume your own Job arguments, see the
                  `Calling AWS Glue APIs in Python
                  <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-calling.html>`__
                  topic in the developer guide.

                  For information about the key-value pairs that AWS Glue consumes to set up your
                  job, see the `Special Parameters Used by AWS Glue
                  <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-glue-arguments.html>`__
                  topic in the developer guide.

                  - *(string) --*

                    - *(string) --*

                - **Connections** *(dict) --*

                  The connections used for this job.

                  - **Connections** *(list) --*

                    A list of connections used by the job.

                    - *(string) --*

                - **MaxRetries** *(integer) --*

                  The maximum number of times to retry this job after a JobRun fails.

                - **AllocatedCapacity** *(integer) --*

                  This field is deprecated. Use ``MaxCapacity`` instead.

                  The number of AWS Glue data processing units (DPUs) allocated to runs of this job.
                  You can allocate from 2 to 100 DPUs; the default is 10. A DPU is a relative
                  measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB
                  of memory. For more information, see the `AWS Glue pricing page
                  <https://aws.amazon.com/glue/pricing/>`__ .

                - **Timeout** *(integer) --*

                  The job timeout in minutes. This is the maximum time that a job run can consume
                  resources before it is terminated and enters ``TIMEOUT`` status. The default is
                  2,880 minutes (48 hours).

                - **MaxCapacity** *(float) --*

                  The number of AWS Glue data processing units (DPUs) that can be allocated when
                  this job runs. A DPU is a relative measure of processing power that consists of 4
                  vCPUs of compute capacity and 16 GB of memory. For more information, see the `AWS
                  Glue pricing page <https://aws.amazon.com/glue/pricing/>`__ .

                  Do not set ``Max Capacity`` if using ``WorkerType`` and ``NumberOfWorkers`` .

                  The value that can be allocated for ``MaxCapacity`` depends on whether you are
                  running a Python shell job or an Apache Spark ETL job:

                  * When you specify a Python shell job (``JobCommand.Name`` =
                      "pythonshell"), you
                  can allocate either 0.0625 or 1 DPU. The default is 0.0625 DPU.

                  * When you specify an Apache Spark ETL job (``JobCommand.Name`` =
                      "glueetl"), you
                  can allocate from 2 to 100 DPUs. The default is 10 DPUs. This job type cannot have
                  a fractional DPU allocation.

                - **WorkerType** *(string) --*

                  The type of predefined worker that is allocated when a job runs. Accepts a value
                  of Standard, G.1X, or G.2X.

                  * For the ``Standard`` worker type, each worker provides 4 vCPU, 16 GB of memory
                  and a 50GB disk, and 2 executors per worker.

                  * For the ``G.1X`` worker type, each worker maps to 1 DPU (4 vCPU, 16 GB of
                  memory, 64 GB disk), and provides 1 executor per worker. We recommend this worker
                  type for memory-intensive jobs.

                  * For the ``G.2X`` worker type, each worker maps to 2 DPU (8 vCPU, 32 GB of
                  memory, 128 GB disk), and provides 1 executor per worker. We recommend this worker
                  type for memory-intensive jobs.

                - **NumberOfWorkers** *(integer) --*

                  The number of workers of a defined ``workerType`` that are allocated when a job
                  runs.

                  The maximum number of workers you can define are 299 for ``G.1X`` , and 149 for
                  ``G.2X`` .

                - **SecurityConfiguration** *(string) --*

                  The name of the ``SecurityConfiguration`` structure to be used with this job.

                - **NotificationProperty** *(dict) --*

                  Specifies configuration properties of a job notification.

                  - **NotifyDelayAfter** *(integer) --*

                    After a job run starts, the number of minutes to wait before sending a job run
                    delay notification.

                - **GlueVersion** *(string) --*

                  Glue version determines the versions of Apache Spark and Python that AWS Glue
                  supports. The Python version indicates the version supported for jobs of type
                  Spark.

                  For more information about the available AWS Glue versions and corresponding Spark
                  and Python versions, see `Glue version
                  <https://docs.aws.amazon.com/glue/latest/dg/add-job.html>`__ in the developer
                  guide.

                  Jobs that are created without specifying a Glue version default to Glue 0.9.
        """


class GetPartitionsPaginator(Boto3Paginator):
    """
    Paginator for `get_partitions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DatabaseName: str,
        TableName: str,
        CatalogId: str = None,
        Expression: str = None,
        Segment: GetPartitionsPaginateSegmentTypeDef = None,
        PaginationConfig: GetPartitionsPaginatePaginationConfigTypeDef = None,
    ) -> GetPartitionsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`Glue.Client.get_partitions`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetPartitions>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              CatalogId='string',
              DatabaseName='string',
              TableName='string',
              Expression='string',
              Segment={
                  'SegmentNumber': 123,
                  'TotalSegments': 123
              },
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type CatalogId: string
        :param CatalogId:

          The ID of the Data Catalog where the partitions in question reside. If none is provided,
          the AWS account ID is used by default.

        :type DatabaseName: string
        :param DatabaseName: **[REQUIRED]**

          The name of the catalog database where the partitions reside.

        :type TableName: string
        :param TableName: **[REQUIRED]**

          The name of the partitions' table.

        :type Expression: string
        :param Expression:

          An expression that filters the partitions to be returned.

          The expression uses SQL syntax similar to the SQL ``WHERE`` filter clause. The SQL
          statement parser `JSQLParser <http://jsqlparser.sourceforge.net/home.php>`__ parses the
          expression.

           *Operators* : The following are the operators that you can use in the ``Expression`` API
           call:

            =

          Checks whether the values of the two operands are equal; if yes, then the condition
          becomes true.

          Example: Assume 'variable a' holds 10 and 'variable b' holds 20.

          (a = b) is not true.

            < >

          Checks whether the values of two operands are equal; if the values are not equal, then the
          condition becomes true.

          Example: (a < > b) is true.

            >

          Checks whether the value of the left operand is greater than the value of the right
          operand; if yes, then the condition becomes true.

          Example: (a > b) is not true.

            <

          Checks whether the value of the left operand is less than the value of the right operand;
          if yes, then the condition becomes true.

          Example: (a < b) is true.

            >=

          Checks whether the value of the left operand is greater than or equal to the value of the
          right operand; if yes, then the condition becomes true.

          Example: (a >= b) is not true.

            <=

          Checks whether the value of the left operand is less than or equal to the value of the
          right operand; if yes, then the condition becomes true.

          Example: (a <= b) is true.

            AND, OR, IN, BETWEEN, LIKE, NOT, IS NULL

          Logical operators.

           *Supported Partition Key Types* : The following are the supported partition keys.

          * ``string``

          * ``date``

          * ``timestamp``

          * ``int``

          * ``bigint``

          * ``long``

          * ``tinyint``

          * ``smallint``

          * ``decimal``

          If an invalid type is encountered, an exception is thrown.

          The following list shows the valid operators on each type. When you define a crawler, the
          ``partitionKey`` type is created as a ``STRING`` , to be compatible with the catalog
          partitions.

           *Sample API Call* :

        :type Segment: dict
        :param Segment:

          The segment of the table's partitions to scan in this request.

          - **SegmentNumber** *(integer) --* **[REQUIRED]**

            The zero-based index number of the segment. For example, if the total number of segments
            is 4, ``SegmentNumber`` values range from 0 through 3.

          - **TotalSegments** *(integer) --* **[REQUIRED]**

            The total number of segments.

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
                'Partitions': [
                    {
                        'Values': [
                            'string',
                        ],
                        'DatabaseName': 'string',
                        'TableName': 'string',
                        'CreationTime': datetime(2015, 1, 1),
                        'LastAccessTime': datetime(2015, 1, 1),
                        'StorageDescriptor': {
                            'Columns': [
                                {
                                    'Name': 'string',
                                    'Type': 'string',
                                    'Comment': 'string',
                                    'Parameters': {
                                        'string': 'string'
                                    }
                                },
                            ],
                            'Location': 'string',
                            'InputFormat': 'string',
                            'OutputFormat': 'string',
                            'Compressed': True|False,
                            'NumberOfBuckets': 123,
                            'SerdeInfo': {
                                'Name': 'string',
                                'SerializationLibrary': 'string',
                                'Parameters': {
                                    'string': 'string'
                                }
                            },
                            'BucketColumns': [
                                'string',
                            ],
                            'SortColumns': [
                                {
                                    'Column': 'string',
                                    'SortOrder': 123
                                },
                            ],
                            'Parameters': {
                                'string': 'string'
                            },
                            'SkewedInfo': {
                                'SkewedColumnNames': [
                                    'string',
                                ],
                                'SkewedColumnValues': [
                                    'string',
                                ],
                                'SkewedColumnValueLocationMaps': {
                                    'string': 'string'
                                }
                            },
                            'StoredAsSubDirectories': True|False
                        },
                        'Parameters': {
                            'string': 'string'
                        },
                        'LastAnalyzedTime': datetime(2015, 1, 1)
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **Partitions** *(list) --*

              A list of requested partitions.

              - *(dict) --*

                Represents a slice of table data.

                - **Values** *(list) --*

                  The values of the partition.

                  - *(string) --*

                - **DatabaseName** *(string) --*

                  The name of the catalog database in which to create the partition.

                - **TableName** *(string) --*

                  The name of the database table in which to create the partition.

                - **CreationTime** *(datetime) --*

                  The time at which the partition was created.

                - **LastAccessTime** *(datetime) --*

                  The last time at which the partition was accessed.

                - **StorageDescriptor** *(dict) --*

                  Provides information about the physical location where the partition is stored.

                  - **Columns** *(list) --*

                    A list of the ``Columns`` in the table.

                    - *(dict) --*

                      A column in a ``Table`` .

                      - **Name** *(string) --*

                        The name of the ``Column`` .

                      - **Type** *(string) --*

                        The data type of the ``Column`` .

                      - **Comment** *(string) --*

                        A free-form text comment.

                      - **Parameters** *(dict) --*

                        These key-value pairs define properties associated with the column.

                        - *(string) --*

                          - *(string) --*

                  - **Location** *(string) --*

                    The physical location of the table. By default, this takes the form of the
                    warehouse location, followed by the database location in the warehouse, followed
                    by the table name.

                  - **InputFormat** *(string) --*

                    The input format: ``SequenceFileInputFormat`` (binary), or ``TextInputFormat`` ,
                    or a custom format.

                  - **OutputFormat** *(string) --*

                    The output format: ``SequenceFileOutputFormat`` (binary), or
                    ``IgnoreKeyTextOutputFormat`` , or a custom format.

                  - **Compressed** *(boolean) --*

                     ``True`` if the data in the table is compressed, or ``False`` if not.

                  - **NumberOfBuckets** *(integer) --*

                    Must be specified if the table contains any dimension columns.

                  - **SerdeInfo** *(dict) --*

                    The serialization/deserialization (SerDe) information.

                    - **Name** *(string) --*

                      Name of the SerDe.

                    - **SerializationLibrary** *(string) --*

                      Usually the class that implements the SerDe. An example is
                      ``org.apache.hadoop.hive.serde2.columnar.ColumnarSerDe`` .

                    - **Parameters** *(dict) --*

                      These key-value pairs define initialization parameters for the SerDe.

                      - *(string) --*

                        - *(string) --*

                  - **BucketColumns** *(list) --*

                    A list of reducer grouping columns, clustering columns, and bucketing columns in
                    the table.

                    - *(string) --*

                  - **SortColumns** *(list) --*

                    A list specifying the sort order of each bucket in the table.

                    - *(dict) --*

                      Specifies the sort order of a sorted column.

                      - **Column** *(string) --*

                        The name of the column.

                      - **SortOrder** *(integer) --*

                        Indicates that the column is sorted in ascending order (``==
                             1`` ), or in
                        descending order (``==0`` ).

                  - **Parameters** *(dict) --*

                    The user-supplied properties in key-value form.

                    - *(string) --*

                      - *(string) --*

                  - **SkewedInfo** *(dict) --*

                    The information about values that appear frequently in a column (skewed values).

                    - **SkewedColumnNames** *(list) --*

                      A list of names of columns that contain skewed values.

                      - *(string) --*

                    - **SkewedColumnValues** *(list) --*

                      A list of values that appear so frequently as to be considered skewed.

                      - *(string) --*

                    - **SkewedColumnValueLocationMaps** *(dict) --*

                      A mapping of skewed values to the columns that contain them.

                      - *(string) --*

                        - *(string) --*

                  - **StoredAsSubDirectories** *(boolean) --*

                     ``True`` if the table data is stored in subdirectories, or ``False`` if not.

                - **Parameters** *(dict) --*

                  These key-value pairs define partition parameters.

                  - *(string) --*

                    - *(string) --*

                - **LastAnalyzedTime** *(datetime) --*

                  The last time at which column statistics were computed for this partition.
        """


class GetSecurityConfigurationsPaginator(Boto3Paginator):
    """
    Paginator for `get_security_configurations`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: GetSecurityConfigurationsPaginatePaginationConfigTypeDef = None
    ) -> GetSecurityConfigurationsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`Glue.Client.get_security_configurations`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetSecurityConfigurations>`_

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
                'SecurityConfigurations': [
                    {
                        'Name': 'string',
                        'CreatedTimeStamp': datetime(2015, 1, 1),
                        'EncryptionConfiguration': {
                            'S3Encryption': [
                                {
                                    'S3EncryptionMode': 'DISABLED'|'SSE-KMS'|'SSE-S3',
                                    'KmsKeyArn': 'string'
                                },
                            ],
                            'CloudWatchEncryption': {
                                'CloudWatchEncryptionMode': 'DISABLED'|'SSE-KMS',
                                'KmsKeyArn': 'string'
                            },
                            'JobBookmarksEncryption': {
                                'JobBookmarksEncryptionMode': 'DISABLED'|'CSE-KMS',
                                'KmsKeyArn': 'string'
                            }
                        }
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **SecurityConfigurations** *(list) --*

              A list of security configurations.

              - *(dict) --*

                Specifies a security configuration.

                - **Name** *(string) --*

                  The name of the security configuration.

                - **CreatedTimeStamp** *(datetime) --*

                  The time at which this security configuration was created.

                - **EncryptionConfiguration** *(dict) --*

                  The encryption configuration associated with this security configuration.

                  - **S3Encryption** *(list) --*

                    The encryption configuration for Amazon Simple Storage Service (Amazon S3) data.

                    - *(dict) --*

                      Specifies how Amazon Simple Storage Service (Amazon S3) data should be
                      encrypted.

                      - **S3EncryptionMode** *(string) --*

                        The encryption mode to use for Amazon S3 data.

                      - **KmsKeyArn** *(string) --*

                        The Amazon Resource Name (ARN) of the KMS key to be used to encrypt the
                        data.

                  - **CloudWatchEncryption** *(dict) --*

                    The encryption configuration for Amazon CloudWatch.

                    - **CloudWatchEncryptionMode** *(string) --*

                      The encryption mode to use for CloudWatch data.

                    - **KmsKeyArn** *(string) --*

                      The Amazon Resource Name (ARN) of the KMS key to be used to encrypt the data.

                  - **JobBookmarksEncryption** *(dict) --*

                    The encryption configuration for job bookmarks.

                    - **JobBookmarksEncryptionMode** *(string) --*

                      The encryption mode to use for job bookmarks data.

                    - **KmsKeyArn** *(string) --*

                      The Amazon Resource Name (ARN) of the KMS key to be used to encrypt the data.
        """


class GetTableVersionsPaginator(Boto3Paginator):
    """
    Paginator for `get_table_versions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DatabaseName: str,
        TableName: str,
        CatalogId: str = None,
        PaginationConfig: GetTableVersionsPaginatePaginationConfigTypeDef = None,
    ) -> GetTableVersionsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`Glue.Client.get_table_versions`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetTableVersions>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              CatalogId='string',
              DatabaseName='string',
              TableName='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type CatalogId: string
        :param CatalogId:

          The ID of the Data Catalog where the tables reside. If none is provided, the AWS account
          ID is used by default.

        :type DatabaseName: string
        :param DatabaseName: **[REQUIRED]**

          The database in the catalog in which the table resides. For Hive compatibility, this name
          is entirely lowercase.

        :type TableName: string
        :param TableName: **[REQUIRED]**

          The name of the table. For Hive compatibility, this name is entirely lowercase.

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
                'TableVersions': [
                    {
                        'Table': {
                            'Name': 'string',
                            'DatabaseName': 'string',
                            'Description': 'string',
                            'Owner': 'string',
                            'CreateTime': datetime(2015, 1, 1),
                            'UpdateTime': datetime(2015, 1, 1),
                            'LastAccessTime': datetime(2015, 1, 1),
                            'LastAnalyzedTime': datetime(2015, 1, 1),
                            'Retention': 123,
                            'StorageDescriptor': {
                                'Columns': [
                                    {
                                        'Name': 'string',
                                        'Type': 'string',
                                        'Comment': 'string',
                                        'Parameters': {
                                            'string': 'string'
                                        }
                                    },
                                ],
                                'Location': 'string',
                                'InputFormat': 'string',
                                'OutputFormat': 'string',
                                'Compressed': True|False,
                                'NumberOfBuckets': 123,
                                'SerdeInfo': {
                                    'Name': 'string',
                                    'SerializationLibrary': 'string',
                                    'Parameters': {
                                        'string': 'string'
                                    }
                                },
                                'BucketColumns': [
                                    'string',
                                ],
                                'SortColumns': [
                                    {
                                        'Column': 'string',
                                        'SortOrder': 123
                                    },
                                ],
                                'Parameters': {
                                    'string': 'string'
                                },
                                'SkewedInfo': {
                                    'SkewedColumnNames': [
                                        'string',
                                    ],
                                    'SkewedColumnValues': [
                                        'string',
                                    ],
                                    'SkewedColumnValueLocationMaps': {
                                        'string': 'string'
                                    }
                                },
                                'StoredAsSubDirectories': True|False
                            },
                            'PartitionKeys': [
                                {
                                    'Name': 'string',
                                    'Type': 'string',
                                    'Comment': 'string',
                                    'Parameters': {
                                        'string': 'string'
                                    }
                                },
                            ],
                            'ViewOriginalText': 'string',
                            'ViewExpandedText': 'string',
                            'TableType': 'string',
                            'Parameters': {
                                'string': 'string'
                            },
                            'CreatedBy': 'string',
                            'IsRegisteredWithLakeFormation': True|False
                        },
                        'VersionId': 'string'
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **TableVersions** *(list) --*

              A list of strings identifying available versions of the specified table.

              - *(dict) --*

                Specifies a version of a table.

                - **Table** *(dict) --*

                  The table in question.

                  - **Name** *(string) --*

                    The table name. For Hive compatibility, this must be entirely lowercase.

                  - **DatabaseName** *(string) --*

                    The name of the database where the table metadata resides. For Hive
                    compatibility, this must be all lowercase.

                  - **Description** *(string) --*

                    A description of the table.

                  - **Owner** *(string) --*

                    The owner of the table.

                  - **CreateTime** *(datetime) --*

                    The time when the table definition was created in the Data Catalog.

                  - **UpdateTime** *(datetime) --*

                    The last time that the table was updated.

                  - **LastAccessTime** *(datetime) --*

                    The last time that the table was accessed. This is usually taken from HDFS, and
                    might not be reliable.

                  - **LastAnalyzedTime** *(datetime) --*

                    The last time that column statistics were computed for this table.

                  - **Retention** *(integer) --*

                    The retention time for this table.

                  - **StorageDescriptor** *(dict) --*

                    A storage descriptor containing information about the physical storage of this
                    table.

                    - **Columns** *(list) --*

                      A list of the ``Columns`` in the table.

                      - *(dict) --*

                        A column in a ``Table`` .

                        - **Name** *(string) --*

                          The name of the ``Column`` .

                        - **Type** *(string) --*

                          The data type of the ``Column`` .

                        - **Comment** *(string) --*

                          A free-form text comment.

                        - **Parameters** *(dict) --*

                          These key-value pairs define properties associated with the column.

                          - *(string) --*

                            - *(string) --*

                    - **Location** *(string) --*

                      The physical location of the table. By default, this takes the form of the
                      warehouse location, followed by the database location in the warehouse,
                      followed by the table name.

                    - **InputFormat** *(string) --*

                      The input format: ``SequenceFileInputFormat`` (binary), or ``TextInputFormat``
                      , or a custom format.

                    - **OutputFormat** *(string) --*

                      The output format: ``SequenceFileOutputFormat`` (binary), or
                      ``IgnoreKeyTextOutputFormat`` , or a custom format.

                    - **Compressed** *(boolean) --*

                       ``True`` if the data in the table is compressed, or ``False`` if not.

                    - **NumberOfBuckets** *(integer) --*

                      Must be specified if the table contains any dimension columns.

                    - **SerdeInfo** *(dict) --*

                      The serialization/deserialization (SerDe) information.

                      - **Name** *(string) --*

                        Name of the SerDe.

                      - **SerializationLibrary** *(string) --*

                        Usually the class that implements the SerDe. An example is
                        ``org.apache.hadoop.hive.serde2.columnar.ColumnarSerDe`` .

                      - **Parameters** *(dict) --*

                        These key-value pairs define initialization parameters for the SerDe.

                        - *(string) --*

                          - *(string) --*

                    - **BucketColumns** *(list) --*

                      A list of reducer grouping columns, clustering columns, and bucketing columns
                      in the table.

                      - *(string) --*

                    - **SortColumns** *(list) --*

                      A list specifying the sort order of each bucket in the table.

                      - *(dict) --*

                        Specifies the sort order of a sorted column.

                        - **Column** *(string) --*

                          The name of the column.

                        - **SortOrder** *(integer) --*

                          Indicates that the column is sorted in ascending order (``== 1`` ), or in
                          descending order (``==0`` ).

                    - **Parameters** *(dict) --*

                      The user-supplied properties in key-value form.

                      - *(string) --*

                        - *(string) --*

                    - **SkewedInfo** *(dict) --*

                      The information about values that appear frequently in a column (skewed
                      values).

                      - **SkewedColumnNames** *(list) --*

                        A list of names of columns that contain skewed values.

                        - *(string) --*

                      - **SkewedColumnValues** *(list) --*

                        A list of values that appear so frequently as to be considered skewed.

                        - *(string) --*

                      - **SkewedColumnValueLocationMaps** *(dict) --*

                        A mapping of skewed values to the columns that contain them.

                        - *(string) --*

                          - *(string) --*

                    - **StoredAsSubDirectories** *(boolean) --*

                       ``True`` if the table data is stored in subdirectories, or ``False`` if not.

                  - **PartitionKeys** *(list) --*

                    A list of columns by which the table is partitioned. Only primitive types are
                    supported as partition keys.

                    When you create a table used by Amazon Athena, and you do not specify any
                    ``partitionKeys`` , you must at least set the value of ``partitionKeys`` to an
                    empty list. For example:

                     ``"PartitionKeys": []``

                    - *(dict) --*

                      A column in a ``Table`` .

                      - **Name** *(string) --*

                        The name of the ``Column`` .

                      - **Type** *(string) --*

                        The data type of the ``Column`` .

                      - **Comment** *(string) --*

                        A free-form text comment.

                      - **Parameters** *(dict) --*

                        These key-value pairs define properties associated with the column.

                        - *(string) --*

                          - *(string) --*

                  - **ViewOriginalText** *(string) --*

                    If the table is a view, the original text of the view; otherwise ``null`` .

                  - **ViewExpandedText** *(string) --*

                    If the table is a view, the expanded text of the view; otherwise ``null`` .

                  - **TableType** *(string) --*

                    The type of this table (``EXTERNAL_TABLE`` , ``VIRTUAL_VIEW`` , etc.).

                  - **Parameters** *(dict) --*

                    These key-value pairs define properties associated with the table.

                    - *(string) --*

                      - *(string) --*

                  - **CreatedBy** *(string) --*

                    The person or entity who created the table.

                  - **IsRegisteredWithLakeFormation** *(boolean) --*

                    Indicates whether the table has been registered with AWS Lake Formation.

                - **VersionId** *(string) --*

                  The ID value that identifies this table version. A ``VersionId`` is a string
                  representation of an integer. Each version is incremented by 1.
        """


class GetTablesPaginator(Boto3Paginator):
    """
    Paginator for `get_tables`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DatabaseName: str,
        CatalogId: str = None,
        Expression: str = None,
        PaginationConfig: GetTablesPaginatePaginationConfigTypeDef = None,
    ) -> GetTablesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`Glue.Client.get_tables`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetTables>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              CatalogId='string',
              DatabaseName='string',
              Expression='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type CatalogId: string
        :param CatalogId:

          The ID of the Data Catalog where the tables reside. If none is provided, the AWS account
          ID is used by default.

        :type DatabaseName: string
        :param DatabaseName: **[REQUIRED]**

          The database in the catalog whose tables to list. For Hive compatibility, this name is
          entirely lowercase.

        :type Expression: string
        :param Expression:

          A regular expression pattern. If present, only those tables whose names match the pattern
          are returned.

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
                'TableList': [
                    {
                        'Name': 'string',
                        'DatabaseName': 'string',
                        'Description': 'string',
                        'Owner': 'string',
                        'CreateTime': datetime(2015, 1, 1),
                        'UpdateTime': datetime(2015, 1, 1),
                        'LastAccessTime': datetime(2015, 1, 1),
                        'LastAnalyzedTime': datetime(2015, 1, 1),
                        'Retention': 123,
                        'StorageDescriptor': {
                            'Columns': [
                                {
                                    'Name': 'string',
                                    'Type': 'string',
                                    'Comment': 'string',
                                    'Parameters': {
                                        'string': 'string'
                                    }
                                },
                            ],
                            'Location': 'string',
                            'InputFormat': 'string',
                            'OutputFormat': 'string',
                            'Compressed': True|False,
                            'NumberOfBuckets': 123,
                            'SerdeInfo': {
                                'Name': 'string',
                                'SerializationLibrary': 'string',
                                'Parameters': {
                                    'string': 'string'
                                }
                            },
                            'BucketColumns': [
                                'string',
                            ],
                            'SortColumns': [
                                {
                                    'Column': 'string',
                                    'SortOrder': 123
                                },
                            ],
                            'Parameters': {
                                'string': 'string'
                            },
                            'SkewedInfo': {
                                'SkewedColumnNames': [
                                    'string',
                                ],
                                'SkewedColumnValues': [
                                    'string',
                                ],
                                'SkewedColumnValueLocationMaps': {
                                    'string': 'string'
                                }
                            },
                            'StoredAsSubDirectories': True|False
                        },
                        'PartitionKeys': [
                            {
                                'Name': 'string',
                                'Type': 'string',
                                'Comment': 'string',
                                'Parameters': {
                                    'string': 'string'
                                }
                            },
                        ],
                        'ViewOriginalText': 'string',
                        'ViewExpandedText': 'string',
                        'TableType': 'string',
                        'Parameters': {
                            'string': 'string'
                        },
                        'CreatedBy': 'string',
                        'IsRegisteredWithLakeFormation': True|False
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **TableList** *(list) --*

              A list of the requested ``Table`` objects.

              - *(dict) --*

                Represents a collection of related data organized in columns and rows.

                - **Name** *(string) --*

                  The table name. For Hive compatibility, this must be entirely lowercase.

                - **DatabaseName** *(string) --*

                  The name of the database where the table metadata resides. For Hive compatibility,
                  this must be all lowercase.

                - **Description** *(string) --*

                  A description of the table.

                - **Owner** *(string) --*

                  The owner of the table.

                - **CreateTime** *(datetime) --*

                  The time when the table definition was created in the Data Catalog.

                - **UpdateTime** *(datetime) --*

                  The last time that the table was updated.

                - **LastAccessTime** *(datetime) --*

                  The last time that the table was accessed. This is usually taken from HDFS, and
                  might not be reliable.

                - **LastAnalyzedTime** *(datetime) --*

                  The last time that column statistics were computed for this table.

                - **Retention** *(integer) --*

                  The retention time for this table.

                - **StorageDescriptor** *(dict) --*

                  A storage descriptor containing information about the physical storage of this
                  table.

                  - **Columns** *(list) --*

                    A list of the ``Columns`` in the table.

                    - *(dict) --*

                      A column in a ``Table`` .

                      - **Name** *(string) --*

                        The name of the ``Column`` .

                      - **Type** *(string) --*

                        The data type of the ``Column`` .

                      - **Comment** *(string) --*

                        A free-form text comment.

                      - **Parameters** *(dict) --*

                        These key-value pairs define properties associated with the column.

                        - *(string) --*

                          - *(string) --*

                  - **Location** *(string) --*

                    The physical location of the table. By default, this takes the form of the
                    warehouse location, followed by the database location in the warehouse, followed
                    by the table name.

                  - **InputFormat** *(string) --*

                    The input format: ``SequenceFileInputFormat`` (binary), or ``TextInputFormat`` ,
                    or a custom format.

                  - **OutputFormat** *(string) --*

                    The output format: ``SequenceFileOutputFormat`` (binary), or
                    ``IgnoreKeyTextOutputFormat`` , or a custom format.

                  - **Compressed** *(boolean) --*

                     ``True`` if the data in the table is compressed, or ``False`` if not.

                  - **NumberOfBuckets** *(integer) --*

                    Must be specified if the table contains any dimension columns.

                  - **SerdeInfo** *(dict) --*

                    The serialization/deserialization (SerDe) information.

                    - **Name** *(string) --*

                      Name of the SerDe.

                    - **SerializationLibrary** *(string) --*

                      Usually the class that implements the SerDe. An example is
                      ``org.apache.hadoop.hive.serde2.columnar.ColumnarSerDe`` .

                    - **Parameters** *(dict) --*

                      These key-value pairs define initialization parameters for the SerDe.

                      - *(string) --*

                        - *(string) --*

                  - **BucketColumns** *(list) --*

                    A list of reducer grouping columns, clustering columns, and bucketing columns in
                    the table.

                    - *(string) --*

                  - **SortColumns** *(list) --*

                    A list specifying the sort order of each bucket in the table.

                    - *(dict) --*

                      Specifies the sort order of a sorted column.

                      - **Column** *(string) --*

                        The name of the column.

                      - **SortOrder** *(integer) --*

                        Indicates that the column is sorted in ascending order (``==
                             1`` ), or in
                        descending order (``==0`` ).

                  - **Parameters** *(dict) --*

                    The user-supplied properties in key-value form.

                    - *(string) --*

                      - *(string) --*

                  - **SkewedInfo** *(dict) --*

                    The information about values that appear frequently in a column (skewed values).

                    - **SkewedColumnNames** *(list) --*

                      A list of names of columns that contain skewed values.

                      - *(string) --*

                    - **SkewedColumnValues** *(list) --*

                      A list of values that appear so frequently as to be considered skewed.

                      - *(string) --*

                    - **SkewedColumnValueLocationMaps** *(dict) --*

                      A mapping of skewed values to the columns that contain them.

                      - *(string) --*

                        - *(string) --*

                  - **StoredAsSubDirectories** *(boolean) --*

                     ``True`` if the table data is stored in subdirectories, or ``False`` if not.

                - **PartitionKeys** *(list) --*

                  A list of columns by which the table is partitioned. Only primitive types are
                  supported as partition keys.

                  When you create a table used by Amazon Athena, and you do not specify any
                  ``partitionKeys`` , you must at least set the value of ``partitionKeys`` to an
                  empty list. For example:

                   ``"PartitionKeys": []``

                  - *(dict) --*

                    A column in a ``Table`` .

                    - **Name** *(string) --*

                      The name of the ``Column`` .

                    - **Type** *(string) --*

                      The data type of the ``Column`` .

                    - **Comment** *(string) --*

                      A free-form text comment.

                    - **Parameters** *(dict) --*

                      These key-value pairs define properties associated with the column.

                      - *(string) --*

                        - *(string) --*

                - **ViewOriginalText** *(string) --*

                  If the table is a view, the original text of the view; otherwise ``null`` .

                - **ViewExpandedText** *(string) --*

                  If the table is a view, the expanded text of the view; otherwise ``null`` .

                - **TableType** *(string) --*

                  The type of this table (``EXTERNAL_TABLE`` , ``VIRTUAL_VIEW`` , etc.).

                - **Parameters** *(dict) --*

                  These key-value pairs define properties associated with the table.

                  - *(string) --*

                    - *(string) --*

                - **CreatedBy** *(string) --*

                  The person or entity who created the table.

                - **IsRegisteredWithLakeFormation** *(boolean) --*

                  Indicates whether the table has been registered with AWS Lake Formation.
        """


class GetTriggersPaginator(Boto3Paginator):
    """
    Paginator for `get_triggers`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DependentJobName: str = None,
        PaginationConfig: GetTriggersPaginatePaginationConfigTypeDef = None,
    ) -> GetTriggersPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`Glue.Client.get_triggers`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetTriggers>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              DependentJobName='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type DependentJobName: string
        :param DependentJobName:

          The name of the job to retrieve triggers for. The trigger that can start this job is
          returned, and if there is no such trigger, all triggers are returned.

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
                'Triggers': [
                    {
                        'Name': 'string',
                        'WorkflowName': 'string',
                        'Id': 'string',
                        'Type': 'SCHEDULED'|'CONDITIONAL'|'ON_DEMAND',
                        'State':
                        'CREATING'|'CREATED'|'ACTIVATING'|'ACTIVATED'|'DEACTIVATING'
                        |'DEACTIVATED'|'DELETING'|'UPDATING',
                        'Description': 'string',
                        'Schedule': 'string',
                        'Actions': [
                            {
                                'JobName': 'string',
                                'Arguments': {
                                    'string': 'string'
                                },
                                'Timeout': 123,
                                'SecurityConfiguration': 'string',
                                'NotificationProperty': {
                                    'NotifyDelayAfter': 123
                                },
                                'CrawlerName': 'string'
                            },
                        ],
                        'Predicate': {
                            'Logical': 'AND'|'ANY',
                            'Conditions': [
                                {
                                    'LogicalOperator': 'EQUALS',
                                    'JobName': 'string',
                                    'State':
                                    'STARTING'|'RUNNING'|'STOPPING'
                                    |'STOPPED'|'SUCCEEDED'|'FAILED'
                                    |'TIMEOUT',
                                    'CrawlerName': 'string',
                                    'CrawlState': 'RUNNING'|'SUCCEEDED'|'CANCELLED'|'FAILED'
                                },
                            ]
                        }
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **Triggers** *(list) --*

              A list of triggers for the specified job.

              - *(dict) --*

                Information about a specific trigger.

                - **Name** *(string) --*

                  The name of the trigger.

                - **WorkflowName** *(string) --*

                  The name of the workflow associated with the trigger.

                - **Id** *(string) --*

                  Reserved for future use.

                - **Type** *(string) --*

                  The type of trigger that this is.

                - **State** *(string) --*

                  The current state of the trigger.

                - **Description** *(string) --*

                  A description of this trigger.

                - **Schedule** *(string) --*

                  A ``cron`` expression used to specify the schedule (see `Time-Based Schedules for
                  Jobs and Crawlers
                  <https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html>`__
                  . For example, to run something every day at 12:15 UTC, you would specify:
                  ``cron(15 12 * * ? *)`` .

                - **Actions** *(list) --*

                  The actions initiated by this trigger.

                  - *(dict) --*

                    Defines an action to be initiated by a trigger.

                    - **JobName** *(string) --*

                      The name of a job to be executed.

                    - **Arguments** *(dict) --*

                      The job arguments used when this trigger fires. For this job run, they replace
                      the default arguments set in the job definition itself.

                      You can specify arguments here that your own job-execution script consumes, as
                      well as arguments that AWS Glue itself consumes.

                      For information about how to specify and consume your own Job arguments, see
                      the `Calling AWS Glue APIs in Python
                      <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-calling.html>`__
                      topic in the developer guide.

                      For information about the key-value pairs that AWS Glue consumes to set up
                      your job, see the `Special Parameters Used by AWS Glue
                      <https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-glue-arguments.html>`__
                      topic in the developer guide.

                      - *(string) --*

                        - *(string) --*

                    - **Timeout** *(integer) --*

                      The ``JobRun`` timeout in minutes. This is the maximum time that a job run can
                      consume resources before it is terminated and enters ``TIMEOUT`` status. The
                      default is 2,880 minutes (48 hours). This overrides the timeout value set in
                      the parent job.

                    - **SecurityConfiguration** *(string) --*

                      The name of the ``SecurityConfiguration`` structure to be used with this
                      action.

                    - **NotificationProperty** *(dict) --*

                      Specifies configuration properties of a job run notification.

                      - **NotifyDelayAfter** *(integer) --*

                        After a job run starts, the number of minutes to wait before sending a job
                        run delay notification.

                    - **CrawlerName** *(string) --*

                      The name of the crawler to be used with this action.

                - **Predicate** *(dict) --*

                  The predicate of this trigger, which defines when it will fire.

                  - **Logical** *(string) --*

                    An optional field if only one condition is listed. If multiple conditions are
                    listed, then this field is required.

                  - **Conditions** *(list) --*

                    A list of the conditions that determine when the trigger will fire.

                    - *(dict) --*

                      Defines a condition under which a trigger fires.

                      - **LogicalOperator** *(string) --*

                        A logical operator.

                      - **JobName** *(string) --*

                        The name of the job whose ``JobRuns`` this condition applies to, and on
                        which this trigger waits.

                      - **State** *(string) --*

                        The condition state. Currently, the values supported are ``SUCCEEDED`` ,
                        ``STOPPED`` , ``TIMEOUT`` , and ``FAILED`` .

                      - **CrawlerName** *(string) --*

                        The name of the crawler to which this condition applies.

                      - **CrawlState** *(string) --*

                        The state of the crawler to which this condition applies.
        """


class GetUserDefinedFunctionsPaginator(Boto3Paginator):
    """
    Paginator for `get_user_defined_functions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DatabaseName: str,
        Pattern: str,
        CatalogId: str = None,
        PaginationConfig: GetUserDefinedFunctionsPaginatePaginationConfigTypeDef = None,
    ) -> GetUserDefinedFunctionsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`Glue.Client.get_user_defined_functions`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetUserDefinedFunctions>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              CatalogId='string',
              DatabaseName='string',
              Pattern='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type CatalogId: string
        :param CatalogId:

          The ID of the Data Catalog where the functions to be retrieved are located. If none is
          provided, the AWS account ID is used by default.

        :type DatabaseName: string
        :param DatabaseName: **[REQUIRED]**

          The name of the catalog database where the functions are located.

        :type Pattern: string
        :param Pattern: **[REQUIRED]**

          An optional function-name pattern string that filters the function definitions returned.

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
                'UserDefinedFunctions': [
                    {
                        'FunctionName': 'string',
                        'ClassName': 'string',
                        'OwnerName': 'string',
                        'OwnerType': 'USER'|'ROLE'|'GROUP',
                        'CreateTime': datetime(2015, 1, 1),
                        'ResourceUris': [
                            {
                                'ResourceType': 'JAR'|'FILE'|'ARCHIVE',
                                'Uri': 'string'
                            },
                        ]
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **UserDefinedFunctions** *(list) --*

              A list of requested function definitions.

              - *(dict) --*

                Represents the equivalent of a Hive user-defined function (``UDF`` ) definition.

                - **FunctionName** *(string) --*

                  The name of the function.

                - **ClassName** *(string) --*

                  The Java class that contains the function code.

                - **OwnerName** *(string) --*

                  The owner of the function.

                - **OwnerType** *(string) --*

                  The owner type.

                - **CreateTime** *(datetime) --*

                  The time at which the function was created.

                - **ResourceUris** *(list) --*

                  The resource URIs for the function.

                  - *(dict) --*

                    The URIs for function resources.

                    - **ResourceType** *(string) --*

                      The type of the resource.

                    - **Uri** *(string) --*

                      The URI for accessing the resource.
        """
