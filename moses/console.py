"""Base module to implement console features on serial and SSH."""
import logging



class GenericConsole:
    """Base class with features supported on both kind of consoles."""

    def __init__(self, device: str):
        """Initialize the object.

        :param device: can be an address or the name of a port used to communicate with the device
        :type device: str
        """

    def send_cmd(self, command: str, timeout: int = 30) -> str:
        """Send a command to the device and returns its output.

        :param command: command to be sent to the target
        :type command: str
        :param timeout: timeout in seconds (default=30)
        :type timeout: int
        :returns: output of the command (till next prompt)

        """
        pass

    def login(self, username: str, password: str, timeout: int = 60) -> None:
        """Try to login user and configure shell to send further commands.

        :param username: username
        :type username: str
        :param password: password
        :type password: str
        :param timeout: timeout in seconds (default=60)
        :type timeout: int

        """
        pass
