import os
import platform
import subprocess
import exceptions
import targetdevice
import logging
import socket

if platform.system() == "Windows":
    should_translate_path = True
    should_create_tmp_key = True
    rsync_cmd = ["wsl.exe", "rsync"]
else:
    should_translate_path = False
    should_create_tmp_key = False
    rsync_cmd = ["rsync"]


def translate_path(originalpath) -> str:
    """Translate Windows path to Linux

    Arguments:
        originalpath {str} -- original path

    Returns:
        str -- path that is valid inside WSL
    """

    originalpath = originalpath.replace("\\", "/")

    result = subprocess.run(
        ["wsl.exe", "wslpath", originalpath], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if result.returncode != 0:
        raise exceptions.LocalCommandError(result)

    return result.stdout.decode("utf-8").rstrip('\n')


def create_tmp_key(keypath) -> str:
    """Create a temporary dummy key and set access rights
    to be able to use it with ssh

    Arguments:
        keypath {path} - - [description]

    Returns:
        str -- path of temp key
    """
    result = subprocess.run(["wsl.exe", "mktemp"],
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if result.returncode != 0:
        raise exceptions.LocalCommandError(result.stderr)

    tmppath = result.stdout.decode("utf-8").strip("\n")

    result = subprocess.run(
        ["wsl.exe", "cp", keypath, tmppath], stderr=subprocess.PIPE)

    if result.returncode != 0:
        raise exceptions.LocalCommandError(result.stderr)

    result = subprocess.run(
        ["wsl.exe", "chmod", "600", tmppath], stderr=subprocess.PIPE)

    if result.returncode != 0:
        raise exceptions.LocalCommandError(result.stderr)

    return tmppath


def remove_tmp_key(keypath):
    """Removes a key created with create_tmp_key

    Arguments:
        kepath {str} -- path of the key
    """
    subprocess.run(["wsl.exe", "rm", keypath], stderr=subprocess.PIPE)


def run_rsync(sourcefolder, deviceid, targetfolder, keypath=None, port=None):
    """Syncs a folder from the host PC to target

    Arguments:
        sourcefolder {str} -- source path
        deviceid {str} -- target device
        targetfolder {str} -- target path
    """

    device = targetdevice.TargetDevices()[deviceid]

    try:
        ip = socket.gethostbyname(device.hostname)
    except socket.gaierror:
        raise exceptions.DNSError(device.hostname)

    if device == None:
        raise exceptions.InvalidDeviceIdError()

    if should_translate_path:
        sourcefolder = translate_path(sourcefolder)

    if keypath is None:
        keypath = device.get_privatekeypath()

    if port is None:
        port = 22

    if should_translate_path:
        keypath = translate_path(keypath)

    if should_create_tmp_key:
        keypath = create_tmp_key(keypath)

    if not sourcefolder.endswith("/"):
        sourcefolder += "/"

    if not targetfolder.endswith("/"):
        targetfolder += "/"

    rsync_args = rsync_cmd + ["-r", "-z", "-l",
                              "-p", "-g", "-o", "-t", "-q", "-e",
                              "ssh -p " + str(port) + " -q -i '" + keypath +
                              "' -o 'StrictHostKeyChecking no' -o 'UserKnownHostsFile /dev/null'",
                              sourcefolder,
                              device.username+"@"+ip+":"+targetfolder]

    result = subprocess.run(
        rsync_args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    if should_create_tmp_key:
        remove_tmp_key(keypath)

    if result.returncode != 0:
        raise exceptions.LocalCommandError(result)
