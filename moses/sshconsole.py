"""Module to implement console features on SSH
"""


import console
import socket
import time
import paramiko
import logging
import io
import exceptions
import sharedssh
import targetdevice
from typing import Optional


class SSHConsole(console.GenericConsole):
    """SSH console
    """

    def __init__(self, device: str):
        """Must be re-defined in subclasses
        Arguments:
            device {str} -- hostname
        """
        if ":" in device:
            self.hostname, portstr = device.split(":")[0:2]
            self.port = int(portstr)
        else:
            self.hostname = device
            self.port = 22

        self.ssh: paramiko.SSHClient = None
        self.channel: paramiko.Channel = None

    def send_cmd(self, command: str, timeout: int = 30) -> str:
        """Sends a command to the device and returns its output

        Arguments:
            command {str} -- command to be sent

        Keyword Arguments:
            timeout {int} -- timeout in seconds (default: {30})

        Returns:
            str -- output of the command (till next prompt)
        """
        super().send_cmd(command, timeout)

        output = error = ""

        try:
            _, stdout, stderr = self.ssh.exec_command(command, timeout=5)

            output = stdout.read().decode("utf-8")
            error = stderr.read().decode("utf-8")

        except paramiko.SSHException as e:
            raise exceptions.SSHError(e)
        except socket.timeout:
            pass

        return (output + error).strip()

    def wait_for_prompt(
        self, channel: paramiko.Channel, prompt: str, timeout: int = 30
    ) -> None:
        """Wait until the specific string is received

        Keyword Arguments:
            prompt {str} -- prompt to wait, if None the one set using
                            {set_prompt} will be used (default: {None})
            timeout {int} -- timeout in seconds (default: {30})
        """
        output = ""

        channel.send("\n".encode("utf-8"))

        start = time.time()

        while not output.endswith(prompt):
            if time.time() - start > timeout:
                raise exceptions.TimeoutError()

            try:
                output += channel.recv(4096).decode("utf-8")
            except UnicodeDecodeError:
                continue
        return

    def login(self, username: str, password: str, timeout: int = 60) -> None:
        """Tries to login user and configures prompt

        Arguments:
            username {str} -- username
            password {str} -- cleartext password

        Keyword Arguments:
            timeout {int} -- timeout in seconds (default: {30})

        Returns:
            bool -- true if login was successful

        Raises:
            exceptions.SSHError : ssh error
            exceptions.OSError : OS related error

        """

        self.password = password
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
                    raise exceptions.TimeoutError()

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

        except paramiko.SSHException as e:
            raise exceptions.SSHError(e)
        except OSError as e:
            raise exceptions.OSError(e)

    def connect(self, username: str, key: str) -> None:
        """Connects to device using keys

        Arguments:
            key {str} -- ssh key
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

        except paramiko.SSHException as e:
            raise exceptions.SSHError(e)

    # enable object to be used in "with" statements
    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        try:
            self.channel.close()
            self.ssh.close()
        except:
            pass
