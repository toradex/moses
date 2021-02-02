"""Base classes for objects that store configuration information."""
import shutil
import os
import io
import logging
import platform
import subprocess
from pathlib import Path
from typing import Optional, Dict, Any
import yaml
import paramiko
import moses_exceptions
import singleton

APP_NAME: str = "moses"


class ConfigurableObject:
    """Base class for objects that can store their configuration in folders and json files.

    Those objects have a folder and a unique id.

    """

    readonlyfields: set = {"folder"}

    @classmethod
    def parse_schema(cls, schema: dict) -> None:
        """Parse the yaml schema and sets read-only fields.

        This function is called at startup, on the object classes of
        objects that support put API calls

        :param schema: schema from YAML definition
        :type schema: dict

        """
        for key, prop in schema["properties"].items():
            if "readOnly" in prop:
                if prop["readOnly"]:
                    cls.readonlyfields.add(key)

    def __init__(self, folder: Optional[Path]):
        """Initialize the object.

        :param folder: folder where configuration is going to be stored.
        :type folder: Path,optional
        """
        self.folder = folder
        # id is a good name for an... id
        # pylint: disable = invalid-name
        self.id: Optional[str] = None

        if self.folder is not None:
            self.id = self.folder.name

    def load(self) -> None:
        """Load object data from YAML file.

        Objects store their data in a folder with a file
        named config.yaml with all the serializable properties

        """
        if self.folder is None:
            raise Exception("")

        fields = {}

        with open(self.folder / "config.yaml", "r") as inp:
            fields = yaml.full_load(inp)

        if not self.is_valid(fields):
            raise ValueError()

        self.__setstate__(fields)

    def _build_folder_path(self) -> Path:
        """Create full folder path from id and other info.

        :returns: path where configuration is stored
        :rtype: Path

        """
        raise NotImplementedError()

    def save(self) -> None:
        """Save object data.

        :raises InvalidObjectIdError: No id has been defined for object
        :raises InvalidObjectStateError: Object state is not valid

        """
        if self.id is None:
            raise moses_exceptions.InvalidObjectIdError()

        if not self.is_valid():
            raise moses_exceptions.InvalidObjectStateError(self.id)

        if self.folder is None:
            self.folder = self._build_folder_path()

            if not self.folder.exists():
                self.folder.mkdir()

        with open(self.folder / "config.yaml", "w") as out:
            yaml.dump(self.__getstate__(), out, indent=4, sort_keys=True)

    # This method provides the default implementation, it can be overridden
    # by derived classes and there self and the argument will be used
    # pylint: disable = unused-argument
    # pylint: disable = no-self-use
    def is_valid(self, fields: dict = None) -> bool:
        """Validate fields of current object.

        :param fields: properties, if None then self.__dict__ is used  (Default value = None)
        :type fields: dict
        :returns: true if all fields contain valid values
        :rtype: bool

        """
        return True

    def destroy(self) -> None:
        """Remove permanently all stored information about the object."""
        # object is not permanent
        if self.folder is None:
            return

        try:
            shutil.rmtree(self.folder)
        # pylint: disable = broad-except
        except BaseException:
            pass

    def check_readonly(self, fields: dict) -> dict:
        """Remove all read-only fields.

        During object updates read-only field are removed,
        after checking that the required value is matching the current one.

        :param fields: properties that need to be updated
        :tpye fields: dict
        :returns: cleaned-up dictionary
        :rtype: dict

        """
        readonlyitems = []

        for key, value in fields.items():
            if key in self.readonlyfields:
                if value != str(self.__dict__[key]):
                    logging.warning(
                        "REST - Attempt to change value of property %s", key
                    )
                readonlyitems.append(key)

        for key in readonlyitems:
            fields.pop(key)

        return fields

    def import_data(self, fields: Dict[str, Any]) -> None:
        """Import data from a field list, checking if changes are required on read-only fields.

        :param fields: properties, if None then self.__dict__
        :type fields: dict

        """
        self.__setstate__(self.check_readonly(fields))

    def __str__(self) -> str:
        """Convert object to string, returning its ID."""
        return str(self.id)

    def __getstate__(self) -> Dict[str, Any]:
        """Return a dictionary with exported properties.

        :return: properties as a dictionary
        :rtype: Dict[str, Any]

        """
        fields = self.__dict__.copy()
        del fields["id"]
        del fields["folder"]
        return fields

    def __setstate__(self, fields: Dict[str, Any]) -> None:
        """Support deserialization from a dictionary."""
        self.__dict__.update(fields)

    def to_json(self) -> Dict[str, Any]:
        """Convert object to an array of json-compatible key-value pairs.

        :return: properties as a dictionary
        :rtype: Dict[str, Any]

        """
        fields = self.__getstate__()
        # we keep id in the info we return via REST
        fields["id"] = self.id
        return fields


