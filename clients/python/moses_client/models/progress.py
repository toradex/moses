# coding: utf-8

"""
    Torizon IDE-backend API

    Toradex API to build and deploy applications running as containers on Torizon  # noqa: E501

    The version of the OpenAPI document: 1.0.14
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from moses_client.configuration import Configuration


class Progress(object):
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
        'id': 'str',
        'progress': 'int',
        'messages': 'list[str]',
        'pending': 'bool',
        'result': 'ErrorInfo'
    }

    attribute_map = {
        'id': 'id',
        'progress': 'progress',
        'messages': 'messages',
        'pending': 'pending',
        'result': 'result'
    }

    def __init__(self, id=None, progress=None, messages=None, pending=None, result=None, local_vars_configuration=None):  # noqa: E501
        """Progress - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._progress = None
        self._messages = None
        self._pending = None
        self._result = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if progress is not None:
            self.progress = progress
        if messages is not None:
            self.messages = messages
        if pending is not None:
            self.pending = pending
        if result is not None:
            self.result = result

    @property
    def id(self):
        """Gets the id of this Progress.  # noqa: E501

        cookie  # noqa: E501

        :return: The id of this Progress.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Progress.

        cookie  # noqa: E501

        :param id: The id of this Progress.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def progress(self):
        """Gets the progress of this Progress.  # noqa: E501

        0%-100%  # noqa: E501

        :return: The progress of this Progress.  # noqa: E501
        :rtype: int
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this Progress.

        0%-100%  # noqa: E501

        :param progress: The progress of this Progress.  # noqa: E501
        :type progress: int
        """

        self._progress = progress

    @property
    def messages(self):
        """Gets the messages of this Progress.  # noqa: E501


        :return: The messages of this Progress.  # noqa: E501
        :rtype: list[str]
        """
        return self._messages

    @messages.setter
    def messages(self, messages):
        """Sets the messages of this Progress.


        :param messages: The messages of this Progress.  # noqa: E501
        :type messages: list[str]
        """

        self._messages = messages

    @property
    def pending(self):
        """Gets the pending of this Progress.  # noqa: E501

        true as long as operation is pending  # noqa: E501

        :return: The pending of this Progress.  # noqa: E501
        :rtype: bool
        """
        return self._pending

    @pending.setter
    def pending(self, pending):
        """Sets the pending of this Progress.

        true as long as operation is pending  # noqa: E501

        :param pending: The pending of this Progress.  # noqa: E501
        :type pending: bool
        """

        self._pending = pending

    @property
    def result(self):
        """Gets the result of this Progress.  # noqa: E501


        :return: The result of this Progress.  # noqa: E501
        :rtype: ErrorInfo
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this Progress.


        :param result: The result of this Progress.  # noqa: E501
        :type result: ErrorInfo
        """

        self._result = result

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
        if not isinstance(other, Progress):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Progress):
            return True

        return self.to_dict() != other.to_dict()
