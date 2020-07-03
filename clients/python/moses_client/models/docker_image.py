# coding: utf-8

"""
    Torizon IDE-backend API

    Toradex API to build and deploy applications running as containers on Torizon  # noqa: E501

    The version of the OpenAPI document: 1.0.5
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from moses_client.configuration import Configuration


class DockerImage(object):
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
        'repo_tags': 'list[str]',
        'repo_digests': 'list[str]',
        'parent': 'str',
        'comment': 'str',
        'created': 'str',
        'container': 'str',
        'container_config': 'DockerContainerConfig',
        'docker_version': 'str',
        'author': 'str',
        'config': 'DockerContainerConfig',
        'architecture': 'str',
        'os': 'str',
        'os_version': 'str',
        'size': 'int',
        'virtual_size': 'int',
        'graph_driver': 'DockerGraphDriverData',
        'root_fs': 'DockerImageRootFS',
        'metadata': 'DockerImageMetadata'
    }

    attribute_map = {
        'id': 'Id',
        'repo_tags': 'RepoTags',
        'repo_digests': 'RepoDigests',
        'parent': 'Parent',
        'comment': 'Comment',
        'created': 'Created',
        'container': 'Container',
        'container_config': 'ContainerConfig',
        'docker_version': 'DockerVersion',
        'author': 'Author',
        'config': 'Config',
        'architecture': 'Architecture',
        'os': 'Os',
        'os_version': 'OsVersion',
        'size': 'Size',
        'virtual_size': 'VirtualSize',
        'graph_driver': 'GraphDriver',
        'root_fs': 'RootFS',
        'metadata': 'Metadata'
    }

    def __init__(self, id=None, repo_tags=None, repo_digests=None, parent=None, comment=None, created=None, container=None, container_config=None, docker_version=None, author=None, config=None, architecture=None, os=None, os_version=None, size=None, virtual_size=None, graph_driver=None, root_fs=None, metadata=None, local_vars_configuration=None):  # noqa: E501
        """DockerImage - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._repo_tags = None
        self._repo_digests = None
        self._parent = None
        self._comment = None
        self._created = None
        self._container = None
        self._container_config = None
        self._docker_version = None
        self._author = None
        self._config = None
        self._architecture = None
        self._os = None
        self._os_version = None
        self._size = None
        self._virtual_size = None
        self._graph_driver = None
        self._root_fs = None
        self._metadata = None
        self.discriminator = None

        self.id = id
        if repo_tags is not None:
            self.repo_tags = repo_tags
        if repo_digests is not None:
            self.repo_digests = repo_digests
        self.parent = parent
        self.comment = comment
        self.created = created
        self.container = container
        if container_config is not None:
            self.container_config = container_config
        self.docker_version = docker_version
        self.author = author
        if config is not None:
            self.config = config
        self.architecture = architecture
        self.os = os
        if os_version is not None:
            self.os_version = os_version
        self.size = size
        self.virtual_size = virtual_size
        self.graph_driver = graph_driver
        self.root_fs = root_fs
        if metadata is not None:
            self.metadata = metadata

    @property
    def id(self):
        """Gets the id of this DockerImage.  # noqa: E501


        :return: The id of this DockerImage.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DockerImage.


        :param id: The id of this DockerImage.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def repo_tags(self):
        """Gets the repo_tags of this DockerImage.  # noqa: E501


        :return: The repo_tags of this DockerImage.  # noqa: E501
        :rtype: list[str]
        """
        return self._repo_tags

    @repo_tags.setter
    def repo_tags(self, repo_tags):
        """Sets the repo_tags of this DockerImage.


        :param repo_tags: The repo_tags of this DockerImage.  # noqa: E501
        :type: list[str]
        """

        self._repo_tags = repo_tags

    @property
    def repo_digests(self):
        """Gets the repo_digests of this DockerImage.  # noqa: E501


        :return: The repo_digests of this DockerImage.  # noqa: E501
        :rtype: list[str]
        """
        return self._repo_digests

    @repo_digests.setter
    def repo_digests(self, repo_digests):
        """Sets the repo_digests of this DockerImage.


        :param repo_digests: The repo_digests of this DockerImage.  # noqa: E501
        :type: list[str]
        """

        self._repo_digests = repo_digests

    @property
    def parent(self):
        """Gets the parent of this DockerImage.  # noqa: E501


        :return: The parent of this DockerImage.  # noqa: E501
        :rtype: str
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this DockerImage.


        :param parent: The parent of this DockerImage.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and parent is None:  # noqa: E501
            raise ValueError("Invalid value for `parent`, must not be `None`")  # noqa: E501

        self._parent = parent

    @property
    def comment(self):
        """Gets the comment of this DockerImage.  # noqa: E501


        :return: The comment of this DockerImage.  # noqa: E501
        :rtype: str
        """
        return self._comment

    @comment.setter
    def comment(self, comment):
        """Sets the comment of this DockerImage.


        :param comment: The comment of this DockerImage.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and comment is None:  # noqa: E501
            raise ValueError("Invalid value for `comment`, must not be `None`")  # noqa: E501

        self._comment = comment

    @property
    def created(self):
        """Gets the created of this DockerImage.  # noqa: E501


        :return: The created of this DockerImage.  # noqa: E501
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this DockerImage.


        :param created: The created of this DockerImage.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and created is None:  # noqa: E501
            raise ValueError("Invalid value for `created`, must not be `None`")  # noqa: E501

        self._created = created

    @property
    def container(self):
        """Gets the container of this DockerImage.  # noqa: E501


        :return: The container of this DockerImage.  # noqa: E501
        :rtype: str
        """
        return self._container

    @container.setter
    def container(self, container):
        """Sets the container of this DockerImage.


        :param container: The container of this DockerImage.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and container is None:  # noqa: E501
            raise ValueError("Invalid value for `container`, must not be `None`")  # noqa: E501

        self._container = container

    @property
    def container_config(self):
        """Gets the container_config of this DockerImage.  # noqa: E501


        :return: The container_config of this DockerImage.  # noqa: E501
        :rtype: DockerContainerConfig
        """
        return self._container_config

    @container_config.setter
    def container_config(self, container_config):
        """Sets the container_config of this DockerImage.


        :param container_config: The container_config of this DockerImage.  # noqa: E501
        :type: DockerContainerConfig
        """

        self._container_config = container_config

    @property
    def docker_version(self):
        """Gets the docker_version of this DockerImage.  # noqa: E501


        :return: The docker_version of this DockerImage.  # noqa: E501
        :rtype: str
        """
        return self._docker_version

    @docker_version.setter
    def docker_version(self, docker_version):
        """Sets the docker_version of this DockerImage.


        :param docker_version: The docker_version of this DockerImage.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and docker_version is None:  # noqa: E501
            raise ValueError("Invalid value for `docker_version`, must not be `None`")  # noqa: E501

        self._docker_version = docker_version

    @property
    def author(self):
        """Gets the author of this DockerImage.  # noqa: E501


        :return: The author of this DockerImage.  # noqa: E501
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this DockerImage.


        :param author: The author of this DockerImage.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and author is None:  # noqa: E501
            raise ValueError("Invalid value for `author`, must not be `None`")  # noqa: E501

        self._author = author

    @property
    def config(self):
        """Gets the config of this DockerImage.  # noqa: E501


        :return: The config of this DockerImage.  # noqa: E501
        :rtype: DockerContainerConfig
        """
        return self._config

    @config.setter
    def config(self, config):
        """Sets the config of this DockerImage.


        :param config: The config of this DockerImage.  # noqa: E501
        :type: DockerContainerConfig
        """

        self._config = config

    @property
    def architecture(self):
        """Gets the architecture of this DockerImage.  # noqa: E501


        :return: The architecture of this DockerImage.  # noqa: E501
        :rtype: str
        """
        return self._architecture

    @architecture.setter
    def architecture(self, architecture):
        """Sets the architecture of this DockerImage.


        :param architecture: The architecture of this DockerImage.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and architecture is None:  # noqa: E501
            raise ValueError("Invalid value for `architecture`, must not be `None`")  # noqa: E501

        self._architecture = architecture

    @property
    def os(self):
        """Gets the os of this DockerImage.  # noqa: E501


        :return: The os of this DockerImage.  # noqa: E501
        :rtype: str
        """
        return self._os

    @os.setter
    def os(self, os):
        """Sets the os of this DockerImage.


        :param os: The os of this DockerImage.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and os is None:  # noqa: E501
            raise ValueError("Invalid value for `os`, must not be `None`")  # noqa: E501

        self._os = os

    @property
    def os_version(self):
        """Gets the os_version of this DockerImage.  # noqa: E501


        :return: The os_version of this DockerImage.  # noqa: E501
        :rtype: str
        """
        return self._os_version

    @os_version.setter
    def os_version(self, os_version):
        """Sets the os_version of this DockerImage.


        :param os_version: The os_version of this DockerImage.  # noqa: E501
        :type: str
        """

        self._os_version = os_version

    @property
    def size(self):
        """Gets the size of this DockerImage.  # noqa: E501


        :return: The size of this DockerImage.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this DockerImage.


        :param size: The size of this DockerImage.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and size is None:  # noqa: E501
            raise ValueError("Invalid value for `size`, must not be `None`")  # noqa: E501

        self._size = size

    @property
    def virtual_size(self):
        """Gets the virtual_size of this DockerImage.  # noqa: E501


        :return: The virtual_size of this DockerImage.  # noqa: E501
        :rtype: int
        """
        return self._virtual_size

    @virtual_size.setter
    def virtual_size(self, virtual_size):
        """Sets the virtual_size of this DockerImage.


        :param virtual_size: The virtual_size of this DockerImage.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and virtual_size is None:  # noqa: E501
            raise ValueError("Invalid value for `virtual_size`, must not be `None`")  # noqa: E501

        self._virtual_size = virtual_size

    @property
    def graph_driver(self):
        """Gets the graph_driver of this DockerImage.  # noqa: E501


        :return: The graph_driver of this DockerImage.  # noqa: E501
        :rtype: DockerGraphDriverData
        """
        return self._graph_driver

    @graph_driver.setter
    def graph_driver(self, graph_driver):
        """Sets the graph_driver of this DockerImage.


        :param graph_driver: The graph_driver of this DockerImage.  # noqa: E501
        :type: DockerGraphDriverData
        """
        if self.local_vars_configuration.client_side_validation and graph_driver is None:  # noqa: E501
            raise ValueError("Invalid value for `graph_driver`, must not be `None`")  # noqa: E501

        self._graph_driver = graph_driver

    @property
    def root_fs(self):
        """Gets the root_fs of this DockerImage.  # noqa: E501


        :return: The root_fs of this DockerImage.  # noqa: E501
        :rtype: DockerImageRootFS
        """
        return self._root_fs

    @root_fs.setter
    def root_fs(self, root_fs):
        """Sets the root_fs of this DockerImage.


        :param root_fs: The root_fs of this DockerImage.  # noqa: E501
        :type: DockerImageRootFS
        """
        if self.local_vars_configuration.client_side_validation and root_fs is None:  # noqa: E501
            raise ValueError("Invalid value for `root_fs`, must not be `None`")  # noqa: E501

        self._root_fs = root_fs

    @property
    def metadata(self):
        """Gets the metadata of this DockerImage.  # noqa: E501


        :return: The metadata of this DockerImage.  # noqa: E501
        :rtype: DockerImageMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this DockerImage.


        :param metadata: The metadata of this DockerImage.  # noqa: E501
        :type: DockerImageMetadata
        """

        self._metadata = metadata

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
        if not isinstance(other, DockerImage):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DockerImage):
            return True

        return self.to_dict() != other.to_dict()
