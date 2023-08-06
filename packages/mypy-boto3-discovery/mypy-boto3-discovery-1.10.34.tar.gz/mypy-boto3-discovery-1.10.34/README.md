# mypy-boto3-discovery

Mypy-friendly auto-generated type annotations for `boto3 discovery 1.10.34` service.
More information can be found [here](https://github.com/vemel/mypy_boto3).

- [mypy-boto3-discovery](#mypy-boto3-discovery)
  - [How to use](#how-to-use)
    - [Type checking](#type-checking)
    - [Code auto-complete](#code-auto-complete)
  - [How it works](#how-it-works)

## How to use

### Type checking

Make sure you have [mypy](https://github.com/python/mypy) installed and activated in your IDE.

Install `boto3-stubs` for `discovery` service.

```bash
pip install boto3-stubs[mypy-boto3-discovery]
```

Use `boto3` with `mypy_boto3` in your project and enjoy type checking.

```python
import boto3

from mypy_boto3 import discovery
# alternative import if you do not want to install mypy_boto3 package
# import mypy_boto3_discovery as discovery

# Use this client as usual, now mypy can check if your code is valid.
client: discovery.Client = boto3.client("discovery")

# works for session as well
session = boto3.session.Session(region="us-west-1")
session_client: discovery.Client = session.client("discovery")


# Paginators need type annotation on creation
describe_agents_paginator: discovery.DescribeAgentsPaginator = client.get_paginator("describe_agents")
describe_continuous_exports_paginator: discovery.DescribeContinuousExportsPaginator = client.get_paginator("describe_continuous_exports")
describe_export_configurations_paginator: discovery.DescribeExportConfigurationsPaginator = client.get_paginator("describe_export_configurations")
describe_export_tasks_paginator: discovery.DescribeExportTasksPaginator = client.get_paginator("describe_export_tasks")
describe_tags_paginator: discovery.DescribeTagsPaginator = client.get_paginator("describe_tags")
list_configurations_paginator: discovery.ListConfigurationsPaginator = client.get_paginator("list_configurations")
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