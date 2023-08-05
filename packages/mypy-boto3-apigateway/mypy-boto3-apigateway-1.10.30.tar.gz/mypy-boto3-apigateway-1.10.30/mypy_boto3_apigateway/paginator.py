"Main interface for apigateway service Paginators"
from __future__ import annotations

from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3.type_defs import Literal
from mypy_boto3_apigateway.type_defs import (
    GetApiKeysPaginatePaginationConfigTypeDef,
    GetApiKeysPaginateResponseTypeDef,
    GetAuthorizersPaginatePaginationConfigTypeDef,
    GetAuthorizersPaginateResponseTypeDef,
    GetBasePathMappingsPaginatePaginationConfigTypeDef,
    GetBasePathMappingsPaginateResponseTypeDef,
    GetClientCertificatesPaginatePaginationConfigTypeDef,
    GetClientCertificatesPaginateResponseTypeDef,
    GetDeploymentsPaginatePaginationConfigTypeDef,
    GetDeploymentsPaginateResponseTypeDef,
    GetDocumentationPartsPaginatePaginationConfigTypeDef,
    GetDocumentationPartsPaginateResponseTypeDef,
    GetDocumentationVersionsPaginatePaginationConfigTypeDef,
    GetDocumentationVersionsPaginateResponseTypeDef,
    GetDomainNamesPaginatePaginationConfigTypeDef,
    GetDomainNamesPaginateResponseTypeDef,
    GetGatewayResponsesPaginatePaginationConfigTypeDef,
    GetGatewayResponsesPaginateResponseTypeDef,
    GetModelsPaginatePaginationConfigTypeDef,
    GetModelsPaginateResponseTypeDef,
    GetRequestValidatorsPaginatePaginationConfigTypeDef,
    GetRequestValidatorsPaginateResponseTypeDef,
    GetResourcesPaginatePaginationConfigTypeDef,
    GetResourcesPaginateResponseTypeDef,
    GetRestApisPaginatePaginationConfigTypeDef,
    GetRestApisPaginateResponseTypeDef,
    GetSdkTypesPaginatePaginationConfigTypeDef,
    GetSdkTypesPaginateResponseTypeDef,
    GetUsagePaginatePaginationConfigTypeDef,
    GetUsagePaginateResponseTypeDef,
    GetUsagePlanKeysPaginatePaginationConfigTypeDef,
    GetUsagePlanKeysPaginateResponseTypeDef,
    GetUsagePlansPaginatePaginationConfigTypeDef,
    GetUsagePlansPaginateResponseTypeDef,
    GetVpcLinksPaginatePaginationConfigTypeDef,
    GetVpcLinksPaginateResponseTypeDef,
)


__all__ = (
    "GetApiKeysPaginator",
    "GetAuthorizersPaginator",
    "GetBasePathMappingsPaginator",
    "GetClientCertificatesPaginator",
    "GetDeploymentsPaginator",
    "GetDocumentationPartsPaginator",
    "GetDocumentationVersionsPaginator",
    "GetDomainNamesPaginator",
    "GetGatewayResponsesPaginator",
    "GetModelsPaginator",
    "GetRequestValidatorsPaginator",
    "GetResourcesPaginator",
    "GetRestApisPaginator",
    "GetSdkTypesPaginator",
    "GetUsagePaginator",
    "GetUsagePlanKeysPaginator",
    "GetUsagePlansPaginator",
    "GetVpcLinksPaginator",
)


class GetApiKeysPaginator(Boto3Paginator):
    """
    Paginator for `get_api_keys`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        nameQuery: str = None,
        customerId: str = None,
        includeValues: bool = None,
        PaginationConfig: GetApiKeysPaginatePaginationConfigTypeDef = None,
    ) -> GetApiKeysPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`APIGateway.Client.get_api_keys`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/GetApiKeys>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              nameQuery='string',
              customerId='string',
              includeValues=True|False,
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type nameQuery: string
        :param nameQuery:

          The name of queried API keys.

        :type customerId: string
        :param customerId:

          The identifier of a customer in AWS Marketplace or an external system, such as a developer
          portal.

        :type includeValues: boolean
        :param includeValues:

          A boolean flag to specify whether (``true`` ) or not (``false`` ) the result contains key
          values.

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
                'warnings': [
                    'string',
                ],
                'items': [
                    {
                        'id': 'string',
                        'value': 'string',
                        'name': 'string',
                        'customerId': 'string',
                        'description': 'string',
                        'enabled': True|False,
                        'createdDate': datetime(2015, 1, 1),
                        'lastUpdatedDate': datetime(2015, 1, 1),
                        'stageKeys': [
                            'string',
                        ],
                        'tags': {
                            'string': 'string'
                        }
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Represents a collection of API keys as represented by an  ApiKeys resource.

              `Use API Keys
              <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-api-keys.html>`__

            - **warnings** *(list) --*

              A list of warning messages logged during the import of API keys when the
              ``failOnWarnings`` option is set to true.

              - *(string) --*

            - **items** *(list) --*

              The current page of elements from this collection.

              - *(dict) --*

                A resource that can be distributed to callers for executing  Method resources that
                require an API key. API keys can be mapped to any  Stage on any  RestApi , which
                indicates that the callers with the API key can make requests to that stage.

                  `Use API Keys
                  <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-api-keys.html>`__

                - **id** *(string) --*

                  The identifier of the API Key.

                - **value** *(string) --*

                  The value of the API Key.

                - **name** *(string) --*

                  The name of the API Key.

                - **customerId** *(string) --*

                  An AWS Marketplace customer identifier , when integrating with the AWS SaaS
                  Marketplace.

                - **description** *(string) --*

                  The description of the API Key.

                - **enabled** *(boolean) --*

                  Specifies whether the API Key can be used by callers.

                - **createdDate** *(datetime) --*

                  The timestamp when the API Key was created.

                - **lastUpdatedDate** *(datetime) --*

                  The timestamp when the API Key was last updated.

                - **stageKeys** *(list) --*

                  A list of  Stage resources that are associated with the  ApiKey resource.

                  - *(string) --*

                - **tags** *(dict) --*

                  The collection of tags. Each tag element is associated with a given resource.

                  - *(string) --*

                    - *(string) --*

            - **NextToken** *(string) --*

              A token to resume pagination.
        """


class GetAuthorizersPaginator(Boto3Paginator):
    """
    Paginator for `get_authorizers`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, restApiId: str, PaginationConfig: GetAuthorizersPaginatePaginationConfigTypeDef = None
    ) -> GetAuthorizersPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`APIGateway.Client.get_authorizers`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/GetAuthorizers>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              restApiId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type restApiId: string
        :param restApiId: **[REQUIRED]**

          [Required] The string identifier of the associated  RestApi .

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
                'items': [
                    {
                        'id': 'string',
                        'name': 'string',
                        'type': 'TOKEN'|'REQUEST'|'COGNITO_USER_POOLS',
                        'providerARNs': [
                            'string',
                        ],
                        'authType': 'string',
                        'authorizerUri': 'string',
                        'authorizerCredentials': 'string',
                        'identitySource': 'string',
                        'identityValidationExpression': 'string',
                        'authorizerResultTtlInSeconds': 123
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Represents a collection of  Authorizer resources.

              `Use Lambda Function as Authorizer
              <https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-use-lambda-authorizer.html>`__
              `Use Cognito User Pool as Authorizer
              <https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-integrate-with-cognito.html>`__

            - **items** *(list) --*

              The current page of elements from this collection.

              - *(dict) --*

                Represents an authorization layer for methods. If enabled on a method, API Gateway
                will activate the authorizer when a client calls the method.

                  `Use Lambda Function as Authorizer
                  <https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-use-lambda-authorizer.html>`__
                  `Use Cognito User Pool as Authorizer
                  <https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-integrate-with-cognito.html>`__

                - **id** *(string) --*

                  The identifier for the authorizer resource.

                - **name** *(string) --*

                  [Required] The name of the authorizer.

                - **type** *(string) --*

                  The authorizer type. Valid values are ``TOKEN`` for a Lambda function using a
                  single authorization token submitted in a custom header, ``REQUEST`` for a Lambda
                  function using incoming request parameters, and ``COGNITO_USER_POOLS`` for using
                  an Amazon Cognito user pool.

                - **providerARNs** *(list) --*

                  A list of the Amazon Cognito user pool ARNs for the ``COGNITO_USER_POOLS``
                  authorizer. Each element is of this format:
                  ``arn:aws:cognito-idp:{region}:{account_id}:userpool/{user_pool_id}`` . For a
                  ``TOKEN`` or ``REQUEST`` authorizer, this is not defined.

                  - *(string) --*

                - **authType** *(string) --*

                  Optional customer-defined field, used in OpenAPI imports and exports without
                  functional impact.

                - **authorizerUri** *(string) --*

                  Specifies the authorizer's Uniform Resource Identifier (URI). For ``TOKEN`` or
                  ``REQUEST`` authorizers, this must be a well-formed Lambda function URI, for
                  example,
                  ``arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2:{account_id}:function:{lambda_function_name}/invocations``
                  . In general, the URI has this form
                  ``arn:aws:apigateway:{region}:lambda:path/{service_api}`` , where ``{region}`` is
                  the same as the region hosting the Lambda function, ``path`` indicates that the
                  remaining substring in the URI should be treated as the path to the resource,
                  including the initial ``/`` . For Lambda functions, this is usually of the form
                  ``/2015-03-31/functions/[FunctionARN]/invocations`` .

                - **authorizerCredentials** *(string) --*

                  Specifies the required credentials as an IAM role for API Gateway to invoke the
                  authorizer. To specify an IAM role for API Gateway to assume, use the role's
                  Amazon Resource Name (ARN). To use resource-based permissions on the Lambda
                  function, specify null.

                - **identitySource** *(string) --*

                  The identity source for which authorization is requested.

                  * For a ``TOKEN`` or ``COGNITO_USER_POOLS`` authorizer, this is required and
                  specifies the request header mapping expression for the custom header holding the
                  authorization token submitted by the client. For example, if the token header name
                  is ``Auth`` , the header mapping expression is ``method.request.header.Auth`` .

                  * For the ``REQUEST`` authorizer, this is required when authorization caching is
                  enabled. The value is a comma-separated string of one or more mapping expressions
                  of the specified request parameters. For example, if an ``Auth`` header, a
                  ``Name`` query string parameter are defined as identity sources, this value is
                  ``method.request.header.Auth, method.request.querystring.Name`` . These parameters
                  will be used to derive the authorization caching key and to perform runtime
                  validation of the ``REQUEST`` authorizer by verifying all of the identity-related
                  request parameters are present, not null and non-empty. Only when this is true
                  does the authorizer invoke the authorizer Lambda function, otherwise, it returns a
                  401 Unauthorized response without calling the Lambda function. The valid value is
                  a string of comma-separated mapping expressions of the specified request
                  parameters. When the authorization caching is not enabled, this property is
                  optional.

                - **identityValidationExpression** *(string) --*

                  A validation expression for the incoming identity token. For ``TOKEN``
                  authorizers, this value is a regular expression. For ``COGNITO_USER_POOLS``
                  authorizers, API Gateway will match the ``aud`` field of the incoming token from
                  the client against the specified regular expression. It will invoke the
                  authorizer's Lambda function when there is a match. Otherwise, it will return a
                  401 Unauthorized response without calling the Lambda function. The validation
                  expression does not apply to the ``REQUEST`` authorizer.

                - **authorizerResultTtlInSeconds** *(integer) --*

                  The TTL in seconds of cached authorizer results. If it equals 0, authorization
                  caching is disabled. If it is greater than 0, API Gateway will cache authorizer
                  responses. If this field is not set, the default value is 300. The maximum value
                  is 3600, or 1 hour.

            - **NextToken** *(string) --*

              A token to resume pagination.
        """


class GetBasePathMappingsPaginator(Boto3Paginator):
    """
    Paginator for `get_base_path_mappings`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        domainName: str,
        PaginationConfig: GetBasePathMappingsPaginatePaginationConfigTypeDef = None,
    ) -> GetBasePathMappingsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`APIGateway.Client.get_base_path_mappings`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/GetBasePathMappings>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              domainName='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type domainName: string
        :param domainName: **[REQUIRED]**

          [Required] The domain name of a  BasePathMapping resource.

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
                'items': [
                    {
                        'basePath': 'string',
                        'restApiId': 'string',
                        'stage': 'string'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Represents a collection of  BasePathMapping resources.

              `Use Custom Domain Names
              <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domains.html>`__

            - **items** *(list) --*

              The current page of elements from this collection.

              - *(dict) --*

                Represents the base path that callers of the API must provide as part of the URL
                after the domain name.

                 A custom domain name plus a ``BasePathMapping`` specification identifies a deployed
                 RestApi in a given stage of the owner  Account .  `Use Custom Domain Names
                 <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domains.html>`__

                - **basePath** *(string) --*

                  The base path name that callers of the API must provide as part of the URL after
                  the domain name.

                - **restApiId** *(string) --*

                  The string identifier of the associated  RestApi .

                - **stage** *(string) --*

                  The name of the associated stage.

            - **NextToken** *(string) --*

              A token to resume pagination.
        """


