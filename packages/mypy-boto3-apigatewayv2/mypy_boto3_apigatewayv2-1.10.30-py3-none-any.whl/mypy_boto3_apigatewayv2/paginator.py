"Main interface for apigatewayv2 service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_apigatewayv2.type_defs import (
    GetApisPaginatePaginationConfigTypeDef,
    GetApisPaginateResponseTypeDef,
    GetAuthorizersPaginatePaginationConfigTypeDef,
    GetAuthorizersPaginateResponseTypeDef,
    GetDeploymentsPaginatePaginationConfigTypeDef,
    GetDeploymentsPaginateResponseTypeDef,
    GetDomainNamesPaginatePaginationConfigTypeDef,
    GetDomainNamesPaginateResponseTypeDef,
    GetIntegrationResponsesPaginatePaginationConfigTypeDef,
    GetIntegrationResponsesPaginateResponseTypeDef,
    GetIntegrationsPaginatePaginationConfigTypeDef,
    GetIntegrationsPaginateResponseTypeDef,
    GetModelsPaginatePaginationConfigTypeDef,
    GetModelsPaginateResponseTypeDef,
    GetRouteResponsesPaginatePaginationConfigTypeDef,
    GetRouteResponsesPaginateResponseTypeDef,
    GetRoutesPaginatePaginationConfigTypeDef,
    GetRoutesPaginateResponseTypeDef,
    GetStagesPaginatePaginationConfigTypeDef,
    GetStagesPaginateResponseTypeDef,
)


__all__ = (
    "GetApisPaginator",
    "GetAuthorizersPaginator",
    "GetDeploymentsPaginator",
    "GetDomainNamesPaginator",
    "GetIntegrationResponsesPaginator",
    "GetIntegrationsPaginator",
    "GetModelsPaginator",
    "GetRouteResponsesPaginator",
    "GetRoutesPaginator",
    "GetStagesPaginator",
)


class GetApisPaginator(Boto3Paginator):
    """
    Paginator for `get_apis`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: GetApisPaginatePaginationConfigTypeDef = None
    ) -> GetApisPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`ApiGatewayV2.Client.get_apis`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/apigatewayv2-2018-11-29/GetApis>`_

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
                'Items': [
                    {
                        'ApiEndpoint': 'string',
                        'ApiId': 'string',
                        'ApiKeySelectionExpression': 'string',
                        'CreatedDate': datetime(2015, 1, 1),
                        'Description': 'string',
                        'DisableSchemaValidation': True|False,
                        'Name': 'string',
                        'ProtocolType': 'WEBSOCKET',
                        'RouteSelectionExpression': 'string',
                        'Version': 'string',
                        'Warnings': [
                            'string',
                        ],
                        'Tags': {
                            'string': 'string'
                        }
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            Success

            - **Items** *(list) --*

              The elements from this collection.

              - *(dict) --*

                Represents an API.

                - **ApiEndpoint** *(string) --*

                  The URI of the API, of the form {api-id}.execute-api.{region}.amazonaws.com. The
                  stage name is typically appended to this URI to form a complete path to a deployed
                  API stage.

                - **ApiId** *(string) --*

                  The API ID.

                - **ApiKeySelectionExpression** *(string) --*

                  An API key selection expression. See `API Key Selection Expressions
                  <https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-apikey-selection-expressions>`__
                  .

                - **CreatedDate** *(datetime) --*

                  The timestamp when the API was created.

                - **Description** *(string) --*

                  The description of the API.

                - **DisableSchemaValidation** *(boolean) --*

                  Avoid validating models when creating a deployment.

                - **Name** *(string) --*

                  The name of the API.

                - **ProtocolType** *(string) --*

                  The API protocol: Currently only WEBSOCKET is supported.

                - **RouteSelectionExpression** *(string) --*

                  The route selection expression for the API.

                - **Version** *(string) --*

                  A version identifier for the API.

                - **Warnings** *(list) --*

                  The warning messages reported when failonwarnings is turned on during API import.

                  - *(string) --*

                - **Tags** *(dict) --*

                  The key-value map of strings. The valid character set is [a-zA-Z+-=
                      ._:/]. The tag
                  key can be up to 128 characters and must not start with aws:. The tag value can be
                  up to 256 characters..

                  - *(string) --*

                    - *(string) --*

                      A string with a length between [1-1600].
        """


