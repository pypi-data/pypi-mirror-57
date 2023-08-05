"Main interface for appsync service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3.type_defs import Literal
from mypy_boto3_appsync.type_defs import (
    ListApiKeysPaginatePaginationConfigTypeDef,
    ListApiKeysPaginateResponseTypeDef,
    ListDataSourcesPaginatePaginationConfigTypeDef,
    ListDataSourcesPaginateResponseTypeDef,
    ListFunctionsPaginatePaginationConfigTypeDef,
    ListFunctionsPaginateResponseTypeDef,
    ListGraphqlApisPaginatePaginationConfigTypeDef,
    ListGraphqlApisPaginateResponseTypeDef,
    ListResolversByFunctionPaginatePaginationConfigTypeDef,
    ListResolversByFunctionPaginateResponseTypeDef,
    ListResolversPaginatePaginationConfigTypeDef,
    ListResolversPaginateResponseTypeDef,
    ListTypesPaginatePaginationConfigTypeDef,
    ListTypesPaginateResponseTypeDef,
)


__all__ = (
    "ListApiKeysPaginator",
    "ListDataSourcesPaginator",
    "ListFunctionsPaginator",
    "ListGraphqlApisPaginator",
    "ListResolversPaginator",
    "ListResolversByFunctionPaginator",
    "ListTypesPaginator",
)


class ListApiKeysPaginator(Boto3Paginator):
    """
    Paginator for `list_api_keys`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, apiId: str, PaginationConfig: ListApiKeysPaginatePaginationConfigTypeDef = None
    ) -> ListApiKeysPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`AppSync.Client.list_api_keys`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/appsync-2017-07-25/ListApiKeys>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              apiId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type apiId: string
        :param apiId: **[REQUIRED]**

          The API ID.

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
                'apiKeys': [
                    {
                        'id': 'string',
                        'description': 'string',
                        'expires': 123
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **apiKeys** *(list) --*

              The ``ApiKey`` objects.

              - *(dict) --*

                Describes an API key.

                Customers invoke AWS AppSync GraphQL API operations with API keys as an identity
                mechanism. There are two key versions:

                 **da1** : This version was introduced at launch in November 2017. These keys always
                 expire after 7 days. Key expiration is managed by Amazon DynamoDB TTL. The keys
                 ceased to be valid after February 21, 2018 and should not be used after that date.

                * ``ListApiKeys`` returns the expiration time in milliseconds.

                * ``CreateApiKey`` returns the expiration time in milliseconds.

                * ``UpdateApiKey`` is not available for this key version.

                * ``DeleteApiKey`` deletes the item from the table.

                * Expiration is stored in Amazon DynamoDB as milliseconds. This results in a bug
                where keys are not automatically deleted because DynamoDB expects the TTL to be
                stored in seconds. As a one-time action, we will delete these keys from the table
                after February 21, 2018.

                 **da2** : This version was introduced in February 2018 when AppSync added support
                 to extend key expiration.

                * ``ListApiKeys`` returns the expiration time in seconds.

                * ``CreateApiKey`` returns the expiration time in seconds and accepts a
                user-provided expiration time in seconds.

                * ``UpdateApiKey`` returns the expiration time in seconds and accepts a
                user-provided expiration time in seconds. Key expiration can only be updated while
                the key has not expired.

                * ``DeleteApiKey`` deletes the item from the table.

                * Expiration is stored in Amazon DynamoDB as seconds.

                - **id** *(string) --*

                  The API key ID.

                - **description** *(string) --*

                  A description of the purpose of the API key.

                - **expires** *(integer) --*

                  The time after which the API key expires. The date is represented as seconds since
                  the epoch, rounded down to the nearest hour.

            - **NextToken** *(string) --*

              A token to resume pagination.
        """


