# mypy-boto3-swf

Mypy-friendly auto-generated type annotations for `boto3 swf 1.10.33` service.
More information can be found [here](https://github.com/vemel/mypy_boto3).

- [mypy-boto3-swf](#mypy-boto3-swf)
  - [How to use](#how-to-use)
    - [Type checking](#type-checking)
    - [Code auto-complete](#code-auto-complete)
  - [How it works](#how-it-works)

## How to use

### Type checking

Make sure you have [mypy](https://github.com/python/mypy) installed and activated in your IDE.

Install `boto3-stubs` for `swf` service.

```bash
pip install boto3-stubs[mypy-boto3-swf]
```

Use `boto3` with `mypy_boto3` in your project and enjoy type checking.

```python
import boto3

from mypy_boto3 import swf
# alternative import if you do not want to install mypy_boto3 package
# import mypy_boto3_swf as swf

# Use this client as usual, now mypy can check if your code is valid.
client: swf.Client = boto3.client("swf")

# works for session as well
session = boto3.session.Session(region="us-west-1")
session_client: swf.Client = session.client("swf")


# Paginators need type annotation on creation
get_workflow_execution_history_paginator: swf.GetWorkflowExecutionHistoryPaginator = client.get_paginator("get_workflow_execution_history")
list_activity_types_paginator: swf.ListActivityTypesPaginator = client.get_paginator("list_activity_types")
list_closed_workflow_executions_paginator: swf.ListClosedWorkflowExecutionsPaginator = client.get_paginator("list_closed_workflow_executions")
list_domains_paginator: swf.ListDomainsPaginator = client.get_paginator("list_domains")
list_open_workflow_executions_paginator: swf.ListOpenWorkflowExecutionsPaginator = client.get_paginator("list_open_workflow_executions")
list_workflow_types_paginator: swf.ListWorkflowTypesPaginator = client.get_paginator("list_workflow_types")
poll_for_decision_task_paginator: swf.PollForDecisionTaskPaginator = client.get_paginator("poll_for_decision_task")
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