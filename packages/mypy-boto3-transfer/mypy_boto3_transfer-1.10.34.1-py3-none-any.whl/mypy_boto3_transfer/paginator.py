"Main interface for transfer service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_transfer.type_defs import ListServersResponseTypeDef, PaginatorConfigTypeDef


__all__ = ("ListServersPaginator",)


class ListServersPaginator(Boto3Paginator):
    """
    [Paginator.ListServers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/transfer.html#Transfer.Paginator.ListServers)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListServersResponseTypeDef:
        """
        [ListServers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/transfer.html#Transfer.Paginator.ListServers.paginate)
        """
