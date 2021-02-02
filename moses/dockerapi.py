"""This module export some functions that access low-level docker api.

This is required to provide some kind of progress during the operation,
since high-level API is based on REST calls.add()
"""
import json
import re
import io
import logging
from typing import Optional, List, Dict, Tuple, Any
import six
from docker import DockerClient
from docker.models.images import Image
import progresscookie
from moses_exceptions import LocalDockerError, RemoteDockerError

#pylint: disable = too-many-arguments


def build_image(client: DockerClient,
                path: str,
                dockerfile: str,
                tag: str,
                platform: Optional[str],
                progress: Optional[progresscookie.ProgressCookie]) -> Optional[Image]:
    """Build an image returning messages generated during the operation.

    :param client: docker API client
    :type client: DockerClient
    :param path: path of the image folder
    :type path: str
    :param dockerfile: dockerfile path
    :type dockerfile: str
    :param tag: tag to be assigned to the newly built image
    :type tag: str
    :param progress: progress object or None
    :type progress: progresscookie.ProgressCookie, optional

    :returns: Docker image or None
    :rtype: Image

    """
    apiclient = client.api

    resp = apiclient.build(
        path=path, dockerfile=dockerfile, tag=tag, pull=True, platform=platform
    )

    image_id = None
    output: List[str] = []

    if isinstance(resp, six.string_types):
        return client.images.get(resp)

    for responsestring in resp:

        for responseline in responsestring.decode("utf-8").split("\r\n"):

            if len(responseline) == 0:
                continue
            try:
                line = json.loads(responseline)
            # pylint: disable = broad-except
            except Exception as exception:
                logging.error(f"Invalid json string {responseline}")
                logging.exception(exception)
                continue

            if "stream" in line:
                progresscookie.progress_message(progress, line["stream"])
                output.append(line["stream"])
            if "aux" in line:
                image_id = line["aux"]["ID"]
            if "message" in line:
                info = None
                raise LocalDockerError(line["message"], log=output, info=info)
            if "error" in line:
                info = None
                if "errorDetail" in line:
                    info = line["errorDetail"]
                raise LocalDockerError(line["error"], log=output, info=info)

    if image_id is not None:
        return client.images.get(image_id)
    return None


class ReadProgress(io.BufferedReader):
    """Helper class used to retrieve messages during deploy operation.

    The class wraps a BufferedReader and returns progress information
    during read operations.
    """

    def __init__(
        self, reader: io.BufferedReader, progress: progresscookie.ProgressCookie
    ) -> None:
        """Initialize object.

        :param reader: original reader that will be wrapped by the class
        :type reader: io.BufferedReader
        :param progress: object used to report progress
        :type progress: progresscookie.ProgressCookie
        """
        self.progress = progress
        super().__init__(reader.raw)

    def read(self, size: Optional[int] = None) -> bytes:
        """Return data and update progress.

        :param size: number of bytes to read
        :type size: int

        """
        buffer = super().read(size)
        self.progress.update_progress_minmax(len(buffer))
        return buffer

    def read1(self, size: int = 0) -> bytes:
        """Return data and update progress.

        :param size: number of bytes to read
        :type size: int

        """
        buffer = super().read1(size)
        self.progress.update_progress_minmax(len(buffer))
        return buffer


def load_image(
    client: DockerClient,
    filepath: str,
    device: Any,
    progress: Optional[progresscookie.ProgressCookie],
) -> Optional[Image]:
    """Load an image on the target device.

    :param client: client
    :type client: DockerClient
    :param filepath: path of the tar file to be imported
    :type filepath: str
    :param device: destination device
    :param progress: progress object or None
    :type progress: progresscookie.ProgressCookie, optional

    :returns: Image or None
    :rtype: Image | None

    """
    apiclient = client.api

    with open(filepath, "rb", buffering=1024 * 1024) as inp:

        if progress is None:
            resp = apiclient.load_image(inp, quiet=True)
        else:
            assert isinstance(inp, io.BufferedReader)
            progressinp = ReadProgress(inp, progress)
            resp = apiclient.load_image(progressinp, quiet=False)

    output = []
    image_id = None

    for line in resp:

        if "stream" in line:
            progresscookie.progress_message(progress, line["stream"])
            output.append(line["stream"])

            match = re.search(
                r"(^Loaded image ID: |^Loaded image: )(.+)$", line["stream"]
            )

            if match is not None:
                image_id = match.group(2)
        if "status" in line:
            msg = line["status"]
            if "id" in line:
                msg += " - " + line["id"]
            progresscookie.progress_message(progress, msg)
            output.append(line["status"])
        if "error" in line:
            info = None
            if "errorDetail" in line:
                info = line["errorDetail"]
            raise RemoteDockerError(
                device, line["error"], log=output, info=info)

    if image_id is not None:
        return client.images.get(image_id)
    return None


def _update_push_progress(progress: progresscookie.ProgressCookie,
                          ids: Dict[str, Tuple[str, int, int]], line: Dict[str, Any]) -> None:
    """Sum all progress repos from all the layers and update progress object.

    :param progress: object used to report operation progress
    :type progress: progresscookie.ProgressCookie
    :param ids: dictionary with all the layers
    :type ids: dict
    :param line: output line (parsed from json)
    :type line: dict
    """
    cur = 0
    tot = 0
    if "id" in line:
        lineid = line["id"]
        if "progressDetail" in line:
            detail = line["progressDetail"]
            if "current" in detail:
                cur = detail["current"]
            if "total" in detail:
                tot = detail["total"]
        if lineid not in ids or line["status"] != ids[lineid][0]:
            ids[lineid] = (line["status"], cur, tot)
            progress.append_message(
                line["status"] + " " + lineid)
        if tot != 0:
            ids[lineid] = (line["status"], cur, tot)
            current = 0
            total = 0
            for i in ids.values():
                current += i[1]
                total += i[2]
            progress.set_minmax(0, total)
            progress.set_progress_minmax(current)


# pylint: disable = too-many-locals
def push_image(client: DockerClient,
               repository: str,
               tag: Optional[str],
               username: str,
               password: str,
               progress: Optional[progresscookie.ProgressCookie]) -> None:
    """Push an image, returning messages generated during the operation via progress.

    :param client: client
    :type client: DockerClient
    :param repository: full path to docker registry
    :type repository: str
    :param tag: tag to be assigned to the newly built image
    :type tag: str
    :param username: username for registry authentication
    :type username: str
    :param password: password/token
    :type password: str
    :param progress: progress object or None
    :type progress: progresscookie.ProgressCookie, optional

    """
    apiclient = client.api

    auth_config = {"username": username, "password": password}

    resp = apiclient.push(
        repository,
        tag,
        auth_config=auth_config,
        stream=True)

    output: List[str] = []
    ids: Dict[str, Tuple[str, int, int]] = {}

    for responsestring in resp:

        for responseline in responsestring.decode("utf-8").split("\r\n"):

            if len(responseline) == 0:
                continue

            print(responseline)

            try:
                line = json.loads(responseline)
            # pylint: disable = broad-except
            except Exception as exception:
                logging.error(f"Invalid json string {responseline}")
                logging.exception(exception)
                continue

            if "stream" in line:
                progresscookie.progress_message(progress, line["stream"])
                output.append(line["stream"])
            if "status" in line:
                if progress is not None:
                    _update_push_progress(progress, ids, line)
            if "error" in line:
                info = None
                if "errorDetail" in line:
                    info = line["errorDetail"]
                raise LocalDockerError(line["error"], log=output, info=info)
