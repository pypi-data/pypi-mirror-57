"Main interface for macie service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_macie.type_defs import (
    ListMemberAccountsResultTypeDef,
    ListS3ResourcesResultTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = ("ListMemberAccountsPaginator", "ListS3ResourcesPaginator")


class ListMemberAccountsPaginator(Boto3Paginator):
    """
    [Paginator.ListMemberAccounts documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/macie.html#Macie.Paginator.ListMemberAccounts)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListMemberAccountsResultTypeDef:
        """
        [ListMemberAccounts.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/macie.html#Macie.Paginator.ListMemberAccounts.paginate)
        """


class ListS3ResourcesPaginator(Boto3Paginator):
    """
    [Paginator.ListS3Resources documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/macie.html#Macie.Paginator.ListS3Resources)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, memberAccountId: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListS3ResourcesResultTypeDef:
        """
        [ListS3Resources.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/macie.html#Macie.Paginator.ListS3Resources.paginate)
        """
