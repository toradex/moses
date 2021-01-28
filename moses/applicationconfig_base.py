"""Base class for application configuration.

ApplicationConfig clas was getting too big, it had to be splitted between multiple files,
depending of features. To ensure validation and coherency, data members and base features
have been extported into a base class, implemented here
"""
import os
import logging
import uuid
import docker
import docker.models.containers
import config
import platformconfig
import datetime
import tags
import pathlib
from pathlib import Path
from typing import Optional, Dict, Any, List


class ApplicationConfigBase(config.ConfigurableKeysObject):
    """Class used to manage an application."""

    readonlyfields = config.ConfigurableKeysObject.readonlyfields.union(
        {"images", "sdkimages"}
    )

    non_nullable_properties = ["dockercomposefile", "startupscript", "shutdownscript"]
    configurations = ["common", "debug", "release"]

    def __init__(self, folder: Optional[pathlib.Path] = None):
        """Load data from the configuration folder.

        :param folder: path of the folder used to store application configuration
        :type folder: pathlib.Path, optional

        """
        super().__init__(folder)

        self.props: Dict[str, Dict[str, str]] = {
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
        }

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

        self.images: Dict[str, str] = {"debug": "", "release": ""}

        self.sdkimages: Dict[str, str] = {"debug": "", "release": ""}

        self.platformid = ""
        self.publickey: Optional[str] = None
        self.privatekey: Optional[str] = None
        self.modificationdate = datetime.datetime.utcnow().isoformat()

        self.extraparms: Dict[str, Dict[str, str]] = {
            "common": {},
            "debug": {},
            "release": {},
        }

        self.dockercomposefile: Dict[str, str] = {
            "common": "",
            "debug": "",
            "release": "",
        }

        self.startupscript: Dict[str, str] = {"common": "", "debug": "", "release": ""}

        self.shutdownscript: Dict[str, str] = {"common": "", "debug": "", "release": ""}

        self.networks: Dict[str, List[str]] = {"common": [], "debug": [], "release": []}

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

        ld = docker.from_env()

        for field in ["images", "sdkimages"]:
            for configuration in ["debug", "release"]:
                imgid = self.__dict__[field][configuration]

                if imgid is None or imgid == "":
                    continue

                try:
                    limg = ld.images.get(imgid)
                except docker.errors.ImageNotFound:
                    self.__dict__[field][configuration] = ""

    def _generate_keys(self) -> None:
        """Generate keys for SSH connectivity.

        The public key is also saved as regular file inside the configuration folder.add()

        """
        super()._generate_keys()

        assert self.folder is not None

        with open(str(self.folder / "id_rsa.pub"), "w") as f:
            assert self.publickey is not None
            f.write(self.publickey)

    def _build_folder_path(self) -> Path:
        """Build folder path (not implemented for applications)."""
        raise Exception("Application must have a defined base folder path.")

    def is_valid(self, fields: dict = None) -> bool:
        """Validate the fields of current object.

        :param fields: object properties as a dictionary, if None is passed then self.__dict__ is used
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

    def _to_json(self) -> Dict[str, Any]:
        """Convert object to an array of json-compatible key-value pairs.

        :return: properties as a dictionary
        :rtype: Dict[str, Any]

        """
        # we return also folder in json
        fields = super()._to_json()
        fields["folder"] = str(self.folder)
        return fields

    def _get_custom_prop(self, configuration: str, property: str) -> Optional[str]:
        """Return value of custom property.

        If there is a configuration-specific value its returned, otherwise
        common value is checked and returned. If no value is found, the function
        return None.

        :param configuration: debug/release
        :type configuration: str
        :param property: property name
        :type property: str
        :return: value of the property of None if it's not defined
        :rtype: str | None

        """
        if property in self.props[configuration]:
            return str(self.props[configuration][property])
        if property in self.props["common"]:
            return str(self.props["common"][property])
        return None

    def _merge_props(
        self, plat: platformconfig.PlatformConfig, configuration: str, prop: str
    ) -> Dict[str, Any]:
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
                    lambda obj, tag, args: self._get_value(obj, tag, args),
                    configuration,
                )
                if newvalue != value:
                    merged[key] = value

        return merged

    def _append_props(
        self, plat: platformconfig.PlatformConfig, configuration: str, prop: str
    ) -> list:
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
                    lambda obj, tag, args: self._get_value(obj, tag, args),
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
            prop in ApplicationConfigBase.non_nullable_properties
            and len(self.__dict__[prop][configuration]) == 0
        ):
            return str(self.__dict__[prop][configuration])

        if (self.__dict__[prop]["common"] is not None) and not (
            prop in ApplicationConfigBase.non_nullable_properties
            and len(self.__dict__[prop]["common"]) == 0
        ):
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

        if obj == "application":
            value = self._get_custom_prop(configuration, tag)

            if value is None:
                value = self._get_prop(configuration, tag)

            if value is None:
                if tag in self.__dict__:
                    value = str(self.__dict__[tag])
                else:
                    value = ""

            return value
        elif obj == "platform":
            return platform._get_value(obj, tag, configuration)
        return ""

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

        appname = self._get_custom_prop(configuration, "appname")

        if appname is None:
            imagename = ""
        else:
            imagename = appname.lower() + "_"

        imagename += self.platformid + "_" + configuration + "_" + self.id
        return imagename