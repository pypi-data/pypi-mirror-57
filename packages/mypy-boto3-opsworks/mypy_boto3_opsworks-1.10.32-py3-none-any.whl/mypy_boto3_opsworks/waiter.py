"Main interface for opsworks service Waiters"
from __future__ import annotations

from typing import List
from botocore.waiter import Waiter as Boto3Waiter
from mypy_boto3_opsworks.type_defs import (
    AppExistsWaitWaiterConfigTypeDef,
    DeploymentSuccessfulWaitWaiterConfigTypeDef,
    InstanceOnlineWaitWaiterConfigTypeDef,
    InstanceRegisteredWaitWaiterConfigTypeDef,
    InstanceStoppedWaitWaiterConfigTypeDef,
    InstanceTerminatedWaitWaiterConfigTypeDef,
)


__all__ = (
    "AppExistsWaiter",
    "DeploymentSuccessfulWaiter",
    "InstanceOnlineWaiter",
    "InstanceRegisteredWaiter",
    "InstanceStoppedWaiter",
    "InstanceTerminatedWaiter",
)


class AppExistsWaiter(Boto3Waiter):
    """
    Waiter for `app_exists` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        StackId: str = None,
        AppIds: List[str] = None,
        WaiterConfig: AppExistsWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        Polls :py:meth:`OpsWorks.Client.describe_apps` every 1 seconds until a successful state is
        reached. An error is returned after 40 failed checks.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/DescribeApps>`_

        **Request Syntax**
        ::

          waiter.wait(
              StackId='string',
              AppIds=[
                  'string',
              ],
              WaiterConfig={
                  'Delay': 123,
                  'MaxAttempts': 123
              }
          )
        :type StackId: string
        :param StackId:

          The app stack ID. If you use this parameter, ``DescribeApps`` returns a description of the
          apps in the specified stack.

        :type AppIds: list
        :param AppIds:

          An array of app IDs for the apps to be described. If you use this parameter,
          ``DescribeApps`` returns a description of the specified apps. Otherwise, it returns a
          description of every app.

          - *(string) --*

        :type WaiterConfig: dict
        :param WaiterConfig:

          A dictionary that provides parameters to control waiting behavior.

          - **Delay** *(integer) --*

            The amount of time in seconds to wait between attempts. Default: 1

          - **MaxAttempts** *(integer) --*

            The maximum number of attempts to be made. Default: 40

        :returns: None
        """


class DeploymentSuccessfulWaiter(Boto3Waiter):
    """
    Waiter for `deployment_successful` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        StackId: str = None,
        AppId: str = None,
        DeploymentIds: List[str] = None,
        WaiterConfig: DeploymentSuccessfulWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        Polls :py:meth:`OpsWorks.Client.describe_deployments` every 15 seconds until a successful
        state is reached. An error is returned after 40 failed checks.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/DescribeDeployments>`_

        **Request Syntax**
        ::

          waiter.wait(
              StackId='string',
              AppId='string',
              DeploymentIds=[
                  'string',
              ],
              WaiterConfig={
                  'Delay': 123,
                  'MaxAttempts': 123
              }
          )
        :type StackId: string
        :param StackId:

          The stack ID. If you include this parameter, the command returns a description of the
          commands associated with the specified stack.

        :type AppId: string
        :param AppId:

          The app ID. If you include this parameter, the command returns a description of the
          commands associated with the specified app.

        :type DeploymentIds: list
        :param DeploymentIds:

          An array of deployment IDs to be described. If you include this parameter, the command
          returns a description of the specified deployments. Otherwise, it returns a description of
          every deployment.

          - *(string) --*

        :type WaiterConfig: dict
        :param WaiterConfig:

          A dictionary that provides parameters to control waiting behavior.

          - **Delay** *(integer) --*

            The amount of time in seconds to wait between attempts. Default: 15

          - **MaxAttempts** *(integer) --*

            The maximum number of attempts to be made. Default: 40

        :returns: None
        """


class InstanceOnlineWaiter(Boto3Waiter):
    """
    Waiter for `instance_online` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        StackId: str = None,
        LayerId: str = None,
        InstanceIds: List[str] = None,
        WaiterConfig: InstanceOnlineWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        Polls :py:meth:`OpsWorks.Client.describe_instances` every 15 seconds until a successful
        state is reached. An error is returned after 40 failed checks.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/DescribeInstances>`_

        **Request Syntax**
        ::

          waiter.wait(
              StackId='string',
              LayerId='string',
              InstanceIds=[
                  'string',
              ],
              WaiterConfig={
                  'Delay': 123,
                  'MaxAttempts': 123
              }
          )
        :type StackId: string
        :param StackId:

          A stack ID. If you use this parameter, ``DescribeInstances`` returns descriptions of the
          instances associated with the specified stack.

        :type LayerId: string
        :param LayerId:

          A layer ID. If you use this parameter, ``DescribeInstances`` returns descriptions of the
          instances associated with the specified layer.

        :type InstanceIds: list
        :param InstanceIds:

          An array of instance IDs to be described. If you use this parameter, ``DescribeInstances``
          returns a description of the specified instances. Otherwise, it returns a description of
          every instance.

          - *(string) --*

        :type WaiterConfig: dict
        :param WaiterConfig:

          A dictionary that provides parameters to control waiting behavior.

          - **Delay** *(integer) --*

            The amount of time in seconds to wait between attempts. Default: 15

          - **MaxAttempts** *(integer) --*

            The maximum number of attempts to be made. Default: 40

        :returns: None
        """


