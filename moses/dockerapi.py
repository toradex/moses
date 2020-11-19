import six
import json
import re
import progresscookie
import targetdevice
import io
import logging
import os
from docker import APIClient, DockerClient
from docker.errors import BuildError
from docker.models.images import Image
from typing import Optional, List
from exceptions import LocalDockerError, RemoteDockerError


def build_image(
    client: DockerClient,
    path: str,
    dockerfile: str,
    tag: str,
    platform: Optional[str],
    progress: Optional[progresscookie.ProgressCookie],
) -> Optional[Image]:
    """builds an image returning messages generated during the operation

    Args:
        client (DockerClient): client
        path (str): path of the image folder
        dockerfile (str): dockerfile path
        tag (str): tag to be assigned to the newly built image
        progress (Optional[ProgressCookie]): progress object or None

    Returns:
        Image - Docker image or None
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
    def __init__(
        self, reader: io.BufferedReader, progress: progresscookie.ProgressCookie
    ):
        self.progress = progress
        super().__init__(reader.raw)

    def read(self, size):
        buffer = super().read(size)
        self.progress.update_progress_minmax(len(buffer))
        return buffer

    def read1(self, size):
        buffer = super().read1(size)
        self.progress.update_progress_minmax(len(buffer))
        return buffer


def load_image(
    client: DockerClient,
    filepath: str,
    device,
    progress: Optional[progresscookie.ProgressCookie],
) -> Optional[Image]:
    """[summary]

    Args:
        client (DockerClient): client
        filepath (str): path of the tar file to be imported
        progress (Optional[ProgressCookie]): progress object or None

    Returns:
        Optional[Image]: Image or None
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
