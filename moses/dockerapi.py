"""This module export some functions that access low-level docker api.

This is required to provide some kind of progress during the operation, 
since high-level API is based on REST calls.add()
"""
import six
import json
import re
import progresscookie
import io
import logging
from docker import APIClient, DockerClient
from docker.errors import BuildError
from docker.models.images import Image
from typing import Optional, List, Dict, Tuple, Any
from exceptions import LocalDockerError, RemoteDockerError


def build_image(
    client: DockerClient,
    path: str,
    dockerfile: str,
    tag: str,
    platform: Optional[str],
    progress: Optional[progresscookie.ProgressCookie],
) -> Optional[Image]:
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

    for r in resp:

        for l in r.decode("utf-8").split("\r\n"):

            if len(l) == 0:
                continue
            try:
                line = json.loads(l)
            except Exception as e:
                logging.error(f"Invalid json string {l}")
                logging.exception(e)
                continue

            if "stream" in line:
                if progress is not None:
                    progress.append_message(line["stream"])
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
    else:
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
            if progress is not None:
                progress.append_message(line["stream"])
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
            if progress is not None:
                progress.append_message(msg)
            output.append(line["status"])
        if "error" in line:
            info = None
            if "errorDetail" in line:
                info = line["errorDetail"]
            raise RemoteDockerError(device, line["error"], log=output, info=info)

    if image_id is not None:
        return client.images.get(image_id)
    else:
        return None


def push_image(
    client: DockerClient,
    repository: str,
    tag: Optional[str],
    username: str,
    password: str,
    progress: Optional[progresscookie.ProgressCookie],
) -> None:
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

    resp = apiclient.push(repository, tag, auth_config=auth_config, stream=True)

    output: List[str] = []
    ids: Dict[str, Tuple[str, int, int]] = {}

    for r in resp:

        for l in r.decode("utf-8").split("\r\n"):

            if len(l) == 0:
                continue

            print(l)

            try:
                line = json.loads(l)
            except Exception as e:
                logging.error(f"Invalid json string {l}")
                logging.exception(e)
                continue

            if "stream" in line:
                if progress is not None:
                    progress.append_message(line["stream"])
                output.append(line["stream"])
            if "status" in line:

                if progress is not None:

                    cur = 0
                    tot = 0

                    if "id" in line:
                        id = line["id"]

                        if "progressDetail" in line:

                            detail = line["progressDetail"]
                            if "current" in detail:
                                cur = detail["current"]
                            if "total" in detail:
                                tot = detail["total"]

                        if id not in ids or line["status"] != ids[id][0]:
                            ids[id] = (line["status"], cur, tot)

                            progress.append_message(line["status"] + " " + id)

                        if tot != 0:
                            ids[id] = (line["status"], cur, tot)

                            gc = 0
                            gt = 0

                            for i in ids.values():
                                gc += i[1]
                                gt += i[2]

                            progress.set_minmax(0, gt)
                            progress.set_progress_minmax(gc)
            if "error" in line:
                info = None
                if "errorDetail" in line:
                    info = line["errorDetail"]
                raise LocalDockerError(line["error"], log=output, info=info)
