"""Implementation of API entry points and management of global objects."""
import logging
import docker
import docker.models.containers
import connexion
import pathlib
import targetdevice
import applicationconfig
import eula
import platformconfig
import config
import exceptions
import progresscookie
from typing import Any, Optional, Dict, Union

APP_VERSION = "1.0"
API_VERSION = "1.0"

EMULATION_IMAGE_NAME = "torizon/binfmt"

# validation of readonly fields is done internally
def remove_readonly(validator: Any, ro: Any, instance: Any, schema: Any) -> None:
    """Skip validation of readonly fields.

    this function is required to avoid that read-only fields passed back during update
    requests will lead to errors, RO fields validation will be done later inside the
    appropriate object

    :param validator:
    :param ro:
    :param instance:
    :param schema:

    """
    return


class CustomJSONEncoder(connexion.apps.flask_app.FlaskJSONEncoder):
    """Object used to encode internal objects to json.

    this will allow the objects to return only specific fields, keep implementation fields
    hidden

    """

    def default(self, obj: Any) -> Union[str, float, Any]:
        """Serialize objects using their _to_json method, when available.

        If the object has a _to_json method, it will be used for serialization

        :param obj: object to be serialized

        """
        to_json = getattr(obj, "_to_json", None)
        if callable(to_json):
            return obj._to_json()
        return connexion.apps.flask_app.FlaskJSONEncoder.default(self, obj)


class ApiResolver(connexion.Resolver):
    """Object used to resolve url to a function inside this module."""

    def resolve(self, operation: Any) -> connexion.Resolution:
        """Generate a function name from an operation path.

        :param operation: connexion

        """
        function = "api."
        firstloop = True
        items = operation.path.split("/")
        for item in items:

            if len(item) == 0:
                continue

            # for parameters we strip the curly braces
            # and _id at the end
            if item.startswith("{"):
                item = item[1:-4]

            if firstloop:
                firstloop = False
            else:
                function += "_"

            function += item

        function += "_" + operation.method
        return connexion.Resolution(
            connexion.utils.get_function_from_name(function), function
        )


def version_get() -> Any:
    """Return version information.

    :returns: API tuple with object and return code

    """
    return ({"app_version": APP_VERSION, "api_version": API_VERSION}, 200)


def version_docker_get() -> Any:
    """Return docker version information.

    Returns: Docker information

    :returns: API tuple with object and return code

    """
    try:
        client = docker.from_env()

        return (client.version(), 200)
    except:
        return ("Docker not responding", 500)


def devices_get() -> Any:
    """Return the list of devices.

    :returns: API tuple with object and return code

    """
    deviceslist = []

    for dev in targetdevice.TargetDevices().values():
        deviceslist.append(dev)

    deviceslist.sort(key=lambda x: x.name)
    return (deviceslist, 200)


def devices_serial_detect_get(port: str, username: str, password: str) -> Any:
    """Detect a serial device on the specified port.

    :param port: serial port (COM*: on Windows, /dev/tty* on Linux)
    :type port: str
    :param username: username for setup (must be in sudoers)
    :param username: str
    :param password: password
    :param password: str

    :returns: API tuple with object and return code

    """
    devices = targetdevice.TargetDevices()

    dev = devices.add_serial_device(port, username, password)
    return (dev, 200)


def devices_network_detect_get(hostname: str, username: str, password: str) -> Any:
    """Detect a network device.

    :param hostname: hostname or ip address
    :type hostname: str
    :param username: user used for setup (must be in sudoers)
    :type username: str
    :param password: password
    :type password: str

    :returns: API tuple with object and return code

    """
    devices = targetdevice.TargetDevices()

    dev = devices.add_network_device(hostname, username, password)
    return (dev, 200)


def devices_device_get(device_id: str) -> Any:
    """Return a device given its id.

    :param device_id: device id
    :type device_id: str

    :returns: API tuple with object and return code

    """
    devices = targetdevice.TargetDevices()

    if device_id not in devices:
        return ("Device not found", 404)

    return (devices[device_id], 200)


def devices_device_put(device_id: str, device: Dict[str, Any]) -> Any:
    """Change device properties.

    :param device_id: device id
    :type device_id: str
    :param device: dictionary of device properties
    :type device: dict

    :returns: API tuple with object and return code

    """
    devices = targetdevice.TargetDevices()

    if device_id not in devices:
        return ("Device not found", 404)

    dev = devices[device_id]

    dev.import_data(device)
    dev.save()
    return (dev, 200)


def devices_device_delete(device_id: str) -> Any:
    """Remove a device given its id.

    :param device_id: device id
    :type device_id: str

    :returns: API tuple with object and return code

    """
    devices = targetdevice.TargetDevices()

    if device_id not in devices:
        return (connexion.NoContent, 404)

    del devices[device_id]
    return (connexion.NoContent, 204)


