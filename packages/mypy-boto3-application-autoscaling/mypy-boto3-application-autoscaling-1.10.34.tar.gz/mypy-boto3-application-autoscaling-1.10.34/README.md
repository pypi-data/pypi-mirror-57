# mypy-boto3-application-autoscaling

Mypy-friendly auto-generated type annotations for `boto3 application-autoscaling 1.10.34` service.
More information can be found [here](https://github.com/vemel/mypy_boto3).

- [mypy-boto3-application-autoscaling](#mypy-boto3-application-autoscaling)
  - [How to use](#how-to-use)
    - [Type checking](#type-checking)
    - [Code auto-complete](#code-auto-complete)
  - [How it works](#how-it-works)

## How to use

### Type checking

Make sure you have [mypy](https://github.com/python/mypy) installed and activated in your IDE.

Install `boto3-stubs` for `application-autoscaling` service.

```bash
pip install boto3-stubs[mypy-boto3-application-autoscaling]
```

Use `boto3` with `mypy_boto3` in your project and enjoy type checking.

```python
import boto3

from mypy_boto3 import application_autoscaling
# alternative import if you do not want to install mypy_boto3 package
# import mypy_boto3_application_autoscaling as application_autoscaling

# Use this client as usual, now mypy can check if your code is valid.
client: application_autoscaling.Client = boto3.client("application-autoscaling")

# works for session as well
session = boto3.session.Session(region="us-west-1")
session_client: application_autoscaling.Client = session.client("application-autoscaling")


# Paginators need type annotation on creation
describe_scalable_targets_paginator: application_autoscaling.DescribeScalableTargetsPaginator = client.get_paginator("describe_scalable_targets")
describe_scaling_activities_paginator: application_autoscaling.DescribeScalingActivitiesPaginator = client.get_paginator("describe_scaling_activities")
describe_scaling_policies_paginator: application_autoscaling.DescribeScalingPoliciesPaginator = client.get_paginator("describe_scaling_policies")
describe_scheduled_actions_paginator: application_autoscaling.DescribeScheduledActionsPaginator = client.get_paginator("describe_scheduled_actions")
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