class GetClientCertificatesPaginator(Boto3Paginator):
    """
    Paginator for `get_client_certificates`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: GetClientCertificatesPaginatePaginationConfigTypeDef = None
    ) -> GetClientCertificatesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`APIGateway.Client.get_client_certificates`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/GetClientCertificates>`_

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
                'items': [
                    {
                        'clientCertificateId': 'string',
                        'description': 'string',
                        'pemEncodedCertificate': 'string',
                        'createdDate': datetime(2015, 1, 1),
                        'expirationDate': datetime(2015, 1, 1),
                        'tags': {
                            'string': 'string'
                        }
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Represents a collection of  ClientCertificate resources.

              `Use Client-Side Certificate
              <https://docs.aws.amazon.com/apigateway/latest/developerguide/getting-started-client-side-ssl-authentication.html>`__

            - **items** *(list) --*

              The current page of elements from this collection.

              - *(dict) --*

                Represents a client certificate used to configure client-side SSL authentication
                while sending requests to the integration endpoint.

                 Client certificates are used to authenticate an API by the backend server. To
                 authenticate an API client (or user), use IAM roles and policies, a custom
                 Authorizer or an Amazon Cognito user pool.  `Use Client-Side Certificate
                 <https://docs.aws.amazon.com/apigateway/latest/developerguide/getting-started-client-side-ssl-authentication.html>`__

                - **clientCertificateId** *(string) --*

                  The identifier of the client certificate.

                - **description** *(string) --*

                  The description of the client certificate.

                - **pemEncodedCertificate** *(string) --*

                  The PEM-encoded public key of the client certificate, which can be used to
                  configure certificate authentication in the integration endpoint .

                - **createdDate** *(datetime) --*

                  The timestamp when the client certificate was created.

                - **expirationDate** *(datetime) --*

                  The timestamp when the client certificate will expire.

                - **tags** *(dict) --*

                  The collection of tags. Each tag element is associated with a given resource.

                  - *(string) --*

                    - *(string) --*

            - **NextToken** *(string) --*

              A token to resume pagination.
        """


class GetDeploymentsPaginator(Boto3Paginator):
    """
    Paginator for `get_deployments`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, restApiId: str, PaginationConfig: GetDeploymentsPaginatePaginationConfigTypeDef = None
    ) -> GetDeploymentsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`APIGateway.Client.get_deployments`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/GetDeployments>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              restApiId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type restApiId: string
        :param restApiId: **[REQUIRED]**

          [Required] The string identifier of the associated  RestApi .

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
                'items': [
                    {
                        'id': 'string',
                        'description': 'string',
                        'createdDate': datetime(2015, 1, 1),
                        'apiSummary': {
                            'string': {
                                'string': {
                                    'authorizationType': 'string',
                                    'apiKeyRequired': True|False
                                }
                            }
                        }
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Represents a collection resource that contains zero or more references to your existing
            deployments, and links that guide you on how to interact with your collection. The
            collection offers a paginated view of the contained deployments.

             To create a new deployment of a  RestApi , make a ``POST`` request against this
             resource. To view, update, or delete an existing deployment, make a ``GET`` , ``PATCH``
             , or ``DELETE`` request, respectively, on a specified  Deployment resource.  `Deploying
             an API
             <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-deploy-api.html>`__
             , `AWS CLI
             <https://docs.aws.amazon.com/cli/latest/reference/apigateway/get-deployment.html>`__ ,
             `AWS SDKs <https://aws.amazon.com/tools/>`__

            - **items** *(list) --*

              The current page of elements from this collection.

              - *(dict) --*

                An immutable representation of a  RestApi resource that can be called by users using
                Stages . A deployment must be associated with a  Stage for it to be callable over
                the Internet.

                 To create a deployment, call ``POST`` on the  Deployments resource of a  RestApi .
                 To view, update, or delete a deployment, call ``GET`` , ``PATCH`` , or ``DELETE``
                 on the specified deployment resource
                 (``/restapis/{restapi_id}/deployments/{deployment_id}`` ).  RestApi ,  Deployments
                 ,  Stage , `AWS CLI
                 <https://docs.aws.amazon.com/cli/latest/reference/apigateway/get-deployment.html>`__
                 , `AWS SDKs <https://aws.amazon.com/tools/>`__

                - **id** *(string) --*

                  The identifier for the deployment resource.

                - **description** *(string) --*

                  The description for the deployment resource.

                - **createdDate** *(datetime) --*

                  The date and time that the deployment resource was created.

                - **apiSummary** *(dict) --*

                  A summary of the  RestApi at the date and time that the deployment resource was
                  created.

                  - *(string) --*

                    - *(dict) --*

                      - *(string) --*

                        - *(dict) --*

                          Represents a summary of a  Method resource, given a particular date and
                          time.

                          - **authorizationType** *(string) --*

                            The method's authorization type. Valid values are ``NONE`` for open
                            access, ``AWS_IAM`` for using AWS IAM permissions, ``CUSTOM`` for using
                            a custom authorizer, or ``COGNITO_USER_POOLS`` for using a Cognito user
                            pool.

                          - **apiKeyRequired** *(boolean) --*

                            Specifies whether the method requires a valid  ApiKey .

            - **NextToken** *(string) --*

              A token to resume pagination.
        """


class GetDocumentationPartsPaginator(Boto3Paginator):
    """
    Paginator for `get_documentation_parts`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        restApiId: str,
        type: Literal[
            "API",
            "AUTHORIZER",
            "MODEL",
            "RESOURCE",
            "METHOD",
            "PATH_PARAMETER",
            "QUERY_PARAMETER",
            "REQUEST_HEADER",
            "REQUEST_BODY",
            "RESPONSE",
            "RESPONSE_HEADER",
            "RESPONSE_BODY",
        ] = None,
        nameQuery: str = None,
        path: str = None,
        locationStatus: Literal["DOCUMENTED", "UNDOCUMENTED"] = None,
        PaginationConfig: GetDocumentationPartsPaginatePaginationConfigTypeDef = None,
    ) -> GetDocumentationPartsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`APIGateway.Client.get_documentation_parts`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/GetDocumentationParts>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              restApiId='string',
              type=
                  'API'|'AUTHORIZER'|'MODEL'|'RESOURCE'|'METHOD'|'PATH_PARAMETER'|'QUERY_PARAMETER'
                  |'REQUEST_HEADER'|'REQUEST_BODY'|'RESPONSE'|'RESPONSE_HEADER'|'RESPONSE_BODY',
              nameQuery='string',
              path='string',
              locationStatus='DOCUMENTED'|'UNDOCUMENTED',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type restApiId: string
        :param restApiId: **[REQUIRED]**

          [Required] The string identifier of the associated  RestApi .

        :type type: string
        :param type:

          The type of API entities of the to-be-retrieved documentation parts.

        :type nameQuery: string
        :param nameQuery:

          The name of API entities of the to-be-retrieved documentation parts.

        :type path: string
        :param path:

          The path of API entities of the to-be-retrieved documentation parts.

        :type locationStatus: string
        :param locationStatus:

          The status of the API documentation parts to retrieve. Valid values are ``DOCUMENTED`` for
          retrieving  DocumentationPart resources with content and ``UNDOCUMENTED`` for
          DocumentationPart resources without content.

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
                'items': [
                    {
                        'id': 'string',
                        'location': {
                            'type':
                            'API'|'AUTHORIZER'|'MODEL'|'RESOURCE'|'METHOD'
                            |'PATH_PARAMETER'|'QUERY_PARAMETER'|'REQUEST_HEADER'
                            |'REQUEST_BODY'|'RESPONSE'|'RESPONSE_HEADER'
                            |'RESPONSE_BODY',
                            'path': 'string',
                            'method': 'string',
                            'statusCode': 'string',
                            'name': 'string'
                        },
                        'properties': 'string'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            The collection of documentation parts of an API.

               `Documenting an API
               <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-documenting-api.html>`__
               ,  DocumentationPart

            - **items** *(list) --*

              The current page of elements from this collection.

              - *(dict) --*

                A documentation part for a targeted API entity.

                A documentation part consists of a content map (``properties`` ) and a target
                (``location`` ). The target specifies an API entity to which the documentation
                content applies. The supported API entity types are ``API`` , ``AUTHORIZER`` ,
                ``MODEL`` , ``RESOURCE`` , ``METHOD`` , ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` ,
                ``REQUEST_HEADER`` , ``REQUEST_BODY`` , ``RESPONSE`` , ``RESPONSE_HEADER`` , and
                ``RESPONSE_BODY`` . Valid ``location`` fields depend on the API entity type. All
                valid fields are not required.

                The content map is a JSON string of API-specific key-value pairs. Although an API
                can use any shape for the content map, only the OpenAPI-compliant documentation
                fields will be injected into the associated API entity definition in the exported
                OpenAPI definition file.

                  `Documenting an API
                  <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-documenting-api.html>`__
                  ,  DocumentationParts

                - **id** *(string) --*

                  The  DocumentationPart identifier, generated by API Gateway when the
                  ``DocumentationPart`` is created.

                - **location** *(dict) --*

                  The location of the API entity to which the documentation applies. Valid fields
                  depend on the targeted API entity type. All the valid location fields are not
                  required. If not explicitly specified, a valid location field is treated as a
                  wildcard and associated documentation content may be inherited by matching
                  entities, unless overridden.

                  - **type** *(string) --*

                    [Required] The type of API entity to which the documentation content applies.
                    Valid values are ``API`` , ``AUTHORIZER`` , ``MODEL`` , ``RESOURCE`` ,
                    ``METHOD`` , ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` , ``REQUEST_HEADER`` ,
                    ``REQUEST_BODY`` , ``RESPONSE`` , ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` .
                    Content inheritance does not apply to any entity of the ``API`` , ``AUTHORIZER``
                    , ``METHOD`` , ``MODEL`` , ``REQUEST_BODY`` , or ``RESOURCE`` type.

                  - **path** *(string) --*

                    The URL path of the target. It is a valid field for the API entity types of
                    ``RESOURCE`` , ``METHOD`` , ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` ,
                    ``REQUEST_HEADER`` , ``REQUEST_BODY`` , ``RESPONSE`` , ``RESPONSE_HEADER`` , and
                    ``RESPONSE_BODY`` . The default value is ``/`` for the root resource. When an
                    applicable child entity inherits the content of another entity of the same type
                    with more general specifications of the other ``location`` attributes, the child
                    entity's ``path`` attribute must match that of the parent entity as a prefix.

                  - **method** *(string) --*

                    The HTTP verb of a method. It is a valid field for the API entity types of
                    ``METHOD`` , ``PATH_PARAMETER`` , ``QUERY_PARAMETER`` , ``REQUEST_HEADER`` ,
                    ``REQUEST_BODY`` , ``RESPONSE`` , ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` .
                    The default value is ``*`` for any method. When an applicable child entity
                    inherits the content of an entity of the same type with more general
                    specifications of the other ``location`` attributes, the child entity's
                    ``method`` attribute must match that of the parent entity exactly.

                  - **statusCode** *(string) --*

                    The HTTP status code of a response. It is a valid field for the API entity types
                    of ``RESPONSE`` , ``RESPONSE_HEADER`` , and ``RESPONSE_BODY`` . The default
                    value is ``*`` for any status code. When an applicable child entity inherits the
                    content of an entity of the same type with more general specifications of the
                    other ``location`` attributes, the child entity's ``statusCode`` attribute must
                    match that of the parent entity exactly.

                  - **name** *(string) --*

                    The name of the targeted API entity. It is a valid and required field for the
                    API entity types of ``AUTHORIZER`` , ``MODEL`` , ``PATH_PARAMETER`` ,
                    ``QUERY_PARAMETER`` , ``REQUEST_HEADER`` , ``REQUEST_BODY`` and
                    ``RESPONSE_HEADER`` . It is an invalid field for any other entity type.

                - **properties** *(string) --*

                  A content map of API-specific key-value pairs describing the targeted API entity.
                  The map must be encoded as a JSON string, e.g., ``"{ \\"description\\": \\"The API
                  does ...\\" }"`` . Only OpenAPI-compliant documentation-related fields from the
                  propertiesmap are exported and, hence, published as part of the API entity
                  definitions, while the original documentation parts are exported in a OpenAPI
                  extension of ``x-amazon-apigateway-documentation`` .

            - **NextToken** *(string) --*

              A token to resume pagination.
        """


