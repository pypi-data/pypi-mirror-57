# mypy-boto3-connect

Mypy-friendly auto-generated type annotations for `boto3 connect 1.10.34` service.
More information can be found [here](https://github.com/vemel/mypy_boto3).

- [mypy-boto3-connect](#mypy-boto3-connect)
  - [How to use](#how-to-use)
    - [Type checking](#type-checking)
    - [Code auto-complete](#code-auto-complete)
  - [How it works](#how-it-works)

## How to use

### Type checking

Make sure you have [mypy](https://github.com/python/mypy) installed and activated in your IDE.

Install `boto3-stubs` for `connect` service.

```bash
pip install boto3-stubs[mypy-boto3-connect]
```

Use `boto3` with `mypy_boto3` in your project and enjoy type checking.

```python
import boto3

from mypy_boto3 import connect
# alternative import if you do not want to install mypy_boto3 package
# import mypy_boto3_connect as connect

# Use this client as usual, now mypy can check if your code is valid.
client: connect.Client = boto3.client("connect")

# works for session as well
session = boto3.session.Session(region="us-west-1")
session_client: connect.Client = session.client("connect")


# Paginators need type annotation on creation
get_metric_data_paginator: connect.GetMetricDataPaginator = client.get_paginator("get_metric_data")
list_contact_flows_paginator: connect.ListContactFlowsPaginator = client.get_paginator("list_contact_flows")
list_hours_of_operations_paginator: connect.ListHoursOfOperationsPaginator = client.get_paginator("list_hours_of_operations")
list_phone_numbers_paginator: connect.ListPhoneNumbersPaginator = client.get_paginator("list_phone_numbers")
list_queues_paginator: connect.ListQueuesPaginator = client.get_paginator("list_queues")
list_routing_profiles_paginator: connect.ListRoutingProfilesPaginator = client.get_paginator("list_routing_profiles")
list_security_profiles_paginator: connect.ListSecurityProfilesPaginator = client.get_paginator("list_security_profiles")
list_user_hierarchy_groups_paginator: connect.ListUserHierarchyGroupsPaginator = client.get_paginator("list_user_hierarchy_groups")
list_users_paginator: connect.ListUsersPaginator = client.get_paginator("list_users")
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