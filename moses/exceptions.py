import sys
import inspect
import logging
import json
import flask
import docker
import os

from typing import Any, Optional, List, Dict

"""
Exceptions and tools to convert them to API response codes
When you add new errors, run this module to re-generate YAML
that can then be pasted inside the API file
"""


class MosesError(Exception):
    """
    Generic base class used to identify app-specific exceptions
    """

    code = -1
    description = ""

    def __init__(self, message=None, exception=None):

        self.exception = exception
        if message is None:
            self.message = (self).description
        else:
            self.message = message

        super().__init__(self.message)


class ObjectNotFound(MosesError):

    code = 404
    description = "Object not found"

    def __init__(self, obj_type, obj_id):
        super().__init__(message=f"{obj_type} {obj_id} not found.")


class InternalServerError(MosesError):

    code = 500
    description = "Unexpected exception."

    def __init__(self, e):
        super().__init__("Exception: " + str(e) if e is not None else "unknown")


class ImageNotFoundError(MosesError):

    code = 520
    description = "Container image not found on local host."

    def __init__(self, image):
        super().__init__("Image " + str(image) + " is not available.")


class IncompatibleDeviceError(MosesError):

    code = 521
    description = "Device is not compatible with selected platform."

    def __init__(self, device):
        super().__init__(
            "Device " + str(device) + " is not compatible with selected platform."
        )


class ConnectionError(MosesError):

    code = 522
    description = "Error communicating with device."

    def __init__(self, device, e):
        super().__init__(
            "Error communicating with device " + str(device) + " exception: " + str(e)
        )


class ContainerNotRunningError(MosesError):

    code = 523
    description = "Container is not running."

    def __init__(self, device, applicationid):
        super().__init__(
            "Container for app "
            + str(applicationid)
            + " is not running on device "
            + str(device)
        )


class SudoError(MosesError):

    code = 524
    description = "User is not enabled to execute commands as root."

    def __init__(self, username):
        super().__init__(
            "User " + str(username) + " is not enabled to execute commands as root."
        )


class DockerError(MosesError):
    def __init__(
        self,
        e: Any,
        log: Optional[List[str]] = None,
        info: Optional[Dict[str, str]] = None,
    ):
        message = "Docker exception: " + str(e)

        if info is not None:
            for key, value in info.items():
                message += f"{os.linesep}{key}:{value}"

        if log is not None:
            for logline in log:
                message += f"{os.linesep}{logline}"

        if isinstance(e, docker.errors.BuildError):
            for line in e.build_log:
                if "stream" in line:
                    message += os.linesep + line["stream"].strip()

        if isinstance(e, Exception):
            super().__init__(message, exception=e)
        else:
            super().__init__(message)


class RemoteDockerError(DockerError):

    code = 525
    description = "Remote docker exception."

    def __init__(
        self,
        device: Any,
        e: Any,
        log: Optional[List[str]] = None,
        info: Optional[Dict[str, str]] = None,
    ):
        remote_info = {"device": device}

        if info is not None:
            remote_info.update(info)
        super().__init__(e, log=log, info=remote_info)


class RemoteImageNotFoundError(MosesError):

    code = 526
    description = "Image not found on remote device."

    def __init__(self, image):
        super().__init__("Image " + str(image) + " is not available.")


class PlatformDoesNotRequireSDKError(MosesError):

    code = 527
    description = "Image not found on remote device."

    def __init__(self, platform_id):
        super().__init__(
            "Platform " + str(platform_id) + " does not require an SDK container."
        )


class PlatformDoesNotExistError(MosesError):

    code = 528
    description = "Platform does not exist."

    def __init__(self, platform_id):
        super().__init__("Platform " + str(platform_id) + " does not exist.")


class RemoteCommandError(MosesError):

    code = 529
    description = "Remote command execution failed."

    def __init__(self, command, errorcode):
        super().__init__(
            "Remote command " + str(command) + " returned error " + str(errorcode)
        )


class LocalDockerError(DockerError):

    code = 530
    description = "Local docker exception."

    def __init__(
        self,
        e: Any,
        log: Optional[List[str]] = None,
        info: Optional[Dict[str, str]] = None,
    ):
        super().__init__(e, log=log, info=info)


