"""Implements console functions over serial connection."""
import time
from typing import Optional, Type
from types import TracebackType
import serial
import console
from moses_exceptions import SerialError, LoginFailedError


class SerialConsole(console.GenericConsole):
    """Class implementing console features on serial port."""

    def __init__(self, device: str):
        """Configure serial connection.

        :param device: serial device (COM*: on Windows,/dev/tty* on Linux)
        :type device: str

        """
        super().__init__(device)
        try:
            self.ser = serial.Serial(
                device, 115200, 8, serial.PARITY_NONE, 1, 5)
        except serial.SerialException as exception:
            raise SerialError(exception) from exception
        self._prompt = ""

    def set_prompt(self, prompt: str) -> None:
        """Configure what should be recognized as prompt.

        :param prompt: prompt string
        :type prompt: str

        """
        self._prompt = prompt

    # Methods of the base console class
    def send_cmd(self, command: str, timeout: int = 30) -> str:
        """Send a command to the device and returns its output.

        :param command: command to be sent
        :type command: str
        :param timeout: timeout in seconds
        :tpye timeout: int
        :returns: output of the command (till next prompt)
        :rtype: str

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
                    raise TimeoutError()

                try:
                    output += self.ser.read_all().decode("utf-8")
                except UnicodeDecodeError:
                    continue

            return output[: len(output) - len(self._prompt)].strip()
        except serial.SerialException as exception:
            raise SerialError(exception) from exception
        except OSError as exception:
            raise OSError(exception) from exception

    def wait_for_prompt(
            self, prompt: Optional[str] = None, timeout: int = 30) -> None:
        """Wait until the specific string is received.

        :param prompt: prompt or None to use the one configured by set_prompt
            (Default value = None)
        :type prompt: str, optional
        :param timeout: timeout in seconds  (Default value = 30)
        :type timeout: int

        """
        output = ""

        if prompt is None:
            prompt = self._prompt

        self.ser.write("\n".encode("utf-8"))

        start = time.time()

        while not output.endswith(prompt):
            if time.time() - start > timeout:
                raise TimeoutError()

            try:
                output += self.ser.read_all().decode("utf-8")
            except UnicodeDecodeError:
                continue

    def _change_password(self, password: str) -> None:
        """Configure a temporary password on 1st login.

        :param password: password
        :type password: str

        """
        self.ser.write(password.encode("utf-8"))
        # write a dummy new passwordself.wait_for_prompt("New password: ")
        self.ser.write("thispasswordwontlast".encode("utf-8"))
        self.wait_for_prompt("Retype new password: ")
        # 2nd one requires \n because there is no waif_for_prompt,
        # # afterwardsself.ser.write("thispasswordwontlast\n".encode("utf-8"))
        time.sleep(5)

    def _restore_password(self, password: str) -> None:
        """Restores old password.

        :param password: password
        :type password: str
        """
        self.ser.write("passwd".encode("utf-8"))
        self.wait_for_prompt("Current password: ")
        self.ser.write("thispasswordwontlast".encode("utf-8"))
        self.wait_for_prompt("New password: ")
        self.ser.write(password.encode("utf-8"))
        self.wait_for_prompt("Retype new password: ")
        self.ser.write(password.encode("utf-8"))
        self.wait_for_prompt()

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

                except TimeoutError:
                    continue

                break

            if not loggedin:
                raise LoginFailedError()

            # wait for any prompt
            start = time.time()

            while self.ser.in_waiting == 0:
                if time.time() - start > timeout:
                    raise TimeoutError()

            time.sleep(10)
            prompt = self.ser.read_all().decode("utf-8")

            if "Login incorrect" in prompt:
                raise LoginFailedError()

            changepwd = False

            if "Current password:" in prompt:
                self._change_password(password)
                changepwd = True

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
                self._restore_password(password)

            time.sleep(5)
            self.ser.flush()
            self.ser.read_all()

        except serial.SerialException as exception:
            raise SerialError(exception) from exception
        except OSError as exception:
            raise OSError(exception) from exception

    def __enter__(self) -> "SerialConsole":
        """Ensure that serial object is managed correctly in with statements."""
        self.ser.__enter__()
        return self

    # pylint: disable = useless-return
    def __exit__(
        self,
        etype: Optional[Type[BaseException]],
        value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> Optional[bool]:
        """Ensure that serial object is managed correctly in with statements."""
        try:
            self.ser.write("exit\n".encode("utf-8"))
            self.ser.__exit__(etype, value, traceback)
        # pylint: disable = broad-except
        except Exception:
            pass
        return None
