# coding: utf-8

"""
    Torizon IDE-backend API

    Toradex API to build and deploy applications running as containers on Torizon  # noqa: E501

    The version of the OpenAPI document: 1.0.12
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from moses_client.configuration import Configuration


class DockerContainerState(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'status': 'str',
        'running': 'bool',
        'paused': 'bool',
        'restarting': 'bool',
        'oom_killed': 'bool',
        'dead': 'bool',
        'pid': 'int',
        'exit_code': 'int',
        'error': 'str',
        'started_at': 'str',
        'finished_at': 'str'
    }

    attribute_map = {
        'status': 'Status',
        'running': 'Running',
        'paused': 'Paused',
        'restarting': 'Restarting',
        'oom_killed': 'OOMKilled',
        'dead': 'Dead',
        'pid': 'Pid',
        'exit_code': 'ExitCode',
        'error': 'Error',
        'started_at': 'StartedAt',
        'finished_at': 'FinishedAt'
    }

    def __init__(self, status=None, running=None, paused=None, restarting=None, oom_killed=None, dead=None, pid=None, exit_code=None, error=None, started_at=None, finished_at=None, local_vars_configuration=None):  # noqa: E501
        """DockerContainerState - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._status = None
        self._running = None
        self._paused = None
        self._restarting = None
        self._oom_killed = None
        self._dead = None
        self._pid = None
        self._exit_code = None
        self._error = None
        self._started_at = None
        self._finished_at = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if running is not None:
            self.running = running
        if paused is not None:
            self.paused = paused
        if restarting is not None:
            self.restarting = restarting
        if oom_killed is not None:
            self.oom_killed = oom_killed
        if dead is not None:
            self.dead = dead
        if pid is not None:
            self.pid = pid
        if exit_code is not None:
            self.exit_code = exit_code
        if error is not None:
            self.error = error
        if started_at is not None:
            self.started_at = started_at
        if finished_at is not None:
            self.finished_at = finished_at

    @property
    def status(self):
        """Gets the status of this DockerContainerState.  # noqa: E501

        The status of the container. For example, `\"running\"` or `\"exited\"`.   # noqa: E501

        :return: The status of this DockerContainerState.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DockerContainerState.

        The status of the container. For example, `\"running\"` or `\"exited\"`.   # noqa: E501

        :param status: The status of this DockerContainerState.  # noqa: E501
        :type status: str
        """
        allowed_values = ["created", "running", "paused", "restarting", "removing", "exited", "dead"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and status not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def running(self):
        """Gets the running of this DockerContainerState.  # noqa: E501

        Whether this container is running.  Note that a running container can be _paused_. The `Running` and `Paused` booleans are not mutually exclusive:  When pausing a container (on Linux), the cgroups freezer is used to suspend all processes in the container. Freezing the process requires the process to be running. As a result, paused containers are both `Running` _and_ `Paused`.  Use the `Status` field instead to determine if a container's state is \"running\".   # noqa: E501

        :return: The running of this DockerContainerState.  # noqa: E501
        :rtype: bool
        """
        return self._running

    @running.setter
    def running(self, running):
        """Sets the running of this DockerContainerState.

        Whether this container is running.  Note that a running container can be _paused_. The `Running` and `Paused` booleans are not mutually exclusive:  When pausing a container (on Linux), the cgroups freezer is used to suspend all processes in the container. Freezing the process requires the process to be running. As a result, paused containers are both `Running` _and_ `Paused`.  Use the `Status` field instead to determine if a container's state is \"running\".   # noqa: E501

        :param running: The running of this DockerContainerState.  # noqa: E501
        :type running: bool
        """

        self._running = running

    @property
    def paused(self):
        """Gets the paused of this DockerContainerState.  # noqa: E501

        Whether this container is paused.  # noqa: E501

        :return: The paused of this DockerContainerState.  # noqa: E501
        :rtype: bool
        """
        return self._paused

    @paused.setter
    def paused(self, paused):
        """Sets the paused of this DockerContainerState.

        Whether this container is paused.  # noqa: E501

        :param paused: The paused of this DockerContainerState.  # noqa: E501
        :type paused: bool
        """

        self._paused = paused

    @property
    def restarting(self):
        """Gets the restarting of this DockerContainerState.  # noqa: E501

        Whether this container is restarting.  # noqa: E501

        :return: The restarting of this DockerContainerState.  # noqa: E501
        :rtype: bool
        """
        return self._restarting

    @restarting.setter
    def restarting(self, restarting):
        """Sets the restarting of this DockerContainerState.

        Whether this container is restarting.  # noqa: E501

        :param restarting: The restarting of this DockerContainerState.  # noqa: E501
        :type restarting: bool
        """

        self._restarting = restarting

    @property
    def oom_killed(self):
        """Gets the oom_killed of this DockerContainerState.  # noqa: E501

        Whether this container has been killed because it ran out of memory.  # noqa: E501

        :return: The oom_killed of this DockerContainerState.  # noqa: E501
        :rtype: bool
        """
        return self._oom_killed

    @oom_killed.setter
    def oom_killed(self, oom_killed):
        """Sets the oom_killed of this DockerContainerState.

        Whether this container has been killed because it ran out of memory.  # noqa: E501

        :param oom_killed: The oom_killed of this DockerContainerState.  # noqa: E501
        :type oom_killed: bool
        """

        self._oom_killed = oom_killed

    @property
    def dead(self):
        """Gets the dead of this DockerContainerState.  # noqa: E501


        :return: The dead of this DockerContainerState.  # noqa: E501
        :rtype: bool
        """
        return self._dead

    @dead.setter
    def dead(self, dead):
        """Sets the dead of this DockerContainerState.


        :param dead: The dead of this DockerContainerState.  # noqa: E501
        :type dead: bool
        """

        self._dead = dead

    @property
    def pid(self):
        """Gets the pid of this DockerContainerState.  # noqa: E501

        The process ID of this container  # noqa: E501

        :return: The pid of this DockerContainerState.  # noqa: E501
        :rtype: int
        """
        return self._pid

    @pid.setter
    def pid(self, pid):
        """Sets the pid of this DockerContainerState.

        The process ID of this container  # noqa: E501

        :param pid: The pid of this DockerContainerState.  # noqa: E501
        :type pid: int
        """

        self._pid = pid

    @property
    def exit_code(self):
        """Gets the exit_code of this DockerContainerState.  # noqa: E501

        The last exit code of this container  # noqa: E501

        :return: The exit_code of this DockerContainerState.  # noqa: E501
        :rtype: int
        """
        return self._exit_code

    @exit_code.setter
    def exit_code(self, exit_code):
        """Sets the exit_code of this DockerContainerState.

        The last exit code of this container  # noqa: E501

        :param exit_code: The exit_code of this DockerContainerState.  # noqa: E501
        :type exit_code: int
        """

        self._exit_code = exit_code

    @property
    def error(self):
        """Gets the error of this DockerContainerState.  # noqa: E501


        :return: The error of this DockerContainerState.  # noqa: E501
        :rtype: str
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this DockerContainerState.


        :param error: The error of this DockerContainerState.  # noqa: E501
        :type error: str
        """

        self._error = error

    @property
    def started_at(self):
        """Gets the started_at of this DockerContainerState.  # noqa: E501

        The time when this container was last started.  # noqa: E501

        :return: The started_at of this DockerContainerState.  # noqa: E501
        :rtype: str
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """Sets the started_at of this DockerContainerState.

        The time when this container was last started.  # noqa: E501

        :param started_at: The started_at of this DockerContainerState.  # noqa: E501
        :type started_at: str
        """

        self._started_at = started_at

    @property
    def finished_at(self):
        """Gets the finished_at of this DockerContainerState.  # noqa: E501

        The time when this container last exited.  # noqa: E501

        :return: The finished_at of this DockerContainerState.  # noqa: E501
        :rtype: str
        """
        return self._finished_at

    @finished_at.setter
    def finished_at(self, finished_at):
        """Sets the finished_at of this DockerContainerState.

        The time when this container last exited.  # noqa: E501

        :param finished_at: The finished_at of this DockerContainerState.  # noqa: E501
        :type finished_at: str
        """

        self._finished_at = finished_at

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DockerContainerState):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DockerContainerState):
            return True

        return self.to_dict() != other.to_dict()
