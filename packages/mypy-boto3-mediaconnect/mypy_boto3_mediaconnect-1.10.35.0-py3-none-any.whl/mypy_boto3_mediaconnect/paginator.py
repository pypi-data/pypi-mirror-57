"Main interface for mediaconnect service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_mediaconnect.type_defs import (
    ListEntitlementsResponseTypeDef,
    ListFlowsResponseTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = ("ListEntitlementsPaginator", "ListFlowsPaginator")


class ListEntitlementsPaginator(Boto3Paginator):
    """
    [Paginator.ListEntitlements documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.35/reference/services/mediaconnect.html#MediaConnect.Paginator.ListEntitlements)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListEntitlementsResponseTypeDef:
        """
        [ListEntitlements.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.35/reference/services/mediaconnect.html#MediaConnect.Paginator.ListEntitlements.paginate)
        """


class ListFlowsPaginator(Boto3Paginator):
    """
    [Paginator.ListFlows documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.35/reference/services/mediaconnect.html#MediaConnect.Paginator.ListFlows)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(self, PaginationConfig: PaginatorConfigTypeDef = None) -> ListFlowsResponseTypeDef:
        """
        [ListFlows.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.35/reference/services/mediaconnect.html#MediaConnect.Paginator.ListFlows.paginate)
        """
