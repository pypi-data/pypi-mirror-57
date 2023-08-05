"Main interface for transfer service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_transfer.type_defs import (
    ListServersPaginatePaginationConfigTypeDef,
    ListServersPaginateResponseTypeDef,
)


__all__ = ("ListServersPaginator",)


class ListServersPaginator(Boto3Paginator):
    """
    Paginator for `list_servers`
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, PaginationConfig: ListServersPaginatePaginationConfigTypeDef = None
    ) -> ListServersPaginateResponseTypeDef:
        """
        Creates an iterator that will paginate through responses from
        :py:meth:`Transfer.Client.list_servers`.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/transfer-2018-11-05/ListServers>`_

        **Request Syntax**
        ::

          response_iterator = paginator.paginate(
              PaginationConfig={
                  'MaxItems': 123,
                  'PageSize': 123,
                  'StartingToken': 'string'
              }
          )
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
                'Servers': [
                    {
                        'Arn': 'string',
                        'IdentityProviderType': 'SERVICE_MANAGED'|'API_GATEWAY',
                        'EndpointType': 'PUBLIC'|'VPC_ENDPOINT',
                        'LoggingRole': 'string',
                        'ServerId': 'string',
                        'State':
                        'OFFLINE'|'ONLINE'|'STARTING'|'STOPPING'|'START_FAILED'
                        |'STOP_FAILED',
                        'UserCount': 123
                    },
                ]
            }
          **Response Structure**

          - *(dict) --*

            - **Servers** *(list) --*

              An array of servers that were listed.

              - *(dict) --*

                Returns properties of the server that was specified.

                - **Arn** *(string) --*

                  The unique Amazon Resource Name (ARN) for the server to be listed.

                - **IdentityProviderType** *(string) --*

                  The authentication method used to validate a user for the server that was
                  specified. This can include Secure Shell (SSH), user name and password
                  combinations, or your own custom authentication method. Valid values include
                  ``SERVICE_MANAGED`` or ``API_GATEWAY`` .

                - **EndpointType** *(string) --*

                  The type of VPC endpoint that your SFTP server is connected to. If your SFTP
                  server is connected to a VPC endpoint, your server isn't accessible over the
                  public internet.

                - **LoggingRole** *(string) --*

                  The AWS Identity and Access Management entity that allows the server to turn on
                  Amazon CloudWatch logging.

                - **ServerId** *(string) --*

                  This value is the unique system assigned identifier for the SFTP servers that were
                  listed.

                - **State** *(string) --*

                  This property describes the condition of the SFTP server for the server that was
                  described. A value of ``ONLINE`` > indicates that the server can accept jobs and
                  transfer files. A ``State`` value of ``OFFLINE`` means that the server cannot
                  perform file transfer operations.

                  The states of ``STARTING`` and ``STOPPING`` indicate that the server is in an
                  intermediate state, either not fully able to respond, or not fully offline. The
                  values of ``START_FAILED`` or ``STOP_FAILED`` can indicate an error condition.

                - **UserCount** *(integer) --*

                  This property is a numeric value that indicates the number of users that are
                  assigned to the SFTP server you specified with the ``ServerId`` .
        """
