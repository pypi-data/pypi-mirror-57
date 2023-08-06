"Main interface for storagegateway service Paginators"
from __future__ import annotations

from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_storagegateway.type_defs import (
    DescribeTapeArchivesOutputTypeDef,
    DescribeTapeRecoveryPointsOutputTypeDef,
    DescribeTapesOutputTypeDef,
    DescribeVTLDevicesOutputTypeDef,
    ListFileSharesOutputTypeDef,
    ListGatewaysOutputTypeDef,
    ListTagsForResourceOutputTypeDef,
    ListTapesOutputTypeDef,
    ListVolumesOutputTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = (
    "DescribeTapeArchivesPaginator",
    "DescribeTapeRecoveryPointsPaginator",
    "DescribeTapesPaginator",
    "DescribeVTLDevicesPaginator",
    "ListFileSharesPaginator",
    "ListGatewaysPaginator",
    "ListTagsForResourcePaginator",
    "ListTapesPaginator",
    "ListVolumesPaginator",
)


class DescribeTapeArchivesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeTapeArchives documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.35/reference/services/storagegateway.html#StorageGateway.Paginator.DescribeTapeArchives)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, TapeARNs: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> DescribeTapeArchivesOutputTypeDef:
        """
        [DescribeTapeArchives.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.35/reference/services/storagegateway.html#StorageGateway.Paginator.DescribeTapeArchives.paginate)
        """


class DescribeTapeRecoveryPointsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeTapeRecoveryPoints documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.35/reference/services/storagegateway.html#StorageGateway.Paginator.DescribeTapeRecoveryPoints)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, GatewayARN: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> DescribeTapeRecoveryPointsOutputTypeDef:
        """
        [DescribeTapeRecoveryPoints.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.35/reference/services/storagegateway.html#StorageGateway.Paginator.DescribeTapeRecoveryPoints.paginate)
        """


class DescribeTapesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeTapes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.35/reference/services/storagegateway.html#StorageGateway.Paginator.DescribeTapes)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        GatewayARN: str,
        TapeARNs: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> DescribeTapesOutputTypeDef:
        """
        [DescribeTapes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.35/reference/services/storagegateway.html#StorageGateway.Paginator.DescribeTapes.paginate)
        """


class DescribeVTLDevicesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeVTLDevices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.35/reference/services/storagegateway.html#StorageGateway.Paginator.DescribeVTLDevices)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        GatewayARN: str,
        VTLDeviceARNs: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> DescribeVTLDevicesOutputTypeDef:
        """
        [DescribeVTLDevices.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.35/reference/services/storagegateway.html#StorageGateway.Paginator.DescribeVTLDevices.paginate)
        """


class ListFileSharesPaginator(Boto3Paginator):
    """
    [Paginator.ListFileShares documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.35/reference/services/storagegateway.html#StorageGateway.Paginator.ListFileShares)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, GatewayARN: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListFileSharesOutputTypeDef:
        """
        [ListFileShares.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.35/reference/services/storagegateway.html#StorageGateway.Paginator.ListFileShares.paginate)
        """


class ListGatewaysPaginator(Boto3Paginator):
    """
    [Paginator.ListGateways documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.35/reference/services/storagegateway.html#StorageGateway.Paginator.ListGateways)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListGatewaysOutputTypeDef:
        """
        [ListGateways.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.35/reference/services/storagegateway.html#StorageGateway.Paginator.ListGateways.paginate)
        """


class ListTagsForResourcePaginator(Boto3Paginator):
    """
    [Paginator.ListTagsForResource documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.35/reference/services/storagegateway.html#StorageGateway.Paginator.ListTagsForResource)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, ResourceARN: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListTagsForResourceOutputTypeDef:
        """
        [ListTagsForResource.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.35/reference/services/storagegateway.html#StorageGateway.Paginator.ListTagsForResource.paginate)
        """


class ListTapesPaginator(Boto3Paginator):
    """
    [Paginator.ListTapes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.35/reference/services/storagegateway.html#StorageGateway.Paginator.ListTapes)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, TapeARNs: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListTapesOutputTypeDef:
        """
        [ListTapes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.35/reference/services/storagegateway.html#StorageGateway.Paginator.ListTapes.paginate)
        """


class ListVolumesPaginator(Boto3Paginator):
    """
    [Paginator.ListVolumes documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.35/reference/services/storagegateway.html#StorageGateway.Paginator.ListVolumes)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, GatewayARN: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListVolumesOutputTypeDef:
        """
        [ListVolumes.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.35/reference/services/storagegateway.html#StorageGateway.Paginator.ListVolumes.paginate)
        """
