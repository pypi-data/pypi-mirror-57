"Main interface for opsworkscm service Paginators"
from __future__ import annotations

from botocore.paginate import Paginator as Boto3Paginator
from mypy_boto3_opsworkscm.type_defs import (
    DescribeBackupsResponseTypeDef,
    DescribeEventsResponseTypeDef,
    DescribeServersResponseTypeDef,
    PaginatorConfigTypeDef,
)


__all__ = ("DescribeBackupsPaginator", "DescribeEventsPaginator", "DescribeServersPaginator")


class DescribeBackupsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeBackups documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/opsworkscm.html#OpsWorksCM.Paginator.DescribeBackups)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self,
        BackupId: str = None,
        ServerName: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None,
    ) -> DescribeBackupsResponseTypeDef:
        """
        [DescribeBackups.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/opsworkscm.html#OpsWorksCM.Paginator.DescribeBackups.paginate)
        """


class DescribeEventsPaginator(Boto3Paginator):
    """
    [Paginator.DescribeEvents documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/opsworkscm.html#OpsWorksCM.Paginator.DescribeEvents)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, ServerName: str, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> DescribeEventsResponseTypeDef:
        """
        [DescribeEvents.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/opsworkscm.html#OpsWorksCM.Paginator.DescribeEvents.paginate)
        """


class DescribeServersPaginator(Boto3Paginator):
    """
    [Paginator.DescribeServers documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/opsworkscm.html#OpsWorksCM.Paginator.DescribeServers)
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def paginate(
        self, ServerName: str = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> DescribeServersResponseTypeDef:
        """
        [DescribeServers.paginate documentation](https://boto3.amazonaws.com/v1/documentation/api/1.10.34/reference/services/opsworkscm.html#OpsWorksCM.Paginator.DescribeServers.paginate)
        """
