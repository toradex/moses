"""Deployment and remote execution features of ApplicationConfig class.

The class is too complex to stay in a single file, code has been 
splitted in feature-specific modules.
This is why sometimes you see calls with self explicitely passed
as first parameter.
"""
import logging
import docker
import docker.models.containers
import paramiko
import platformconfig
import remotedocker
import exceptions
import targetdevice
import tags
import sharedssh
import stat
import rsync
import progresscookie
from applicationconfig_base import ApplicationConfigBase
from applicationconfig_sdk import start_sdk_container
from typing import Optional, Any


def _get_container_name(self: ApplicationConfigBase, img: Any) -> str:
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


def deploy_image(
    self: ApplicationConfigBase,
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
            logging.error("Image has never been build for application %s.", self.folder)
            raise exceptions.ImageNotFoundError("")

        ld = docker.from_env()

        try:
            limg = _get_local_image(self, configuration)
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

                    progresscookie.progress_message(
                        progress, "Image on target is already up to date."
                    )
                    return

                logging.info("DEPLOY - Image on target is not up to date.")

                progresscookie.progress_message(
                    progress, "Image on target is not up to date, removing it."
                )

                # we need to stop active containers
                containers = rd.get_containers(
                    {"name": _get_container_name(self, rimg)}
                )

                if len(containers) > 0:
                    # it is safe to assume it's only one,
                    # since names must be unique
                    logging.warning("DEPLOY - terminating running instance.")
                    containers[0].remove(force=True)

                rd.delete_image(rimg["Id"], True)

                progresscookie.progress_message(progress, "Image has been removed.")

            else:
                logging.info("DEPLOY - Image not found on target device.")

                progresscookie.progress_message(
                    progress, "Image not found on target device."
                )

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

            progresscookie.progress_message(
                progress, "Image exported, deploying to the target."
            )

            rd.load_image(limg, outputpath, progress)

            progresscookie.progress_message(progress, "Image deployed.")

            logging.info("DEPLOY - Image deployed.")

    except docker.errors.DockerException as e:
        raise exceptions.LocalDockerError(e)


def _runscript(
    self: ApplicationConfigBase,
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
    script = self._get_prop(configuration, scriptname)
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
            targetscriptpath = self._get_work_folder() / (script + "." + configuration)
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

        progresscookie.progress_message(progress, f"running script {scriptfile}")

        transport = ssh.get_transport()

        assert transport is not None

        session = transport.open_session()

        session.exec_command("cd " + scriptpath + "&&" + "./" + scriptfile)

        while not session.exit_status_ready():
            while session.recv_ready():
                msg = session.recv(1024).decode("UTF-8")
                logging.info(msg)
                progresscookie.progress_message(progress, msg)
            while session.recv_stderr_ready():
                msg = session.recv_stderr(1024).decode("UTF-8")
                logging.warning(msg)
                progresscookie.progress_message(progress, msg)

        if session.recv_exit_status() != 0:
            logging.error("Error executing " + scriptname + ".")

        logging.info("Running script:" + scriptname + " done.")


def _get_local_image(
    self: ApplicationConfigBase, configuration: str
) -> docker.models.images.Image:
    """Check that the image exists.

    :param configuration: debug/release
    :type configuration: str
    :return: image
    :rtype: docker.models.images.Image
    """
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
    return limg


def _run_dockercompose(
    self: ApplicationConfigBase,
    configuration: str,
    device: targetdevice.TargetDevice,
    progress: Optional[progresscookie.ProgressCookie],
    plat: platformconfig.PlatformConfig,
) -> None:
    """Execute docker-compose up, if a dockerfile is configured for the application.

    :param configuration: debug/release
    :type configuration: str
    :param device: target device
    :type device: targetdevice.TargetDevice
    :param progress: object used to report operation progress
    :type progress: Optional[progresscookie.ProgressCookie]
    :param plat: platform
    :type plat: platformconfig.PlatformConfig

    If no dockercompose file has been configured for the application, then the system will
    try to run the one configured for the platform.
    """
    dockercomposefile = self._get_prop(configuration, "dockercomposefile")
    dockercomposefilepath = None

    assert self.id is not None
    assert self.folder is not None
    assert plat.folder is not None
    assert device.homefolder is not None

    if dockercomposefile is not None and len(dockercomposefile) > 0:
        dockercomposefilepath = self.folder / dockercomposefile
    else:
        dockercomposefile = plat.get_prop(configuration, "dockercomposefile")
        if dockercomposefile is not None and len(dockercomposefile) > 0:
            dockercomposefilepath = plat.folder / dockercomposefile
    if dockercomposefilepath is not None:
        assert dockercomposefile is not None
        progresscookie.progress_message(progress, "running docker-compose...")
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
                "cd " + device.homefolder + "/" + self.id + " && docker-compose up -d"
            )
            while not session.exit_status_ready():
                while session.recv_ready():
                    msg = session.recv(1024).decode("UTF-8")
                    logging.info(msg)
                    progresscookie.progress_message(progress, msg)
                while session.recv_stderr_ready():
                    msg = session.recv_stderr(1024).decode("UTF-8")
                    logging.warning(msg)
                    progresscookie.progress_message(progress, msg)
            if session.recv_exit_status() != 0:
                logging.error("Error executing docker-compose.")


def run(
    self: ApplicationConfigBase,
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

    limg = _get_local_image(self, configuration)

    with remotedocker.RemoteDocker(device) as rd:

        container = get_container(self, configuration, device)

        if container is not None:

            progresscookie.progress_message(progress, "Stopping current instance...")

            stop(self, configuration, device)

            assert device.id is not None

            if device.id in self.logs:
                if configuration in self.logs[device.id]:
                    del self.logs[device.id][configuration]

        # check scripts for both application and platform, both are deployed
        # if app script exist, then it's the only one invoked (but still has a
        # chance to invoke platform one if needed since it has been deployed in
        # the same place)
        progresscookie.progress_message(progress, "running startup script...")

        _runscript(self, configuration, plat, device, "startupscript", progress)

        _run_dockercompose(self, configuration, device, progress, plat)

        ports = self._merge_props(plat, configuration, "ports")
        volumes = self._merge_props(plat, configuration, "volumes")
        devices = self._append_props(plat, configuration, "devices")
        extraparms = self._merge_props(plat, configuration, "extraparms")
        networks = list(
            dict.fromkeys(self._append_props(plat, configuration, "networks"))
        )

        progresscookie.progress_message(progress, "Starting new instance...")

        return rd.run_image(
            limg,
            _get_container_name(self, limg),
            ports,
            volumes,
            devices,
            plat.privileged,
            extraparms,
            networks,
        ).attrs


def stop(
    self: ApplicationConfigBase, configuration: str, device: targetdevice.TargetDevice
) -> None:
    """Stop the application container.

    :param configuration: debug/release
    :type configuration: str
    :param device: target device
    :type device: targetdevice.TargetDevice

    """
    plat = platformconfig.PlatformConfigs().get_platform(self.platformid)

    container = get_container(self, configuration, device)

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
    dockercomposefile = self._get_prop(configuration, "dockercomposefile")

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
                "cd " + device.homefolder + "/" + self.id + " && docker-compose down"
            )

            while not session.exit_status_ready():
                while session.recv_ready():
                    logging.info(session.recv(1024).decode("UTF-8"))
                while session.recv_stderr_ready():
                    logging.warning(session.recv_stderr(1024).decode("UTF-8"))

            if session.recv_exit_status() != 0:
                logging.error("Error executing docker-compose.")

    # run shutdown scripts
    _runscript(self, configuration, plat, device, "shutdownscript", None)


def get_container(
    self: ApplicationConfigBase,
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

        limg = _get_local_image(self, configuration)

        with remotedocker.RemoteDocker(device) as rd:
            if not only_running or rd.is_container_running(
                _get_container_name(self, limg)
            ):
                return rd.get_container(_get_container_name(self, limg))
    except docker.errors.DockerException as e:
        raise exceptions.LocalDockerError(e)

    return None


def sync_folders(
    self: ApplicationConfigBase,
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
    container = get_container(self, configuration, device)

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
        start_sdk_container(self, configuration, True, progress)

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
                self.username + "@" + device.get_current_ip() + ":" + containerfolder
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
