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

APP_NAME = "moses"

SERVER_CONFIG = {
    "commandtimeout": 30
}


class ConfigurableObject:
    """ Base class for objects that can store their configuration
        in folders and json files.
        Those objects have a folder and a unique id.
    """

    readonlyfields = {"folder"}

    @classmethod
    def parse_schema(cls, schema):
        """parses the yaml schema and sets read-only fields

        Arguments:
            schema {dict} -- yaml object
        """
        for key, prop in schema["properties"].items():
            if "readOnly" in prop:
                if prop["readOnly"]:
                    cls.readonlyfields.add(key)

    def __init__(self, folder):

        self.folder = folder

        if not self.folder:
            self.id = None
        else:
            self.id = self.folder.name

    def load(self):
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

    def save(self):
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

    def is_valid(self, fields=None) -> bool:
        """Validate fields of current object

        Arguments:
            fields {dictionary} -- dictionary with values, if None then
                                   self.__dict__ will be used

        Returns:
            bool -- true if all fields contain valid values
        """
        pass

    def destroy(self):
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
                if value != self.__dict__[key]:
                    logging.warning(
                        "REST - Attempt to change value of property %s", key)
                readonlyitems.append(key)

        [fields.pop(key) for key in readonlyitems]
        return fields

    def import_data(self, fields: dict):
        """Import data from a field list, checking read-only
        properties

        Arguments:
            fields {dict} -- fields and values
        """
        self.__setstate__(self.check_readonly(fields))

    # convert object to string

    def __str__(self):
        return self.id

    # support serialization
    def __getstate__(self):
        fields = self.__dict__.copy()
        del fields["id"]
        del fields["folder"]
        return fields

    def __setstate__(self, fields):
        self.__dict__.update(fields)

    def _to_json(self):
        fields = self.__getstate__()
        # we keep id in the info we return via REST
        fields["id"] = self.id
        return fields


class ConfigurableKeysObject(ConfigurableObject):
    """Implements and object that manages ssh public/private keys
    """

    def __init__(self, folder):

        self.publickey = None
        self.privatekey = None
        self.username = None

        super().__init__(folder)

    def save(self):
        """Save object data
        """

        super().save()

        if self.privatekey is None:
            self._generate_keys()
            self.save()

    def _generate_keys(self):
        """Generates SSH keys used to connect with the device over SSH
        """
        key = paramiko.RSAKey.generate(2048)
        with io.StringIO() as keystrio:
            key.write_private_key(keystrio)
            self.privatekey = keystrio.getvalue()

            if self.folder is not None:
                key.write_private_key_file(self.folder / "id_rsa")

        self.publickey = "ssh-rsa "+key.get_base64()

    # support serialization
    def _to_json(self):
        fields = super()._to_json()
        del fields["privatekey"]
        del fields["publickey"]
        return fields

    def get_privatekeypath(self) -> str:
        """returns path for the private key file

        Returns:
            str -- path
        """
        return os.path.join(self.folder, "id_rsa")


def _create_folders():
    if not SERVER_CONFIG["datapath"].exists():
        SERVER_CONFIG["datapath"].mkdir()

    if not SERVER_CONFIG["devicespath"].exists():
        SERVER_CONFIG["devicespath"].mkdir()

    if not SERVER_CONFIG["platformspath"].exists():
        SERVER_CONFIG["platformspath"].mkdir()

    if not SERVER_CONFIG["standardplatformspath"].exists():
        SERVER_CONFIG["standardplatformspath"].mkdir()


def init_config():
    """Initializes configuration

    Assigns default values to parameter, then loads configuration
    from a json file passed as argument and creates required
    folders
    """

    SERVER_CONFIG["apppath"] = pathlib.Path(
        os.path.dirname(os.path.abspath(__file__)))
    SERVER_CONFIG["datapath"] = pathlib.Path.home() / ("."+APP_NAME)

    # TODO: parse command line args
    # TODO: load configuration from file
    # TODO: convert strings to paths

    # derives additional settings if not present
    if "devicespath" not in SERVER_CONFIG:
        SERVER_CONFIG["devicespath"] = SERVER_CONFIG["datapath"] / "devices"

    if "platformspath" not in SERVER_CONFIG:
        SERVER_CONFIG["platformspath"] = SERVER_CONFIG["datapath"] \
            / "platforms"

    if "standardplatformspath" not in SERVER_CONFIG:
        SERVER_CONFIG["standardplatformspath"] = SERVER_CONFIG["apppath"] \
            / "platforms"

    _create_folders()
