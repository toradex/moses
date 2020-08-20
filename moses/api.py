"""Implementation of API entry points and management of global objects
"""
import json
import logging
import serial
import docker
import connexion
import pathlib
import targetdevice
import applicationconfig
import eula
import platformconfig
import config
import exceptions
import flask

APP_VERSION = "1.0"
API_VERSION = "1.0"


def remove_readonly(validator, ro, instance, schema):
    return


class CustomJSONEncoder(connexion.apps.flask_app.FlaskJSONEncoder):

    def default(self, obj):  # pylint: disable=E0202
        to_json = getattr(obj, "_to_json", None)
        if callable(to_json):
            return obj._to_json()
        return connexion.apps.flask_app.FlaskJSONEncoder.default(self, obj)


class ApiResolver(connexion.Resolver):

    def resolve(self, operation):
        """Generates a function name from an operation path

        Arguments:
            operation {connexion.operation.Operation} -- operation
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

        function += "_"+operation.method
        return connexion.Resolution(
            connexion.utils.get_function_from_name(function),
            function)


def version_get() -> dict:
    """Returns version information

    Returns:
        dict -- app_version and api_version as strings
    """

    return {"app_version": APP_VERSION,
            "api_version": API_VERSION
            }


def version_docker_get():
    """Returns docker version information

    Returns: Docker information
    """

    try:
        client = docker.from_env()

        return client.version()
    except:
        return ("Docker not responding", 500)


def devices_get():
    """Returns the list of devices

    Returns:
        dict -- devices
    """
    deviceslist = []

    for dev in targetdevice.TargetDevices().values():
        deviceslist.append(dev)

    deviceslist.sort(key=lambda x: x.name)
    return deviceslist


def devices_serial_detect_get(port, username, password):
    """Detects a serial device on the specified port

    Arguments:
        port {str} -- port name
        username {str} -- username
        password {str} -- password
    """
    devices = targetdevice.TargetDevices()

    dev = devices.add_serial_device(port, username, password)
    return (dev, 200)


def devices_network_detect_get(hostname, username, password):
    """Detects a network device

    Arguments:
        hostname {str} -- hostname or ip address
        username {str} -- username
        password {str} -- password
    """
    devices = targetdevice.TargetDevices()

    dev = devices.add_network_device(hostname, username, password)
    return (dev, 200)


def devices_device_get(device_id):
    """Returns a device given its id

    Arguments:
        device_id {str} -- device serial number

    Returns:
        targetdevice.TargetDevice -- device or 404 error
    """
    devices = targetdevice.TargetDevices()

    if device_id not in devices:
        return ("Device not found", 404)

    return devices[device_id]


def devices_device_put(device_id, device):
    """Changes device properties

    Arguments:
        device_id {str} -- device id (must exists)
        device {dict} -- device properties
    """
    devices = targetdevice.TargetDevices()

    if device_id not in devices:
        return ("Device not found", 404)

    dev = devices[device_id]

    dev.import_data(device)
    dev.save()
    return dev


def devices_device_delete(device_id):
    """Removes a device given its id

    Arguments:
        device_id {str} -- device serial number

    Returns:
        targetdevice.TargetDevice -- device or 404 error
    """
    devices = targetdevice.TargetDevices()

    if device_id not in devices:
        return (connexion.NoContent, 404)

    del devices[device_id]
    return (connexion.NoContent, 204)


def devices_device_update_get(device_id):
    """Retrieves updated device information from network
    """
    devices = targetdevice.TargetDevices()

    if device_id not in devices:
        return ("Device not found", 404)

    devices.refresh_device_info(device_id)
    return (devices[device_id], 200)


def devices_device_docker_open_get(device_id, port=0):
    devices = targetdevice.TargetDevices()

    if device_id not in devices:
        return ("Device not found", 404)

    device = devices.get(device_id)
    port = device.expose_docker(port)
    return (port, 200)


def devices_device_docker_close_get(device_id):
    devices = targetdevice.TargetDevices()

    if device_id not in devices:
        return ("Device not found", 404)

    device = devices.get(device_id)
    device.stop_exposing_docker()
    return (connexion.NoContent, 200)


def devices_device_docker_port_get(device_id):
    devices = targetdevice.TargetDevices()

    if device_id not in devices:
        return ("Device not found", 404)

    device = devices.get(device_id)
    port = device.get_docker_port()
    return (port, 200)


def devices_device_ssh_open_get(device_id, port=0):
    devices = targetdevice.TargetDevices()

    if device_id not in devices:
        return ("Device not found", 404)

    device = devices.get(device_id)
    port = device.expose_ssh(port)
    return (port, 200)


def devices_device_ssh_close_get(device_id):
    devices = targetdevice.TargetDevices()

    if device_id not in devices:
        return ("Device not found", 404)

    device = devices.get(device_id)
    device.stop_exposing_ssh()
    return (connexion.NoContent, 200)


def devices_device_ssh_port_get(device_id):
    devices = targetdevice.TargetDevices()

    if device_id not in devices:
        return ("Device not found", 404)

    device = devices.get(device_id)
    port = device.get_ssh_port()
    return (port, 200)


def devices_device_processes_get(device_id):
    devices = targetdevice.TargetDevices()

    if device_id not in devices:
        return ("Device not found", 404)

    processes = devices[device_id].get_process_list()
    processes.sort(key=lambda x: x["pid"])
    return (processes, 200)


def devices_device_memory_get(device_id):
    devices = targetdevice.TargetDevices()

    if device_id not in devices:
        return ("Device not found", 404)

    return (devices[device_id].get_memoryinfo(), 200)


def devices_device_storage_get(device_id):
    devices = targetdevice.TargetDevices()

    if device_id not in devices:
        return ("Device not found", 404)

    mountpoints = devices[device_id].get_storageinfo()
    mountpoints.sort(key=lambda x: x["mountpoint"])
    return (mountpoints, 200)


def devices_device_images_get(device_id):
    """Returns a list of the containers running on a specific device

    Arguments:
        device_id {str} -- device id
    """
    devices = targetdevice.TargetDevices()

    if device_id not in devices:
        return ("Device not found", 404)

    images = devices[device_id].get_images()
    images.sort(key=lambda x: x["RepoTags"][0] if (
        "RepoTags" in x.keys() and len(x["RepoTags"]) > 0) else "~"+x["Id"])
    return (images, 200)


def devices_device_images_image_get(device_id, image_id):
    devices = targetdevice.TargetDevices()

    if device_id not in devices:
        return ("Device not found", 404)

    image = devices[device_id].get_image(image_id)

    if image is None:
        return ("Image not found", 404)
    return (image.attrs, 200)


def devices_device_images_image_delete(device_id, image_id):
    devices = targetdevice.TargetDevices()

    if device_id not in devices:
        return ("Device not found", 404)

    device = devices.get(device_id)
    device.remove_image(image_id)
    return (connexion.NoContent, 204)


def devices_device_containers_get(device_id):
    """Returns a list of the containers running on a specific device

    Arguments:
        device_id {str} -- device id
    """
    devices = targetdevice.TargetDevices()

    if device_id not in devices:
        return ("Device not found", 404)

    containers = devices[device_id].get_containers()
    containers.sort(key=lambda x: x["Name"]
                    if ("Name" in x.keys() and x["Name"] is not None) else "~"+x["Id"])
    return (containers, 200)


def devices_device_containers_container_get(device_id, container_id):
    devices = targetdevice.TargetDevices()

    if device_id not in devices:
        return ("Device not found", 404)

    container = devices[device_id].get_container(container_id)

    if container is None:
        return ("Container not found", 404)
    return (container.attrs, 200)


def devices_device_containers_container_delete(device_id, container_id):
    devices = targetdevice.TargetDevices()

    if device_id not in devices:
        return ("Device not found", 404)

    device = devices.get(device_id)
    device.remove_container(container_id)
    return (connexion.NoContent, 204)


def devices_device_containers_container_start_get(device_id, container_id):
    devices = targetdevice.TargetDevices()

    if device_id not in devices:
        return ("Device not found", 404)

    device = devices.get(device_id)
    container = device.start_container(container_id)
    return (container.attrs, 200)


def devices_device_containers_container_stop_get(device_id, container_id):
    devices = targetdevice.TargetDevices()

    if device_id not in devices:
        return ("Device not found", 404)

    device = devices.get(device_id)
    container = device.stop_container(container_id)
    return (container.attrs, 200)


def devices_device_containers_container_processes_get(device_id, container_id):
    devices = targetdevice.TargetDevices()

    if device_id not in devices:
        return ("Device not found", 404)

    processes = devices[device_id].get_container_process_list(container_id)
    processes.sort(key=lambda x: x["pid"])
    return (processes, 200)


def devices_device_containers_container_memory_get(device_id, container_id):
    devices = targetdevice.TargetDevices()

    if device_id not in devices:
        return ("Device not found", 404)

    return (devices[device_id].get_container_memoryinfo(container_id), 200)


def devices_device_containers_container_storage_get(device_id, container_id):
    devices = targetdevice.TargetDevices()

    if device_id not in devices:
        return ("Device not found", 404)

    mountpoints = devices[device_id].get_container_storageinfo(container_id)
    mountpoints.sort(key=lambda x: x["mountpoint"])
    return (mountpoints, 200)


def devices_device_containers_container_logs_get(device_id, container_id, restart):
    devices = targetdevice.TargetDevices()

    if device_id not in devices:
        return ("Device not found", 404)

    device = devices[device_id]
    line = device.get_container_logs(container_id, restart)

    if line is None:
        return (connexion.NoContent, 204)

    return (line, 200)


def devices_device_privatekey_get(device_id):
    devices = targetdevice.TargetDevices()

    if device_id not in devices:
        return ("Device not found", 404)

    return (devices[device_id].get_privatekeypath(), 200)


def devices_device_syncfolders_get(device_id, sourcefolder, destfolder):
    """Syncs a folder on the host with one on the target device

    Arguments:
        device_id {str} -- target device
        sourcefolder {src} -- source folder
        destfolder {src} -- target folder
    """
    devices = targetdevice.TargetDevices()

    if device_id not in devices:
        return ("Device not found", 404)

    devices[device_id].sync_folders(sourcefolder, destfolder)
    return (connexion.NoContent, 200)


def devices_device_current_ip_get(device_id):
    """Syncs a folder on the host with one on the target device

    Arguments:
        device_id {str} -- target device
    """
    devices = targetdevice.TargetDevices()

    if device_id not in devices:
        return ("Device not found", 404)

    return (devices[device_id].get_current_ip(), 200)

def eulas_get():
    """Returns a list of eulas

    Returns:
        [list] -- eulas
    """

    eulas=eula.EULAs()

    eulalist=list(eulas.values())
    eulalist.sort(key=lambda x: x.title)

    return eulalist

def eulas_eula_get(eula_id):
    """Returns an eula given its id

    Arguments:
        eula_id {str} -- eula id

    Returns:
        [dict] -- eula
    """

    eulas = eula.EULAs()

    if eula_id not in eulas:
        return ("eula not found", 404)

    e = eulas.get(eula_id)
    return e

def eulas_eula_put(eula_id, e):
    """Changes device properties

    Arguments:
        eula_id {str} -- eula id (must exists)
        e {dict} -- eula properties
    """
    eulas = eula.EULAs()

    if eula_id not in eulas:
        return ("eula not found", 404)

    eulaupdated = eulas[eula_id]

    eulaupdated.import_data(e)
    eulaupdated.save()
    return eulaupdated

def platforms_get(runtime=None):
    """Returns a list of platforms

    Arguments:
        standard {bool} -- standard, if specified can be used to
                           select only standard/non-standard platforms

    Returns:
        [list] -- platforms
    """

    platforms = platformconfig.PlatformConfigs()

    platformslist = platforms.get_platforms(runtime)

    platformslist.sort(key=lambda x: x.name)
    return platformslist


def platforms_platform_get(platform_id):
    """Returns a platform given its id

    Arguments:
        platform_id {str} -- platform id

    Returns:
        [dict] -- platform
    """

    platforms = platformconfig.PlatformConfigs()

    if platform_id not in platforms:
        return ("Platform not found", 404)

    platform = platforms.get(platform_id)
    return platform


def platforms_platform_compatibledevices_get(platform_id):
    """Returns a list of devices that are compatible with the selected platform

    Arguments:
        platform_id {[type]} -- [description]

    Returns:
        [type] -- [description]
    """
    platforms = platformconfig.PlatformConfigs()

    if platform_id not in platforms:
        return ("Platform not found", 404)

    platform = platforms.get(platform_id)
    deviceslist = platform.get_compatible_devices()
    deviceslist.sort(key=lambda x: x.name)
    return deviceslist


def applications_create_get(platform_id, path, username):
    """Creates a new application

    Arguments:
        folder {string} -- Folder where application configuration must be
                           stored
    """
    applications = applicationconfig.ApplicationConfigs()
    platforms = platformconfig.PlatformConfigs()

    if platform_id not in platforms:
        return ("Platform not found", 404)

    app = applications.create_new_application(pathlib.Path(path),
                                              platforms[platform_id],
                                              username)
    return (app, 200)


def applications_load_get(path):
    """Loads an existing application

    Arguments:
        platform_id {str} -- platform id
        folder {string} -- Folder where application configuration is stored
    """
    applications = applicationconfig.ApplicationConfigs()

    return (applications.load_application(pathlib.Path(path)),
            200)


def applications_application_get(application_id):
    """Returns an application given its id

    Arguments:
        application_id {str} -- application id

    Returns:
        [dict] -- application
    """

    applications = applicationconfig.ApplicationConfigs()

    if application_id not in applications:
        return ("Application not found", 404)

    return (applications[application_id], 200)


def applications_application_put(application_id, application):
    """Changes application properties

    Arguments:
        application_id {str} -- application id (must be loaded)
        app {dict} -- application properties
    """
    apps = applicationconfig.ApplicationConfigs()

    if application_id not in apps:
        return ("Application not found", 404)

    app = apps[application_id]

    app.import_data(application)
    app.touch()
    app.save()
    return app


def applications_application_delete(application_id):
    """Changes application properties

    Arguments:
        application_id {str} -- application id (must be loaded)
        app {dict} -- application properties
    """
    apps = applicationconfig.ApplicationConfigs()

    if application_id not in apps:
        return ("Application not found", 404)

    apps[application_id].destroy()
    del apps[application_id]
    return (connexion.NoContent, 204)


def applications_application_updated_get(application_id, configuration):
    """check if container is up to date

    Arguments:
        application_id {str} -- application id
        configuration -- debug/release
    """
    applications = applicationconfig.ApplicationConfigs()

    if application_id not in applications:
        return ("Application not found", 404)

    if applications[application_id].check_image(configuration):
        return (True, 200)
    return (False, 200)


def applications_application_build_get(application_id, configuration):
    """builds the application container

    Arguments:
        application_id {str} -- application id
        configuration -- debug/release
    """
    applications = applicationconfig.ApplicationConfigs()

    if application_id not in applications:
        return ("Application not found", 404)

    applications[application_id].build_image(configuration)
    return (connexion.NoContent, 200)


def applications_application_deploy_get(application_id, configuration, deviceid):
    """deploys the application container

    Arguments:
        application_id {str} -- application
        configuration {str} -- debug/release
        deviceid {str} -- device
    """
    applications = applicationconfig.ApplicationConfigs()

    if application_id not in applications:
        return ("Application not found", 404)

    app = applications.get(application_id)

    devices = targetdevice.TargetDevices()

    if deviceid not in devices:
        return ("Device not found", 404)

    app.deploy_image(configuration, devices[deviceid])

    return (connexion.NoContent, 200)


def applications_application_run_get(application_id, configuration, deviceid):
    """runs the application container

    Arguments:
        application_id {str} -- application
        configuration {str} -- debug/release
        deviceid {str} -- device
    """
    applications = applicationconfig.ApplicationConfigs()

    if application_id not in applications:
        return ("Application not found", 404)

    app = applications.get(application_id)

    devices = targetdevice.TargetDevices()

    if deviceid not in devices:
        return ("Device not found", 404)

    container = app.run(configuration, devices[deviceid])
    return (container, 200)


def applications_application_stop_get(application_id, configuration, deviceid):
    """stops the application container

    Arguments:
        application_id {str} -- application
        configuration {str} -- debug/release
        deviceid {str} -- device
    """
    applications = applicationconfig.ApplicationConfigs()

    if application_id not in applications:
        return ("Application not found", 404)

    app = applications.get(application_id)

    devices = targetdevice.TargetDevices()

    if deviceid not in devices:
        return ("Device not found", 404)

    app.stop(configuration, devices[deviceid])
    return (connexion.NoContent, 200)


def applications_application_container_get(
        application_id, configuration, deviceid):
    """Returns app currently running container

    Arguments:
        application_id {str} -- application
        configuration {str} -- debug/release
        deviceid {str} -- device
    """
    applications = applicationconfig.ApplicationConfigs()

    if application_id not in applications:
        return ("Application not found", 404)

    app = applications.get(application_id)

    devices = targetdevice.TargetDevices()

    if deviceid not in devices:
        return ("Device not found", 404)

    configuration = app.get_container(configuration, devices[deviceid])
    return (configuration.attrs, 200)


def applications_application_container_logs_get(application_id, configuration, deviceid, restart):
    """Returns app currently running container

    Arguments:
        application_id {str} -- application
        configuration {str} -- debug/release
        deviceid {str} -- device
        restart { bool } -- read log from the beginning
    """
    applications = applicationconfig.ApplicationConfigs()

    if application_id not in applications:
        return ("Application not found", 404)

    app = applications.get(application_id)

    devices = targetdevice.TargetDevices()

    if deviceid not in devices:
        return ("Device not found", 404)

    line = app.get_container_logs(
        configuration, devices[deviceid], restart)

    if line is None:
        return (connexion.NoContent, 204)

    return (line, 200)


def applications_application_sdk_run_get(application_id, configuration, build):
    """Runs the SDK container and returns SSH address for connection

    Arguments:
        application_id {str} -- application

    Returns:
        url -- address of the SSH port on the container
    """
    applications = applicationconfig.ApplicationConfigs()

    if application_id not in applications:
        return ("Application not found", 404)

    app = applications.get(application_id)

    if build is None:
        build = True

    app.start_sdk_container(configuration, build)

    return (app.sdksshaddress, 200)


def applications_application_sdk_update_get(application_id, configuration):
    """Updates the SDK for an application

    Arguments:
        application_id {str} -- application
        configuration {str} -- debug/release
    """
    applications = applicationconfig.ApplicationConfigs()

    if application_id not in applications:
        return ("Application not found", 404)

    app = applications.get(application_id)
    app.update_sdk(configuration)
    return (connexion.NoContent, 200)


def applications_application_syncfolders_get(application_id, sourcefolder,
                                             configuration, deviceid, destfolder, source_is_sdk):
    """Sincronizes a folder between the SDK container and the target

    Arguments:
        application_id {str} -- application
        sourcefolder {str}} -- path on the SDK container
        configuration {str} -- debug/release
        deviceid {str} -- device
        destfolder {str} -- path on the target device
        source_is_sdk {bool} -- source if from SDK container

    """
    applications = applicationconfig.ApplicationConfigs()

    if application_id not in applications:
        return ("Application not found", 404)

    app = applications.get(application_id)

    if source_is_sdk is None:
        source_is_sdk = True

    app.sync_folders(sourcefolder, configuration,
                     deviceid, destfolder, source_is_sdk)
    return (connexion.NoContent, 200)


def applications_application_privatekey_get(application_id):
    applications = applicationconfig.ApplicationConfigs()

    if application_id not in applications:
        return ("Application not found", 404)

    app = applications.get(application_id)
    return (app.get_privatekeypath(), 200)


def applications_application_reseal_get(application_id):
    applications = applicationconfig.ApplicationConfigs()

    if application_id not in applications:
        return ("Application not found", 404)

    app = applications.get(application_id)
    app.reseal()
    return (connexion.NoContent, 200)


def setup_pullcontainers_get():
    """Pulls all base containers needed for the different applications

    Raises:
        exceptions.PullImageError: error during image pull
    """

    dockerclient = docker.from_env()    
    failed = []

    for p in platformconfig.PlatformConfigs():

        plat = platformconfig.PlatformConfigs()[p]

        for k, v in plat.baseimage.items():
            if v is not None:
                logging.info("PULL - Pulling container %s:%s", v[0], v[1])
                try:
                    dockerclient.images.pull(v[0], v[1])
                except:
                    logging.exception(
                        "PULL - Pull operation failed for image %s:%s.", v[0], v[1])
                    failed.append(str(v[0])+":"+str(v[1]))

        for k, v in plat.sdkbaseimage.items():
            if v is not None:
                logging.info("PULL - Pulling container %s:%s", v[0], v[1])
                try:
                    dockerclient.images.pull(v[0], v[1])
                except:
                    logging.exception(
                        "PULL - Pull operation failed for image %s:%s.", v[0], v[1])
                    failed.append(str(v[0])+":"+str(v[1]))

    if len(failed) != 0:
        raise exceptions.PullImageError(failed)


def init_api():
    """Initializes the api and allocates all required objects
    """

    config.init_config()
