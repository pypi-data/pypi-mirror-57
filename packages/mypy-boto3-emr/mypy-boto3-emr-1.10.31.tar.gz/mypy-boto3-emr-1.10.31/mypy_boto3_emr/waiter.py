"Main interface for emr service Waiters"
from __future__ import annotations

from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_emr.type_defs import (
    ClusterRunningWaitWaiterConfigTypeDef,
    ClusterTerminatedWaitWaiterConfigTypeDef,
    StepCompleteWaitWaiterConfigTypeDef,
)


__all__ = ("ClusterRunningWaiter", "ClusterTerminatedWaiter", "StepCompleteWaiter")


class ClusterRunningWaiter(Boto3Waiter):
    """
    Waiter for `cluster_running` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self, ClusterId: str, WaiterConfig: ClusterRunningWaitWaiterConfigTypeDef = None
    ) -> None:
        """
        Polls :py:meth:`EMR.Client.describe_cluster` every 30 seconds until a successful state is
        reached. An error is returned after 60 failed checks.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticmapreduce-2009-03-31/DescribeCluster>`_

        **Request Syntax**
        ::

          waiter.wait(
              ClusterId='string',
              WaiterConfig={
                  'Delay': 123,
                  'MaxAttempts': 123
              }
          )
        :type ClusterId: string
        :param ClusterId: **[REQUIRED]**

          The identifier of the cluster to describe.

        :type WaiterConfig: dict
        :param WaiterConfig:

          A dictionary that provides parameters to control waiting behavior.

          - **Delay** *(integer) --*

            The amount of time in seconds to wait between attempts. Default: 30

          - **MaxAttempts** *(integer) --*

            The maximum number of attempts to be made. Default: 60

        :returns: None
        """


class ClusterTerminatedWaiter(Boto3Waiter):
    """
    Waiter for `cluster_terminated` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self, ClusterId: str, WaiterConfig: ClusterTerminatedWaitWaiterConfigTypeDef = None
    ) -> None:
        """
        Polls :py:meth:`EMR.Client.describe_cluster` every 30 seconds until a successful state is
        reached. An error is returned after 60 failed checks.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticmapreduce-2009-03-31/DescribeCluster>`_

        **Request Syntax**
        ::

          waiter.wait(
              ClusterId='string',
              WaiterConfig={
                  'Delay': 123,
                  'MaxAttempts': 123
              }
          )
        :type ClusterId: string
        :param ClusterId: **[REQUIRED]**

          The identifier of the cluster to describe.

        :type WaiterConfig: dict
        :param WaiterConfig:

          A dictionary that provides parameters to control waiting behavior.

          - **Delay** *(integer) --*

            The amount of time in seconds to wait between attempts. Default: 30

          - **MaxAttempts** *(integer) --*

            The maximum number of attempts to be made. Default: 60

        :returns: None
        """


class StepCompleteWaiter(Boto3Waiter):
    """
    Waiter for `step_complete` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self, ClusterId: str, StepId: str, WaiterConfig: StepCompleteWaitWaiterConfigTypeDef = None
    ) -> None:
        """
        Polls :py:meth:`EMR.Client.describe_step` every 30 seconds until a successful state is
        reached. An error is returned after 60 failed checks.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/elasticmapreduce-2009-03-31/DescribeStep>`_

        **Request Syntax**
        ::

          waiter.wait(
              ClusterId='string',
              StepId='string',
              WaiterConfig={
                  'Delay': 123,
                  'MaxAttempts': 123
              }
          )
        :type ClusterId: string
        :param ClusterId: **[REQUIRED]**

          The identifier of the cluster with steps to describe.

        :type StepId: string
        :param StepId: **[REQUIRED]**

          The identifier of the step to describe.

        :type WaiterConfig: dict
        :param WaiterConfig:

          A dictionary that provides parameters to control waiting behavior.

          - **Delay** *(integer) --*

            The amount of time in seconds to wait between attempts. Default: 30

          - **MaxAttempts** *(integer) --*

            The maximum number of attempts to be made. Default: 60

        :returns: None
        """