def devices_device_update_get(device_id: str) -> Any:
    """Retrieve updated device information from network.

    :param device_id: device id
    :type device_id: str

    :returns: API tuple with object and return code

    """
    devices = targetdevice.TargetDevices()

    if device_id not in devices:
        return ("Device not found", 404)

    devices.refresh_device_info(device_id)
    return (devices[device_id], 200)


def devices_device_docker_open_get(device_id: str, port: int = 0) -> Any:
    """Redirect the devices's docker interface on a local port.

    :param device_id: device id
    :type device_id: str
    :param port: int:  (Default value = 0)
    :type port: int

    :returns: API tuple with object and return code

    """
    devices = targetdevice.TargetDevices()

    if device_id not in devices:
        return ("Device not found", 404)

    device = devices[device_id]
    hostport = device.expose_docker(port)
    return (hostport, 200)


def devices_device_docker_close_get(device_id: str) -> Any:
    """Terminate docker port sharing.

    :param device_id: device id
    :type device_id: str

    :returns: API tuple with object and return code

    """
    devices = targetdevice.TargetDevices()

    if device_id not in devices:
        return ("Device not found", 404)

    device = devices[device_id]
    device.stop_exposing_docker()
    return (connexion.NoContent, 200)


def devices_device_docker_port_get(device_id: str) -> Any:
    """Return current local port where docker APIs are exposed.

    :param device_id: device id
    :type device_id: str

    :returns: API tuple with object and return code

    """
    devices = targetdevice.TargetDevices()

    if device_id not in devices:
        return ("Device not found", 404)

    device = devices[device_id]
    port = device.get_docker_port()
    return (port, 200)


def devices_device_ssh_open_get(device_id: str, port: int = 0) -> Any:
    """Open a SSH connection and tunnels it to a local port.

    :param device_id: device id
    :type device_id: str
    :param port: port (Default value = 0)
    :type port: int

    :returns: API tuple with object and return code


    """
    devices = targetdevice.TargetDevices()

    if device_id not in devices:
        return ("Device not found", 404)

    device = devices[device_id]
    port = device.expose_ssh(port)
    return (port, 200)


def devices_device_ssh_close_get(device_id: str) -> Any:
    """Terminate SSH port sharing.

    :param device_id: device id
    :type device_id: str

    :returns: API tuple with object and return code

    """
    devices = targetdevice.TargetDevices()

    if device_id not in devices:
        return ("Device not found", 404)

    device = devices[device_id]
    device.stop_exposing_ssh()
    return (connexion.NoContent, 200)


def devices_device_ssh_port_get(device_id: str) -> Any:
    """Return currently used SHH local port.

    :param device_id: device id
    :type device_id: str

    :returns: API tuple with object and return code

    """
    devices = targetdevice.TargetDevices()

    if device_id not in devices:
        return ("Device not found", 404)

    device = devices[device_id]
    port = device.get_ssh_port()
    return (port, 200)


def devices_device_processes_get(device_id: str) -> Any:
    """Return a list of the processes running on the device.

    :param device_id: device id
    :type device_id: str

    :returns: API tuple with object and return code

    """
    devices = targetdevice.TargetDevices()

    if device_id not in devices:
        return ("Device not found", 404)

    processes = devices[device_id].get_process_list()
    processes.sort(key=lambda x: x["pid"])
    return (processes, 200)


def devices_device_memory_get(device_id: str) -> Any:
    """Return information about memory usage on the device.

    :param device_id: device id
    :type device_id: str

    :returns: API tuple with object and return code

    """
    devices = targetdevice.TargetDevices()

    if device_id not in devices:
        return ("Device not found", 404)

    return (devices[device_id].get_memoryinfo(), 200)


def devices_device_storage_get(device_id: str) -> Any:
    """Return information about storage available on the device.

    :param device_id: device id
    :type device_id: str

    :returns: API tuple with object and return code

    """
    devices = targetdevice.TargetDevices()

    if device_id not in devices:
        return ("Device not found", 404)

    mountpoints = devices[device_id].get_storageinfo()
    mountpoints.sort(key=lambda x: x["mountpoint"])
    return (mountpoints, 200)


def devices_device_images_get(device_id: str) -> Any:
    """Return the list of container images currently on the device.

    :param device_id: device id
    :type device_id: str

    :returns: API tuple with object and return code

    """
    devices = targetdevice.TargetDevices()

    if device_id not in devices:
        return ("Device not found", 404)

    images = devices[device_id].get_images()
    images.sort(
        key=lambda x: x["RepoTags"][0]
        if ("RepoTags" in x.keys() and len(x["RepoTags"]) > 0)
        else "~" + x["Id"]
    )
    return (images, 200)


