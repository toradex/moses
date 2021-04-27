"""SDK-related features of ApplicationConfig class.

The class is too complex to stay in a single file, code has been
splitted in feature-specific modules.
This is why sometimes you see calls with self explicitely passed
as first parameter.
"""
import os
import shutil
import socket
import time
import logging
import platform as platform_module
from typing import Optional
import docker
import docker.models.containers
import paramiko
import platformconfig
import moses_exceptions
import tags
import progresscookie
import dockerapi
from applicationconfig_base import ApplicationConfigBase


def _get_sdk_container_name(self: ApplicationConfigBase,
                            configuration: str) -> str:
    """Return the name of the SDK container for this application.

    :param configuration: debug/release
    :type configuration: str

    :returns: container instance name
    :rtype: str

    """
    # this function will be part of ApplicationConfig via import,
    # members of base class ApplicationConfigBase are accessed
    # pylint: disable=protected-access
    assert self.id is not None

    platform = platformconfig.PlatformConfigs().get_platform(self.platformid)

    assert platform.id is not None

    if not platform.usesdk:
        raise moses_exceptions.PlatformDoesNotRequireSDKError(self.platformid)

    appname = self.get_custom_prop(configuration, "appname")

    if appname is None:
        instance = ""
    else:
        instance = appname.lower() + "_"

    instance += platform.id
    instance += "_"
    instance += configuration
    instance += "_"
    instance += self.id
    instance += "_sdk"

    instance = instance.replace(":", "_")
    instance = instance.replace("/", "_")
    return instance

# pylint: disable=too-many-locals
def _build_sdk_image(self: ApplicationConfigBase,
                     configuration: str,
                     progress: Optional[progresscookie.ProgressCookie]) -> None:
    """Generate Dockerfile and build SDK image.

    If the SDK container is running it wil be stopped and restarted

    :param configuration: debug/release
    :type configuration: str
    :param progress: object used to report progress of the operation
    :type progress: progresscookie.ProgressCookie, optional

    """
    # this function will be part of ApplicationConfig via import,
    # members of base class ApplicationConfigBase are accessed
    # pylint: disable=protected-access

    assert self.folder is not None

    containerwasrunning = False

    platform = platformconfig.PlatformConfigs().get_platform(self.platformid)

    assert platform.folder is not None

    instance = _get_sdk_container_name(self, configuration)

    localdocker = docker.from_env()

    try:

        # if an instance is running, stop and remove it
        # pylint: disable = broad-except
        try:
            sdkcontainer = localdocker.containers.get(instance)

            containerwasrunning = True
            if sdkcontainer.status == "running":
                sdkcontainer.stop()
            else:
                self.sdksshaddress = None

            sdkcontainer.remove()
        except docker.errors.NotFound:
            pass
        except Exception:
            # on some Windows PCs an internal server errror is generated instead.
            # see TIE-260
            if platform_module.system() == "Windows":
                pass
            else:
                raise

        sdkcontainername = platform.get_prop(configuration, "sdkcontainer")

        assert sdkcontainername is not None

        dockertemplatefull = platform.folder / sdkcontainername

        dockerfile = self._get_work_folder() / ("Dockerfile_SDK." + configuration)

        tags.apply_template(
            str(dockertemplatefull),
            str(dockerfile),
            self._get_value,
            configuration,
        )

        # copy contents of data subfolder to app path
        platformfilesfolder = platform.folder / "sdkfiles"
        filesfolder = self.folder / "sdkfiles"

        if platformfilesfolder.exists():
            if filesfolder.exists():
                shutil.rmtree(filesfolder)
            shutil.copytree(platformfilesfolder, filesfolder)

        # for some reasons also docker on windows wants / paths
        dockerfilerelpath = str(os.path.relpath(dockerfile, self.folder)).replace(
            "\\", "/"
        )

        sdkimage = dockerapi.build_image(
            localdocker,
            str(self.folder),
            dockerfilerelpath,
            self.get_sdk_image_name(configuration),
            None,
            progress,
        )

        if sdkimage is None:
            raise moses_exceptions.ImageNotFoundError(
                self.get_sdk_image_name(configuration)
            )

        localdocker.containers.prune()

        self.sdkimages[configuration] = str(sdkimage.id)
        self.save()

        if containerwasrunning:
            start_sdk_container(self, configuration, False, progress)

    except docker.errors.DockerException as exception:
        raise moses_exceptions.LocalDockerError(exception)


