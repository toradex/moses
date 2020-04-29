# coding: utf-8

"""
    Torizon Deployment API

    Toradex Development API to build and deploy application on Torizon  # noqa: E501

    The version of the OpenAPI document: 1.0.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from moses_client.configuration import Configuration


class DockerMount(object):
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
        'target': 'str',
        'source': 'str',
        'type': 'str',
        'read_only': 'bool',
        'consistency': 'str',
        'bind_options': 'DockerMountBindOptions',
        'volume_options': 'DockerMountVolumeOptions',
        'tmpfs_options': 'DockerMountTmpfsOptions'
    }

    attribute_map = {
        'target': 'Target',
        'source': 'Source',
        'type': 'Type',
        'read_only': 'ReadOnly',
        'consistency': 'Consistency',
        'bind_options': 'BindOptions',
        'volume_options': 'VolumeOptions',
        'tmpfs_options': 'TmpfsOptions'
    }

    def __init__(self, target=None, source=None, type=None, read_only=None, consistency=None, bind_options=None, volume_options=None, tmpfs_options=None, local_vars_configuration=None):  # noqa: E501
        """DockerMount - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._target = None
        self._source = None
        self._type = None
        self._read_only = None
        self._consistency = None
        self._bind_options = None
        self._volume_options = None
        self._tmpfs_options = None
        self.discriminator = None

        if target is not None:
            self.target = target
        if source is not None:
            self.source = source
        if type is not None:
            self.type = type
        if read_only is not None:
            self.read_only = read_only
        if consistency is not None:
            self.consistency = consistency
        if bind_options is not None:
            self.bind_options = bind_options
        if volume_options is not None:
            self.volume_options = volume_options
        if tmpfs_options is not None:
            self.tmpfs_options = tmpfs_options

    @property
    def target(self):
        """Gets the target of this DockerMount.  # noqa: E501

        Container path.  # noqa: E501

        :return: The target of this DockerMount.  # noqa: E501
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this DockerMount.

        Container path.  # noqa: E501

        :param target: The target of this DockerMount.  # noqa: E501
        :type: str
        """

        self._target = target

    @property
    def source(self):
        """Gets the source of this DockerMount.  # noqa: E501

        Mount source (e.g. a volume name, a host path).  # noqa: E501

        :return: The source of this DockerMount.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this DockerMount.

        Mount source (e.g. a volume name, a host path).  # noqa: E501

        :param source: The source of this DockerMount.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def type(self):
        """Gets the type of this DockerMount.  # noqa: E501

        The mount type. Available types:  - `bind` Mounts a file or directory from the host into the container. Must exist prior to creating the container. - `volume` Creates a volume with the given name and options (or uses a pre-existing volume with the same name and options). These are **not** removed when the container is removed. - `tmpfs` Create a tmpfs with the given options. The mount source cannot be specified for tmpfs.   # noqa: E501

        :return: The type of this DockerMount.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DockerMount.

        The mount type. Available types:  - `bind` Mounts a file or directory from the host into the container. Must exist prior to creating the container. - `volume` Creates a volume with the given name and options (or uses a pre-existing volume with the same name and options). These are **not** removed when the container is removed. - `tmpfs` Create a tmpfs with the given options. The mount source cannot be specified for tmpfs.   # noqa: E501

        :param type: The type of this DockerMount.  # noqa: E501
        :type: str
        """
        allowed_values = ["bind", "volume", "tmpfs"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def read_only(self):
        """Gets the read_only of this DockerMount.  # noqa: E501

        Whether the mount should be read-only.  # noqa: E501

        :return: The read_only of this DockerMount.  # noqa: E501
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """Sets the read_only of this DockerMount.

        Whether the mount should be read-only.  # noqa: E501

        :param read_only: The read_only of this DockerMount.  # noqa: E501
        :type: bool
        """

        self._read_only = read_only

    @property
    def consistency(self):
        """Gets the consistency of this DockerMount.  # noqa: E501

        The consistency requirement for the mount: `default`, `consistent`, `cached`, or `delegated`.  # noqa: E501

        :return: The consistency of this DockerMount.  # noqa: E501
        :rtype: str
        """
        return self._consistency

    @consistency.setter
    def consistency(self, consistency):
        """Sets the consistency of this DockerMount.

        The consistency requirement for the mount: `default`, `consistent`, `cached`, or `delegated`.  # noqa: E501

        :param consistency: The consistency of this DockerMount.  # noqa: E501
        :type: str
        """

        self._consistency = consistency

    @property
    def bind_options(self):
        """Gets the bind_options of this DockerMount.  # noqa: E501


        :return: The bind_options of this DockerMount.  # noqa: E501
        :rtype: DockerMountBindOptions
        """
        return self._bind_options

    @bind_options.setter
    def bind_options(self, bind_options):
        """Sets the bind_options of this DockerMount.


        :param bind_options: The bind_options of this DockerMount.  # noqa: E501
        :type: DockerMountBindOptions
        """

        self._bind_options = bind_options

    @property
    def volume_options(self):
        """Gets the volume_options of this DockerMount.  # noqa: E501


        :return: The volume_options of this DockerMount.  # noqa: E501
        :rtype: DockerMountVolumeOptions
        """
        return self._volume_options

    @volume_options.setter
    def volume_options(self, volume_options):
        """Sets the volume_options of this DockerMount.


        :param volume_options: The volume_options of this DockerMount.  # noqa: E501
        :type: DockerMountVolumeOptions
        """

        self._volume_options = volume_options

    @property
    def tmpfs_options(self):
        """Gets the tmpfs_options of this DockerMount.  # noqa: E501


        :return: The tmpfs_options of this DockerMount.  # noqa: E501
        :rtype: DockerMountTmpfsOptions
        """
        return self._tmpfs_options

    @tmpfs_options.setter
    def tmpfs_options(self, tmpfs_options):
        """Sets the tmpfs_options of this DockerMount.


        :param tmpfs_options: The tmpfs_options of this DockerMount.  # noqa: E501
        :type: DockerMountTmpfsOptions
        """

        self._tmpfs_options = tmpfs_options

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
        if not isinstance(other, DockerMount):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DockerMount):
            return True

        return self.to_dict() != other.to_dict()
