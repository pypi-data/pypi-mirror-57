# mypy-boto3-robomaker

Mypy-friendly auto-generated type annotations for `boto3 robomaker 1.10.33` service.
More information can be found [here](https://github.com/vemel/mypy_boto3).

- [mypy-boto3-robomaker](#mypy-boto3-robomaker)
  - [How to use](#how-to-use)
    - [Type checking](#type-checking)
    - [Code auto-complete](#code-auto-complete)
  - [How it works](#how-it-works)

## How to use

### Type checking

Make sure you have [mypy](https://github.com/python/mypy) installed and activated in your IDE.

Install `boto3-stubs` for `robomaker` service.

```bash
pip install boto3-stubs[mypy-boto3-robomaker]
```

Use `boto3` with `mypy_boto3` in your project and enjoy type checking.

```python
import boto3

from mypy_boto3 import robomaker
# alternative import if you do not want to install mypy_boto3 package
# import mypy_boto3_robomaker as robomaker

# Use this client as usual, now mypy can check if your code is valid.
client: robomaker.Client = boto3.client("robomaker")

# works for session as well
session = boto3.session.Session(region="us-west-1")
session_client: robomaker.Client = session.client("robomaker")


# Paginators need type annotation on creation
list_deployment_jobs_paginator: robomaker.ListDeploymentJobsPaginator = client.get_paginator("list_deployment_jobs")
list_fleets_paginator: robomaker.ListFleetsPaginator = client.get_paginator("list_fleets")
list_robot_applications_paginator: robomaker.ListRobotApplicationsPaginator = client.get_paginator("list_robot_applications")
list_robots_paginator: robomaker.ListRobotsPaginator = client.get_paginator("list_robots")
list_simulation_applications_paginator: robomaker.ListSimulationApplicationsPaginator = client.get_paginator("list_simulation_applications")
list_simulation_jobs_paginator: robomaker.ListSimulationJobsPaginator = client.get_paginator("list_simulation_jobs")
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