class InstanceRegisteredWaiter(Boto3Waiter):
    """
    Waiter for `instance_registered` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        StackId: str = None,
        LayerId: str = None,
        InstanceIds: List[str] = None,
        WaiterConfig: InstanceRegisteredWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        Polls :py:meth:`OpsWorks.Client.describe_instances` every 15 seconds until a successful
        state is reached. An error is returned after 40 failed checks.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/DescribeInstances>`_

        **Request Syntax**
        ::

          waiter.wait(
              StackId='string',
              LayerId='string',
              InstanceIds=[
                  'string',
              ],
              WaiterConfig={
                  'Delay': 123,
                  'MaxAttempts': 123
              }
          )
        :type StackId: string
        :param StackId:

          A stack ID. If you use this parameter, ``DescribeInstances`` returns descriptions of the
          instances associated with the specified stack.

        :type LayerId: string
        :param LayerId:

          A layer ID. If you use this parameter, ``DescribeInstances`` returns descriptions of the
          instances associated with the specified layer.

        :type InstanceIds: list
        :param InstanceIds:

          An array of instance IDs to be described. If you use this parameter, ``DescribeInstances``
          returns a description of the specified instances. Otherwise, it returns a description of
          every instance.

          - *(string) --*

        :type WaiterConfig: dict
        :param WaiterConfig:

          A dictionary that provides parameters to control waiting behavior.

          - **Delay** *(integer) --*

            The amount of time in seconds to wait between attempts. Default: 15

          - **MaxAttempts** *(integer) --*

            The maximum number of attempts to be made. Default: 40

        :returns: None
        """


class InstanceStoppedWaiter(Boto3Waiter):
    """
    Waiter for `instance_stopped` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        StackId: str = None,
        LayerId: str = None,
        InstanceIds: List[str] = None,
        WaiterConfig: InstanceStoppedWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        Polls :py:meth:`OpsWorks.Client.describe_instances` every 15 seconds until a successful
        state is reached. An error is returned after 40 failed checks.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/DescribeInstances>`_

        **Request Syntax**
        ::

          waiter.wait(
              StackId='string',
              LayerId='string',
              InstanceIds=[
                  'string',
              ],
              WaiterConfig={
                  'Delay': 123,
                  'MaxAttempts': 123
              }
          )
        :type StackId: string
        :param StackId:

          A stack ID. If you use this parameter, ``DescribeInstances`` returns descriptions of the
          instances associated with the specified stack.

        :type LayerId: string
        :param LayerId:

          A layer ID. If you use this parameter, ``DescribeInstances`` returns descriptions of the
          instances associated with the specified layer.

        :type InstanceIds: list
        :param InstanceIds:

          An array of instance IDs to be described. If you use this parameter, ``DescribeInstances``
          returns a description of the specified instances. Otherwise, it returns a description of
          every instance.

          - *(string) --*

        :type WaiterConfig: dict
        :param WaiterConfig:

          A dictionary that provides parameters to control waiting behavior.

          - **Delay** *(integer) --*

            The amount of time in seconds to wait between attempts. Default: 15

          - **MaxAttempts** *(integer) --*

            The maximum number of attempts to be made. Default: 40

        :returns: None
        """


class InstanceTerminatedWaiter(Boto3Waiter):
    """
    Waiter for `instance_terminated` name.
    """

    # pylint: disable=arguments-differ,redefined-outer-name,redefined-builtin
    def wait(
        self,
        StackId: str = None,
        LayerId: str = None,
        InstanceIds: List[str] = None,
        WaiterConfig: InstanceTerminatedWaitWaiterConfigTypeDef = None,
    ) -> None:
        """
        Polls :py:meth:`OpsWorks.Client.describe_instances` every 15 seconds until a successful
        state is reached. An error is returned after 40 failed checks.

        See also: `AWS API Documentation
        <https://docs.aws.amazon.com/goto/WebAPI/opsworks-2013-02-18/DescribeInstances>`_

        **Request Syntax**
        ::

          waiter.wait(
              StackId='string',
              LayerId='string',
              InstanceIds=[
                  'string',
              ],
              WaiterConfig={
                  'Delay': 123,
                  'MaxAttempts': 123
              }
          )
        :type StackId: string
        :param StackId:

          A stack ID. If you use this parameter, ``DescribeInstances`` returns descriptions of the
          instances associated with the specified stack.

        :type LayerId: string
        :param LayerId:

          A layer ID. If you use this parameter, ``DescribeInstances`` returns descriptions of the
          instances associated with the specified layer.

        :type InstanceIds: list
        :param InstanceIds:

          An array of instance IDs to be described. If you use this parameter, ``DescribeInstances``
          returns a description of the specified instances. Otherwise, it returns a description of
          every instance.

          - *(string) --*

        :type WaiterConfig: dict
        :param WaiterConfig:

          A dictionary that provides parameters to control waiting behavior.

          - **Delay** *(integer) --*

            The amount of time in seconds to wait between attempts. Default: 15

          - **MaxAttempts** *(integer) --*

            The maximum number of attempts to be made. Default: 40

        :returns: None
        """
