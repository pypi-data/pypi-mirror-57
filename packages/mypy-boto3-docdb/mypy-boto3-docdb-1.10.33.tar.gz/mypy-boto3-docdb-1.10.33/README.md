# mypy-boto3-docdb

Mypy-friendly auto-generated type annotations for `boto3 docdb 1.10.33` service.
More information can be found [here](https://github.com/vemel/mypy_boto3).

- [mypy-boto3-docdb](#mypy-boto3-docdb)
  - [How to use](#how-to-use)
    - [Type checking](#type-checking)
    - [Code auto-complete](#code-auto-complete)
  - [How it works](#how-it-works)

## How to use

### Type checking

Make sure you have [mypy](https://github.com/python/mypy) installed and activated in your IDE.

Install `boto3-stubs` for `docdb` service.

```bash
pip install boto3-stubs[mypy-boto3-docdb]
```

Use `boto3` with `mypy_boto3` in your project and enjoy type checking.

```python
import boto3

from mypy_boto3 import docdb
# alternative import if you do not want to install mypy_boto3 package
# import mypy_boto3_docdb as docdb

# Use this client as usual, now mypy can check if your code is valid.
client: docdb.Client = boto3.client("docdb")

# works for session as well
session = boto3.session.Session(region="us-west-1")
session_client: docdb.Client = session.client("docdb")


# Waiters need type annotation on creation
db_instance_available_waiter: docdb.DBInstanceAvailableWaiter = client.get_waiter("db_instance_available")
db_instance_deleted_waiter: docdb.DBInstanceDeletedWaiter = client.get_waiter("db_instance_deleted")

# Paginators need type annotation on creation
describe_db_clusters_paginator: docdb.DescribeDBClustersPaginator = client.get_paginator("describe_db_clusters")
describe_db_engine_versions_paginator: docdb.DescribeDBEngineVersionsPaginator = client.get_paginator("describe_db_engine_versions")
describe_db_instances_paginator: docdb.DescribeDBInstancesPaginator = client.get_paginator("describe_db_instances")
describe_db_subnet_groups_paginator: docdb.DescribeDBSubnetGroupsPaginator = client.get_paginator("describe_db_subnet_groups")
describe_events_paginator: docdb.DescribeEventsPaginator = client.get_paginator("describe_events")
describe_orderable_db_instance_options_paginator: docdb.DescribeOrderableDBInstanceOptionsPaginator = client.get_paginator("describe_orderable_db_instance_options")
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