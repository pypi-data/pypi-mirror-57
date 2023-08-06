"Main interface for es service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_es.type_defs import (
    DescribeReservedElasticsearchInstanceOfferingsResponseTypeDef,
    DescribeReservedElasticsearchInstancesResponseTypeDef,
    GetUpgradeHistoryResponseTypeDef,
    ListElasticsearchInstanceTypesResponseTypeDef,
    ListElasticsearchVersionsResponseTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = (
    "DescribeReservedElasticsearchInstanceOfferingsPaginator",
    "DescribeReservedElasticsearchInstancesPaginator",
    "GetUpgradeHistoryPaginator",
    "ListElasticsearchInstanceTypesPaginator",
    "ListElasticsearchVersionsPaginator",
)


class DescribeReservedElasticsearchInstanceOfferingsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeReservedElasticsearchInstanceOfferings documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/es.html#ElasticsearchService.Paginator.DescribeReservedElasticsearchInstanceOfferings)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ReservedElasticsearchInstanceOfferingId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> DescribeReservedElasticsearchInstanceOfferingsResponseTypeDef:
        """
        [DescribeReservedElasticsearchInstanceOfferings.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/es.html#ElasticsearchService.Paginator.DescribeReservedElasticsearchInstanceOfferings.paginate)
        """


class DescribeReservedElasticsearchInstancesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeReservedElasticsearchInstances documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/es.html#ElasticsearchService.Paginator.DescribeReservedElasticsearchInstances)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ReservedElasticsearchInstanceId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> DescribeReservedElasticsearchInstancesResponseTypeDef:
        """
        [DescribeReservedElasticsearchInstances.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/es.html#ElasticsearchService.Paginator.DescribeReservedElasticsearchInstances.paginate)
        """


class GetUpgradeHistoryPaginator(Boto3Paginator):
    """
    [Paginator.GetUpgradeHistory documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/es.html#ElasticsearchService.Paginator.GetUpgradeHistory)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, DomainName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> GetUpgradeHistoryResponseTypeDef:
        """
        [GetUpgradeHistory.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/es.html#ElasticsearchService.Paginator.GetUpgradeHistory.paginate)
        """


class ListElasticsearchInstanceTypesPaginator(Boto3Paginator):
    """
    [Paginator.ListElasticsearchInstanceTypes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/es.html#ElasticsearchService.Paginator.ListElasticsearchInstanceTypes)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ElasticsearchVersion: str,
        DomainName: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> ListElasticsearchInstanceTypesResponseTypeDef:
        """
        [ListElasticsearchInstanceTypes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/es.html#ElasticsearchService.Paginator.ListElasticsearchInstanceTypes.paginate)
        """


class ListElasticsearchVersionsPaginator(Boto3Paginator):
    """
    [Paginator.ListElasticsearchVersions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/es.html#ElasticsearchService.Paginator.ListElasticsearchVersions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListElasticsearchVersionsResponseTypeDef:
        """
        [ListElasticsearchVersions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/es.html#ElasticsearchService.Paginator.ListElasticsearchVersions.paginate)
        """