def devices_device_images_image_get(device_id: str, image_id: str) -> Any:
    """Return information on a specific image.

    :param device_id: device id
    :type device_id: str
    :param image_id: image ID (SHA)
    :type image_id: str

    :returns: API tuple with object and return code

    """
    devices = targetdevice.TargetDevices()

    if device_id not in devices:
        return ("Device not found", 404)

    image = devices[device_id].get_image(image_id)

    if image is None:
        return ("Image not found", 404)
    return (image.attrs, 200)


def devices_device_images_image_delete(device_id: str, image_id: str) -> Any:
    """Remove a specific image.

    :param device_id: device id
    :type device_id: str
    :param image_id: image ID (SHA)
    :type image_id: str

    :returns: API tuple with object and return code

    """
    devices = targetdevice.TargetDevices()

    if device_id not in devices:
        return ("Device not found", 404)

    device = devices[device_id]
    device.remove_image(image_id)
    return (connexion.NoContent, 204)


def devices_device_containers_get(device_id: str) -> Any:
    """Return the list of containers currently running or suspended on the device.

    :param device_id: device id
    :type device_id: str

    :returns: API tuple with object and return code

    """
    devices = targetdevice.TargetDevices()

    if device_id not in devices:
        return ("Device not found", 404)

    containers = devices[device_id].get_containers()
    containers.sort(
        key=lambda x: x["Name"]
        if ("Name" in x.keys() and x["Name"] is not None)
        else "~" + x["Id"]
    )
    return (containers, 200)


def devices_device_containers_container_get(device_id: str, container_id: str) -> Any:
    """Return information about a specific container.

    :param device_id: device id
    :type device_id: str
    :param container_id: container id (SHA)
    :type container_id: str

    :returns: API tuple with object and return code

    """
    devices = targetdevice.TargetDevices()

    if device_id not in devices:
        return ("Device not found", 404)

    container = devices[device_id].get_container(container_id)

    if container is None:
        return ("Container not found", 404)
    return (container.attrs, 200)


def devices_device_containers_container_delete(
    device_id: str, container_id: str
) -> Any:
    """Delete a specific container.

    :param device_id: device id
    :type device_id: str
    :param container_id: container id (SHA)
    :type container_id: str

    :returns: API tuple with object and return code

    """
    devices = targetdevice.TargetDevices()

    if device_id not in devices:
        return ("Device not found", 404)

    device = devices[device_id]
    device.remove_container(container_id)
    return (connexion.NoContent, 204)


def devices_device_containers_container_start_get(
    device_id: str, container_id: str
) -> Any:
    """Start a specific container.

    :param device_id: device id
    :type device_id: str
    :param container_id: container id (SHA)
    :type container_id: str

    :returns: API tuple with object and return code

    """
    devices = targetdevice.TargetDevices()

    if device_id not in devices:
        return ("Device not found", 404)

    device = devices[device_id]
    container = device.start_container(container_id)
    return (container.attrs, 200)


def devices_device_containers_container_stop_get(
    device_id: str, container_id: str
) -> Any:
    """Stop a specific container.

    :param device_id: device id
    :type device_id: str
    :param container_id: container id (SHA)
    :type container_id: str

    :returns: API tuple with object and return code

    """
    devices = targetdevice.TargetDevices()

    if device_id not in devices:
        return ("Device not found", 404)

    device = devices[device_id]
    container = device.stop_container(container_id)
    return (container.attrs, 200)


def devices_device_containers_container_processes_get(
    device_id: str, container_id: str
) -> Any:
    """Return list of processes running inside a specific container.

    :param device_id: device id
    :type device_id: str
    :param container_id: container id (SHA)
    :type container_id: str

    :returns: API tuple with object and return code

    """
    devices = targetdevice.TargetDevices()

    if device_id not in devices:
        return ("Device not found", 404)

    processes = devices[device_id].get_container_process_list(container_id)
    processes.sort(key=lambda x: x["pid"])
    return (processes, 200)


def devices_device_containers_container_memory_get(
    device_id: str, container_id: str
) -> Any:
    """Return memory information about a specific container.

    :param device_id: device id
    :type device_id: str
    :param container_id: container id (SHA)
    :type container_id: str

    :returns: API tuple with object and return code

    """
    devices = targetdevice.TargetDevices()

    if device_id not in devices:
        return ("Device not found", 404)

    return (devices[device_id].get_container_memoryinfo(container_id), 200)


def devices_device_containers_container_storage_get(
    device_id: str, container_id: str
) -> Any:
    """Return information about mountpoints and storage for a specific container.

    :param device_id: device id
    :type device_id: str
    :param container_id: container id (SHA)
    :type container_id: str

    :returns: API tuple with object and return code

    """
    devices = targetdevice.TargetDevices()

    if device_id not in devices:
        return ("Device not found", 404)

    mountpoints = devices[device_id].get_container_storageinfo(container_id)
    mountpoints.sort(key=lambda x: x["mountpoint"])
    return (mountpoints, 200)


