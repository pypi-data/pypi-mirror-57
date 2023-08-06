# mypy-boto3-apigateway

Mypy-friendly auto-generated type annotations for `boto3 apigateway 1.10.34` service.
More information can be found [here](https://github.com/vemel/mypy_boto3).

- [mypy-boto3-apigateway](#mypy-boto3-apigateway)
  - [How to use](#how-to-use)
    - [Type checking](#type-checking)
    - [Code auto-complete](#code-auto-complete)
  - [How it works](#how-it-works)

## How to use

### Type checking

Make sure you have [mypy](https://github.com/python/mypy) installed and activated in your IDE.

Install `boto3-stubs` for `apigateway` service.

```bash
pip install boto3-stubs[mypy-boto3-apigateway]
```

Use `boto3` with `mypy_boto3` in your project and enjoy type checking.

```python
import boto3

from mypy_boto3 import apigateway
# alternative import if you do not want to install mypy_boto3 package
# import mypy_boto3_apigateway as apigateway

# Use this client as usual, now mypy can check if your code is valid.
client: apigateway.Client = boto3.client("apigateway")

# works for session as well
session = boto3.session.Session(region="us-west-1")
session_client: apigateway.Client = session.client("apigateway")


# Paginators need type annotation on creation
get_api_keys_paginator: apigateway.GetApiKeysPaginator = client.get_paginator("get_api_keys")
get_authorizers_paginator: apigateway.GetAuthorizersPaginator = client.get_paginator("get_authorizers")
get_base_path_mappings_paginator: apigateway.GetBasePathMappingsPaginator = client.get_paginator("get_base_path_mappings")
get_client_certificates_paginator: apigateway.GetClientCertificatesPaginator = client.get_paginator("get_client_certificates")
get_deployments_paginator: apigateway.GetDeploymentsPaginator = client.get_paginator("get_deployments")
get_documentation_parts_paginator: apigateway.GetDocumentationPartsPaginator = client.get_paginator("get_documentation_parts")
get_documentation_versions_paginator: apigateway.GetDocumentationVersionsPaginator = client.get_paginator("get_documentation_versions")
get_domain_names_paginator: apigateway.GetDomainNamesPaginator = client.get_paginator("get_domain_names")
get_gateway_responses_paginator: apigateway.GetGatewayResponsesPaginator = client.get_paginator("get_gateway_responses")
get_models_paginator: apigateway.GetModelsPaginator = client.get_paginator("get_models")
get_request_validators_paginator: apigateway.GetRequestValidatorsPaginator = client.get_paginator("get_request_validators")
get_resources_paginator: apigateway.GetResourcesPaginator = client.get_paginator("get_resources")
get_rest_apis_paginator: apigateway.GetRestApisPaginator = client.get_paginator("get_rest_apis")
get_sdk_types_paginator: apigateway.GetSdkTypesPaginator = client.get_paginator("get_sdk_types")
get_usage_paginator: apigateway.GetUsagePaginator = client.get_paginator("get_usage")
get_usage_plan_keys_paginator: apigateway.GetUsagePlanKeysPaginator = client.get_paginator("get_usage_plan_keys")
get_usage_plans_paginator: apigateway.GetUsagePlansPaginator = client.get_paginator("get_usage_plans")
get_vpc_links_paginator: apigateway.GetVpcLinksPaginator = client.get_paginator("get_vpc_links")
```

## How it works

Fully automated [builder](https://github.com/vemel/mypy_boto3) carefully generates
type annotations for each service, patiently waiting for `boto3` updates. It delivers
a drop-in type annotations for you and makes sure that:

- Latest version of `boto3` is used.
- Each public class and method of every `boto3` service gets valid type annotations
  extracted from latest documentation (blame `botocore` docs if types are incorrect).
- Type annotations include up-to-date documentation.
- Code is processed by [black](https://github.com/psf/black) for readability.

## Submodules

- `master` - Install `mypy-boto3` package.