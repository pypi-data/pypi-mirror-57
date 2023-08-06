# mypy-boto3-appstream

Mypy-friendly auto-generated type annotations for `boto3 appstream 1.10.33` service.
More information can be found [here](https://github.com/vemel/mypy_boto3).

- [mypy-boto3-appstream](#mypy-boto3-appstream)
  - [How to use](#how-to-use)
    - [Type checking](#type-checking)
    - [Code auto-complete](#code-auto-complete)
  - [How it works](#how-it-works)

## How to use

### Type checking

Make sure you have [mypy](https://github.com/python/mypy) installed and activated in your IDE.

Install `boto3-stubs` for `appstream` service.

```bash
pip install boto3-stubs[mypy-boto3-appstream]
```

Use `boto3` with `mypy_boto3` in your project and enjoy type checking.

```python
import boto3

from mypy_boto3 import appstream
# alternative import if you do not want to install mypy_boto3 package
# import mypy_boto3_appstream as appstream

# Use this client as usual, now mypy can check if your code is valid.
client: appstream.Client = boto3.client("appstream")

# works for session as well
session = boto3.session.Session(region="us-west-1")
session_client: appstream.Client = session.client("appstream")


# Waiters need type annotation on creation
fleet_started_waiter: appstream.FleetStartedWaiter = client.get_waiter("fleet_started")
fleet_stopped_waiter: appstream.FleetStoppedWaiter = client.get_waiter("fleet_stopped")

# Paginators need type annotation on creation
describe_directory_configs_paginator: appstream.DescribeDirectoryConfigsPaginator = client.get_paginator("describe_directory_configs")
describe_fleets_paginator: appstream.DescribeFleetsPaginator = client.get_paginator("describe_fleets")
describe_image_builders_paginator: appstream.DescribeImageBuildersPaginator = client.get_paginator("describe_image_builders")
describe_images_paginator: appstream.DescribeImagesPaginator = client.get_paginator("describe_images")
describe_sessions_paginator: appstream.DescribeSessionsPaginator = client.get_paginator("describe_sessions")
describe_stacks_paginator: appstream.DescribeStacksPaginator = client.get_paginator("describe_stacks")
describe_user_stack_associations_paginator: appstream.DescribeUserStackAssociationsPaginator = client.get_paginator("describe_user_stack_associations")
describe_users_paginator: appstream.DescribeUsersPaginator = client.get_paginator("describe_users")
list_associated_fleets_paginator: appstream.ListAssociatedFleetsPaginator = client.get_paginator("list_associated_fleets")
list_associated_stacks_paginator: appstream.ListAssociatedStacksPaginator = client.get_paginator("list_associated_stacks")
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