class GetAuthorizersPaginator(Boto3Paginator):
    """
    Paginator for `get_authorizers`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, ApiId: str, PaginationConfig: GetAuthorizersPaginatePaginationConfigTypeDef = None
    ) -> GetAuthorizersPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`ApiGatewayV2.Client.get_authorizers`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/apigatewayv2-2018-11-29/GetAuthorizers>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              ApiId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type ApiId: string
        :param ApiId: **[REQUIRED]**

          The API identifier.

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
                'Items': [
                    {
                        'AuthorizerCredentialsArn': 'string',
                        'AuthorizerId': 'string',
                        'AuthorizerResultTtlInSeconds': 123,
                        'AuthorizerType': 'REQUEST',
                        'AuthorizerUri': 'string',
                        'IdentitySource': [
                            'string',
                        ],
                        'IdentityValidationExpression': 'string',
                        'Name': 'string',
                        'ProviderArns': [
                            'string',
                        ]
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            Success

            - **Items** *(list) --*

              The elements from this collection.

              - *(dict) --*

                Represents an authorizer.

                - **AuthorizerCredentialsArn** *(string) --*

                  Specifies the required credentials as an IAM role for API Gateway to invoke the
                  authorizer. To specify an IAM role for API Gateway to assume, use the role's
                  Amazon Resource Name (ARN). To use resource-based permissions on the Lambda
                  function, specify null.

                - **AuthorizerId** *(string) --*

                  The authorizer identifier.

                - **AuthorizerResultTtlInSeconds** *(integer) --*

                  The time to live (TTL), in seconds, of cached authorizer results. If it equals 0,
                  authorization caching is disabled. If it is greater than 0, API Gateway will cache
                  authorizer responses. If this field is not set, the default value is 300. The
                  maximum value is 3600, or 1 hour.

                - **AuthorizerType** *(string) --*

                  The authorizer type. Currently the only valid value is REQUEST, for a Lambda
                  function using incoming request parameters.

                - **AuthorizerUri** *(string) --*

                  The authorizer's Uniform Resource Identifier (URI). ForREQUEST authorizers, this
                  must be a well-formed Lambda function URI, for example,
                  arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:{account_id}:function:{lambda_function_name}/invocations.
                  In general, the URI has this form:
                  arn:aws:apigateway:{region}:lambda:path/{service_api} , where {region} is the same
                  as the region hosting the Lambda function, path indicates that the remaining
                  substring in the URI should be treated as the path to the resource, including the
                  initial /. For Lambda functions, this is usually of the form
                  /2015-03-31/functions/[FunctionARN]/invocations.

                - **IdentitySource** *(list) --*

                  The identity source for which authorization is requested.

                  For the REQUEST authorizer, this is required when authorization caching is
                  enabled. The value is a comma-separated string of one or more mapping expressions
                  of the specified request parameters. For example, if an Auth header and a Name
                  query string parameters are defined as identity sources, this value is
                  method.request.header.Auth, method.request.querystring.Name. These parameters will
                  be used to derive the authorization caching key and to perform runtime validation
                  of the REQUEST authorizer by verifying all of the identity-related request
                  parameters are present, not null, and non-empty. Only when this is true does the
                  authorizer invoke the authorizer Lambda function, otherwise, it returns a 401
                  Unauthorized response without calling the Lambda function. The valid value is a
                  string of comma-separated mapping expressions of the specified request parameters.
                  When the authorization caching is not enabled, this property is optional.

                  - *(string) --*

                - **IdentityValidationExpression** *(string) --*

                  The validation expression does not apply to the REQUEST authorizer.

                - **Name** *(string) --*

                  The name of the authorizer.

                - **ProviderArns** *(list) --*

                  For REQUEST authorizer, this is not defined.

                  - *(string) --*

                    Represents an Amazon Resource Name (ARN).
        """


