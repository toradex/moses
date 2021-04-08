"""Image build features of ApplicationConfig class.

The class is too complex to stay in a single file, code has been
splitted in feature-specific modules.
This is why sometimes you see calls with self explicitely passed
as first parameter.
"""
import os
import shutil
import logging
from typing import Optional
import docker
import docker.models.containers
import platformconfig
import moses_exceptions
import tags
import progresscookie
import dockerapi
from applicationconfig_base import ApplicationConfigBase


def check_image(self: ApplicationConfigBase, configuration: str) -> bool:
    """Check if the image is up to date.

    :param configuration: debug/release
    :type configuration: str

    :returns: true if the image is up to date
    :rtype: bool

    """
    try:
        localdocker = docker.from_env()

        if self.images[configuration] is None or self.images[configuration] == "":
            logging.info("Image has never been built.")
            return False

        img = None

        try:
            img = localdocker.images.get(self.images[configuration])
        except docker.errors.ImageNotFound:
            pass

        if img is None:
            logging.info("Image does not exist.")
            return False

        if img.attrs["Created"] < self.modificationdate:
            logging.info("Image is older than configuration.")
            return False

        logging.info("Image is up to date.")
        return True
    except docker.errors.DockerException as exception:
        raise moses_exceptions.LocalDockerError(exception)


# pylint: disable=too-many-locals
def build_image(self: ApplicationConfigBase, configuration: str,
                progress: Optional[progresscookie.ProgressCookie]) -> None:
    """Generate Dockerfile and build the image.

    :param configuration: debug/release
    :type configuration: str
    :param progress: object used to report progress of the operation
    :type progress: progresscookie.ProgressCookie, optional

    """
    # this function will be part of ApplicationConfig via import
    # members of base class ApplicationConfigBase are accessed
    # pylint: disable=protected-access
    assert self.folder is not None

    try:
        localdocker = docker.from_env()

        platform = platformconfig.PlatformConfigs().get_platform(self.platformid)

        assert platform is not None
        assert platform.folder is not None

        dockertemplatefull = platform.folder / str(
            platform.get_prop(configuration, "container")
        )
        dockerfile = self._get_work_folder() / ("Dockerfile." + configuration)

        tags.apply_template(
            str(dockertemplatefull),
            str(dockerfile),
            self._get_value,
            configuration,
        )

        # copy contents of data subfolder to app path
        platformfilesfolder = platform.folder / "files"
        filesfolder = self.folder / "files"

        if platformfilesfolder.exists():
            if filesfolder.exists():
                shutil.rmtree(filesfolder)
            shutil.copytree(platformfilesfolder, filesfolder)

        # for some reasons also docker on windows wants / paths
        dockerfilerelpath = str(os.path.relpath(dockerfile, self.folder)).replace(
            "\\", "/"
        )

        if platform.architecture == "":
            img = dockerapi.build_image(
                localdocker,
                str(self.folder),
                dockerfilerelpath,
                self._get_image_name(configuration),
                None,
                progress,
            )
        else:
            img = dockerapi.build_image(
                localdocker,
                str(self.folder),
                dockerfilerelpath,
                self._get_image_name(configuration),
                platform.architecture,
                progress,
            )

        if img is None:
            raise moses_exceptions.ImageNotFoundError(
                self._get_image_name(configuration))

        tag = self.get_custom_prop(configuration, "tag")

        if tag is not None:
            parts = tag.split(":")
            parts_count = len(parts)
            if parts_count > 1:
                repository = ":".join(parts[0:parts_count - 1])
                tag = parts[parts_count - 1]
                img.tag(repository, tag)
            else:
                img.tag(tag)

        if self.images[configuration] is not None and self.images[configuration] != "":

            oldimg = None

            try:
                oldimg = localdocker.images.get(self.images[configuration])
            except docker.errors.ImageNotFound:
                pass

            if oldimg is not None:
                localdocker.images.remove(
                    image=oldimg.id, force=True, noprune=False)

        self.images[configuration] = str(img.id)
        self.save()

        localdocker.containers.prune()

    except docker.errors.DockerException as exception:
        raise moses_exceptions.LocalDockerError(exception)
