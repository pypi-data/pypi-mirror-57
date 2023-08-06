"Main interface for cloudhsm service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_cloudhsm.type_defs import (
    ListHapgsResponseTypeDef,
    ListHsmsResponseTypeDef,
    ListLunaClientsResponseTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = ("ListHapgsPaginator", "ListHsmsPaginator", "ListLunaClientsPaginator")


class ListHapgsPaginator(Boto3Paginator):
    """
    [Paginator.ListHapgs documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cloudhsm.html#CloudHSM.Paginator.ListHapgs)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(self, PaginationConfig: PaginatorConfigTypeDef = None) -> ListHapgsResponseTypeDef:
        """
        [ListHapgs.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cloudhsm.html#CloudHSM.Paginator.ListHapgs.paginate)
        """


class ListHsmsPaginator(Boto3Paginator):
    """
    [Paginator.ListHsms documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cloudhsm.html#CloudHSM.Paginator.ListHsms)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(self, PaginationConfig: PaginatorConfigTypeDef = None) -> ListHsmsResponseTypeDef:
        """
        [ListHsms.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cloudhsm.html#CloudHSM.Paginator.ListHsms.paginate)
        """


class ListLunaClientsPaginator(Boto3Paginator):
    """
    [Paginator.ListLunaClients documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cloudhsm.html#CloudHSM.Paginator.ListLunaClients)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListLunaClientsResponseTypeDef:
        """
        [ListLunaClients.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/cloudhsm.html#CloudHSM.Paginator.ListLunaClients.paginate)
        """
