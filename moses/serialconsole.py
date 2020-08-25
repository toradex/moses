import time
import serial
import console
import exceptions
from typing import Optional

"""This module is used to communicate to the device over serial port
"""


class SerialConsole(console.GenericConsole):
    """Class implementing console features on serial port

        Arguments:
            console {console.GenericConsole} -- base class
    """

    def __init__(self, device: str):
        """Must be re-defined in subclasses

        Arguments:
            device {str} -- port name
        """
        try:
            self.ser = serial.Serial(device, 115200, 8, serial.PARITY_NONE, 1, 5)
        except serial.SerialException as e:
            raise exceptions.SerialError(e)
        self._prompt = ""

    def set_prompt(self, prompt: str) -> None:
        """Configures what should be recognized as prompt

        Arguments:
            prompt {str} -- current prompt (including trailing spaces)
        """
        self._prompt = prompt

    # Methods of the base console class
    def send_cmd(self, command: str, timeout: int = 30) -> str:
        """Sends a command to the device and returns its output

        Arguments:
            command {str} -- command to be sent

        Keyword Arguments:
            timeout {int} -- timeout in seconds (default: {30})

        Returns:
            str -- output of the command (till next prompt)
        """
        output = ""

        try:
            super().send_cmd(command, timeout)
            self.ser.flush()
            self.ser.write(command.encode("utf-8"))
            self.ser.write("\n".encode("utf-8"))

            start = time.time()

            while not output.endswith(self._prompt):
                if time.time() - start > timeout:
                    raise exceptions.TimeoutError()

                try:
                    output += self.ser.read_all().decode("utf-8")
                except UnicodeDecodeError:
                    continue

            return output[: len(output) - len(self._prompt)].strip()
        except serial.SerialException as e:
            raise exceptions.SerialError(e)
        except OSError as e:
            raise exceptions.OSError(e)

    def wait_for_prompt(self, prompt: Optional[str] = None, timeout: int = 30) -> None:
        """Wait until the specific string is received

        Keyword Arguments:
            prompt {str} -- prompt to wait, if None the one set using
                            {set_prompt} will be used (default: {None})
            timeout {int} -- timeout in seconds (default: {30})
        """
        output = ""

        if prompt is None:
            prompt = self._prompt

        self.ser.write("\n".encode("utf-8"))

        start = time.time()

        while not output.endswith(prompt):
            if time.time() - start > timeout:
                raise exceptions.TimeoutError()

            try:
                output += self.ser.read_all().decode("utf-8")
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
        """

        try:

            loggedin = False
            start = time.time()
            count = 0

            while time.time() - start < timeout:

                if count % 2:
                    self.ser.write("\n\n\n\n".encode("utf-8"))
                else:
                    # just in case we are already at the shell prompt
                    self.ser.write("exit\n".encode("utf-8"))

                count = count + 1

                try:
                    # we need to figure out if we are at login prompt
                    self.wait_for_prompt("login: ")

                    # write username
                    self.ser.write(username.encode("utf-8"))

                    # wait for prompt sends the EOL
                    self.wait_for_prompt("Password: ")

                    # write password
                    self.ser.write(password.encode("utf-8"))
                    self.ser.write("\n".encode("utf-8"))

                    loggedin = True

                except exceptions.TimeoutError:
                    continue

                break

            if not loggedin:
                raise exceptions.LoginFailedError()

            # wait for any prompt
            start = time.time()

            while self.ser.in_waiting == 0:
                if time.time() - start > timeout:
                    raise exceptions.TimeoutError()

            time.sleep(10)
            prompt = self.ser.read_all().decode("utf-8")

            if "Login incorrect" in prompt:
                raise exceptions.LoginFailedError()

            changepwd = False

            if "Current password:" in prompt:
                # write password
                self.ser.write(password.encode("utf-8"))

                # write a dummy new password
                self.wait_for_prompt("New password: ")
                self.ser.write("thispasswordwontlast".encode("utf-8"))
                self.wait_for_prompt("Retype new password: ")
                # 2nd one requires \n because there is no waif_for_prompt afterwards
                self.ser.write("thispasswordwontlast\n".encode("utf-8"))

                changepwd = True
                time.sleep(5)

            # we reached the prompt
            # send command to configure it to a known state
            self.ser.write("PS1=__$".encode("utf-8"))
            self.set_prompt("__$")
            self.wait_for_prompt()
            # disable local echo
            self.ser.write("stty -echo".encode("utf-8"))
            self.wait_for_prompt()
            self.ser.write("cd".encode("utf-8"))
            self.wait_for_prompt()

            if changepwd:
                self.ser.write("passwd".encode("utf-8"))
                self.wait_for_prompt("Current password: ")
                self.ser.write("thispasswordwontlast".encode("utf-8"))
                self.wait_for_prompt("New password: ")
                self.ser.write(password.encode("utf-8"))
                self.wait_for_prompt("Retype new password: ")
                self.ser.write(password.encode("utf-8"))
                self.wait_for_prompt()

            time.sleep(5)
            self.ser.flush()
            self.ser.read_all()

        except serial.SerialException as e:
            raise exceptions.SerialError(e)
        except OSError as e:
            raise exceptions.OSError(e)

    # enable object to be used in "with" statements
    def __enter__(self):
        self.ser.__enter__()
        return self

    def __exit__(self, type, value, traceback):
        try:
            self.ser.write("exit\n".encode("utf-8"))
            self.ser.__exit__(type, value, traceback)
        except:
            pass
