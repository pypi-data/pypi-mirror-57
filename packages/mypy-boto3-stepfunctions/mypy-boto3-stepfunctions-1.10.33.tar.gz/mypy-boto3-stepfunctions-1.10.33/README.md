# mypy-boto3-stepfunctions

Mypy-friendly auto-generated type annotations for `boto3 stepfunctions 1.10.33` service.
More information can be found [here](https://github.com/vemel/mypy_boto3).

- [mypy-boto3-stepfunctions](#mypy-boto3-stepfunctions)
  - [How to use](#how-to-use)
    - [Type checking](#type-checking)
    - [Code auto-complete](#code-auto-complete)
  - [How it works](#how-it-works)

## How to use

### Type checking

Make sure you have [mypy](https://github.com/python/mypy) installed and activated in your IDE.

Install `boto3-stubs` for `stepfunctions` service.

```bash
pip install boto3-stubs[mypy-boto3-stepfunctions]
```

Use `boto3` with `mypy_boto3` in your project and enjoy type checking.

```python
import boto3

from mypy_boto3 import stepfunctions
# alternative import if you do not want to install mypy_boto3 package
# import mypy_boto3_stepfunctions as stepfunctions

# Use this client as usual, now mypy can check if your code is valid.
client: stepfunctions.Client = boto3.client("stepfunctions")

# works for session as well
session = boto3.session.Session(region="us-west-1")
session_client: stepfunctions.Client = session.client("stepfunctions")


# Paginators need type annotation on creation
get_execution_history_paginator: stepfunctions.GetExecutionHistoryPaginator = client.get_paginator("get_execution_history")
list_activities_paginator: stepfunctions.ListActivitiesPaginator = client.get_paginator("list_activities")
list_executions_paginator: stepfunctions.ListExecutionsPaginator = client.get_paginator("list_executions")
list_state_machines_paginator: stepfunctions.ListStateMachinesPaginator = client.get_paginator("list_state_machines")
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