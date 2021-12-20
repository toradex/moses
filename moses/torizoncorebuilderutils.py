"""Utils for use Torizon Core Builder."""
from typing import Dict, Optional, Tuple, Union
import os
import tempfile
import logging
import docker
# type ignore is needed because docker lib has no stubs for typing
from docker.errors import APIError # type: ignore
from docker.models.containers import Container
import dockerapi
import progresscookie
from moses_exceptions import TorizonCoreBuilderError

# pylint: disable=too-few-public-methods
class TorizonCoreBuilderUtils:
    """Class with static methods for run Torizon Core Builder commands."""

    TCBUILDER_REPO = "torizon/torizoncore-builder"
    TCBUILDER_TAG = "3.2"

    @staticmethod
    def pull_docker_image(
        progress: Optional[progresscookie.ProgressCookie]) -> None:
        """."""
        dockerclient = docker.client.from_env()
        dockerapi.pull_image(
            dockerclient,
            TorizonCoreBuilderUtils.TCBUILDER_REPO,
            TorizonCoreBuilderUtils.TCBUILDER_TAG,
            progress
        )

    @staticmethod
    def yaml_build (
        workspacepath: str,
        yamlfilepath: str,
        progress: Optional[progresscookie.ProgressCookie]) -> None:
        """Run Torizon Core Builder Build."""
        volumes = [
            "deploy:/deploy",
            f"{workspacepath}:/workdir",
            "storage:/storage"
        ]

        TorizonCoreBuilderUtils.__run_tcbuilder(
            f"build \
                --file {yamlfilepath} \
                --force",
            volumes,
            progress
        )

    # pylint: disable=too-many-arguments
    @staticmethod
    def isolate (workspacepath: str,
        host: str,
        username: str,
        password: str,
        output_dir: str,
        progress: Optional[progresscookie.ProgressCookie]) -> None:
        """Run Torizon Core Builder Deploy."""
        volumes = [
            "deploy:/deploy",
            f"{workspacepath}:/workdir",
            "storage:/storage"
        ]

        TorizonCoreBuilderUtils.__run_tcbuilder(
            f"isolate \
                --remote-host {host} \
                --remote-username {username} \
                --remote-password {password} \
                --changes-directory {output_dir}",
            volumes,
            progress
        )

    @staticmethod
    def unpack (workspacepath: str,
        outputpath: str,
        progress: Optional[progresscookie.ProgressCookie]) -> None:
        """Run Torizon Core unpack command."""
        volumes = [
            "deploy:/deploy",
            f"{workspacepath}:/workdir",
            "storage:/storage"
        ]

        TorizonCoreBuilderUtils.__run_tcbuilder(
            f"images \
                --remove-storage \
                unpack \
                {outputpath}",
            volumes,
            progress
        )

    @staticmethod
    def deploy (workspacepath: str,
        host: str,
        username: str,
        password: str,
        progress: Optional[progresscookie.ProgressCookie]) -> None:
        """Run Torizon Core Builder Deploy."""
        volumes = [
            "deploy:/deploy",
            f"{workspacepath}:/workdir",
            "storage:/storage"
        ]

        TorizonCoreBuilderUtils.__run_tcbuilder(
            f"deploy \
                --remote-host {host} \
                --remote-username {username} \
                --remote-password {password} \
                --reboot",
            volumes,
            progress
        )

    @staticmethod
    def publish (credentials: str,
        composefile: str,
        packagename: str,
        packageversion: str,
        progress: Optional[progresscookie.ProgressCookie]) -> None:
        """Run Torizon Core Builder Publish."""
        cmdln,vols = TorizonCoreBuilderUtils.__get_publish_args(
            credentials,
            composefile,
            packagename,
            packageversion
        )

        TorizonCoreBuilderUtils.__run_tcbuilder(
            cmdln,
            vols,
            progress
        )

    @staticmethod
    def union (branch: str,
        workspacepath:str,
        progress: Optional[progresscookie.ProgressCookie]) -> None:
        """Run Torizo Core Builder Union."""
        volumes = [
            "deploy:/deploy",
            f"{workspacepath}:/workdir",
            "storage:/storage"
        ]

        TorizonCoreBuilderUtils.__run_tcbuilder(
            f"union {branch}",
            volumes,
            progress
        )

    @staticmethod
    def push (branch: str,
        workspacepath: str,
        credentialspath: str,
        progress: Optional[progresscookie.ProgressCookie]) -> None:
        """Run Torizon Core Builder Union."""
        volumes = [
            "deploy:/deploy",
            f"{workspacepath}:/workdir",
            "storage:/storage"
        ]

        TorizonCoreBuilderUtils.__run_tcbuilder(
            f"push --credentials {credentialspath} {branch}",
            volumes,
            progress
        )

    @staticmethod
    def dt_checkout (workspacepath:str,
        progress: Optional[progresscookie.ProgressCookie]) -> None:
        """Run Torizon Core Builder dt checkout."""
        volumes = [
            "deploy:/deploy",
            f"{workspacepath}:/workdir",
            "storage:/storage"
        ]

        TorizonCoreBuilderUtils.__run_tcbuilder(
            "dt checkout",
            volumes,
            progress
        )

    @staticmethod
    def __run_tcbuilder(
        cmdline: str,
        volumes: Union[Dict[str,Dict[str,str]], list],
        progress: Optional[progresscookie.ProgressCookie]) -> None:

        dockerclient = docker.client.from_env()
        # make shure to remove deploy
        try:
            dockerclient.api.remove_volume("deploy", force=True)
        except APIError:
            # if that doesn't exist nobody care
            pass

        container = dockerclient.containers.run(
            image=":".join([
                TorizonCoreBuilderUtils.TCBUILDER_REPO,
                TorizonCoreBuilderUtils.TCBUILDER_TAG
            ]),
            command=cmdline,
            volumes=volumes,
            remove=True,
            detach=True
        )

        # new way
        TorizonCoreBuilderUtils.__process_run_stream(
            container,
            progress
        )

    @staticmethod
    def __get_publish_args(
        credentials: str,
        composefile: str,
        packagename: str,
        packageversion: str) -> Tuple[str, Dict[str,Dict[str,str]]]:

        credentialspath=os.path.dirname(credentials)
        credentialsfile=os.path.basename(credentials)
        composepath=os.path.dirname(composefile)
        composefile=os.path.basename(composefile)
        cmdline=f"push --credentials /credentials/{credentialsfile}\
            --package-name {packagename} \
            --package-version {packageversion} \
            /compose/{composefile}"

        volumes = {
            credentialspath: { "bind":"/credentials", "mode":"ro" },
            composepath: { "bind":"/compose", "mode": "ro" },
            tempfile.gettempdir() : { "bind":"/storage", "mode": "rw"}
        }
        return cmdline,volumes

    @staticmethod
    def __process_run_stream(
        container: Container,
        progress: Optional[progresscookie.ProgressCookie]) -> None:
        stream = container.logs(stream=True)

        for line in stream:
            progresscookie.progress_message(progress, line.decode())

        exit_code = container.wait()
        logging.info(f"TCB ExitCode {exit_code}")

        # throw exception
        if exit_code["StatusCode"] != 0:
            raise TorizonCoreBuilderError(exit_code["StatusCode"])
