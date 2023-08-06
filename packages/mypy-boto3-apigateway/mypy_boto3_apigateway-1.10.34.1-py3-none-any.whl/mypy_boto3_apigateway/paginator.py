"Main interface for apigateway service Paginators"
from __future__ import annotations

import sys
from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_apigateway.type_defs import (
    ApiKeysTypeDef,
    AuthorizersTypeDef,
    BasePathMappingsTypeDef,
    ClientCertificatesTypeDef,
    DeploymentsTypeDef,
    DocumentationPartsTypeDef,
    DocumentationVersionsTypeDef,
    DomainNamesTypeDef,
    GatewayResponsesTypeDef,
    ModelsTypeDef,
    PaginatorConfigTypeDef,
    RequestValidatorsTypeDef,
    ResourcesTypeDef,
    RestApisTypeDef,
    SdkTypesTypeDef,
    UsagePlanKeysTypeDef,
    UsagePlansTypeDef,
    UsageTypeDef,
    VpcLinksTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


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
    [Paginator.GetApiKeys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/apigateway.html#APIGateway.Paginator.GetApiKeys)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        nameQuery: str = None,
        customerId: str = None,
        includeValues: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> ApiKeysTypeDef:
        """
        [GetApiKeys.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/apigateway.html#APIGateway.Paginator.GetApiKeys.paginate)
        """


class GetAuthorizersPaginator(Boto3Paginator):
    """
    [Paginator.GetAuthorizers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/apigateway.html#APIGateway.Paginator.GetAuthorizers)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, restApiId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> AuthorizersTypeDef:
        """
        [GetAuthorizers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/apigateway.html#APIGateway.Paginator.GetAuthorizers.paginate)
        """


class GetBasePathMappingsPaginator(Boto3Paginator):
    """
    [Paginator.GetBasePathMappings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/apigateway.html#APIGateway.Paginator.GetBasePathMappings)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, domainName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> BasePathMappingsTypeDef:
        """
        [GetBasePathMappings.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/apigateway.html#APIGateway.Paginator.GetBasePathMappings.paginate)
        """


class GetClientCertificatesPaginator(Boto3Paginator):
    """
    [Paginator.GetClientCertificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/apigateway.html#APIGateway.Paginator.GetClientCertificates)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ClientCertificatesTypeDef:
        """
        [GetClientCertificates.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/apigateway.html#APIGateway.Paginator.GetClientCertificates.paginate)
        """


class GetDeploymentsPaginator(Boto3Paginator):
    """
    [Paginator.GetDeployments documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/apigateway.html#APIGateway.Paginator.GetDeployments)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, restApiId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> DeploymentsTypeDef:
        """
        [GetDeployments.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/apigateway.html#APIGateway.Paginator.GetDeployments.paginate)
        """


class GetDocumentationPartsPaginator(Boto3Paginator):
    """
    [Paginator.GetDocumentationParts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/apigateway.html#APIGateway.Paginator.GetDocumentationParts)
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
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> DocumentationPartsTypeDef:
        """
        [GetDocumentationParts.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/apigateway.html#APIGateway.Paginator.GetDocumentationParts.paginate)
        """


class GetDocumentationVersionsPaginator(Boto3Paginator):
    """
    [Paginator.GetDocumentationVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/apigateway.html#APIGateway.Paginator.GetDocumentationVersions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, restApiId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> DocumentationVersionsTypeDef:
        """
        [GetDocumentationVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/apigateway.html#APIGateway.Paginator.GetDocumentationVersions.paginate)
        """


class GetDomainNamesPaginator(Boto3Paginator):
    """
    [Paginator.GetDomainNames documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/apigateway.html#APIGateway.Paginator.GetDomainNames)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(self, PaginationConfig: PaginatorConfigTypeDef = None) -> DomainNamesTypeDef:
        """
        [GetDomainNames.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/apigateway.html#APIGateway.Paginator.GetDomainNames.paginate)
        """


class GetGatewayResponsesPaginator(Boto3Paginator):
    """
    [Paginator.GetGatewayResponses documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/apigateway.html#APIGateway.Paginator.GetGatewayResponses)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, restApiId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> GatewayResponsesTypeDef:
        """
        [GetGatewayResponses.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/apigateway.html#APIGateway.Paginator.GetGatewayResponses.paginate)
        """


class GetModelsPaginator(Boto3Paginator):
    """
    [Paginator.GetModels documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/apigateway.html#APIGateway.Paginator.GetModels)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, restApiId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ModelsTypeDef:
        """
        [GetModels.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/apigateway.html#APIGateway.Paginator.GetModels.paginate)
        """


class GetRequestValidatorsPaginator(Boto3Paginator):
    """
    [Paginator.GetRequestValidators documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/apigateway.html#APIGateway.Paginator.GetRequestValidators)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, restApiId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> RequestValidatorsTypeDef:
        """
        [GetRequestValidators.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/apigateway.html#APIGateway.Paginator.GetRequestValidators.paginate)
        """


class GetResourcesPaginator(Boto3Paginator):
    """
    [Paginator.GetResources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/apigateway.html#APIGateway.Paginator.GetResources)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        restApiId: str,
        embed: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> ResourcesTypeDef:
        """
        [GetResources.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/apigateway.html#APIGateway.Paginator.GetResources.paginate)
        """


class GetRestApisPaginator(Boto3Paginator):
    """
    [Paginator.GetRestApis documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/apigateway.html#APIGateway.Paginator.GetRestApis)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(self, PaginationConfig: PaginatorConfigTypeDef = None) -> RestApisTypeDef:
        """
        [GetRestApis.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/apigateway.html#APIGateway.Paginator.GetRestApis.paginate)
        """


class GetSdkTypesPaginator(Boto3Paginator):
    """
    [Paginator.GetSdkTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/apigateway.html#APIGateway.Paginator.GetSdkTypes)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(self, PaginationConfig: PaginatorConfigTypeDef = None) -> SdkTypesTypeDef:
        """
        [GetSdkTypes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/apigateway.html#APIGateway.Paginator.GetSdkTypes.paginate)
        """


class GetUsagePaginator(Boto3Paginator):
    """
    [Paginator.GetUsage documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/apigateway.html#APIGateway.Paginator.GetUsage)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        usagePlanId: str,
        startDate: str,
        endDate: str,
        keyId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> UsageTypeDef:
        """
        [GetUsage.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/apigateway.html#APIGateway.Paginator.GetUsage.paginate)
        """


class GetUsagePlanKeysPaginator(Boto3Paginator):
    """
    [Paginator.GetUsagePlanKeys documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/apigateway.html#APIGateway.Paginator.GetUsagePlanKeys)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        usagePlanId: str,
        nameQuery: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> UsagePlanKeysTypeDef:
        """
        [GetUsagePlanKeys.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/apigateway.html#APIGateway.Paginator.GetUsagePlanKeys.paginate)
        """


class GetUsagePlansPaginator(Boto3Paginator):
    """
    [Paginator.GetUsagePlans documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/apigateway.html#APIGateway.Paginator.GetUsagePlans)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, keyId: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> UsagePlansTypeDef:
        """
        [GetUsagePlans.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/apigateway.html#APIGateway.Paginator.GetUsagePlans.paginate)
        """


class GetVpcLinksPaginator(Boto3Paginator):
    """
    [Paginator.GetVpcLinks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/apigateway.html#APIGateway.Paginator.GetVpcLinks)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(self, PaginationConfig: PaginatorConfigTypeDef = None) -> VpcLinksTypeDef:
        """
        [GetVpcLinks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/apigateway.html#APIGateway.Paginator.GetVpcLinks.paginate)
        """