class GetDeploymentsPaginator(Boto3Paginator):
    """
    Paginator for `get_deployments`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, ApiId: str, PaginationConfig: GetDeploymentsPaginatePaginationConfigTypeDef = None
    ) -> GetDeploymentsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`ApiGatewayV2.Client.get_deployments`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/apigatewayv2-2018-11-29/GetDeployments>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              ApiId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type ApiId: string
        :param ApiId: **[REQUIRED]**

          The API identifier.

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
                'Items': [
                    {
                        'CreatedDate': datetime(2015, 1, 1),
                        'DeploymentId': 'string',
                        'DeploymentStatus': 'PENDING'|'FAILED'|'DEPLOYED',
                        'DeploymentStatusMessage': 'string',
                        'Description': 'string'
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            Success

            - **Items** *(list) --*

              The elements from this collection.

              - *(dict) --*

                An immutable representation of an API that can be called by users. A Deployment must
                be associated with a Stage for it to be callable over the internet.

                - **CreatedDate** *(datetime) --*

                  The date and time when the Deployment resource was created.

                - **DeploymentId** *(string) --*

                  The identifier for the deployment.

                - **DeploymentStatus** *(string) --*

                  The status of the deployment: PENDING, FAILED, or SUCCEEDED.

                - **DeploymentStatusMessage** *(string) --*

                  May contain additional feedback on the status of an API deployment.

                - **Description** *(string) --*

                  The description for the deployment.
        """


class GetDomainNamesPaginator(Boto3Paginator):
    """
    Paginator for `get_domain_names`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: GetDomainNamesPaginatePaginationConfigTypeDef = None
    ) -> GetDomainNamesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`ApiGatewayV2.Client.get_domain_names`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/apigatewayv2-2018-11-29/GetDomainNames>`_

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
                'Items': [
                    {
                        'ApiMappingSelectionExpression': 'string',
                        'DomainName': 'string',
                        'DomainNameConfigurations': [
                            {
                                'ApiGatewayDomainName': 'string',
                                'CertificateArn': 'string',
                                'CertificateName': 'string',
                                'CertificateUploadDate': datetime(2015, 1, 1),
                                'EndpointType': 'REGIONAL'|'EDGE',
                                'HostedZoneId': 'string',
                                'SecurityPolicy': 'TLS_1_0'|'TLS_1_2',
                                'DomainNameStatus': 'AVAILABLE'|'UPDATING',
                                'DomainNameStatusMessage': 'string'
                            },
                        ],
                        'Tags': {
                            'string': 'string'
                        }
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            Success

            - **Items** *(list) --*

              The elements from this collection.

              - *(dict) --*

                Represents a domain name.

                - **ApiMappingSelectionExpression** *(string) --*

                  The API mapping selection expression.

                - **DomainName** *(string) --*

                  The name of the DomainName resource.

                - **DomainNameConfigurations** *(list) --*

                  The domain name configurations.

                  - *(dict) --*

                    The domain name configuration.

                    - **ApiGatewayDomainName** *(string) --*

                      A domain name for the WebSocket API.

                    - **CertificateArn** *(string) --*

                      An AWS-managed certificate that will be used by the edge-optimized endpoint
                      for this domain name. AWS Certificate Manager is the only supported source.

                    - **CertificateName** *(string) --*

                      The user-friendly name of the certificate that will be used by the
                      edge-optimized endpoint for this domain name.

                    - **CertificateUploadDate** *(datetime) --*

                      The timestamp when the certificate that was used by edge-optimized endpoint
                      for this domain name was uploaded.

                    - **EndpointType** *(string) --*

                      The endpoint type.

                    - **HostedZoneId** *(string) --*

                      The Amazon Route 53 Hosted Zone ID of the endpoint.

                    - **SecurityPolicy** *(string) --*

                      The Transport Layer Security (TLS) version of the security policy for this
                      domain name. The valid values are TLS_1_0 and TLS_1_2.

                    - **DomainNameStatus** *(string) --*

                      The status of the domain name migration. The valid values are AVAILABLE and
                      UPDATING. If the status is UPDATING, the domain cannot be modified further
                      until the existing operation is complete. If it is AVAILABLE, the domain can
                      be updated.

                    - **DomainNameStatusMessage** *(string) --*

                      An optional text message containing detailed information about status of the
                      domain name migration.

                - **Tags** *(dict) --*

                  The key-value map of strings. The valid character set is [a-zA-Z+-=
                      ._:/]. The tag
                  key can be up to 128 characters and must not start with aws:. The tag value can be
                  up to 256 characters..

                  - *(string) --*

                    - *(string) --*

                      A string with a length between [1-1600].
        """


