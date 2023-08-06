# mypy-boto3-dms

Mypy-friendly auto-generated type annotations for `boto3 dms 1.10.36` service.
More information can be found [here](https://github.com/vemel/mypy_boto3).

- [mypy-boto3-dms](#mypy-boto3-dms)
  - [How to use](#how-to-use)
    - [Type checking](#type-checking)
    - [Code auto-complete](#code-auto-complete)
  - [How it works](#how-it-works)

## How to use

### Type checking

Make sure you have [mypy](https://github.com/python/mypy) installed and activated in your IDE.

Install `boto3-stubs` for `dms` service.

```bash
python -m pip install boto3-stubs[mypy-boto3-dms]

# build service index. You should execute this command everytime
# you update boto3-stubs or install/remove services
python -m python -m mypy_boto3
```

Use `boto3` with `mypy_boto3` in your project and enjoy type checking.

```python
import boto3

from mypy_boto3 import dms
# alternative import if you do not want to install mypy_boto3 package
# import mypy_boto3_dms as dms

# Use this client as usual, now mypy can check if your code is valid.
# Check if your IDE supports function overloads,
# you probably do not need explicit type annotations
# client = boto3.client("dms")
client: dms.Client = boto3.client("dms")

# works for session as well
session = boto3.session.Session(region="us-west-1")
session_client: dms.Client = session.client("dms")


# Waiters need type annotation on creation
endpoint_deleted_waiter: dms.EndpointDeletedWaiter = client.get_waiter("endpoint_deleted")
replication_instance_available_waiter: dms.ReplicationInstanceAvailableWaiter = client.get_waiter("replication_instance_available")
replication_instance_deleted_waiter: dms.ReplicationInstanceDeletedWaiter = client.get_waiter("replication_instance_deleted")
replication_task_deleted_waiter: dms.ReplicationTaskDeletedWaiter = client.get_waiter("replication_task_deleted")
replication_task_ready_waiter: dms.ReplicationTaskReadyWaiter = client.get_waiter("replication_task_ready")
replication_task_running_waiter: dms.ReplicationTaskRunningWaiter = client.get_waiter("replication_task_running")
replication_task_stopped_waiter: dms.ReplicationTaskStoppedWaiter = client.get_waiter("replication_task_stopped")
test_connection_succeeds_waiter: dms.TestConnectionSucceedsWaiter = client.get_waiter("test_connection_succeeds")

# Paginators need type annotation on creation
describe_certificates_paginator: dms.DescribeCertificatesPaginator = client.get_paginator("describe_certificates")
describe_connections_paginator: dms.DescribeConnectionsPaginator = client.get_paginator("describe_connections")
describe_endpoint_types_paginator: dms.DescribeEndpointTypesPaginator = client.get_paginator("describe_endpoint_types")
describe_endpoints_paginator: dms.DescribeEndpointsPaginator = client.get_paginator("describe_endpoints")
describe_event_subscriptions_paginator: dms.DescribeEventSubscriptionsPaginator = client.get_paginator("describe_event_subscriptions")
describe_events_paginator: dms.DescribeEventsPaginator = client.get_paginator("describe_events")
describe_orderable_replication_instances_paginator: dms.DescribeOrderableReplicationInstancesPaginator = client.get_paginator("describe_orderable_replication_instances")
describe_replication_instances_paginator: dms.DescribeReplicationInstancesPaginator = client.get_paginator("describe_replication_instances")
describe_replication_subnet_groups_paginator: dms.DescribeReplicationSubnetGroupsPaginator = client.get_paginator("describe_replication_subnet_groups")
describe_replication_task_assessment_results_paginator: dms.DescribeReplicationTaskAssessmentResultsPaginator = client.get_paginator("describe_replication_task_assessment_results")
describe_replication_tasks_paginator: dms.DescribeReplicationTasksPaginator = client.get_paginator("describe_replication_tasks")
describe_schemas_paginator: dms.DescribeSchemasPaginator = client.get_paginator("describe_schemas")
describe_table_statistics_paginator: dms.DescribeTableStatisticsPaginator = client.get_paginator("describe_table_statistics")
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