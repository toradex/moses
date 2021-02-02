"""Classes used to manage applications."""
import os
import logging
import datetime
from pathlib import Path
from typing import Optional, Dict
import docker
import docker.models.containers
import singleton
import platformconfig
import moses_exceptions
import targetdevice
import logs
from applicationconfig_base import ApplicationConfigBase

# those imports implement additional methods of the ApplicationConfig class
import applicationconfig_build
import applicationconfig_deployrun
import applicationconfig_sdk
import applicationconfig_dockerexport


class ApplicationConfig(ApplicationConfigBase):
    """Class used to manage an application."""

    get_container = applicationconfig_deployrun.get_container
    deploy_image = applicationconfig_deployrun.deploy_image
    run = applicationconfig_deployrun.run
    stop = applicationconfig_deployrun.stop
    sync_folders = applicationconfig_deployrun.sync_folders

    check_image = applicationconfig_build.check_image
    build_image = applicationconfig_build.build_image

    get_sdk_container = applicationconfig_sdk.get_sdk_container
    update_sdk = applicationconfig_sdk.update_sdk
    start_sdk_container = applicationconfig_sdk.start_sdk_container

    get_docker_commandline = applicationconfig_dockerexport.get_docker_commandline
    get_docker_composefile = applicationconfig_dockerexport.get_docker_composefile
    push_to_registry = applicationconfig_dockerexport.push_to_registry

    def touch(self) -> None:
        """Set modification date to current time."""
        self.modificationdate = datetime.datetime.utcnow().isoformat()

    def destroy(self) -> None:
        """Remove the application and all associated files, containers and images."""
        try:
            localdocker = docker.from_env()

            if self.images["debug"] is not None and self.images["debug"] != "":
                if localdocker.images.get(self.images["debug"]) is not None:
                    localdocker.images.remove(
                        image=self.images["debug"], force=True, prune=True)

            if self.images["release"] is not None and self.images["release"] != "":
                if localdocker.images.get(self.images["release"]) is not None:
                    localdocker.images.remove(
                        image=self.images["release"], force=True, prune=True
                    )

            if self.sdkimages["debug"] is not None and self.sdkimages["debug"] != "":
                if localdocker.images.get(self.sdkimages["debug"]) is not None:
                    localdocker.images.remove(
                        image=self.sdkimages["debug"], force=True, prune=True
                    )

            if (self.sdkimages["release"]
                    is not None and self.sdkimages["release"] != ""):
                if localdocker.images.get(
                        self.sdkimages["release"]) is not None:
                    localdocker.images.remove(
                        image=self.sdkimages["release"], force=True, prune=True
                    )
            super().destroy()
        # pylint: disable = broad-except
        except Exception:
            logging.exception("Exception destroying application object")

    def reseal(self) -> None:
        """Remove keys and ids from app configuration.

        Cleans up app-id and keys. Those will be re-created next time
        the application will be re-opened. This can be used to upload
        the app configuration to a git repo that can be cloned/forked
        and avoids that all the clones keep the same IDs.
        After this operation the application won't be usable anymore.

        """
        assert self.id is not None
        assert self.folder is not None

        applications = ApplicationConfigs()
        applications.pop(self.id)
        self.id = "00000000-0000-0000-0000-000000000000"
        self.privatekey = ""
        self.publickey = ""
        try:
            os.remove(self.folder / "id_rsa")
            os.remove(self.folder / "id_rsa.pub")
        # pylint: disable = broad-except
        except Exception:
            pass
        self.save()

    def get_container_logs(self, configuration: str,
                           device: targetdevice.TargetDevice, restart: bool) -> Optional[str]:
        """Return one line from the container logs.

        :param configuration: debug/release
        :type configuration: str
        :param device: target device where container is running
        :type device: targetdevice.TargetDevice
        :param restart: if True logs will be read from the beginning
        :type restart: bool
        :returns: log line on None for EOF
        :rtype: str | None

        """
        log = None

        container = self.get_container(
            configuration, device, only_running=False)

        if container is None:
            return None

        assert device.id is not None

        if not device.id in self.logs:
            self.logs[device.id] = {}

        if configuration in self.logs[device.id] and not restart:
            log = self.logs[device.id][configuration]
        else:
            log = container.logs(stream=True)
            self.logs[device.id][configuration] = log

        return logs.get_log_chunk(log)


class ApplicationConfigs(Dict[str, ApplicationConfig],
                         metaclass=singleton.Singleton):
    """Class used to manage the applications.

    It does not load all the objects at startup, apps are loaded on demand.

    """

    def load_application(self, folder: Path) -> ApplicationConfig:
        """Load an application from the filesystem.

        :param folder: path to the folder where application data is stored
        :type folder: pathlib.Path

        :returns: application object
        :rtype: ApplicationConfig

        """
        if not os.path.exists(folder):
            raise moses_exceptions.InvalidPathError(folder)

        app = ApplicationConfig(folder)

        # in this way we check that the platform is valid
        plat = platformconfig.PlatformConfigs().get_platform(app.platformid)

        if plat is None:
            return None

        assert app.id is not None

        # pylint false positive, self is a dict, so we can add items
        # pylint: disable=unsupported-assignment-operation
        self[app.id] = app
        return app

    def create_new_application(
            self, rootfolder: Path,
            platform: platformconfig.PlatformConfig,
            username: str) -> ApplicationConfig:
        """Create a new application.

        :param rootfolder: base folder when application folder will be created
        :type rootfolder: pathlib.Path
        :param platform: platform that will be associated to this application
        :type platform: PlatformConfig
        :param username: username used inside the application containre
        :type username: str

        :returns: application object
        :rtype: ApplicationConfig

        """
        # finds a new folder for the app config
        counter = 0

        if not os.path.exists(rootfolder):
            raise moses_exceptions.InvalidPathError(rootfolder)

        while (rootfolder / ("appconfig_" + str(counter))).exists():
            counter += 1

        app = ApplicationConfig(rootfolder / ("appconfig_" + str(counter)))

        assert platform.id is not None

        app.platformid = platform.id
        app.username = username
        app.save()

        assert app.id is not None

        # pylint false positive, self is a dict, so we can add items
        # pylint: disable=unsupported-assignment-operation
        self[app.id] = app
        return app