class GetIntegrationResponsesPaginator(Boto3Paginator):
    """
    Paginator for `get_integration_responses`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ApiId: str,
        IntegrationId: str,
        PaginationConfig: GetIntegrationResponsesPaginatePaginationConfigTypeDef = None,
    ) -> GetIntegrationResponsesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`ApiGatewayV2.Client.get_integration_responses`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/apigatewayv2-2018-11-29/GetIntegrationResponses>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              ApiId='string',
              IntegrationId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type ApiId: string
        :param ApiId: **[REQUIRED]**

          The API identifier.

        :type IntegrationId: string
        :param IntegrationId: **[REQUIRED]**

          The integration ID.

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
                'Items': [
                    {
                        'ContentHandlingStrategy': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT',
                        'IntegrationResponseId': 'string',
                        'IntegrationResponseKey': 'string',
                        'ResponseParameters': {
                            'string': 'string'
                        },
                        'ResponseTemplates': {
                            'string': 'string'
                        },
                        'TemplateSelectionExpression': 'string'
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            Success

            - **Items** *(list) --*

              The elements from this collection.

              - *(dict) --*

                Represents an integration response.

                - **ContentHandlingStrategy** *(string) --*

                  Specifies how to handle response payload content type conversions. Supported
                  values are CONVERT_TO_BINARY and CONVERT_TO_TEXT, with the following behaviors:

                  CONVERT_TO_BINARY: Converts a response payload from a Base64-encoded string to the
                  corresponding binary blob.

                  CONVERT_TO_TEXT: Converts a response payload from a binary blob to a
                  Base64-encoded string.

                  If this property is not defined, the response payload will be passed through from
                  the integration response to the route response or method response without
                  modification.

                - **IntegrationResponseId** *(string) --*

                  The integration response ID.

                - **IntegrationResponseKey** *(string) --*

                  The integration response key.

                - **ResponseParameters** *(dict) --*

                  A key-value map specifying response parameters that are passed to the method
                  response from the backend. The key is a method response header parameter name and
                  the mapped value is an integration response header value, a static value enclosed
                  within a pair of single quotes, or a JSON expression from the integration response
                  body. The mapping key must match the pattern of method.response.header.{name},
                  where name is a valid and unique header name. The mapped non-static value must
                  match the pattern of integration.response.header.{name} or
                  integration.response.body.{JSON-expression}, where name is a valid and unique
                  response header name and JSON-expression is a valid JSON expression without the $
                  prefix.

                  - *(string) --*

                    - *(string) --*

                      A string with a length between [1-512].

                - **ResponseTemplates** *(dict) --*

                  The collection of response templates for the integration response as a
                  string-to-string map of key-value pairs. Response templates are represented as a
                  key/value map, with a content-type as the key and a template as the value.

                  - *(string) --*

                    - *(string) --*

                      A string with a length between [0-32768].

                - **TemplateSelectionExpression** *(string) --*

                  The template selection expressions for the integration response.
        """


