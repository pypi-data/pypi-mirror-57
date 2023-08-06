# mypy-boto3-dynamodb

Mypy-friendly auto-generated type annotations for `boto3 dynamodb 1.10.33` service.
More information can be found [here](https://github.com/vemel/mypy_boto3).

- [mypy-boto3-dynamodb](#mypy-boto3-dynamodb)
  - [How to use](#how-to-use)
    - [Type checking](#type-checking)
    - [Code auto-complete](#code-auto-complete)
  - [How it works](#how-it-works)

## How to use

### Type checking

Make sure you have [mypy](https://github.com/python/mypy) installed and activated in your IDE.

Install `boto3-stubs` for `dynamodb` service.

```bash
pip install boto3-stubs[mypy-boto3-dynamodb]
```

Use `boto3` with `mypy_boto3` in your project and enjoy type checking.

```python
import boto3

from mypy_boto3 import dynamodb
# alternative import if you do not want to install mypy_boto3 package
# import mypy_boto3_dynamodb as dynamodb

# Use this client as usual, now mypy can check if your code is valid.
client: dynamodb.Client = boto3.client("dynamodb")

# works for session as well
session = boto3.session.Session(region="us-west-1")
session_client: dynamodb.Client = session.client("dynamodb")

# Do you prefer resource approach? We've got you covered!
resource: dynamodb.ServiceResource = boto3.resource("dynamodb")

# Waiters need type annotation on creation
table_exists_waiter: dynamodb.TableExistsWaiter = client.get_waiter("table_exists")
table_not_exists_waiter: dynamodb.TableNotExistsWaiter = client.get_waiter("table_not_exists")

# Paginators need type annotation on creation
list_backups_paginator: dynamodb.ListBackupsPaginator = client.get_paginator("list_backups")
list_tables_paginator: dynamodb.ListTablesPaginator = client.get_paginator("list_tables")
list_tags_of_resource_paginator: dynamodb.ListTagsOfResourcePaginator = client.get_paginator("list_tags_of_resource")
query_paginator: dynamodb.QueryPaginator = client.get_paginator("query")
scan_paginator: dynamodb.ScanPaginator = client.get_paginator("scan")
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