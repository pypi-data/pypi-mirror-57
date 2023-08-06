# mypy-boto3-sms

Mypy-friendly auto-generated type annotations for `boto3 sms 1.10.33` service.
More information can be found [here](https://github.com/vemel/mypy_boto3).

- [mypy-boto3-sms](#mypy-boto3-sms)
  - [How to use](#how-to-use)
    - [Type checking](#type-checking)
    - [Code auto-complete](#code-auto-complete)
  - [How it works](#how-it-works)

## How to use

### Type checking

Make sure you have [mypy](https://github.com/python/mypy) installed and activated in your IDE.

Install `boto3-stubs` for `sms` service.

```bash
pip install boto3-stubs[mypy-boto3-sms]
```

Use `boto3` with `mypy_boto3` in your project and enjoy type checking.

```python
import boto3

from mypy_boto3 import sms
# alternative import if you do not want to install mypy_boto3 package
# import mypy_boto3_sms as sms

# Use this client as usual, now mypy can check if your code is valid.
client: sms.Client = boto3.client("sms")

# works for session as well
session = boto3.session.Session(region="us-west-1")
session_client: sms.Client = session.client("sms")


# Paginators need type annotation on creation
get_connectors_paginator: sms.GetConnectorsPaginator = client.get_paginator("get_connectors")
get_replication_jobs_paginator: sms.GetReplicationJobsPaginator = client.get_paginator("get_replication_jobs")
get_replication_runs_paginator: sms.GetReplicationRunsPaginator = client.get_paginator("get_replication_runs")
get_servers_paginator: sms.GetServersPaginator = client.get_paginator("get_servers")
list_apps_paginator: sms.ListAppsPaginator = client.get_paginator("list_apps")
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