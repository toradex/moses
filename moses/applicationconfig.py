import os
import io
import shutil
import platform as platform_module
import logging
import uuid
from pathlib import Path
import tarfile
import docker
import paramiko
import singleton
import config
import platformconfig
import remotedocker
import exceptions
import datetime
import targetdevice
import socket
import utils
import sharedssh
import stat
import time
import socket
import rsync
import pathlib
import progresscookie
import dockerapi
from typing import Optional, Dict, Any, List


class RemoteImageNotFoundException(Exception):
    pass


class ContainerAlreadyRunning(Exception):
    pass


class ApplicationConfig(config.ConfigurableKeysObject):
    """Class used to manage an application
    """

    readonlyfields = config.ConfigurableKeysObject.readonlyfields.union(
        {"images", "sdkimages"}
    )

    non_nullable_properties = ["dockercomposefile", "startupscript", "shutdownscript"]
    configurations = ["common", "debug", "release"]

    def __init__(self, folder: Optional[pathlib.Path] = None):
        """Loads data from a configuration folder

        Arguments:
            folder {Path} -- Path of the folder used to store
                             target information
        """
        super().__init__(folder)

        self.props: Dict[str, Dict[str, str]] = {
            "common": {
                "expose": "",
                "arg": "",
                "env": "",
                "preinstallcommands": "",
                "extrapackages": "",
                "devpackages": "",
                "buildfiles": "",
                "buildcommands": "",
                "targetfiles": "",
                "targetcommands": "",
                "command": "",
                "sdkpreinstallcommands": "",
                "sdkpostinstallcommands": "",
            },
            "debug": {"arg": "ARG SSHUSERNAME=" "#%application.username%#\n"},
            "release": {},
        }

        self.ports: Dict[str, Dict[str, str]] = {
            "common": {},
            "debug": {},
            "release": {},
        }
        self.volumes: Dict[str, Dict[str, str]] = {
            "common": {},
            "debug": {},
            "release": {},
        }
        self.devices: Dict[str, List[str]] = {"common": [], "debug": [], "release": []}

        self.images: Dict[str, str] = {"debug": "", "release": ""}

        self.sdkimages: Dict[str, str] = {"debug": "", "release": ""}

        self.platformid = ""
        self.publickey: Optional[str] = None
        self.privatekey: Optional[str] = None
        self.modificationdate = datetime.datetime.utcnow().isoformat()

        self.extraparms: Dict[str, Dict[str, str]] = {
            "common": {},
            "debug": {},
            "release": {},
        }

        self.dockercomposefile: Dict[str, str] = {
            "common": "",
            "debug": "",
            "release": "",
        }

        self.startupscript: Dict[str, str] = {"common": "", "debug": "", "release": ""}

        self.shutdownscript: Dict[str, str] = {"common": "", "debug": "", "release": ""}

        self.networks: Dict[str, List[str]] = {"common": [], "debug": [], "release": []}

        self.sdksshaddress: Optional[Dict[str, Any]] = None

        if self.folder is not None and self.folder.exists():
            self.load()
        else:
            self.id = str(uuid.uuid4())

        self.logs: Dict[str, Any] = {}

    def save(self) -> None:

        if self.folder is None:
            return

        # we got a folder, but it may not be an existing one
        if not self.folder.exists():
            self.folder.mkdir()

        super().save()

    def load(self) -> None:
        super().load()

        if self.id == "00000000-0000-0000-0000-000000000000":
            self.id = str(uuid.uuid4())
            self.privatekey = None
            self.publickey = None
            self.save()

    def _generate_keys(self):
        super()._generate_keys()
        with open(str(self.folder / "id_rsa.pub"), "w") as f:
            f.write(self.publickey)

    def _build_folder_path(self) -> Path:
        raise Exception("Application must have a defined base folder path.")

    def is_valid(self, fields=None) -> bool:
        """Validate fields of current object

        Arguments:
            fields {dictionary} -- dictionary with values, if None then
                                   self.__dict__ will be used

        Returns:
            bool -- true if all fields contain valid values
        """

        if fields is None:
            fields = self.__dict__

        if fields["platformid"] not in platformconfig.PlatformConfigs():
            logging.error(
                "Invalid platform id %s in application %s",
                fields["platformid"],
                self.folder,
            )
            return False

        # some properties can't be returned/set as null in the REST API
        for prop in ApplicationConfig.non_nullable_properties:
            for conf in ApplicationConfig.configurations:
                if fields[prop][conf] is None:
                    fields[prop][conf] = ""

        return True

    def __getstate__(self):
        # for applications we keep id in the serialized format
        fields = super().__getstate__()
        fields["id"] = self.id
        fields["sdksshaddress"] = self.sdksshaddress
        del fields["logs"]
        return fields

    def _to_json(self):
        # we return also folder in json
        fields = super()._to_json()
        fields["folder"] = str(self.folder)
        return fields

    def get_custom_prop(self, configuration: str, property: str):
        if property in self.props[configuration]:
            return str(self.props[configuration][property])
        if property in self.props["common"]:
            return str(self.props["common"][property])
        return None

    def _get_value(self, obj: str, tag: str, configuration: str) -> str:
        """Returns value for a tag in the format application/platform.tag

        Arguments:
            obj {str} -- application/platform
            tag {str} -- tag
            configuration {str} -- active configuration

        Returns:
            str -- value of the tag or empty string
        """

        platform = platformconfig.PlatformConfigs().get_platform(self.platformid)

        if obj == "application":
            value = self.get_custom_prop(configuration, tag)

            if value is None:
                value = self.get_prop(configuration, tag)

            if value is None:
                if tag in self.__dict__:
                    value = str(self.__dict__[tag])
                else:
                    value = ""

            return value
        elif obj == "platform":
            return platform._get_value(obj, tag, configuration)
        return ""

    def _get_work_folder(self) -> Path:
        """ Return app work folder

            Create it if needed

        Returns:
            Path -- work folder, it's granted to exists
        """

        if self.folder is None:
            raise Exception("Folder is not configured.")

        workfolder: Path = self.folder / "work"

        if not os.path.exists(workfolder):
            workfolder.mkdir()

        return workfolder

    def check_image(self, configuration: str):
        """ Checks if the image is up to date

        Arguments:
            configuration {str} - debug/release
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
        except docker.errors.DockerException as e:
            raise exceptions.LocalDockerError(e)

    def _get_image_name(self, configuration: str):
        """ Return image name

        Arguments:
            configuration {str} - debug/release
        """
        assert self.id is not None

        appname = self.get_custom_prop(configuration, "appname")

        if appname is None:
            imagename = ""
        else:
            imagename = appname.lower() + "_"

        imagename += self.platformid + "_" + configuration + "_" + self.id
        return imagename

    def build_image(
        self, configuration: str, progress: Optional[progresscookie.ProgressCookie]
    ):
        """Generate complete dockerfile from template and
        builds the image

        Arguments:
            configuration {str} - debug/release
            progress (Optional[ProgressCookie]): progress object or None
        """

        assert self.folder is not None

        try:
            localdocker = docker.from_env()

            # we must remove the old image first
            if (
                self.images[configuration] is not None
                and self.images[configuration] != ""
            ):

                oldimg = None

                try:
                    oldimg = localdocker.images.get(self.images[configuration])
                except docker.errors.ImageNotFound:
                    pass

                if oldimg is not None:
                    localdocker.images.remove(
                        image=oldimg.id, force=True, noprune=False
                    )

            platform = platformconfig.PlatformConfigs().get_platform(self.platformid)

            assert platform is not None
            assert platform.folder is not None

            dockertemplatefull = platform.folder / str(
                platform.get_prop(configuration, "container")
            )
            dockerfile = self._get_work_folder() / ("Dockerfile." + configuration)

            utils.apply_template(
                str(dockertemplatefull),
                str(dockerfile),
                lambda obj, tag, args: self._get_value(obj, tag, args),
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
                raise exceptions.ImageNotFoundError(self._get_image_name(configuration))

            tag = self.get_custom_prop(configuration, "tag")

            if tag is not None:
                parts = tag.split(":")
                if len(parts) > 1:
                    repository, tag = parts
                    img.tag(repository, tag)
                else:
                    img.tag(tag)

            self.images[configuration] = str(img.id)
            self.save()

            localdocker.containers.prune()

        except docker.errors.DockerException as e:
            raise exceptions.LocalDockerError(e)

    def deploy_image(
        self,
        configuration: str,
        device: targetdevice.TargetDevice,
        progress: Optional[progresscookie.ProgressCookie],
    ):
        """
        Checks if container needs to be deployed to remote and then
        transfers the actual file and loads it in the images collection

        Arguments:
            configuration {str} -- debug/release container type
            device {TargetDevice} -- device where container has to be deployed
            progress (Optional[ProgressCookie]): progress object or None
        """

        try:
            imgid = self.images[configuration]

            if imgid is None or imgid == "":
                logging.error(
                    "Image has never been build for application %s.", self.folder
                )
                raise exceptions.ImageNotFoundError("")

            ld = docker.from_env()

            try:
                limg = ld.images.get(imgid)
            except docker.errors.ImageNotFound:
                logging.error(
                    "Image %s not found when deploying application %s.",
                    imgid,
                    self.folder,
                )
                raise exceptions.ImageNotFoundError(imgid)

            if len(limg.tags) == 0:
                self.images[configuration] = ""
                self.save()
                logging.error(
                    "Image %s has no tags when deploying application %s.",
                    imgid,
                    self.folder,
                )
                raise exceptions.ImageNotFoundError(imgid)

            plat = platformconfig.PlatformConfigs().get_platform(self.platformid)

            if not plat.check_device_compatibility(device):
                logging.error(
                    "Incompatible platform %s selected for device %s when deploying app %s",
                    plat.name,
                    device.id,
                    self.folder,
                )
                raise exceptions.IncompatibleDeviceError(device.id)

            with remotedocker.RemoteDocker(device) as rd:

                rimg = rd.get_image_by_tag(limg.tags[0])

                if rimg is not None:
                    # image is up to date
                    if limg.attrs["Created"] == rimg["Created"]:

                        if progress is not None:
                            progress.append_message(
                                "Image on target is already up to date."
                            )
                        return

                    logging.info("DEPLOY - Image on target is not up to date.")

                    if progress is not None:
                        progress.append_message(
                            "Image on target is not up to date, removing it."
                        )

                    # we need to stop active containers
                    containers = rd.get_containers(
                        {"name": self.get_container_name(rimg)}
                    )

                    if len(containers) > 0:
                        # it is safe to assume it's only one,
                        # since names must be unique
                        logging.warning("DEPLOY - terminating running instance.")
                        containers[0].remove(force=True)

                    rd.delete_image(rimg["Id"], True)

                    if progress is not None:
                        progress.append_message("Image has been removed.")

                else:
                    logging.info("DEPLOY - Image not found on target device.")

                    if progress is not None:
                        progress.append_message("Image not found on target device.")

                if progress is not None:
                    progress.append_message("Exporting local image.")
                    progress.set_minmax(0, limg.attrs["Size"] * 2)

                stream = limg.save()
                outputpath = str(self._get_work_folder() / (configuration + ".tar"))

                with open(outputpath, "wb") as f:
                    for chunk in stream:
                        f.write(chunk)
                        if progress is not None:
                            progress.update_progress_minmax(len(chunk))

                    f.flush()
                    f.close()

                logging.info("DEPLOY - Image exported.")

                if progress is not None:
                    progress.append_message("Image exported, deploying to the target.")

                rd.load_image(limg, outputpath, progress)

                if progress is not None:
                    progress.append_message("Image deployed.")

                logging.info("DEPLOY - Image deployed.")

        except docker.errors.DockerException as e:
            raise exceptions.LocalDockerError(e)

    def _merge_props(
        self, plat: platformconfig.PlatformConfig, configuration: str, prop: str
    ) -> dict:
        """merges values from multiple dictionaries
        The platform common one is taken first, then configuration
        is applied, then app common, then app configuration

        Arguments:
            plat {platformconfig.PlatformConfig} -- [description]
            configuration {str} - debug/release
            prop {str} -- property

        Returns:
            dict -- merged values
        """
        merged = plat.__dict__[prop]["common"].copy()
        merged.update(plat.__dict__[prop][configuration])
        merged.update(self.__dict__[prop]["common"])
        merged.update(self.__dict__[prop][configuration])

        for key, value in merged.items():
            if isinstance(value, str):
                newvalue = utils.replace_tags(
                    value,
                    lambda obj, tag, args: self._get_value(obj, tag, args),
                    configuration,
                )
                if newvalue != value:
                    merged[key] = value

        return merged

    def _append_props(
        self, plat: platformconfig.PlatformConfig, configuration: str, prop: str
    ) -> list:
        """append values from multiple lists
        The platform common one is taken first, then configuration
        is appended, then app common, then app configuration

        Arguments:
            plat {platformconfig.PlatformConfig} -- [description]
            configuration {str} - debug/release
            prop {str} -- property

        Returns:
            list -- merged values
        """

        merged = plat.__dict__[prop]["common"].copy()
        merged.extend(plat.__dict__[prop][configuration])
        merged.extend(self.__dict__[prop]["common"])
        merged.extend(self.__dict__[prop][configuration])

        return list(
            map(
                lambda i: i
                if not isinstance(i, str)
                else utils.replace_tags(
                    i,
                    lambda obj, tag, args: self._get_value(obj, tag, args),
                    configuration,
                ),
                merged,
            )
        )

    def get_prop(self, configuration: str, prop: str):
        """Return a property by checking different layers
        application/configuration
        application/common

        Arguments:
            plat {platformconfig.PlatformConfig} -- [description]
            configuration {str} -- debug/release
            prop {str} -- property name
        """
        if not prop in self.__dict__:
            return None

        if not isinstance(self.__dict__[prop], dict):
            return str(self.__dict__[prop])

        if (self.__dict__[prop][configuration] is not None) and not (
            prop in ApplicationConfig.non_nullable_properties
            and len(self.__dict__[prop][configuration]) == 0
        ):
            return str(self.__dict__[prop][configuration])

        if (self.__dict__[prop]["common"] is not None) and not (
            prop in ApplicationConfig.non_nullable_properties
            and len(self.__dict__[prop]["common"]) == 0
        ):
            return str(self.__dict__[prop]["common"])

        return None

    def _runscript(
        self,
        configuration: str,
        plat: platformconfig.PlatformConfig,
        device: targetdevice.TargetDevice,
        scriptname: str,
        progress: Optional[progresscookie.ProgressCookie],
    ):
        """Runs a script configured as "scriptname" property in platform and/or application

        Arguments:
            configuration {str} -- debug/release
            plat {platformconfig.PlatformConfig} -- platform
            device {targetdevice.TargetDevice} -- device
            scriptname {str} -- name of the property storing the script filename
        """

        assert plat.folder is not None

        # check scripts for both application and platform, both are deployed
        # if app script exist, then it's the only one invoked (but still has a
        # chance to invoke platform one if needed since it has been deployed in
        # the same place)
        script = self.get_prop(configuration, scriptname)
        platformscript = plat.get_prop(configuration, scriptname)

        if script == "":
            script = None

        if platformscript == "":
            platformscript = None

        if script is not None or platformscript is not None:

            logging.info("Running script:" + scriptname)

            ssh = sharedssh.SharedSSHClient.get_connection(device)

            with paramiko.SFTPClient.from_transport(ssh.get_transport()) as sftp:

                sftp.chdir(device.homefolder)

                try:
                    sftp.stat(self.id)
                except:
                    sftp.mkdir(self.id)

                sftp.chdir(self.id)

                if script is not None:
                    fullscriptpath = self.folder / script
                    targetscriptpath = self._get_work_folder() / (
                        script + "." + configuration
                    )
                    utils.apply_template(
                        fullscriptpath,
                        targetscriptpath,
                        lambda obj, tag, args: self._get_value(obj, tag, args),
                        configuration,
                    )
                    sftp.put(targetscriptpath, script, confirm=True)
                    sftp.chmod(script, stat.S_IXUSR | stat.S_IRUSR | stat.S_IWUSR)

                if platformscript is not None:
                    fullplatformscript = plat.folder / platformscript
                    targetplatformscript = self._get_work_folder() / (
                        platformscript + "." + configuration
                    )
                    utils.apply_template(
                        str(fullplatformscript),
                        str(targetplatformscript),
                        lambda obj, tag, args: self._get_value(obj, tag, args),
                        configuration,
                    )
                    sftp.put(targetplatformscript, platformscript, confirm=True)
                    sftp.chmod(
                        platformscript, stat.S_IXUSR | stat.S_IRUSR | stat.S_IWUSR
                    )

            scriptpath = device.homefolder + "/" + str(self.id)

            if script is not None:
                scriptfile = script
            else:
                scriptfile = platformscript

            if progress is not None:
                progress.append_message(f"running script {scriptfile}")

            with ssh.get_transport().open_session() as session:

                session.exec_command("cd " + scriptpath + "&&" + "./" + scriptfile)

                while not session.exit_status_ready():
                    while session.recv_ready():
                        msg = session.recv(1024).decode("UTF-8")
                        logging.info(msg)
                        if progress is not None:
                            progress.append_message(msg)
                    while session.recv_stderr_ready():
                        msg = session.recv_stderr(1024).decode("UTF-8")
                        logging.warning(msg)
                        if progress is not None:
                            progress.append_message(msg)

                if session.recv_exit_status() != 0:
                    logging.error("Error executing " + scriptname + ".")

            logging.info("Running script:" + scriptname + " done.")

    def run(
        self,
        configuration: str,
        device: targetdevice.TargetDevice,
        progress: Optional[progresscookie.ProgressCookie],
    ):
        """Runs application selected container on the specified device.

        Arguments:
            configuration {str} -- debug/release
            device {TargetDevice} -- device

        Raises:
            ImageNotFoundError -- Image was not on the target
            IncompatibleDeviceError -- Device can't run selected image
            ConnectionError -- Can't connect to device
        """

        assert self.id is not None

        plat = platformconfig.PlatformConfigs().get_platform(self.platformid)

        imgid = self.images[configuration]

        if imgid is None or imgid == "":
            raise exceptions.ImageNotFoundError("")

        ld = docker.from_env()

        try:
            limg = ld.images.get(imgid)
        except docker.errors.ImageNotFound:
            logging.error("Image %s not found", imgid)
            raise exceptions.ImageNotFoundError(imgid)
        except docker.errors.DockerException as e:
            raise exceptions.LocalDockerError(e)

        with remotedocker.RemoteDocker(device) as rd:

            container = self.get_container(configuration, device)

            if container is not None:

                if progress is not None:
                    progress.append_message("Stopping current instance...")

                self.stop(configuration, device)

                assert device.id is not None

                if device.id in self.logs:
                    if configuration in self.logs[device.id]:
                        del self.logs[device.id][configuration]

            # check scripts for both application and platform, both are deployed
            # if app script exist, then it's the only one invoked (but still has a
            # chance to invoke platform one if needed since it has been deployed in
            # the same place)
            if progress is not None:
                progress.append_message("running startup script...")

            self._runscript(configuration, plat, device, "startupscript", progress)

            # for docker-compose only one file is deployed used, and application one takes precedence
            # over the platform one
            dockercomposefile = self.get_prop(configuration, "dockercomposefile")
            dockercomposefilepath = None

            if dockercomposefile is not None and len(dockercomposefile) > 0:
                dockercomposefilepath = self.folder / dockercomposefile
            else:
                dockercomposefile = plat.get_prop(configuration, "dockercomposefile")
                if dockercomposefile is not None and len(dockercomposefile) > 0:
                    dockercomposefilepath = plat.folder / dockercomposefile

            if dockercomposefilepath is not None:

                if progress is not None:
                    progress.append_message("running docker-compose...")

                ssh = sharedssh.SharedSSHClient.get_connection(device)

                with paramiko.SFTPClient.from_transport(ssh.get_transport()) as sftp:

                    sftp.chdir(device.homefolder)

                    try:
                        sftp.stat(self.id)
                    except:
                        sftp.mkdir(self.id)

                    sftp.chdir(self.id)

                    targetdockercomposepath = self._get_work_folder() / (
                        dockercomposefile + "." + configuration
                    )
                    utils.apply_template(
                        dockercomposefilepath,
                        targetdockercomposepath,
                        lambda obj, tag, args: self._get_value(obj, tag, args),
                        configuration,
                    )
                    sftp.put(targetdockercomposepath, "docker-compose.yml")

                    with ssh.get_transport().open_session() as session:
                        session.exec_command(
                            "cd "
                            + device.homefolder
                            + "/"
                            + self.id
                            + " && docker-compose up -d"
                        )

                        while not session.exit_status_ready():
                            while session.recv_ready():
                                msg = session.recv(1024).decode("UTF-8")
                                logging.info(msg)
                                if progress is not None:
                                    progress.append_message(msg)
                            while session.recv_stderr_ready():
                                msg = session.recv_stderr(1024).decode("UTF-8")
                                logging.warning(msg)
                                if progress is not None:
                                    progress.append_message(msg)

                        if session.recv_exit_status() != 0:
                            logging.error("Error executing docker-compose.")

            ports = self._merge_props(plat, configuration, "ports")
            volumes = self._merge_props(plat, configuration, "volumes")
            devices = self._append_props(plat, configuration, "devices")
            extraparms = self._merge_props(plat, configuration, "extraparms")
            networks = list(
                dict.fromkeys(self._append_props(plat, configuration, "networks"))
            )

            if progress is not None:
                progress.append_message("Starting new instance...")

            return rd.run_image(
                limg,
                self.get_container_name(limg),
                ports,
                volumes,
                devices,
                plat.privileged,
                extraparms,
                networks,
            ).attrs

    def stop(self, configuration: str, device):
        """Stops application container

        Arguments:
            configuration {str} -- debug/release
            device {TargetDevice} -- device
        """
        plat = platformconfig.PlatformConfigs().get_platform(self.platformid)

        container = self.get_container(configuration, device)

        if container is None:
            return

        try:
            if container.status == "running" or container.status == "restarting":

                # try to detach from network first
                networks = list(
                    dict.fromkeys(self._append_props(plat, configuration, "networks"))
                )

                if len(networks) > 0:

                    with remotedocker.RemoteDocker(device) as rd:
                        # collect networks to ensure that they are available
                        nets = []

                        for network in networks:
                            nets.append(rd.get_network(network))

                        for network in nets:
                            if network is not None:
                                network.disconnect(container, force=True)

                container.stop()

            container.remove()
        except docker.errors.DockerException as e:
            raise exceptions.RemoteDockerError(device, str(e))

        # check if we need to run docker-compose down
        dockercomposefile = self.get_prop(configuration, "dockercomposefile")

        if dockercomposefile is not None and len(dockercomposefile) > 0:
            dockercomposefile = plat.get_prop(configuration, "dockercomposefile")

        if dockercomposefile is not None and len(dockercomposefile) > 0:

            ssh = sharedssh.SharedSSHClient.get_connection(device)

            with paramiko.SFTPClient.from_transport(ssh.get_transport()) as sftp:

                with ssh.get_transport().open_session() as session:
                    session.exec_command(
                        "cd "
                        + device.homefolder
                        + "/"
                        + self.id
                        + " && docker-compose down"
                    )

                    while not session.exit_status_ready():
                        while session.recv_ready():
                            logging.info(session.recv(1024).decode("UTF-8"))
                        while session.recv_stderr_ready():
                            logging.warning(session.recv_stderr(1024).decode("UTF-8"))

                    if session.recv_exit_status() != 0:
                        logging.error("Error executing docker-compose.")

        # run shutdown scripts
        self._runscript(configuration, plat, device, "shutdownscript", None)

    def get_container(
        self, configuration, device, only_running=True
    ) -> docker.models.containers.Container:
        """Returns information about current container running on target

        Arguments:
            configuration {str} -- debug/release
            device {TargetDevice} -- device
            only_running {bool} -- return the container only if it's currently running
        """
        imgid = self.images[configuration]

        if imgid is None or imgid == "":
            raise exceptions.ImageNotFoundError("")

        try:
            ld = docker.from_env()

            try:
                limg = ld.images.get(imgid)
            except docker.errors.ImageNotFound:
                raise exceptions.ImageNotFoundError(imgid)

            with remotedocker.RemoteDocker(device) as rd:
                if not only_running or rd.is_container_running(
                    self.get_container_name(limg)
                ):
                    return rd.get_container(self.get_container_name(limg))
        except docker.errors.DockerException as e:
            raise exceptions.LocalDockerError(e)

        return None

    def get_sdk_container(
        self, configuration: str
    ) -> docker.models.containers.Container:
        """Returns information about current SDK container

        Arguments:
            configuration {str} -- debug/release
        """

        instance = self._get_sdk_container_name(configuration)

        try:
            localdocker = docker.from_env()
            cnt = localdocker.containers.get(instance)

            return cnt
        except docker.errors.DockerException as e:
            raise exceptions.SDKContainerNotFoundError(e)

        return None

    def get_container_name(self, img) -> str:
        """Builds up container name from an image

        Arguments:
            img {docker.models.images.Image} -- Image

        Returns:
            str -- full container name
        """

        imagename = ""

        if type(img) is docker.models.images.Image:
            imagename = img.tags[0]
        elif type(img) is dict:
            imagename = img["RepoTags"][0]
        elif type(img) is list:
            imagename = img[0] + ":" + img[1]
        else:
            imagename = str(img)

        imagename = imagename.replace(":", "_")
        imagename = imagename.replace("/", "_")
        return imagename + "_instance"

    def _get_sdk_container_name(self, configuration: str) -> str:
        """Return the name of the SDK container for this application

        Arguments:
            configuration {str} -- debug/release

        Raises:
            exceptions.PlatformDoesNotExistError: invalid platform id
            exceptions.PlatformDoesNotRequireSDKError: platform does not need an SDK

        Returns:
            str -- container instance name
        """

        assert self.id is not None

        platform = platformconfig.PlatformConfigs().get_platform(self.platformid)

        assert platform.id is not None

        if not platform.usesdk:
            raise exceptions.PlatformDoesNotRequireSDKError(self.platformid)

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

    def _get_sdk_image_name(self, configuration: str) -> str:
        """Returns the name of the SDK container image for the application

        Arguments:
            configuration {str} -- debug/release

        Returns:
            str -- image name
        """

        assert self.id is not None

        platform = platformconfig.PlatformConfigs().get_platform(self.platformid)

        assert platform.id is not None

        if not platform.usesdk:
            raise exceptions.PlatformDoesNotRequireSDKError(self.platformid)

        appname = self.get_custom_prop(configuration, "appname")

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
        self, configuration: str, progress: Optional[progresscookie.ProgressCookie]
    ):
        """Builds a new image of the SDK container

        Arguments:
            configuration {str} -- active configuration
            progress (Optional[ProgressCookie]): progress object or None

        Raises:
            exceptions.PlatformDoesNotRequireSDKError: [description]
        """

        assert self.folder is not None

        containerwasrunning = False

        platform = platformconfig.PlatformConfigs().get_platform(self.platformid)

        assert platform.folder is not None

        instance = self._get_sdk_container_name(configuration)

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

            sdkcontainername = platform.get_prop(configuration, "sdkcontainer")

            assert sdkcontainername is not None

            dockertemplatefull = platform.folder / sdkcontainername

            dockerfile = self._get_work_folder() / ("Dockerfile_SDK." + configuration)

            utils.apply_template(
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
                self._get_sdk_image_name(configuration),
                None,
                progress,
            )

            if sdkimage is None:
                raise exceptions.ImageNotFoundError(
                    self._get_sdk_image_name(configuration)
                )

            localdocker.containers.prune()

            self.sdkimages[configuration] = str(sdkimage.id)
            self.save()

            if containerwasrunning:
                self.start_sdk_container(configuration, False, progress)

        except docker.errors.DockerException as e:
            raise exceptions.LocalDockerError(e)

    def _sync_sysroot(self, configuration: str):
        """Copies sysroot folders from container to SDK container

        Arguments:
            configuration {str} -- debug/release

        Raises:
            exceptions.SDKContainerNotRunningError: [description]
            exceptions.ImageNotFoundError: [description]
            exceptions.ImageNotFoundError: [description]
            exceptions.LocalDockerError: [description]
            exceptions.RemoteCommandError: [description]
            exceptions.SSHError: [description]
        """

        assert self.folder is not None

        self.start_sdk_container(configuration, True, None)

        if self.sdksshaddress is None:
            raise exceptions.SDKContainerNotRunningError(self.id)

        plat = platformconfig.PlatformConfigs().get_platform(self.platformid)

        if self.images[configuration] is None or self.images[configuration] == "":
            raise exceptions.ImageNotFoundError(configuration)

        try:
            d = docker.from_env()

            try:
                image = d.images.get(self.images[configuration])
            except docker.errors.ImageNotFound:
                raise exceptions.ImageNotFoundError(self.images[configuration])

            # starts a dummy container, just to export FS
            container = d.containers.run(image.id, detach=True)

            try:

                outputpath = self._get_work_folder() / (
                    "filesystem_" + configuration + ".tar"
                )

                if outputpath.exists():
                    os.remove(str(outputpath))

                with open(outputpath, "wb") as output:
                    for c in container.export():
                        output.write(c)

                    output.flush()
                    output.close()

            except:
                container.stop()
                container.remove(force=True)
                raise

            container.stop()
            container.remove(force=True)
        except docker.errors.DockerException as e:
            raise exceptions.LocalDockerError(e)

        # extract sysroot contents
        destfolder = self._get_work_folder() / ("sysroot_" + configuration)

        if destfolder.exists():
            shutil.rmtree(str(destfolder))

        destfolder.mkdir()

        # strips begginning "/" from paths and adds terminating "/"
        roots = [r if len(r) == 0 else r[1:] + "/" for r in plat.sysroots["lib"]] + [
            r if len(r) == 0 else r[1:] + "/" for r in plat.sysroots["include"]
        ]

        with tarfile.open(outputpath, "r:") as archive:
            members = archive.getmembers()

            # checks files in selected folder
            for member in members:

                if not any([member.name.startswith(r) for r in roots]):
                    continue

                try:
                    if member.isfile() or member.isdir():
                        archive.extract(member, path=destfolder)
                    elif member.issym() or member.islnk():
                        try:
                            archive.extract(member, path=destfolder)
                        except RecursionError:
                            logging.warning(
                                "SYNC - Invalid link %s in container filesystem.",
                                member.name,
                            )
                except OSError as e:
                    logging.warning(
                        "SYNC - Error %d extracting %s from container filesystem.",
                        e.errno,
                        member.name,
                    )

        # we can copy sysroot to the SDK container via ssh
        try:
            with paramiko.SSHClient() as ssh:
                ssh.load_system_host_keys()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

                ssh.connect(
                    "localhost",
                    self.sdksshaddress["HostPort"],
                    username=plat.sdkcontainerusername,
                    password=plat.sdkcontainerpassword,
                )

                stdout = ssh.exec_command("rm -fR sysroot")[1]
                status = stdout.channel.recv_exit_status()

                if status != 0:
                    raise exceptions.RemoteCommandError("rm -fR sysroot", status)

                with paramiko.SFTPClient.from_transport(ssh.get_transport()) as sftp:

                    try:
                        sftp.stat(".ssh")
                    except FileNotFoundError:
                        sftp.mkdir(".ssh")

                    try:
                        sftp.stat(".ssh/id_rsa")
                        sftp.remove(".ssh/id_rsa")
                    except FileNotFoundError:
                        pass

                    sftp.put(str(self.folder / "id_rsa"), ".ssh/id_rsa", confirm=True)
                    sftp.chmod(".ssh/id_rsa", 0o600)

                    sftp.mkdir("sysroot")

                    for dirpath, dirs, files in os.walk(destfolder):

                        remote = dirpath.replace(str(destfolder), "sysroot", 1)

                        # convert win path separator to linux
                        remote = remote.replace("\\", "/")

                        for dir in dirs:
                            logging.info(
                                "SYNC - Creating remote folder %s", remote + "/" + dir
                            )
                            sftp.mkdir(remote + "/" + dir)

                        for file in files:
                            logging.info("SYNC - Copying file %s", remote + "/" + file)
                            sftp.put(
                                os.path.join(dirpath, file),
                                remote + "/" + file,
                                confirm=True,
                            )

        except paramiko.SSHException as e:
            raise exceptions.SSHError(e)

    def update_sdk(
        self, configuration: str, progress: Optional[progresscookie.ProgressCookie]
    ):
        """Updates the application SDK

        Args:
            configuration (str): debug/release
            progress (Optional[progresscookie.ProgressCookie]): progress object or None

        Raises:
            exceptions.PlatformDoesNotRequireSDKError: self explanatory
            exceptions.SDKRequiresConfiguration: wrong configuration passed
        """

        platform = platformconfig.PlatformConfigs().get_platform(self.platformid)

        if not platform.usesdk:
            raise exceptions.PlatformDoesNotRequireSDKError(self.platformid)

        if platform.usesysroots:
            self._sync_sysroot(configuration)
        else:
            if configuration is None:
                raise exceptions.SDKRequiresConfiguration()
            self._build_sdk_image(configuration, progress)

    def start_sdk_container(
        self,
        configuration: str,
        build: bool,
        progress: Optional[progresscookie.ProgressCookie],
    ):
        """
        Runs an instance of the SDK container that will be specific
        for this application object

        Arguments:
            configuration {str} - debug/release
            build {bool} - build container if it does not exist yet
            progress (Optional[ProgressCookie]): progress object or None

        Raises:
            exceptions.PlatformDoesNotRequireSDKError -- raised if the
                                                         platform does
                                                         not need an SDK
        """

        if self.sdksshaddress is not None:
            ports = {"22/tcp": int(self.sdksshaddress["HostPort"])}
        else:
            # None is a valid value when you want host-assigned port
            ports = {"22/tcp": None}  # type: ignore

        self.sdksshaddress = None

        instance = self._get_sdk_container_name(configuration)
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

        if container is None:
            if platform.usesdk and not platform.usesysroots:
                try:
                    _ = localdocker.images.get(self._get_sdk_image_name(configuration))
                except docker.errors.NotFound:
                    if build:
                        logging.info("SDK - SDK image not found, building it.")
                        self._build_sdk_image(configuration, progress)
                    else:
                        raise exceptions.ImageNotFoundError(
                            self._get_sdk_image_name(configuration)
                        )

            try:
                container = localdocker.containers.run(
                    self._get_sdk_image_name(configuration),
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
                self.sdksshaddress = container.attrs["NetworkSettings"]["Ports"][
                    "22/tcp"
                ][0]
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
            self.sdksshaddress = container.attrs["NetworkSettings"]["Ports"]["22/tcp"][
                0
            ]

    def sync_folders(
        self,
        sourcefolder: str,
        configuration: str,
        deviceid: str,
        containerfolder: str,
        source_is_sdk: bool,
        progress: Optional[progresscookie.ProgressCookie],
    ):
        """Sync folders from host/SDK container to the app container

        Arguments:
            sourcefolder {str} -- source folder
            configuration {str} -- app configuration (debug/release)
            deviceid {str} -- target device
            containerfolder {str} -- target folder inside the app container
            source_is_sdk {bool} -- source folder is inside the app container
            progress (Optional[ProgressCookie]): progress object or None

        Raises:
            exceptions.ContainerNotRunningError: target container must be running
            exceptions.SDKContainerNotRunningError: if source is SDK, SDK container must be running
            exceptions.RemoteCommandError: Error executing rsync command
        """
        # get device info
        plat = platformconfig.PlatformConfigs().get_platform(self.platformid)
        device = targetdevice.TargetDevices()[deviceid]

        # check that app container is running
        container = self.get_container(configuration, device)

        if container is None:
            raise exceptions.ContainerNotRunningError(device, self.id)

        if container.status != "running":
            raise exceptions.ContainerNotRunningError(device, self.id)

        if "host" in container.attrs["NetworkSettings"]["Networks"]:
            port = "2222"
        else:

            if not "2222/tcp" in container.attrs["NetworkSettings"]["Ports"]:
                raise exceptions.ContainerDoesNotSupportSSH()

            ports = container.attrs["NetworkSettings"]["Ports"]["2222/tcp"]
            port = ports[0]["HostPort"]

        if source_is_sdk:
            self.start_sdk_container(configuration, True, progress)

            if self.sdksshaddress is None:
                raise exceptions.SDKContainerNotRunningError(self.id)

            # connect to SDK container
            with paramiko.SSHClient() as ssh:
                ssh.load_system_host_keys()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

                ssh.connect(
                    "localhost",
                    self.sdksshaddress["HostPort"],
                    username=plat.sdkcontainerusername,
                    password=plat.sdkcontainerpassword,
                )

                with paramiko.SFTPClient.from_transport(ssh.get_transport()) as sftp:

                    try:
                        sftp.stat(".ssh")
                    except FileNotFoundError:
                        sftp.mkdir(".ssh")

                    try:
                        sftp.stat(".ssh/id_rsa")
                        sftp.remove(".ssh/id_rsa")
                    except FileNotFoundError:
                        pass

                    assert self.folder is not None

                    sftp.put(str(self.folder / "id_rsa"), ".ssh/id_rsa", confirm=True)
                    sftp.chmod(".ssh/id_rsa", 0o600)

                rsynccommand = "rsync -rzv "
                rsynccommand += (
                    '-e "ssh -p ' + port + ' -o \\"StrictHostKeyChecking no\\"" '
                )
                # source
                rsynccommand += sourcefolder + "/* "

                assert self.username is not None

                # destination
                rsynccommand += (
                    self.username
                    + "@"
                    + device.get_current_ip()
                    + ":"
                    + containerfolder
                )

                _, stdout, stderr = ssh.exec_command(rsynccommand)

                output = ""

                if progress is not None:
                    for line in iter(stdout.readline(), ""):
                        progress.append_message(line)
                        output += line

                status = stdout.channel.recv_exit_status()

                if status != 0:

                    try:
                        output = "".join(stderr.readlines())
                        output += "".join(stdout.readlines())

                        logging.warning(output)
                    except:
                        pass
                    raise exceptions.RemoteCommandError(rsynccommand, status)
        else:
            rsync.run_rsync(
                sourcefolder,
                deviceid,
                containerfolder,
                self.get_privatekeypath(),
                int(port),
                progress,
            )

    def touch(self):
        """ Set modification date to current time
        """

        self.modificationdate = datetime.datetime.utcnow().isoformat()

    def destroy(self):
        """Removes app and all associated files
        """

        try:
            d = docker.from_env()

            if self.images["debug"] is not None and self.images["debug"] != "":
                if d.images.get(self.images["debug"]) is not None:
                    d.images.remove(image=self.images["debug"], force=True, prune=True)

            if self.images["release"] is not None and self.images["release"] != "":
                if d.images.get(self.images["release"]) is not None:
                    d.images.remove(
                        image=self.images["release"], force=True, prune=True
                    )

            if self.sdkimages["debug"] is not None and self.sdkimages["debug"] != "":
                if d.images.get(self.sdkimages["debug"]) is not None:
                    d.images.remove(
                        image=self.sdkimages["debug"], force=True, prune=True
                    )

            if (
                self.sdkimages["release"] is not None
                and self.sdkimages["release"] != ""
            ):
                if d.images.get(self.sdkimages["release"]) is not None:
                    d.images.remove(
                        image=self.sdkimages["release"], force=True, prune=True
                    )
            super().destroy()
        except:
            logging.exception("Exception destroying application object")

    def reseal(self):
        """ Cleans up app-id and keys. Those will be re-created next time
            the application will be re-opened. This can be used to upload
            the app configuration to a git repo that can be cloned/forked
            and avoids that all the clones keep the same IDsself.
            After this operation the application won't be usable anymore.
        """
        applications = ApplicationConfigs()
        applications.pop(self.id)
        self.id = "00000000-0000-0000-0000-000000000000"
        self.privatekey = ""
        self.publickey = ""
        try:
            os.remove(self.folder / "id_rsa")
            os.remove(self.folder / "id_rsa.pub")
        except:
            pass
        self.save()

    def get_container_logs(self, configuration, device, restart):
        """Returns container logs

        Arguments:
            configuration {str} -- app configuration (debug/release)
            device {TargetDevice} -- target device
            restart {bool} -- reloads log generator

        Returns:
            line {str} -- log line on None for EOF
        """

        log = None

        container = self.get_container(configuration, device, only_running=False)

        if container is None:
            return None

        if not device.id in self.logs:
            self.logs[device.id] = {}

        if configuration in self.logs[device.id] and not restart:
            log = self.logs[device.id][configuration]
        else:
            log = container.logs(stream=True)
            self.logs[device.id][configuration] = log

        return utils.get_log_chunk(log)


class ApplicationConfigs(Dict[str, ApplicationConfig], metaclass=singleton.Singleton):
    """Class used to manage the applications.
       It does not load all the objects at startup, apps are loaded on demand.
    """

    def load_application(self, folder):
        """Loads an application from the filesystem

        Arguments:
            folder {Path} -- folder
        """

        if not os.path.exists(folder):
            raise exceptions.InvalidPathError(folder)

        app = ApplicationConfig(folder)

        # in this way we check that the platform is valid
        plat = platformconfig.PlatformConfigs().get_platform(app.platformid)

        if plat is None:
            return None

        self[app.id] = app
        return app

    def create_new_application(
        self, rootfolder, platform, username
    ) -> ApplicationConfig:
        """static function used to create a new application

        Arguments:
            rootfolder {folder} -- Folder where app files are stored
            platform {PlatformConfig} -- platform
        """
        # finds a new folder for the app config
        c = 0

        if not os.path.exists(rootfolder):
            raise exceptions.InvalidPathError(rootfolder)

        while (rootfolder / ("appconfig_" + str(c))).exists():
            c += 1

        app = ApplicationConfig(rootfolder / ("appconfig_" + str(c)))

        app.platformid = platform.id
        app.username = username
        app.save()

        assert app.id is not None

        self[app.id] = app
        return app
