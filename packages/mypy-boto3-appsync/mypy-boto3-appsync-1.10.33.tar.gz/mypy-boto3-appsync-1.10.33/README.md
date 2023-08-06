# mypy-boto3-appsync

Mypy-friendly auto-generated type annotations for `boto3 appsync 1.10.33` service.
More information can be found [here](https://github.com/vemel/mypy_boto3).

- [mypy-boto3-appsync](#mypy-boto3-appsync)
  - [How to use](#how-to-use)
    - [Type checking](#type-checking)
    - [Code auto-complete](#code-auto-complete)
  - [How it works](#how-it-works)

## How to use

### Type checking

Make sure you have [mypy](https://github.com/python/mypy) installed and activated in your IDE.

Install `boto3-stubs` for `appsync` service.

```bash
pip install boto3-stubs[mypy-boto3-appsync]
```

Use `boto3` with `mypy_boto3` in your project and enjoy type checking.

```python
import boto3

from mypy_boto3 import appsync
# alternative import if you do not want to install mypy_boto3 package
# import mypy_boto3_appsync as appsync

# Use this client as usual, now mypy can check if your code is valid.
client: appsync.Client = boto3.client("appsync")

# works for session as well
session = boto3.session.Session(region="us-west-1")
session_client: appsync.Client = session.client("appsync")


# Paginators need type annotation on creation
list_api_keys_paginator: appsync.ListApiKeysPaginator = client.get_paginator("list_api_keys")
list_data_sources_paginator: appsync.ListDataSourcesPaginator = client.get_paginator("list_data_sources")
list_functions_paginator: appsync.ListFunctionsPaginator = client.get_paginator("list_functions")
list_graphql_apis_paginator: appsync.ListGraphqlApisPaginator = client.get_paginator("list_graphql_apis")
list_resolvers_paginator: appsync.ListResolversPaginator = client.get_paginator("list_resolvers")
list_resolvers_by_function_paginator: appsync.ListResolversByFunctionPaginator = client.get_paginator("list_resolvers_by_function")
list_types_paginator: appsync.ListTypesPaginator = client.get_paginator("list_types")
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