class GetIntegrationsPaginator(Boto3Paginator):
    """
    Paginator for `get_integrations`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, ApiId: str, PaginationConfig: GetIntegrationsPaginatePaginationConfigTypeDef = None
    ) -> GetIntegrationsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`ApiGatewayV2.Client.get_integrations`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/apigatewayv2-2018-11-29/GetIntegrations>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              ApiId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type ApiId: string
        :param ApiId: **[REQUIRED]**

          The API identifier.

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
                'Items': [
                    {
                        'ConnectionId': 'string',
                        'ConnectionType': 'INTERNET'|'VPC_LINK',
                        'ContentHandlingStrategy': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT',
                        'CredentialsArn': 'string',
                        'Description': 'string',
                        'IntegrationId': 'string',
                        'IntegrationMethod': 'string',
                        'IntegrationResponseSelectionExpression': 'string',
                        'IntegrationType': 'AWS'|'HTTP'|'MOCK'|'HTTP_PROXY'|'AWS_PROXY',
                        'IntegrationUri': 'string',
                        'PassthroughBehavior': 'WHEN_NO_MATCH'|'NEVER'|'WHEN_NO_TEMPLATES',
                        'RequestParameters': {
                            'string': 'string'
                        },
                        'RequestTemplates': {
                            'string': 'string'
                        },
                        'TemplateSelectionExpression': 'string',
                        'TimeoutInMillis': 123
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            Success

            - **Items** *(list) --*

              The elements from this collection.

              - *(dict) --*

                Represents an integration.

                - **ConnectionId** *(string) --*

                  The connection ID.

                - **ConnectionType** *(string) --*

                  The type of the network connection to the integration endpoint. Currently the only
                  valid value is INTERNET, for connections through the public routable internet.

                - **ContentHandlingStrategy** *(string) --*

                  Specifies how to handle response payload content type conversions. Supported
                  values are CONVERT_TO_BINARY and CONVERT_TO_TEXT, with the following behaviors:

                  CONVERT_TO_BINARY: Converts a response payload from a Base64-encoded string to the
                  corresponding binary blob.

                  CONVERT_TO_TEXT: Converts a response payload from a binary blob to a
                  Base64-encoded string.

                  If this property is not defined, the response payload will be passed through from
                  the integration response to the route response or method response without
                  modification.

                - **CredentialsArn** *(string) --*

                  Specifies the credentials required for the integration, if any. For AWS
                  integrations, three options are available. To specify an IAM Role for API Gateway
                  to assume, use the role's Amazon Resource Name (ARN). To require that the caller's
                  identity be passed through from the request, specify the string
                  arn:aws:iam::*:user/*. To use resource-based permissions on supported AWS
                  services, specify null.

                - **Description** *(string) --*

                  Represents the description of an integration.

                - **IntegrationId** *(string) --*

                  Represents the identifier of an integration.

                - **IntegrationMethod** *(string) --*

                  Specifies the integration's HTTP method type.

                - **IntegrationResponseSelectionExpression** *(string) --*

                  The integration response selection expression for the integration. See
                  `Integration Response Selection Expressions
                  <https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-integration-response-selection-expressions>`__
                  .

                - **IntegrationType** *(string) --*

                  The integration type of an integration. One of the following:

                  AWS: for integrating the route or method request with an AWS service action,
                  including the Lambda function-invoking action. With the Lambda function-invoking
                  action, this is referred to as the Lambda custom integration. With any other AWS
                  service action, this is known as AWS integration.

                  AWS_PROXY: for integrating the route or method request with the Lambda
                  function-invoking action with the client request passed through as-is. This
                  integration is also referred to as Lambda proxy integration.

                  HTTP: for integrating the route or method request with an HTTP endpoint. This
                  integration is also referred to as the HTTP custom integration.

                  HTTP_PROXY: for integrating route or method request with an HTTP endpoint, with
                  the client request passed through as-is. This is also referred to as HTTP proxy
                  integration.

                  MOCK: for integrating the route or method request with API Gateway as a "loopback"
                  endpoint without invoking any backend.

                - **IntegrationUri** *(string) --*

                  For a Lambda proxy integration, this is the URI of the Lambda function.

                - **PassthroughBehavior** *(string) --*

                  Specifies the pass-through behavior for incoming requests based on the
                  Content-Type header in the request, and the available mapping templates specified
                  as the requestTemplates property on the Integration resource. There are three
                  valid values: WHEN_NO_MATCH, WHEN_NO_TEMPLATES, and NEVER.

                  WHEN_NO_MATCH passes the request body for unmapped content types through to the
                  integration backend without transformation.

                  NEVER rejects unmapped content types with an HTTP 415 Unsupported Media Type
                  response.

                  WHEN_NO_TEMPLATES allows pass-through when the integration has no content types
                  mapped to templates. However, if there is at least one content type defined,
                  unmapped content types will be rejected with the same HTTP 415 Unsupported Media
                  Type response.

                - **RequestParameters** *(dict) --*

                  A key-value map specifying request parameters that are passed from the method
                  request to the backend. The key is an integration request parameter name and the
                  associated value is a method request parameter value or static value that must be
                  enclosed within single quotes and pre-encoded as required by the backend. The
                  method request parameter value must match the pattern of
                  method.request.{location}.{name} , where {location} is querystring, path, or
                  header; and {name} must be a valid and unique method request parameter name.

                  - *(string) --*

                    - *(string) --*

                      A string with a length between [1-512].

                - **RequestTemplates** *(dict) --*

                  Represents a map of Velocity templates that are applied on the request payload
                  based on the value of the Content-Type header sent by the client. The content type
                  value is the key in this map, and the template (as a String) is the value.

                  - *(string) --*

                    - *(string) --*

                      A string with a length between [0-32768].

                - **TemplateSelectionExpression** *(string) --*

                  The template selection expression for the integration.

                - **TimeoutInMillis** *(integer) --*

                  Custom timeout between 50 and 29,000 milliseconds. The default value is 29,000
                  milliseconds or 29 seconds.
        """


