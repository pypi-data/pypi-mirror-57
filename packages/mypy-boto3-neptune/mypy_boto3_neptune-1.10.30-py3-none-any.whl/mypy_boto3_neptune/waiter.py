"Main interface for neptune service Waiters"
from __future__ import annotations

from typing import List
from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_neptune.type_defs import (
    DbInstanceAvailableWaitFiltersTypeDef,
    DbInstanceAvailableWaitWaiterConfigTypeDef,
    DbInstanceDeletedWaitFiltersTypeDef,
    DbInstanceDeletedWaitWaiterConfigTypeDef,
)


__all__ = ("DBInstanceAvailableWaiter", "DBInstanceDeletedWaiter")


class DBInstanceAvailableWaiter(Boto3Waiter):
    """
    Waiter for `db_instance_available` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        DBInstanceIdentifier: str = None,
        Filters: List[DbInstanceAvailableWaitFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        WaiterConfig: DbInstanceAvailableWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        Polls :py:meth:`Neptune.Client.describe_db_instances` every 30 seconds until a successful
        state is reached. An error is returned after 60 failed checks.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/DescribeDBInstances>`_

        **Request Syntax**
        ::

          waiter.wait(
              DBInstanceIdentifier='string',
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              MaxRecords=123,
              Marker='string',
              WaiterConfig={
                  'Delay': 123,
                  'MaxAttempts': 123
              }
          )
        :type DBInstanceIdentifier: string
        :param DBInstanceIdentifier:

          The user-supplied instance identifier. If this parameter is specified, information from
          only the specific DB instance is returned. This parameter isn't case-sensitive.

          Constraints:

          * If supplied, must match the identifier of an existing DBInstance.

        :type Filters: list
        :param Filters:

          A filter that specifies one or more DB instances to describe.

          Supported filters:

          * ``db-cluster-id`` - Accepts DB cluster identifiers and DB cluster Amazon Resource Names
          (ARNs). The results list will only include information about the DB instances associated
          with the DB clusters identified by these ARNs.

          * ``db-instance-id`` - Accepts DB instance identifiers and DB instance Amazon Resource
          Names (ARNs). The results list will only include information about the DB instances
          identified by these ARNs.

          - *(dict) --*

            This type is not currently supported.

            - **Name** *(string) --* **[REQUIRED]**

              This parameter is not currently supported.

            - **Values** *(list) --* **[REQUIRED]**

              This parameter is not currently supported.

              - *(string) --*

        :type MaxRecords: integer
        :param MaxRecords:

          The maximum number of records to include in the response. If more records exist than the
          specified ``MaxRecords`` value, a pagination token called a marker is included in the
          response so that the remaining results can be retrieved.

          Default: 100

          Constraints: Minimum 20, maximum 100.

        :type Marker: string
        :param Marker:

          An optional pagination token provided by a previous ``DescribeDBInstances`` request. If
          this parameter is specified, the response includes only records beyond the marker, up to
          the value specified by ``MaxRecords`` .

        :type WaiterConfig: dict
        :param WaiterConfig:

          A dictionary that provides parameters to control waiting behavior.

          - **Delay** *(integer) --*

            The amount of time in seconds to wait between attempts. Default: 30

          - **MaxAttempts** *(integer) --*

            The maximum number of attempts to be made. Default: 60

        :returns: None
        """


class DBInstanceDeletedWaiter(Boto3Waiter):
    """
    Waiter for `db_instance_deleted` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        DBInstanceIdentifier: str = None,
        Filters: List[DbInstanceDeletedWaitFiltersTypeDef] = None,
        MaxRecords: int = None,
        Marker: str = None,
        WaiterConfig: DbInstanceDeletedWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        Polls :py:meth:`Neptune.Client.describe_db_instances` every 30 seconds until a successful
        state is reached. An error is returned after 60 failed checks.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/neptune-2014-10-31/DescribeDBInstances>`_

        **Request Syntax**
        ::

          waiter.wait(
              DBInstanceIdentifier='string',
              Filters=[
                  {
                      'Name': 'string',
                      'Values': [
                          'string',
                      ]
                  },
              ],
              MaxRecords=123,
              Marker='string',
              WaiterConfig={
                  'Delay': 123,
                  'MaxAttempts': 123
              }
          )
        :type DBInstanceIdentifier: string
        :param DBInstanceIdentifier:

          The user-supplied instance identifier. If this parameter is specified, information from
          only the specific DB instance is returned. This parameter isn't case-sensitive.

          Constraints:

          * If supplied, must match the identifier of an existing DBInstance.

        :type Filters: list
        :param Filters:

          A filter that specifies one or more DB instances to describe.

          Supported filters:

          * ``db-cluster-id`` - Accepts DB cluster identifiers and DB cluster Amazon Resource Names
          (ARNs). The results list will only include information about the DB instances associated
          with the DB clusters identified by these ARNs.

          * ``db-instance-id`` - Accepts DB instance identifiers and DB instance Amazon Resource
          Names (ARNs). The results list will only include information about the DB instances
          identified by these ARNs.

          - *(dict) --*

            This type is not currently supported.

            - **Name** *(string) --* **[REQUIRED]**

              This parameter is not currently supported.

            - **Values** *(list) --* **[REQUIRED]**

              This parameter is not currently supported.

              - *(string) --*

        :type MaxRecords: integer
        :param MaxRecords:

          The maximum number of records to include in the response. If more records exist than the
          specified ``MaxRecords`` value, a pagination token called a marker is included in the
          response so that the remaining results can be retrieved.

          Default: 100

          Constraints: Minimum 20, maximum 100.

        :type Marker: string
        :param Marker:

          An optional pagination token provided by a previous ``DescribeDBInstances`` request. If
          this parameter is specified, the response includes only records beyond the marker, up to
          the value specified by ``MaxRecords`` .

        :type WaiterConfig: dict
        :param WaiterConfig:

          A dictionary that provides parameters to control waiting behavior.

          - **Delay** *(integer) --*

            The amount of time in seconds to wait between attempts. Default: 30

          - **MaxAttempts** *(integer) --*

            The maximum number of attempts to be made. Default: 60

        :returns: None
        """