class GetDocumentationVersionsPaginator(Boto3Paginator):
    """
    Paginator for `get_documentation_versions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        restApiId: str,
        PaginationConfig: GetDocumentationVersionsPaginatePaginationConfigTypeDef = None,
    ) -> GetDocumentationVersionsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`APIGateway.Client.get_documentation_versions`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/GetDocumentationVersions>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              restApiId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type restApiId: string
        :param restApiId: **[REQUIRED]**

          [Required] The string identifier of the associated  RestApi .

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
                'items': [
                    {
                        'version': 'string',
                        'createdDate': datetime(2015, 1, 1),
                        'description': 'string'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            The collection of documentation snapshots of an API.

            Use the  DocumentationVersions to manage documentation snapshots associated with various
            API stages.

              `Documenting an API
              <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-documenting-api.html>`__
              ,  DocumentationPart ,  DocumentationVersion

            - **items** *(list) --*

              The current page of elements from this collection.

              - *(dict) --*

                A snapshot of the documentation of an API.

                Publishing API documentation involves creating a documentation version associated
                with an API stage and exporting the versioned documentation to an external (e.g.,
                OpenAPI) file.

                  `Documenting an API
                  <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-documenting-api.html>`__
                  ,  DocumentationPart ,  DocumentationVersions

                - **version** *(string) --*

                  The version identifier of the API documentation snapshot.

                - **createdDate** *(datetime) --*

                  The date when the API documentation snapshot is created.

                - **description** *(string) --*

                  The description of the API documentation snapshot.

            - **NextToken** *(string) --*

              A token to resume pagination.
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
        :py:meth:`APIGateway.Client.get_domain_names`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/GetDomainNames>`_

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
                'items': [
                    {
                        'domainName': 'string',
                        'certificateName': 'string',
                        'certificateArn': 'string',
                        'certificateUploadDate': datetime(2015, 1, 1),
                        'regionalDomainName': 'string',
                        'regionalHostedZoneId': 'string',
                        'regionalCertificateName': 'string',
                        'regionalCertificateArn': 'string',
                        'distributionDomainName': 'string',
                        'distributionHostedZoneId': 'string',
                        'endpointConfiguration': {
                            'types': [
                                'REGIONAL'|'EDGE'|'PRIVATE',
                            ],
                            'vpcEndpointIds': [
                                'string',
                            ]
                        },
                        'domainNameStatus': 'AVAILABLE'|'UPDATING'|'PENDING',
                        'domainNameStatusMessage': 'string',
                        'securityPolicy': 'TLS_1_0'|'TLS_1_2',
                        'tags': {
                            'string': 'string'
                        }
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Represents a collection of  DomainName resources.

              `Use Client-Side Certificate
              <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domains.html>`__

            - **items** *(list) --*

              The current page of elements from this collection.

              - *(dict) --*

                Represents a custom domain name as a user-friendly host name of an API ( RestApi ).

                When you deploy an API, API Gateway creates a default host name for the API. This
                default API host name is of the ``{restapi-id}.execute-api.{region}.amazonaws.com``
                format. With the default host name, you can access the API's root resource with the
                URL of ``https://{restapi-id}.execute-api.{region}.amazonaws.com/{stage}/`` . When
                you set up a custom domain name of ``apis.example.com`` for this API, you can then
                access the same resource using the URL of the ``https://apis.examples.com/myApi`` ,
                where ``myApi`` is the base path mapping ( BasePathMapping ) of your API under the
                custom domain name.

                   `Set a Custom Host Name for an API
                   <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domains.html>`__

                - **domainName** *(string) --*

                  The custom domain name as an API host name, for example, ``my-api.example.com`` .

                - **certificateName** *(string) --*

                  The name of the certificate that will be used by edge-optimized endpoint for this
                  domain name.

                - **certificateArn** *(string) --*

                  The reference to an AWS-managed certificate that will be used by edge-optimized
                  endpoint for this domain name. AWS Certificate Manager is the only supported
                  source.

                - **certificateUploadDate** *(datetime) --*

                  The timestamp when the certificate that was used by edge-optimized endpoint for
                  this domain name was uploaded.

                - **regionalDomainName** *(string) --*

                  The domain name associated with the regional endpoint for this custom domain name.
                  You set up this association by adding a DNS record that points the custom domain
                  name to this regional domain name. The regional domain name is returned by API
                  Gateway when you create a regional endpoint.

                - **regionalHostedZoneId** *(string) --*

                  The region-specific Amazon Route 53 Hosted Zone ID of the regional endpoint. For
                  more information, see `Set up a Regional Custom Domain Name
                  <https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-regional-api-custom-domain-create.html>`__
                  and `AWS Regions and Endpoints for API Gateway
                  <https://docs.aws.amazon.com/general/latest/gr/rande.html#apigateway_region>`__ .

                - **regionalCertificateName** *(string) --*

                  The name of the certificate that will be used for validating the regional domain
                  name.

                - **regionalCertificateArn** *(string) --*

                  The reference to an AWS-managed certificate that will be used for validating the
                  regional domain name. AWS Certificate Manager is the only supported source.

                - **distributionDomainName** *(string) --*

                  The domain name of the Amazon CloudFront distribution associated with this custom
                  domain name for an edge-optimized endpoint. You set up this association when
                  adding a DNS record pointing the custom domain name to this distribution name. For
                  more information about CloudFront distributions, see the `Amazon CloudFront
                  documentation <https://aws.amazon.com/documentation/cloudfront/>`__ .

                - **distributionHostedZoneId** *(string) --*

                  The region-agnostic Amazon Route 53 Hosted Zone ID of the edge-optimized endpoint.
                  The valid value is ``Z2FDTNDATAQYW2`` for all the regions. For more information,
                  see `Set up a Regional Custom Domain Name
                  <https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-regional-api-custom-domain-create.html>`__
                  and `AWS Regions and Endpoints for API Gateway
                  <https://docs.aws.amazon.com/general/latest/gr/rande.html#apigateway_region>`__ .

                - **endpointConfiguration** *(dict) --*

                  The endpoint configuration of this  DomainName showing the endpoint types of the
                  domain name.

                  - **types** *(list) --*

                    A list of endpoint types of an API ( RestApi ) or its custom domain name (
                    DomainName ). For an edge-optimized API and its custom domain name, the endpoint
                    type is ``"EDGE"`` . For a regional API and its custom domain name, the endpoint
                    type is ``REGIONAL`` . For a private API, the endpoint type is ``PRIVATE`` .

                    - *(string) --*

                      The endpoint type. The valid values are ``EDGE`` for edge-optimized API setup,
                      most suitable for mobile applications; ``REGIONAL`` for regional API endpoint
                      setup, most suitable for calling from AWS Region; and ``PRIVATE`` for private
                      APIs.

                  - **vpcEndpointIds** *(list) --*

                    A list of VpcEndpointIds of an API ( RestApi ) against which to create Route53
                    ALIASes. It is only supported for ``PRIVATE`` endpoint type.

                    - *(string) --*

                - **domainNameStatus** *(string) --*

                  The status of the  DomainName migration. The valid values are ``AVAILABLE`` and
                  ``UPDATING`` . If the status is ``UPDATING`` , the domain cannot be modified
                  further until the existing operation is complete. If it is ``AVAILABLE`` , the
                  domain can be updated.

                - **domainNameStatusMessage** *(string) --*

                  An optional text message containing detailed information about status of the
                  DomainName migration.

                - **securityPolicy** *(string) --*

                  The Transport Layer Security (TLS) version + cipher suite for this  DomainName .
                  The valid values are ``TLS_1_0`` and ``TLS_1_2`` .

                - **tags** *(dict) --*

                  The collection of tags. Each tag element is associated with a given resource.

                  - *(string) --*

                    - *(string) --*

            - **NextToken** *(string) --*

              A token to resume pagination.
        """


