"Main interface for dms service Paginators"
from __future__ import annotations

from datetime import datetime
import sys
from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_dms.type_defs import (
    DescribeCertificatesResponseTypeDef,
    DescribeConnectionsResponseTypeDef,
    DescribeEndpointTypesResponseTypeDef,
    DescribeEndpointsResponseTypeDef,
    DescribeEventSubscriptionsResponseTypeDef,
    DescribeEventsResponseTypeDef,
    DescribeOrderableReplicationInstancesResponseTypeDef,
    DescribeReplicationInstancesResponseTypeDef,
    DescribeReplicationSubnetGroupsResponseTypeDef,
    DescribeReplicationTaskAssessmentResultsResponseTypeDef,
    DescribeReplicationTasksResponseTypeDef,
    DescribeSchemasResponseTypeDef,
    DescribeTableStatisticsResponseTypeDef,
    FilterTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "DescribeCertificatesPaginator",
    "DescribeConnectionsPaginator",
    "DescribeEndpointTypesPaginator",
    "DescribeEndpointsPaginator",
    "DescribeEventSubscriptionsPaginator",
    "DescribeEventsPaginator",
    "DescribeOrderableReplicationInstancesPaginator",
    "DescribeReplicationInstancesPaginator",
    "DescribeReplicationSubnetGroupsPaginator",
    "DescribeReplicationTaskAssessmentResultsPaginator",
    "DescribeReplicationTasksPaginator",
    "DescribeSchemasPaginator",
    "DescribeTableStatisticsPaginator",
)


class DescribeCertificatesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeCertificates documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeCertificates)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, Filters: List[FilterTypeDef] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> DescribeCertificatesResponseTypeDef:
        """
        [DescribeCertificates.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeCertificates.paginate)
        """


class DescribeConnectionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeConnections documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeConnections)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, Filters: List[FilterTypeDef] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> DescribeConnectionsResponseTypeDef:
        """
        [DescribeConnections.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeConnections.paginate)
        """


class DescribeEndpointTypesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeEndpointTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeEndpointTypes)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, Filters: List[FilterTypeDef] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> DescribeEndpointTypesResponseTypeDef:
        """
        [DescribeEndpointTypes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeEndpointTypes.paginate)
        """


class DescribeEndpointsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeEndpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeEndpoints)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, Filters: List[FilterTypeDef] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> DescribeEndpointsResponseTypeDef:
        """
        [DescribeEndpoints.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeEndpoints.paginate)
        """


class DescribeEventSubscriptionsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeEventSubscriptions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeEventSubscriptions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        SubscriptionName: str = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> DescribeEventSubscriptionsResponseTypeDef:
        """
        [DescribeEventSubscriptions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeEventSubscriptions.paginate)
        """


class DescribeEventsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeEvents)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        SourceIdentifier: str = None,
        SourceType: Literal["replication-instance"] = None,
        StartTime: datetime = None,
        EndTime: datetime = None,
        Duration: int = None,
        EventCategories: List[str] = None,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> DescribeEventsResponseTypeDef:
        """
        [DescribeEvents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeEvents.paginate)
        """


class DescribeOrderableReplicationInstancesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeOrderableReplicationInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeOrderableReplicationInstances)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> DescribeOrderableReplicationInstancesResponseTypeDef:
        """
        [DescribeOrderableReplicationInstances.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeOrderableReplicationInstances.paginate)
        """


class DescribeReplicationInstancesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeReplicationInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeReplicationInstances)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, Filters: List[FilterTypeDef] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> DescribeReplicationInstancesResponseTypeDef:
        """
        [DescribeReplicationInstances.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeReplicationInstances.paginate)
        """


class DescribeReplicationSubnetGroupsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeReplicationSubnetGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeReplicationSubnetGroups)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, Filters: List[FilterTypeDef] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> DescribeReplicationSubnetGroupsResponseTypeDef:
        """
        [DescribeReplicationSubnetGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeReplicationSubnetGroups.paginate)
        """


class DescribeReplicationTaskAssessmentResultsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeReplicationTaskAssessmentResults documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeReplicationTaskAssessmentResults)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, ReplicationTaskArn: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> DescribeReplicationTaskAssessmentResultsResponseTypeDef:
        """
        [DescribeReplicationTaskAssessmentResults.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeReplicationTaskAssessmentResults.paginate)
        """


class DescribeReplicationTasksPaginator(Boto3Paginator):
    """
    [Paginator.DescribeReplicationTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeReplicationTasks)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        Filters: List[FilterTypeDef] = None,
        WithoutSettings: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> DescribeReplicationTasksResponseTypeDef:
        """
        [DescribeReplicationTasks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeReplicationTasks.paginate)
        """


class DescribeSchemasPaginator(Boto3Paginator):
    """
    [Paginator.DescribeSchemas documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeSchemas)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, EndpointArn: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> DescribeSchemasResponseTypeDef:
        """
        [DescribeSchemas.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeSchemas.paginate)
        """


class DescribeTableStatisticsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeTableStatistics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeTableStatistics)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ReplicationTaskArn: str,
        Filters: List[FilterTypeDef] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> DescribeTableStatisticsResponseTypeDef:
        """
        [DescribeTableStatistics.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/dms.html#DatabaseMigrationService.Paginator.DescribeTableStatistics.paginate)
        """
