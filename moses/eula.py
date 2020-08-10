"""Classes used to manage eulas. 
"""
import config
import shutil
import logging
from pathlib import Path
import singleton
import exceptions

class EULA(config.ConfigurableObject):
    """Stores information about a specific eula and it's acceptance status
    """

    readonlyfields = {"title", "question", "filepath"}

    def __init__(self, folder):        

        super().__init__(folder)

        self.title = ""
        self.question = ""
        self.filename = ""
        self.visualized = False
        self.accepted = False

        if self.folder is not None:
            self.load()

        self.filepath = str(self.folder / self.filename)     

    def is_valid(self, fields=None) -> bool:
        return True   


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
                eula = EULA(dir)
                self[eula.id] = eula
            except Exception as e:
                logging.exception("Can't create eula from folder %s."
                                  "Error: %s",
                                  str(dir), str(e))
