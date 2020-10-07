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


class DockerVersion(object):
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
        'platform': 'DockerVersionPlatform',
        'components': 'list[DockerVersionComponents]',
        'version': 'str',
        'api_version': 'str',
        'min_api_version': 'str',
        'git_commit': 'str',
        'go_version': 'str',
        'os': 'str',
        'arch': 'str',
        'kernel_version': 'str',
        'experimental': 'bool',
        'build_time': 'str'
    }

    attribute_map = {
        'platform': 'Platform',
        'components': 'Components',
        'version': 'Version',
        'api_version': 'ApiVersion',
        'min_api_version': 'MinAPIVersion',
        'git_commit': 'GitCommit',
        'go_version': 'GoVersion',
        'os': 'Os',
        'arch': 'Arch',
        'kernel_version': 'KernelVersion',
        'experimental': 'Experimental',
        'build_time': 'BuildTime'
    }

    def __init__(self, platform=None, components=None, version=None, api_version=None, min_api_version=None, git_commit=None, go_version=None, os=None, arch=None, kernel_version=None, experimental=None, build_time=None, local_vars_configuration=None):  # noqa: E501
        """DockerVersion - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._platform = None
        self._components = None
        self._version = None
        self._api_version = None
        self._min_api_version = None
        self._git_commit = None
        self._go_version = None
        self._os = None
        self._arch = None
        self._kernel_version = None
        self._experimental = None
        self._build_time = None
        self.discriminator = None

        if platform is not None:
            self.platform = platform
        if components is not None:
            self.components = components
        if version is not None:
            self.version = version
        if api_version is not None:
            self.api_version = api_version
        if min_api_version is not None:
            self.min_api_version = min_api_version
        if git_commit is not None:
            self.git_commit = git_commit
        if go_version is not None:
            self.go_version = go_version
        if os is not None:
            self.os = os
        if arch is not None:
            self.arch = arch
        if kernel_version is not None:
            self.kernel_version = kernel_version
        if experimental is not None:
            self.experimental = experimental
        if build_time is not None:
            self.build_time = build_time

    @property
    def platform(self):
        """Gets the platform of this DockerVersion.  # noqa: E501


        :return: The platform of this DockerVersion.  # noqa: E501
        :rtype: DockerVersionPlatform
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this DockerVersion.


        :param platform: The platform of this DockerVersion.  # noqa: E501
        :type platform: DockerVersionPlatform
        """

        self._platform = platform

    @property
    def components(self):
        """Gets the components of this DockerVersion.  # noqa: E501


        :return: The components of this DockerVersion.  # noqa: E501
        :rtype: list[DockerVersionComponents]
        """
        return self._components

    @components.setter
    def components(self, components):
        """Sets the components of this DockerVersion.


        :param components: The components of this DockerVersion.  # noqa: E501
        :type components: list[DockerVersionComponents]
        """

        self._components = components

    @property
    def version(self):
        """Gets the version of this DockerVersion.  # noqa: E501


        :return: The version of this DockerVersion.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this DockerVersion.


        :param version: The version of this DockerVersion.  # noqa: E501
        :type version: str
        """

        self._version = version

    @property
    def api_version(self):
        """Gets the api_version of this DockerVersion.  # noqa: E501


        :return: The api_version of this DockerVersion.  # noqa: E501
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this DockerVersion.


        :param api_version: The api_version of this DockerVersion.  # noqa: E501
        :type api_version: str
        """

        self._api_version = api_version

    @property
    def min_api_version(self):
        """Gets the min_api_version of this DockerVersion.  # noqa: E501


        :return: The min_api_version of this DockerVersion.  # noqa: E501
        :rtype: str
        """
        return self._min_api_version

    @min_api_version.setter
    def min_api_version(self, min_api_version):
        """Sets the min_api_version of this DockerVersion.


        :param min_api_version: The min_api_version of this DockerVersion.  # noqa: E501
        :type min_api_version: str
        """

        self._min_api_version = min_api_version

    @property
    def git_commit(self):
        """Gets the git_commit of this DockerVersion.  # noqa: E501


        :return: The git_commit of this DockerVersion.  # noqa: E501
        :rtype: str
        """
        return self._git_commit

    @git_commit.setter
    def git_commit(self, git_commit):
        """Sets the git_commit of this DockerVersion.


        :param git_commit: The git_commit of this DockerVersion.  # noqa: E501
        :type git_commit: str
        """

        self._git_commit = git_commit

    @property
    def go_version(self):
        """Gets the go_version of this DockerVersion.  # noqa: E501


        :return: The go_version of this DockerVersion.  # noqa: E501
        :rtype: str
        """
        return self._go_version

    @go_version.setter
    def go_version(self, go_version):
        """Sets the go_version of this DockerVersion.


        :param go_version: The go_version of this DockerVersion.  # noqa: E501
        :type go_version: str
        """

        self._go_version = go_version

    @property
    def os(self):
        """Gets the os of this DockerVersion.  # noqa: E501


        :return: The os of this DockerVersion.  # noqa: E501
        :rtype: str
        """
        return self._os

    @os.setter
    def os(self, os):
        """Sets the os of this DockerVersion.


        :param os: The os of this DockerVersion.  # noqa: E501
        :type os: str
        """

        self._os = os

    @property
    def arch(self):
        """Gets the arch of this DockerVersion.  # noqa: E501


        :return: The arch of this DockerVersion.  # noqa: E501
        :rtype: str
        """
        return self._arch

    @arch.setter
    def arch(self, arch):
        """Sets the arch of this DockerVersion.


        :param arch: The arch of this DockerVersion.  # noqa: E501
        :type arch: str
        """

        self._arch = arch

    @property
    def kernel_version(self):
        """Gets the kernel_version of this DockerVersion.  # noqa: E501


        :return: The kernel_version of this DockerVersion.  # noqa: E501
        :rtype: str
        """
        return self._kernel_version

    @kernel_version.setter
    def kernel_version(self, kernel_version):
        """Sets the kernel_version of this DockerVersion.


        :param kernel_version: The kernel_version of this DockerVersion.  # noqa: E501
        :type kernel_version: str
        """

        self._kernel_version = kernel_version

    @property
    def experimental(self):
        """Gets the experimental of this DockerVersion.  # noqa: E501


        :return: The experimental of this DockerVersion.  # noqa: E501
        :rtype: bool
        """
        return self._experimental

    @experimental.setter
    def experimental(self, experimental):
        """Sets the experimental of this DockerVersion.


        :param experimental: The experimental of this DockerVersion.  # noqa: E501
        :type experimental: bool
        """

        self._experimental = experimental

    @property
    def build_time(self):
        """Gets the build_time of this DockerVersion.  # noqa: E501


        :return: The build_time of this DockerVersion.  # noqa: E501
        :rtype: str
        """
        return self._build_time

    @build_time.setter
    def build_time(self, build_time):
        """Sets the build_time of this DockerVersion.


        :param build_time: The build_time of this DockerVersion.  # noqa: E501
        :type build_time: str
        """

        self._build_time = build_time

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
        if not isinstance(other, DockerVersion):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DockerVersion):
            return True

        return self.to_dict() != other.to_dict()
