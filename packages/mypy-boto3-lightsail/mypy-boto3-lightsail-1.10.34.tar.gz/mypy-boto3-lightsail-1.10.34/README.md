# mypy-boto3-lightsail

Mypy-friendly auto-generated type annotations for `boto3 lightsail 1.10.34` service.
More information can be found [here](https://github.com/vemel/mypy_boto3).

- [mypy-boto3-lightsail](#mypy-boto3-lightsail)
  - [How to use](#how-to-use)
    - [Type checking](#type-checking)
    - [Code auto-complete](#code-auto-complete)
  - [How it works](#how-it-works)

## How to use

### Type checking

Make sure you have [mypy](https://github.com/python/mypy) installed and activated in your IDE.

Install `boto3-stubs` for `lightsail` service.

```bash
pip install boto3-stubs[mypy-boto3-lightsail]
```

Use `boto3` with `mypy_boto3` in your project and enjoy type checking.

```python
import boto3

from mypy_boto3 import lightsail
# alternative import if you do not want to install mypy_boto3 package
# import mypy_boto3_lightsail as lightsail

# Use this client as usual, now mypy can check if your code is valid.
client: lightsail.Client = boto3.client("lightsail")

# works for session as well
session = boto3.session.Session(region="us-west-1")
session_client: lightsail.Client = session.client("lightsail")


# Paginators need type annotation on creation
get_active_names_paginator: lightsail.GetActiveNamesPaginator = client.get_paginator("get_active_names")
get_blueprints_paginator: lightsail.GetBlueprintsPaginator = client.get_paginator("get_blueprints")
get_bundles_paginator: lightsail.GetBundlesPaginator = client.get_paginator("get_bundles")
get_cloud_formation_stack_records_paginator: lightsail.GetCloudFormationStackRecordsPaginator = client.get_paginator("get_cloud_formation_stack_records")
get_disk_snapshots_paginator: lightsail.GetDiskSnapshotsPaginator = client.get_paginator("get_disk_snapshots")
get_disks_paginator: lightsail.GetDisksPaginator = client.get_paginator("get_disks")
get_domains_paginator: lightsail.GetDomainsPaginator = client.get_paginator("get_domains")
get_export_snapshot_records_paginator: lightsail.GetExportSnapshotRecordsPaginator = client.get_paginator("get_export_snapshot_records")
get_instance_snapshots_paginator: lightsail.GetInstanceSnapshotsPaginator = client.get_paginator("get_instance_snapshots")
get_instances_paginator: lightsail.GetInstancesPaginator = client.get_paginator("get_instances")
get_key_pairs_paginator: lightsail.GetKeyPairsPaginator = client.get_paginator("get_key_pairs")
get_load_balancers_paginator: lightsail.GetLoadBalancersPaginator = client.get_paginator("get_load_balancers")
get_operations_paginator: lightsail.GetOperationsPaginator = client.get_paginator("get_operations")
get_relational_database_blueprints_paginator: lightsail.GetRelationalDatabaseBlueprintsPaginator = client.get_paginator("get_relational_database_blueprints")
get_relational_database_bundles_paginator: lightsail.GetRelationalDatabaseBundlesPaginator = client.get_paginator("get_relational_database_bundles")
get_relational_database_events_paginator: lightsail.GetRelationalDatabaseEventsPaginator = client.get_paginator("get_relational_database_events")
get_relational_database_parameters_paginator: lightsail.GetRelationalDatabaseParametersPaginator = client.get_paginator("get_relational_database_parameters")
get_relational_database_snapshots_paginator: lightsail.GetRelationalDatabaseSnapshotsPaginator = client.get_paginator("get_relational_database_snapshots")
get_relational_databases_paginator: lightsail.GetRelationalDatabasesPaginator = client.get_paginator("get_relational_databases")
get_static_ips_paginator: lightsail.GetStaticIpsPaginator = client.get_paginator("get_static_ips")
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