"""Implements the singleton patter using metaclass."""

from typing import Dict, Any


class Singleton(type):
    """Metaclass used to have a single instance of a specific class.

    Used to maintain lists of devices, platforms, applications, eulas etc.
    Object is allocated on first call.
    """

    # we must use class name because we are inside the class declaration
    _instances: Dict[Any, "Singleton"] = {}

    def __call__(
        cls: "Singleton", *args: tuple, **kwargs: Dict[str, Any]
    ) -> "Singleton":
        """Return singleton object, allocating it if needed.

        :return: the one and only instance of the object
        :rtype: Singleton
        """
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
