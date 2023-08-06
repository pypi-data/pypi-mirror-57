# mypy-boto3-es

Mypy-friendly auto-generated type annotations for `boto3 es 1.10.38` service.
More information can be found [here](https://github.com/vemel/mypy_boto3).

- [mypy-boto3-es](#mypy-boto3-es)
  - [How to use](#how-to-use)
    - [Type checking](#type-checking)
    - [Code auto-complete](#code-auto-complete)
  - [How it works](#how-it-works)

## How to use

### Type checking

Make sure you have [mypy](https://github.com/python/mypy) installed and activated in your IDE.

Install `boto3-stubs` for `es` service.

```bash
python -m pip install boto3-stubs[mypy-boto3-es]

# build service index. You should execute this command everytime
# you install or remove service packages
python -m mypy_boto3
```

Use `boto3` with `mypy_boto3` in your project and enjoy type checking.

```python
import boto3

from mypy_boto3 import es
# alternative import if you do not want to install mypy_boto3 package
# import mypy_boto3_es as es

# Use this client as usual, now mypy can check if your code is valid.
# Check if your IDE supports function overloads,
# you probably do not need explicit type annotations
# client = boto3.client("es")
client: es.ElasticsearchServiceClient = boto3.client("es")

# works for session as well
session = boto3.session.Session(region="us-west-1")
session_client: es.ElasticsearchServiceClient = session.client("es")


# Paginators need type annotation on creation
describe_reserved_elasticsearch_instance_offerings_paginator: es.DescribeReservedElasticsearchInstanceOfferingsPaginator = client.get_paginator("describe_reserved_elasticsearch_instance_offerings")
describe_reserved_elasticsearch_instances_paginator: es.DescribeReservedElasticsearchInstancesPaginator = client.get_paginator("describe_reserved_elasticsearch_instances")
get_upgrade_history_paginator: es.GetUpgradeHistoryPaginator = client.get_paginator("get_upgrade_history")
list_elasticsearch_instance_types_paginator: es.ListElasticsearchInstanceTypesPaginator = client.get_paginator("list_elasticsearch_instance_types")
list_elasticsearch_versions_paginator: es.ListElasticsearchVersionsPaginator = client.get_paginator("list_elasticsearch_versions")
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