def get_sdk_container(self: ApplicationConfigBase,
                      configuration: str) -> docker.models.containers.Container:
    """Return SDK container object.

    :param configuration: debug/release
    :type configuration: str

    :returns: container instance
    :rtype: docker.models.containers.Container

    """
    instance = _get_sdk_container_name(self, configuration)

    # pylint: disable=broad-except
    try:
        localdocker = docker.from_env()
        cnt = localdocker.containers.get(instance)

        return cnt
    except docker.errors.DockerException as exception:
        raise moses_exceptions.SDKContainerNotFoundError(exception)
    except Exception as exception:
        # on some Windows PCs an internal server errror is generated instead.
        # see TIE-260
        if platform_module.system() == "Windows":
            raise moses_exceptions.SDKContainerNotFoundError(exception)
        raise


def update_sdk(self: ApplicationConfigBase,
               configuration: str,
               progress: Optional[progresscookie.ProgressCookie]) -> None:
    """Update the application SDK.

    :param configuration: debug/release
    :type configuration: str
    :param progress: object used to report progress of the operation
    :type progress: progresscookie.ProgressCookie, optional

    """
    platform = platformconfig.PlatformConfigs().get_platform(self.platformid)

    if not platform.usesdk:
        raise moses_exceptions.PlatformDoesNotRequireSDKError(self.platformid)

    if configuration is None:
        raise moses_exceptions.SDKRequiresConfiguration()
    _build_sdk_image(self, configuration, progress)


# pylint: disable = too-many-branches
# pylint: disable = too-many-statements
def start_sdk_container(self: ApplicationConfigBase,
                        configuration: str,
                        build: bool,
                        progress: Optional[progresscookie.ProgressCookie]) -> None:
    """Run an instance of the application's SDK container.

    :param configuration: debug/release
    :type configuration: str
    :param build: if True, then SDK image is built if not existing
    :type build: bool
    :param progress: object used to report progress of the operation
    :type progress: progresscookie.ProgressCookie, optional

    """
    ports = {"22/tcp": int(self.sdksshaddress["HostPort"])
             if self.sdksshaddress is not None else None}

    self.sdksshaddress = None

    instance = _get_sdk_container_name(self, configuration)
    platform = platformconfig.PlatformConfigs().get_platform(self.platformid)

    if not platform.usesdk:
        raise moses_exceptions.PlatformDoesNotRequireSDKError(self.platformid)

    localdocker = docker.from_env()

    # pylint: disable = broad-except
    try:
        container = localdocker.containers.get(instance)

        if container.status != "running":
            try:
                container.stop()
                container.remove()
            except Exception:
                pass
            container = None
    except docker.errors.NotFound:
        container = None
    except Exception:
        # on some Windows PCs an internal server errror is generated instead.
        # see TIE-260
        if platform_module.system() == "Windows":
            container = None
        else:
            raise

    if container is not None:
        if platform.usessh:
            self.sdksshaddress = container.attrs["NetworkSettings"]["Ports"]["22/tcp"][0]
        else:
            self.sdksshaddress = None
    else:
        if platform.usesdk and not platform.usesysroots:
            try:
                _ = localdocker.images.get(
                    self.get_sdk_image_name(configuration))
            except docker.errors.NotFound as exception:
                if build:
                    logging.info("SDK - SDK image not found, building it.")
                    _build_sdk_image(self, configuration, progress)
                else:
                    raise moses_exceptions.ImageNotFoundError(
                        self.get_sdk_image_name(configuration)
                    ) from exception

        try:
            container = localdocker.containers.run(
                self.get_sdk_image_name(configuration),
                name=instance,
                detach=True,
                ports=ports,
            )
        except docker.errors.DockerException:
            self.sdksshaddress = None
            self.save()
            raise

        while container.status == "created":
            container = localdocker.containers.get(instance)

        if not platform.usessh:
            self.sdksshaddress = None
        else:
            starttime = time.time()

            while time.time() < starttime + 60:
                try:
                    # check that ssh server is active
                    self.sdksshaddress = container.attrs["NetworkSettings"]["Ports"]["22/tcp"][
                        0
                    ]
                    self.save()

                    if self.sdksshaddress is None:
                        raise moses_exceptions.InternalServerError(None)

                    port = int(self.sdksshaddress["HostPort"])
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    result = sock.connect_ex(("127.0.0.1", port))
                    sock.close()

                    if result != 0:
                        continue

                    ssh = paramiko.SSHClient()

                    ssh.connect(
                        "127.0.0.1",
                        port=port,
                        username=platform.sdkcontainerusername,
                        password=platform.sdkcontainerpassword,
                    )

                    return
                # pylint: disable = broad-except
                except Exception:
                    pass

                raise moses_exceptions.TimeoutError()