class GetGatewayResponsesPaginator(Boto3Paginator):
    """
    Paginator for `get_gateway_responses`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        restApiId: str,
        PaginationConfig: GetGatewayResponsesPaginatePaginationConfigTypeDef = None,
    ) -> GetGatewayResponsesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`APIGateway.Client.get_gateway_responses`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/GetGatewayResponses>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              restApiId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type restApiId: string
        :param restApiId: **[REQUIRED]**

          [Required] The string identifier of the associated  RestApi .

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
                'items': [
                    {
                        'responseType':
                        'DEFAULT_4XX'|'DEFAULT_5XX'|'RESOURCE_NOT_FOUND'
                        |'UNAUTHORIZED'|'INVALID_API_KEY'|'ACCESS_DENIED'
                        |'AUTHORIZER_FAILURE'|'AUTHORIZER_CONFIGURATION_ERROR'
                        |'INVALID_SIGNATURE'|'EXPIRED_TOKEN'
                        |'MISSING_AUTHENTICATION_TOKEN'|'INTEGRATION_FAILURE'
                        |'INTEGRATION_TIMEOUT'|'API_CONFIGURATION_ERROR'
                        |'UNSUPPORTED_MEDIA_TYPE'|'BAD_REQUEST_PARAMETERS'
                        |'BAD_REQUEST_BODY'|'REQUEST_TOO_LARGE'|'THROTTLED'
                        |'QUOTA_EXCEEDED',
                        'statusCode': 'string',
                        'responseParameters': {
                            'string': 'string'
                        },
                        'responseTemplates': {
                            'string': 'string'
                        },
                        'defaultResponse': True|False
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            The collection of the  GatewayResponse instances of a  RestApi as a ``responseType``
            -to- GatewayResponse object map of key-value pairs. As such, pagination is not supported
            for querying this collection.

             For more information about valid gateway response types, see `Gateway Response Types
             Supported by API Gateway
             <https://docs.aws.amazon.com/apigateway/latest/developerguide/supported-gateway-response-types.html>`__
             Example: Get the collection of gateway responses of an API Request

            This example request shows how to retrieve the  GatewayResponses collection from an API.

             ``GET /restapis/o81lxisefl/gatewayresponses HTTP/1.1 Host:
             beta-apigateway.us-east-1.amazonaws.com Content-Type: application/json X-Amz-Date:
             20170503T220604Z Authorization: AWS4-HMAC-SHA256
             Credential={access-key-id}/20170503/us-east-1/apigateway/aws4_request,
             SignedHeaders=content-type;host;x-amz-date,
             Signature=59b42fe54a76a5de8adf2c67baa6d39206f8e9ad49a1d77ccc6a5da3103a398a
             Cache-Control: no-cache Postman-Token: 5637af27-dc29-fc5c-9dfe-0645d52cb515``

             Response

            The successful operation returns the ``200 OK`` status code and a payload similar to the
            following:

             ``{ "_links": { "curies": { "href":
             "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-gatewayresponse-{rel}.html",
             "name": "gatewayresponse", "templated": true }, "self": { "href":
             "/restapis/o81lxisefl/gatewayresponses" }, "first": { "href":
             "/restapis/o81lxisefl/gatewayresponses" }, "gatewayresponse:by-type": { "href":
             "/restapis/o81lxisefl/gatewayresponses/{response_type}", "templated": true }, "item": [
             { "href": "/restapis/o81lxisefl/gatewayresponses/INTEGRATION_FAILURE" }, { "href":
             "/restapis/o81lxisefl/gatewayresponses/RESOURCE_NOT_FOUND" }, { "href":
             "/restapis/o81lxisefl/gatewayresponses/REQUEST_TOO_LARGE" }, { "href":
             "/restapis/o81lxisefl/gatewayresponses/THROTTLED" }, { "href":
             "/restapis/o81lxisefl/gatewayresponses/UNSUPPORTED_MEDIA_TYPE" }, { "href":
             "/restapis/o81lxisefl/gatewayresponses/AUTHORIZER_CONFIGURATION_ERROR" }, { "href":
             "/restapis/o81lxisefl/gatewayresponses/DEFAULT_5XX" }, { "href":
             "/restapis/o81lxisefl/gatewayresponses/DEFAULT_4XX" }, { "href":
             "/restapis/o81lxisefl/gatewayresponses/BAD_REQUEST_PARAMETERS" }, { "href":
             "/restapis/o81lxisefl/gatewayresponses/BAD_REQUEST_BODY" }, { "href":
             "/restapis/o81lxisefl/gatewayresponses/EXPIRED_TOKEN" }, { "href":
             "/restapis/o81lxisefl/gatewayresponses/ACCESS_DENIED" }, { "href":
             "/restapis/o81lxisefl/gatewayresponses/INVALID_API_KEY" }, { "href":
             "/restapis/o81lxisefl/gatewayresponses/UNAUTHORIZED" }, { "href":
             "/restapis/o81lxisefl/gatewayresponses/API_CONFIGURATION_ERROR" }, { "href":
             "/restapis/o81lxisefl/gatewayresponses/QUOTA_EXCEEDED" }, { "href":
             "/restapis/o81lxisefl/gatewayresponses/INTEGRATION_TIMEOUT" }, { "href":
             "/restapis/o81lxisefl/gatewayresponses/MISSING_AUTHENTICATION_TOKEN" }, { "href":
             "/restapis/o81lxisefl/gatewayresponses/INVALID_SIGNATURE" }, { "href":
             "/restapis/o81lxisefl/gatewayresponses/AUTHORIZER_FAILURE" } ] }, "_embedded": {
             "item": [ { "_links": { "self": { "href":
             "/restapis/o81lxisefl/gatewayresponses/INTEGRATION_FAILURE" }, "gatewayresponse:put": {
             "href": "/restapis/o81lxisefl/gatewayresponses/{response_type}", "templated": true },
             "gatewayresponse:update": { "href":
             "/restapis/o81lxisefl/gatewayresponses/INTEGRATION_FAILURE" } }, "defaultResponse":
             true, "responseParameters": {}, "responseTemplates": { "application/json":
             "{\\"message\\":$context.error.messageString}" }, "responseType":
             "INTEGRATION_FAILURE", "statusCode": "504" }, { "_links": { "self": { "href":
             "/restapis/o81lxisefl/gatewayresponses/RESOURCE_NOT_FOUND" }, "gatewayresponse:put": {
             "href": "/restapis/o81lxisefl/gatewayresponses/{response_type}", "templated": true },
             "gatewayresponse:update": { "href":
             "/restapis/o81lxisefl/gatewayresponses/RESOURCE_NOT_FOUND" } }, "defaultResponse":
             true, "responseParameters": {}, "responseTemplates": { "application/json":
             "{\\"message\\":$context.error.messageString}" }, "responseType": "RESOURCE_NOT_FOUND",
             "statusCode": "404" }, { "_links": { "self": { "href":
             "/restapis/o81lxisefl/gatewayresponses/REQUEST_TOO_LARGE" }, "gatewayresponse:put": {
             "href": "/restapis/o81lxisefl/gatewayresponses/{response_type}", "templated": true },
             "gatewayresponse:update": { "href":
             "/restapis/o81lxisefl/gatewayresponses/REQUEST_TOO_LARGE" } }, "defaultResponse": true,
             "responseParameters": {}, "responseTemplates": { "application/json":
             "{\\"message\\":$context.error.messageString}" }, "responseType": "REQUEST_TOO_LARGE",
             "statusCode": "413" }, { "_links": { "self": { "href":
             "/restapis/o81lxisefl/gatewayresponses/THROTTLED" }, "gatewayresponse:put": { "href":
             "/restapis/o81lxisefl/gatewayresponses/{response_type}", "templated": true },
             "gatewayresponse:update": { "href": "/restapis/o81lxisefl/gatewayresponses/THROTTLED" }
             }, "defaultResponse": true, "responseParameters": {}, "responseTemplates": {
             "application/json": "{\\"message\\":$context.error.messageString}" }, "responseType":
             "THROTTLED", "statusCode": "429" }, { "_links": { "self": { "href":
             "/restapis/o81lxisefl/gatewayresponses/UNSUPPORTED_MEDIA_TYPE" },
             "gatewayresponse:put": { "href":
             "/restapis/o81lxisefl/gatewayresponses/{response_type}", "templated": true },
             "gatewayresponse:update": { "href":
             "/restapis/o81lxisefl/gatewayresponses/UNSUPPORTED_MEDIA_TYPE" } }, "defaultResponse":
             true, "responseParameters": {}, "responseTemplates": { "application/json":
             "{\\"message\\":$context.error.messageString}" }, "responseType":
             "UNSUPPORTED_MEDIA_TYPE", "statusCode": "415" }, { "_links": { "self": { "href":
             "/restapis/o81lxisefl/gatewayresponses/AUTHORIZER_CONFIGURATION_ERROR" },
             "gatewayresponse:put": { "href":
             "/restapis/o81lxisefl/gatewayresponses/{response_type}", "templated": true },
             "gatewayresponse:update": { "href":
             "/restapis/o81lxisefl/gatewayresponses/AUTHORIZER_CONFIGURATION_ERROR" } },
             "defaultResponse": true, "responseParameters": {}, "responseTemplates": {
             "application/json": "{\\"message\\":$context.error.messageString}" }, "responseType":
             "AUTHORIZER_CONFIGURATION_ERROR", "statusCode": "500" }, { "_links": { "self": {
             "href": "/restapis/o81lxisefl/gatewayresponses/DEFAULT_5XX" }, "gatewayresponse:put": {
             "href": "/restapis/o81lxisefl/gatewayresponses/{response_type}", "templated": true },
             "gatewayresponse:update": { "href": "/restapis/o81lxisefl/gatewayresponses/DEFAULT_5XX"
             } }, "defaultResponse": true, "responseParameters": {}, "responseTemplates": {
             "application/json": "{\\"message\\":$context.error.messageString}" }, "responseType":
             "DEFAULT_5XX" }, { "_links": { "self": { "href":
             "/restapis/o81lxisefl/gatewayresponses/DEFAULT_4XX" }, "gatewayresponse:put": { "href":
             "/restapis/o81lxisefl/gatewayresponses/{response_type}", "templated": true },
             "gatewayresponse:update": { "href": "/restapis/o81lxisefl/gatewayresponses/DEFAULT_4XX"
             } }, "defaultResponse": true, "responseParameters": {}, "responseTemplates": {
             "application/json": "{\\"message\\":$context.error.messageString}" }, "responseType":
             "DEFAULT_4XX" }, { "_links": { "self": { "href":
             "/restapis/o81lxisefl/gatewayresponses/BAD_REQUEST_PARAMETERS" },
             "gatewayresponse:put": { "href":
             "/restapis/o81lxisefl/gatewayresponses/{response_type}", "templated": true },
             "gatewayresponse:update": { "href":
             "/restapis/o81lxisefl/gatewayresponses/BAD_REQUEST_PARAMETERS" } }, "defaultResponse":
             true, "responseParameters": {}, "responseTemplates": { "application/json":
             "{\\"message\\":$context.error.messageString}" }, "responseType":
             "BAD_REQUEST_PARAMETERS", "statusCode": "400" }, { "_links": { "self": { "href":
             "/restapis/o81lxisefl/gatewayresponses/BAD_REQUEST_BODY" }, "gatewayresponse:put": {
             "href": "/restapis/o81lxisefl/gatewayresponses/{response_type}", "templated": true },
             "gatewayresponse:update": { "href":
             "/restapis/o81lxisefl/gatewayresponses/BAD_REQUEST_BODY" } }, "defaultResponse": true,
             "responseParameters": {}, "responseTemplates": { "application/json":
             "{\\"message\\":$context.error.messageString}" }, "responseType": "BAD_REQUEST_BODY",
             "statusCode": "400" }, { "_links": { "self": { "href":
             "/restapis/o81lxisefl/gatewayresponses/EXPIRED_TOKEN" }, "gatewayresponse:put": {
             "href": "/restapis/o81lxisefl/gatewayresponses/{response_type}", "templated": true },
             "gatewayresponse:update": { "href":
             "/restapis/o81lxisefl/gatewayresponses/EXPIRED_TOKEN" } }, "defaultResponse": true,
             "responseParameters": {}, "responseTemplates": { "application/json":
             "{\\"message\\":$context.error.messageString}" }, "responseType": "EXPIRED_TOKEN",
             "statusCode": "403" }, { "_links": { "self": { "href":
             "/restapis/o81lxisefl/gatewayresponses/ACCESS_DENIED" }, "gatewayresponse:put": {
             "href": "/restapis/o81lxisefl/gatewayresponses/{response_type}", "templated": true },
             "gatewayresponse:update": { "href":
             "/restapis/o81lxisefl/gatewayresponses/ACCESS_DENIED" } }, "defaultResponse": true,
             "responseParameters": {}, "responseTemplates": { "application/json":
             "{\\"message\\":$context.error.messageString}" }, "responseType": "ACCESS_DENIED",
             "statusCode": "403" }, { "_links": { "self": { "href":
             "/restapis/o81lxisefl/gatewayresponses/INVALID_API_KEY" }, "gatewayresponse:put": {
             "href": "/restapis/o81lxisefl/gatewayresponses/{response_type}", "templated": true },
             "gatewayresponse:update": { "href":
             "/restapis/o81lxisefl/gatewayresponses/INVALID_API_KEY" } }, "defaultResponse": true,
             "responseParameters": {}, "responseTemplates": { "application/json":
             "{\\"message\\":$context.error.messageString}" }, "responseType": "INVALID_API_KEY",
             "statusCode": "403" }, { "_links": { "self": { "href":
             "/restapis/o81lxisefl/gatewayresponses/UNAUTHORIZED" }, "gatewayresponse:put": {
             "href": "/restapis/o81lxisefl/gatewayresponses/{response_type}", "templated": true },
             "gatewayresponse:update": { "href":
             "/restapis/o81lxisefl/gatewayresponses/UNAUTHORIZED" } }, "defaultResponse": true,
             "responseParameters": {}, "responseTemplates": { "application/json":
             "{\\"message\\":$context.error.messageString}" }, "responseType": "UNAUTHORIZED",
             "statusCode": "401" }, { "_links": { "self": { "href":
             "/restapis/o81lxisefl/gatewayresponses/API_CONFIGURATION_ERROR" },
             "gatewayresponse:put": { "href":
             "/restapis/o81lxisefl/gatewayresponses/{response_type}", "templated": true },
             "gatewayresponse:update": { "href":
             "/restapis/o81lxisefl/gatewayresponses/API_CONFIGURATION_ERROR" } }, "defaultResponse":
             true, "responseParameters": {}, "responseTemplates": { "application/json":
             "{\\"message\\":$context.error.messageString}" }, "responseType":
             "API_CONFIGURATION_ERROR", "statusCode": "500" }, { "_links": { "self": { "href":
             "/restapis/o81lxisefl/gatewayresponses/QUOTA_EXCEEDED" }, "gatewayresponse:put": {
             "href": "/restapis/o81lxisefl/gatewayresponses/{response_type}", "templated": true },
             "gatewayresponse:update": { "href":
             "/restapis/o81lxisefl/gatewayresponses/QUOTA_EXCEEDED" } }, "defaultResponse": true,
             "responseParameters": {}, "responseTemplates": { "application/json":
             "{\\"message\\":$context.error.messageString}" }, "responseType": "QUOTA_EXCEEDED",
             "statusCode": "429" }, { "_links": { "self": { "href":
             "/restapis/o81lxisefl/gatewayresponses/INTEGRATION_TIMEOUT" }, "gatewayresponse:put": {
             "href": "/restapis/o81lxisefl/gatewayresponses/{response_type}", "templated": true },
             "gatewayresponse:update": { "href":
             "/restapis/o81lxisefl/gatewayresponses/INTEGRATION_TIMEOUT" } }, "defaultResponse":
             true, "responseParameters": {}, "responseTemplates": { "application/json":
             "{\\"message\\":$context.error.messageString}" }, "responseType":
             "INTEGRATION_TIMEOUT", "statusCode": "504" }, { "_links": { "self": { "href":
             "/restapis/o81lxisefl/gatewayresponses/MISSING_AUTHENTICATION_TOKEN" },
             "gatewayresponse:put": { "href":
             "/restapis/o81lxisefl/gatewayresponses/{response_type}", "templated": true },
             "gatewayresponse:update": { "href":
             "/restapis/o81lxisefl/gatewayresponses/MISSING_AUTHENTICATION_TOKEN" } },
             "defaultResponse": true, "responseParameters": {}, "responseTemplates": {
             "application/json": "{\\"message\\":$context.error.messageString}" }, "responseType":
             "MISSING_AUTHENTICATION_TOKEN", "statusCode": "403" }, { "_links": { "self": { "href":
             "/restapis/o81lxisefl/gatewayresponses/INVALID_SIGNATURE" }, "gatewayresponse:put": {
             "href": "/restapis/o81lxisefl/gatewayresponses/{response_type}", "templated": true },
             "gatewayresponse:update": { "href":
             "/restapis/o81lxisefl/gatewayresponses/INVALID_SIGNATURE" } }, "defaultResponse": true,
             "responseParameters": {}, "responseTemplates": { "application/json":
             "{\\"message\\":$context.error.messageString}" }, "responseType": "INVALID_SIGNATURE",
             "statusCode": "403" }, { "_links": { "self": { "href":
             "/restapis/o81lxisefl/gatewayresponses/AUTHORIZER_FAILURE" }, "gatewayresponse:put": {
             "href": "/restapis/o81lxisefl/gatewayresponses/{response_type}", "templated": true },
             "gatewayresponse:update": { "href":
             "/restapis/o81lxisefl/gatewayresponses/AUTHORIZER_FAILURE" } }, "defaultResponse":
             true, "responseParameters": {}, "responseTemplates": { "application/json":
             "{\\"message\\":$context.error.messageString}" }, "responseType": "AUTHORIZER_FAILURE",
             "statusCode": "500" } ] } }``

                `Customize Gateway Responses
                <https://docs.aws.amazon.com/apigateway/latest/developerguide/customize-gateway-responses.html>`__

            - **items** *(list) --*

              Returns the entire collection, because of no pagination support.

              - *(dict) --*

                A gateway response of a given response type and status code, with optional response
                parameters and mapping templates.

                 For more information about valid gateway response types, see `Gateway Response
                 Types Supported by API Gateway
                 <https://docs.aws.amazon.com/apigateway/latest/developerguide/supported-gateway-response-types.html>`__
                 Example: Get a Gateway Response of a given response type Request

                This example shows how to get a gateway response of the
                ``MISSING_AUTHENTICATION_TOKEN`` type.

                 ``GET /restapis/o81lxisefl/gatewayresponses/MISSING_AUTHENTICATION_TOKEN HTTP/1.1
                 Host: beta-apigateway.us-east-1.amazonaws.com Content-Type: application/json
                 X-Amz-Date: 20170503T202516Z Authorization: AWS4-HMAC-SHA256
                 Credential={access-key-id}/20170503/us-east-1/apigateway/aws4_request,
                 SignedHeaders=content-type;host;x-amz-date,
                 Signature=1b52460e3159c1a26cff29093855d50ea141c1c5b937528fecaf60f51129697a
                 Cache-Control: no-cache Postman-Token: 3b2a1ce9-c848-2e26-2e2f-9c2caefbed45``

                The response type is specified as a URL path.

                 Response

                The successful operation returns the ``200 OK`` status code and a payload similar to
                the following:

                 ``{ "_links": { "curies": { "href":
                 "http://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-gatewayresponse-{rel}.html",
                 "name": "gatewayresponse", "templated": true }, "self": { "href":
                 "/restapis/o81lxisefl/gatewayresponses/MISSING_AUTHENTICATION_TOKEN" },
                 "gatewayresponse:delete": { "href":
                 "/restapis/o81lxisefl/gatewayresponses/MISSING_AUTHENTICATION_TOKEN" },
                 "gatewayresponse:put": { "href":
                 "/restapis/o81lxisefl/gatewayresponses/{response_type}", "templated": true },
                 "gatewayresponse:update": { "href":
                 "/restapis/o81lxisefl/gatewayresponses/MISSING_AUTHENTICATION_TOKEN" } },
                 "defaultResponse": false, "responseParameters": {
                 "gatewayresponse.header.x-request-path": "method.request.path.petId",
                 "gatewayresponse.header.Access-Control-Allow-Origin": "'a.b.c'",
                 "gatewayresponse.header.x-request-query": "method.request.querystring.q",
                 "gatewayresponse.header.x-request-header": "method.request.header.Accept" },
                 "responseTemplates": { "application/json": "{\\n \\"message\\":
                 $context.error.messageString,\\n \\"type\\": \\"$context.error.responseType\\",\\n
                 \\"stage\\": \\"$context.stage\\",\\n \\"resourcePath\\":
                 \\"$context.resourcePath\\",\\n \\"stageVariables.a\\": \\"$stageVariables.a\\",\\n
                 \\"statusCode\\": \\"'404'\\"\\n}" }, "responseType":
                 "MISSING_AUTHENTICATION_TOKEN", "statusCode": "404" }``

                    `Customize Gateway Responses
                    <https://docs.aws.amazon.com/apigateway/latest/developerguide/customize-gateway-responses.html>`__

                - **responseType** *(string) --*

                  The response type of the associated  GatewayResponse . Valid values are

                  * ACCESS_DENIED

                  * API_CONFIGURATION_ERROR

                  * AUTHORIZER_FAILURE

                  * AUTHORIZER_CONFIGURATION_ERROR

                  * BAD_REQUEST_PARAMETERS

                  * BAD_REQUEST_BODY

                  * DEFAULT_4XX

                  * DEFAULT_5XX

                  * EXPIRED_TOKEN

                  * INVALID_SIGNATURE

                  * INTEGRATION_FAILURE

                  * INTEGRATION_TIMEOUT

                  * INVALID_API_KEY

                  * MISSING_AUTHENTICATION_TOKEN

                  * QUOTA_EXCEEDED

                  * REQUEST_TOO_LARGE

                  * RESOURCE_NOT_FOUND

                  * THROTTLED

                  * UNAUTHORIZED

                  * UNSUPPORTED_MEDIA_TYPE

                - **statusCode** *(string) --*

                  The HTTP status code for this  GatewayResponse .

                - **responseParameters** *(dict) --*

                  Response parameters (paths, query strings and headers) of the  GatewayResponse as
                  a string-to-string map of key-value pairs.

                  - *(string) --*

                    - *(string) --*

                - **responseTemplates** *(dict) --*

                  Response templates of the  GatewayResponse as a string-to-string map of key-value
                  pairs.

                  - *(string) --*

                    - *(string) --*

                - **defaultResponse** *(boolean) --*

                  A Boolean flag to indicate whether this  GatewayResponse is the default gateway
                  response (``true`` ) or not (``false`` ). A default gateway response is one
                  generated by API Gateway without any customization by an API developer.

            - **NextToken** *(string) --*

              A token to resume pagination.
        """