def devices_device_containers_container_logs_get(
    device_id: str, container_id: str, restart: bool
) -> Any:
    """Return logs for a specific container (line by line).

    :param device_id: device id
    :type device_id: str
    :param container_id: container id (SHA)
    :type container_id: str

    :returns: API tuple with object and return code

    """
    devices = targetdevice.TargetDevices()

    if device_id not in devices:
        return ("Device not found", 404)

    device = devices[device_id]
    line = device.get_container_logs(container_id, restart)

    if line is None:
        return (connexion.NoContent, 204)

    return (line, 200)


def devices_device_privatekey_get(device_id: str) -> Any:
    """Return private key for SSH connection with the device.

    :param device_id: device id
    :type device_id: str

    :returns: API tuple with object and return code

    """
    devices = targetdevice.TargetDevices()

    if device_id not in devices:
        return ("Device not found", 404)

    return (devices[device_id].get_privatekeypath(), 200)


def devices_device_syncfolders_get(
    device_id: str, sourcefolder: str, destfolder: str, progress_id: str = None
) -> Any:
    """Sync a folder on the host with one on the target device.

    :param device_id: device id
    :type device_id: str
    :param sourcefolder: source folder (on local machine)
    :type sourcefolder: str
    :param destfolder: destination folder (on the device)
    :type destfolder: str
    :param progress_id: progress object ID  (Default value = None)
    :type progress_id: str

    :returns: API tuple with object and return code

    """
    cookies = progresscookie.ProgressCookies()
    progress = None

    if progress_id is not None and progress_id in cookies:
        progress = cookies[progress_id]

    try:
        devices = targetdevice.TargetDevices()

        if device_id not in devices:
            raise exceptions.ObjectNotFound("Device", device_id)

        devices[device_id].sync_folders(sourcefolder, destfolder, progress)

        if progress is not None:
            progress.completed()

        return (connexion.NoContent, 200)
    except Exception as e:
        if progress is not None:
            progress.report_error(e)
        raise e


def devices_device_current_ip_get(device_id: str) -> Any:
    """Return the device current IP address.

    :param device_id: device id
    :type device_id: str

    :returns: API tuple with object and return code

    """
    devices = targetdevice.TargetDevices()

    if device_id not in devices:
        return ("Device not found", 404)

    return (devices[device_id].get_current_ip(), 200)


def eulas_get() -> Any:
    """Return a list of eulas.

    :returns: API tuple with object and return code

    """
    eulas = eula.EULAs()

    eulalist = list(eulas.values())
    eulalist.sort(key=lambda x: x.title)

    return (eulalist, 200)


def eulas_eula_get(eula_id: str) -> Any:
    """Return information about a specific eula.

    :param eula_id: eula id
    :type eula_id: str

    :returns: API tuple with object and return code

    """
    eulas = eula.EULAs()

    if eula_id not in eulas:
        return ("eula not found", 404)

    e = eulas.get(eula_id)
    return (e, 200)


def eulas_eula_put(eula_id: str, e: Dict[str, Any]) -> Any:
    """Change eula properties.

    :param eula_id: eula id
    :type eula_id: str
    :param e: Eula properties
    :type e: dict

    :returns: API tuple with object and return code

    """
    eulas = eula.EULAs()

    if eula_id not in eulas:
        return ("eula not found", 404)

    eulaupdated = eulas[eula_id]

    eulaupdated.import_data(e)
    eulaupdated.save()
    return (eulaupdated, 200)


def platforms_get(runtime: Optional[str] = None) -> Any:
    """Return a list of platforms.

    API returns the list of all platform (when runtime is none) or platforms supporting the specified runtime

    :param runtime: runtime id or None  (Default value = None)
    :type runtime: str

    :returns: API tuple with object and return code

    """
    platforms = platformconfig.PlatformConfigs()

    platformslist = platforms.get_platforms(runtime)

    platformslist.sort(key=lambda x: x.name)
    return (platformslist, 200)


def platforms_platform_get(platform_id: str) -> Any:
    """Return a platform given its id.

    :param platform_id: platform id
    :type platform_id: str

    :returns: API tuple with object and return code

    """
    platforms = platformconfig.PlatformConfigs()

    if platform_id not in platforms:
        return ("Platform not found", 404)

    return (platforms[platform_id], 200)


def platforms_platform_compatibledevices_get(platform_id: str) -> Any:
    """Return a list of devices that are compatible with the selected platform.

    :param platform_id: platform id
    :type platform_id: str

    :returns: API tuple with object and return code

    """
    platforms = platformconfig.PlatformConfigs()

    if platform_id not in platforms:
        return ("Platform not found", 404)

    platform = platforms[platform_id]
    deviceslist = platform.get_compatible_devices()
    deviceslist.sort(key=lambda x: x.name)
    return (deviceslist, 200)


