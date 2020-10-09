"""Classes used to manage platforms. Platforms define containers
that will run on a device.
"""
import config
import shutil
import logging
from pathlib import Path
import singleton
import targetdevice
import exceptions
import eula
from typing import Optional, List, Dict


class PlatformConfig(config.ConfigurableObject):
    """Class used to manage a platform
    """

    def __init__(self, folder=None, standard=False):
        """Loads data from a configuration folder

        Arguments:
            folder {Path} -- Path of the folder used to store
                             target information
            standard {bool} -- true if the platform is a standard
                               one provided directly by toradex

        """
        super().__init__(folder)

        self.standard = standard
        self.version = ""
        self.name = ""
        self.description = ""
        self.usesysroots = False
        self.sysroots: Dict[str, List[str]] = None
        self.sdkcontainer: Optional[str] = None
        self.usesdk = False
        self.supportedmodels = ["*"]
        self.unsupportedmodels = []
        self.container = {"common": None, "debug": None, "release": None}

        self.baseimage = {"common": None, "debug": None, "release": None}

        self.sdkcontainer = {"common": None, "debug": None, "release": None}

        self.sdkbaseimage = {"common": None, "debug": None, "release": None}
        self.sdkcontainerusername = "build"
        self.sdkcontainerpassword = "build"

        self.privileged = False
        self.ports = {"common": {}, "debug": {}, "release": {}}
        self.volumes = {"common": {}, "debug": {}, "release": {}}
        self.devices = {"common": [], "debug": [], "release": []}

        self.extraparms = {"common": {}, "debug": {}, "release": {}}

        self.dockercompose = {"common": None, "debug": None, "release": None}

        self.startupscript = {"common": None, "debug": None, "release": None}

        self.shutdownscript = {"common": None, "debug": None, "release": None}

        self.props = {"common": {}, "debug": {}, "release": {}}

        self.runtimes = []

        self.networks = {"common": [], "debug": [], "release": []}

        self.tags = []
        self.eulas = []
        self.disabled = False
        self.architecture = ""

        if self.folder is not None:
            self.load()

    def _build_folder_path(self) -> Path:
        if not self.standard:
            return config.ServerConfig().platformspath / self.id
        else:
            return config.ServerConfig().standardplatformspath / self.id

    def destroy(self):
        if self.standard:
            raise Exception("Can't delete a standard platform.")
        super().destroy()

    def save(self):
        """Save object data
        """

        if self.standard:
            raise Exception("Can't overwrite a standard platform.")

        super().save()

    def is_valid(self, fields: dict = None) -> bool:
        """Validate fields of current object

        Arguments:
            fields {dictionary} -- dictionary with values, if None then
                                   self.__dict__ will be used

        Returns:
            bool -- true if all fields contain valid values
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
                if fields["sysroots"] is None or type(fields["sysroots"]) is not dict:
                    return False

                for k in fields["sysroots"].keys():
                    if fields["sysroots"][k] is None or len(fields["sysroots"][k]) == 0:
                        fields["sysroots"][k] = ["/"]
                    else:
                        for r in fields["sysroots"][k]:
                            if not r.startswith("/"):
                                logging.error(
                                    "Platform sysroots must be absolute paths in plaform %s.",
                                    self.id,
                                )
                                return False

                    fields["sysroots"][k] = list(
                        map(
                            lambda r: r[:-1] if r.endswith("/") else r,
                            fields["sysroots"][k],
                        )
                    )
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
        """Checks if this platform support a specific HW model

        Arguments:
            model {str} -- Model code (ex: 0028)

        Returns:
            bool -- [description]
        """
        if model in self.unsupportedmodels:
            return False

        if "*" in self.supportedmodels:
            return True

        return model in self.supportedmodels

    def get_prop(self, configuration: str, prop: str) -> Optional[str]:
        """Return configuration-specific property or common one
        if the specific one is not available

        Arguments:
            configuration {str} -- debug/release
            prop {str} -- property
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

    def get_custom_prop(self, configuration: str, property: str):
        if property in self.props[configuration]:
            return str(self.props[configuration][property])
        if property in self.props["common"]:
            return str(self.props["common"][property])
        return None

    def _get_value(self, obj: str, tag: str, configuration: str) -> str:
        """Returns value for a tag in the format application/platform.tag

        Arguments:
            obj {str} -- application/platform
            tag {str} -- tag
            configuration {str} -- active configuration

        Returns:
            str -- value of the tag or empty string
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
        """Checks if a device is compatible with this platform

        Arguments:
            device {targetdevice.TargetDevice} -- device

        Returns:
            bool -- true is device is compatible
        """

        if device.model in self.supportedmodels:
            return True

        if device.model in self.unsupportedmodels:
            return False

        if "*" in self.supportedmodels:
            return True

        return False

    def get_compatible_devices(self) -> List[targetdevice.TargetDevice]:
        """Returns a list of devices that are compabile with the platform

        Returns:
            list -- list of targetdevice.TargetDevice objects
        """
        return [
            d
            for d in targetdevice.TargetDevices().values()
            if self.check_device_compatibility(d)
        ]


class PlatformConfigs(Dict[str, PlatformConfig], metaclass=singleton.Singleton):
    """Class used to manage the collection of platforms
    """

    def __init__(self):
        """ Iterates on all platforms in standard and custom folders
        """
        path = config.ServerConfig().standardplatformspath

        subfolders = [dir for dir in path.iterdir() if dir.is_dir()]

        for dir in subfolders:
            try:
                plat = PlatformConfig(dir, True)
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
                self[plat.id] = plat
            except:
                logging.exception("Can't create platform from folder %s.", str(dir))

    def __delitem__(self, key: str):
        """Removes a platform given its id

        Args:
            key (str): id
        """
        if key not in self:
            return

        self[key].destroy()
        dict.__delitem__(self, key)

    def get_platform(self, platformid: str) -> PlatformConfig:
        """Returns a platform give its id

        Args:
            platformid (str): id

        Raises:
            exceptions.PlatformDoesNotExistError: [description]

        Returns:
            PlatformConfig: [description]
        """
        if platformid not in self:
            raise exceptions.PlatformDoesNotExistError(platformid)

        return self[platformid]

    def get_platforms(self, runtime: Optional[str]) -> List[PlatformConfig]:
        """Return a list of plaforms supporting a specific runtime

        Arguments:
            runtime {str} -- runtime or None for no filtering

        Returns:
            list -- list of platforms
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
