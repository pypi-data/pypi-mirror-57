"Main interface for elasticache service Waiters"
from __future__ import annotations

from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_elasticache.type_defs import (
    CacheClusterAvailableWaitWaiterConfigTypeDef,
    CacheClusterDeletedWaitWaiterConfigTypeDef,
    ReplicationGroupAvailableWaitWaiterConfigTypeDef,
    ReplicationGroupDeletedWaitWaiterConfigTypeDef,
)


__all__ = (
    "CacheClusterAvailableWaiter",
    "CacheClusterDeletedWaiter",
    "ReplicationGroupAvailableWaiter",
    "ReplicationGroupDeletedWaiter",
)


class CacheClusterAvailableWaiter(Boto3Waiter):
    """
    Waiter for `cache_cluster_available` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        CacheClusterId: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        ShowCacheNodeInfo: bool = None,
        ShowCacheClustersNotInReplicationGroups: bool = None,
        WaiterConfig: CacheClusterAvailableWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        Polls :py:meth:`ElastiCache.Client.describe_cache_clusters` every 15 seconds until a
        successful state is reached. An error is returned after 40 failed checks.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/DescribeCacheClusters>`_

        **Request Syntax**
        ::

          waiter.wait(
              CacheClusterId='string',
              MaxRecords=123,
              Marker='string',
              ShowCacheNodeInfo=True|False,
              ShowCacheClustersNotInReplicationGroups=True|False,
              WaiterConfig={
                  'Delay': 123,
                  'MaxAttempts': 123
              }
          )
        :type CacheClusterId: string
        :param CacheClusterId:

          The user-supplied cluster identifier. If this parameter is specified, only information
          about that specific cluster is returned. This parameter isn't case sensitive.

        :type MaxRecords: integer
        :param MaxRecords:

          The maximum number of records to include in the response. If more records exist than the
          specified ``MaxRecords`` value, a marker is included in the response so that the remaining
          results can be retrieved.

          Default: 100

          Constraints: minimum 20; maximum 100.

        :type Marker: string
        :param Marker:

          An optional marker returned from a prior request. Use this marker for pagination of
          results from this operation. If this parameter is specified, the response includes only
          records beyond the marker, up to the value specified by ``MaxRecords`` .

        :type ShowCacheNodeInfo: boolean
        :param ShowCacheNodeInfo:

          An optional flag that can be included in the ``DescribeCacheCluster`` request to retrieve
          information about the individual cache nodes.

        :type ShowCacheClustersNotInReplicationGroups: boolean
        :param ShowCacheClustersNotInReplicationGroups:

          An optional flag that can be included in the ``DescribeCacheCluster`` request to show only
          nodes (API/CLI: clusters) that are not members of a replication group. In practice, this
          mean Memcached and single node Redis clusters.

        :type WaiterConfig: dict
        :param WaiterConfig:

          A dictionary that provides parameters to control waiting behavior.

          - **Delay** *(integer) --*

            The amount of time in seconds to wait between attempts. Default: 15

          - **MaxAttempts** *(integer) --*

            The maximum number of attempts to be made. Default: 40

        :returns: None
        """


class CacheClusterDeletedWaiter(Boto3Waiter):
    """
    Waiter for `cache_cluster_deleted` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        CacheClusterId: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        ShowCacheNodeInfo: bool = None,
        ShowCacheClustersNotInReplicationGroups: bool = None,
        WaiterConfig: CacheClusterDeletedWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        Polls :py:meth:`ElastiCache.Client.describe_cache_clusters` every 15 seconds until a
        successful state is reached. An error is returned after 40 failed checks.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/DescribeCacheClusters>`_

        **Request Syntax**
        ::

          waiter.wait(
              CacheClusterId='string',
              MaxRecords=123,
              Marker='string',
              ShowCacheNodeInfo=True|False,
              ShowCacheClustersNotInReplicationGroups=True|False,
              WaiterConfig={
                  'Delay': 123,
                  'MaxAttempts': 123
              }
          )
        :type CacheClusterId: string
        :param CacheClusterId:

          The user-supplied cluster identifier. If this parameter is specified, only information
          about that specific cluster is returned. This parameter isn't case sensitive.

        :type MaxRecords: integer
        :param MaxRecords:

          The maximum number of records to include in the response. If more records exist than the
          specified ``MaxRecords`` value, a marker is included in the response so that the remaining
          results can be retrieved.

          Default: 100

          Constraints: minimum 20; maximum 100.

        :type Marker: string
        :param Marker:

          An optional marker returned from a prior request. Use this marker for pagination of
          results from this operation. If this parameter is specified, the response includes only
          records beyond the marker, up to the value specified by ``MaxRecords`` .

        :type ShowCacheNodeInfo: boolean
        :param ShowCacheNodeInfo:

          An optional flag that can be included in the ``DescribeCacheCluster`` request to retrieve
          information about the individual cache nodes.

        :type ShowCacheClustersNotInReplicationGroups: boolean
        :param ShowCacheClustersNotInReplicationGroups:

          An optional flag that can be included in the ``DescribeCacheCluster`` request to show only
          nodes (API/CLI: clusters) that are not members of a replication group. In practice, this
          mean Memcached and single node Redis clusters.

        :type WaiterConfig: dict
        :param WaiterConfig:

          A dictionary that provides parameters to control waiting behavior.

          - **Delay** *(integer) --*

            The amount of time in seconds to wait between attempts. Default: 15

          - **MaxAttempts** *(integer) --*

            The maximum number of attempts to be made. Default: 40

        :returns: None
        """


