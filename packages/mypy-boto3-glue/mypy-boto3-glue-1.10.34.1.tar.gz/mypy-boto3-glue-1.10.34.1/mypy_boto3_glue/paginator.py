"Main interface for glue service Paginators"
from __future__ import annotations

from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_glue.type_defs import (
    GetClassifiersResponseTypeDef,
    GetConnectionsFilterTypeDef,
    GetConnectionsResponseTypeDef,
    GetCrawlerMetricsResponseTypeDef,
    GetCrawlersResponseTypeDef,
    GetDatabasesResponseTypeDef,
    GetDevEndpointsResponseTypeDef,
    GetJobRunsResponseTypeDef,
    GetJobsResponseTypeDef,
    GetPartitionsResponseTypeDef,
    GetSecurityConfigurationsResponseTypeDef,
    GetTableVersionsResponseTypeDef,
    GetTablesResponseTypeDef,
    GetTriggersResponseTypeDef,
    GetUserDefinedFunctionsResponseTypeDef,
    PaginatorConfigTypeDef,
    SegmentTypeDef,
)


__all__ = (
    "GetClassifiersPaginator",
    "GetConnectionsPaginator",
    "GetCrawlerMetricsPaginator",
    "GetCrawlersPaginator",
    "GetDatabasesPaginator",
    "GetDevEndpointsPaginator",
    "GetJobRunsPaginator",
    "GetJobsPaginator",
    "GetPartitionsPaginator",
    "GetSecurityConfigurationsPaginator",
    "GetTableVersionsPaginator",
    "GetTablesPaginator",
    "GetTriggersPaginator",
    "GetUserDefinedFunctionsPaginator",
)


class GetClassifiersPaginator(Boto3Paginator):
    """
    [Paginator.GetClassifiers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/glue.html#Glue.Paginator.GetClassifiers)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> GetClassifiersResponseTypeDef:
        """
        [GetClassifiers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/glue.html#Glue.Paginator.GetClassifiers.paginate)
        """


class GetConnectionsPaginator(Boto3Paginator):
    """
    [Paginator.GetConnections documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/glue.html#Glue.Paginator.GetConnections)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        CatalogId: str = None,
        Filter: GetConnectionsFilterTypeDef = None,
        HidePassword: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> GetConnectionsResponseTypeDef:
        """
        [GetConnections.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/glue.html#Glue.Paginator.GetConnections.paginate)
        """


class GetCrawlerMetricsPaginator(Boto3Paginator):
    """
    [Paginator.GetCrawlerMetrics documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/glue.html#Glue.Paginator.GetCrawlerMetrics)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, CrawlerNameList: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> GetCrawlerMetricsResponseTypeDef:
        """
        [GetCrawlerMetrics.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/glue.html#Glue.Paginator.GetCrawlerMetrics.paginate)
        """


class GetCrawlersPaginator(Boto3Paginator):
    """
    [Paginator.GetCrawlers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/glue.html#Glue.Paginator.GetCrawlers)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> GetCrawlersResponseTypeDef:
        """
        [GetCrawlers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/glue.html#Glue.Paginator.GetCrawlers.paginate)
        """


class GetDatabasesPaginator(Boto3Paginator):
    """
    [Paginator.GetDatabases documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/glue.html#Glue.Paginator.GetDatabases)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, CatalogId: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> GetDatabasesResponseTypeDef:
        """
        [GetDatabases.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/glue.html#Glue.Paginator.GetDatabases.paginate)
        """


class GetDevEndpointsPaginator(Boto3Paginator):
    """
    [Paginator.GetDevEndpoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/glue.html#Glue.Paginator.GetDevEndpoints)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> GetDevEndpointsResponseTypeDef:
        """
        [GetDevEndpoints.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/glue.html#Glue.Paginator.GetDevEndpoints.paginate)
        """


class GetJobRunsPaginator(Boto3Paginator):
    """
    [Paginator.GetJobRuns documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/glue.html#Glue.Paginator.GetJobRuns)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, JobName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> GetJobRunsResponseTypeDef:
        """
        [GetJobRuns.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/glue.html#Glue.Paginator.GetJobRuns.paginate)
        """


class GetJobsPaginator(Boto3Paginator):
    """
    [Paginator.GetJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/glue.html#Glue.Paginator.GetJobs)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(self, PaginationConfig: PaginatorConfigTypeDef = None) -> GetJobsResponseTypeDef:
        """
        [GetJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/glue.html#Glue.Paginator.GetJobs.paginate)
        """


class GetPartitionsPaginator(Boto3Paginator):
    """
    [Paginator.GetPartitions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/glue.html#Glue.Paginator.GetPartitions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DatabaseName: str,
        TableName: str,
        CatalogId: str = None,
        Expression: str = None,
        Segment: SegmentTypeDef = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> GetPartitionsResponseTypeDef:
        """
        [GetPartitions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/glue.html#Glue.Paginator.GetPartitions.paginate)
        """


class GetSecurityConfigurationsPaginator(Boto3Paginator):
    """
    [Paginator.GetSecurityConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/glue.html#Glue.Paginator.GetSecurityConfigurations)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> GetSecurityConfigurationsResponseTypeDef:
        """
        [GetSecurityConfigurations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/glue.html#Glue.Paginator.GetSecurityConfigurations.paginate)
        """


class GetTableVersionsPaginator(Boto3Paginator):
    """
    [Paginator.GetTableVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/glue.html#Glue.Paginator.GetTableVersions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DatabaseName: str,
        TableName: str,
        CatalogId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> GetTableVersionsResponseTypeDef:
        """
        [GetTableVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/glue.html#Glue.Paginator.GetTableVersions.paginate)
        """


class GetTablesPaginator(Boto3Paginator):
    """
    [Paginator.GetTables documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/glue.html#Glue.Paginator.GetTables)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DatabaseName: str,
        CatalogId: str = None,
        Expression: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> GetTablesResponseTypeDef:
        """
        [GetTables.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/glue.html#Glue.Paginator.GetTables.paginate)
        """


class GetTriggersPaginator(Boto3Paginator):
    """
    [Paginator.GetTriggers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/glue.html#Glue.Paginator.GetTriggers)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, DependentJobName: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> GetTriggersResponseTypeDef:
        """
        [GetTriggers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/glue.html#Glue.Paginator.GetTriggers.paginate)
        """


class GetUserDefinedFunctionsPaginator(Boto3Paginator):
    """
    [Paginator.GetUserDefinedFunctions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/glue.html#Glue.Paginator.GetUserDefinedFunctions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        DatabaseName: str,
        Pattern: str,
        CatalogId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> GetUserDefinedFunctionsResponseTypeDef:
        """
        [GetUserDefinedFunctions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/glue.html#Glue.Paginator.GetUserDefinedFunctions.paginate)
        """
