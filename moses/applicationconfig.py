"""Classes used to manage applications."""
import os
import shutil
import platform as platform_module
import logging
import uuid
import tarfile
import docker
import docker.models.containers
import paramiko
import singleton
import config
import platformconfig
import remotedocker
import exceptions
import datetime
import targetdevice
import socket
import logs
import tags
import sharedssh
import stat
import time
import socket
import rsync
import pathlib
import progresscookie
import dockerapi
from pathlib import Path
from typing import Optional, Dict, Any, List, Callable, Tuple
import yaml


def _blkio_weight_device_cmdline_helper(devices: list) -> str:
    """Translate parameters in command line-compatible format."""
    cmdline = ""

    for v in devices:
        cmdline += "--blkio-weight-device " + v["Path"] + ":" + str(v["Weight"]) + " "

    return cmdline


def _device_read_bps_cmdline_helper(limits: list) -> str:
    """Translate parameters in command line-compatible format."""
    cmdline = ""

    for v in limits:
        cmdline += "--device-read-bps " + v["Path"] + ":" + str(v["Rate"]) + " "

    return cmdline


def _device_write_bps_cmdline_helper(limits: list) -> str:
    """Translate parameters in command line-compatible format."""
    cmdline = ""

    for v in limits:
        cmdline += "--device-write-bps " + v["Path"] + ":" + str(v["Rate"]) + " "

    return cmdline


def _device_read_iops_cmdline_helper(limits: list) -> str:
    """Translate parameters in command line-compatible format."""
    cmdline = ""

    for v in limits:
        cmdline += "--device-read-iops " + v["Path"] + ":" + str(v["Rate"]) + " "

    return cmdline


def _device_write_iops_cmdline_helper(limits: list) -> str:
    """Translate parameters in command line-compatible format."""
    cmdline = ""

    for v in limits:
        cmdline += "--device-write-iops " + +v["Path"] + ":" + str(v["Rate"]) + " "

    return cmdline


def _log_config_cmdline_helper(value: dict) -> str:
    """Translate parameters in command line-compatible format."""
    cmdline = "--log-driver " + value["type"]

    for v in value["config"].items():
        cmdline += " --log-opt " + v[0] + "=" + v[1] + " "

    return cmdline


def _mounts_cmdline_helper(mounts: dict) -> str:
    """Translate parameters in command line-compatible format."""
    cmdline = ""

    for m in mounts:
        cmdline += "--mount "
        cmdline += "type=" + m["type"]
        cmdline += ",source=" + m["source"]
        cmdline += ",target=" + m["target"]
        cmdline += ",readonly=" + ("1" if m["read_only"] else "0") + " "

    return cmdline


def _ports_cmdline_helper(ports: dict) -> str:
    """Translate parameters in command line-compatible format."""
    cmdline = ""

    for p in ports.items():
        cmdline += "--publish "
        containerport = p[0]

        if p[1] is None:
            cmdline += containerport + " "
        elif isinstance(p[1], int):
            cmdline += str(p[1]) + ":" + containerport + " "
        elif isinstance(p[1], tuple):
            cmdline += p[1][0] + ":" + p[1][1] + ":" + containerport + " "

    return cmdline


def _restart_policy_cmdline_helper(value: dict) -> str:
    """Translate parameters in command line-compatible format."""
    cmdline = ""

    cmdline += "--restart-condition " + value["Name"] + " "
    cmdline += "--restart-max-attempts" + value["MaximumRetryCount"] + " "

    return cmdline


def _ulimits_cmdline_helper(ulimits: list) -> str:
    """Translate parameters in command line-compatible format."""
    cmdline = ""

    for u in ulimits:
        cmdline += "--ulimit " + u.name + "=" + str(u.soft) + ":" + str(u.hard) + " "

    return cmdline


def _volumes_cmdline_helper(volumes: dict) -> str:
    """Translate parameters in command line-compatible format."""
    cmdline = ""

    for v in volumes.items():
        cmdline += " --volume " + v[0] + v[1]["bind"] + "," + v[1]["mode"]

    return cmdline


