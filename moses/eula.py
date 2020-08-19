"""Classes used to manage eulas. 
"""
import config
import shutil
import logging
from pathlib import Path
import singleton
import exceptions
import shutil
import os


class EULA(config.ConfigurableObject):
    """Stores information about a specific eula and it's acceptance status
    """

    readonlyfields = {"title", "question", "filepath"}

    def __init__(self, folder: str, standard: bool):
        """Loads eula information from folder

        Args:
            folder (str): root folder for the object
            standard (bool): if True the eula has been loaded from the install path
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
            self.filepath = str(self.folder / self.filename)

    def is_valid(self, fields=None) -> bool:
        return True

    def _to_json(self):
        fields = super()._to_json()
        del fields["standard"]
        return fields

    def save(self):
        """Save object data
        """

        if self.standard:
            self.folder = config.SERVER_CONFIG["eulaspath"] / self.id
            
            try:
                os.mkdir(self.folder)
            except:
                pass

            self.standard = False

        super().save()


class EULAs(dict, metaclass=singleton.Singleton):
    """Manages eulas for the different platforms

    Works only as a container, Specific properties are accessed
    using the :class:`eula` class
    """

    def __init__(self):
        """ Iterates on all eulas 
        """
        path = config.SERVER_CONFIG["standardeulaspath"]

        subfolders = [dir for dir in path.iterdir() if dir.is_dir()]

        for dir in subfolders:
            try:
                eula = EULA(dir, True)
                self[eula.id] = eula
            except Exception as e:
                logging.exception("Can't create eula from folder %s."
                                  "Error: %s",
                                  str(dir), str(e))

        path = config.SERVER_CONFIG["eulaspath"]

        subfolders = [dir for dir in path.iterdir() if dir.is_dir()]

        for dir in subfolders:
            try:
                eula = EULA(dir, False)

                self[eula.id] = eula
            except Exception as e:
                logging.exception("Can't create eula from folder %s."
                                  "Error: %s",
                                  str(dir), str(e))
