"""Implements console functions over SSH connection."""
import io
import socket
import time
from types import TracebackType
from typing import Optional, Type
import paramiko
import console
import sharedssh
# pylint: disable = redefined-builtin
from moses_exceptions import SSHError, TimeoutError, OSError
# pylint: enable = redefined-builtin


class SSHConsole(console.GenericConsole):
    """Implementation of console over SSH."""

    def __init__(self, device: str):
        """Initialize object.

        :param device: target hostname
        :type device: str

        """
        super().__init__(device)
        if ":" in device:
            self.hostname, portstr = device.split(":")[0:2]
            self.port = int(portstr)
        else:
            self.hostname = device
            self.port = 22

        self.ssh: Optional[paramiko.SSHClient] = None
        self.channel: Optional[paramiko.Channel] = None

    def send_cmd(self, command: str, timeout: int = 5) -> str:
        """Send a command to the device and returns its output.

        :param command: command to send
        :type command: str
        :param timeout: timeout in seconds (Default value = 5)
        :param timeout: int
        :returns: output of the command (till next prompt)
        :rtype: str

        """
        output = error = ""

        try:
            assert self.ssh is not None

            _, stdout, stderr = self.ssh.exec_command(command, timeout)

            output = stdout.read().decode("utf-8")
            error = stderr.read().decode("utf-8")

        except paramiko.SSHException as exception:
            raise SSHError(exception) from exception
        except socket.timeout:
            pass

        return (output + error).strip()

    # pylint: disable = no-self-use
    def wait_for_prompt(
            self, channel: paramiko.Channel, prompt: str, timeout: int = 30) -> None:
        """Wait until the specific string is received.

        :param prompt: prompt or None to use the one configured by set_prompt
            (Default value = None)
        :type prompt: str, optional
        :param timeout: timeout in seconds  (Default value = 30)
        :type timeout: int

        """
        output = ""

        channel.send("\n".encode("utf-8"))

        start = time.time()

        while not output.endswith(prompt):
            if time.time() - start > timeout:
                raise TimeoutError()

            try:
                output += channel.recv(4096).decode("utf-8")
            except UnicodeDecodeError:
                continue

    def login(self, username: str, password: str, timeout: int = 60) -> None:
        """Try to login user and configures prompt.

        An exception is generated if login attempts fail.

        :param username: username
        :type username: str
        :param password: password
        :tpye password: str
        :param timeout: timeout in seconds (Default value = 60)
        :type timeout: int

        """
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(sharedssh.IgnorePolicy())

        try:

            self.ssh.connect(
                self.hostname,
                port=self.port,
                username=username,
                password=password,
                allow_agent=False,
            )

            channel = self.ssh.invoke_shell()

            start = time.time()

            while not channel.recv_ready():
                time.sleep(1)
                if time.time() > start + timeout:
                    raise TimeoutError()

            prompt = channel.recv(4096).decode("utf-8")

            if "Current password: " in prompt:
                channel.send(password.encode("utf-8"))

                # write a dummy new password
                self.wait_for_prompt(channel, "New password: ")
                channel.send("thispasswordwontlast".encode("utf-8"))
                self.wait_for_prompt(channel, "Retype new password: ")
                channel.send("thispasswordwontlast".encode("utf-8"))

                self.wait_for_prompt(
                    channel, "passwd: password updated successfully\r\n"
                )

                self.ssh.close()

                self.ssh.connect(
                    self.hostname,
                    port=self.port,
                    username=username,
                    password="thispasswordwontlast",
                    allow_agent=False,
                )

                channel = self.ssh.invoke_shell()
                channel.send("passwd".encode("utf-8"))
                self.wait_for_prompt(channel, "Current password: ")
                channel.send("thispasswordwontlast".encode("utf-8"))
                self.wait_for_prompt(channel, "New password: ")
                channel.send(password.encode("utf-8"))
                self.wait_for_prompt(channel, "Retype new password: ")
                channel.send(password.encode("utf-8"))
                self.wait_for_prompt(
                    channel, "passwd: password updated successfully\r\n"
                )

                self.ssh.close()

                self.ssh.connect(
                    self.hostname,
                    port=self.port,
                    username=username,
                    password=password,
                    allow_agent=False,
                )

        except paramiko.SSHException as exception:
            raise SSHError(exception) from exception
        except OSError as exception:
            raise OSError(exception) from exception

    def connect(self, username: str, key: str) -> None:
        """Connect to the device using SSH key.

        :param username: username
        :type username: str
        :param key: SSH key encoded in ASCII
        :type key: str

        """
        try:
            k = paramiko.RSAKey.from_private_key(io.StringIO(key))

            self.ssh = paramiko.SSHClient()
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            self.ssh.connect(
                self.hostname,
                port=self.port,
                username=username,
                pkey=k,
                allow_agent=False,
            )

        except paramiko.SSHException as exception:
            raise SSHError(exception) from exception

    def __enter__(self) -> "SSHConsole":
        """Ensure that object state is managed correctly in with statements."""
        return self

    # pylint: disable = useless-return
    def __exit__(
        self,
        etype: Optional[Type[BaseException]],
        value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> Optional[bool]:
        """Ensure that object state is managed correctly in with statements."""
        try:
            if self.channel is not None:
                self.channel.close()
            if self.ssh is not None:
                self.ssh.close()
        # pylint: disable = broad-except
        except Exception:
            pass
        return None