def applications_create_get(platform_id: str, path: str, username: str) -> Any:
    """Create a new application.

    :param platform_id: platform id
    :type platform_id: str
    :param path: base path for the application folder
    :type path:  str
    :param username: username to be used inside the container
    :type username: str

    :returns: API tuple with object and return code

    """
    applications = applicationconfig.ApplicationConfigs()
    platforms = platformconfig.PlatformConfigs()

    if platform_id not in platforms:
        return ("Platform not found", 404)

    app = applications.create_new_application(
        pathlib.Path(path), platforms[platform_id], username
    )
    return (app, 200)


def applications_load_get(path: str) -> Any:
    """Load an existing application.

    :param path: path of the application folder
    :type path:  str

    :returns: API tuple with object and return code

    """
    applications = applicationconfig.ApplicationConfigs()

    return (applications.load_application(pathlib.Path(path)), 200)


def applications_application_get(application_id: str) -> Any:
    """Return an application given its id.

    :param application_id: application id
    :type application_id: str

    :returns: API tuple with object and return code

    """
    applications = applicationconfig.ApplicationConfigs()

    if application_id not in applications:
        return ("Application not found", 404)

    return (applications[application_id], 200)


def applications_application_put(
    application_id: str, application: Dict[str, Any]
) -> Any:
    """Change application properties.

    :param application_id: application id
    :type application_id: str
    :param application: application properties
    :type application: dict

    :returns: API tuple with object and return code

    """
    apps = applicationconfig.ApplicationConfigs()

    if application_id not in apps:
        return ("Application not found", 404)

    app = apps[application_id]

    app.import_data(application)
    app.touch()
    app.save()
    return (app, 200)


def applications_application_delete(application_id: str) -> Any:
    """Delete a specific application.

    :param application_id: application id
    :type application_id: str
    :param application: application properties
    :type application: dict

    :returns: API tuple with object and return code

    """
    apps = applicationconfig.ApplicationConfigs()

    if application_id not in apps:
        return ("Application not found", 404)

    apps[application_id].destroy()
    del apps[application_id]
    return (connexion.NoContent, 204)


def applications_application_updated_get(
    application_id: str, configuration: str
) -> Any:
    """Delete a specific application.

    :param application_id: application id
    :type application_id: str
    :param configuration: debug/release
    :type configuration: str

    :returns: API tuple with object and return code

    """
    applications = applicationconfig.ApplicationConfigs()

    if application_id not in applications:
        return ("Application not found", 404)

    if applications[application_id].check_image(configuration):
        return (True, 200)
    return (False, 200)


def applications_application_build_get(
    application_id: str, configuration: str, progress_id: str = None
) -> Any:
    """Build the application container.

    :param application_id: application id
    :type application_id: str
    :param configuration: debug/release
    :type configuration: str
    :param progress_id: progress object id  (Default value = None)
    :type progress_id: str

    :returns: API tuple with object and return code

    """
    cookies = progresscookie.ProgressCookies()
    progress = None

    if progress_id is not None and progress_id in cookies:
        progress = cookies[progress_id]

    try:
        applications = applicationconfig.ApplicationConfigs()

        if application_id not in applications:
            raise exceptions.ObjectNotFound("Application", application_id)

        applications[application_id].build_image(configuration, progress)

        if progress is not None:
            progress.completed()

        return (connexion.NoContent, 200)
    except Exception as e:
        if progress is not None:
            progress.report_error(e)
        raise e


def applications_application_deploy_get(
    application_id: str, configuration: str, device_id: str, progress_id: str = None
) -> Any:
    """Deploy the application container.

    :param application_id: application id
    :type application_id: str
    :param configuration: debug/release
    :type configuration: str
    :param device_id: device id
    :type device_id: str
    :param progress_id: progress object id  (Default value = None)
    :type progress_id: str

    :returns: API tuple with object and return code

    """
    cookies = progresscookie.ProgressCookies()
    progress = None

    if progress_id is not None and progress_id in cookies:
        progress = cookies[progress_id]

    try:
        applications = applicationconfig.ApplicationConfigs()

        if application_id not in applications:
            return ("Application not found", 404)

        app = applications[application_id]

        devices = targetdevice.TargetDevices()

        if device_id not in devices:
            return ("Device not found", 404)

        app.deploy_image(configuration, devices[device_id], progress)

        if progress is not None:
            progress.completed()

        return (connexion.NoContent, 200)
    except Exception as e:
        if progress is not None:
            progress.report_error(e)
        raise e


def applications_application_run_get(
    application_id: str, configuration: str, device_id: str, progress_id: str = None
) -> Any:
    """Run the application container.

    :param application_id: application id
    :type application_id: str
    :param configuration: debug/release
    :type configuration: str
    :param device_id: device id
    :type device_id: str
    :param progress_id: progress object id  (Default value = None)
    :type progress_id: str

    :returns: API tuple with object and return code

    """
    cookies = progresscookie.ProgressCookies()
    progress = None

    if progress_id is not None and progress_id in cookies:
        progress = cookies[progress_id]

    try:
        applications = applicationconfig.ApplicationConfigs()

        if application_id not in applications:
            return ("Application not found", 404)

        app = applications[application_id]

        devices = targetdevice.TargetDevices()

        if device_id not in devices:
            return ("Device not found", 404)

        container = app.run(configuration, devices[device_id], progress)

        if progress is not None:
            progress.completed()

        return (container, 200)
    except Exception as e:
        if progress is not None:
            progress.report_error(e)
        raise e


