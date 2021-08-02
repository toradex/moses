"""Module defining functions used during target device detection."""
import logging
from typing import TYPE_CHECKING, Dict, List
import console
from moses_exceptions import (
    SudoError,
    InvalidDeviceError,
    InvalidDeviceIdError)

# used to allow mypy to check types declared in a module
# that can't be imported directly to avoid cyclic import
if TYPE_CHECKING:
    import targetdevice


def unlock_ssh(
    console_: console.GenericConsole, dev: "targetdevice.TargetDevice", timeout: int
) -> None:
    """Enable ssh connection to the device without having to use a password.

    :param console_: serial or SSH console
    :type console_: console.GenericConsole
    :param dev: target device
    :type dev: "targetdevice.TargetDevice"
    :param timeout: timeout in seconds
    :type timeout: int

    """
    keysfile = console_.send_cmd("ls .ssh/authorized_keys", timeout)

    keys = None

    # file does not exists
    if keysfile != ".ssh/authorized_keys":
        keys = dev.publickey
    else:
        keys = console_.send_cmd("cat .ssh/authorized_keys", timeout)

        assert dev.publickey is not None

        if dev.publickey not in keys:
            keys += "\n" + dev.publickey

    assert keys is not None

    # regenerates the keys file
    console_.send_cmd("mkdir .ssh")
    console_.send_cmd('echo "' + keys + '" > .ssh/authorized_keys')
    console_.send_cmd("chmod 644 .ssh/authorized_keys")
    console_.send_cmd("chmod 700 .ssh")


def check_sudo(
    console_: console.GenericConsole, username: str, password: str
) -> None:
    """Check that user can run commands as root.

    If sudo is not enabled for the user, then an exception is rised

    :param console_: serial or SSH console
    :type console_: console.GenericConsole
    :param username: username
    :type username: str
    :param password: password
    :type password: str

    """
    if "sudo enabled" not in console_.send_cmd(
        'echo "' + password + '" | sudo -S echo "sudo enabled"'
    ):
        raise SudoError(username)


# pylint: disable = unnecessary-pass
# pylint: disable = unused-argument
# pylint: disable = fixme
def add_debug_warning(
        console_: console.GenericConsole, timeout: int) -> None:
    """Add a warning message at boot for devices where ide-connectivity has been enabled.

    :param console_: SSH or serial console
    :type console_: console.GenericConsole
    :param timeout: timeout in seconds
    :type timeout: int
    """
    # TODO add a warning to boot scripts
    pass


def reboot_device(console_: console.GenericConsole,
                  password: str) -> None:
    """Reboot target device at the end of setup process.

    :param console: serial or SSH console
    :type console: console.GenericConsole
    :param password: password
    :type password: str

    """
    try:
        console_.send_cmd("echo " + password + " | sudo -S reboot", 0)
    except TimeoutError:
        pass


def enable_docker_interface(
    console_: console.GenericConsole, timeout: int, password: str
) -> None:
    """Enable docker TCP/IP interface on localhost.

    :param console: serial or SSH console
    :type console: console.GenericConsole
    :param timeout: timeout in seconds
    :type timeout: int
    :param password: password
    :type password: str

    """
    # checks if override folder exists
    folder = (
        console_.send_cmd(
            "echo "
            + password
            + " | sudo -S ls /etc/systemd/system/docker.service.d 2> /dev/null",
            timeout,
        )
        .strip()
        .rstrip("\x00")
    )

    # creates it
    if len(folder) == 0:
        console_.send_cmd(
            "echo "
            + password
            + " | sudo -S  mkdir -p /etc/systemd/system/docker.service.d",
            timeout,
        )

    # creates override file
    console_.send_cmd(
        "echo " + password + " | sudo -S sh -c \"echo '[Service]\n"
        "ExecStart=\n"
        "ExecStart=/usr/bin/dockerd -H fd:// -H tcp://127.0.0.1:2375\n"
        "' > /etc/systemd/system/docker.service.d/override.conf\"",
        timeout,
    )


