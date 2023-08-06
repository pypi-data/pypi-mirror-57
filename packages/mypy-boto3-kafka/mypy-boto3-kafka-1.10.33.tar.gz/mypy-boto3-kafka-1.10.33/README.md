# mypy-boto3-kafka

Mypy-friendly auto-generated type annotations for `boto3 kafka 1.10.33` service.
More information can be found [here](https://github.com/vemel/mypy_boto3).

- [mypy-boto3-kafka](#mypy-boto3-kafka)
  - [How to use](#how-to-use)
    - [Type checking](#type-checking)
    - [Code auto-complete](#code-auto-complete)
  - [How it works](#how-it-works)

## How to use

### Type checking

Make sure you have [mypy](https://github.com/python/mypy) installed and activated in your IDE.

Install `boto3-stubs` for `kafka` service.

```bash
pip install boto3-stubs[mypy-boto3-kafka]
```

Use `boto3` with `mypy_boto3` in your project and enjoy type checking.

```python
import boto3

from mypy_boto3 import kafka
# alternative import if you do not want to install mypy_boto3 package
# import mypy_boto3_kafka as kafka

# Use this client as usual, now mypy can check if your code is valid.
client: kafka.Client = boto3.client("kafka")

# works for session as well
session = boto3.session.Session(region="us-west-1")
session_client: kafka.Client = session.client("kafka")


# Paginators need type annotation on creation
list_cluster_operations_paginator: kafka.ListClusterOperationsPaginator = client.get_paginator("list_cluster_operations")
list_clusters_paginator: kafka.ListClustersPaginator = client.get_paginator("list_clusters")
list_configuration_revisions_paginator: kafka.ListConfigurationRevisionsPaginator = client.get_paginator("list_configuration_revisions")
list_configurations_paginator: kafka.ListConfigurationsPaginator = client.get_paginator("list_configurations")
list_nodes_paginator: kafka.ListNodesPaginator = client.get_paginator("list_nodes")
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