class ListDataSourcesPaginator(Boto3Paginator):
    """
    Paginator for `list_data_sources`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, apiId: str, PaginationConfig: ListDataSourcesPaginatePaginationConfigTypeDef = None
    ) -> ListDataSourcesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`AppSync.Client.list_data_sources`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/appsync-2017-07-25/ListDataSources>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              apiId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type apiId: string
        :param apiId: **[REQUIRED]**

          The API ID.

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
                'dataSources': [
                    {
                        'dataSourceArn': 'string',
                        'name': 'string',
                        'description': 'string',
                        'type':
                        'AWS_LAMBDA'|'AMAZON_DYNAMODB'|'AMAZON_ELASTICSEARCH'|'NONE'
                        |'HTTP'|'RELATIONAL_DATABASE',
                        'serviceRoleArn': 'string',
                        'dynamodbConfig': {
                            'tableName': 'string',
                            'awsRegion': 'string',
                            'useCallerCredentials': True|False,
                            'deltaSyncConfig': {
                                'baseTableTTL': 123,
                                'deltaSyncTableName': 'string',
                                'deltaSyncTableTTL': 123
                            },
                            'versioned': True|False
                        },
                        'lambdaConfig': {
                            'lambdaFunctionArn': 'string'
                        },
                        'elasticsearchConfig': {
                            'endpoint': 'string',
                            'awsRegion': 'string'
                        },
                        'httpConfig': {
                            'endpoint': 'string',
                            'authorizationConfig': {
                                'authorizationType': 'AWS_IAM',
                                'awsIamConfig': {
                                    'signingRegion': 'string',
                                    'signingServiceName': 'string'
                                }
                            }
                        },
                        'relationalDatabaseConfig': {
                            'relationalDatabaseSourceType': 'RDS_HTTP_ENDPOINT',
                            'rdsHttpEndpointConfig': {
                                'awsRegion': 'string',
                                'dbClusterIdentifier': 'string',
                                'databaseName': 'string',
                                'schema': 'string',
                                'awsSecretStoreArn': 'string'
                            }
                        }
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **dataSources** *(list) --*

              The ``DataSource`` objects.

              - *(dict) --*

                Describes a data source.

                - **dataSourceArn** *(string) --*

                  The data source ARN.

                - **name** *(string) --*

                  The name of the data source.

                - **description** *(string) --*

                  The description of the data source.

                - **type** *(string) --*

                  The type of the data source.

                  * **AMAZON_DYNAMODB** : The data source is an Amazon DynamoDB table.

                  * **AMAZON_ELASTICSEARCH** : The data source is an Amazon Elasticsearch Service
                  domain.

                  * **AWS_LAMBDA** : The data source is an AWS Lambda function.

                  * **NONE** : There is no data source. This type is used when you wish to invoke a
                  GraphQL operation without connecting to a data source, such as performing data
                  transformation with resolvers or triggering a subscription to be invoked from a
                  mutation.

                  * **HTTP** : The data source is an HTTP endpoint.

                  * **RELATIONAL_DATABASE** : The data source is a relational database.

                - **serviceRoleArn** *(string) --*

                  The AWS IAM service role ARN for the data source. The system assumes this role
                  when accessing the data source.

                - **dynamodbConfig** *(dict) --*

                  Amazon DynamoDB settings.

                  - **tableName** *(string) --*

                    The table name.

                  - **awsRegion** *(string) --*

                    The AWS Region.

                  - **useCallerCredentials** *(boolean) --*

                    Set to TRUE to use Amazon Cognito credentials with this data source.

                  - **deltaSyncConfig** *(dict) --*

                    The ``DeltaSyncConfig`` for a versioned datasource.

                    - **baseTableTTL** *(integer) --*

                      The number of minutes an Item is stored in the datasource.

                    - **deltaSyncTableName** *(string) --*

                      The Delta Sync table name.

                    - **deltaSyncTableTTL** *(integer) --*

                      The number of minutes a Delta Sync log entry is stored in the Delta Sync
                      table.

                  - **versioned** *(boolean) --*

                    Set to TRUE to use Conflict Detection and Resolution with this data source.

                - **lambdaConfig** *(dict) --*

                  AWS Lambda settings.

                  - **lambdaFunctionArn** *(string) --*

                    The ARN for the Lambda function.

                - **elasticsearchConfig** *(dict) --*

                  Amazon Elasticsearch Service settings.

                  - **endpoint** *(string) --*

                    The endpoint.

                  - **awsRegion** *(string) --*

                    The AWS Region.

                - **httpConfig** *(dict) --*

                  HTTP endpoint settings.

                  - **endpoint** *(string) --*

                    The HTTP URL endpoint. You can either specify the domain name or IP, and port
                    combination, and the URL scheme must be HTTP or HTTPS. If the port is not
                    specified, AWS AppSync uses the default port 80 for the HTTP endpoint and port
                    443 for HTTPS endpoints.

                  - **authorizationConfig** *(dict) --*

                    The authorization config in case the HTTP endpoint requires authorization.

                    - **authorizationType** *(string) --*

                      The authorization type required by the HTTP endpoint.

                      * **AWS_IAM** : The authorization type is Sigv4.

                    - **awsIamConfig** *(dict) --*

                      The AWS IAM settings.

                      - **signingRegion** *(string) --*

                        The signing region for AWS IAM authorization.

                      - **signingServiceName** *(string) --*

                        The signing service name for AWS IAM authorization.

                - **relationalDatabaseConfig** *(dict) --*

                  Relational database settings.

                  - **relationalDatabaseSourceType** *(string) --*

                    Source type for the relational database.

                    * **RDS_HTTP_ENDPOINT** : The relational database source type is an Amazon RDS
                    HTTP endpoint.

                  - **rdsHttpEndpointConfig** *(dict) --*

                    Amazon RDS HTTP endpoint settings.

                    - **awsRegion** *(string) --*

                      AWS Region for RDS HTTP endpoint.

                    - **dbClusterIdentifier** *(string) --*

                      Amazon RDS cluster identifier.

                    - **databaseName** *(string) --*

                      Logical database name.

                    - **schema** *(string) --*

                      Logical schema name.

                    - **awsSecretStoreArn** *(string) --*

                      AWS secret store ARN for database credentials.

            - **NextToken** *(string) --*

              A token to resume pagination.
        """


