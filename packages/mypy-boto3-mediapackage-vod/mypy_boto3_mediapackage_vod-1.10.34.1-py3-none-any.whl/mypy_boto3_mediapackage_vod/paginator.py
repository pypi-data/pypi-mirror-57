"Main interface for mediapackage-vod service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_mediapackage_vod.type_defs import (
    ListAssetsResponseTypeDef,
    ListPackagingConfigurationsResponseTypeDef,
    ListPackagingGroupsResponseTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = (
    "ListAssetsPaginator",
    "ListPackagingConfigurationsPaginator",
    "ListPackagingGroupsPaginator",
)


class ListAssetsPaginator(Boto3Paginator):
    """
    [Paginator.ListAssets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/mediapackage-vod.html#MediaPackageVod.Paginator.ListAssets)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PackagingGroupId: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListAssetsResponseTypeDef:
        """
        [ListAssets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/mediapackage-vod.html#MediaPackageVod.Paginator.ListAssets.paginate)
        """


class ListPackagingConfigurationsPaginator(Boto3Paginator):
    """
    [Paginator.ListPackagingConfigurations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/mediapackage-vod.html#MediaPackageVod.Paginator.ListPackagingConfigurations)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PackagingGroupId: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListPackagingConfigurationsResponseTypeDef:
        """
        [ListPackagingConfigurations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/mediapackage-vod.html#MediaPackageVod.Paginator.ListPackagingConfigurations.paginate)
        """


class ListPackagingGroupsPaginator(Boto3Paginator):
    """
    [Paginator.ListPackagingGroups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/mediapackage-vod.html#MediaPackageVod.Paginator.ListPackagingGroups)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListPackagingGroupsResponseTypeDef:
        """
        [ListPackagingGroups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/mediapackage-vod.html#MediaPackageVod.Paginator.ListPackagingGroups.paginate)
        """
