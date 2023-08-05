"Main interface for athena service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_athena.type_defs import (
    GetQueryResultsPaginatePaginationConfigTypeDef,
    GetQueryResultsPaginateResponseTypeDef,
    ListNamedQueriesPaginatePaginationConfigTypeDef,
    ListNamedQueriesPaginateResponseTypeDef,
    ListQueryExecutionsPaginatePaginationConfigTypeDef,
    ListQueryExecutionsPaginateResponseTypeDef,
)


__all__ = ("GetQueryResultsPaginator", "ListNamedQueriesPaginator", "ListQueryExecutionsPaginator")


class GetQueryResultsPaginator(Boto3Paginator):
    """
    Paginator for `get_query_results`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        QueryExecutionId: str,
        PaginationConfig: GetQueryResultsPaginatePaginationConfigTypeDef = None,
    ) -> GetQueryResultsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`Athena.Client.get_query_results`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/athena-2017-05-18/GetQueryResults>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              QueryExecutionId='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type QueryExecutionId: string
        :param QueryExecutionId: **[REQUIRED]**

          The unique ID of the query execution.

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than
            the value specified in max-items then a ``NextToken`` will be provided in the output
            that you can use to resume pagination.

          - **PageSize** *(integer) --*

            The size of each page.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'UpdateCount': 123,
                'ResultSet': {
                    'Rows': [
                        {
                            'Data': [
                                {
                                    'VarCharValue': 'string'
                                },
                            ]
                        },
                    ],
                    'ResultSetMetadata': {
                        'ColumnInfo': [
                            {
                                'CatalogName': 'string',
                                'SchemaName': 'string',
                                'TableName': 'string',
                                'Name': 'string',
                                'Label': 'string',
                                'Type': 'string',
                                'Precision': 123,
                                'Scale': 123,
                                'Nullable': 'NOT_NULL'|'NULLABLE'|'UNKNOWN',
                                'CaseSensitive': True|False
                            },
                        ]
                    }
                },

            }
          **Response Structure**

          - *(dict) --*

            - **UpdateCount** *(integer) --*

              The number of rows inserted with a CREATE TABLE AS SELECT statement.

            - **ResultSet** *(dict) --*

              The results of the query execution.

              - **Rows** *(list) --*

                The rows in the table.

                - *(dict) --*

                  The rows that comprise a query result table.

                  - **Data** *(list) --*

                    The data that populates a row in a query result table.

                    - *(dict) --*

                      A piece of data (a field in the table).

                      - **VarCharValue** *(string) --*

                        The value of the datum.

              - **ResultSetMetadata** *(dict) --*

                The metadata that describes the column structure and data types of a table of query
                results.

                - **ColumnInfo** *(list) --*

                  Information about the columns returned in a query result metadata.

                  - *(dict) --*

                    Information about the columns in a query execution result.

                    - **CatalogName** *(string) --*

                      The catalog to which the query results belong.

                    - **SchemaName** *(string) --*

                      The schema name (database name) to which the query results belong.

                    - **TableName** *(string) --*

                      The table name for the query results.

                    - **Name** *(string) --*

                      The name of the column.

                    - **Label** *(string) --*

                      A column label.

                    - **Type** *(string) --*

                      The data type of the column.

                    - **Precision** *(integer) --*

                      For ``DECIMAL`` data types, specifies the total number of digits, up to 38.
                      For performance reasons, we recommend up to 18 digits.

                    - **Scale** *(integer) --*

                      For ``DECIMAL`` data types, specifies the total number of digits in the
                      fractional part of the value. Defaults to 0.

                    - **Nullable** *(string) --*

                      Indicates the column's nullable status.

                    - **CaseSensitive** *(boolean) --*

                      Indicates whether values in the column are case-sensitive.
        """


class ListNamedQueriesPaginator(Boto3Paginator):
    """
    Paginator for `list_named_queries`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        WorkGroup: str = None,
        PaginationConfig: ListNamedQueriesPaginatePaginationConfigTypeDef = None,
    ) -> ListNamedQueriesPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`Athena.Client.list_named_queries`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/athena-2017-05-18/ListNamedQueries>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              WorkGroup='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type WorkGroup: string
        :param WorkGroup:

          The name of the workgroup from which the named queries are being returned.

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than
            the value specified in max-items then a ``NextToken`` will be provided in the output
            that you can use to resume pagination.

          - **PageSize** *(integer) --*

            The size of each page.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'NamedQueryIds': [
                    'string',
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **NamedQueryIds** *(list) --*

              The list of unique query IDs.

              - *(string) --*
        """


class ListQueryExecutionsPaginator(Boto3Paginator):
    """
    Paginator for `list_query_executions`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        WorkGroup: str = None,
        PaginationConfig: ListQueryExecutionsPaginatePaginationConfigTypeDef = None,
    ) -> ListQueryExecutionsPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`Athena.Client.list_query_executions`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/athena-2017-05-18/ListQueryExecutions>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              WorkGroup='string',
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
        :type WorkGroup: string
        :param WorkGroup:

          The name of the workgroup from which queries are being returned.

        :type PaginationConfig: dict
        :param PaginationConfig:

          A dictionary that provides parameters to control pagination.

          - **MaxItems** *(integer) --*

            The total number of items to return. If the total number of items available is more than
            the value specified in max-items then a ``NextToken`` will be provided in the output
            that you can use to resume pagination.

          - **PageSize** *(integer) --*

            The size of each page.

          - **StartingToken** *(string) --*

            A token to specify where to start paginating. This is the ``NextToken`` from a previous
            response.

        :rtype: dict
        :returns:

          **Response Syntax**

          ::

            {
                'QueryExecutionIds': [
                    'string',
                ],

            }
          **Response Structure**

          - *(dict) --*

            - **QueryExecutionIds** *(list) --*

              The unique IDs of each query execution as an array of strings.

              - *(string) --*
        """
