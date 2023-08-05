"Main interface for route53 service Waiters"
from __future__ import annotations

from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_route53.type_defs import ResourceRecordSetsChangedWaitWaiterConfigTypeDef


__all__ = ("ResourceRecordSetsChangedWaiter",)


class ResourceRecordSetsChangedWaiter(Boto3Waiter):
    """
    Waiter for `resource_record_sets_changed` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self, Id: str, WaiterConfig: ResourceRecordSetsChangedWaitWaiterConfigTypeDef = None
    ) -> None:
        """
        Polls :py:meth:`Route53.Client.get_change` every 30 seconds until a successful state is
        reached. An error is returned after 60 failed checks.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/route53-2013-04-01/GetChange>`_

        **Request Syntax**
        ::

          waiter.wait(
              Id='string',
              WaiterConfig={
                  'Delay': 123,
                  'MaxAttempts': 123
              }
          )
        :type Id: string
        :param Id: **[REQUIRED]**

          The ID of the change batch request. The value that you specify here is the value that
          ``ChangeResourceRecordSets`` returned in the ``Id`` element when you submitted the
          request.

        :type WaiterConfig: dict
        :param WaiterConfig:

          A dictionary that provides parameters to control waiting behavior.

          - **Delay** *(integer) --*

            The amount of time in seconds to wait between attempts. Default: 30

          - **MaxAttempts** *(integer) --*

            The maximum number of attempts to be made. Default: 60

        :returns: None
        """
