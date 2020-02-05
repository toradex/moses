import sys
import inspect
import logging
import json
import flask

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


class InternalServerError(MosesError):

    code = 500
    description = "Unexpected exception."

    def __init__(self, e):
        super().__init__("Exception: " +
                         str(e))


class ImageNotFoundError(MosesError):

    code = 520
    description = "Container image not found on local host."

    def __init__(self, image):
        super().__init__("Image " +
                         str(image) +
                         " is not available.")


class IncompatibleDeviceError(MosesError):

    code = 521
    description = "Device is not compatible with selected platform."

    def __init__(self, device):
        super().__init__("Device " +
                         str(device) +
                         " is not compatible with selected platform.")


class ConnectionError(MosesError):

    code = 522
    description = "Error communicating with device."

    def __init__(self, device, e):
        super().__init__("Error communicating with device " +
                         str(device) +
                         " exception: " +
                         str(e))


class ContainerNotRunningError(MosesError):

    code = 523
    description = "Container is not running."

    def __init__(self, device, applicationid):
        super().__init__("Container for app " +
                         str(applicationid) +
                         " is not running on device " +
                         str(device))


class SudoError(MosesError):

    code = 524
    description = "User is not enabled to execute commands as root."

    def __init__(self, username):
        super().__init__("User " +
                         str(username) +
                         " is not enabled to execute commands as root.")


class RemoteDockerError(MosesError):

    code = 525
    description = "Remote docker exception."

    def __init__(self, device, e):
        super().__init__("Docker error on device " +
                         str(device) +
                         ":" + str(e), exception=e)


class RemoteImageNotFoundError(MosesError):

    code = 526
    description = "Image not found on remote device."

    def __init__(self, image):
        super().__init__("Image " +
                         str(image) +
                         " is not available.")


class PlatformDoesNotRequireSDKError(MosesError):

    code = 527
    description = "Image not found on remote device."

    def __init__(self, platform_id):
        super().__init__("Platform " +
                         str(platform_id) +
                         " does not require an SDK container.")


class PlatformDoesNotExistError(MosesError):

    code = 528
    description = "Platform does not exist."

    def __init__(self, platform_id):
        super().__init__("Platform " +
                         str(platform_id) +
                         " does not exist.")


class RemoteCommandError(MosesError):

    code = 529
    description = "Remote command execution failed."

    def __init__(self, command, errorcode):
        super().__init__("Remote command " +
                         str(command) +
                         " returned error " +
                         str(errorcode))


class LocalDockerError(MosesError):

    code = 530
    description = "Local docker exception."

    def __init__(self, e):
        super().__init__("Docker exception: " +
                         str(e), exception=e)


class InvalidObjectIdError(MosesError):

    code = 531
    description = "Object Does not have a valid id."

    def __init__(self):
        super().__init__()


class InvalidObjectStateError(MosesError):

    code = 532
    description = "Object cannot be saved because it's in an invalid state."

    def __init__(self, objid):
        super().__init__("Object "+str(objid)+" is in an invalid state.")


class SSHError(MosesError):
    code = 533
    description = "SSH error."

    def __init__(self, e):
        super().__init__("SSH error: "+str(e), exception=e)


class OSError(MosesError):
    code = 534
    description = "OS error."

    def __init__(self, e):
        super().__init__("OS error: "+str(e), exception=e)


class InvalidDeviceIdError(MosesError):
    code = 535
    description = "Invalid device id."

    def __init__(self):
        super().__init__()


class SerialError(MosesError):
    code = 536
    description = "Serial port error."

    def __init__(self, e):
        super().__init__("Serial port error: "+str(e), exception=e)


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
        super().__init__("SSH tunnel error: "+str(e), exception=e)


class InvalidPathError(MosesError):
    code = 540
    description = "Invalid path."

    def __init__(self, path):
        super().__init__("Invalid path: "+str(path))


class SDKContainerNotRunningError(MosesError):
    code = 541
    description = "SDK container is not running."

    def __init__(self, applicationid):
        super().__init__("SDK container for app "
                         + str(applicationid)
                         + " is not running.")


class PullImageError(MosesError):
    code = 542
    description = "Error pulling images from registry."

    def __init__(self):
        super().__init__("Error pulling some of the image from registry.")


class SDKRequiresConfiguration(MosesError):
    code = 543
    description = "Platform requires that a configuration is specified for SDK generation."

    def __init__(self):
        super().__init__("Platform requires debug/release configuration for SDK generation.")


def encode_error(e: MosesError):

    fields = {
        "code": (e).code,
        "description": (e).description,
        "message": str(e)
    }

    logging.error("Error: %d %s %s", (e).code, (e).description, str(e))

    if e.exception is not None:
        logging.error("Exception: %s", str(e))
        logging.error(e.exception)

    return flask.Response(
        response=json.dumps(fields),
        status=(e).code,
        mimetype="application/json")


def encode_exception(e):

    fields = {
        "code": 500,
        "description": "Internal server error",
        "message": str(e)
    }

    logging.error(e, exc_info=True)

    return flask.Response(
        response=json.dumps(fields),
        status=500,
        mimetype="application/json")


# If we're running in stand alone mode, export the exceptions as yaml
# definitions that can be pasted in swagger.yaml
if __name__ == '__main__':

    print("responses:")

    classes = inspect.getmembers(sys.modules[__name__], inspect.isclass)
    sortedclasses = []

    for c in classes:
        if MosesError not in c[1].__bases__:
            continue

        sortedclasses.append(c[1])

    sortedclasses.sort(key=lambda c: c.code)

    p = 0

    for c in sortedclasses:

        if p == c.code:
            print("Invalid duplicated code: "+str(p))
            exit()

        p = c
        print("  "+c.__name__+"_"+str(c.code)+":")
        print("    description: "+c.description)
        print("    schema:")
        print("      $ref: \"#/definitions/ErrorInfo\"")