class GetModelsPaginator(Boto3Paginator):
    """
    Paginator for `get_models`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, restApiId: str, PaginationConfig: GetModelsPaginatePaginationConfigTypeDef = None
    ) -> GetModelsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`APIGateway.Client.get_models`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/GetModels>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              restApiId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type restApiId: string
        :param restApiId: **[REQUIRED]**

          [Required] The string identifier of the associated  RestApi .

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
                'items': [
                    {
                        'id': 'string',
                        'name': 'string',
                        'description': 'string',
                        'schema': 'string',
                        'contentType': 'string'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Represents a collection of  Model resources.

               Method ,  MethodResponse , `Models and Mappings
               <https://docs.aws.amazon.com/apigateway/latest/developerguide/models-mappings.html>`__

            - **items** *(list) --*

              The current page of elements from this collection.

              - *(dict) --*

                Represents the data structure of a method's request or response payload.

                A request model defines the data structure of the client-supplied request payload. A
                response model defines the data structure of the response payload returned by the
                back end. Although not required, models are useful for mapping payloads between the
                front end and back end.

                A model is used for generating an API's SDK, validating the input request body, and
                creating a skeletal mapping template.

                    Method ,  MethodResponse , `Models and Mappings
                    <https://docs.aws.amazon.com/apigateway/latest/developerguide/models-mappings.html>`__

                - **id** *(string) --*

                  The identifier for the model resource.

                - **name** *(string) --*

                  The name of the model. Must be an alphanumeric string.

                - **description** *(string) --*

                  The description of the model.

                - **schema** *(string) --*

                  The schema for the model. For ``application/json`` models, this should be `JSON
                  schema draft 4 <https://tools.ietf.org/html/draft-zyp-json-schema-04>`__ model. Do
                  not include "\\*/" characters in the description of any properties because such
                  "\\*/" characters may be interpreted as the closing marker for comments in some
                  languages, such as Java or JavaScript, causing the installation of your API's SDK
                  generated by API Gateway to fail.

                - **contentType** *(string) --*

                  The content-type for the model.

            - **NextToken** *(string) --*

              A token to resume pagination.
        """


class GetRequestValidatorsPaginator(Boto3Paginator):
    """
    Paginator for `get_request_validators`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        restApiId: str,
        PaginationConfig: GetRequestValidatorsPaginatePaginationConfigTypeDef = None,
    ) -> GetRequestValidatorsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`APIGateway.Client.get_request_validators`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/GetRequestValidators>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              restApiId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type restApiId: string
        :param restApiId: **[REQUIRED]**

          [Required] The string identifier of the associated  RestApi .

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
                'items': [
                    {
                        'id': 'string',
                        'name': 'string',
                        'validateRequestBody': True|False,
                        'validateRequestParameters': True|False
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            A collection of  RequestValidator resources of a given  RestApi .

            In OpenAPI, the  RequestValidators of an API is defined by the
            `x-amazon-apigateway-request-validators
            <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions.html#api-gateway-swagger-extensions-request-validators.html>`__
            extension.

              `Enable Basic Request Validation in API Gateway
              <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-method-request-validation.html>`__

            - **items** *(list) --*

              The current page of elements from this collection.

              - *(dict) --*

                A set of validation rules for incoming  Method requests.

                In OpenAPI, a  RequestValidator of an API is defined by the
                `x-amazon-apigateway-request-validators.requestValidator
                <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions.html#api-gateway-swagger-extensions-request-validators.requestValidator.html>`__
                object. It the referenced using the `x-amazon-apigateway-request-validator
                <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-swagger-extensions.html#api-gateway-swagger-extensions-request-validator>`__
                property.

                  `Enable Basic Request Validation in API Gateway
                  <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-method-request-validation.html>`__

                - **id** *(string) --*

                  The identifier of this  RequestValidator .

                - **name** *(string) --*

                  The name of this  RequestValidator

                - **validateRequestBody** *(boolean) --*

                  A Boolean flag to indicate whether to validate a request body according to the
                  configured  Model schema.

                - **validateRequestParameters** *(boolean) --*

                  A Boolean flag to indicate whether to validate request parameters (``true`` ) or
                  not (``false`` ).

            - **NextToken** *(string) --*

              A token to resume pagination.
        """