class GetModelsPaginator(Boto3Paginator):
    """
    Paginator for `get_models`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, ApiId: str, PaginationConfig: GetModelsPaginatePaginationConfigTypeDef = None
    ) -> GetModelsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`ApiGatewayV2.Client.get_models`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/apigatewayv2-2018-11-29/GetModels>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              ApiId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type ApiId: string
        :param ApiId: **[REQUIRED]**

          The API identifier.

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
                'Items': [
                    {
                        'ContentType': 'string',
                        'Description': 'string',
                        'ModelId': 'string',
                        'Name': 'string',
                        'Schema': 'string'
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            Success

            - **Items** *(list) --*

              The elements from this collection.

              - *(dict) --*

                Represents a data model for an API. See `Create Models and Mapping Templates for
                Request and Response Mappings
                <https://docs.aws.amazon.com/apigateway/latest/developerguide/models-mappings.html>`__
                .

                - **ContentType** *(string) --*

                  The content-type for the model, for example, "application/json".

                - **Description** *(string) --*

                  The description of the model.

                - **ModelId** *(string) --*

                  The model identifier.

                - **Name** *(string) --*

                  The name of the model. Must be alphanumeric.

                - **Schema** *(string) --*

                  The schema for the model. For application/json models, this should be JSON schema
                  draft 4 model.
        """


class GetRouteResponsesPaginator(Boto3Paginator):
    """
    Paginator for `get_route_responses`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ApiId: str,
        RouteId: str,
        PaginationConfig: GetRouteResponsesPaginatePaginationConfigTypeDef = None,
    ) -> GetRouteResponsesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`ApiGatewayV2.Client.get_route_responses`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/apigatewayv2-2018-11-29/GetRouteResponses>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              ApiId='string',
              RouteId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type ApiId: string
        :param ApiId: **[REQUIRED]**

          The API identifier.

        :type RouteId: string
        :param RouteId: **[REQUIRED]**

          The route ID.

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
                'Items': [
                    {
                        'ModelSelectionExpression': 'string',
                        'ResponseModels': {
                            'string': 'string'
                        },
                        'ResponseParameters': {
                            'string': {
                                'Required': True|False
                            }
                        },
                        'RouteResponseId': 'string',
                        'RouteResponseKey': 'string'
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            Success

            - **Items** *(list) --*

              The elements from this collection.

              - *(dict) --*

                Represents a route response.

                - **ModelSelectionExpression** *(string) --*

                  Represents the model selection expression of a route response.

                - **ResponseModels** *(dict) --*

                  Represents the response models of a route response.

                  - *(string) --*

                    - *(string) --*

                      A string with a length between [1-128].

                - **ResponseParameters** *(dict) --*

                  Represents the response parameters of a route response.

                  - *(string) --*

                    - *(dict) --*

                      Validation constraints imposed on parameters of a request (path, query string,
                      headers).

                      - **Required** *(boolean) --*

                        Whether or not the parameter is required.

                - **RouteResponseId** *(string) --*

                  Represents the identifier of a route response.

                - **RouteResponseKey** *(string) --*

                  Represents the route response key of a route response.
        """


