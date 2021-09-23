"""Utils for use Torizon Core Builder."""
from typing import Dict, Optional, Tuple
from types import SimpleNamespace
import os
import tempfile
import docker
import dockerapi
import progresscookie
from moses_exceptions import LocalCommandError

# pylint: disable=too-few-public-methods
class TorizonCoreBuilderUtils:
    """Class with static methods for run Torizon Core Builder commands."""

    TCBUILDER_REPO = "torizon/torizoncore-builder"
    TCBUILDER_TAG = "3.1"

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
    def __run_tcbuilder(
        cmdline: str,
        volumes: Dict[str,Dict[str,str]],
        progress: Optional[progresscookie.ProgressCookie]) -> None:

        dockerclient = docker.client.from_env()
        dockerapi.pull_image(
            dockerclient,
            TorizonCoreBuilderUtils.TCBUILDER_REPO,
            TorizonCoreBuilderUtils.TCBUILDER_TAG,
            progress
        )

        container = dockerclient.containers.run(
            ":".join([
                TorizonCoreBuilderUtils.TCBUILDER_REPO,
                TorizonCoreBuilderUtils.TCBUILDER_TAG
            ]),
            command=cmdline,
            volumes=volumes,
            remove=True,
            detach=True
        )

        retcode = container.wait()

        if retcode["StatusCode"] != 0:
            raise LocalCommandError(
                SimpleNamespace(
                    args=cmdline,
                    returncode=retcode["StatusCode"],
                    stderr=container.logs()
                )
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