class ListFunctionsPaginator(Boto3Paginator):
    """
    Paginator for `list_functions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, apiId: str, PaginationConfig: ListFunctionsPaginatePaginationConfigTypeDef = None
    ) -> ListFunctionsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`AppSync.Client.list_functions`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/appsync-2017-07-25/ListFunctions>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              apiId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type apiId: string
        :param apiId: **[REQUIRED]**

          The GraphQL API ID.

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
                'functions': [
                    {
                        'functionId': 'string',
                        'functionArn': 'string',
                        'name': 'string',
                        'description': 'string',
                        'dataSourceName': 'string',
                        'requestMappingTemplate': 'string',
                        'responseMappingTemplate': 'string',
                        'functionVersion': 'string'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **functions** *(list) --*

              A list of ``Function`` objects.

              - *(dict) --*

                A function is a reusable entity. Multiple functions can be used to compose the
                resolver logic.

                - **functionId** *(string) --*

                  A unique ID representing the ``Function`` object.

                - **functionArn** *(string) --*

                  The ARN of the ``Function`` object.

                - **name** *(string) --*

                  The name of the ``Function`` object.

                - **description** *(string) --*

                  The ``Function`` description.

                - **dataSourceName** *(string) --*

                  The name of the ``DataSource`` .

                - **requestMappingTemplate** *(string) --*

                  The ``Function`` request mapping template. Functions support only the 2018-05-29
                  version of the request mapping template.

                - **responseMappingTemplate** *(string) --*

                  The ``Function`` response mapping template.

                - **functionVersion** *(string) --*

                  The version of the request mapping template. Currently only the 2018-05-29 version
                  of the template is supported.

            - **NextToken** *(string) --*

              A token to resume pagination.
        """