def applications_application_stop_get(
    application_id: str, configuration: str, device_id: str
) -> Any:
    """Stop the application container.

    :param application_id: application id
    :type application_id: str
    :param configuration: debug/release
    :type configuration: str
    :param device_id: device id
    :type device_id: str

    :returns: API tuple with object and return code

    """
    applications = applicationconfig.ApplicationConfigs()

    if application_id not in applications:
        return ("Application not found", 404)

    app = applications[application_id]

    devices = targetdevice.TargetDevices()

    if device_id not in devices:
        return ("Device not found", 404)

    app.stop(configuration, devices[device_id])
    return (connexion.NoContent, 200)


def applications_application_container_get(
    application_id: str, configuration: str, device_id: str
) -> Any:
    """Return the application's container properties.

    :param application_id: application id
    :type application_id: str
    :param configuration: debug/release
    :type configuration: str
    :param device_id: device id
    :type device_id: str

    :returns: API tuple with object and return code

    """
    applications = applicationconfig.ApplicationConfigs()

    if application_id not in applications:
        return ("Application not found", 404)

    app = applications[application_id]

    devices = targetdevice.TargetDevices()

    if device_id not in devices:
        return ("Device not found", 404)

    cfg = app.get_container(configuration, devices[device_id])

    if cfg is None:
        return ("Container not found", 404)

    return (cfg.attrs, 200)


def applications_application_sdk_container_get(
    application_id: str, configuration: str
) -> Any:
    """Return the application's SDK container instance.

    :param application_id: application id
    :type application_id: str
    :param configuration: debug/release
    :type configuration: str

    :returns: API tuple with object and return code

    """
    applications = applicationconfig.ApplicationConfigs()

    if application_id not in applications:
        return ("Application not found", 404)

    app = applications[application_id]
    cfg = app.get_sdk_container(configuration)

    if cfg is None:
        return (connexion.NoContent, 204)

    return (cfg.attrs, 200)


def applications_application_container_logs_get(
    application_id: str, configuration: str, device_id: str, restart: bool
) -> Any:
    """Return one line from the container's log.

    :param application_id: application id
    :type application_id: str
    :param configuration: debug/release
    :type configuration: str
    :param device_id: device id
    :type device_id: str
    :param restart: when true force the operation to return logs from the first one
    :type restart: bool

    :returns: API tuple with object and return code
    """
    applications = applicationconfig.ApplicationConfigs()

    if application_id not in applications:
        return ("Application not found", 404)

    app = applications[application_id]

    devices = targetdevice.TargetDevices()

    if device_id not in devices:
        return ("Device not found", 404)

    line = app.get_container_logs(configuration, devices[device_id], restart)

    if line is None:
        return (connexion.NoContent, 204)

    return (line, 200)


def applications_application_docker_commandline_get(
    application_id: str, configuration: str
) -> Any:
    """Return docker command line for the application's container.

    :param application_id: application id
    :type application_id: str
    :param configuration: debug/release
    :type configuration: str

    :returns: API tuple with object and return code

    """
    applications = applicationconfig.ApplicationConfigs()

    if application_id not in applications:
        return ("Application not found", 404)

    app = applications.get(application_id)

    assert app is not None

    return (app.get_docker_commandline(configuration), 200)


def applications_application_docker_composefile_get(
    application_id: str, configuration: str
) -> Any:
    """Return docker-compose YAML for the application's container.

    :param application_id: application id
    :type application_id: str
    :param configuration: debug/release
    :type configuration: str

    :returns: API tuple with object and return code

    """
    applications = applicationconfig.ApplicationConfigs()

    if application_id not in applications:
        return ("Application not found", 404)

    app = applications.get(application_id)

    assert app is not None

    return (app.get_docker_composefile(configuration), 200)


def applications_application_push_to_registry_get(
    application_id: str,
    configuration: str,
    username: str,
    password: str,
    progress_id: str = None,
) -> Any:
    """Push application's container to docker registry.

    :param application_id: application id
    :type application_id: str
    :param configuration: debug/release
    :type configuration: str
    :param username: username for docker login
    :type username: str
    :param password: password for docker login
    :type password: str
    :param progress_id: progress object id  (Default value = None)
    :type progress_id: str

    :returns: API tuple with object and return code

    """
    cookies = progresscookie.ProgressCookies()
    progress = None

    if progress_id is not None and progress_id in cookies:
        progress = cookies[progress_id]

    try:
        applications = applicationconfig.ApplicationConfigs()

        if application_id not in applications:
            return ("Application not found", 404)

        app = applications[application_id]

        app.push_to_registry(configuration, username, password, progress)

        if progress is not None:
            progress.completed()

        return (connexion.NoContent, 200)
    except Exception as e:
        if progress is not None:
            progress.report_error(e)
        raise e