class ApplicationConfig(config.ConfigurableKeysObject):
    """Class used to manage an application."""

    readonlyfields = config.ConfigurableKeysObject.readonlyfields.union(
        {"images", "sdkimages"}
    )

    non_nullable_properties = ["dockercomposefile", "startupscript", "shutdownscript"]
    configurations = ["common", "debug", "release"]

    def __init__(self, folder: Optional[pathlib.Path] = None):
        """Load data from the configuration folder.

        :param folder: path of the folder used to store application configuration
        :type folder: pathlib.Path, optional

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
        """Save object data."""
        if self.folder is None:
            return

        # we got a folder, but it may not be an existing one
        if not self.folder.exists():
            self.folder.mkdir()

        super().save()

    def load(self) -> None:
        """Load configuration from an existing folder.

        This will re-create keys and ids if those have been cleaned-up using the reseal function

        """
        super().load()

        if self.id == "00000000-0000-0000-0000-000000000000":
            self.id = str(uuid.uuid4())
            self.privatekey = None
            self.publickey = None
            self.save()

        ld = docker.from_env()

        for field in ["images", "sdkimages"]:
            for configuration in ["debug", "release"]:
                imgid = self.__dict__[field][configuration]

                if imgid is None or imgid == "":
                    continue

                try:
                    limg = ld.images.get(imgid)
                except docker.errors.ImageNotFound:
                    self.__dict__[field][configuration] = ""

    def _generate_keys(self) -> None:
        """Generate keys for SSH connectivity.

        The public key is also saved as regular file inside the configuration folder.add()

        """
        super()._generate_keys()

        assert self.folder is not None

        with open(str(self.folder / "id_rsa.pub"), "w") as f:
            assert self.publickey is not None
            f.write(self.publickey)

    def _build_folder_path(self) -> Path:
        """Build folder path (not implemented for applications)."""
        raise Exception("Application must have a defined base folder path.")

    def is_valid(self, fields: dict = None) -> bool:
        """Validate the fields of current object.

        :param fields: object properties as a dictionary, if None is passed then self.__dict__ is used
        :type fields: dict
        :returns: true if all fields contain valid values
        :rtype: bool

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

    def __getstate__(self) -> Dict[str, Any]:
        """Return a dictionary with exported properties.

        :return: properties as a dictionary
        :rtype: Dict[str, Any]

        """
        # for applications we keep id in the serialized format
        fields = super().__getstate__()
        fields["id"] = self.id
        fields["sdksshaddress"] = self.sdksshaddress
        if "logs" in fields:
            del fields["logs"]
        return fields

    def _to_json(self) -> Dict[str, Any]:
        """Convert object to an array of json-compatible key-value pairs.

        :return: properties as a dictionary
        :rtype: Dict[str, Any]

        """
        # we return also folder in json
        fields = super()._to_json()
        fields["folder"] = str(self.folder)
        return fields

    def get_custom_prop(self, configuration: str, property: str) -> Optional[str]:
        """Return value of custom property.

        If there is a configuration-specific value its returned, otherwise
        common value is checked and returned. If no value is found, the function
        return None.

        :param configuration: debug/release
        :type configuration: str
        :param property: property name
        :type property: str
        :return: value of the property of None if it's not defined
        :rtype: str | None

        """
        if property in self.props[configuration]:
            return str(self.props[configuration][property])
        if property in self.props["common"]:
            return str(self.props["common"][property])
        return None

    def _get_value(self, obj: str, tag: str, configuration: str) -> str:
        """Return value for a tag in the format <application/platform>.tag.

        :param obj: application or platform
        :type obj: str
        :param tag: tag name
        :type tag: str
        :param configuration: debug/release
        :type obj: str
        :returns: value of the tag or empty string
        :rtype: str

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
        """Return app work folder.

        If folder does not exists, it will be created

        :returns: work folder, it's granted to exists
        :rtype: pathlib.Path

        """
        if self.folder is None:
            raise Exception("Folder is not configured.")

        workfolder: Path = self.folder / "work"

        if not os.path.exists(workfolder):
            workfolder.mkdir()

        return workfolder

    def check_image(self, configuration: str) -> bool:
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
        except docker.errors.DockerException as e:
            raise exceptions.LocalDockerError(e)

    def _get_image_name(self, configuration: str) -> str:
        """Return image tag for the application.

        :param configuration: str
        :param configuration: str:

        :returns: unique tag for the image
        :rtype: str

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
    ) -> None:
        """Generate Dockerfile and build the image.

        :param configuration: debug/release
        :type configuration: str
        :param progress: object used to report progress of the operation
        :type progress: progresscookie.ProgressCookie, optional

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

            tags.apply_template(
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
    ) -> None:
        """Deploy image to a target device.

        The function checks if the image is already up-to-date on the target
        and returns with no error if that's the case

        :param configuration: debug/release
        :type configuration: str
        :param device: device where image must be deployed
        :type device: targetdevice.TargetDevice
        :param progress: object used to report operation progress
        :type progress: progresscookie.ProgressCookie, optional

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
    ) -> Dict[str, Any]:
        """Merge common and configuration-specific values in dictionaries.

        This internal function is used to generate a single dictionary with
        values specified at different levels of configuration (plaform, application,
        common and configuration-specific)

        :param plat: platform
        :type plat: platformconfig.PlatformConfig
        :param configuration: debug/release
        :type configuration: str
        :param prop: property name
        :param prop: str
        :returns: merged dictionary
        :rtype: Dict[str,Any]

        """
        merged = plat.__dict__[prop]["common"].copy()
        merged.update(plat.__dict__[prop][configuration])
        merged.update(self.__dict__[prop]["common"])
        merged.update(self.__dict__[prop][configuration])

        for key, value in merged.items():
            if isinstance(value, str):
                newvalue = tags.replace_tags(
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
        """Append values of a property from the different levels of configuration.

        The platform common one is taken first, then configuration
        is appended, then app common, then app configuration

        :param plat: platform
        :type plat: platformconfig.PlatformConfig
        :param configuration: debug/release
        :type configuration: str
        :param prop: property name
        :param prop: str
        :returns: merged values
        :rtype: list

        """
        merged = plat.__dict__[prop]["common"].copy()
        merged.extend(plat.__dict__[prop][configuration])
        merged.extend(self.__dict__[prop]["common"])
        merged.extend(self.__dict__[prop][configuration])

        return list(
            map(
                lambda i: i
                if not isinstance(i, str)
                else tags.replace_tags(
                    i,
                    lambda obj, tag, args: self._get_value(obj, tag, args),
                    configuration,
                ),
                merged,
            )
        )

    def get_prop(self, configuration: str, prop: str) -> Optional[str]:
        """Return a property depending on specific configuration.

        :param configuration: debug/release
        :type configuration: str
        :param prop: property name
        :type prop: str
        :returns: property value or None
        :rtype: str | None

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
    ) -> None:
        """Run a script configured as "scriptname" property in platform and/or application.

        :param configuration: debug/release
        :type configuration: str
        :param plat: platform
        :type plat: platformconfig.PlatformConfig
        :param device: target device
        :type device: targetdevice.TargetDevice
        :param scriptname: property where script name is saved
        :type scriptname: str
        :param progress: object used to report execution progress
        :type progress: progresscookie.ProgressCookie, optional

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

            transport = ssh.get_transport()

            assert transport is not None

            sftp = paramiko.sftp_client.SFTP.from_transport(transport)

            assert sftp is not None
            assert self.id is not None

            sftp.chdir(device.homefolder)

            try:
                sftp.stat(self.id)
            except:
                sftp.mkdir(self.id)

            sftp.chdir(self.id)

            if script is not None:

                assert self.folder is not None

                fullscriptpath = self.folder / script
                targetscriptpath = self._get_work_folder() / (
                    script + "." + configuration
                )
                tags.apply_template(
                    str(fullscriptpath),
                    str(targetscriptpath),
                    lambda obj, tag, args: self._get_value(obj, tag, args),
                    configuration,
                )
                sftp.put(str(targetscriptpath), script, confirm=True)
                sftp.chmod(script, stat.S_IXUSR | stat.S_IRUSR | stat.S_IWUSR)

            if platformscript is not None:
                fullplatformscript = plat.folder / platformscript
                targetplatformscript = self._get_work_folder() / (
                    platformscript + "." + configuration
                )
                tags.apply_template(
                    str(fullplatformscript),
                    str(targetplatformscript),
                    lambda obj, tag, args: self._get_value(obj, tag, args),
                    configuration,
                )
                sftp.put(str(targetplatformscript), platformscript, confirm=True)
                sftp.chmod(platformscript, stat.S_IXUSR | stat.S_IRUSR | stat.S_IWUSR)

            scriptpath = device.homefolder + "/" + str(self.id)

            scriptfile = None

            if script is not None:
                scriptfile = script
            else:
                scriptfile = platformscript

            assert scriptfile is not None

            if progress is not None:
                progress.append_message(f"running script {scriptfile}")

            transport = ssh.get_transport()

            assert transport is not None

            session = transport.open_session()

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
    ) -> docker.models.containers.Container:
        """Run the application container on the specified device.

        :param configuration: debug/release
        :type configuration: str
        :param device: target device
        :type device: targetdevice.TargetDevice
        :param progress: object used to report execution progress
        :type progress: progresscookie.ProgressCookie, optional

        :returns: container instance
        :rtype: docker.models.containers.Container

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

            assert self.folder is not None
            assert plat.folder is not None

            if dockercomposefile is not None and len(dockercomposefile) > 0:
                dockercomposefilepath = self.folder / dockercomposefile
            else:
                dockercomposefile = plat.get_prop(configuration, "dockercomposefile")
                if dockercomposefile is not None and len(dockercomposefile) > 0:
                    dockercomposefilepath = plat.folder / dockercomposefile

            if dockercomposefilepath is not None:

                assert dockercomposefile is not None

                if progress is not None:
                    progress.append_message("running docker-compose...")

                ssh = sharedssh.SharedSSHClient.get_connection(device)

                transport = ssh.get_transport()

                assert transport is not None

                sftp = paramiko.SFTPClient.from_transport(transport)

                assert sftp is not None

                sftp.chdir(device.homefolder)

                try:
                    sftp.stat(self.id)
                except:
                    sftp.mkdir(self.id)

                sftp.chdir(self.id)

                targetdockercomposepath = self._get_work_folder() / (
                    dockercomposefile + "." + configuration
                )
                tags.apply_template(
                    str(dockercomposefilepath),
                    str(targetdockercomposepath),
                    lambda obj, tag, args: self._get_value(obj, tag, args),
                    configuration,
                )
                sftp.put(str(targetdockercomposepath), "docker-compose.yml")

                with transport.open_session() as session:
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

    def stop(self, configuration: str, device: targetdevice.TargetDevice) -> None:
        """Stop the application container.

        :param configuration: debug/release
        :type configuration: str
        :param device: target device
        :type device: targetdevice.TargetDevice

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

            assert ssh is not None

            transport = ssh.get_transport()

            assert transport is not None

            sftp = paramiko.SFTPClient.from_transport(transport)

            with transport.open_session() as session:

                assert self.id is not None

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
        self,
        configuration: str,
        device: targetdevice.TargetDevice,
        only_running: bool = True,
    ) -> Optional[docker.models.containers.Container]:
        """Return the application container instance.

        :param configuration: debug/release
        :type configuration: str
        :param device: target device
        :type device: targetdevice.TargetDevice
        :param only_running: if set to True will not return stopped/exited/suspended instances
        :type only_running: bool

        :returns: container instance
        :rtype: docker.models.containers.Container | None

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
        """Return SDK container object.

        :param configuration: debug/release
        :type configuration: str

        :returns: container instance
        :rtype: docker.models.containers.Container

        """
        instance = self._get_sdk_container_name(configuration)

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

    def get_container_name(self, img: Any) -> str:
        """Build container name from an image.

        :param img: docker image (can be object, dict or list of name and tag)
        :returns: full container name
        :rtype: str

        """
        imagename = ""

        if type(img) is docker.models.images.Image:
            imagename = img.tags[0]
        elif type(img) is dict:
            assert "RepoTags" in img
            imagename = img["RepoTags"][0]
        elif type(img) is list:
            assert len(img) == 2
            imagename = img[0] + ":" + img[1]
        else:
            imagename = str(img)

        imagename = imagename.replace(":", "_")
        imagename = imagename.replace("/", "_")
        return imagename + "_instance"

    def _get_sdk_container_name(self, configuration: str) -> str:
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

    def _sync_sysroot(self, configuration: str) -> None:
        """Copy sysroot folders from container to SDK container.

        :param configuration: debug/release
        :type configuration: str

        """
        assert self.folder is not None
        assert self.id is not None

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

                assert ssh is not None

                transport = ssh.get_transport()

                assert transport is not None

                sftp = paramiko.SFTPClient.from_transport(transport)

                assert sftp is not None

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
        device_id: str,
        containerfolder: str,
        source_is_sdk: bool,
        progress: Optional[progresscookie.ProgressCookie],
    ) -> None:
        """Sync folders from host/SDK container to the app container.

        :param sourcefolder: source path (depends on source_is_sdk)
        :type sourcefolder: str
        :param configuration: debug/release
        :type configuration: str
        :param device_id: device id
        :type device_id: str
        :param containerfolder: target folder (inside app container)
        :type containerfolder: str
        :param source_is_sdk: if True source folder will be inside SDK container, otherwise on the local filesystem
        :type source_is_sdk: bool
        :param progress: object used to report operation progress
        :type progress: progresscookie.ProgressCookie, optional

        """
        # get device info
        plat = platformconfig.PlatformConfigs().get_platform(self.platformid)
        device = targetdevice.TargetDevices()[device_id]

        # check that app container is running
        container = self.get_container(configuration, device)

        assert self.id is not None

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

                transport = ssh.get_transport()

                assert transport is not None

                sftp = paramiko.sftp_client.SFTP.from_transport(transport)

                assert sftp is not None

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
                sftp.close

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
                    for line in iter(stdout.readline, ""):
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
                device_id,
                containerfolder,
                self.get_privatekeypath(),
                int(port),
                progress,
            )

    def touch(self) -> None:
        """Set modification date to current time."""
        self.modificationdate = datetime.datetime.utcnow().isoformat()

    def destroy(self) -> None:
        """Remove the application and all associated files, containers and images."""
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
        except:
            pass
        self.save()

    def get_container_logs(
        self, configuration: str, device: targetdevice.TargetDevice, restart: bool
    ) -> Optional[str]:
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

        container = self.get_container(configuration, device, only_running=False)

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

    boolean_parms: Dict[str, str] = {
        "auto_remove": "--rm",
        "detach": "--detach",
        "init": "--init",
        "network_disabled": "--network=none",
        "oom_kill_disable": "--oom-kill-disable",
        "privileged": "--privileged",
        "publish_all_ports": "--publish-all",
        "read_only": "--read-only",
        "remove": "--rm",
        "tty": "--tty",
    }

    str_parms: Dict[str, str] = {
        "cgroup_parent": "--cgroup-parent",
        "cpuset_cpus": "--cpuset-cpus",
        "cpuset_mems": "--cpuset-mems",
        "domainname": "--domainname",
        "entrypoint": "--entrypoint",
        "hostname": "--hostname",
        "ipc_mode": "--ipc",
        "isolation": "--isolation",
        "kernel_memory": "--kernel-memory",
        "mac_address": "--mac-address",
        "mem_limit": "--memory",
        "mem_reservation": "--memory-reservation",
        "memswap_limit": "--memory-swap",
        "name": "--name",
        "network": "--network",
        "network_mode": "--network",
        "pid_mode": "--pid",
        "pids_limit": "--pids-limit",
        "platform": "--platform",
        "runtime": "--runtime",
        "shm_size": "--shm-size",
        "stop_signal": "--stop-signal",
        "user": "--user",
        "userns_mode": "--userns",
        "uts_mode": "--uts",
        "volume_driver": "--volume-driver",
        "working_dir": "--workdir",
    }

    int_parms: Dict[str, str] = {
        "blkio_weight": "--blkio-weight",
        "cpu_period": "--cpu-period",
        "cpu_quota": "--cpu_quota",
        "cpu_rt_period": "--cpu-rt-period",
        "cpu_rt_runtime": "--cpu-rt-runtime",
        "cpu_shares": "--cpu-shares",
        "kernel_memory": "--kernel-memory",
        "mem_limit": "--memory",
        "mem_reservation": "--memory-reservation",
        "mem_limit": "--memory",
        "mem_swappiness": "--memory-swappiness",
        "memswap_limit": "--memory-swap",
        "oom_score_adj": "--oom-score-adj",
        "pids_limit": "--pids-limit",
        "shm_size": "--shm-size",
        "user": "--user",
    }

    repeated_list_parms: Dict[str, str] = {
        "cap_add": "--cap-add",
        "cap_drop": "--cap-drop",
        "device_cgroup_rules": "--device-cgroup-rule",
        "devices": "--device",
        "dns": "--dns",
        "dns_opt": "--dns-option",
        "dns_search": "--dns-search",
        "domainname": "--domainname",
        "environment": "--env",
        "group_add": "--group-add",
        "labels": "--label",
        "security_opt": "--security-opt",
        "volumes_from": "--volumes-from",
    }

    joined_list_parms: Dict[str, Tuple] = {"entrypoint": ("--entrypoint", " ")}

    key_val_dict_parms: Dict[str, Tuple] = {
        "environment": ("--env", "="),
        "extra_hosts": ("--add-host", ":"),
        "labels": ("--label", "="),
        "links": ("--link", ":"),
        "storage_opts": ("--storage-opt", "="),
        "sysctls": ("--sysctl", "="),
    }

    special_parms: Dict[str, Callable[..., str]] = {
        "blkio_weight_device": _blkio_weight_device_cmdline_helper,
        "device_read_bps": _device_read_bps_cmdline_helper,
        "device_write_bps": _device_write_bps_cmdline_helper,
        "device_read_iops": _device_read_iops_cmdline_helper,
        "device_write_iops": _device_write_iops_cmdline_helper,
        "log_config": _log_config_cmdline_helper,
        "mounts": _mounts_cmdline_helper,
        "ports": _ports_cmdline_helper,
        "restart_policy": _restart_policy_cmdline_helper,
        "ulimits": _ulimits_cmdline_helper,
        "volumes": _volumes_cmdline_helper,
    }

    def get_docker_commandline(self, configuration: str) -> str:
        """Return a docker command line that can be used to run the application's container.

        :param configuration: debug/release
        :type configuration: str
        :returns: command line for Linux target
        :rtype: str

        Returns:
            str: command line for Linux target
        """
        plat = platformconfig.PlatformConfigs().get_platform(self.platformid)

        if plat is None:
            return None

        ports = self._merge_props(plat, configuration, "ports")
        volumes = self._merge_props(plat, configuration, "volumes")
        devices = self._append_props(plat, configuration, "devices")
        extraparms = self._merge_props(plat, configuration, "extraparms")
        networks = list(
            dict.fromkeys(self._append_props(plat, configuration, "networks"))
        )

        cmdline = "docker run"

        # parse extraparms
        for parm in extraparms:
            rawvalue = extraparms[parm]

            rawvalue = tags.replace_tags(
                rawvalue,
                lambda obj, tag, args: self._get_value(obj, tag, args),
                configuration,
            )
            value = yaml.full_load(rawvalue)

            if parm in ApplicationConfig.boolean_parms:
                if value:
                    cmdline += " " + ApplicationConfig.boolean_parms[parm]
                    continue

            if isinstance(value, str):
                if parm in ApplicationConfig.str_parms:
                    cmdline += (
                        " " + ApplicationConfig.str_parms[parm] + " '" + value + "'"
                    )
                    continue

            if isinstance(value, int):
                if parm in ApplicationConfig.int_parms:
                    cmdline += (
                        " " + ApplicationConfig.int_parms[parm] + " " + str(value)
                    )
                    continue

            if isinstance(value, list):
                if parm in ApplicationConfig.repeated_list_parms:
                    for v in value:
                        cmdline += (
                            " "
                            + ApplicationConfig.repeated_list_parms[parm]
                            + " '"
                            + v
                            + "' "
                        )
                    continue

                if parm in ApplicationConfig.joined_list_parms:
                    cmdline += (
                        " " + ApplicationConfig.repeated_list_parms[parm][0] + " '"
                    )
                    for v in value:
                        cmdline += v + ApplicationConfig.repeated_list_parms[parm][1]
                    continue
                    cmdline += "'"

            if isinstance(value, dict):
                if parm in ApplicationConfig.key_val_dict_parms:
                    for v in value.items():
                        cmdline += (
                            " "
                            + ApplicationConfig.key_val_dict_parms[parm][0]
                            + " "
                            + v[0]
                            + ApplicationConfig.key_val_dict_parms[parm][1]
                            + v[1]
                            + " "
                        )
                    continue

            if parm in ApplicationConfig.special_parms:
                cmdline += " " + ApplicationConfig.special_parms[parm](value)
                continue

            logging.warning(
                "Parameter %s can't be converted into command line parameter", parm
            )

        # parse mountpoints
        for v in volumes.items():
            cmdline += " --volume " + v[0] + ":" + v[1]

        # parse networks
        for n in networks:
            cmdline += " --network " + n

        # parse devices
        for d in devices:
            cmdline += " --device " + d + ":" + d

        # parse ports
        for p in ports.items():
            if p[1] is None:
                cmdline += " --publish " + p[0]
            else:
                cmdline += " --publish " + str(p[1]) + ":" + p[0]

        cmdline += " " + self._get_image_name(configuration)

        # check if there's a command specified in extra parms
        if "command" in extraparms:
            value = extraparms["command"]

            if isinstance(value, list):
                cmdline += " '" + (" ".join(value)) + "'"
            else:
                cmdline += " '" + str(value) + "'"

        return cmdline

    compose_parms: Dict[str, Optional[Callable]] = {
        "cap_add": None,
        "cap_drop": None,
        "cgroup_parent": None,
        "command": None,
        "devices": None,
        "domainname": None,
        "dns": None,
        "dns_search": None,
        "entrypoint": None,
        "environment": None,
        "extra_hosts": lambda x: (
            "extra_hosts",
            map((lambda h: h[0] + ":" + h[1]), x.items()),
        ),
        "healtcheck": None,
        "hostname": None,
        "init": None,
        "isolation": None,
        "labels": None,
        "log_config": None,
        "name": lambda x: ("container_name", x),
        "network_mode": None,
        "pid_mode": lambda x: ("pid", x),
        "ports": lambda x: (
            "ports",
            list(map(lambda y: str(y[0]) + ":" + str(y[1]), x[1].items())),
        ),
        "privileged": None,
        "read_only": None,
        "restart": None,
        "shm_size": None,
        "stdin_open": None,
        "tty": None,
        "user": None,
        "volumes": (
            lambda x: (
                "volumes",
                list(
                    map(
                        lambda y: str(y[0])
                        + ":"
                        + str(y[1]["bind"])
                        + ","
                        + str(y[1]["mode"]),
                        x[1].items(),
                    )
                ),
            )
        ),
        "working_dir": None,
    }

    def get_docker_composefile(self, configuration: str) -> Optional[str]:
        """Return a docker-compose file that can be used to run the application's container and its dependencies.

        :param configuration: debug/release
        :type configuration: str
        :returns: content of the compose file (*nix line-endings)
        :rtype: str | None

        """
        plat = platformconfig.PlatformConfigs().get_platform(self.platformid)

        if plat is None:
            return None

        ports = self._merge_props(plat, configuration, "ports")
        volumes = self._merge_props(plat, configuration, "volumes")
        devices = self._append_props(plat, configuration, "devices")
        extraparms = self._merge_props(plat, configuration, "extraparms")
        networks = list(
            dict.fromkeys(self._append_props(plat, configuration, "networks"))
        )

        composefile = self.get_prop(configuration, "dockercomposefile")

        if composefile is None or len(composefile) == 0:
            composefile = plat.get_prop(configuration, "dockercomposefile")

        if composefile is not None and len(composefile) > 0:
            assert self.folder is not None

            with open(os.path.join(self.folder, composefile), "r") as f:
                composeyaml = yaml.load(f, Loader=yaml.FullLoader)
        else:
            composeyaml = yaml.load("services: {}", Loader=yaml.FullLoader)

        # create and fill new service
        service = dict()

        # merge volumes, devices, ports into extraparms (we can't have multiple instances of the same parameter)
        if not "ports" in extraparms:
            extraparms["ports"] = dict()

        if not "devices" in extraparms:
            extraparms["devices"] = list()

        if not "volumes" in extraparms:
            extraparms["volumes"] = dict()

        for p in ports.items():
            if p[1] == "":
                extraparms["ports"][p[0]] = None
            else:
                extraparms["ports"][p[0]] = p[1]

        for v in volumes.items():
            bind, mode = (v[1] + ",rw").split(",")[0:2]
            extraparms["volumes"][v[0]] = {"bind": bind, "mode": mode}

        extraparms["devices"].extend(devices)

        # process extraparms and add them to the dictionary
        for ep in extraparms.keys():
            if ep in ApplicationConfig.compose_parms:
                if ApplicationConfig.compose_parms[ep] is None:
                    service[ep] = extraparms[ep]
                else:

                    helperfn = ApplicationConfig.compose_parms[ep]

                    assert helperfn is not None

                    parm, value = helperfn((ep, extraparms[ep]))
                    service[parm] = value

        service["image"] = self._get_image_name(configuration)

        if self.get_prop(configuration, "depends_on") is not None:
            service["depends_on"] = self.get_prop(configuration, "depends_on")
        else:
            service["depends_on"] = list(composeyaml["services"].keys())

        composeyaml["services"][self._get_image_name(configuration)] = service

        return yaml.dump(composeyaml)

    def push_to_registry(
        self,
        configuration: str,
        username: str,
        password: str,
        progress: Optional[progresscookie.ProgressCookie],
    ) -> None:
        """Push the application container to a docker registry.

        :param configuration: debug/release
        :type configuration: str
        :param username: username
        :type username: str
        :param password: password
        :param password: str
        :param progress: object use to report operation progress
        :type progress: progresscookie.ProgressCookie, optional

        Image should have been built at least once for the required
        configuration.

        """
        tag = self.get_custom_prop(configuration, "tag")

        if tag is None:
            raise exceptions.NoTagError()

        repository = None

        parts = tag.split(":")
        parts_count=len(parts)
        if parts_count > 1:
            repository=":".join(parts[0:parts_count-1])
            tag = parts[parts_count-1]            
        else:
            repository = tag
            tag = None

        imgid = self.images[configuration]

        if imgid is None or imgid == "":
            logging.error("Image has never been build for application %s.", self.folder)
            raise exceptions.ImageNotFoundError("")

        localdocker = docker.from_env()

        try:
            limg = localdocker.images.get(imgid)
        except docker.errors.ImageNotFound:
            logging.error(
                "Image %s not found when deploying application %s.",
                imgid,
                self.folder,
            )
            raise exceptions.ImageNotFoundError(imgid)

        # ensure that the image is correctly tagged
        limg.tag(repository, tag)

        dockerapi.push_image(localdocker, repository, tag, username, password, progress)


class ApplicationConfigs(Dict[str, ApplicationConfig], metaclass=singleton.Singleton):
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
            raise exceptions.InvalidPathError(folder)

        app = ApplicationConfig(folder)

        # in this way we check that the platform is valid
        plat = platformconfig.PlatformConfigs().get_platform(app.platformid)

        if plat is None:
            return None

        assert app.id is not None

        self[app.id] = app
        return app

    def create_new_application(
        self, rootfolder: Path, platform: platformconfig.PlatformConfig, username: str
    ) -> ApplicationConfig:
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
        c = 0

        if not os.path.exists(rootfolder):
            raise exceptions.InvalidPathError(rootfolder)

        while (rootfolder / ("appconfig_" + str(c))).exists():
            c += 1

        app = ApplicationConfig(rootfolder / ("appconfig_" + str(c)))

        assert platform.id is not None

        app.platformid = platform.id
        app.username = username
        app.save()

        assert app.id is not None

        self[app.id] = app
        return app