class GetRoutesPaginator(Boto3Paginator):
    """
    Paginator for `get_routes`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, ApiId: str, PaginationConfig: GetRoutesPaginatePaginationConfigTypeDef = None
    ) -> GetRoutesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`ApiGatewayV2.Client.get_routes`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/apigatewayv2-2018-11-29/GetRoutes>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              ApiId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type ApiId: string
        :param ApiId: **[REQUIRED]**

          The API identifier.

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
                'Items': [
                    {
                        'ApiKeyRequired': True|False,
                        'AuthorizationScopes': [
                            'string',
                        ],
                        'AuthorizationType': 'NONE'|'AWS_IAM'|'CUSTOM',
                        'AuthorizerId': 'string',
                        'ModelSelectionExpression': 'string',
                        'OperationName': 'string',
                        'RequestModels': {
                            'string': 'string'
                        },
                        'RequestParameters': {
                            'string': {
                                'Required': True|False
                            }
                        },
                        'RouteId': 'string',
                        'RouteKey': 'string',
                        'RouteResponseSelectionExpression': 'string',
                        'Target': 'string'
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            Success

            - **Items** *(list) --*

              The elements from this collection.

              - *(dict) --*

                Represents a route.

                - **ApiKeyRequired** *(boolean) --*

                  Specifies whether an API key is required for this route.

                - **AuthorizationScopes** *(list) --*

                  A list of authorization scopes configured on a route. The scopes are used with a
                  COGNITO_USER_POOLS authorizer to authorize the method invocation. The
                  authorization works by matching the route scopes against the scopes parsed from
                  the access token in the incoming request. The method invocation is authorized if
                  any route scope matches a claimed scope in the access token. Otherwise, the
                  invocation is not authorized. When the route scope is configured, the client must
                  provide an access token instead of an identity token for authorization purposes.

                  - *(string) --*

                    A string with a length between [1-64].

                - **AuthorizationType** *(string) --*

                  The authorization type for the route. Valid values are NONE for open access,
                  AWS_IAM for using AWS IAM permissions, and CUSTOM for using a Lambda authorizer

                - **AuthorizerId** *(string) --*

                  The identifier of the Authorizer resource to be associated with this route, if the
                  authorizationType is CUSTOM . The authorizer identifier is generated by API
                  Gateway when you created the authorizer.

                - **ModelSelectionExpression** *(string) --*

                  The model selection expression for the route.

                - **OperationName** *(string) --*

                  The operation name for the route.

                - **RequestModels** *(dict) --*

                  The request models for the route.

                  - *(string) --*

                    - *(string) --*

                      A string with a length between [1-128].

                - **RequestParameters** *(dict) --*

                  The request parameters for the route.

                  - *(string) --*

                    - *(dict) --*

                      Validation constraints imposed on parameters of a request (path, query string,
                      headers).

                      - **Required** *(boolean) --*

                        Whether or not the parameter is required.

                - **RouteId** *(string) --*

                  The route ID.

                - **RouteKey** *(string) --*

                  The route key for the route.

                - **RouteResponseSelectionExpression** *(string) --*

                  The route response selection expression for the route.

                - **Target** *(string) --*

                  The target for the route.
        """


