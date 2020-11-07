"""Module used to store configuration information
"""
import yaml
import shutil
import os
import io
import logging
import paramiko
import pathlib
import exceptions
import platform
import subprocess
import singleton
from typing import Optional, Dict, Any

APP_NAME: str = "moses"


class ConfigurableObject:
    """ Base class for objects that can store their configuration
        in folders and json files.
        Those objects have a folder and a unique id.
    """

    readonlyfields: set = {"folder"}

    @classmethod
    def parse_schema(cls, schema: dict) -> None:
        """parses the yaml schema and sets read-only fields

        Arguments:
            schema {dict} -- yaml object
        """
        for key, prop in schema["properties"].items():
            if "readOnly" in prop:
                if prop["readOnly"]:
                    cls.readonlyfields.add(key)

    def __init__(self, folder: Optional[pathlib.Path]):

        self.folder = folder
        self.id: Optional[str] = None

        if self.folder is not None:
            self.id = self.folder.name

    def load(self) -> None:
        """Loads object data
        """
        if self.folder is None:
            raise Exception("")

        fields = {}

        with open(self.folder / "config.yaml", "r") as inp:
            fields = yaml.full_load(inp)

        if not self.is_valid(fields):
            raise ValueError()

        self.__setstate__(fields)

    def _build_folder_path(self) -> pathlib.Path:
        """Create full folder path from id and other info

        Returns:
            pathlib.Path -- path where configuration is stored
        """
        raise NotImplementedError()

    def save(self) -> None:
        """Save object data

        Raises:
            InvalidObjectIdError: No id has been defined for object
            InvalidObjectStateError: Object state is not valid
        """

        if self.id is None:
            raise exceptions.InvalidObjectIdError()

        if not self.is_valid():
            raise exceptions.InvalidObjectStateError(self.id)

        if self.folder is None:
            self.folder = self._build_folder_path()

            if not self.folder.exists():
                self.folder.mkdir()

        with open(self.folder / "config.yaml", "w") as out:
            yaml.dump(self.__getstate__(), out, indent=4, sort_keys=True)

    def is_valid(self, fields: dict = None) -> bool:
        """Validate fields of current object

        Arguments:
            fields {dict} -- dictionary with values, if None then
                                   self.__dict__ will be used

        Returns:
            bool -- true if all fields contain valid values
        """
        pass

    def destroy(self) -> None:
        """Removes permanently stored information about the device
        """

        # device is not permanent
        if self.folder is None:
            return

        try:
            shutil.rmtree(self.folder)
        except:
            pass

    def check_readonly(self, fields: dict) -> dict:
        """remove all read-only fields after checking that
        the value is matching the current one

        Arguments:
            fields {dict} -- fields

        Returns:
            dict -- cleaned-up dictionary
        """

        readonlyitems = []

        for key, value in fields.items():
            if key in self.readonlyfields:
                if value != str(self.__dict__[key]):
                    logging.warning(
                        "REST - Attempt to change value of property %s", key
                    )
                readonlyitems.append(key)

        [fields.pop(key) for key in readonlyitems]
        return fields

    def import_data(self, fields: Dict[str, Any]) -> None:
        """Import data from a field list, checking read-only
        properties

        Arguments:
            fields {dict} -- fields and values
        """
        self.__setstate__(self.check_readonly(fields))

    # convert object to string

    def __str__(self) -> str:
        return str(self.id)

    # support serialization
    def __getstate__(self) -> Dict[str, Any]:
        fields = self.__dict__.copy()
        del fields["id"]
        del fields["folder"]
        return fields

    def __setstate__(self, fields) -> None:
        self.__dict__.update(fields)

    def _to_json(self) -> dict:
        fields = self.__getstate__()
        # we keep id in the info we return via REST
        fields["id"] = self.id
        return fields


class ConfigurableKeysObject(ConfigurableObject):
    """Implements and object that manages ssh public/private keys
    """

    def __init__(self, folder: Optional[pathlib.Path]):

        self.publickey: Optional[str] = None
        self.privatekey: Optional[str] = None
        self.username: Optional[str] = None

        super().__init__(folder)

    def save(self) -> None:
        """Save object data
        """

        super().save()

        if self.privatekey is None:
            self._generate_keys()
            self.save()

    def _generate_keys(self) -> None:
        """Generates SSH keys used to connect with the device over SSH
        """

        if self.folder is None:
            return

        key = paramiko.RSAKey.generate(2048)
        keypath = self.folder / "id_rsa"
        with io.StringIO() as keystrio:
            key.write_private_key(keystrio)
            self.privatekey = keystrio.getvalue()

            if self.folder is not None:
                key.write_private_key_file(keypath)

        self.publickey = "ssh-rsa " + key.get_base64()

        if platform.system() == "Windows":
            subprocess.run(["icacls.exe", keypath, "/c", "/t", "/Inheritance:d"])
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

    # support serialization

    def _to_json(self) -> dict:
        fields = super()._to_json()
        del fields["privatekey"]
        del fields["publickey"]
        return fields

    def get_privatekeypath(self) -> Optional[str]:
        """returns path for the private key file

        Returns:
            str -- path
        """
        if self.folder is None:
            return None
        return os.path.join(self.folder, "id_rsa")


class ServerConfig(metaclass=singleton.Singleton):
    def _create_folders(self) -> None:
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

    def __init__(self):
        """Initializes configuration

        Assigns default values to parameter, then loads configuration
        from a json file passed as argument and creates required
        folders
        """

        self.commandtimeout: int = 30
        self.apppath = pathlib.Path(os.path.dirname(os.path.abspath(__file__)))
        self.datapath = pathlib.Path.home() / ("." + APP_NAME)

        self.devicespath = self.datapath / "devices"

        self.platformspath = self.datapath / "platforms"

        self.standardplatformspath = self.apppath / "platforms"

        self.standardeulaspath = self.apppath / "eulas"

        self.eulaspath = self.datapath / "eulas"

        self._create_folders()
