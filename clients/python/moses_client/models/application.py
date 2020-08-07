# coding: utf-8

"""
    Torizon IDE-backend API

    Toradex API to build and deploy applications running as containers on Torizon  # noqa: E501

    The version of the OpenAPI document: 1.0.7
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from moses_client.configuration import Configuration


class Application(object):
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
        'platformid': 'str',
        'folder': 'str',
        'props': 'dict(str, dict(str, str))',
        'dockercomposefile': 'dict(str, str)',
        'startupscript': 'dict(str, str)',
        'shutdownscript': 'dict(str, str)',
        'ports': 'dict(str, dict(str, str))',
        'volumes': 'dict(str, dict(str, str))',
        'devices': 'dict(str, list[str])',
        'networks': 'dict(str, list[str])',
        'extraparms': 'dict(str, dict(str, str))',
        'username': 'str',
        'images': 'dict(str, str)',
        'sdkimages': 'dict(str, str)'
    }

    attribute_map = {
        'id': 'id',
        'platformid': 'platformid',
        'folder': 'folder',
        'props': 'props',
        'dockercomposefile': 'dockercomposefile',
        'startupscript': 'startupscript',
        'shutdownscript': 'shutdownscript',
        'ports': 'ports',
        'volumes': 'volumes',
        'devices': 'devices',
        'networks': 'networks',
        'extraparms': 'extraparms',
        'username': 'username',
        'images': 'images',
        'sdkimages': 'sdkimages'
    }

    def __init__(self, id=None, platformid=None, folder=None, props=None, dockercomposefile=None, startupscript=None, shutdownscript=None, ports=None, volumes=None, devices=None, networks=None, extraparms=None, username=None, images=None, sdkimages=None, local_vars_configuration=None):  # noqa: E501
        """Application - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._platformid = None
        self._folder = None
        self._props = None
        self._dockercomposefile = None
        self._startupscript = None
        self._shutdownscript = None
        self._ports = None
        self._volumes = None
        self._devices = None
        self._networks = None
        self._extraparms = None
        self._username = None
        self._images = None
        self._sdkimages = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if platformid is not None:
            self.platformid = platformid
        if folder is not None:
            self.folder = folder
        if props is not None:
            self.props = props
        if dockercomposefile is not None:
            self.dockercomposefile = dockercomposefile
        if startupscript is not None:
            self.startupscript = startupscript
        if shutdownscript is not None:
            self.shutdownscript = shutdownscript
        if ports is not None:
            self.ports = ports
        if volumes is not None:
            self.volumes = volumes
        if devices is not None:
            self.devices = devices
        if networks is not None:
            self.networks = networks
        if extraparms is not None:
            self.extraparms = extraparms
        if username is not None:
            self.username = username
        if images is not None:
            self.images = images
        if sdkimages is not None:
            self.sdkimages = sdkimages

    @property
    def id(self):
        """Gets the id of this Application.  # noqa: E501

        Unique id  # noqa: E501

        :return: The id of this Application.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Application.

        Unique id  # noqa: E501

        :param id: The id of this Application.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def platformid(self):
        """Gets the platformid of this Application.  # noqa: E501

        id of the platform used to generate this application configuration  # noqa: E501

        :return: The platformid of this Application.  # noqa: E501
        :rtype: str
        """
        return self._platformid

    @platformid.setter
    def platformid(self, platformid):
        """Sets the platformid of this Application.

        id of the platform used to generate this application configuration  # noqa: E501

        :param platformid: The platformid of this Application.  # noqa: E501
        :type platformid: str
        """

        self._platformid = platformid

    @property
    def folder(self):
        """Gets the folder of this Application.  # noqa: E501

        folder where application configuration and extra files are stored  # noqa: E501

        :return: The folder of this Application.  # noqa: E501
        :rtype: str
        """
        return self._folder

    @folder.setter
    def folder(self, folder):
        """Sets the folder of this Application.

        folder where application configuration and extra files are stored  # noqa: E501

        :param folder: The folder of this Application.  # noqa: E501
        :type folder: str
        """

        self._folder = folder

    @property
    def props(self):
        """Gets the props of this Application.  # noqa: E501

        Custom application properties  # noqa: E501

        :return: The props of this Application.  # noqa: E501
        :rtype: dict(str, dict(str, str))
        """
        return self._props

    @props.setter
    def props(self, props):
        """Sets the props of this Application.

        Custom application properties  # noqa: E501

        :param props: The props of this Application.  # noqa: E501
        :type props: dict(str, dict(str, str))
        """

        self._props = props

    @property
    def dockercomposefile(self):
        """Gets the dockercomposefile of this Application.  # noqa: E501

        path of docker-compose file to be used to start additional containers needed by the app  # noqa: E501

        :return: The dockercomposefile of this Application.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._dockercomposefile

    @dockercomposefile.setter
    def dockercomposefile(self, dockercomposefile):
        """Sets the dockercomposefile of this Application.

        path of docker-compose file to be used to start additional containers needed by the app  # noqa: E501

        :param dockercomposefile: The dockercomposefile of this Application.  # noqa: E501
        :type dockercomposefile: dict(str, str)
        """

        self._dockercomposefile = dockercomposefile

    @property
    def startupscript(self):
        """Gets the startupscript of this Application.  # noqa: E501

        path of script to be run when application debugging starts  # noqa: E501

        :return: The startupscript of this Application.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._startupscript

    @startupscript.setter
    def startupscript(self, startupscript):
        """Sets the startupscript of this Application.

        path of script to be run when application debugging starts  # noqa: E501

        :param startupscript: The startupscript of this Application.  # noqa: E501
        :type startupscript: dict(str, str)
        """

        self._startupscript = startupscript

    @property
    def shutdownscript(self):
        """Gets the shutdownscript of this Application.  # noqa: E501

        path of script to be run when application debugging stops  # noqa: E501

        :return: The shutdownscript of this Application.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._shutdownscript

    @shutdownscript.setter
    def shutdownscript(self, shutdownscript):
        """Sets the shutdownscript of this Application.

        path of script to be run when application debugging stops  # noqa: E501

        :param shutdownscript: The shutdownscript of this Application.  # noqa: E501
        :type shutdownscript: dict(str, str)
        """

        self._shutdownscript = shutdownscript

    @property
    def ports(self):
        """Gets the ports of this Application.  # noqa: E501

        ports to be exposed from the container  # noqa: E501

        :return: The ports of this Application.  # noqa: E501
        :rtype: dict(str, dict(str, str))
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        """Sets the ports of this Application.

        ports to be exposed from the container  # noqa: E501

        :param ports: The ports of this Application.  # noqa: E501
        :type ports: dict(str, dict(str, str))
        """

        self._ports = ports

    @property
    def volumes(self):
        """Gets the volumes of this Application.  # noqa: E501

        Local folders to be mounted \"A mount points inside a container  # noqa: E501

        :return: The volumes of this Application.  # noqa: E501
        :rtype: dict(str, dict(str, str))
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        """Sets the volumes of this Application.

        Local folders to be mounted \"A mount points inside a container  # noqa: E501

        :param volumes: The volumes of this Application.  # noqa: E501
        :type volumes: dict(str, dict(str, str))
        """

        self._volumes = volumes

    @property
    def devices(self):
        """Gets the devices of this Application.  # noqa: E501

        Additional devices to be shared inside container  # noqa: E501

        :return: The devices of this Application.  # noqa: E501
        :rtype: dict(str, list[str])
        """
        return self._devices

    @devices.setter
    def devices(self, devices):
        """Sets the devices of this Application.

        Additional devices to be shared inside container  # noqa: E501

        :param devices: The devices of this Application.  # noqa: E501
        :type devices: dict(str, list[str])
        """

        self._devices = devices

    @property
    def networks(self):
        """Gets the networks of this Application.  # noqa: E501

        Networks used by container (in debug it will always be also on bridge)  # noqa: E501

        :return: The networks of this Application.  # noqa: E501
        :rtype: dict(str, list[str])
        """
        return self._networks

    @networks.setter
    def networks(self, networks):
        """Sets the networks of this Application.

        Networks used by container (in debug it will always be also on bridge)  # noqa: E501

        :param networks: The networks of this Application.  # noqa: E501
        :type networks: dict(str, list[str])
        """

        self._networks = networks

    @property
    def extraparms(self):
        """Gets the extraparms of this Application.  # noqa: E501

        Additional parameter passed to the run call (check docker SDK for python for reference, value is YAML)  # noqa: E501

        :return: The extraparms of this Application.  # noqa: E501
        :rtype: dict(str, dict(str, str))
        """
        return self._extraparms

    @extraparms.setter
    def extraparms(self, extraparms):
        """Sets the extraparms of this Application.

        Additional parameter passed to the run call (check docker SDK for python for reference, value is YAML)  # noqa: E501

        :param extraparms: The extraparms of this Application.  # noqa: E501
        :type extraparms: dict(str, dict(str, str))
        """

        self._extraparms = extraparms

    @property
    def username(self):
        """Gets the username of this Application.  # noqa: E501

        user account used to run the application inside the container  # noqa: E501

        :return: The username of this Application.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this Application.

        user account used to run the application inside the container  # noqa: E501

        :param username: The username of this Application.  # noqa: E501
        :type username: str
        """

        self._username = username

    @property
    def images(self):
        """Gets the images of this Application.  # noqa: E501

        SHA-ids of the debug and release images  # noqa: E501

        :return: The images of this Application.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._images

    @images.setter
    def images(self, images):
        """Sets the images of this Application.

        SHA-ids of the debug and release images  # noqa: E501

        :param images: The images of this Application.  # noqa: E501
        :type images: dict(str, str)
        """

        self._images = images

    @property
    def sdkimages(self):
        """Gets the sdkimages of this Application.  # noqa: E501

        SHA-ids of the debug and release SDK images  # noqa: E501

        :return: The sdkimages of this Application.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._sdkimages

    @sdkimages.setter
    def sdkimages(self, sdkimages):
        """Sets the sdkimages of this Application.

        SHA-ids of the debug and release SDK images  # noqa: E501

        :param sdkimages: The sdkimages of this Application.  # noqa: E501
        :type sdkimages: dict(str, str)
        """

        self._sdkimages = sdkimages

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
        if not isinstance(other, Application):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Application):
            return True

        return self.to_dict() != other.to_dict()