class GetStagesPaginator(Boto3Paginator):
    """
    Paginator for `get_stages`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, ApiId: str, PaginationConfig: GetStagesPaginatePaginationConfigTypeDef = None
    ) -> GetStagesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`ApiGatewayV2.Client.get_stages`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/apigatewayv2-2018-11-29/GetStages>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              ApiId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type ApiId: string
        :param ApiId: **[REQUIRED]**

          The API identifier.

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
                'Items': [
                    {
                        'AccessLogSettings': {
                            'DestinationArn': 'string',
                            'Format': 'string'
                        },
                        'ClientCertificateId': 'string',
                        'CreatedDate': datetime(2015, 1, 1),
                        'DefaultRouteSettings': {
                            'DataTraceEnabled': True|False,
                            'DetailedMetricsEnabled': True|False,
                            'LoggingLevel': 'ERROR'|'INFO'|'false',
                            'ThrottlingBurstLimit': 123,
                            'ThrottlingRateLimit': 123.0
                        },
                        'DeploymentId': 'string',
                        'Description': 'string',
                        'LastUpdatedDate': datetime(2015, 1, 1),
                        'RouteSettings': {
                            'string': {
                                'DataTraceEnabled': True|False,
                                'DetailedMetricsEnabled': True|False,
                                'LoggingLevel': 'ERROR'|'INFO'|'false',
                                'ThrottlingBurstLimit': 123,
                                'ThrottlingRateLimit': 123.0
                            }
                        },
                        'StageName': 'string',
                        'StageVariables': {
                            'string': 'string'
                        },
                        'Tags': {
                            'string': 'string'
                        }
                    },
                ],

            }
          **Response Structure**

          - *(dict) --*

            Success

            - **Items** *(list) --*

              The elements from this collection.

              - *(dict) --*

                Represents an API stage.

                - **AccessLogSettings** *(dict) --*

                  Settings for logging access in this stage.

                  - **DestinationArn** *(string) --*

                    The ARN of the CloudWatch Logs log group to receive access logs.

                  - **Format** *(string) --*

                    A single line format of the access logs of data, as specified by selected
                    $context variables. The format must include at least $context.requestId.

                - **ClientCertificateId** *(string) --*

                  The identifier of a client certificate for a Stage.

                - **CreatedDate** *(datetime) --*

                  The timestamp when the stage was created.

                - **DefaultRouteSettings** *(dict) --*

                  Default route settings for the stage.

                  - **DataTraceEnabled** *(boolean) --*

                    Specifies whether (true) or not (false) data trace logging is enabled for this
                    route. This property affects the log entries pushed to Amazon CloudWatch Logs.

                  - **DetailedMetricsEnabled** *(boolean) --*

                    Specifies whether detailed metrics are enabled.

                  - **LoggingLevel** *(string) --*

                    Specifies the logging level for this route: DEBUG, INFO, or WARN. This property
                    affects the log entries pushed to Amazon CloudWatch Logs.

                  - **ThrottlingBurstLimit** *(integer) --*

                    Specifies the throttling burst limit.

                  - **ThrottlingRateLimit** *(float) --*

                    Specifies the throttling rate limit.

                - **DeploymentId** *(string) --*

                  The identifier of the Deployment that the Stage is associated with.

                - **Description** *(string) --*

                  The description of the stage.

                - **LastUpdatedDate** *(datetime) --*

                  The timestamp when the stage was last updated.

                - **RouteSettings** *(dict) --*

                  Route settings for the stage.

                  - *(string) --*

                    - *(dict) --*

                      Represents a collection of route settings.

                      - **DataTraceEnabled** *(boolean) --*

                        Specifies whether (true) or not (false) data trace logging is enabled for
                        this route. This property affects the log entries pushed to Amazon
                        CloudWatch Logs.

                      - **DetailedMetricsEnabled** *(boolean) --*

                        Specifies whether detailed metrics are enabled.

                      - **LoggingLevel** *(string) --*

                        Specifies the logging level for this route: DEBUG, INFO, or WARN. This
                        property affects the log entries pushed to Amazon CloudWatch Logs.

                      - **ThrottlingBurstLimit** *(integer) --*

                        Specifies the throttling burst limit.

                      - **ThrottlingRateLimit** *(float) --*

                        Specifies the throttling rate limit.

                - **StageName** *(string) --*

                  The name of the stage.

                - **StageVariables** *(dict) --*

                  A map that defines the stage variables for a stage resource. Variable names can
                  have alphanumeric and underscore characters, and the values must match
                  [A-Za-z0-9-._~:/?#&=,]+.

                  - *(string) --*

                    - *(string) --*

                      A string with a length between [0-2048].

                - **Tags** *(dict) --*

                  The key-value map of strings. The valid character set is [a-zA-Z+-=
                      ._:/]. The tag
                  key can be up to 128 characters and must not start with aws:. The tag value can be
                  up to 256 characters..

                  - *(string) --*

                    - *(string) --*

                      A string with a length between [1-1600].
        """
