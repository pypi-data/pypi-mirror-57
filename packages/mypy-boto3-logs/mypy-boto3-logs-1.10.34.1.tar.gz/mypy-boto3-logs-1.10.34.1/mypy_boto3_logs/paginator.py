"Main interface for logs service Paginators"
from __future__ import annotations

import sys
from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_logs.type_defs import (
    DescribeDestinationsResponseTypeDef,
    DescribeExportTasksResponseTypeDef,
    DescribeLogGroupsResponseTypeDef,
    DescribeLogStreamsResponseTypeDef,
    DescribeMetricFiltersResponseTypeDef,
    DescribeQueriesResponseTypeDef,
    DescribeResourcePoliciesResponseTypeDef,
    DescribeSubscriptionFiltersResponseTypeDef,
    FilterLogEventsResponseTypeDef,
    PaginatorConfigTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = (
    "DescribeDestinationsPaginator",
    "DescribeExportTasksPaginator",
    "DescribeLogGroupsPaginator",
    "DescribeLogStreamsPaginator",
    "DescribeMetricFiltersPaginator",
    "DescribeQueriesPaginator",
    "DescribeResourcePoliciesPaginator",
    "DescribeSubscriptionFiltersPaginator",
    "FilterLogEventsPaginator",
)


class DescribeDestinationsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeDestinations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeDestinations)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, DestinationNamePrefix: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> DescribeDestinationsResponseTypeDef:
        """
        [DescribeDestinations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeDestinations.paginate)
        """


class DescribeExportTasksPaginator(Boto3Paginator):
    """
    [Paginator.DescribeExportTasks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeExportTasks)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        taskId: str = None,
        statusCode: Literal[
            "CANCELLED", "COMPLETED", "FAILED", "PENDING", "PENDING_CANCEL", "RUNNING"
        ] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> DescribeExportTasksResponseTypeDef:
        """
        [DescribeExportTasks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeExportTasks.paginate)
        """


class DescribeLogGroupsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeLogGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeLogGroups)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, logGroupNamePrefix: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> DescribeLogGroupsResponseTypeDef:
        """
        [DescribeLogGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeLogGroups.paginate)
        """


class DescribeLogStreamsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeLogStreams documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeLogStreams)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        logGroupName: str,
        logStreamNamePrefix: str = None,
        orderBy: Literal["LogStreamName", "LastEventTime"] = None,
        descending: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> DescribeLogStreamsResponseTypeDef:
        """
        [DescribeLogStreams.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeLogStreams.paginate)
        """


class DescribeMetricFiltersPaginator(Boto3Paginator):
    """
    [Paginator.DescribeMetricFilters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeMetricFilters)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        logGroupName: str = None,
        filterNamePrefix: str = None,
        metricName: str = None,
        metricNamespace: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> DescribeMetricFiltersResponseTypeDef:
        """
        [DescribeMetricFilters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeMetricFilters.paginate)
        """


class DescribeQueriesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeQueries documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeQueries)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        logGroupName: str = None,
        status: Literal["Scheduled", "Running", "Complete", "Failed", "Cancelled"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> DescribeQueriesResponseTypeDef:
        """
        [DescribeQueries.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeQueries.paginate)
        """


class DescribeResourcePoliciesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeResourcePolicies documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeResourcePolicies)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> DescribeResourcePoliciesResponseTypeDef:
        """
        [DescribeResourcePolicies.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeResourcePolicies.paginate)
        """


class DescribeSubscriptionFiltersPaginator(Boto3Paginator):
    """
    [Paginator.DescribeSubscriptionFilters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeSubscriptionFilters)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        logGroupName: str,
        filterNamePrefix: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> DescribeSubscriptionFiltersResponseTypeDef:
        """
        [DescribeSubscriptionFilters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/logs.html#CloudWatchLogs.Paginator.DescribeSubscriptionFilters.paginate)
        """


class FilterLogEventsPaginator(Boto3Paginator):
    """
    [Paginator.FilterLogEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/logs.html#CloudWatchLogs.Paginator.FilterLogEvents)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        logGroupName: str,
        logStreamNames: List[str] = None,
        logStreamNamePrefix: str = None,
        startTime: int = None,
        endTime: int = None,
        filterPattern: str = None,
        interleaved: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> FilterLogEventsResponseTypeDef:
        """
        [FilterLogEvents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/logs.html#CloudWatchLogs.Paginator.FilterLogEvents.paginate)
        """