class ListGraphqlApisPaginator(Boto3Paginator):
    """
    Paginator for `list_graphql_apis`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListGraphqlApisPaginatePaginationConfigTypeDef = None
    ) -> ListGraphqlApisPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`AppSync.Client.list_graphql_apis`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/appsync-2017-07-25/ListGraphqlApis>`_

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
                'graphqlApis': [
                    {
                        'name': 'string',
                        'apiId': 'string',
                        'authenticationType':
                        'API_KEY'|'AWS_IAM'|'AMAZON_COGNITO_USER_POOLS'
                        |'OPENID_CONNECT',
                        'logConfig': {
                            'fieldLogLevel': 'NONE'|'ERROR'|'ALL',
                            'cloudWatchLogsRoleArn': 'string',
                            'excludeVerboseContent': True|False
                        },
                        'userPoolConfig': {
                            'userPoolId': 'string',
                            'awsRegion': 'string',
                            'defaultAction': 'ALLOW'|'DENY',
                            'appIdClientRegex': 'string'
                        },
                        'openIDConnectConfig': {
                            'issuer': 'string',
                            'clientId': 'string',
                            'iatTTL': 123,
                            'authTTL': 123
                        },
                        'arn': 'string',
                        'uris': {
                            'string': 'string'
                        },
                        'tags': {
                            'string': 'string'
                        },
                        'additionalAuthenticationProviders': [
                            {
                                'authenticationType':
                                'API_KEY'|'AWS_IAM'
                                |'AMAZON_COGNITO_USER_POOLS'
                                |'OPENID_CONNECT',
                                'openIDConnectConfig': {
                                    'issuer': 'string',
                                    'clientId': 'string',
                                    'iatTTL': 123,
                                    'authTTL': 123
                                },
                                'userPoolConfig': {
                                    'userPoolId': 'string',
                                    'awsRegion': 'string',
                                    'appIdClientRegex': 'string'
                                }
                            },
                        ]
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **graphqlApis** *(list) --*

              The ``GraphqlApi`` objects.

              - *(dict) --*

                Describes a GraphQL API.

                - **name** *(string) --*

                  The API name.

                - **apiId** *(string) --*

                  The API ID.

                - **authenticationType** *(string) --*

                  The authentication type.

                - **logConfig** *(dict) --*

                  The Amazon CloudWatch Logs configuration.

                  - **fieldLogLevel** *(string) --*

                    The field logging level. Values can be NONE, ERROR, or ALL.

                    * **NONE** : No field-level logs are captured.

                    * **ERROR** : Logs the following information only for the fields that are in
                    error:

                      * The error section in the server response.

                      * Field-level errors.

                      * The generated request/response functions that got resolved for error fields.

                    * **ALL** : The following information is logged for all fields in the query:

                      * Field-level tracing information.

                      * The generated request/response functions that got resolved for each field.

                  - **cloudWatchLogsRoleArn** *(string) --*

                    The service role that AWS AppSync will assume to publish to Amazon CloudWatch
                    logs in your account.

                  - **excludeVerboseContent** *(boolean) --*

                    Set to TRUE to exclude sections that contain information such as headers,
                    context, and evaluated mapping templates, regardless of logging level.

                - **userPoolConfig** *(dict) --*

                  The Amazon Cognito user pool configuration.

                  - **userPoolId** *(string) --*

                    The user pool ID.

                  - **awsRegion** *(string) --*

                    The AWS Region in which the user pool was created.

                  - **defaultAction** *(string) --*

                    The action that you want your GraphQL API to take when a request that uses
                    Amazon Cognito user pool authentication doesn't match the Amazon Cognito user
                    pool configuration.

                  - **appIdClientRegex** *(string) --*

                    A regular expression for validating the incoming Amazon Cognito user pool app
                    client ID.

                - **openIDConnectConfig** *(dict) --*

                  The OpenID Connect configuration.

                  - **issuer** *(string) --*

                    The issuer for the OpenID Connect configuration. The issuer returned by
                    discovery must exactly match the value of ``iss`` in the ID token.

                  - **clientId** *(string) --*

                    The client identifier of the Relying party at the OpenID identity provider. This
                    identifier is typically obtained when the Relying party is registered with the
                    OpenID identity provider. You can specify a regular expression so the AWS
                    AppSync can validate against multiple client identifiers at a time.

                  - **iatTTL** *(integer) --*

                    The number of milliseconds a token is valid after being issued to a user.

                  - **authTTL** *(integer) --*

                    The number of milliseconds a token is valid after being authenticated.

                - **arn** *(string) --*

                  The ARN.

                - **uris** *(dict) --*

                  The URIs.

                  - *(string) --*

                    - *(string) --*

                - **tags** *(dict) --*

                  The tags.

                  - *(string) --*

                    The key for the tag.

                    - *(string) --*

                      The value for the tag.

                - **additionalAuthenticationProviders** *(list) --*

                  A list of additional authentication providers for the ``GraphqlApi`` API.

                  - *(dict) --*

                    Describes an additional authentication provider.

                    - **authenticationType** *(string) --*

                      The authentication type: API key, AWS IAM, OIDC, or Amazon Cognito user pools.

                    - **openIDConnectConfig** *(dict) --*

                      The OpenID Connect configuration.

                      - **issuer** *(string) --*

                        The issuer for the OpenID Connect configuration. The issuer returned by
                        discovery must exactly match the value of ``iss`` in the ID token.

                      - **clientId** *(string) --*

                        The client identifier of the Relying party at the OpenID identity provider.
                        This identifier is typically obtained when the Relying party is registered
                        with the OpenID identity provider. You can specify a regular expression so
                        the AWS AppSync can validate against multiple client identifiers at a time.

                      - **iatTTL** *(integer) --*

                        The number of milliseconds a token is valid after being issued to a user.

                      - **authTTL** *(integer) --*

                        The number of milliseconds a token is valid after being authenticated.

                    - **userPoolConfig** *(dict) --*

                      The Amazon Cognito user pool configuration.

                      - **userPoolId** *(string) --*

                        The user pool ID.

                      - **awsRegion** *(string) --*

                        The AWS Region in which the user pool was created.

                      - **appIdClientRegex** *(string) --*

                        A regular expression for validating the incoming Amazon Cognito user pool
                        app client ID.

            - **NextToken** *(string) --*

              A token to resume pagination.
        """


