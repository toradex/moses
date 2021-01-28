"""Functions used to execute rsync.

Rsync is used to deploy files between local PC and the device.
Files can be on the local filesystems or in containers.
Functions work also on Windows, translating paths and relying on 
rsync provided by WSL.
"""
import platform
import subprocess
import exceptions
import targetdevice
import socket
import sharedssh
import progresscookie
from typing import Optional, List

should_translate_path: bool = False
should_create_tmp_key: bool = False
rsync_cmd: List[str] = ["rsync"]

if platform.system() == "Windows":
    should_translate_path = True
    should_create_tmp_key = True
    rsync_cmd = ["wsl.exe", "rsync"]


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
        raise exceptions.LocalCommandError(result)

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
        raise exceptions.LocalCommandError(result)

    tmppath = result.stdout.decode("utf-8").strip("\n")

    result = subprocess.run(["wsl.exe", "cp", keypath, tmppath], stderr=subprocess.PIPE)

    if result.returncode != 0:
        raise exceptions.LocalCommandError(result)

    result = subprocess.run(
        ["wsl.exe", "chmod", "600", tmppath], stderr=subprocess.PIPE
    )

    if result.returncode != 0:
        raise exceptions.LocalCommandError(result)

    return tmppath


def remove_tmp_key(keypath: str) -> None:
    """Remove a key created with create_tmp_key.

    :param kepath: Linux path
    :type keypath: str

    """
    subprocess.run(["wsl.exe", "rm", keypath], stderr=subprocess.PIPE)


def run_rsync(
    sourcefolder: str,
    device_id: str,
    targetfolder: str,
    keypath: Optional[str] = None,
    port: int = None,
    progress: Optional[progresscookie.ProgressCookie] = None,
) -> None:
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

    try:
        ip, mdns = sharedssh.resolve_hostname(device.hostname)
    except socket.gaierror:
        raise exceptions.DNSError(device.hostname)

    if device is None:
        raise exceptions.InvalidDeviceIdError()

    if should_translate_path:
        sourcefolder = translate_path(sourcefolder)

    if keypath is None:
        keypath = device.get_privatekeypath()

    assert keypath is not None

    if port is None:
        port = 22

    try:

        if should_translate_path:
            keypath = translate_path(keypath)

        if should_create_tmp_key:
            keypath = create_tmp_key(keypath)

        if not sourcefolder.endswith("/"):
            sourcefolder += "/"

        if not targetfolder.endswith("/"):
            targetfolder += "/"

        assert device.username is not None

        rsync_args = rsync_cmd + [
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
            device.username + "@" + ip + ":" + targetfolder,
        ]

        process = subprocess.Popen(
            rsync_args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
        )

        if progress is not None:

            assert process.stdout is not None

            while process.poll() is None:
                progress.append_message(process.stdout.readline().decode("utf-8"))
        else:
            process.wait()

        if process.returncode != 0:
            raise exceptions.LocalCommandError(process)

    finally:

        if should_create_tmp_key:
            remove_tmp_key(keypath)

