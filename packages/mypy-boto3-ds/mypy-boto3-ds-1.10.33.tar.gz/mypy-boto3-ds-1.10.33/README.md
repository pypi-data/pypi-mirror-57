# mypy-boto3-ds

Mypy-friendly auto-generated type annotations for `boto3 ds 1.10.33` service.
More information can be found [here](https://github.com/vemel/mypy_boto3).

- [mypy-boto3-ds](#mypy-boto3-ds)
  - [How to use](#how-to-use)
    - [Type checking](#type-checking)
    - [Code auto-complete](#code-auto-complete)
  - [How it works](#how-it-works)

## How to use

### Type checking

Make sure you have [mypy](https://github.com/python/mypy) installed and activated in your IDE.

Install `boto3-stubs` for `ds` service.

```bash
pip install boto3-stubs[mypy-boto3-ds]
```

Use `boto3` with `mypy_boto3` in your project and enjoy type checking.

```python
import boto3

from mypy_boto3 import ds
# alternative import if you do not want to install mypy_boto3 package
# import mypy_boto3_ds as ds

# Use this client as usual, now mypy can check if your code is valid.
client: ds.Client = boto3.client("ds")

# works for session as well
session = boto3.session.Session(region="us-west-1")
session_client: ds.Client = session.client("ds")


# Paginators need type annotation on creation
describe_directories_paginator: ds.DescribeDirectoriesPaginator = client.get_paginator("describe_directories")
describe_domain_controllers_paginator: ds.DescribeDomainControllersPaginator = client.get_paginator("describe_domain_controllers")
describe_shared_directories_paginator: ds.DescribeSharedDirectoriesPaginator = client.get_paginator("describe_shared_directories")
describe_snapshots_paginator: ds.DescribeSnapshotsPaginator = client.get_paginator("describe_snapshots")
describe_trusts_paginator: ds.DescribeTrustsPaginator = client.get_paginator("describe_trusts")
list_ip_routes_paginator: ds.ListIpRoutesPaginator = client.get_paginator("list_ip_routes")
list_log_subscriptions_paginator: ds.ListLogSubscriptionsPaginator = client.get_paginator("list_log_subscriptions")
list_schema_extensions_paginator: ds.ListSchemaExtensionsPaginator = client.get_paginator("list_schema_extensions")
list_tags_for_resource_paginator: ds.ListTagsForResourcePaginator = client.get_paginator("list_tags_for_resource")
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