def get_version_info_from_console(
    console_: console.GenericConsole, dev: "targetdevice.TargetDevice", timeout: int
) -> None:
    """Collect device version info from a console.

    :param console_: serial or SSH console
    :type console_: console.GenericConsole
    :param dev: target device
    :type dev: "targetdevice.TargetDevice"
    :param timeout: timeout in seconds
    :type timeout: int

    """
    dev.hwrev = console_.send_cmd(
        "cat /proc/device-tree/toradex,board-rev", timeout
    ).rstrip("\x00")

    # Community device
    if "No such file or directory" in dev.hwrev:
        dev.hwrev = "v?.?"

    dev.kernelrelease = console_.send_cmd(
        "uname -r", timeout).rstrip("\x00\n")

    dev.kernelversion = console_.send_cmd(
        "uname -v", timeout).rstrip("\x00\n")

    dev.distroversion = (
        console_.send_cmd(
            "cat /usr/lib/os-release | grep PRETTY_NAME=", timeout)
        .rstrip("\x00")
        .strip()
    )

    dev.distroversion = dev.distroversion.lstrip("PRETTY_NAME=")
    dev.distroversion = dev.distroversion.strip('"')

# dictionary with supported modules
MODELS : Dict[str,List[str]] =  {
"0014": ["colibri-imx6","Colibri iMX6S 256MB","arm7vl"],
"0015": ["colibri-imx6","Colibri iMX6DL 512MB","arm7vl"],
"0016": ["colibri-imx6","Colibri iMX6S 256MB IT","arm7vl"],
"0017": ["colibri-imx6","Colibri iMX6DL 512MB IT","arm7vl"],
"0027": ["apalis-imx6","Apalis iMX6Q 1GB","arm7vl"],
"0028": ["apalis-imx6","Apalis iMX6Q 2GB IT","arm7vl"],
"0029": ["apalis-imx6","Apalis iMX6D 512MB","arm7vl"],
"0032": ["colibri-imx7","Colibri iMX7S 256MB","arm7vl"],
"0033": ["colibri-imx7","Colibri iMX7D 512MB","arm7vl"],
"0035": ["apalis-imx7","Apalis iMX6D 1GB IT","arm7vl"],
"0036": ["colibri-imx6ull","Colibri iMX6ULL 256MB","arm7vl"],
"0037": ["apalis-imx8","Apalis iMX8QM 4GB WB IT","aarch64"],
"0038": ["colibri-imx8","Colibri iMX8QXP 2GB WB IT","aarch64"],
"0039": ["colibri-imx7","Colibri iMX7D 1GB","arm7vl"],
"0040": ["colibri-imx6ull","Colibri iMX6ULL 512MB WB IT","arm7vl"],
"0044": ["colibri-imx6ull","Colibri iMX6ULL 512MB IT","arm7vl"],
"0045": ["colibri-imx6ull","Colibri iMX6ULL 512MB WB","arm7vl"],
"0046": ["apalis-imx8x","Apalis iMX8QXP 2GB WB IT","aarch64"],
"0047": ["apalis-imx8","Apalis iMX8QM 4GB IT","aarch64"],
"0048": ["apalis-imx8","Apalis iMX8QP 2GB WB","aarch64"],
"0049": ["apalis-imx8","Apalis iMX8QP 2GB","aarch64"],
"0050": ["colibri-imx8","Colibri iMX8QXP 2GB IT","aarch64"],
"0051": ["colibri-imx8","Colibri iMX8DX 1GB WB","aarch64"],
"0052": ["colibri-imx8","Colibri iMX8DX 1GB","aarch64"],
"0053": ["apalis-imx8x","Apalis iMX8QXP 2GB ECC IT","aarch64"],
"0054": ["apalis-imx8x","Apalis iMX8DXP 1GB","aarch64"],
"0055": ["verdin-imx8","Verdin iMX8M Mini Quad 2GB WB IT","aarch64"],
"0056": ["verdin-imx8","Verdin iMX8M Nano Quad 1GB WB","aarch64"],
"0057": ["verdin-imx8","Verdin iMX8M Mini DualLite 1GB","aarch64"],
"0058": ["verdin-imx8","Verdin iMX8M Plus Quad 4GB WB IT","aarch64"],
"0059": ["verdin-imx8","Verdin iMX8M Mini Quad 2GB IT","aarch64"],
"0060": ["verdin-imx8","Verdin iMX8M Mini DualLite 1GB WB IT","aarch64"],
"0061": ["verdin-imx8","Verdin iMX8M Plus Quad 2GB","aarch64"],
"0062": ["colibri-imx6ull","Colibri iMX6ULL 1GB IT","arm7vl"],
"0063": ["verdin-imx8","Verdin iMX8M Plus Quad 4GB IT","aarch64"],
"0064": ["verdin-imx8","Verdin iMX8M Plus Quad 2GB WB IT","aarch64"],
"0065": ["verdin-imx8","Verdin iMX8M Plus QuadLite 1GB IT","aarch64"],
"0066": ["verdin-imx8","Verdin iMX8M Plus Quad 8GB WB","aarch64"]
}