class ReplicationGroupAvailableWaiter(Boto3Waiter):
    """
    Waiter for `replication_group_available` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        ReplicationGroupId: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        WaiterConfig: ReplicationGroupAvailableWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        Polls :py:meth:`ElastiCache.Client.describe_replication_groups` every 15 seconds until a
        successful state is reached. An error is returned after 40 failed checks.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/DescribeReplicationGroups>`_

        **Request Syntax**
        ::

          waiter.wait(
              ReplicationGroupId='string',
              MaxRecords=123,
              Marker='string',
              WaiterConfig={
                  'Delay': 123,
                  'MaxAttempts': 123
              }
          )
        :type ReplicationGroupId: string
        :param ReplicationGroupId:

          The identifier for the replication group to be described. This parameter is not case
          sensitive.

          If you do not specify this parameter, information about all replication groups is
          returned.

        :type MaxRecords: integer
        :param MaxRecords:

          The maximum number of records to include in the response. If more records exist than the
          specified ``MaxRecords`` value, a marker is included in the response so that the remaining
          results can be retrieved.

          Default: 100

          Constraints: minimum 20; maximum 100.

        :type Marker: string
        :param Marker:

          An optional marker returned from a prior request. Use this marker for pagination of
          results from this operation. If this parameter is specified, the response includes only
          records beyond the marker, up to the value specified by ``MaxRecords`` .

        :type WaiterConfig: dict
        :param WaiterConfig:

          A dictionary that provides parameters to control waiting behavior.

          - **Delay** *(integer) --*

            The amount of time in seconds to wait between attempts. Default: 15

          - **MaxAttempts** *(integer) --*

            The maximum number of attempts to be made. Default: 40

        :returns: None
        """


class ReplicationGroupDeletedWaiter(Boto3Waiter):
    """
    Waiter for `replication_group_deleted` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        ReplicationGroupId: str = None,
        MaxRecords: int = None,
        Marker: str = None,
        WaiterConfig: ReplicationGroupDeletedWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        Polls :py:meth:`ElastiCache.Client.describe_replication_groups` every 15 seconds until a
        successful state is reached. An error is returned after 40 failed checks.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/DescribeReplicationGroups>`_

        **Request Syntax**
        ::

          waiter.wait(
              ReplicationGroupId='string',
              MaxRecords=123,
              Marker='string',
              WaiterConfig={
                  'Delay': 123,
                  'MaxAttempts': 123
              }
          )
        :type ReplicationGroupId: string
        :param ReplicationGroupId:

          The identifier for the replication group to be described. This parameter is not case
          sensitive.

          If you do not specify this parameter, information about all replication groups is
          returned.

        :type MaxRecords: integer
        :param MaxRecords:

          The maximum number of records to include in the response. If more records exist than the
          specified ``MaxRecords`` value, a marker is included in the response so that the remaining
          results can be retrieved.

          Default: 100

          Constraints: minimum 20; maximum 100.

        :type Marker: string
        :param Marker:

          An optional marker returned from a prior request. Use this marker for pagination of
          results from this operation. If this parameter is specified, the response includes only
          records beyond the marker, up to the value specified by ``MaxRecords`` .

        :type WaiterConfig: dict
        :param WaiterConfig:

          A dictionary that provides parameters to control waiting behavior.

          - **Delay** *(integer) --*

            The amount of time in seconds to wait between attempts. Default: 15

          - **MaxAttempts** *(integer) --*

            The maximum number of attempts to be made. Default: 40

        :returns: None
        """