class GetResourcesPaginator(Boto3Paginator):
    """
    Paginator for `get_resources`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        restApiId: str,
        embed: List[str] = None,
        PaginationConfig: GetResourcesPaginatePaginationConfigTypeDef = None,
    ) -> GetResourcesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`APIGateway.Client.get_resources`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/GetResources>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              restApiId='string',
              embed=[
                  'string',
              ],
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type restApiId: string
        :param restApiId: **[REQUIRED]**

          [Required] The string identifier of the associated  RestApi .

        :type embed: list
        :param embed:

          A query parameter used to retrieve the specified resources embedded in the returned
          Resources resource in the response. This ``embed`` parameter value is a list of
          comma-separated strings. Currently, the request supports only retrieval of the embedded
          Method resources this way. The query parameter value must be a single-valued list and
          contain the ``"methods"`` string. For example, ``GET
          /restapis/{restapi_id}/resources?embed=methods`` .

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
                'items': [
                    {
                        'id': 'string',
                        'parentId': 'string',
                        'pathPart': 'string',
                        'path': 'string',
                        'resourceMethods': {
                            'string': {
                                'httpMethod': 'string',
                                'authorizationType': 'string',
                                'authorizerId': 'string',
                                'apiKeyRequired': True|False,
                                'requestValidatorId': 'string',
                                'operationName': 'string',
                                'requestParameters': {
                                    'string': True|False
                                },
                                'requestModels': {
                                    'string': 'string'
                                },
                                'methodResponses': {
                                    'string': {
                                        'statusCode': 'string',
                                        'responseParameters': {
                                            'string': True|False
                                        },
                                        'responseModels': {
                                            'string': 'string'
                                        }
                                    }
                                },
                                'methodIntegration': {
                                    'type': 'HTTP'|'AWS'|'MOCK'|'HTTP_PROXY'|'AWS_PROXY',
                                    'httpMethod': 'string',
                                    'uri': 'string',
                                    'connectionType': 'INTERNET'|'VPC_LINK',
                                    'connectionId': 'string',
                                    'credentials': 'string',
                                    'requestParameters': {
                                        'string': 'string'
                                    },
                                    'requestTemplates': {
                                        'string': 'string'
                                    },
                                    'passthroughBehavior': 'string',
                                    'contentHandling': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT',
                                    'timeoutInMillis': 123,
                                    'cacheNamespace': 'string',
                                    'cacheKeyParameters': [
                                        'string',
                                    ],
                                    'integrationResponses': {
                                        'string': {
                                            'statusCode': 'string',
                                            'selectionPattern': 'string',
                                            'responseParameters': {
                                                'string': 'string'
                                            },
                                            'responseTemplates': {
                                                'string': 'string'
                                            },
                                            'contentHandling': 'CONVERT_TO_BINARY'|'CONVERT_TO_TEXT'
                                        }
                                    }
                                },
                                'authorizationScopes': [
                                    'string',
                                ]
                            }
                        }
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Represents a collection of  Resource resources.

              `Create an API
              <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__

            - **items** *(list) --*

              The current page of elements from this collection.

              - *(dict) --*

                Represents an API resource.

                  `Create an API
                  <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__

                - **id** *(string) --*

                  The resource's identifier.

                - **parentId** *(string) --*

                  The parent resource's identifier.

                - **pathPart** *(string) --*

                  The last path segment for this resource.

                - **path** *(string) --*

                  The full path for this resource.

                - **resourceMethods** *(dict) --*

                  Gets an API resource's method of a given HTTP verb.

                  The resource methods are a map of methods indexed by methods' HTTP verbs enabled
                  on the resource. This method map is included in the ``200 OK`` response of the
                  ``GET /restapis/{restapi_id}/resources/{resource_id}`` or ``GET
                  /restapis/{restapi_id}/resources/{resource_id}?embed=methods`` request.

                   Example: Get the GET method of an API resource Request ``GET
                   /restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET HTTP/1.1 Content-Type:
                   application/json Host: apigateway.us-east-1.amazonaws.com X-Amz-Date:
                   20170223T031827Z Authorization: AWS4-HMAC-SHA256
                   Credential={access_key_ID}/20170223/us-east-1/apigateway/aws4_request,
                   SignedHeaders=content-type;host;x-amz-date, Signature=
                       {sig4_hash}``  Response ``{
                   "_links": { "curies": [ { "href":
                   "https://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-integration-{rel}.html",
                   "name": "integration", "templated": true }, { "href":
                   "https://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-integration-response-{rel}.html",
                   "name": "integrationresponse", "templated": true }, { "href":
                   "https://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-method-{rel}.html",
                   "name": "method", "templated": true }, { "href":
                   "https://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-method-response-{rel}.html",
                   "name": "methodresponse", "templated": true } ], "self": { "href":
                   "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET", "name": "GET", "title":
                   "GET" }, "integration:put": { "href":
                   "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" },
                   "method:delete": { "href":
                   "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET" }, "method:integration":
                   { "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" },
                   "method:responses": { "href":
                   "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200", "name":
                   "200", "title": "200" }, "method:update": { "href":
                   "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET" }, "methodresponse:put":
                   { "href":
                   "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/{status_code}",
                   "templated": true } }, "apiKeyRequired": false, "authorizationType": "NONE",
                   "httpMethod": "GET", "_embedded": { "method:integration": { "_links": { "self": {
                   "href": "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" },
                   "integration:delete": { "href":
                   "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" },
                   "integration:responses": { "href":
                   "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200",
                   "name": "200", "title": "200" }, "integration:update": { "href":
                   "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" },
                   "integrationresponse:put": { "href":
                   "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/{status_code}",
                   "templated": true } }, "cacheKeyParameters": [], "cacheNamespace": "3kzxbg5sa2",
                   "credentials": "arn:aws:iam::123456789012:role/apigAwsProxyRole", "httpMethod":
                   "POST", "passthroughBehavior": "WHEN_NO_MATCH", "requestParameters": {
                   "integration.request.header.Content-Type": "'application/x-amz-json-1.1'" },
                   "requestTemplates": { "application/json": "{\\n}" }, "type": "AWS", "uri":
                   "arn:aws:apigateway:us-east-1:kinesis:action/ListStreams", "_embedded": {
                   "integration:responses": { "_links": { "self": { "href":
                   "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200",
                   "name": "200", "title": "200" }, "integrationresponse:delete": { "href":
                   "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200"
                   }, "integrationresponse:update": { "href":
                   "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200"
                   } }, "responseParameters": { "method.response.header.Content-Type":
                   "'application/xml'" }, "responseTemplates": { "application/json":
                   "$util.urlDecode(\\"%3CkinesisStreams%3E#foreach($stream in
                   $input.path('$.StreamNames'))%3Cstream%3E%3Cname%3E$stream%3C/name%3E%3C/stream%3E#end%3C/kinesisStreams%3E\\")\\n"
                   }, "statusCode": "200" } } }, "method:responses": { "_links": { "self": { "href":
                   "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200", "name":
                   "200", "title": "200" }, "methodresponse:delete": { "href":
                   "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200" },
                   "methodresponse:update": { "href":
                   "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200" } },
                   "responseModels": { "application/json": "Empty" }, "responseParameters": {
                   "method.response.header.Content-Type": false }, "statusCode": "200" } } }``

                  If the ``OPTIONS`` is enabled on the resource, you can follow the example here to
                  get that method. Just replace the ``GET`` of the last path segment in the request
                  URL with ``OPTIONS`` .

                  - *(string) --*

                    - *(dict) --*

                      Represents a client-facing interface by which the client calls the API to
                      access back-end resources. A **Method** resource is integrated with an
                      Integration resource. Both consist of a request and one or more responses. The
                      method request takes the client input that is passed to the back end through
                      the integration request. A method response returns the output from the back
                      end to the client through an integration response. A method request is
                      embodied in a **Method** resource, whereas an integration request is embodied
                      in an  Integration resource. On the other hand, a method response is
                      represented by a  MethodResponse resource, whereas an integration response is
                      represented by an  IntegrationResponse resource.

                       Example: Retrive the GET method on a specified resource Request

                      The following example request retrieves the information about the GET method
                      on an API resource (``3kzxbg5sa2`` ) of an API (``fugvjdxtri`` ).

                       ``GET /restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET HTTP/1.1
                       Content-Type: application/json Host: apigateway.us-east-1.amazonaws.com
                       X-Amz-Date: 20160603T210259Z Authorization: AWS4-HMAC-SHA256
                       Credential=
                           {access_key_ID}/20160603/us-east-1/apigateway/aws4_request,
                       SignedHeaders=content-type;host;x-amz-date, Signature=
                           {sig4_hash}``  Response

                      The successful response returns a ``200 OK`` status code and a payload similar
                      to the following:

                       ``{ "_links": { "curies": [ { "href":
                       "https://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-integration-{rel}.html",
                       "name": "integration", "templated": true }, { "href":
                       "https://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-integration-response-{rel}.html",
                       "name": "integrationresponse", "templated": true }, { "href":
                       "https://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-method-{rel}.html",
                       "name": "method", "templated": true }, { "href":
                       "https://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-method-response-{rel}.html",
                       "name": "methodresponse", "templated": true } ], "self": { "href":
                       "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET", "name": "GET",
                       "title": "GET" }, "integration:put": { "href":
                       "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" },
                       "method:delete": { "href":
                       "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET" },
                       "method:integration": { "href":
                       "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" },
                       "method:responses": { "href":
                       "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200",
                       "name": "200", "title": "200" }, "method:update": { "href":
                       "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET" },
                       "methodresponse:put": { "href":
                       "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/{status_code}",
                       "templated": true } }, "apiKeyRequired": true, "authorizationType": "NONE",
                       "httpMethod": "GET", "_embedded": { "method:integration": { "_links": {
                       "self": { "href":
                       "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" },
                       "integration:delete": { "href":
                       "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" },
                       "integration:responses": { "href":
                       "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200",
                       "name": "200", "title": "200" }, "integration:update": { "href":
                       "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration" },
                       "integrationresponse:put": { "href":
                       "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/{status_code}",
                       "templated": true } }, "cacheKeyParameters": [], "cacheNamespace":
                       "3kzxbg5sa2", "credentials":
                       "arn:aws:iam::123456789012:role/apigAwsProxyRole", "httpMethod": "POST",
                       "passthroughBehavior": "WHEN_NO_MATCH", "requestParameters": {
                       "integration.request.header.Content-Type": "'application/x-amz-json-1.1'" },
                       "requestTemplates": { "application/json": "{\\n}" }, "type": "AWS", "uri":
                       "arn:aws:apigateway:us-east-1:kinesis:action/ListStreams", "_embedded": {
                       "integration:responses": { "_links": { "self": { "href":
                       "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200",
                       "name": "200", "title": "200" }, "integrationresponse:delete": { "href":
                       "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200"
                       }, "integrationresponse:update": { "href":
                       "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200"
                       } }, "responseParameters": { "method.response.header.Content-Type":
                       "'application/xml'" }, "responseTemplates": { "application/json":
                       "$util.urlDecode(\\"%3CkinesisStreams%3E%23foreach(%24stream%20in%20%24input.path(%27%24.StreamNames%27))%3Cstream%3E%3Cname%3E%24stream%3C%2Fname%3E%3C%2Fstream%3E%23end%3C%2FkinesisStreams%3E\\")"
                       }, "statusCode": "200" } } }, "method:responses": { "_links": { "self": {
                       "href":
                       "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200",
                       "name": "200", "title": "200" }, "methodresponse:delete": { "href":
                       "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200" },
                       "methodresponse:update": { "href":
                       "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200" } },
                       "responseModels": { "application/json": "Empty" }, "responseParameters": {
                       "method.response.header.Content-Type": false }, "statusCode": "200" } } }``

                      In the example above, the response template for the ``200 OK`` response maps
                      the JSON output from the ``ListStreams`` action in the back end to an XML
                      output. The mapping template is URL-encoded as
                      ``%3CkinesisStreams%3E%23foreach(%24stream%20in%20%24input.path(%27%24.StreamNames%27))%3Cstream%3E%3Cname%3E%24stream%3C%2Fname%3E%3C%2Fstream%3E%23end%3C%2FkinesisStreams%3E``
                      and the output is decoded using the `$util.urlDecode()
                      <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-mapping-template-reference.html#util-templat-reference>`__
                      helper function.

                          MethodResponse ,  Integration ,  IntegrationResponse ,  Resource , `Set up
                          an API's method
                          <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-method-settings.html>`__

                      - **httpMethod** *(string) --*

                        The method's HTTP verb.

                      - **authorizationType** *(string) --*

                        The method's authorization type. Valid values are ``NONE`` for open access,
                        ``AWS_IAM`` for using AWS IAM permissions, ``CUSTOM`` for using a custom
                        authorizer, or ``COGNITO_USER_POOLS`` for using a Cognito user pool.

                      - **authorizerId** *(string) --*

                        The identifier of an  Authorizer to use on this method. The
                        ``authorizationType`` must be ``CUSTOM`` .

                      - **apiKeyRequired** *(boolean) --*

                        A boolean flag specifying whether a valid  ApiKey is required to invoke this
                        method.

                      - **requestValidatorId** *(string) --*

                        The identifier of a  RequestValidator for request validation.

                      - **operationName** *(string) --*

                        A human-friendly operation identifier for the method. For example, you can
                        assign the ``operationName`` of ``ListPets`` for the ``GET /pets`` method in
                        the ``PetStore`` example.

                      - **requestParameters** *(dict) --*

                        A key-value map defining required or optional method request parameters that
                        can be accepted by API Gateway. A key is a method request parameter name
                        matching the pattern of ``method.request.{location}.{name}`` , where
                        ``location`` is ``querystring`` , ``path`` , or ``header`` and ``name`` is a
                        valid and unique parameter name. The value associated with the key is a
                        Boolean flag indicating whether the parameter is required (``true`` ) or
                        optional (``false`` ). The method request parameter names defined here are
                        available in  Integration to be mapped to integration request parameters or
                        templates.

                        - *(string) --*

                          - *(boolean) --*

                      - **requestModels** *(dict) --*

                        A key-value map specifying data schemas, represented by  Model resources,
                        (as the mapped value) of the request payloads of given content types (as the
                        mapping key).

                        - *(string) --*

                          - *(string) --*

                      - **methodResponses** *(dict) --*

                        Gets a method response associated with a given HTTP status code.

                        The collection of method responses are encapsulated in a key-value map,
                        where the key is a response's HTTP status code and the value is a
                        MethodResponse resource that specifies the response returned to the caller
                        from the back end through the integration response.

                         Example: Get a 200 OK response of a GET method Request

                         ``GET /restapis/uojnr9hd57/resources/0cjtch/methods/GET/responses/200
                         HTTP/1.1 Content-Type: application/json Host:
                         apigateway.us-east-1.amazonaws.com Content-Length: 117 X-Amz-Date:
                         20160613T215008Z Authorization: AWS4-HMAC-SHA256
                         Credential=
                             {access_key_ID}/20160613/us-east-1/apigateway/aws4_request,
                         SignedHeaders=content-type;host;x-amz-date, Signature=
                             {sig4_hash}``
                         Response

                        The successful response returns a ``200 OK`` status code and a payload
                        similar to the following:

                         ``{ "_links": { "curies": { "href":
                         "https://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-method-response-{rel}.html",
                         "name": "methodresponse", "templated": true }, "self": { "href":
                         "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/responses/200", "title":
                         "200" }, "methodresponse:delete": { "href":
                         "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/responses/200" },
                         "methodresponse:update": { "href":
                         "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/responses/200" } },
                         "responseModels": { "application/json": "Empty" }, "responseParameters": {
                         "method.response.header.operator": false,
                         "method.response.header.operand_2": false,
                         "method.response.header.operand_1": false }, "statusCode": "200" }``

                           `AWS CLI
                           <https://docs.aws.amazon.com/cli/latest/reference/apigateway/get-method-response.html>`__

                        - *(string) --*

                          - *(dict) --*

                            Represents a method response of a given HTTP status code returned to the
                            client. The method response is passed from the back end through the
                            associated integration response that can be transformed using a mapping
                            template.

                             Example: A **MethodResponse** instance of an API Request

                            The example request retrieves a **MethodResponse** of the 200 status
                            code.

                             ``GET
                             /restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200
                             HTTP/1.1 Content-Type: application/json Host:
                             apigateway.us-east-1.amazonaws.com X-Amz-Date: 20160603T222952Z
                             Authorization: AWS4-HMAC-SHA256
                             Credential=
                                 {access_key_ID}/20160603/us-east-1/apigateway/aws4_request,
                             SignedHeaders=
                                 content-type;host;x-amz-date, Signature=
                                     {sig4_hash}``
                             Response

                            The successful response returns ``200 OK`` status and a payload as
                            follows:

                             ``{ "_links": { "curies": { "href":
                             "https://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-method-response-{rel}.html",
                             "name": "methodresponse", "templated": true }, "self": { "href":
                             "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200",
                             "title": "200" }, "methodresponse:delete": { "href":
                             "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200"
                             }, "methodresponse:update": { "href":
                             "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/responses/200" }
                             }, "responseModels": { "application/json": "Empty" },
                             "responseParameters": { "method.response.header.Content-Type": false },
                             "statusCode": "200" }``

                                Method ,  IntegrationResponse ,  Integration  `Creating an API
                                <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__

                            - **statusCode** *(string) --*

                              The method response's status code.

                            - **responseParameters** *(dict) --*

                              A key-value map specifying required or optional response parameters
                              that API Gateway can send back to the caller. A key defines a method
                              response header and the value specifies whether the associated method
                              response header is required or not. The expression of the key must
                              match the pattern ``method.response.header.{name}`` , where ``name``
                              is a valid and unique header name. API Gateway passes certain
                              integration response data to the method response headers specified
                              here according to the mapping you prescribe in the API's
                              IntegrationResponse . The integration response data that can be mapped
                              include an integration response header expressed in
                              ``integration.response.header.{name}`` , a static value enclosed
                              within a pair of single quotes (e.g., ``'application/json'`` ), or a
                              JSON expression from the back-end response payload in the form of
                              ``integration.response.body.{JSON-expression}`` , where
                              ``JSON-expression`` is a valid JSON expression without the ``$``
                              prefix.)

                              - *(string) --*

                                - *(boolean) --*

                            - **responseModels** *(dict) --*

                              Specifies the  Model resources used for the response's content-type.
                              Response models are represented as a key/value map, with a
                              content-type as the key and a  Model name as the value.

                              - *(string) --*

                                - *(string) --*

                      - **methodIntegration** *(dict) --*

                        Gets the method's integration responsible for passing the client-submitted
                        request to the back end and performing necessary transformations to make the
                        request compliant with the back end.

                         Example:  Request

                         ``GET /restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration
                         HTTP/1.1 Content-Type: application/json Host:
                         apigateway.us-east-1.amazonaws.com Content-Length: 117 X-Amz-Date:
                         20160613T213210Z Authorization: AWS4-HMAC-SHA256
                         Credential=
                             {access_key_ID}/20160613/us-east-1/apigateway/aws4_request,
                         SignedHeaders=content-type;host;x-amz-date, Signature=
                             {sig4_hash}``
                         Response

                        The successful response returns a ``200 OK`` status code and a payload
                        similar to the following:

                         ``{ "_links": { "curies": [ { "href":
                         "https://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-integration-{rel}.html",
                         "name": "integration", "templated": true }, { "href":
                         "https://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-integration-response-{rel}.html",
                         "name": "integrationresponse", "templated": true } ], "self": { "href":
                         "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration" },
                         "integration:delete": { "href":
                         "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration" },
                         "integration:responses": { "href":
                         "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration/responses/200",
                         "name": "200", "title": "200" }, "integration:update": { "href":
                         "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration" },
                         "integrationresponse:put": { "href":
                         "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration/responses/{status_code}",
                         "templated": true } }, "cacheKeyParameters": [], "cacheNamespace":
                         "0cjtch", "credentials": "arn:aws:iam::123456789012:role/apigAwsProxyRole",
                         "httpMethod": "POST", "passthroughBehavior": "WHEN_NO_MATCH",
                         "requestTemplates": { "application/json": "{\\n \\"a\\":
                         \\"$input.params('operand1')\\",\\n \\"b\\":
                         \\"$input.params('operand2')\\", \\n \\"op\\":
                         \\"$input.params('operator')\\" \\n}" }, "type": "AWS", "uri":
                         "arn:aws:apigateway:us-west-2:lambda:path//2015-03-31/functions/arn:aws:lambda:us-west-2:123456789012:function:Calc/invocations",
                         "_embedded": { "integration:responses": { "_links": { "self": { "href":
                         "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration/responses/200",
                         "name": "200", "title": "200" }, "integrationresponse:delete": { "href":
                         "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration/responses/200"
                         }, "integrationresponse:update": { "href":
                         "/restapis/uojnr9hd57/resources/0cjtch/methods/GET/integration/responses/200"
                         } }, "responseParameters": { "method.response.header.operator":
                         "integration.response.body.op", "method.response.header.operand_2":
                         "integration.response.body.b", "method.response.header.operand_1":
                         "integration.response.body.a" }, "responseTemplates": { "application/json":
                         "#set($res =
                              $input.path('$'))\\n{\\n \\"result\\": \\"$res.a, $res.b,
                         $res.op =
                             > $res.c\\",\\n \\"a\\" : \\"$res.a\\",\\n \\"b\\" :
                         \\"$res.b\\",\\n \\"op\\" : \\"$res.op\\",\\n \\"c\\" : \\"$res.c\\"\\n}"
                         }, "selectionPattern": "", "statusCode": "200" } } }``

                           `AWS CLI
                           <https://docs.aws.amazon.com/cli/latest/reference/apigateway/get-integration.html>`__

                        - **type** *(string) --*

                          Specifies an API method integration type. The valid value is one of the
                          following:

                          * ``AWS`` : for integrating the API method request with an AWS service
                          action, including the Lambda function-invoking action. With the Lambda
                          function-invoking action, this is referred to as the Lambda custom
                          integration. With any other AWS service action, this is known as AWS
                          integration.

                          * ``AWS_PROXY`` : for integrating the API method request with the Lambda
                          function-invoking action with the client request passed through as-is.
                          This integration is also referred to as the Lambda proxy integration.

                          * ``HTTP`` : for integrating the API method request with an HTTP endpoint,
                          including a private HTTP endpoint within a VPC. This integration is also
                          referred to as the HTTP custom integration.

                          * ``HTTP_PROXY`` : for integrating the API method request with an HTTP
                          endpoint, including a private HTTP endpoint within a VPC, with the client
                          request passed through as-is. This is also referred to as the HTTP proxy
                          integration.

                          * ``MOCK`` : for integrating the API method request with API Gateway as a
                          "loop-back" endpoint without invoking any backend.

                          For the HTTP and HTTP proxy integrations, each integration can specify a
                          protocol (``http/https`` ), port and path. Standard 80 and 443 ports are
                          supported as well as custom ports above 1024. An HTTP or HTTP proxy
                          integration with a ``connectionType`` of ``VPC_LINK`` is referred to as a
                          private integration and uses a  VpcLink to connect API Gateway to a
                          network load balancer of a VPC.

                        - **httpMethod** *(string) --*

                          Specifies the integration's HTTP method type.

                        - **uri** *(string) --*

                          Specifies Uniform Resource Identifier (URI) of the integration endpoint.

                          * For ``HTTP`` or ``HTTP_PROXY`` integrations, the URI must be a fully
                          formed, encoded HTTP(S) URL according to the `RFC-3986 specification
                          <https://en.wikipedia.org/wiki/Uniform_Resource_Identifier>`__ , for
                          either standard integration, where ``connectionType`` is not ``VPC_LINK``
                          , or private integration, where ``connectionType`` is ``VPC_LINK`` . For a
                          private HTTP integration, the URI is not used for routing.

                          * For ``AWS`` or ``AWS_PROXY`` integrations, the URI is of the form
                          ``arn:aws:apigateway:{region}:{subdomain.service
                          |service}:path|action/{service_api}``
                          . Here, ``{Region}`` is the API Gateway region (e.g., ``us-east-1`` );
                          ``{service}`` is the name of the integrated AWS service (e.g., ``s3`` );
                          and ``{subdomain}`` is a designated subdomain supported by certain AWS
                          service for fast host-name lookup. ``action`` can be used for an AWS
                          service action-based API, using an ``Action={name}&{p1}=
                              {v1}&p2={v2}...``
                          query string. The ensuing ``{service_api}`` refers to a supported action
                          ``{name}`` plus any required input parameters. Alternatively, ``path`` can
                          be used for an AWS service path-based API. The ensuing ``service_api``
                          refers to the path to an AWS service resource, including the region of the
                          integrated AWS service, if applicable. For example, for integration with
                          the S3 API of ```GetObject
                          <https://docs.aws.amazon.com/AmazonS3/latest/API/RESTObjectGET.html>`__``
                          , the ``uri`` can be either
                          ``arn:aws:apigateway:us-west-2:s3:action/GetObject&Bucket={bucket}&Key={key}``
                          or ``arn:aws:apigateway:us-west-2:s3:path/{bucket}/{key}``

                        - **connectionType** *(string) --*

                          The type of the network connection to the integration endpoint. The valid
                          value is ``INTERNET`` for connections through the public routable internet
                          or ``VPC_LINK`` for private connections between API Gateway and a network
                          load balancer in a VPC. The default value is ``INTERNET`` .

                        - **connectionId** *(string) --*

                          The (```id``
                          <https://docs.aws.amazon.com/apigateway/api-reference/resource/vpc-link/#id>`__
                          ) of the  VpcLink used for the integration when
                          ``connectionType=VPC_LINK`` and undefined, otherwise.

                        - **credentials** *(string) --*

                          Specifies the credentials required for the integration, if any. For AWS
                          integrations, three options are available. To specify an IAM Role for API
                          Gateway to assume, use the role's Amazon Resource Name (ARN). To require
                          that the caller's identity be passed through from the request, specify the
                          string ``arn:aws:iam::\\*:user/\\*`` . To use resource-based permissions
                          on supported AWS services, specify null.

                        - **requestParameters** *(dict) --*

                          A key-value map specifying request parameters that are passed from the
                          method request to the back end. The key is an integration request
                          parameter name and the associated value is a method request parameter
                          value or static value that must be enclosed within single quotes and
                          pre-encoded as required by the back end. The method request parameter
                          value must match the pattern of ``method.request.{location}.{name}`` ,
                          where ``location`` is ``querystring`` , ``path`` , or ``header`` and
                          ``name`` must be a valid and unique method request parameter name.

                          - *(string) --*

                            - *(string) --*

                        - **requestTemplates** *(dict) --*

                          Represents a map of Velocity templates that are applied on the request
                          payload based on the value of the Content-Type header sent by the client.
                          The content type value is the key in this map, and the template (as a
                          String) is the value.

                          - *(string) --*

                            - *(string) --*

                        - **passthroughBehavior** *(string) --*

                          Specifies how the method request body of an unmapped content type will be
                          passed through the integration request to the back end without
                          transformation. A content type is unmapped if no mapping template is
                          defined in the integration or the content type does not match any of the
                          mapped content types, as specified in ``requestTemplates`` . The valid
                          value is one of the following:

                          * ``WHEN_NO_MATCH`` : passes the method request body through the
                          integration request to the back end without transformation when the method
                          request content type does not match any content type associated with the
                          mapping templates defined in the integration request.

                          * ``WHEN_NO_TEMPLATES`` : passes the method request body through the
                          integration request to the back end without transformation when no mapping
                          template is defined in the integration request. If a template is defined
                          when this option is selected, the method request of an unmapped
                          content-type will be rejected with an HTTP ``415 Unsupported Media Type``
                          response.

                          * ``NEVER`` : rejects the method request with an HTTP ``415 Unsupported
                          Media Type`` response when either the method request content type does not
                          match any content type associated with the mapping templates defined in
                          the integration request or no mapping template is defined in the
                          integration request.

                        - **contentHandling** *(string) --*

                          Specifies how to handle request payload content type conversions.
                          Supported values are ``CONVERT_TO_BINARY`` and ``CONVERT_TO_TEXT`` , with
                          the following behaviors:

                          * ``CONVERT_TO_BINARY`` : Converts a request payload from a Base64-encoded
                          string to the corresponding binary blob.

                          * ``CONVERT_TO_TEXT`` : Converts a request payload from a binary blob to a
                          Base64-encoded string.

                          If this property is not defined, the request payload will be passed
                          through from the method request to integration request without
                          modification, provided that the ``passthroughBehavior`` is configured to
                          support payload pass-through.

                        - **timeoutInMillis** *(integer) --*

                          Custom timeout between 50 and 29,000 milliseconds. The default value is
                          29,000 milliseconds or 29 seconds.

                        - **cacheNamespace** *(string) --*

                          An API-specific tag group of related cached parameters. To be valid values
                          for ``cacheKeyParameters`` , these parameters must also be specified for
                          Method  ``requestParameters`` .

                        - **cacheKeyParameters** *(list) --*

                          A list of request parameters whose values API Gateway caches. To be valid
                          values for ``cacheKeyParameters`` , these parameters must also be
                          specified for  Method  ``requestParameters`` .

                          - *(string) --*

                        - **integrationResponses** *(dict) --*

                          Specifies the integration's responses.

                           Example: Get integration responses of a method Request

                           ``GET
                           /restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200
                           HTTP/1.1 Content-Type: application/json Host:
                           apigateway.us-east-1.amazonaws.com X-Amz-Date: 20160607T191449Z
                           Authorization: AWS4-HMAC-SHA256
                           Credential=
                               {access_key_ID}/20160607/us-east-1/apigateway/aws4_request,
                           SignedHeaders=content-type;host;x-amz-date, Signature=
                               {sig4_hash}``
                           Response

                          The successful response returns ``200 OK`` status and a payload as
                          follows:

                           ``{ "_links": { "curies": { "href":
                           "https://docs.aws.amazon.com/apigateway/latest/developerguide/restapi-integration-response-{rel}.html",
                           "name": "integrationresponse", "templated": true }, "self": { "href":
                           "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200",
                           "title": "200" }, "integrationresponse:delete": { "href":
                           "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200"
                           }, "integrationresponse:update": { "href":
                           "/restapis/fugvjdxtri/resources/3kzxbg5sa2/methods/GET/integration/responses/200"
                           } }, "responseParameters": { "method.response.header.Content-Type":
                           "'application/xml'" }, "responseTemplates": { "application/json":
                           "$util.urlDecode(\\"%3CkinesisStreams%3E#foreach($stream in
                           $input.path('$.StreamNames'))%3Cstream%3E%3Cname%3E$stream%3C/name%3E%3C/stream%3E#end%3C/kinesisStreams%3E\\")\\n"
                           }, "statusCode": "200" }``

                             `Creating an API
                             <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__

                          - *(string) --*

                            - *(dict) --*

                              Represents an integration response. The status code must map to an
                              existing  MethodResponse , and parameters and templates can be used to
                              transform the back-end response.

                                `Creating an API
                                <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__

                              - **statusCode** *(string) --*

                                Specifies the status code that is used to map the integration
                                response to an existing  MethodResponse .

                              - **selectionPattern** *(string) --*

                                Specifies the regular expression (regex) pattern used to choose an
                                integration response based on the response from the back end. For
                                example, if the success response returns nothing and the error
                                response returns some string, you could use the ``.+`` regex to
                                match error response. However, make sure that the error response
                                does not contain any newline (``\\n`` ) character in such cases. If
                                the back end is an AWS Lambda function, the AWS Lambda function
                                error header is matched. For all other HTTP and AWS back ends, the
                                HTTP status code is matched.

                              - **responseParameters** *(dict) --*

                                A key-value map specifying response parameters that are passed to
                                the method response from the back end. The key is a method response
                                header parameter name and the mapped value is an integration
                                response header value, a static value enclosed within a pair of
                                single quotes, or a JSON expression from the integration response
                                body. The mapping key must match the pattern of
                                ``method.response.header.{name}`` , where ``name`` is a valid and
                                unique header name. The mapped non-static value must match the
                                pattern of ``integration.response.header.{name}`` or
                                ``integration.response.body.{JSON-expression}`` , where ``name`` is
                                a valid and unique response header name and ``JSON-expression`` is a
                                valid JSON expression without the ``$`` prefix.

                                - *(string) --*

                                  - *(string) --*

                              - **responseTemplates** *(dict) --*

                                Specifies the templates used to transform the integration response
                                body. Response templates are represented as a key/value map, with a
                                content-type as the key and a template as the value.

                                - *(string) --*

                                  - *(string) --*

                              - **contentHandling** *(string) --*

                                Specifies how to handle response payload content type conversions.
                                Supported values are ``CONVERT_TO_BINARY`` and ``CONVERT_TO_TEXT`` ,
                                with the following behaviors:

                                * ``CONVERT_TO_BINARY`` : Converts a response payload from a
                                Base64-encoded string to the corresponding binary blob.

                                * ``CONVERT_TO_TEXT`` : Converts a response payload from a binary
                                blob to a Base64-encoded string.

                                If this property is not defined, the response payload will be passed
                                through from the integration response to the method response without
                                modification.

                      - **authorizationScopes** *(list) --*

                        A list of authorization scopes configured on the method. The scopes are used
                        with a ``COGNITO_USER_POOLS`` authorizer to authorize the method invocation.
                        The authorization works by matching the method scopes against the scopes
                        parsed from the access token in the incoming request. The method invocation
                        is authorized if any method scopes matches a claimed scope in the access
                        token. Otherwise, the invocation is not authorized. When the method scope is
                        configured, the client must provide an access token instead of an identity
                        token for authorization purposes.

                        - *(string) --*

            - **NextToken** *(string) --*

              A token to resume pagination.
        """


