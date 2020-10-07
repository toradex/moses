# coding: utf-8

"""
    Torizon IDE-backend API

    Toradex API to build and deploy applications running as containers on Torizon  # noqa: E501

    The version of the OpenAPI document: 1.0.9
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from moses_client.configuration import Configuration


class ErrorInfo(object):
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
        'code': 'int',
        'message': 'str',
        'description': 'str'
    }

    attribute_map = {
        'code': 'code',
        'message': 'message',
        'description': 'description'
    }

    def __init__(self, code=None, message=None, description=None, local_vars_configuration=None):  # noqa: E501
        """ErrorInfo - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._code = None
        self._message = None
        self._description = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if message is not None:
            self.message = message
        if description is not None:
            self.description = description

    @property
    def code(self):
        """Gets the code of this ErrorInfo.  # noqa: E501

        error code  # noqa: E501

        :return: The code of this ErrorInfo.  # noqa: E501
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ErrorInfo.

        error code  # noqa: E501

        :param code: The code of this ErrorInfo.  # noqa: E501
        :type code: int
        """

        self._code = code

    @property
    def message(self):
        """Gets the message of this ErrorInfo.  # noqa: E501

        specific error message  # noqa: E501

        :return: The message of this ErrorInfo.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ErrorInfo.

        specific error message  # noqa: E501

        :param message: The message of this ErrorInfo.  # noqa: E501
        :type message: str
        """

        self._message = message

    @property
    def description(self):
        """Gets the description of this ErrorInfo.  # noqa: E501

        generic error description  # noqa: E501

        :return: The description of this ErrorInfo.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ErrorInfo.

        generic error description  # noqa: E501

        :param description: The description of this ErrorInfo.  # noqa: E501
        :type description: str
        """

        self._description = description

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
        if not isinstance(other, ErrorInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ErrorInfo):
            return True

        return self.to_dict() != other.to_dict()
