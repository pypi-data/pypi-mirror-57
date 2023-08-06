# mypy-boto3-mgh

Mypy-friendly auto-generated type annotations for `boto3 mgh 1.10.33` service.
More information can be found [here](https://github.com/vemel/mypy_boto3).

- [mypy-boto3-mgh](#mypy-boto3-mgh)
  - [How to use](#how-to-use)
    - [Type checking](#type-checking)
    - [Code auto-complete](#code-auto-complete)
  - [How it works](#how-it-works)

## How to use

### Type checking

Make sure you have [mypy](https://github.com/python/mypy) installed and activated in your IDE.

Install `boto3-stubs` for `mgh` service.

```bash
pip install boto3-stubs[mypy-boto3-mgh]
```

Use `boto3` with `mypy_boto3` in your project and enjoy type checking.

```python
import boto3

from mypy_boto3 import mgh
# alternative import if you do not want to install mypy_boto3 package
# import mypy_boto3_mgh as mgh

# Use this client as usual, now mypy can check if your code is valid.
client: mgh.Client = boto3.client("mgh")

# works for session as well
session = boto3.session.Session(region="us-west-1")
session_client: mgh.Client = session.client("mgh")


# Paginators need type annotation on creation
list_created_artifacts_paginator: mgh.ListCreatedArtifactsPaginator = client.get_paginator("list_created_artifacts")
list_discovered_resources_paginator: mgh.ListDiscoveredResourcesPaginator = client.get_paginator("list_discovered_resources")
list_migration_tasks_paginator: mgh.ListMigrationTasksPaginator = client.get_paginator("list_migration_tasks")
list_progress_update_streams_paginator: mgh.ListProgressUpdateStreamsPaginator = client.get_paginator("list_progress_update_streams")
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