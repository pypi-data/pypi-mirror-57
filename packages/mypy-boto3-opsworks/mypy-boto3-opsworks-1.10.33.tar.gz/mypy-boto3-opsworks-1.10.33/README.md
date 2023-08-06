# mypy-boto3-opsworks

Mypy-friendly auto-generated type annotations for `boto3 opsworks 1.10.33` service.
More information can be found [here](https://github.com/vemel/mypy_boto3).

- [mypy-boto3-opsworks](#mypy-boto3-opsworks)
  - [How to use](#how-to-use)
    - [Type checking](#type-checking)
    - [Code auto-complete](#code-auto-complete)
  - [How it works](#how-it-works)

## How to use

### Type checking

Make sure you have [mypy](https://github.com/python/mypy) installed and activated in your IDE.

Install `boto3-stubs` for `opsworks` service.

```bash
pip install boto3-stubs[mypy-boto3-opsworks]
```

Use `boto3` with `mypy_boto3` in your project and enjoy type checking.

```python
import boto3

from mypy_boto3 import opsworks
# alternative import if you do not want to install mypy_boto3 package
# import mypy_boto3_opsworks as opsworks

# Use this client as usual, now mypy can check if your code is valid.
client: opsworks.Client = boto3.client("opsworks")

# works for session as well
session = boto3.session.Session(region="us-west-1")
session_client: opsworks.Client = session.client("opsworks")

# Do you prefer resource approach? We've got you covered!
resource: opsworks.ServiceResource = boto3.resource("opsworks")

# Waiters need type annotation on creation
app_exists_waiter: opsworks.AppExistsWaiter = client.get_waiter("app_exists")
deployment_successful_waiter: opsworks.DeploymentSuccessfulWaiter = client.get_waiter("deployment_successful")
instance_online_waiter: opsworks.InstanceOnlineWaiter = client.get_waiter("instance_online")
instance_registered_waiter: opsworks.InstanceRegisteredWaiter = client.get_waiter("instance_registered")
instance_stopped_waiter: opsworks.InstanceStoppedWaiter = client.get_waiter("instance_stopped")
instance_terminated_waiter: opsworks.InstanceTerminatedWaiter = client.get_waiter("instance_terminated")

# Paginators need type annotation on creation
describe_ecs_clusters_paginator: opsworks.DescribeEcsClustersPaginator = client.get_paginator("describe_ecs_clusters")
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