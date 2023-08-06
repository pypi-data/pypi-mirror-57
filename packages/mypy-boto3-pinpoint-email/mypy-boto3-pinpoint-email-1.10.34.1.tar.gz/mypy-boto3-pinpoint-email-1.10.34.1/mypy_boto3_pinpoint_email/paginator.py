"Main interface for pinpoint-email service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_pinpoint_email.type_defs import (
    GetDedicatedIpsResponseTypeDef,
    ListConfigurationSetsResponseTypeDef,
    ListDedicatedIpPoolsResponseTypeDef,
    ListDeliverabilityTestReportsResponseTypeDef,
    ListEmailIdentitiesResponseTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = (
    "GetDedicatedIpsPaginator",
    "ListConfigurationSetsPaginator",
    "ListDedicatedIpPoolsPaginator",
    "ListDeliverabilityTestReportsPaginator",
    "ListEmailIdentitiesPaginator",
)


class GetDedicatedIpsPaginator(Boto3Paginator):
    """
    [Paginator.GetDedicatedIps documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/pinpoint-email.html#PinpointEmail.Paginator.GetDedicatedIps)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PoolName: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> GetDedicatedIpsResponseTypeDef:
        """
        [GetDedicatedIps.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/pinpoint-email.html#PinpointEmail.Paginator.GetDedicatedIps.paginate)
        """


class ListConfigurationSetsPaginator(Boto3Paginator):
    """
    [Paginator.ListConfigurationSets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/pinpoint-email.html#PinpointEmail.Paginator.ListConfigurationSets)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListConfigurationSetsResponseTypeDef:
        """
        [ListConfigurationSets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/pinpoint-email.html#PinpointEmail.Paginator.ListConfigurationSets.paginate)
        """


class ListDedicatedIpPoolsPaginator(Boto3Paginator):
    """
    [Paginator.ListDedicatedIpPools documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/pinpoint-email.html#PinpointEmail.Paginator.ListDedicatedIpPools)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListDedicatedIpPoolsResponseTypeDef:
        """
        [ListDedicatedIpPools.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/pinpoint-email.html#PinpointEmail.Paginator.ListDedicatedIpPools.paginate)
        """


class ListDeliverabilityTestReportsPaginator(Boto3Paginator):
    """
    [Paginator.ListDeliverabilityTestReports documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/pinpoint-email.html#PinpointEmail.Paginator.ListDeliverabilityTestReports)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListDeliverabilityTestReportsResponseTypeDef:
        """
        [ListDeliverabilityTestReports.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/pinpoint-email.html#PinpointEmail.Paginator.ListDeliverabilityTestReports.paginate)
        """


class ListEmailIdentitiesPaginator(Boto3Paginator):
    """
    [Paginator.ListEmailIdentities documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/pinpoint-email.html#PinpointEmail.Paginator.ListEmailIdentities)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListEmailIdentitiesResponseTypeDef:
        """
        [ListEmailIdentities.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/pinpoint-email.html#PinpointEmail.Paginator.ListEmailIdentities.paginate)
        """
