# mypy-boto3-apigatewayv2

Mypy-friendly auto-generated type annotations for `boto3 apigatewayv2 1.10.34` service.
More information can be found [here](https://github.com/vemel/mypy_boto3).

- [mypy-boto3-apigatewayv2](#mypy-boto3-apigatewayv2)
  - [How to use](#how-to-use)
    - [Type checking](#type-checking)
    - [Code auto-complete](#code-auto-complete)
  - [How it works](#how-it-works)

## How to use

### Type checking

Make sure you have [mypy](https://github.com/python/mypy) installed and activated in your IDE.

Install `boto3-stubs` for `apigatewayv2` service.

```bash
pip install boto3-stubs[mypy-boto3-apigatewayv2]
```

Use `boto3` with `mypy_boto3` in your project and enjoy type checking.

```python
import boto3

from mypy_boto3 import apigatewayv2
# alternative import if you do not want to install mypy_boto3 package
# import mypy_boto3_apigatewayv2 as apigatewayv2

# Use this client as usual, now mypy can check if your code is valid.
client: apigatewayv2.Client = boto3.client("apigatewayv2")

# works for session as well
session = boto3.session.Session(region="us-west-1")
session_client: apigatewayv2.Client = session.client("apigatewayv2")


# Paginators need type annotation on creation
get_apis_paginator: apigatewayv2.GetApisPaginator = client.get_paginator("get_apis")
get_authorizers_paginator: apigatewayv2.GetAuthorizersPaginator = client.get_paginator("get_authorizers")
get_deployments_paginator: apigatewayv2.GetDeploymentsPaginator = client.get_paginator("get_deployments")
get_domain_names_paginator: apigatewayv2.GetDomainNamesPaginator = client.get_paginator("get_domain_names")
get_integration_responses_paginator: apigatewayv2.GetIntegrationResponsesPaginator = client.get_paginator("get_integration_responses")
get_integrations_paginator: apigatewayv2.GetIntegrationsPaginator = client.get_paginator("get_integrations")
get_models_paginator: apigatewayv2.GetModelsPaginator = client.get_paginator("get_models")
get_route_responses_paginator: apigatewayv2.GetRouteResponsesPaginator = client.get_paginator("get_route_responses")
get_routes_paginator: apigatewayv2.GetRoutesPaginator = client.get_paginator("get_routes")
get_stages_paginator: apigatewayv2.GetStagesPaginator = client.get_paginator("get_stages")
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