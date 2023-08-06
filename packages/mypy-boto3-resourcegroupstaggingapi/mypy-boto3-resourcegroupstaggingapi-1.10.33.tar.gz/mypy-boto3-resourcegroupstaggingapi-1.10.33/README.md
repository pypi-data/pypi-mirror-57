# mypy-boto3-resourcegroupstaggingapi

Mypy-friendly auto-generated type annotations for `boto3 resourcegroupstaggingapi 1.10.33` service.
More information can be found [here](https://github.com/vemel/mypy_boto3).

- [mypy-boto3-resourcegroupstaggingapi](#mypy-boto3-resourcegroupstaggingapi)
  - [How to use](#how-to-use)
    - [Type checking](#type-checking)
    - [Code auto-complete](#code-auto-complete)
  - [How it works](#how-it-works)

## How to use

### Type checking

Make sure you have [mypy](https://github.com/python/mypy) installed and activated in your IDE.

Install `boto3-stubs` for `resourcegroupstaggingapi` service.

```bash
pip install boto3-stubs[mypy-boto3-resourcegroupstaggingapi]
```

Use `boto3` with `mypy_boto3` in your project and enjoy type checking.

```python
import boto3

from mypy_boto3 import resourcegroupstaggingapi
# alternative import if you do not want to install mypy_boto3 package
# import mypy_boto3_resourcegroupstaggingapi as resourcegroupstaggingapi

# Use this client as usual, now mypy can check if your code is valid.
client: resourcegroupstaggingapi.Client = boto3.client("resourcegroupstaggingapi")

# works for session as well
session = boto3.session.Session(region="us-west-1")
session_client: resourcegroupstaggingapi.Client = session.client("resourcegroupstaggingapi")


# Paginators need type annotation on creation
get_compliance_summary_paginator: resourcegroupstaggingapi.GetComplianceSummaryPaginator = client.get_paginator("get_compliance_summary")
get_resources_paginator: resourcegroupstaggingapi.GetResourcesPaginator = client.get_paginator("get_resources")
get_tag_keys_paginator: resourcegroupstaggingapi.GetTagKeysPaginator = client.get_paginator("get_tag_keys")
get_tag_values_paginator: resourcegroupstaggingapi.GetTagValuesPaginator = client.get_paginator("get_tag_values")
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