class ConfigurableKeysObject(ConfigurableObject):
    """Implement a ConfigurableObject that manages a public/private key pair."""

    def __init__(self, folder: Optional[Path]):
        """Initialize the object.

        :param folder: folder where configuration data is stored
        :type folder: Path, optional
        """
        self.publickey: Optional[str] = None
        self.privatekey: Optional[str] = None
        self.username: Optional[str] = None

        super().__init__(folder)

    def _build_folder_path(self) -> Path:
        """Create full folder path from id and other info.

        :returns: path where configuration is stored
        :rtype: Path

        """
        raise NotImplementedError()

    def save(self) -> None:
        """Save object data.

        On object first save the key pair is generated and stored inside the object's configuration
        """
        super().save()

        if self.privatekey is None:
            self._generate_keys()
            self.save()

    def _generate_keys(self) -> None:
        """Generate public/private key pair.

        Object has to be saved to store them permanently
        """
        if self.folder is None:
            return

        key = paramiko.RSAKey.generate(2048)
        keypath = self.folder / "id_rsa"
        with io.StringIO() as keystrio:
            key.write_private_key(keystrio)
            self.privatekey = keystrio.getvalue()

            if self.folder is not None:
                key.write_private_key_file(str(keypath))

        self.publickey = "ssh-rsa " + key.get_base64()

        if platform.system() == "Windows":
            # pylint: disable = subprocess-run-check
            subprocess.run(
                ["icacls.exe", keypath, "/c", "/t", "/Inheritance:d"])
            subprocess.run(
                [
                    "icacls.exe",
                    keypath,
                    "/c",
                    "/t",
                    "/Remove",
                    "Administrator",
                    "Authenticated Users",
                    "BUILTIN\\Administrators",
                    "BUILTIN",
                    "Everyone",
                    "System",
                    "Users",
                ]
            )
            subprocess.run(
                ["icacls.exe", keypath, "/c", "/t", "/Grant", os.getlogin() + ":F"]
            )
        else:
            os.chmod(keypath, 0o600)

    def to_json(self) -> Dict[str, Any]:
        """Convert object to an array of json-compatible key-value pairs.

        Remove keys from json serialization

        :return: properties as a dictionary
        :rtype: Dict[str, Any]

        """
        fields = super().to_json()
        del fields["privatekey"]
        del fields["publickey"]
        return fields

    def get_privatekeypath(self) -> Optional[str]:
        """Return path for the private key file.

        :returns: path or None if keys haven't been generated yet

        """
        if self.folder is None:
            return None
        return os.path.join(self.folder, "id_rsa")


# pylint: disable = too-many-instance-attributes
# pylint: disable = too-few-public-methods
class ServerConfig(metaclass=singleton.Singleton):
    """Class used to store application parameters."""

    def _create_folders(self) -> None:
        """Create the different folders required by the application."""
        if not self.datapath.exists():
            self.datapath.mkdir()

        if not self.devicespath.exists():
            self.devicespath.mkdir()

        if not self.platformspath.exists():
            self.platformspath.mkdir()

        if not self.standardplatformspath.exists():
            self.standardplatformspath.mkdir()

        if not self.standardeulaspath.exists():
            self.standardeulaspath.mkdir()

        if not self.eulaspath.exists():
            self.eulaspath.mkdir()

    def __init__(self) -> None:
        """Initialize configuration.

        Assigns default values to parameter, then loads configuration
        from a json file passed as argument and creates required
        folders
        """
        self.commandtimeout: int = 30
        self.apppath = Path(os.path.dirname(os.path.abspath(__file__)))
        self.datapath = Path.home() / ("." + APP_NAME)

        self.devicespath = self.datapath / "devices"

        self.platformspath = self.datapath / "platforms"

        self.standardplatformspath = self.apppath / "platforms"

        self.standardeulaspath = self.apppath / "eulas"

        self.eulaspath = self.datapath / "eulas"

        self._create_folders()
