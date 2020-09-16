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


class Eula(object):
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
        'title': 'str',
        'question': 'str',
        'filepath': 'str',
        'visualized': 'bool',
        'accepted': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'title': 'title',
        'question': 'question',
        'filepath': 'filepath',
        'visualized': 'visualized',
        'accepted': 'accepted'
    }

    def __init__(self, id=None, title=None, question=None, filepath=None, visualized=None, accepted=None, local_vars_configuration=None):  # noqa: E501
        """Eula - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._title = None
        self._question = None
        self._filepath = None
        self._visualized = None
        self._accepted = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if title is not None:
            self.title = title
        if question is not None:
            self.question = question
        if filepath is not None:
            self.filepath = filepath
        if visualized is not None:
            self.visualized = visualized
        if accepted is not None:
            self.accepted = accepted

    @property
    def id(self):
        """Gets the id of this Eula.  # noqa: E501

        Unique name (should be filesystem-compatible)  # noqa: E501

        :return: The id of this Eula.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Eula.

        Unique name (should be filesystem-compatible)  # noqa: E501

        :param id: The id of this Eula.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def title(self):
        """Gets the title of this Eula.  # noqa: E501

        eula title  # noqa: E501

        :return: The title of this Eula.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Eula.

        eula title  # noqa: E501

        :param title: The title of this Eula.  # noqa: E501
        :type title: str
        """

        self._title = title

    @property
    def question(self):
        """Gets the question of this Eula.  # noqa: E501

        message shown to the user to accept/decline license  # noqa: E501

        :return: The question of this Eula.  # noqa: E501
        :rtype: str
        """
        return self._question

    @question.setter
    def question(self, question):
        """Sets the question of this Eula.

        message shown to the user to accept/decline license  # noqa: E501

        :param question: The question of this Eula.  # noqa: E501
        :type question: str
        """

        self._question = question

    @property
    def filepath(self):
        """Gets the filepath of this Eula.  # noqa: E501

        full path of the file containing the license text  # noqa: E501

        :return: The filepath of this Eula.  # noqa: E501
        :rtype: str
        """
        return self._filepath

    @filepath.setter
    def filepath(self, filepath):
        """Sets the filepath of this Eula.

        full path of the file containing the license text  # noqa: E501

        :param filepath: The filepath of this Eula.  # noqa: E501
        :type filepath: str
        """

        self._filepath = filepath

    @property
    def visualized(self):
        """Gets the visualized of this Eula.  # noqa: E501

        true if license has been shown at least once to user  # noqa: E501

        :return: The visualized of this Eula.  # noqa: E501
        :rtype: bool
        """
        return self._visualized

    @visualized.setter
    def visualized(self, visualized):
        """Sets the visualized of this Eula.

        true if license has been shown at least once to user  # noqa: E501

        :param visualized: The visualized of this Eula.  # noqa: E501
        :type visualized: bool
        """

        self._visualized = visualized

    @property
    def accepted(self):
        """Gets the accepted of this Eula.  # noqa: E501

        true if user accepted the license  # noqa: E501

        :return: The accepted of this Eula.  # noqa: E501
        :rtype: bool
        """
        return self._accepted

    @accepted.setter
    def accepted(self, accepted):
        """Sets the accepted of this Eula.

        true if user accepted the license  # noqa: E501

        :param accepted: The accepted of this Eula.  # noqa: E501
        :type accepted: bool
        """

        self._accepted = accepted

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
        if not isinstance(other, Eula):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Eula):
            return True

        return self.to_dict() != other.to_dict()
