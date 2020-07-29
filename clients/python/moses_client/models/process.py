# coding: utf-8

"""
    Torizon IDE-backend API

    Toradex API to build and deploy applications running as containers on Torizon  # noqa: E501

    The version of the OpenAPI document: 1.0.6
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from moses_client.configuration import Configuration


class Process(object):
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
        'pid': 'int',
        'ppid': 'int',
        'user': 'str',
        'time': 'str',
        'nice': 'int',
        'state': 'str',
        'args': 'str'
    }

    attribute_map = {
        'pid': 'pid',
        'ppid': 'ppid',
        'user': 'user',
        'time': 'time',
        'nice': 'nice',
        'state': 'state',
        'args': 'args'
    }

    def __init__(self, pid=None, ppid=None, user=None, time=None, nice=None, state=None, args=None, local_vars_configuration=None):  # noqa: E501
        """Process - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._pid = None
        self._ppid = None
        self._user = None
        self._time = None
        self._nice = None
        self._state = None
        self._args = None
        self.discriminator = None

        if pid is not None:
            self.pid = pid
        if ppid is not None:
            self.ppid = ppid
        if user is not None:
            self.user = user
        if time is not None:
            self.time = time
        if nice is not None:
            self.nice = nice
        if state is not None:
            self.state = state
        if args is not None:
            self.args = args

    @property
    def pid(self):
        """Gets the pid of this Process.  # noqa: E501

        process id  # noqa: E501

        :return: The pid of this Process.  # noqa: E501
        :rtype: int
        """
        return self._pid

    @pid.setter
    def pid(self, pid):
        """Sets the pid of this Process.

        process id  # noqa: E501

        :param pid: The pid of this Process.  # noqa: E501
        :type pid: int
        """

        self._pid = pid

    @property
    def ppid(self):
        """Gets the ppid of this Process.  # noqa: E501

        parent process id  # noqa: E501

        :return: The ppid of this Process.  # noqa: E501
        :rtype: int
        """
        return self._ppid

    @ppid.setter
    def ppid(self, ppid):
        """Sets the ppid of this Process.

        parent process id  # noqa: E501

        :param ppid: The ppid of this Process.  # noqa: E501
        :type ppid: int
        """

        self._ppid = ppid

    @property
    def user(self):
        """Gets the user of this Process.  # noqa: E501


        :return: The user of this Process.  # noqa: E501
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this Process.


        :param user: The user of this Process.  # noqa: E501
        :type user: str
        """

        self._user = user

    @property
    def time(self):
        """Gets the time of this Process.  # noqa: E501

        cpu time  # noqa: E501

        :return: The time of this Process.  # noqa: E501
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this Process.

        cpu time  # noqa: E501

        :param time: The time of this Process.  # noqa: E501
        :type time: str
        """

        self._time = time

    @property
    def nice(self):
        """Gets the nice of this Process.  # noqa: E501

        nice value  # noqa: E501

        :return: The nice of this Process.  # noqa: E501
        :rtype: int
        """
        return self._nice

    @nice.setter
    def nice(self, nice):
        """Sets the nice of this Process.

        nice value  # noqa: E501

        :param nice: The nice of this Process.  # noqa: E501
        :type nice: int
        """

        self._nice = nice

    @property
    def state(self):
        """Gets the state of this Process.  # noqa: E501

        process state code  # noqa: E501

        :return: The state of this Process.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Process.

        process state code  # noqa: E501

        :param state: The state of this Process.  # noqa: E501
        :type state: str
        """

        self._state = state

    @property
    def args(self):
        """Gets the args of this Process.  # noqa: E501

        command used to start process  # noqa: E501

        :return: The args of this Process.  # noqa: E501
        :rtype: str
        """
        return self._args

    @args.setter
    def args(self, args):
        """Sets the args of this Process.

        command used to start process  # noqa: E501

        :param args: The args of this Process.  # noqa: E501
        :type args: str
        """

        self._args = args

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
        if not isinstance(other, Process):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Process):
            return True

        return self.to_dict() != other.to_dict()
