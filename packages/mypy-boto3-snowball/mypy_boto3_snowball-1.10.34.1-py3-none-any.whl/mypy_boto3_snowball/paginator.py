"Main interface for snowball service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_snowball.type_defs import (
    DescribeAddressesResultTypeDef,
    ListClusterJobsResultTypeDef,
    ListClustersResultTypeDef,
    ListCompatibleImagesResultTypeDef,
    ListJobsResultTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = (
    "DescribeAddressesPaginator",
    "ListClusterJobsPaginator",
    "ListClustersPaginator",
    "ListCompatibleImagesPaginator",
    "ListJobsPaginator",
)


class DescribeAddressesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeAddresses documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/snowball.html#Snowball.Paginator.DescribeAddresses)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> DescribeAddressesResultTypeDef:
        """
        [DescribeAddresses.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/snowball.html#Snowball.Paginator.DescribeAddresses.paginate)
        """


class ListClusterJobsPaginator(Boto3Paginator):
    """
    [Paginator.ListClusterJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/snowball.html#Snowball.Paginator.ListClusterJobs)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, ClusterId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListClusterJobsResultTypeDef:
        """
        [ListClusterJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/snowball.html#Snowball.Paginator.ListClusterJobs.paginate)
        """


class ListClustersPaginator(Boto3Paginator):
    """
    [Paginator.ListClusters documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/snowball.html#Snowball.Paginator.ListClusters)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListClustersResultTypeDef:
        """
        [ListClusters.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/snowball.html#Snowball.Paginator.ListClusters.paginate)
        """


class ListCompatibleImagesPaginator(Boto3Paginator):
    """
    [Paginator.ListCompatibleImages documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/snowball.html#Snowball.Paginator.ListCompatibleImages)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListCompatibleImagesResultTypeDef:
        """
        [ListCompatibleImages.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/snowball.html#Snowball.Paginator.ListCompatibleImages.paginate)
        """


class ListJobsPaginator(Boto3Paginator):
    """
    [Paginator.ListJobs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/snowball.html#Snowball.Paginator.ListJobs)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(self, PaginationConfig: PaginatorConfigTypeDef = None) -> ListJobsResultTypeDef:
        """
        [ListJobs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/snowball.html#Snowball.Paginator.ListJobs.paginate)
        """
