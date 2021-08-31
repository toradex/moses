"""Implementation of OTA-related features."""
import os
import tempfile
from types import SimpleNamespace
from typing import Optional, Any, List, Tuple, Dict
import yaml
import docker
import dockerapi
from applicationconfig_base import ApplicationConfigBase
import applicationconfig_dockerexport
from moses_exceptions import InternalServerError, \
    InvalidOrMissingParameterError, \
    InvalidPathError, \
    ImageNotFoundError, LocalCommandError
import platformconfig
import progresscookie

TCBUILDER_REPO = "torizon/torizoncore-builder"
TCBUILDER_TAG = "3.1"

def publish(
    self: ApplicationConfigBase,
    credentials: str,
    dockeruser: str,
    dockerpass: str,
    progress: Optional[progresscookie.ProgressCookie]) -> bool:
    """Publish a new version on the OTA server.

    The function:
    - generates a docker-compose file
    - pushes release image to repo
    - replaces tags with SHA-IDs in docker-compose file
    - checks that all images are available on public repos
    - creates an update and uploads it to the server
    Args:
        credentials (str): The credentials to use for the publish.

    Returns:
        bool: True if the publish was successful, otherwise False.
    """
    # this function will be part of ApplicationConfig via import
    # members of base class ApplicationConfigBase are accessed
    # pylint: disable=protected-access
    if not self.otapackagename:
        raise InvalidOrMissingParameterError("otapackagename")
    if not self.otapackageversion:
        raise InvalidOrMissingParameterError("otapackagename")

    if credentials and not os.path.exists(credentials):
        raise InvalidPathError(credentials)

    if not self.images["release"]:
        raise ImageNotFoundError("")

    platform = platformconfig.PlatformConfigs().get_platform(self.platformid)
    dockerplatform = platform.architecture

    progresscookie.progress_message(progress,"Generating docker-compose base file...")

    composefile = applicationconfig_dockerexport.get_docker_composefile(self,"release")

    if not composefile:
        raise InternalServerError("Error generating docker-compose file.")

    composeyaml=yaml.load(composefile)

    dockerclient = docker.client.from_env()

    progresscookie.progress_message(progress,"Pushing release container to docker registry...")

    applicationconfig_dockerexport.push_to_registry(self,"release",dockeruser,dockerpass,progress)

    progresscookie.progress_message(progress,"Fixing image IDs in compose file...")

    images = _replace_image_tags(composeyaml, dockerclient, dockerplatform, progress)

    progresscookie.progress_message(progress,"Checking that images are accessible...")

    _check_images_on_registry(images, dockerclient, dockerplatform, progress)

    progresscookie.progress_message(progress,"Generating OTA-compatible docker-compose file...")

    composepath = os.path.join(self._get_work_folder(),"docker-compose.ota.yaml")

    with open(composepath,"w") as composeoutputfile:
        yaml.dump(composeyaml, composeoutputfile)

    progresscookie.progress_message(progress,"Pushing new package to OTA server...")

    _run_tcbuilder(self, dockerclient, credentials, composepath, progress)

    return True

def _run_tcbuilder(
    self: ApplicationConfigBase,
    dockerclient: docker.DockerClient,
    credentials: str,
    composepath: str,
    progress: Optional[progresscookie.ProgressCookie]) -> None:
    dockerapi.pull_image(dockerclient,TCBUILDER_REPO,TCBUILDER_TAG,progress)

    cmdline,volumes = _get_tcbuilder_args(
        credentials, composepath, self.otapackagename, self.otapackageversion)

    container = dockerclient.containers.run(
        ":".join([TCBUILDER_REPO,TCBUILDER_TAG]),
        command=cmdline,volumes=volumes,remove=True, detach=True)

    retcode = container.wait()

    if retcode["StatusCode"] != 0:
        raise LocalCommandError(
            SimpleNamespace(args=cmdline,returncode=retcode["StatusCode"],stderr=container.logs()))

def _get_tcbuilder_args(
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


def _check_images_on_registry(
    images: List,
    dockerclient: docker.DockerClient,
    dockerplatform:str,
    progress: Optional[progresscookie.ProgressCookie]) -> None :
    for image in images:
        dockerapi.pull_image(
            dockerclient,image,None,progress,dockerplatform)

def _replace_image_tags(
    composeyaml: Any,
    dockerclient:docker.DockerClient,
    dockerplatform:str,
    progress: Optional[progresscookie.ProgressCookie]) -> List:
    if not "services" in composeyaml:
        raise InternalServerError("No services are defined in docker-compose file.")

    images = []

    for service in composeyaml["services"].values():
        if not "image" in service:
            raise InternalServerError("Services must provide an image name.")

        imagename = service["image"]

        if imagename.startswith("sha256:"):
            raise InvalidOrMissingParameterError("image can't be referenced by sha256 only.")
        if "@" in imagename:
            reponame=imagename.split("@")[:-1]
            imageid=imagename.split("@")[-1]
        else:
            if ":" in imagename:
                reponame = ":".join(imagename.split(":")[0:-1])
                tag = imagename.split(":")[-1]
            else:
                reponame = imagename
                tag = "latest"
            try:
                image = dockerclient.images.get(imagename)
            except docker.errors.ImageNotFound:
                dockerapi.pull_image(dockerclient,reponame,tag, progress, dockerplatform)
                image = dockerclient.images.get(imagename)

            imageid = image.attrs["RepoDigests"][0]

        images.append(imageid)
        service["image"]=imageid
    return images