class GetRestApisPaginator(Boto3Paginator):
    """
    Paginator for `get_rest_apis`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: GetRestApisPaginatePaginationConfigTypeDef = None
    ) -> GetRestApisPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`APIGateway.Client.get_rest_apis`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/GetRestApis>`_

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
                'items': [
                    {
                        'id': 'string',
                        'name': 'string',
                        'description': 'string',
                        'createdDate': datetime(2015, 1, 1),
                        'version': 'string',
                        'warnings': [
                            'string',
                        ],
                        'binaryMediaTypes': [
                            'string',
                        ],
                        'minimumCompressionSize': 123,
                        'apiKeySource': 'HEADER'|'AUTHORIZER',
                        'endpointConfiguration': {
                            'types': [
                                'REGIONAL'|'EDGE'|'PRIVATE',
                            ],
                            'vpcEndpointIds': [
                                'string',
                            ]
                        },
                        'policy': 'string',
                        'tags': {
                            'string': 'string'
                        }
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Contains references to your APIs and links that guide you in how to interact with your
            collection. A collection offers a paginated view of your APIs.

              `Create an API
              <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__

            - **items** *(list) --*

              The current page of elements from this collection.

              - *(dict) --*

                Represents a REST API.

                  `Create an API
                  <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-create-api.html>`__

                - **id** *(string) --*

                  The API's identifier. This identifier is unique across all of your APIs in API
                  Gateway.

                - **name** *(string) --*

                  The API's name.

                - **description** *(string) --*

                  The API's description.

                - **createdDate** *(datetime) --*

                  The timestamp when the API was created.

                - **version** *(string) --*

                  A version identifier for the API.

                - **warnings** *(list) --*

                  The warning messages reported when ``failonwarnings`` is turned on during API
                  import.

                  - *(string) --*

                - **binaryMediaTypes** *(list) --*

                  The list of binary media types supported by the  RestApi . By default, the
                  RestApi supports only UTF-8-encoded text payloads.

                  - *(string) --*

                - **minimumCompressionSize** *(integer) --*

                  A nullable integer that is used to enable compression (with non-negative between 0
                  and 10485760 (10M) bytes, inclusive) or disable compression (with a null value) on
                  an API. When compression is enabled, compression or decompression is not applied
                  on the payload if the payload size is smaller than this value. Setting it to zero
                  allows compression for any payload size.

                - **apiKeySource** *(string) --*

                  The source of the API key for metering requests according to a usage plan. Valid
                  values are:

                  * ``HEADER`` to read the API key from the ``X-API-Key`` header of a request.

                  * ``AUTHORIZER`` to read the API key from the ``UsageIdentifierKey`` from a custom
                  authorizer.

                - **endpointConfiguration** *(dict) --*

                  The endpoint configuration of this  RestApi showing the endpoint types of the API.

                  - **types** *(list) --*

                    A list of endpoint types of an API ( RestApi ) or its custom domain name (
                    DomainName ). For an edge-optimized API and its custom domain name, the endpoint
                    type is ``"EDGE"`` . For a regional API and its custom domain name, the endpoint
                    type is ``REGIONAL`` . For a private API, the endpoint type is ``PRIVATE`` .

                    - *(string) --*

                      The endpoint type. The valid values are ``EDGE`` for edge-optimized API setup,
                      most suitable for mobile applications; ``REGIONAL`` for regional API endpoint
                      setup, most suitable for calling from AWS Region; and ``PRIVATE`` for private
                      APIs.

                  - **vpcEndpointIds** *(list) --*

                    A list of VpcEndpointIds of an API ( RestApi ) against which to create Route53
                    ALIASes. It is only supported for ``PRIVATE`` endpoint type.

                    - *(string) --*

                - **policy** *(string) --* A stringified JSON policy document that applies to this
                RestApi regardless of the caller and  Method configuration.

                - **tags** *(dict) --*

                  The collection of tags. Each tag element is associated with a given resource.

                  - *(string) --*

                    - *(string) --*

            - **NextToken** *(string) --*

              A token to resume pagination.
        """


