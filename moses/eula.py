"""Classes used to manage End User License Agreements."""
import os
import logging
from typing import Dict, Any
from pathlib import Path
import singleton
import config


# pylint: disable = too-many-instance-attributes
class EULA(config.ConfigurableObject):
    """Class that stores information about a specific eula and it's acceptance status."""

    readonlyfields: set = config.ConfigurableObject.readonlyfields.union(
        {"title", "question", "filepath"}
    )

    def __init__(self, folder: Path, standard: bool):
        """Load eula information from folder.

        :param folder: root folder for the object
        :type folder: pathlib.Path
        :param standard: if true the Eula has been loaded from the install path
            and must be saved to a different location
        :type standard: bool

        """
        super().__init__(folder)

        self.standard = standard
        self.title = ""
        self.question = ""
        self.filename = ""
        self.visualized = False
        self.accepted = False

        if self.folder is not None:
            self.load()

        if standard:
            assert self.folder is not None
            self.filepath = str(self.folder / self.filename)

    def is_valid(self, fields: Dict[str, Any] = None) -> bool:
        """Check if the object is valid.

        No actual validation performed, Eulas are mostly static objects

        """
        return True

    def to_json(self) -> Dict[str, Any]:
        """Convert object to an array of json-compatible key-value pairs.

        :return: properties as a dictionary
        :rtype: Dict[str, Any]

        """
        fields = super().to_json()
        del fields["standard"]
        return fields

    def _build_folder_path(self) -> Path:
        """Create full folder path from id and other info.

        :returns: path where configuration is stored
        :rtype: Path

        """
        assert self.id is not None

        return config.ServerConfig().eulaspath / self.id

    def save(self) -> None:
        """Save object data.

        Eulas are loaded from install folder but must be saved to the user's home folder
        because install folder may not be writable.
        """
        assert self.id is not None

        if self.standard:
            self.folder = config.ServerConfig().eulaspath / self.id

            try:
                assert self.folder is not None

                os.mkdir(self.folder)
            # pylint: disable = broad-except
            except BaseException:
                pass

            self.standard = False

        super().save()


# pylint: disable = too-few-public-methods
class EULAs(Dict[str, EULA], metaclass=singleton.Singleton):
    """Class to manage eulas for the different platforms.

    Works only as a container, Specific properties are accessed
    using the :class:`eula` class

    """

    def __init__(self) -> None:
        """Iterate on all eulas and load them."""
        path = config.ServerConfig().standardeulaspath

        subfolders = [dir for dir in path.iterdir() if dir.is_dir()]

        for subfolder in subfolders:
            try:
                eula = EULA(subfolder, True)

                assert eula.id is not None

                # pylint false positive, self is a dict, so we can add items
                # pylint: disable=unsupported-assignment-operation
                self[eula.id] = eula
            # pylint: disable = broad-except
            except Exception as exception:
                logging.exception(
                    "Can't create eula from folder %s." "Error: %s", str(
                        subfolder), str(exception)
                )

        path = config.ServerConfig().eulaspath

        subfolders = [dir for dir in path.iterdir() if dir.is_dir()]

        for subfolder in subfolders:
            try:
                eula = EULA(subfolder, False)

                assert eula.id is not None

                # pylint false positive, self is a dict, so we can add items
                # pylint: disable=unsupported-assignment-operation
                self[eula.id] = eula
            # pylint: disable = broad-except
            except Exception as exception:
                logging.exception(
                    "Can't create eula from folder %s." "Error: %s", str(
                        subfolder), str(exception)
                )
