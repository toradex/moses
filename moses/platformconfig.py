"""Classes used to manage platforms.

Platforms define containers that will run on a device.
"""
import config
import logging
from pathlib import Path
import singleton
import targetdevice
import exceptions
import eula
from typing import Optional, List, Dict, Any


class PlatformConfig(config.ConfigurableObject):
    """Class used to manage a platform."""

    def __init__(self, folder: Path = None, standard: bool = False) -> None:
        """Load data from a configuration folder.

        :param folder: Path of the folder used to store configuration
        :type folder: pathlib.Path

        :param standard: True if the plaform is provided by Toradex as part of default setup
        :type standard: bool

        """
        super().__init__(folder)

        self.standard = standard
        self.version = ""
        self.name = ""
        self.description = ""
        self.usesysroots = False
        self.usesdk = False
        self.supportedmodels = ["*"]
        self.unsupportedmodels: List[str] = []
        self.container = {"common": None, "debug": None, "release": None}

        self.baseimage = {"common": None, "debug": None, "release": None}

        self.sdkcontainer: Dict[str, Optional[str]] = {
            "common": None,
            "debug": None,
            "release": None,
        }

        self.sdkbaseimage = {"common": None, "debug": None, "release": None}
        self.sdkcontainerusername = "build"
        self.sdkcontainerpassword = "build"

        self.privileged = False
        self.ports: Dict[str, Dict[str, str]] = {
            "common": {},
            "debug": {},
            "release": {},
        }
        self.volumes: Dict[str, Dict[str, str]] = {
            "common": {},
            "debug": {},
            "release": {},
        }
        self.devices: Dict[str, List[str]] = {"common": [], "debug": [], "release": []}

        self.extraparms: Dict[str, Dict[str, Any]] = {
            "common": {},
            "debug": {},
            "release": {},
        }

        self.dockercompose: Dict[str, Optional[str]] = {
            "common": None,
            "debug": None,
            "release": None,
        }

        self.startupscript: Dict[str, Optional[str]] = {
            "common": None,
            "debug": None,
            "release": None,
        }

        self.shutdownscript: Dict[str, Optional[str]] = {
            "common": None,
            "debug": None,
            "release": None,
        }

        self.props: Dict[str, Dict[str, str]] = {
            "common": {},
            "debug": {},
            "release": {},
        }

        self.runtimes: List[str] = []

        self.networks: Dict[str, List[str]] = {"common": [], "debug": [], "release": []}

        self.tags: List[str] = []
        self.eulas: List[str] = []
        self.disabled = False
        self.architecture = ""
        self.deprecated = False

        if self.folder is not None:
            self.load()

    def _build_folder_path(self) -> Path:
        """Create a folder path concatenating base folder and the platform id."""
        assert self.id is not None
        if not self.standard:
            return config.ServerConfig().platformspath / self.id
        else:
            return config.ServerConfig().standardplatformspath / self.id

    def destroy(self) -> None:
        """Remove the platform (can't be done on standard ones)."""
        if self.standard:
            raise Exception("Can't delete a standard platform.")
        super().destroy()

    def save(self) -> None:
        """Save object data."""
        if self.standard:
            raise Exception("Can't overwrite a standard platform.")

        super().save()

    def is_valid(self, fields: dict = None) -> bool:
        """Validate the fields of current object.

        :param fields: object properties as a dictionary, if None is passed then self.__dict__ is used
        :type fields: dict
        :returns: true if all fields contain valid values
        :rtype: bool

        """
        if fields is None:
            fields = self.__dict__

        if (
            fields["container"]["common"] is None
            and fields["container"]["release"] is None
        ):
            logging.error("Release container not defined in plaform %s.", self.id)
            return False

        if (
            fields["container"]["common"] is None
            and fields["container"]["debug"] is None
        ):
            logging.error("Debug container not defined in plaform %s.", self.id)
            return False

        if fields["usesdk"]:

            if (
                fields["sdkbaseimage"]["common"] is None
                and fields["sdkbaseimage"]["release"] is None
            ):
                logging.error(
                    "Release sdk base image not defined in plaform %s.", self.id
                )
                return False

            if (
                fields["sdkbaseimage"]["common"] is None
                and fields["sdkbaseimage"]["debug"] is None
            ):
                logging.error(
                    "Debug sdk base image not defined in plaform %s.", self.id
                )
                return False

            if fields["usesysroot"]:
                logging.error("sysroots are no longer supported by the ide-backend.")
                return False
            else:
                if (
                    fields["sdkcontainer"]["common"] is None
                    and fields["sdkcontainer"]["release"] is None
                ):
                    logging.error(
                        "Release sdk container not defined in plaform %s.", self.id
                    )
                    return False

                if (
                    fields["sdkcontainer"]["common"] is None
                    and fields["sdkcontainer"]["debug"] is None
                ):
                    logging.error(
                        "Debug sdk container not defined in plaform %s.", self.id
                    )
                    return False

        return True

    def supports_model(self, model: str) -> bool:
        """Check if this platform support a specific HW model.

        :param model: Toradex model code
        :type model: str
        :returns: true if model is supported
        :rtype: bool

        """
        if model in self.unsupportedmodels:
            return False

        if "*" in self.supportedmodels:
            return True

        return model in self.supportedmodels

    def get_prop(self, configuration: str, prop: str) -> Optional[str]:
        """Return value for a base property.

        If there is a configuration-specific value, it's returned, otherwise the function
        checks for a common value, if even this one has not been configured, then it will
        return None.

        :param configuration: debug/release
        :type configuration: str
        :param prop: property name
        :type prop: str
        :returns: property value or None
        :rtype: str | None

        """
        if not prop in self.__dict__:
            return None

        # those properties are used to generate a tag
        if prop == "baseimage" or prop == "sdkbaseimage":
            if self.__dict__[prop][configuration] is not None:
                return ":".join(self.__dict__[prop][configuration])
            if self.__dict__[prop]["common"] is not None:
                return ":".join(self.__dict__[prop]["common"])

        if isinstance(self.__dict__[prop], dict):
            if self.__dict__[prop][configuration] is not None:
                return str(self.__dict__[prop][configuration])
            if self.__dict__[prop]["common"] is not None:
                return str(self.__dict__[prop]["common"])
        else:
            return str(self.__dict__[prop])
        return None

    def get_custom_prop(self, configuration: str, property: str) -> Optional[str]:
        """Return value for a custom property.

        If there is a configuration-specific value, it's returned, otherwise the function
        checks for a common value, if even this one has not been configured, then it will
        return None.

        :param configuration: debug/release
        :type configuration: str
        :param prop: property name
        :type prop: str
        :returns: property value or None
        :rtype: str | None

        """
        if property in self.props[configuration]:
            return str(self.props[configuration][property])
        if property in self.props["common"]:
            return str(self.props["common"][property])
        return None

    def _get_value(self, obj: str, tag: str, configuration: str) -> str:
        """Return value for a tag checking base and custom properties.

        This function is used to replace values in templates.

        :param obj: object name, must be "platform"
        :type obj: str
        :param tag: tag name
        :type tag: str
        :param configuration: debug/release
        :type configuration: str
        :param obj: str:
        :returns: value of the tag or empty string

        """
        if obj != "platform":
            return ""

        value = self.get_custom_prop(configuration, tag)

        if value is None:
            value = self.get_prop(configuration, tag)

        if value is None:
            if tag in self.__dict__:
                value = str(self.__dict__[tag])
            else:
                value = ""

        return value

    def check_device_compatibility(self, device: targetdevice.TargetDevice) -> bool:
        """Check if a device is compatible with this platform.

        :param device: target device
        :type device: targetdevice.TargetDevice
        :returns: true is device is compatible
        :rtype: bool

        """
        if device.model in self.supportedmodels:
            return True

        if device.model in self.unsupportedmodels:
            return False

        if "*" in self.supportedmodels:
            return True

        return False

    def get_compatible_devices(self) -> List[targetdevice.TargetDevice]:
        """Return a list of devices that are compabile with the platform.

        :returns: list of devices that are compatible with this platform
        :rtype: List[targetdevice.TargetDevice]

        """
        return [
            d
            for d in targetdevice.TargetDevices().values()
            if self.check_device_compatibility(d)
        ]


