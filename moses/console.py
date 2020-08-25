"""Base module to implement console features on serial and SSH
"""
import logging


class GenericConsole:
    """Base features supported on both kind of consoles
    """

    def __init__(self, device: str):
        """Must be re-defined in subclasses
        Arguments:
            device {str} -- port, ip depending on subclass
        """

    def send_cmd(self, command: str, timeout: int = 30) -> str:
        """Sends a command to the device and returns its output

        Arguments:
            command {str} -- command to be sent

        Keyword Arguments:
            timeout {int} -- timeout in seconds (default: {30})

        Returns:
            str -- output of the command (till next prompt)
        """
        pass

    def login(self, username: str, password: str, timeout: int = 60) -> None:
        """Tries to login user and configures prompt

        Arguments:
            username {str} -- username
            password {str} -- cleartext password

        Keyword Arguments:
            timeout {int} -- timeout in seconds (default: {30})

        """