class ListResolversPaginator(Boto3Paginator):
    """
    Paginator for `list_resolvers`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        apiId: str,
        typeName: str,
        PaginationConfig: ListResolversPaginatePaginationConfigTypeDef = None,
    ) -> ListResolversPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`AppSync.Client.list_resolvers`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/appsync-2017-07-25/ListResolvers>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              apiId='string',
              typeName='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type apiId: string
        :param apiId: **[REQUIRED]**

          The API ID.

        :type typeName: string
        :param typeName: **[REQUIRED]**

          The type name.

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
                'resolvers': [
                    {
                        'typeName': 'string',
                        'fieldName': 'string',
                        'dataSourceName': 'string',
                        'resolverArn': 'string',
                        'requestMappingTemplate': 'string',
                        'responseMappingTemplate': 'string',
                        'kind': 'UNIT'|'PIPELINE',
                        'pipelineConfig': {
                            'functions': [
                                'string',
                            ]
                        },
                        'syncConfig': {
                            'conflictHandler': 'OPTIMISTIC_CONCURRENCY'|'LAMBDA'|'AUTOMERGE'|'NONE',
                            'conflictDetection': 'VERSION'|'NONE',
                            'lambdaConflictHandlerConfig': {
                                'lambdaConflictHandlerArn': 'string'
                            }
                        },
                        'cachingConfig': {
                            'ttl': 123,
                            'cachingKeys': [
                                'string',
                            ]
                        }
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **resolvers** *(list) --*

              The ``Resolver`` objects.

              - *(dict) --*

                Describes a resolver.

                - **typeName** *(string) --*

                  The resolver type name.

                - **fieldName** *(string) --*

                  The resolver field name.

                - **dataSourceName** *(string) --*

                  The resolver data source name.

                - **resolverArn** *(string) --*

                  The resolver ARN.

                - **requestMappingTemplate** *(string) --*

                  The request mapping template.

                - **responseMappingTemplate** *(string) --*

                  The response mapping template.

                - **kind** *(string) --*

                  The resolver type.

                  * **UNIT** : A UNIT resolver type. A UNIT resolver is the default resolver type. A
                  UNIT resolver enables you to execute a GraphQL query against a single data source.

                  * **PIPELINE** : A PIPELINE resolver type. A PIPELINE resolver enables you to
                  execute a series of ``Function`` in a serial manner. You can use a pipeline
                  resolver to execute a GraphQL query against multiple data sources.

                - **pipelineConfig** *(dict) --*

                  The ``PipelineConfig`` .

                  - **functions** *(list) --*

                    A list of ``Function`` objects.

                    - *(string) --*

                - **syncConfig** *(dict) --*

                  The ``SyncConfig`` for a resolver attached to a versioned datasource.

                  - **conflictHandler** *(string) --*

                    The Conflict Resolution strategy to perform in the event of a conflict.

                    * **OPTIMISTIC_CONCURRENCY** : Resolve conflicts by rejecting mutations when
                    versions do not match the latest version at the server.

                    * **AUTOMERGE** : Resolve conflicts with the Automerge conflict resolution
                    strategy.

                    * **LAMBDA** : Resolve conflicts with a Lambda function supplied in the
                    LambdaConflictHandlerConfig.

                  - **conflictDetection** *(string) --*

                    The Conflict Detection strategy to use.

                    * **VERSION** : Detect conflicts based on object versions for this resolver.

                    * **NONE** : Do not detect conflicts when executing this resolver.

                  - **lambdaConflictHandlerConfig** *(dict) --*

                    The ``LambdaConflictHandlerConfig`` when configuring LAMBDA as the Conflict
                    Handler.

                    - **lambdaConflictHandlerArn** *(string) --*

                      The Arn for the Lambda function to use as the Conflict Handler.

                - **cachingConfig** *(dict) --*

                  The caching configuration for the resolver.

                  - **ttl** *(integer) --*

                    The TTL in seconds for a resolver that has caching enabled.

                    Valid values are between 1 and 3600 seconds.

                  - **cachingKeys** *(list) --*

                    The caching keys for a resolver that has caching enabled.

                    Valid values are entries from the ``$context.identity`` and
                    ``$context.arguments`` maps.

                    - *(string) --*

            - **NextToken** *(string) --*

              A token to resume pagination.
        """