def applications_application_sdk_run_get(
    application_id: str, configuration: str, build: bool, progress_id: str = None
) -> Any:
    """Run the SDK container and return SSH address for connection.

    :param application_id: application id
    :type application_id: str
    :param configuration: debug/release
    :type configuration: str
    :param build: if true and SDK container does not exist, it will be built
    :type build: boolean
    :param progress_id: progress object id  (Default value = None)
    :type progress_id: str

    :returns: API tuple with object and return code

    """
    cookies = progresscookie.ProgressCookies()
    progress = None

    if progress_id is not None and progress_id in cookies:
        progress = cookies[progress_id]

    try:
        applications = applicationconfig.ApplicationConfigs()

        if application_id not in applications:
            raise exceptions.ObjectNotFound("Application", application_id)

        app = applications[application_id]

        if build is None:
            build = True

        cookies = progresscookie.ProgressCookies()
        progress = None

        if progress_id is not None and progress_id in cookies:
            progress = cookies[progress_id]

        app.start_sdk_container(configuration, build, progress)

        if progress is not None:
            progress.completed()

        return (app.sdksshaddress, 200)
    except Exception as e:
        if progress is not None:
            progress.report_error(e)
        raise e


def applications_application_sdk_update_get(
    application_id: str, configuration: str, progress_id: str = None
) -> Any:
    """Update/build the SDK for an application.

    :param application_id: application id
    :type application_id: str
    :param configuration: debug/release
    :type configuration: str
    :param progress_id: progress object id  (Default value = None)
    :type progress_id: str

    :returns: API tuple with object and return code

    """
    cookies = progresscookie.ProgressCookies()
    progress = None

    if progress_id is not None and progress_id in cookies:
        progress = cookies[progress_id]

    try:
        applications = applicationconfig.ApplicationConfigs()

        if application_id not in applications:
            raise exceptions.ObjectNotFound("Application", application_id)

        cookies = progresscookie.ProgressCookies()
        progress = None

        if progress_id is not None and progress_id in cookies:
            progress = cookies[progress_id]

        app = applications[application_id]
        app.update_sdk(configuration, progress)

        if progress is not None:
            progress.completed()

        return (connexion.NoContent, 200)
    except Exception as e:
        if progress is not None:
            progress.report_error(e)
        raise e


def applications_application_syncfolders_get(
    application_id: str,
    sourcefolder: str,
    configuration: str,
    device_id: str,
    destfolder: str,
    source_is_sdk: bool,
    progress_id: str = None,
) -> Any:
    """Syncronize a folder between the SDK container and the target.

    :param application_id: application id
    :type application_id: str
    :param sourcefolder: source folder (on local machine or inside SDK container)
    :type sourcefolder: str
    :param configuration: debug/release
    :type configuration: str
    :param device_id: device id
    :type device_id: str
    :param destfolder: destination folder (on device)
    :type destfolder: str
    :param source_is_sdk: if true the source path will be inside the SDK container
    :type source_is_sdk: bool
    :param progress_id: progress object id  (Default value = None)
    :type progress_id: str

    :returns: API tuple with object and return code

    """
    cookies = progresscookie.ProgressCookies()
    progress = None

    if progress_id is not None and progress_id in cookies:
        progress = cookies[progress_id]

    try:
        applications = applicationconfig.ApplicationConfigs()

        if application_id not in applications:
            raise exceptions.ObjectNotFound("Application", application_id)

        app = applications[application_id]

        if source_is_sdk is None:
            source_is_sdk = True

        app.sync_folders(
            sourcefolder, configuration, device_id, destfolder, source_is_sdk, progress
        )

        if progress is not None:
            progress.completed()

        return (connexion.NoContent, 200)
    except Exception as e:
        if progress is not None:
            progress.report_error(e)
        raise e


def applications_application_privatekey_get(application_id: str) -> Any:
    """Return the application's private key.

    :param application_id: application id
    :type application_id: str

    :returns: API tuple with object and return code

    """
    applications = applicationconfig.ApplicationConfigs()

    if application_id not in applications:
        return ("Application not found", 404)

    app = applications[application_id]
    return (app.get_privatekeypath(), 200)


def applications_application_reseal_get(application_id: str) -> Any:
    """Clean all the IDs/keys from application.

    :param application_id: application id
    :type application_id: str

    :returns: API tuple with object and return code

    """
    applications = applicationconfig.ApplicationConfigs()

    if application_id not in applications:
        return ("Application not found", 404)

    app = applications[application_id]
    app.reseal()
    return (connexion.NoContent, 200)


