# mypy-boto3-cloudformation

Mypy-friendly auto-generated type annotations for `boto3 cloudformation 1.10.33` service.
More information can be found [here](https://github.com/vemel/mypy_boto3).

- [mypy-boto3-cloudformation](#mypy-boto3-cloudformation)
  - [How to use](#how-to-use)
    - [Type checking](#type-checking)
    - [Code auto-complete](#code-auto-complete)
  - [How it works](#how-it-works)

## How to use

### Type checking

Make sure you have [mypy](https://github.com/python/mypy) installed and activated in your IDE.

Install `boto3-stubs` for `cloudformation` service.

```bash
pip install boto3-stubs[mypy-boto3-cloudformation]
```

Use `boto3` with `mypy_boto3` in your project and enjoy type checking.

```python
import boto3

from mypy_boto3 import cloudformation
# alternative import if you do not want to install mypy_boto3 package
# import mypy_boto3_cloudformation as cloudformation

# Use this client as usual, now mypy can check if your code is valid.
client: cloudformation.Client = boto3.client("cloudformation")

# works for session as well
session = boto3.session.Session(region="us-west-1")
session_client: cloudformation.Client = session.client("cloudformation")

# Do you prefer resource approach? We've got you covered!
resource: cloudformation.ServiceResource = boto3.resource("cloudformation")

# Waiters need type annotation on creation
change_set_create_complete_waiter: cloudformation.ChangeSetCreateCompleteWaiter = client.get_waiter("change_set_create_complete")
stack_create_complete_waiter: cloudformation.StackCreateCompleteWaiter = client.get_waiter("stack_create_complete")
stack_delete_complete_waiter: cloudformation.StackDeleteCompleteWaiter = client.get_waiter("stack_delete_complete")
stack_exists_waiter: cloudformation.StackExistsWaiter = client.get_waiter("stack_exists")
stack_import_complete_waiter: cloudformation.StackImportCompleteWaiter = client.get_waiter("stack_import_complete")
stack_update_complete_waiter: cloudformation.StackUpdateCompleteWaiter = client.get_waiter("stack_update_complete")
type_registration_complete_waiter: cloudformation.TypeRegistrationCompleteWaiter = client.get_waiter("type_registration_complete")

# Paginators need type annotation on creation
describe_account_limits_paginator: cloudformation.DescribeAccountLimitsPaginator = client.get_paginator("describe_account_limits")
describe_change_set_paginator: cloudformation.DescribeChangeSetPaginator = client.get_paginator("describe_change_set")
describe_stack_events_paginator: cloudformation.DescribeStackEventsPaginator = client.get_paginator("describe_stack_events")
describe_stacks_paginator: cloudformation.DescribeStacksPaginator = client.get_paginator("describe_stacks")
list_change_sets_paginator: cloudformation.ListChangeSetsPaginator = client.get_paginator("list_change_sets")
list_exports_paginator: cloudformation.ListExportsPaginator = client.get_paginator("list_exports")
list_imports_paginator: cloudformation.ListImportsPaginator = client.get_paginator("list_imports")
list_stack_instances_paginator: cloudformation.ListStackInstancesPaginator = client.get_paginator("list_stack_instances")
list_stack_resources_paginator: cloudformation.ListStackResourcesPaginator = client.get_paginator("list_stack_resources")
list_stack_set_operation_results_paginator: cloudformation.ListStackSetOperationResultsPaginator = client.get_paginator("list_stack_set_operation_results")
list_stack_set_operations_paginator: cloudformation.ListStackSetOperationsPaginator = client.get_paginator("list_stack_set_operations")
list_stack_sets_paginator: cloudformation.ListStackSetsPaginator = client.get_paginator("list_stack_sets")
list_stacks_paginator: cloudformation.ListStacksPaginator = client.get_paginator("list_stacks")
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