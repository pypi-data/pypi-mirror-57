"Main interface for pricing service Paginators"
from __future__ import annotations

from typing import List
from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_pricing.type_defs import (
    DescribeServicesResponseTypeDef,
    FilterTypeDef,
    GetAttributeValuesResponseTypeDef,
    GetProductsResponseTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = ("DescribeServicesPaginator", "GetAttributeValuesPaginator", "GetProductsPaginator")


class DescribeServicesPaginator(Boto3Paginator):
    """
    [Paginator.DescribeServices documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/pricing.html#Pricing.Paginator.DescribeServices)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ServiceCode: str = None,
        FormatVersion: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> DescribeServicesResponseTypeDef:
        """
        [DescribeServices.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/pricing.html#Pricing.Paginator.DescribeServices.paginate)
        """


class GetAttributeValuesPaginator(Boto3Paginator):
    """
    [Paginator.GetAttributeValues documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/pricing.html#Pricing.Paginator.GetAttributeValues)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, ServiceCode: str, AttributeName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> GetAttributeValuesResponseTypeDef:
        """
        [GetAttributeValues.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/pricing.html#Pricing.Paginator.GetAttributeValues.paginate)
        """


class GetProductsPaginator(Boto3Paginator):
    """
    [Paginator.GetProducts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/pricing.html#Pricing.Paginator.GetProducts)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        ServiceCode: str = None,
        Filters: List[FilterTypeDef] = None,
        FormatVersion: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> GetProductsResponseTypeDef:
        """
        [GetProducts.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/pricing.html#Pricing.Paginator.GetProducts.paginate)
        """
