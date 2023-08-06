"Main interface for forecast service Paginators"
from __future__ import annotations

from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_forecast.type_defs import (
    FilterTypeDef,
    ListDatasetGroupsResponseTypeDef,
    ListDatasetImportJobsResponseTypeDef,
    ListDatasetsResponseTypeDef,
    ListForecastExportJobsResponseTypeDef,
    ListForecastsResponseTypeDef,
    ListPredictorsResponseTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = (
    "ListDatasetGroupsPaginator",
    "ListDatasetImportJobsPaginator",
    "ListDatasetsPaginator",
    "ListForecastExportJobsPaginator",
    "ListForecastsPaginator",
    "ListPredictorsPaginator",
)


class ListDatasetGroupsPaginator(Boto3Paginator):
    """
    [Paginator.ListDatasetGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/forecast.html#ForecastService.Paginator.ListDatasetGroups)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListDatasetGroupsResponseTypeDef:
        """
        [ListDatasetGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/forecast.html#ForecastService.Paginator.ListDatasetGroups.paginate)
        """


class ListDatasetImportJobsPaginator(Boto3Paginator):
    """
    [Paginator.ListDatasetImportJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/forecast.html#ForecastService.Paginator.ListDatasetImportJobs)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, Filters: List[FilterTypeDef] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListDatasetImportJobsResponseTypeDef:
        """
        [ListDatasetImportJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/forecast.html#ForecastService.Paginator.ListDatasetImportJobs.paginate)
        """


class ListDatasetsPaginator(Boto3Paginator):
    """
    [Paginator.ListDatasets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/forecast.html#ForecastService.Paginator.ListDatasets)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListDatasetsResponseTypeDef:
        """
        [ListDatasets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/forecast.html#ForecastService.Paginator.ListDatasets.paginate)
        """


class ListForecastExportJobsPaginator(Boto3Paginator):
    """
    [Paginator.ListForecastExportJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/forecast.html#ForecastService.Paginator.ListForecastExportJobs)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, Filters: List[FilterTypeDef] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListForecastExportJobsResponseTypeDef:
        """
        [ListForecastExportJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/forecast.html#ForecastService.Paginator.ListForecastExportJobs.paginate)
        """


class ListForecastsPaginator(Boto3Paginator):
    """
    [Paginator.ListForecasts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/forecast.html#ForecastService.Paginator.ListForecasts)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, Filters: List[FilterTypeDef] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListForecastsResponseTypeDef:
        """
        [ListForecasts.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/forecast.html#ForecastService.Paginator.ListForecasts.paginate)
        """


class ListPredictorsPaginator(Boto3Paginator):
    """
    [Paginator.ListPredictors documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/forecast.html#ForecastService.Paginator.ListPredictors)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, Filters: List[FilterTypeDef] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListPredictorsResponseTypeDef:
        """
        [ListPredictors.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/forecast.html#ForecastService.Paginator.ListPredictors.paginate)
        """