def _get_hostname_from_model(model: str) -> str:
    """Return default hostname for specific model.

    :param model: model string
    :type model: str

    :returns: device name prefix
    :rtype: str

    """
    if model in MODELS:
        return MODELS[model][0]
    return "toradex-"+model


def setup_device_from_console(dev: "targetdevice.TargetDevice",
                              console_: console.GenericConsole, timeout: int
                              ) -> "targetdevice.TargetDevice":
    """Create a new device collecting its information from the console.

    :param console: serial or SSH console
    :type console: console.GenericConsole
    :param timeout: timeout in seconds
    :type timeout: int
    :returns: device object
    :rtype: targetdevice.TargetDevice

    """
    dev.id = console_.send_cmd(
        "cat /proc/device-tree/serial-number", timeout
    ).rstrip("\x00")

    dev.cpu_architecture = console_.send_cmd(
        "arch"
    ).strip()

    # Toradex Devices has product Id
    productid = console_.send_cmd(
        "cat /proc/device-tree/toradex,product-id", timeout
    ).rstrip("\x00")

    if "No such file or directory" not in productid:
        logging.info("DETECT - Toradex device id %s", dev.id)
        dev.model = productid
        dev.hostname = _get_hostname_from_model(dev.model)
    elif len(str(dev.id)) > 0:
        logging.info("DETECT - Community device id %s", dev.id)
        dev.runningtorizon = False

        # Check if the distro have docker
        dockercheck = console_.send_cmd("ls /var/run/docker.sock", timeout).rstrip(
            "\x00"
        )

        if "No such file or directory" in dockercheck:
            logging.info(
                "Docker socket not present, make sure you\
                    have docker installed and running on your board.")
            raise InvalidDeviceError(dev)

        # Check if the board in running arm or arm64
        archcheck = console_.send_cmd("arch", timeout).rstrip("\x00")

        if "arm" not in archcheck:
            logging.info("Unsupported architecture %s", archcheck)
            raise InvalidDeviceError(dev)

        # Community Devices has Model name
        dev.model = console_.send_cmd("cat /proc/device-tree/model", timeout).rstrip(
            "\x00"
        )

        dev.hostname = console_.send_cmd(
            "cat /etc/hostname", timeout).rstrip("\x00")
        # make sure to resolve it with .local
        dev.hostname += ".local"
    else:
        raise InvalidDeviceIdError()

    logging.info(
        "DETECT - %s detected :: Model %s",
        dev.hostname,
        dev.model)

    dev.name = (
        console_.send_cmd(
            "cat /proc/device-tree/model",
            timeout).rstrip("\x00")
        + "("
        + dev.id
        + ")"
    )

    dev.hostname = console_.send_cmd(
        "hostname", timeout).rstrip("\x00").strip()
    # make sure to resolve it with .local
    dev.hostname += ".local"

    dev.homefolder = console_.send_cmd(
        "echo $HOME", timeout).rstrip("\x00").strip()

    get_version_info_from_console(console_, dev, timeout)

    if not dev.is_valid():
        logging.warning("DETECT - Device information is not valid.")
        logging.warning(repr(dev))
        raise InvalidDeviceError(dev)
    return dev
