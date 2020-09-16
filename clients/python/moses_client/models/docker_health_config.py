# coding: utf-8

"""
    Torizon IDE-backend API

    Toradex API to build and deploy applications running as containers on Torizon  # noqa: E501

    The version of the OpenAPI document: 1.0.8
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from moses_client.configuration import Configuration


class DockerHealthConfig(object):
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
        'test': 'list[str]',
        'interval': 'int',
        'timeout': 'int',
        'retries': 'int',
        'start_period': 'int'
    }

    attribute_map = {
        'test': 'Test',
        'interval': 'Interval',
        'timeout': 'Timeout',
        'retries': 'Retries',
        'start_period': 'StartPeriod'
    }

    def __init__(self, test=None, interval=None, timeout=None, retries=None, start_period=None, local_vars_configuration=None):  # noqa: E501
        """DockerHealthConfig - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._test = None
        self._interval = None
        self._timeout = None
        self._retries = None
        self._start_period = None
        self.discriminator = None

        if test is not None:
            self.test = test
        if interval is not None:
            self.interval = interval
        if timeout is not None:
            self.timeout = timeout
        if retries is not None:
            self.retries = retries
        if start_period is not None:
            self.start_period = start_period

    @property
    def test(self):
        """Gets the test of this DockerHealthConfig.  # noqa: E501

        The test to perform. Possible values are:  - `[]` inherit healthcheck from image or parent image - `[\"NONE\"]` disable healthcheck - `[\"CMD\", args...]` exec arguments directly - `[\"CMD-SHELL\", command]` run command with system's default shell   # noqa: E501

        :return: The test of this DockerHealthConfig.  # noqa: E501
        :rtype: list[str]
        """
        return self._test

    @test.setter
    def test(self, test):
        """Sets the test of this DockerHealthConfig.

        The test to perform. Possible values are:  - `[]` inherit healthcheck from image or parent image - `[\"NONE\"]` disable healthcheck - `[\"CMD\", args...]` exec arguments directly - `[\"CMD-SHELL\", command]` run command with system's default shell   # noqa: E501

        :param test: The test of this DockerHealthConfig.  # noqa: E501
        :type test: list[str]
        """

        self._test = test

    @property
    def interval(self):
        """Gets the interval of this DockerHealthConfig.  # noqa: E501

        The time to wait between checks in nanoseconds. It should be 0 or at least 1000000 (1 ms). 0 means inherit.  # noqa: E501

        :return: The interval of this DockerHealthConfig.  # noqa: E501
        :rtype: int
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this DockerHealthConfig.

        The time to wait between checks in nanoseconds. It should be 0 or at least 1000000 (1 ms). 0 means inherit.  # noqa: E501

        :param interval: The interval of this DockerHealthConfig.  # noqa: E501
        :type interval: int
        """

        self._interval = interval

    @property
    def timeout(self):
        """Gets the timeout of this DockerHealthConfig.  # noqa: E501

        The time to wait before considering the check to have hung. It should be 0 or at least 1000000 (1 ms). 0 means inherit.  # noqa: E501

        :return: The timeout of this DockerHealthConfig.  # noqa: E501
        :rtype: int
        """
        return self._timeout

    @timeout.setter
    def timeout(self, timeout):
        """Sets the timeout of this DockerHealthConfig.

        The time to wait before considering the check to have hung. It should be 0 or at least 1000000 (1 ms). 0 means inherit.  # noqa: E501

        :param timeout: The timeout of this DockerHealthConfig.  # noqa: E501
        :type timeout: int
        """

        self._timeout = timeout

    @property
    def retries(self):
        """Gets the retries of this DockerHealthConfig.  # noqa: E501

        The number of consecutive failures needed to consider a container as unhealthy. 0 means inherit.  # noqa: E501

        :return: The retries of this DockerHealthConfig.  # noqa: E501
        :rtype: int
        """
        return self._retries

    @retries.setter
    def retries(self, retries):
        """Sets the retries of this DockerHealthConfig.

        The number of consecutive failures needed to consider a container as unhealthy. 0 means inherit.  # noqa: E501

        :param retries: The retries of this DockerHealthConfig.  # noqa: E501
        :type retries: int
        """

        self._retries = retries

    @property
    def start_period(self):
        """Gets the start_period of this DockerHealthConfig.  # noqa: E501

        Start period for the container to initialize before starting health-retries countdown in nanoseconds. It should be 0 or at least 1000000 (1 ms). 0 means inherit.  # noqa: E501

        :return: The start_period of this DockerHealthConfig.  # noqa: E501
        :rtype: int
        """
        return self._start_period

    @start_period.setter
    def start_period(self, start_period):
        """Sets the start_period of this DockerHealthConfig.

        Start period for the container to initialize before starting health-retries countdown in nanoseconds. It should be 0 or at least 1000000 (1 ms). 0 means inherit.  # noqa: E501

        :param start_period: The start_period of this DockerHealthConfig.  # noqa: E501
        :type start_period: int
        """

        self._start_period = start_period

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
        if not isinstance(other, DockerHealthConfig):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DockerHealthConfig):
            return True

        return self.to_dict() != other.to_dict()
