"Main interface for route53 service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_route53.type_defs import (
    ListHealthChecksResponseTypeDef,
    ListHostedZonesResponseTypeDef,
    ListQueryLoggingConfigsResponseTypeDef,
    ListResourceRecordSetsResponseTypeDef,
    ListVPCAssociationAuthorizationsResponseTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = (
    "ListHealthChecksPaginator",
    "ListHostedZonesPaginator",
    "ListQueryLoggingConfigsPaginator",
    "ListResourceRecordSetsPaginator",
    "ListVPCAssociationAuthorizationsPaginator",
)


class ListHealthChecksPaginator(Boto3Paginator):
    """
    [Paginator.ListHealthChecks documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/route53.html#Route53.Paginator.ListHealthChecks)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListHealthChecksResponseTypeDef:
        """
        [ListHealthChecks.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/route53.html#Route53.Paginator.ListHealthChecks.paginate)
        """


class ListHostedZonesPaginator(Boto3Paginator):
    """
    [Paginator.ListHostedZones documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/route53.html#Route53.Paginator.ListHostedZones)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, DelegationSetId: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListHostedZonesResponseTypeDef:
        """
        [ListHostedZones.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/route53.html#Route53.Paginator.ListHostedZones.paginate)
        """


class ListQueryLoggingConfigsPaginator(Boto3Paginator):
    """
    [Paginator.ListQueryLoggingConfigs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/route53.html#Route53.Paginator.ListQueryLoggingConfigs)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, HostedZoneId: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListQueryLoggingConfigsResponseTypeDef:
        """
        [ListQueryLoggingConfigs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/route53.html#Route53.Paginator.ListQueryLoggingConfigs.paginate)
        """


class ListResourceRecordSetsPaginator(Boto3Paginator):
    """
    [Paginator.ListResourceRecordSets documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/route53.html#Route53.Paginator.ListResourceRecordSets)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, HostedZoneId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListResourceRecordSetsResponseTypeDef:
        """
        [ListResourceRecordSets.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/route53.html#Route53.Paginator.ListResourceRecordSets.paginate)
        """


class ListVPCAssociationAuthorizationsPaginator(Boto3Paginator):
    """
    [Paginator.ListVPCAssociationAuthorizations documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/route53.html#Route53.Paginator.ListVPCAssociationAuthorizations)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        HostedZoneId: str,
        MaxResults: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> ListVPCAssociationAuthorizationsResponseTypeDef:
        """
        [ListVPCAssociationAuthorizations.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/route53.html#Route53.Paginator.ListVPCAssociationAuthorizations.paginate)
        """
