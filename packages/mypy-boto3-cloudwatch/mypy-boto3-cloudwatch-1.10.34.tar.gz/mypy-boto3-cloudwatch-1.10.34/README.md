# mypy-boto3-cloudwatch

Mypy-friendly auto-generated type annotations for `boto3 cloudwatch 1.10.34` service.
More information can be found [here](https://github.com/vemel/mypy_boto3).

- [mypy-boto3-cloudwatch](#mypy-boto3-cloudwatch)
  - [How to use](#how-to-use)
    - [Type checking](#type-checking)
    - [Code auto-complete](#code-auto-complete)
  - [How it works](#how-it-works)

## How to use

### Type checking

Make sure you have [mypy](https://github.com/python/mypy) installed and activated in your IDE.

Install `boto3-stubs` for `cloudwatch` service.

```bash
pip install boto3-stubs[mypy-boto3-cloudwatch]
```

Use `boto3` with `mypy_boto3` in your project and enjoy type checking.

```python
import boto3

from mypy_boto3 import cloudwatch
# alternative import if you do not want to install mypy_boto3 package
# import mypy_boto3_cloudwatch as cloudwatch

# Use this client as usual, now mypy can check if your code is valid.
client: cloudwatch.Client = boto3.client("cloudwatch")

# works for session as well
session = boto3.session.Session(region="us-west-1")
session_client: cloudwatch.Client = session.client("cloudwatch")

# Do you prefer resource approach? We've got you covered!
resource: cloudwatch.ServiceResource = boto3.resource("cloudwatch")

# Waiters need type annotation on creation
alarm_exists_waiter: cloudwatch.AlarmExistsWaiter = client.get_waiter("alarm_exists")

# Paginators need type annotation on creation
describe_alarm_history_paginator: cloudwatch.DescribeAlarmHistoryPaginator = client.get_paginator("describe_alarm_history")
describe_alarms_paginator: cloudwatch.DescribeAlarmsPaginator = client.get_paginator("describe_alarms")
get_metric_data_paginator: cloudwatch.GetMetricDataPaginator = client.get_paginator("get_metric_data")
list_dashboards_paginator: cloudwatch.ListDashboardsPaginator = client.get_paginator("list_dashboards")
list_metrics_paginator: cloudwatch.ListMetricsPaginator = client.get_paginator("list_metrics")
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