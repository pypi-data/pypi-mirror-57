# mypy-boto3-elasticache

Mypy-friendly auto-generated type annotations for `boto3 elasticache 1.10.33` service.
More information can be found [here](https://github.com/vemel/mypy_boto3).

- [mypy-boto3-elasticache](#mypy-boto3-elasticache)
  - [How to use](#how-to-use)
    - [Type checking](#type-checking)
    - [Code auto-complete](#code-auto-complete)
  - [How it works](#how-it-works)

## How to use

### Type checking

Make sure you have [mypy](https://github.com/python/mypy) installed and activated in your IDE.

Install `boto3-stubs` for `elasticache` service.

```bash
pip install boto3-stubs[mypy-boto3-elasticache]
```

Use `boto3` with `mypy_boto3` in your project and enjoy type checking.

```python
import boto3

from mypy_boto3 import elasticache
# alternative import if you do not want to install mypy_boto3 package
# import mypy_boto3_elasticache as elasticache

# Use this client as usual, now mypy can check if your code is valid.
client: elasticache.Client = boto3.client("elasticache")

# works for session as well
session = boto3.session.Session(region="us-west-1")
session_client: elasticache.Client = session.client("elasticache")


# Waiters need type annotation on creation
cache_cluster_available_waiter: elasticache.CacheClusterAvailableWaiter = client.get_waiter("cache_cluster_available")
cache_cluster_deleted_waiter: elasticache.CacheClusterDeletedWaiter = client.get_waiter("cache_cluster_deleted")
replication_group_available_waiter: elasticache.ReplicationGroupAvailableWaiter = client.get_waiter("replication_group_available")
replication_group_deleted_waiter: elasticache.ReplicationGroupDeletedWaiter = client.get_waiter("replication_group_deleted")

# Paginators need type annotation on creation
describe_cache_clusters_paginator: elasticache.DescribeCacheClustersPaginator = client.get_paginator("describe_cache_clusters")
describe_cache_engine_versions_paginator: elasticache.DescribeCacheEngineVersionsPaginator = client.get_paginator("describe_cache_engine_versions")
describe_cache_parameter_groups_paginator: elasticache.DescribeCacheParameterGroupsPaginator = client.get_paginator("describe_cache_parameter_groups")
describe_cache_parameters_paginator: elasticache.DescribeCacheParametersPaginator = client.get_paginator("describe_cache_parameters")
describe_cache_security_groups_paginator: elasticache.DescribeCacheSecurityGroupsPaginator = client.get_paginator("describe_cache_security_groups")
describe_cache_subnet_groups_paginator: elasticache.DescribeCacheSubnetGroupsPaginator = client.get_paginator("describe_cache_subnet_groups")
describe_engine_default_parameters_paginator: elasticache.DescribeEngineDefaultParametersPaginator = client.get_paginator("describe_engine_default_parameters")
describe_events_paginator: elasticache.DescribeEventsPaginator = client.get_paginator("describe_events")
describe_replication_groups_paginator: elasticache.DescribeReplicationGroupsPaginator = client.get_paginator("describe_replication_groups")
describe_reserved_cache_nodes_paginator: elasticache.DescribeReservedCacheNodesPaginator = client.get_paginator("describe_reserved_cache_nodes")
describe_reserved_cache_nodes_offerings_paginator: elasticache.DescribeReservedCacheNodesOfferingsPaginator = client.get_paginator("describe_reserved_cache_nodes_offerings")
describe_service_updates_paginator: elasticache.DescribeServiceUpdatesPaginator = client.get_paginator("describe_service_updates")
describe_snapshots_paginator: elasticache.DescribeSnapshotsPaginator = client.get_paginator("describe_snapshots")
describe_update_actions_paginator: elasticache.DescribeUpdateActionsPaginator = client.get_paginator("describe_update_actions")
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