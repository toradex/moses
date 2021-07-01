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
                device, 115200,
                serial.EIGHTBITS, serial.PARITY_NONE,
                serial.STOPBITS_ONE, 5)
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
        except (TimeoutError,UnicodeDecodeError):
            raise
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
        self.wait_for_prompt("New password: ")

        self.ser.write("thispasswordwontlast".encode("utf-8"))
        self.wait_for_prompt("Retype new password: ")

        # 2nd one requires \n because there is no waif_for_prompt
        self.ser.write("thispasswordwontlast\n".encode("utf-8"))
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
            changepwd = False
            start = time.time()
            self.ser.flush()

            while time.time() - start < timeout:

                try:
                    # <ENTER>
                    self.ser.write("\n".encode("utf-8"))
                    self.wait_for_prompt("login: ")

                    # input username
                    self.ser.write(username.encode("utf-8"))
                    self.wait_for_prompt("Password: ")

                    # input password
                    self.ser.write(password.encode("utf-8"))
                    self.ser.write("\n".encode("utf-8"))

                    # wait for get response
                    start2 = time.time()
                    while self.ser.in_waiting == 0:
                        if time.time() - start2 > timeout:
                            raise TimeoutError()

                    time.sleep(10)
                    output = self.ser.read_all().decode("utf-8")

                    # succes?
                    if "~$" in output:
                        loggedin = True
                    # we need to change passwd
                    elif "Current password: " in output:
                        self._change_password(password)
                        changepwd = True
                        loggedin = True

                    break

                except TimeoutError:
                    self.ser.write("exit\n".encode("utf-8"))
                    continue

            if not loggedin:
                raise LoginFailedError()

            # wait for prompt
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
        except TimeoutError as exception:
            raise TimeoutError(exception) from exception
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