class GetSdkTypesPaginator(Boto3Paginator):
    """
    Paginator for `get_sdk_types`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: GetSdkTypesPaginatePaginationConfigTypeDef = None
    ) -> GetSdkTypesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`APIGateway.Client.get_sdk_types`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/GetSdkTypes>`_

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
                'items': [
                    {
                        'id': 'string',
                        'friendlyName': 'string',
                        'description': 'string',
                        'configurationProperties': [
                            {
                                'name': 'string',
                                'friendlyName': 'string',
                                'description': 'string',
                                'required': True|False,
                                'defaultValue': 'string'
                            },
                        ]
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            The collection of  SdkType instances.

            - **items** *(list) --*

              The current page of elements from this collection.

              - *(dict) --*

                A type of SDK that API Gateway can generate.

                - **id** *(string) --*

                  The identifier of an  SdkType instance.

                - **friendlyName** *(string) --*

                  The user-friendly name of an  SdkType instance.

                - **description** *(string) --*

                  The description of an  SdkType .

                - **configurationProperties** *(list) --*

                  A list of configuration properties of an  SdkType .

                  - *(dict) --*

                    A configuration property of an SDK type.

                    - **name** *(string) --*

                      The name of a an  SdkType configuration property.

                    - **friendlyName** *(string) --*

                      The user-friendly name of an  SdkType configuration property.

                    - **description** *(string) --*

                      The description of an  SdkType configuration property.

                    - **required** *(boolean) --*

                      A boolean flag of an  SdkType configuration property to indicate if the
                      associated SDK configuration property is required (``true`` ) or not
                      (``false`` ).

                    - **defaultValue** *(string) --*

                      The default value of an  SdkType configuration property.

            - **NextToken** *(string) --*

              A token to resume pagination.
        """


class GetUsagePaginator(Boto3Paginator):
    """
    Paginator for `get_usage`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        usagePlanId: str,
        startDate: str,
        endDate: str,
        keyId: str = None,
        PaginationConfig: GetUsagePaginatePaginationConfigTypeDef = None,
    ) -> GetUsagePaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`APIGateway.Client.get_usage`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/GetUsage>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              usagePlanId='string',
              keyId='string',
              startDate='string',
              endDate='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type usagePlanId: string
        :param usagePlanId: **[REQUIRED]**

          [Required] The Id of the usage plan associated with the usage data.

        :type keyId: string
        :param keyId:

          The Id of the API key associated with the resultant usage data.

        :type startDate: string
        :param startDate: **[REQUIRED]**

          [Required] The starting date (e.g., 2016-01-01) of the usage data.

        :type endDate: string
        :param endDate: **[REQUIRED]**

          [Required] The ending date (e.g., 2016-12-31) of the usage data.

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
                'usagePlanId': 'string',
                'startDate': 'string',
                'endDate': 'string',
                'items': {
                    'string': [
                        [
                            123,
                        ],
                    ]
                },
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Represents the usage data of a usage plan.

               `Create and Use Usage Plans
               <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-usage-plans.html>`__
               , `Manage Usage in a Usage Plan
               <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-create-usage-plans-with-console.html#api-gateway-usage-plan-manage-usage>`__

            - **usagePlanId** *(string) --*

              The plan Id associated with this usage data.

            - **startDate** *(string) --*

              The starting date of the usage data.

            - **endDate** *(string) --*

              The ending date of the usage data.

            - **items** *(dict) --*

              The usage data, as daily logs of used and remaining quotas, over the specified time
              interval indexed over the API keys in a usage plan. For example, ``{..., "values" : {
              "{api_key}" : [ [0, 100], [10, 90], [100, 10]]}`` , where ``{api_key}`` stands for an
              API key value and the daily log entry is of the format ``[used quota, remaining
              quota]`` .

              - *(string) --*

                - *(list) --*

                  - *(list) --*

                    - *(integer) --*

            - **NextToken** *(string) --*

              A token to resume pagination.
        """


class GetUsagePlanKeysPaginator(Boto3Paginator):
    """
    Paginator for `get_usage_plan_keys`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        usagePlanId: str,
        nameQuery: str = None,
        PaginationConfig: GetUsagePlanKeysPaginatePaginationConfigTypeDef = None,
    ) -> GetUsagePlanKeysPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`APIGateway.Client.get_usage_plan_keys`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/GetUsagePlanKeys>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              usagePlanId='string',
              nameQuery='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type usagePlanId: string
        :param usagePlanId: **[REQUIRED]**

          [Required] The Id of the  UsagePlan resource representing the usage plan containing the
          to-be-retrieved  UsagePlanKey resource representing a plan customer.

        :type nameQuery: string
        :param nameQuery:

          A query parameter specifying the name of the to-be-returned usage plan keys.

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
                'items': [
                    {
                        'id': 'string',
                        'type': 'string',
                        'value': 'string',
                        'name': 'string'
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Represents the collection of usage plan keys added to usage plans for the associated API
            keys and, possibly, other types of keys.

              `Create and Use Usage Plans
              <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-usage-plans.html>`__

            - **items** *(list) --*

              The current page of elements from this collection.

              - *(dict) --*

                Represents a usage plan key to identify a plan customer.

                To associate an API stage with a selected API key in a usage plan, you must create a
                UsagePlanKey resource to represent the selected  ApiKey .

                 "  `Create and Use Usage Plans
                 <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-usage-plans.html>`__

                - **id** *(string) --*

                  The Id of a usage plan key.

                - **type** *(string) --*

                  The type of a usage plan key. Currently, the valid key type is ``API_KEY`` .

                - **value** *(string) --*

                  The value of a usage plan key.

                - **name** *(string) --*

                  The name of a usage plan key.

            - **NextToken** *(string) --*

              A token to resume pagination.
        """


class GetUsagePlansPaginator(Boto3Paginator):
    """
    Paginator for `get_usage_plans`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        keyId: str = None,
        PaginationConfig: GetUsagePlansPaginatePaginationConfigTypeDef = None,
    ) -> GetUsagePlansPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`APIGateway.Client.get_usage_plans`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/GetUsagePlans>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              keyId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type keyId: string
        :param keyId:

          The identifier of the API key associated with the usage plans.

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
                'items': [
                    {
                        'id': 'string',
                        'name': 'string',
                        'description': 'string',
                        'apiStages': [
                            {
                                'apiId': 'string',
                                'stage': 'string',
                                'throttle': {
                                    'string': {
                                        'burstLimit': 123,
                                        'rateLimit': 123.0
                                    }
                                }
                            },
                        ],
                        'throttle': {
                            'burstLimit': 123,
                            'rateLimit': 123.0
                        },
                        'quota': {
                            'limit': 123,
                            'offset': 123,
                            'period': 'DAY'|'WEEK'|'MONTH'
                        },
                        'productCode': 'string',
                        'tags': {
                            'string': 'string'
                        }
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            Represents a collection of usage plans for an AWS account.

              `Create and Use Usage Plans
              <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-usage-plans.html>`__

            - **items** *(list) --*

              The current page of elements from this collection.

              - *(dict) --*

                Represents a usage plan than can specify who can assess associated API stages with
                specified request limits and quotas.

                In a usage plan, you associate an API by specifying the API's Id and a stage name of
                the specified API. You add plan customers by adding API keys to the plan.

                   `Create and Use Usage Plans
                   <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-usage-plans.html>`__

                - **id** *(string) --*

                  The identifier of a  UsagePlan resource.

                - **name** *(string) --*

                  The name of a usage plan.

                - **description** *(string) --*

                  The description of a usage plan.

                - **apiStages** *(list) --*

                  The associated API stages of a usage plan.

                  - *(dict) --*

                    API stage name of the associated API stage in a usage plan.

                    - **apiId** *(string) --*

                      API Id of the associated API stage in a usage plan.

                    - **stage** *(string) --*

                      API stage name of the associated API stage in a usage plan.

                    - **throttle** *(dict) --*

                      Map containing method level throttling information for API stage in a usage
                      plan.

                      - *(string) --*

                        - *(dict) --*

                          The API request rate limits.

                          - **burstLimit** *(integer) --*

                            The API request burst limit, the maximum rate limit over a time ranging
                            from one to a few seconds, depending upon whether the underlying token
                            bucket is at its full capacity.

                          - **rateLimit** *(float) --*

                            The API request steady-state rate limit.

                - **throttle** *(dict) --*

                  The request throttle limits of a usage plan.

                  - **burstLimit** *(integer) --*

                    The API request burst limit, the maximum rate limit over a time ranging from one
                    to a few seconds, depending upon whether the underlying token bucket is at its
                    full capacity.

                  - **rateLimit** *(float) --*

                    The API request steady-state rate limit.

                - **quota** *(dict) --*

                  The maximum number of permitted requests per a given unit time interval.

                  - **limit** *(integer) --*

                    The maximum number of requests that can be made in a given time period.

                  - **offset** *(integer) --*

                    The number of requests subtracted from the given limit in the initial time
                    period.

                  - **period** *(string) --*

                    The time period in which the limit applies. Valid values are "DAY", "WEEK" or
                    "MONTH".

                - **productCode** *(string) --*

                  The AWS Markeplace product identifier to associate with the usage plan as a SaaS
                  product on AWS Marketplace.

                - **tags** *(dict) --*

                  The collection of tags. Each tag element is associated with a given resource.

                  - *(string) --*

                    - *(string) --*

            - **NextToken** *(string) --*

              A token to resume pagination.
        """


class GetVpcLinksPaginator(Boto3Paginator):
    """
    Paginator for `get_vpc_links`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: GetVpcLinksPaginatePaginationConfigTypeDef = None
    ) -> GetVpcLinksPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`APIGateway.Client.get_vpc_links`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/apigateway-2015-07-09/GetVpcLinks>`_

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
                'items': [
                    {
                        'id': 'string',
                        'name': 'string',
                        'description': 'string',
                        'targetArns': [
                            'string',
                        ],
                        'status': 'AVAILABLE'|'PENDING'|'DELETING'|'FAILED',
                        'statusMessage': 'string',
                        'tags': {
                            'string': 'string'
                        }
                    },
                ],
                'NextToken': 'string'
            }
          **Response Structure**

          - *(dict) --*

            The collection of VPC links under the caller's account in a region.

              `Getting Started with Private Integrations
              <https://docs.aws.amazon.com/apigateway/latest/developerguide/getting-started-with-private-integration.html>`__
              , `Set up Private Integrations
              <https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-private-integration.html>`__

            - **items** *(list) --*

              The current page of elements from this collection.

              - *(dict) --*

                A API Gateway VPC link for a  RestApi to access resources in an Amazon Virtual
                Private Cloud (VPC).

                To enable access to a resource in an Amazon Virtual Private Cloud through Amazon API
                Gateway, you, as an API developer, create a  VpcLink resource targeted for one or
                more network load balancers of the VPC and then integrate an API method with a
                private integration that uses the  VpcLink . The private integration has an
                integration type of ``HTTP`` or ``HTTP_PROXY`` and has a connection type of
                ``VPC_LINK`` . The integration uses the ``connectionId`` property to identify the
                VpcLink used.

                - **id** *(string) --*

                  The identifier of the  VpcLink . It is used in an  Integration to reference this
                  VpcLink .

                - **name** *(string) --*

                  The name used to label and identify the VPC link.

                - **description** *(string) --*

                  The description of the VPC link.

                - **targetArns** *(list) --*

                  The ARNs of network load balancers of the VPC targeted by the VPC link. The
                  network load balancers must be owned by the same AWS account of the API owner.

                  - *(string) --*

                - **status** *(string) --*

                  The status of the VPC link. The valid values are ``AVAILABLE`` , ``PENDING`` ,
                  ``DELETING`` , or ``FAILED`` . Deploying an API will wait if the status is
                  ``PENDING`` and will fail if the status is ``DELETING`` .

                - **statusMessage** *(string) --*

                  A description about the VPC link status.

                - **tags** *(dict) --*

                  The collection of tags. Each tag element is associated with a given resource.

                  - *(string) --*

                    - *(string) --*

            - **NextToken** *(string) --*

              A token to resume pagination.
        """