class PlatformConfigs(Dict[str, PlatformConfig], metaclass=singleton.Singleton):
    """Class used to manage the collection of platforms."""

    def __init__(self) -> None:
        """Enumerate platforms in the different folders and load them."""
        path = config.ServerConfig().standardplatformspath

        subfolders = [dir for dir in path.iterdir() if dir.is_dir()]

        for dir in subfolders:
            try:
                plat = PlatformConfig(dir, True)
                assert plat.id is not None
                self[plat.id] = plat
            except Exception as e:
                logging.exception(
                    "Can't create platform from folder %s." "Error: %s",
                    str(dir),
                    str(e),
                )

        path = config.ServerConfig().platformspath

        subfolders = [dir for dir in path.iterdir() if dir.is_dir()]

        for dir in subfolders:
            try:
                plat = PlatformConfig(dir, False)
                assert plat.id is not None
                self[plat.id] = plat
            except:
                logging.exception("Can't create platform from folder %s.", str(dir))

    def __delitem__(self, platform_id: str) -> None:
        """Remove a platform given its id.

        :param platform_id: platform id
        :type platform_id: str

        """
        if platform_id not in self:
            return

        self[platform_id].destroy()
        dict.__delitem__(self, platform_id)

    def get_platform(self, platform_id: str) -> PlatformConfig:
        """Return a platform given its id.

        :param platform_id: platform id
        :type platform_id: str
        :returns: plaform object
        :rtype: PlatformConfig

        """
        if platform_id not in self:
            raise exceptions.PlatformDoesNotExistError(platform_id)

        return self[platform_id]

    def get_platforms(self, runtime: Optional[str]) -> List[PlatformConfig]:
        """Return a list of plaforms supporting a specific runtime.

        Platform that require an EULA won't be returned if the Eula hasn't been accepted

        :param runtime: required runtime or None to get full list of platforms
        :type runtime: str, optional
        :returns: list of platform objects
        :rtype: List[PlatformConfig]

        """
        platformslist = []
        eulas = eula.EULAs()

        for plat in self.values():

            if plat.disabled:
                continue

            eulaaccepted = True

            for e in plat.eulas:
                if e in eulas:
                    if not eulas[e].accepted:
                        logging.warning(
                            "Platform %s can't be used because EULA %s has not been accepted.",
                            plat.id,
                            e,
                        )
                        eulaaccepted = False
                        break

            if not eulaaccepted:
                continue

            if runtime is not None:
                if runtime not in plat.runtimes:
                    continue

            platformslist.append(plat)

        return platformslist
