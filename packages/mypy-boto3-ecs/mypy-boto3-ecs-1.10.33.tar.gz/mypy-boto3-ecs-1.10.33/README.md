# mypy-boto3-ecs

Mypy-friendly auto-generated type annotations for `boto3 ecs 1.10.33` service.
More information can be found [here](https://github.com/vemel/mypy_boto3).

- [mypy-boto3-ecs](#mypy-boto3-ecs)
  - [How to use](#how-to-use)
    - [Type checking](#type-checking)
    - [Code auto-complete](#code-auto-complete)
  - [How it works](#how-it-works)

## How to use

### Type checking

Make sure you have [mypy](https://github.com/python/mypy) installed and activated in your IDE.

Install `boto3-stubs` for `ecs` service.

```bash
pip install boto3-stubs[mypy-boto3-ecs]
```

Use `boto3` with `mypy_boto3` in your project and enjoy type checking.

```python
import boto3

from mypy_boto3 import ecs
# alternative import if you do not want to install mypy_boto3 package
# import mypy_boto3_ecs as ecs

# Use this client as usual, now mypy can check if your code is valid.
client: ecs.Client = boto3.client("ecs")

# works for session as well
session = boto3.session.Session(region="us-west-1")
session_client: ecs.Client = session.client("ecs")


# Waiters need type annotation on creation
services_inactive_waiter: ecs.ServicesInactiveWaiter = client.get_waiter("services_inactive")
services_stable_waiter: ecs.ServicesStableWaiter = client.get_waiter("services_stable")
tasks_running_waiter: ecs.TasksRunningWaiter = client.get_waiter("tasks_running")
tasks_stopped_waiter: ecs.TasksStoppedWaiter = client.get_waiter("tasks_stopped")

# Paginators need type annotation on creation
list_account_settings_paginator: ecs.ListAccountSettingsPaginator = client.get_paginator("list_account_settings")
list_attributes_paginator: ecs.ListAttributesPaginator = client.get_paginator("list_attributes")
list_clusters_paginator: ecs.ListClustersPaginator = client.get_paginator("list_clusters")
list_container_instances_paginator: ecs.ListContainerInstancesPaginator = client.get_paginator("list_container_instances")
list_services_paginator: ecs.ListServicesPaginator = client.get_paginator("list_services")
list_task_definition_families_paginator: ecs.ListTaskDefinitionFamiliesPaginator = client.get_paginator("list_task_definition_families")
list_task_definitions_paginator: ecs.ListTaskDefinitionsPaginator = client.get_paginator("list_task_definitions")
list_tasks_paginator: ecs.ListTasksPaginator = client.get_paginator("list_tasks")
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