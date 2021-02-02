"""Functions used to execute rsync.

Rsync is used to deploy files between local PC and the device.
Files can be on the local filesystems or in containers.
Functions work also on Windows, translating paths and relying on
rsync provided by WSL.
"""
import platform
import subprocess
import socket
from typing import Optional, List
import targetdevice
import nameresolution
import progresscookie
from moses_exceptions import LocalCommandError, DNSError

SHOULD_TRANSLATE_PATH: bool = False
SHOULD_CREATE_TMP_KEY: bool = False
RSYNC_CMD: List[str] = ["rsync"]

if platform.system() == "Windows":
    SHOULD_TRANSLATE_PATH = True
    SHOULD_CREATE_TMP_KEY = True
    RSYNC_CMD = ["wsl.exe", "rsync"]

# we check return code to encapsulate exception
# pylint: disable = subprocess-run-check


def translate_path(originalpath: str) -> str:
    """Translate Windows path to Linux.

    :param originalpath: Windows path
    :type originalpath: str
    :returns: Linux path that is valid inside WSL
    :rtype: str

    """
    originalpath = originalpath.replace("\\", "/")

    result = subprocess.run(
        ["wsl.exe", "wslpath", originalpath],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    if result.returncode != 0:
        raise LocalCommandError(result)

    return result.stdout.decode("utf-8").rstrip("\n")


def create_tmp_key(keypath: str) -> str:
    """Create a temporary dummy key.

    Create the file and set access rights to be able to use it with ssh/rsync.

    :param keypath: Linux path of the key file
    :type keypath: str
    :returns: path of temp key
    :rtype: str

    """
    result = subprocess.run(
        ["wsl.exe", "mktemp"], stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )

    if result.returncode != 0:
        raise LocalCommandError(result)

    tmppath = result.stdout.decode("utf-8").strip("\n")

    result = subprocess.run(
        ["wsl.exe", "cp", keypath, tmppath], stderr=subprocess.PIPE)

    if result.returncode != 0:
        raise LocalCommandError(result)

    result = subprocess.run(
        ["wsl.exe", "chmod", "600", tmppath], stderr=subprocess.PIPE
    )

    if result.returncode != 0:
        raise LocalCommandError(result)

    return tmppath


def remove_tmp_key(keypath: str) -> None:
    """Remove a key created with create_tmp_key.

    :param kepath: Linux path
    :type keypath: str

    """
    subprocess.run(["wsl.exe", "rm", keypath], stderr=subprocess.PIPE)


# pylint: disable = too-many-arguments
# pylint: disable = too-many-branches
def run_rsync(
        sourcefolder: str,
        device_id: str,
        targetfolder: str,
        keypath: Optional[str] = None,
        port: int = None,
        progress: Optional[progresscookie.ProgressCookie] = None) -> None:
    """Sync a folder from the host PC to target.

    :param sourcefolder: source folder
    :type sourcefolder: str
    :param device_id: device id
    :type device_id: str
    :param targetfolder: destination folder (on target)
    :type targetfolder: str
    :param keypath: local path of the SSH key used to authenticate (None will use device key)
    :type keypath: str
    :param port: port used for SSH connection (None will use 22)
    :type port: int
    :param progress: object used to report operation's progress  (Default value = None)
    :type progress: progresscookie.ProgressCookie, optional

    """
    device = targetdevice.TargetDevices()[device_id]

    assert device is not None

    try:
        ipaddress, _ = nameresolution.resolve_hostname(device.hostname)
    except socket.gaierror as exception:
        raise DNSError(device.hostname) from exception

    if keypath is None:
        keypath = device.get_privatekeypath()

    assert keypath is not None

    port = 22 if port is None else port

    try:

        if SHOULD_TRANSLATE_PATH:
            sourcefolder = translate_path(sourcefolder)
            keypath = translate_path(keypath)

        if SHOULD_CREATE_TMP_KEY:
            keypath = create_tmp_key(keypath)

        if not sourcefolder.endswith("/"):
            sourcefolder += "/"

        if not targetfolder.endswith("/"):
            targetfolder += "/"

        assert device.username is not None

        rsync_args = RSYNC_CMD + [
            "-r",
            "-z",
            "-l",
            "-p",
            "-g",
            "-o",
            "-t",
            "-q" if progress is None else "-v",
            "-e",
            "ssh -p "
            + str(port)
            + " -q -i '"
            + keypath
            + "' -o 'StrictHostKeyChecking no' -o 'UserKnownHostsFile /dev/null'",
            sourcefolder,
            device.username + "@" + ipaddress + ":" + targetfolder,
        ]

        process = subprocess.Popen(
            rsync_args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
        )

        if progress is not None:

            assert process.stdout is not None

            while process.poll() is None:
                progress.append_message(
                    process.stdout.readline().decode("utf-8"))
        else:
            process.wait()

        if process.returncode != 0:
            raise LocalCommandError(process)

    finally:

        if SHOULD_CREATE_TMP_KEY:
            remove_tmp_key(keypath)
