"Main interface for athena service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_athena.type_defs import (
    GetQueryResultsOutputTypeDef,
    ListNamedQueriesOutputTypeDef,
    ListQueryExecutionsOutputTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = ("GetQueryResultsPaginator", "ListNamedQueriesPaginator", "ListQueryExecutionsPaginator")


class GetQueryResultsPaginator(Boto3Paginator):
    """
    [Paginator.GetQueryResults documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/athena.html#Athena.Paginator.GetQueryResults)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, QueryExecutionId: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> GetQueryResultsOutputTypeDef:
        """
        [GetQueryResults.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/athena.html#Athena.Paginator.GetQueryResults.paginate)
        """


class ListNamedQueriesPaginator(Boto3Paginator):
    """
    [Paginator.ListNamedQueries documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/athena.html#Athena.Paginator.ListNamedQueries)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, WorkGroup: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListNamedQueriesOutputTypeDef:
        """
        [ListNamedQueries.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/athena.html#Athena.Paginator.ListNamedQueries.paginate)
        """


class ListQueryExecutionsPaginator(Boto3Paginator):
    """
    [Paginator.ListQueryExecutions documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/athena.html#Athena.Paginator.ListQueryExecutions)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, WorkGroup: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> ListQueryExecutionsOutputTypeDef:
        """
        [ListQueryExecutions.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/athena.html#Athena.Paginator.ListQueryExecutions.paginate)
        """