class ListResolversByFunctionPaginator(Boto3Paginator):
    """
    Paginator for `list_resolvers_by_function`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        apiId: str,
        functionId: str,
        PaginationConfig: ListResolversByFunctionPaginatePaginationConfigTypeDef = None,
    ) -> ListResolversByFunctionPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`AppSync.Client.list_resolvers_by_function`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/appsync-2017-07-25/ListResolversByFunction>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              apiId='string',
              functionId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type apiId: string
        :param apiId: **[REQUIRED]**

          The API ID.

        :type functionId: string
        :param functionId: **[REQUIRED]**

          The Function ID.

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
                'resolvers': [
                    {
                        'typeName': 'string',
                        'fieldName': 'string',
                        'dataSourceName': 'string',
                        'resolverArn': 'string',
                        'requestMappingTemplate': 'string',
                        'responseMappingTemplate': 'string',
                        'kind': 'UNIT'|'PIPELINE',
                        'pipelineConfig': {
                            'functions': [
                                'string',
                            ]
                        },
                        'syncConfig': {
                            'conflictHandler': 'OPTIMISTIC_CONCURRENCY'|'LAMBDA'|'AUTOMERGE'|'NONE',
                            'conflictDetection': 'VERSION'|'NONE',
                            'lambdaConflictHandlerConfig': {
                                'lambdaConflictHandlerArn': 'string'
                            }
                        },
                        'cachingConfig': {
                            'ttl': 123,
                            'cachingKeys': [
                                'string',
                            ]
                        }
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **resolvers** *(list) --*

              The list of resolvers.

              - *(dict) --*

                Describes a resolver.

                - **typeName** *(string) --*

                  The resolver type name.

                - **fieldName** *(string) --*

                  The resolver field name.

                - **dataSourceName** *(string) --*

                  The resolver data source name.

                - **resolverArn** *(string) --*

                  The resolver ARN.

                - **requestMappingTemplate** *(string) --*

                  The request mapping template.

                - **responseMappingTemplate** *(string) --*

                  The response mapping template.

                - **kind** *(string) --*

                  The resolver type.

                  * **UNIT** : A UNIT resolver type. A UNIT resolver is the default resolver type. A
                  UNIT resolver enables you to execute a GraphQL query against a single data source.

                  * **PIPELINE** : A PIPELINE resolver type. A PIPELINE resolver enables you to
                  execute a series of ``Function`` in a serial manner. You can use a pipeline
                  resolver to execute a GraphQL query against multiple data sources.

                - **pipelineConfig** *(dict) --*

                  The ``PipelineConfig`` .

                  - **functions** *(list) --*

                    A list of ``Function`` objects.

                    - *(string) --*

                - **syncConfig** *(dict) --*

                  The ``SyncConfig`` for a resolver attached to a versioned datasource.

                  - **conflictHandler** *(string) --*

                    The Conflict Resolution strategy to perform in the event of a conflict.

                    * **OPTIMISTIC_CONCURRENCY** : Resolve conflicts by rejecting mutations when
                    versions do not match the latest version at the server.

                    * **AUTOMERGE** : Resolve conflicts with the Automerge conflict resolution
                    strategy.

                    * **LAMBDA** : Resolve conflicts with a Lambda function supplied in the
                    LambdaConflictHandlerConfig.

                  - **conflictDetection** *(string) --*

                    The Conflict Detection strategy to use.

                    * **VERSION** : Detect conflicts based on object versions for this resolver.

                    * **NONE** : Do not detect conflicts when executing this resolver.

                  - **lambdaConflictHandlerConfig** *(dict) --*

                    The ``LambdaConflictHandlerConfig`` when configuring LAMBDA as the Conflict
                    Handler.

                    - **lambdaConflictHandlerArn** *(string) --*

                      The Arn for the Lambda function to use as the Conflict Handler.

                - **cachingConfig** *(dict) --*

                  The caching configuration for the resolver.

                  - **ttl** *(integer) --*

                    The TTL in seconds for a resolver that has caching enabled.

                    Valid values are between 1 and 3600 seconds.

                  - **cachingKeys** *(list) --*

                    The caching keys for a resolver that has caching enabled.

                    Valid values are entries from the ``$context.identity`` and
                    ``$context.arguments`` maps.

                    - *(string) --*

            - **NextToken** *(string) --*

              A token to resume pagination.
        """


class ListTypesPaginator(Boto3Paginator):
    """
    Paginator for `list_types`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        apiId: str,
        format: Literal["SDL", "JSON"],
        PaginationConfig: ListTypesPaginatePaginationConfigTypeDef = None,
    ) -> ListTypesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`AppSync.Client.list_types`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/appsync-2017-07-25/ListTypes>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              apiId='string',
              format='SDL'|'JSON',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type apiId: string
        :param apiId: **[REQUIRED]**

          The API ID.

        :type format: string
        :param format: **[REQUIRED]**

          The type format: SDL or JSON.

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
                'types': [
                    {
                        'name': 'string',
                        'description': 'string',
                        'arn': 'string',
                        'definition': 'string',
                        'format': 'SDL'|'JSON'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            - **types** *(list) --*

              The ``Type`` objects.

              - *(dict) --*

                Describes a type.

                - **name** *(string) --*

                  The type name.

                - **description** *(string) --*

                  The type description.

                - **arn** *(string) --*

                  The type ARN.

                - **definition** *(string) --*

                  The type definition.

                - **format** *(string) --*

                  The type format: SDL or JSON.

            - **NextToken** *(string) --*

              A token to resume pagination.
        """
