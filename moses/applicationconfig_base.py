"""Base class for application configuration.

ApplicationConfig clas was getting too big, it had to be splitted between multiple files,
depending of features. To ensure validation and coherency, data members and base features
have been extported into a base class, implemented here
"""
import os
import logging
import uuid
import datetime
from pathlib import Path
from typing import Optional, Dict, Any, Callable, Mapping
import docker
import docker.models.containers
import config
import properties
import platformconfig
import tags


# pylint: disable=too-many-instance-attributes
class ApplicationConfigBase(
        config.ConfigurableKeysObject, properties.PropertiesObject):
    """Class used to manage an application."""

    readonlyfields = config.ConfigurableKeysObject.readonlyfields.union(
        {"images", "sdkimages"}
    )

    publicfields: set = set()

    non_nullable_properties = [
        "dockercomposefile",
        "startupscript",
        "shutdownscript"]
    configurations = ["common", "debug", "release"]

    def __init__(self, folder: Optional[Path] = None):
        """Load data from the configuration folder.

        :param folder: path of the folder used to store application configuration
        :type folder: Path, optional

        """
        properties.PropertiesObject.__init__(self)
        config.ConfigurableKeysObject.__init__(self, folder)

        self.props.update({
            "common": {
                "expose": "",
                "arg": "",
                "env": "",
                "preinstallcommands": "",
                "extrapackages": "",
                "devpackages": "",
                "buildfiles": "",
                "buildcommands": "",
                "targetfiles": "",
                "targetcommands": "",
                "command": "",
                "sdkpreinstallcommands": "",
                "sdkpostinstallcommands": "",
            },
            "debug": {"arg": "ARG SSHUSERNAME=" "#%application.username%#\n"},
            "release": {},
        })

        self.images: Dict[str, str] = {"debug": "", "release": ""}

        self.sdkimages: Dict[str, str] = {"debug": "", "release": ""}

        self.platformid = ""
        self.publickey: Optional[str] = None
        self.privatekey: Optional[str] = None
        self.modificationdate = datetime.datetime.utcnow().isoformat()

        self.sdksshaddress: Optional[Dict[str, Any]] = None

        if self.folder is not None and self.folder.exists():
            self.load()
        else:
            self.id = str(uuid.uuid4())

        self.logs: Dict[str, Any] = {}

    def save(self) -> None:
        """Save object data."""
        if self.folder is None:
            return

        # we got a folder, but it may not be an existing one
        if not self.folder.exists():
            self.folder.mkdir()

        super().save()

    def load(self) -> None:
        """Load configuration from an existing folder.

        This will re-create keys and ids if those have been cleaned-up using the reseal function

        """
        super().load()

        if self.id == "00000000-0000-0000-0000-000000000000":
            self.id = str(uuid.uuid4())
            self.privatekey = None
            self.publickey = None
            self.save()

        localdocker = docker.from_env()

        for field in ["images", "sdkimages"]:
            for configuration in ["debug", "release"]:
                imgid = self.__dict__[field][configuration]

                if imgid is None or imgid == "":
                    continue

                try:
                    _ = localdocker.images.get(imgid)
                except docker.errors.ImageNotFound:
                    logging.error(f"Image {imgid} not found")
                    self.__dict__[field][configuration] = ""

    def _generate_keys(self) -> None:
        """Generate keys for SSH connectivity.

        The public key is also saved as regular file inside the configuration folder.add()

        """
        super()._generate_keys()

        assert self.folder is not None

        with open(str(self.folder / "id_rsa.pub"), "w") as keyfile:
            assert self.publickey is not None
            keyfile.write(self.publickey)

    def _build_folder_path(self) -> Path:
        """Build folder path (not implemented for applications)."""
        raise Exception("Application must have a defined base folder path.")

    def is_valid(self, fields: dict = None) -> bool:
        """Validate the fields of current object.

        :param fields: object properties as a dictionary, if None is passed
            then self.__dict__ is used
        :type fields: dict
        :returns: true if all fields contain valid values
        :rtype: bool

        """
        if fields is None:
            fields = self.__dict__

        if fields["platformid"] not in platformconfig.PlatformConfigs():
            logging.error(
                "Invalid platform id %s in application %s",
                fields["platformid"],
                self.folder,
            )
            return False

        # some properties can't be returned/set as null in the REST API
        for prop in ApplicationConfigBase.non_nullable_properties:
            for conf in ApplicationConfigBase.configurations:
                if fields[prop][conf] is None:
                    fields[prop][conf] = ""

        return True

    def __getstate__(self) -> Dict[str, Any]:
        """Return a dictionary with exported properties.

        :return: properties as a dictionary
        :rtype: Dict[str, Any]

        """
        # for applications we keep id in the serialized format
        fields = super().__getstate__()
        fields["id"] = self.id
        fields["sdksshaddress"] = self.sdksshaddress
        if "logs" in fields:
            del fields["logs"]
        return fields

    def to_json(self) -> Dict[str, Any]:
        """Convert object to an array of json-compatible key-value pairs.

        :return: properties as a dictionary
        :rtype: Dict[str, Any]

        """
        # we return also folder in json
        fields = super().to_json()
        fields["folder"] = str(self.folder)
        return fields

    def _merge_props(self, plat: platformconfig.PlatformConfig,
                     configuration: str, prop: str) -> Dict[str, Any]:
        """Merge common and configuration-specific values in dictionaries.

        This internal function is used to generate a single dictionary with
        values specified at different levels of configuration (plaform, application,
        common and configuration-specific)

        :param plat: platform
        :type plat: platformconfig.PlatformConfig
        :param configuration: debug/release
        :type configuration: str
        :param prop: property name
        :param prop: str
        :returns: merged dictionary
        :rtype: Dict[str,Any]

        """
        merged = plat.__dict__[prop]["common"].copy()
        merged.update(plat.__dict__[prop][configuration])
        merged.update(self.__dict__[prop]["common"])
        merged.update(self.__dict__[prop][configuration])

        for key, value in merged.items():
            if isinstance(value, str):
                newvalue = tags.replace_tags(
                    value,
                    self._get_value,
                    configuration,
                )
                if newvalue != value:
                    merged[key] = newvalue

        return merged

    def _append_props(self, plat: platformconfig.PlatformConfig,
                      configuration: str, prop: str) -> list:
        """Append values of a property from the different levels of configuration.

        The platform common one is taken first, then configuration
        is appended, then app common, then app configuration

        :param plat: platform
        :type plat: platformconfig.PlatformConfig
        :param configuration: debug/release
        :type configuration: str
        :param prop: property name
        :param prop: str
        :returns: merged values
        :rtype: list

        """
        merged = plat.__dict__[prop]["common"].copy()
        merged.extend(plat.__dict__[prop][configuration])
        merged.extend(self.__dict__[prop]["common"])
        merged.extend(self.__dict__[prop][configuration])

        return list(
            map(
                lambda i: i
                if not isinstance(i, str)
                else tags.replace_tags(
                    i,
                    self._get_value,
                    configuration,
                ),
                merged,
            )
        )

    def _get_prop(self, configuration: str, prop: str) -> Optional[str]:
        """Return a property depending on specific configuration.

        :param configuration: debug/release
        :type configuration: str
        :param prop: property name
        :type prop: str
        :returns: property value or None
        :rtype: str | None

        """
        if not prop in self.__dict__:
            return None

        if not isinstance(self.__dict__[prop], dict):
            return str(self.__dict__[prop])

        if (self.__dict__[prop][configuration] is not None) and not (
                prop in ApplicationConfigBase.non_nullable_properties and
                len(self.__dict__[prop][configuration]) == 0):
            return str(self.__dict__[prop][configuration])

        if (self.__dict__[prop]["common"] is not None) and not (
                prop in ApplicationConfigBase.non_nullable_properties and
                len(self.__dict__[prop]["common"]) == 0):
            return str(self.__dict__[prop]["common"])

        return None

    def _get_value(self, obj: str, tag: str, configuration: str) -> str:
        """Return value for a tag in the format <application/platform>.tag.

        :param obj: application or platform
        :type obj: str
        :param tag: tag name
        :type tag: str
        :param configuration: debug/release
        :type obj: str
        :returns: value of the tag or empty string
        :rtype: str

        """
        platform = platformconfig.PlatformConfigs().get_platform(self.platformid)
        value: Optional[str] = ""

        if obj == "application":
            value = self.get_custom_prop(configuration, tag)

            if value is None:
                value = self._get_prop(configuration, tag)

            if value is None:
                if tag in self.__dict__:
                    value = str(self.__dict__[tag])
                else:
                    value = ""
        elif obj == "platform":
            value = platform.get_value(obj, tag, configuration)

        assert value is not None
        return value

    def _get_work_folder(self) -> Path:
        """Return app work folder.

        If folder does not exists, it will be created

        :returns: work folder, it's granted to exists
        :rtype: pathlib.Path

        """
        if self.folder is None:
            raise Exception("Folder is not configured.")

        workfolder: Path = self.folder / "work"

        if not os.path.exists(workfolder):
            workfolder.mkdir()

        return workfolder

    def _get_image_name(self, configuration: str) -> str:
        """Return image tag for the application.

        :param configuration: str
        :param configuration: str:

        :returns: unique tag for the image
        :rtype: str

        """
        assert self.id is not None

        appname = self.get_custom_prop(configuration, "appname")

        if appname is None:
            imagename = ""
        else:
            imagename = appname.lower() + "_"

        imagename += self.platformid + "_" + configuration + "_" + self.id
        return imagename

    def get_sdk_image_name(self, configuration: str) -> str:
        """Return the name of the SDK container image for the application.

        :param configuration: debug/release
        :type configuration: str

        :returns: sdk image name
        :rtype: str

        """
        # this function will be part of ApplicationConfig via import,
        # members of base class ApplicationConfigBase are accessed
        # pylint: disable=protected-access
        assert self.id is not None

        platform = platformconfig.PlatformConfigs().get_platform(self.platformid)

        assert platform.id is not None

        if not platform.usesdk:
            return ""

        appname = self.get_custom_prop(configuration, "appname")

        if appname is None:
            imagename = ""
        else:
            imagename = appname.lower() + "_"

        imagename += platform.id
        imagename += "_"
        imagename += configuration
        imagename += "_"
        imagename += self.id
        imagename += "_sdk_image"

        imagename = imagename.replace(":", "_")
        imagename = imagename.replace("/", "_")

        return imagename

    def _get_image_tags(self:Any) -> Dict[str,Any]:
        image_tags={}

        image_tags["debug"]=self._get_image_name("debug")
        image_tags["release"]=self._get_image_name("release")
        return image_tags

    def _get_sdkimage_tags(self:Any) -> Dict[str,Any]:
        sdkimage_tags={}

        sdkimage_tags["debug"]=self.get_sdk_image_name("debug")
        sdkimage_tags["release"]=self.get_sdk_image_name("release")
        return sdkimage_tags

    generatedfields : Mapping[str,Callable[[Any],Dict[str,Any]]] = dict(
        imagetags=_get_image_tags,
        sdkimagetags=_get_sdkimage_tags,
        **config.ConfigurableKeysObject.generatedfields)
    