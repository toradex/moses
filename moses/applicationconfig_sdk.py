"""SDK-related features of ApplicationConfig class.

The class is too complex to stay in a single file, code has been 
splitted in feature-specific modules.
This is why sometimes you see calls with self explicitely passed
as first parameter.
"""
import os
import shutil
import platform as platform_module
import logging
import docker
import docker.models.containers
import paramiko
import platformconfig
import exceptions
import socket
import tags
import time
import socket
import progresscookie
import dockerapi
from applicationconfig_base import ApplicationConfigBase
from typing import Optional


def _get_sdk_container_name(self: ApplicationConfigBase, configuration: str) -> str:
    """Return the name of the SDK container for this application.

    :param configuration: debug/release
    :type configuration: str

    :returns: container instance name
    :rtype: str

    """
    assert self.id is not None

    platform = platformconfig.PlatformConfigs().get_platform(self.platformid)

    assert platform.id is not None

    if not platform.usesdk:
        raise exceptions.PlatformDoesNotRequireSDKError(self.platformid)

    appname = self._get_custom_prop(configuration, "appname")

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


def _get_sdk_image_name(self: ApplicationConfigBase, configuration: str) -> str:
    """Return the name of the SDK container image for the application.

    :param configuration: debug/release
    :type configuration: str

    :returns: sdk image name
    :rtype: str

    """
    assert self.id is not None

    platform = platformconfig.PlatformConfigs().get_platform(self.platformid)

    assert platform.id is not None

    if not platform.usesdk:
        raise exceptions.PlatformDoesNotRequireSDKError(self.platformid)

    appname = self._get_custom_prop(configuration, "appname")

    if appname is None:
        imagename = ""
    else:
        imagename = appname.lower() + "_"

    imagename += platform.id
    imagename += "_"
    imagename += configuration
    imagename += "_"
    imagename += self.id
    imagename += "_sdk_image"

    imagename = imagename.replace(":", "_")
    imagename = imagename.replace("/", "_")

    return imagename


def _build_sdk_image(
    self: ApplicationConfigBase,
    configuration: str,
    progress: Optional[progresscookie.ProgressCookie],
) -> None:
    """Generate Dockerfile and build SDK image.

    If the SDK container is running it wil be stopped and restarted

    :param configuration: debug/release
    :type configuration: str
    :param progress: object used to report progress of the operation
    :type progress: progresscookie.ProgressCookie, optional

    """
    assert self.folder is not None

    containerwasrunning = False

    platform = platformconfig.PlatformConfigs().get_platform(self.platformid)

    assert platform.folder is not None

    instance = _get_sdk_container_name(self, configuration)

    localdocker = docker.from_env()

    try:

        # if an instance is running, stop and remove it
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
        except:
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
            lambda obj, tag, args: self._get_value(obj, tag, args),
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
            _get_sdk_image_name(self, configuration),
            None,
            progress,
        )

        if sdkimage is None:
            raise exceptions.ImageNotFoundError(
                _get_sdk_image_name(self, configuration)
            )

        localdocker.containers.prune()

        self.sdkimages[configuration] = str(sdkimage.id)
        self.save()

        if containerwasrunning:
            start_sdk_container(self, configuration, False, progress)

    except docker.errors.DockerException as e:
        raise exceptions.LocalDockerError(e)


def get_sdk_container(
    self: ApplicationConfigBase, configuration: str
) -> docker.models.containers.Container:
    """Return SDK container object.

    :param configuration: debug/release
    :type configuration: str

    :returns: container instance
    :rtype: docker.models.containers.Container

    """
    instance = _get_sdk_container_name(self, configuration)

    try:
        localdocker = docker.from_env()
        cnt = localdocker.containers.get(instance)

        return cnt
    except docker.errors.DockerException as e:
        raise exceptions.SDKContainerNotFoundError(e)
    except Exception as e:
        # on some Windows PCs an internal server errror is generated instead.
        # see TIE-260
        if platform_module.system() == "Windows":
            raise exceptions.SDKContainerNotFoundError(e)
        else:
            raise


def update_sdk(
    self: ApplicationConfigBase,
    configuration: str,
    progress: Optional[progresscookie.ProgressCookie],
) -> None:
    """Update the application SDK.

    :param configuration: debug/release
    :type configuration: str
    :param progress: object used to report progress of the operation
    :type progress: progresscookie.ProgressCookie, optional

    """
    platform = platformconfig.PlatformConfigs().get_platform(self.platformid)

    if not platform.usesdk:
        raise exceptions.PlatformDoesNotRequireSDKError(self.platformid)

    if configuration is None:
        raise exceptions.SDKRequiresConfiguration()
    _build_sdk_image(self, configuration, progress)


def start_sdk_container(
    self: ApplicationConfigBase,
    configuration: str,
    build: bool,
    progress: Optional[progresscookie.ProgressCookie],
) -> None:
    """Run an instance of the application's SDK container.

    :param configuration: debug/release
    :type configuration: str
    :param build: if True, then SDK image is built if not existing
    :type build: bool
    :param progress: object used to report progress of the operation
    :type progress: progresscookie.ProgressCookie, optional

    """
    if self.sdksshaddress is not None:
        ports = {"22/tcp": int(self.sdksshaddress["HostPort"])}
    else:
        # None is a valid value when you want host-assigned port
        ports = {"22/tcp": None}  # type: ignore

    self.sdksshaddress = None

    instance = _get_sdk_container_name(self, configuration)
    platform = platformconfig.PlatformConfigs().get_platform(self.platformid)

    localdocker = docker.from_env()

    try:
        container = localdocker.containers.get(instance)

        if container.status != "running":
            try:
                container.stop()
                container.remove()
            except:
                pass
            container = None
    except docker.errors.NotFound:
        container = None
    except:
        # on some Windows PCs an internal server errror is generated instead.
        # see TIE-260
        if platform_module.system() == "Windows":
            container = None
        else:
            raise

    if container is None:
        if platform.usesdk and not platform.usesysroots:
            try:
                _ = localdocker.images.get(_get_sdk_image_name(self, configuration))
            except docker.errors.NotFound:
                if build:
                    logging.info("SDK - SDK image not found, building it.")
                    _build_sdk_image(self, configuration, progress)
                else:
                    raise exceptions.ImageNotFoundError(
                        _get_sdk_image_name(self, configuration)
                    )

        try:
            container = localdocker.containers.run(
                _get_sdk_image_name(self, configuration),
                name=instance,
                detach=True,
                ports=ports,
            )
        except Exception as e:
            self.sdksshaddress = None
            self.save()
            raise e

        while container.status == "created":
            container = localdocker.containers.get(instance)

        starttime = time.time()

        try:
            # check that ssh server is active
            self.sdksshaddress = container.attrs["NetworkSettings"]["Ports"]["22/tcp"][
                0
            ]
            self.save()

            port = int(self.sdksshaddress["HostPort"])
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex(("127.0.0.1", port))
            sock.close()

            if result != 0:
                return

            ssh = paramiko.SSHClient()

            ssh.connect(
                "127.0.0.1",
                port=port,
                username=platform.sdkcontainerusername,
                password=platform.sdkcontainerpassword,
            )

            return

        except:
            if time.time() > starttime + 60:
                raise exceptions.TimeoutError()
    else:
        self.sdksshaddress = container.attrs["NetworkSettings"]["Ports"]["22/tcp"][0]