def setup_pullcontainers_get(progress_id: str = None) -> Any:
    """Pull all base containers needed for the different applications.

    :param progress_id: progress object id  (Default value = None)
    :type progress_id: str

    :returns: API tuple with object and return code

    """
    progress: Optional[progresscookie.ProgressCookie] = None

    try:
        cookies = progresscookie.ProgressCookies()

        if progress_id is not None and progress_id in cookies:
            progress = cookies[progress_id]

        dockerclient = docker.from_env()
        failed = []

        counter = 0
        max = len(platformconfig.PlatformConfigs()) + 1

        try:
            if progress is not None:
                progress.append_message(f"Downloading {EMULATION_IMAGE_NAME}")

            dockerclient.images.pull(EMULATION_IMAGE_NAME)
        except:
            logging.exception(
                f"PULL - Pull operation failed for image {EMULATION_IMAGE_NAME}"
            )
            failed.append(EMULATION_IMAGE_NAME)

        counter = 1

        for p in platformconfig.PlatformConfigs():

            plat = platformconfig.PlatformConfigs()[p]

            if progress is not None:
                progress.set_progress(int(counter * 100 / max))
                counter += 1

            for k, v in plat.baseimage.items():
                if v is not None:
                    logging.info("PULL - Pulling container %s:%s", v[0], v[1])
                    try:
                        if progress is not None:
                            progress.append_message(f"Downloading {v[0]}:{v[1]}")

                        if plat.architecture is not None and plat.architecture != "":
                            dockerclient.images.pull(
                                v[0], v[1], platform=plat.architecture
                            )
                        else:
                            dockerclient.images.pull(v[0], v[1])
                    except:
                        logging.exception(
                            "PULL - Pull operation failed for image %s:%s.", v[0], v[1]
                        )
                        failed.append(str(v[0]) + ":" + str(v[1]))

            for k, v in plat.sdkbaseimage.items():
                if v is not None:
                    logging.info("PULL - Pulling container %s:%s", v[0], v[1])
                    try:
                        if progress is not None:
                            progress.append_message(f"Downloading {v[0]}:{v[1]}")

                        if plat.architecture is not None and plat.architecture != "":
                            dockerclient.images.pull(
                                v[0], v[1], platform=plat.architecture
                            )
                        else:
                            dockerclient.images.pull(v[0], v[1])
                    except:
                        logging.exception(
                            "PULL - Pull operation failed for image %s:%s.", v[0], v[1]
                        )
                        failed.append(str(v[0]) + ":" + str(v[1]))

        if len(failed) != 0:
            raise exceptions.PullImageError(failed)

        if progress is not None:
            progress.set_progress(100)
            progress.completed()

    except Exception as ex:
        if progress is not None:
            progress.report_error(ex)
        raise ex

    return (connexion.NoContent, 200)


def setup_enableemulation_get(progress_id: str = None) -> Any:
    """Enable ARM emulation by running a privileged container.

    :param progress_id: progress object id  (Default value = None)
    :type progress_id: str

    :returns: API tuple with object and return code

    """
    progress: Optional[progresscookie.ProgressCookie] = None

    try:
        cookies = progresscookie.ProgressCookies()

        if progress_id is not None and progress_id in cookies:
            progress = cookies[progress_id]

        dockerclient = docker.from_env()

        output = dockerclient.containers.run(
            EMULATION_IMAGE_NAME, remove=True, privileged=True, stderr=True, stdout=True
        )

        if progress is not None:
            outputstr = output.decode("utf-8")

            for l in outputstr.split("\n"):
                progress.append_message(l)

            progress.completed()

    except Exception as ex:
        if progress is not None:
            progress.report_error(ex)
        raise ex

    return (connexion.NoContent, 200)


def progress_create_get() -> Any:
    """Create a new progress object.

    :returns: API tuple with object and return code

    """
    cookies = progresscookie.ProgressCookies()
    cookie = cookies.create_cookie()

    progress_data = cookies.get_update(cookie.id, False)

    return (progress_data, 200)


def progress_delete_get(progress_id: str = "") -> Any:
    """Destroy a progress object.

    :param progress_id: progress object id  (Default value = "")
    :type progress_id: str

    :returns: API tuple with object and return code

    """
    cookies = progresscookie.ProgressCookies()

    cookies.delete_cookie(progress_id)

    return (connexion.NoContent, 200)


def progress_status_get(progress_id: str = "") -> Any:
    """Return a progress object.

    :param progress_id: progress object id  (Default value = "")
    :type progress_id: str

    :returns: API tuple with object and return code

    """
    cookies = progresscookie.ProgressCookies()
    progress_data = cookies.get_update(progress_id, True)

    if progress_data is None:
        return (connexion.NoContent, 404)

    return (progress_data, 200)


def init_api() -> None:
    """Initialize the api and allocates all required objects."""
    config.ServerConfig()