class InvalidObjectIdError(MosesError):

    code = 531
    description = "Object Does not have a valid id."

    def __init__(self):
        super().__init__()


class InvalidObjectStateError(MosesError):

    code = 532
    description = "Object cannot be saved because it's in an invalid state."

    def __init__(self, objid):
        super().__init__("Object " + str(objid) + " is in an invalid state.")


class SSHError(MosesError):
    code = 533
    description = "SSH error."

    def __init__(self, e):
        super().__init__("SSH error: " + str(e), exception=e)


class OSError(MosesError):
    code = 534
    description = "OS error."

    def __init__(self, e):
        super().__init__("OS error: " + str(e), exception=e)


class InvalidDeviceIdError(MosesError):
    code = 535
    description = "Invalid device id."

    def __init__(self):
        super().__init__()


class SerialError(MosesError):
    code = 536
    description = "Serial port error."

    def __init__(self, e):
        super().__init__("Serial port error: " + str(e), exception=e)


class TimeoutError(MosesError):
    code = 537
    description = "Command timeout."

    def __init__(self):
        super().__init__()


class LoginFailedError(MosesError):
    code = 538
    description = "Login failed."

    def __init__(self):
        super().__init__()


class SSHTunnelError(MosesError):
    code = 539
    description = "SSH tunnel error."

    def __init__(self, e):
        super().__init__("SSH tunnel error: " + str(e), exception=e)


class InvalidPathError(MosesError):
    code = 540
    description = "Invalid path."

    def __init__(self, path):
        super().__init__("Invalid path: " + str(path))


class SDKContainerNotRunningError(MosesError):
    code = 541
    description = "SDK container is not running."

    def __init__(self, applicationid):
        super().__init__(
            "SDK container for app " + str(applicationid) + " is not running."
        )


class PullImageError(MosesError):
    code = 542
    description = "Error pulling images from registry."

    def __init__(self, failed: list):
        message = "Can't pull images: " + ",".join(failed)
        super().__init__(message)


class SDKRequiresConfiguration(MosesError):
    code = 543
    description = (
        "Platform requires that a configuration is specified for SDK generation."
    )

    def __init__(self):
        super().__init__(
            "Platform requires debug/release configuration for SDK generation."
        )


class LocalCommandError(MosesError):

    code = 544
    description = "Local command execution failed."

    def __init__(self, result):
        message = (
            "Local command "
            + str(result.args)
            + " returned error "
            + str(result.returncode)
        )

        if result.stderr is not None:
            message = result.stderr.decode("utf-8")

        super().__init__(message)


class DNSError(MosesError):
    code = 545
    description = "Error resolving device hostname."

    def __init__(self, hostname):
        super().__init__("Can't find a valid IP for " + hostname)


class InvalidDeviceError(MosesError):
    code = 546
    description = "Device information is not valid."

    def __init__(self, device):
        super().__init__("Device information is not valid " + repr(device))


class InvalidModelError(MosesError):
    code = 547
    description = "Model id not recognized."

    def __init__(self, model):
        super().__init__("Model id not recognized " + model)


class SDKContainerNotFoundError(MosesError):
    code = 548
    description = "SDK container not found."

    def __init__(self, e):
        super().__init__("SDK Container not found: " + str(e), exception=e)


class ContainerDoesNotSupportSSH(MosesError):
    code = 549
    description = "Container does not support SSH."

    def __init__(self):
        super().__init__("Application container does not expose SSH port 2222")


class NoTagError(MosesError):
    code = 550
    description = "No tag has been specified for the image."

    def __init__(self):
        super().__init__(
            "No tag has been specified for the image, please set tag property before pushing."
        )


def encode_error(e: MosesError):

    fields = {"code": (e).code, "description": (e).description, "message": str(e)}

    logging.error("Error: %d %s %s", (e).code, (e).description, str(e))

    if e.exception is not None:
        logging.error("Exception: %s", str(e))
        logging.error(e.exception)

    return flask.Response(
        response=json.dumps(fields), status=(e).code, mimetype="application/json"
    )


def encode_exception(e):

    fields = {"code": 500, "description": "Internal server error", "message": str(e)}

    logging.error(e, exc_info=True)

    return flask.Response(
        response=json.dumps(fields), status=500, mimetype="application/json"
    )

