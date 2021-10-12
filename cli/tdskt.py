#!python3

import sys
import os
import logging
import argparse
import tabulate
import json
import threading
import signal
import yaml
import moses_client.api.applications_api
import moses_client.api.devices_api
import moses_client.api.eulas_api
import moses_client.api.platforms_api
import moses_client.api.progress_api
import moses_client.api.setup_api
import moses_client.api.version_api
import moses_client.models

from typing import Optional

api_client = moses_client.ApiClient()

def progress_function(api, progress_id):

    while True:
        progress = api.progress_status(progress_id=progress_id)

        for msg in progress.messages:
            print(msg)

        if progress.progress != -1:
            print(f"{progress.progress}%")

        if progress.pending == False:
            break

    if progress.result.code >= 200 and progress.result.code <= 299:
        print("operation completed successfully")
    else:
        if not progress.result.message is None:
            print(progress.result.message)

        if not progress.result.description is None:
            print(progress.result.description)

    api.progress_delete(progress_id=progress_id)


progress = None


def handle_progress(args) -> Optional[str]:

    global progress

    if not args.progress:
        return ""

    api = moses_client.api.progress_api.ProgressApi(api_client)
    progress = api.progress_create()

    thread = threading.Thread(
        target=progress_function, args=(
            api, progress.id))

    thread.start()

    return progress.id

def generate_dict_list(obj: dict) -> list:
    """Converts a dictionary into a table

    Arguments:
        obj -- dictionary to dump

    Returns:
        list -- list of name-value sub-elements
    """
    l = []

    for key, value in obj.items():
        l.append([key, value])

    return l


def generate_prop_list(obj) -> list:
    """Convers an object from moses API into table

    Arguments:
        obj -- object to dump, must have attribute_map

    Returns:
        list -- list of name-value sub-elements
    """
    l = []

    for k in obj.attribute_map:
        value = getattr(obj, k)

        if isinstance(value, list):

            newvalue = ""

            for v in value:
                try:
                    if getattr(value, "attribute_map") is not None:
                        v = tabulate.tabulate(
                            generate_prop_list(value), tablefmt="plain"
                        )
                except BaseException:
                    pass

                newvalue += str(v) + "\n"

            value = newvalue
        elif isinstance(value, dict):
            value = tabulate.tabulate(
                [[k, v] for k, v in value.items()], tablefmt="plain"
            )
        else:
            try:
                if getattr(value, "attribute_map") is not None:
                    value = tabulate.tabulate(
                        generate_prop_list(value), tablefmt="plain"
                    )
            except BaseException:
                pass

        l.append([k, value])

    return l


def generate_eula_list_item(e: moses_client.models.Eula) -> dict:
    """Convert eula into dump table row

    Arguments:
        p {moses_client.models.Eula} -- object from the API

    Returns:
        dict -- name-value dict
    """
    item = dict()

    item["Id"] = e.id
    item["Title"] = e.title
    item["Accepted"] = e.accepted
    item["Visualized"] = e.visualized
    return item


def cmd_handler_eulas(args) -> int:
    """Dump out a list of all EULAs

    Arguments:
        args -- parsed command line arguments

    Returns:
        int -- 0 for success
    """
    api = moses_client.api.eulas_api.EulasApi(api_client)
    eulas = api.eulas_get()
    eulalist = map(generate_eula_list_item, eulas)
    logging.info(tabulate.tabulate(eulalist, headers="keys", tablefmt="plain"))
    return 0

def cmd_handler_eula_info(args) -> int:
    """Dump information about a specific platform, given its id

    Arguments:
        args -- parsed command line arguments

    Returns:
        int -- 0 for success
    """
    api = moses_client.api.eulas_api.EulasApi(api_client)
    eula = api.eula_get(args.eula_id)
    logging.info(
        tabulate.tabulate(
            generate_prop_list(eula),
            headers=["Property", "Value"],
            tablefmt="plain",
        )
    )
    return 0

def cmd_handler_eula_setprop(args) -> int:
    """Change Eula's property

    Arguments:
        args {[type]} -- command line arguments

    Returns:
        int -- 0 for success
    """
    api = moses_client.api.eulas_api.EulasApi(api_client)
    eula = api.eula_get(args.eula_id)

    setattr(eula,args.property,yaml.full_load(args.value))
    api.eula_modify(args.eula_id,e=eula)
    return 0


def generate_platform_list_item(p: moses_client.models.Platform) -> dict:
    """Convert platform into dump table row

    Arguments:
        p {moses_client.models.Platform} -- object from the API

    Returns:
        dict -- name-value dict
    """
    item = dict()

    item["Id"] = p.id
    item["Name"] = p.name
    item["Version"] = p.version
    item["Custom"] = p.standard
    return item


def cmd_handler_platforms(args) -> int:
    """Dump out a list of supported platforms

    Arguments:
        args -- parsed command line arguments

    Returns:
        int -- 0 for success
    """
    api = moses_client.api.platforms_api.PlatformsApi(api_client)
    platforms = api.platforms_get()
    platlist = map(generate_platform_list_item, platforms)
    logging.info(tabulate.tabulate(platlist, headers="keys", tablefmt="plain"))
    return 0


def cmd_handler_platform_info(args) -> int:
    """Dump information about a specific platform, given its id

    Arguments:
        args -- parsed command line arguments

    Returns:
        int -- 0 for success
    """
    api = moses_client.api.platforms_api.PlatformsApi(api_client)
    platform = api.platform_get(args.platform_id)
    logging.info(
        tabulate.tabulate(
            generate_prop_list(platform),
            headers=["Property", "Value"],
            tablefmt="plain",
        )
    )
    return 0


def cmd_handler_platform_compatible(args) -> int:
    """Dump a list of devices that are compatible with this platforms

    Arguments:
        args -- parsed command line arguments

    Returns:
        int -- 0 for success
    """
    api = moses_client.api.platforms_api.PlatformsApi(api_client)
    devices = api.platform_compatibledevices_get(args.platform_id)
    deviceslist = map(generate_device_list_item, devices)
    logging.info(
        tabulate.tabulate(
            deviceslist,
            headers="keys",
            tablefmt="plain"))
    return 0


def generate_device_list_item(d: moses_client.models.TargetDevice) -> dict:
    """Convert device into dump table row

    Arguments:
        p {moses_client.models.TargetDevice} -- object from the API

    Returns:
        dict -- name-value dict
    """
    item = dict()

    item["Id"] = d.id
    item["Name"] = d.name
    item["Model"] = d.model
    item["HW release"] = d.hwrev
    return item


def cmd_handler_devices(args) -> int:
    """Dumps out a list of configured devices

    Arguments:
        args -- parsed command line arguments

    Returns:
        int -- 0 for success
    """
    api = moses_client.api.devices_api.DevicesApi(api_client)
    devices = api.devices_get()
    deviceslist = map(generate_device_list_item, devices)
    logging.info(
        tabulate.tabulate(
            deviceslist,
            headers="keys",
            tablefmt="plain"))
    return 0


def cmd_handler_device_info(args) -> int:
    """Dump information about a specific platform, given its id

    Arguments:
        args -- parsed command line arguments

    Returns:
        int -- 0 for success
    """
    api = moses_client.api.devices_api.DevicesApi(api_client)
    device = api.device_get(args.device_id)
    logging.info(
        tabulate.tabulate(
            generate_prop_list(device), headers=["Property", "Value"], tablefmt="plain"
        )
    )
    return 0


def cmd_handler_device_delete(args) -> int:
    """Dump information about a specific platform, given its id

    Arguments:
        args -- parsed command line arguments

    Returns:
        int -- 0 for success
    """
    api = moses_client.api.devices_api.DevicesApi(api_client)
    device = api.device_delete(args.device_id)
    logging.info("Device %s has been successfully deleted.", args.device_id)
    return 0


def cmd_handler_device_mem(args) -> int:
    """Returns information about memory usage on the host OS

    Arguments:
        args -- parsed command line arguments

    Returns:
        int -- 0 for success
    """
    api = moses_client.api.devices_api.DevicesApi(api_client)
    meminfo = api.device_getmemory(args.device_id)
    logging.info(
        tabulate.tabulate(
            generate_prop_list(meminfo), headers=["Property", "Value"], tablefmt="plain"
        )
    )
    return 0


def generate_mountpoint_list_item(m: moses_client.models.MountPoint) -> dict:
    """Convert image into dump table row

    Arguments:
        p {moses_client.models.TargetDevice} -- object from the API

    Returns:
        dict -- name-value dict
    """
    item = dict()

    item["Mount poinf"] = m.mountpoint
    item["FS"] = m.filesystem
    item["Size"] = m.size
    item["Available"] = m.available
    return item


def cmd_handler_device_storage(args) -> int:
    """Returns information about mountpoints on the host OS

    Arguments:
        args -- parsed command line arguments

    Returns:
        int -- 0 for success
    """
    api = moses_client.api.devices_api.DevicesApi(api_client)
    mountpoints = api.device_getmountpoints(args.device_id)
    mountpointslist = map(generate_mountpoint_list_item, mountpoints)
    logging.info(
        tabulate.tabulate(
            mountpointslist,
            headers="keys",
            tablefmt="plain"))
    return 0


def generate_process_list_item(p: moses_client.models.Process) -> dict:
    """Convert image into dump table row

    Arguments:
        p {moses_client.models.TargetDevice} -- object from the API

    Returns:
        dict -- name-value dict
    """
    item = dict()

    item["PID"] = p.pid
    item["PPID"] = p.ppid
    item["User"] = p.user
    item["Time"] = p.time
    item["Nice"] = p.nice
    item["State"] = p.state
    item["Args"] = p.args
    return item


def cmd_handler_device_ps(args) -> int:
    """Dumps a list of the processes currently running on the host

    Arguments:
        args -- parsed command line arguments

    Returns:
        int -- 0 for success
    """
    api = moses_client.api.devices_api.DevicesApi(api_client)
    processes = api.device_getprocesses(args.device_id)
    processeslist = map(generate_process_list_item, processes)
    logging.info(
        tabulate.tabulate(
            processeslist,
            headers="keys",
            tablefmt="plain"))
    return 0


def generate_image_list_item(i: moses_client.models.DockerImage) -> dict:
    """Convert image into dump table row

    Arguments:
        p {moses_client.models.TargetDevice} -- object from the API

    Returns:
        dict -- name-value dict
    """
    item = dict()

    item["Id"] = i.id
    item["Tags"] = i.repo_tags
    item["Created"] = i.created
    return item


def cmd_handler_device_images(args) -> int:
    """Dump a list of images on the target device

    Arguments:
        args -- parsed command line arguments

    Returns:
        int -- 0 for success
    """
    api = moses_client.api.devices_api.DevicesApi(api_client)
    images = api.device_getimages(args.device_id)
    imageslist = map(generate_image_list_item, images)
    logging.info(
        tabulate.tabulate(
            imageslist,
            headers="keys",
            tablefmt="plain"))
    return 0


def cmd_handler_device_image_info(args) -> int:
    """Dump information about a specific image, given its id

    Arguments:
        args -- parsed command line arguments

    Returns:
        int -- 0 for success
    """
    api = moses_client.api.devices_api.DevicesApi(api_client)
    image = api.images_getimage(args.device_id, args.image_id)
    logging.info(
        tabulate.tabulate(
            generate_prop_list(image), headers=["Property", "Value"], tablefmt="plain"
        )
    )
    return 0


def cmd_handler_device_image_delete(args) -> int:
    """Delete an image given its ID

    Arguments:
        args -- parsed command line arguments

    Returns:
        int -- 0 for success
    """
    api = moses_client.api.devices_api.DevicesApi(api_client)
    api.images_deleteimage(args.device_id, args.image_id)
    logging.info("Image %s has been successfully deleted.", args.image_id)
    return 0


def generate_container_list_item(
        c: moses_client.models.DockerContainer) -> dict:
    """Convert image into dump table row
    """
    item = dict()

    item["Id"] = c.id
    item["Name"] = c.name
    item["State"] = c.state
    return item


def cmd_handler_device_containers(args) -> int:
    """Dump a list of images on the target device

    Arguments:
        args -- parsed command line arguments

    Returns:
        int -- 0 for success
    """
    api = moses_client.api.devices_api.DevicesApi(api_client)
    containers = api.device_getcontainers(args.device_id)
    containerslist = map(generate_container_list_item, containers)
    logging.info(
        tabulate.tabulate(
            containerslist,
            headers="keys",
            tablefmt="plain"))
    return 0


def cmd_handler_device_container_info(args) -> int:
    """Dump information about a specific container, given its id

    Arguments:
        args -- parsed command line arguments

    Returns:
        int -- 0 for success
    """
    api = moses_client.api.devices_api.DevicesApi(api_client)
    container = api.containers_getcontainer(args.device_id, args.container_id)
    logging.info(
        tabulate.tabulate(
            generate_prop_list(container),
            headers=["Property", "Value"],
            tablefmt="plain",
        )
    )
    return 0


def cmd_handler_device_container_delete(args) -> int:
    """Delete a container given its ID

    Arguments:
        args -- parsed command line arguments

    Returns:
        int -- 0 for success
    """
    api = moses_client.api.devices_api.DevicesApi(api_client)
    api.containers_deletecontainer(args.device_id, args.container_id)
    logging.info(
        "Container %s has been successfully deleted.",
        args.container_id)
    return 0


def cmd_handler_device_container_start(args) -> int:
    """Starts a container given its ID

    Arguments:
        args -- parsed command line arguments

    Returns:
        int -- 0 for success
    """
    api = moses_client.api.devices_api.DevicesApi(api_client)
    api.container_start(args.device_id, args.container_id)
    logging.info(
        "Container %s has been successfully started.",
        args.container_id)
    return 0


def cmd_handler_device_container_stop(args) -> int:
    """Stops a container given its ID

    Arguments:
        args -- parsed command line arguments

    Returns:
        int -- 0 for success
    """
    api = moses_client.api.devices_api.DevicesApi(api_client)
    api.container_stop(args.device_id, args.container_id)
    logging.info(
        "Container %s has been successfully stopped.",
        args.container_id)
    return 0


def cmd_handler_device_container_mem(args) -> int:
    """Returns information about memory usage of a specific container

    Arguments:
        args -- parsed command line arguments

    Returns:
        int -- 0 for success
    """
    api = moses_client.api.devices_api.DevicesApi(api_client)
    meminfo = api.container_getmemory(args.device_id, args.container_id)
    logging.info(
        tabulate.tabulate(
            generate_prop_list(meminfo), headers=["Property", "Value"], tablefmt="plain"
        )
    )
    return 0


def cmd_handler_device_container_storage(args) -> int:
    """Returns information about mountpoints in a container

    Arguments:
        args -- parsed command line arguments

    Returns:
        int -- 0 for success
    """
    api = moses_client.api.devices_api.DevicesApi(api_client)
    mountpoints = api.container_getmountpoints(
        args.device_id, args.container_id)
    mountpointslist = map(generate_mountpoint_list_item, mountpoints)
    logging.info(
        tabulate.tabulate(
            mountpointslist,
            headers="keys",
            tablefmt="plain"))
    return 0


def cmd_handler_device_container_ps(args) -> int:
    """Dumps a list of the processes currently running inside a container

    Arguments:
        args -- parsed command line arguments

    Returns:
        int -- 0 for success
    """
    api = moses_client.api.devices_api.DevicesApi(api_client)
    processes = api.container_getprocesses(args.device_id, args.container_id)
    processeslist = map(generate_process_list_item, processes)
    logging.info(
        tabulate.tabulate(
            processeslist,
            headers="keys",
            tablefmt="plain"))
    return 0


def cmd_handler_device_container_logs(args) -> int:
    """Returns information about mountpoints in a container

    Arguments:
        args -- parsed command line arguments

    Returns:
        int -- 0 for success
    """
    api = moses_client.api.devices_api.DevicesApi(api_client)

    restart = True

    while True:
        line = api.container_getlogs(
            args.device_id,
            args.container_id,
            restart=restart)
        restart = False
        if len(line) == 0:
            break

        logging.info(line)

    return 0


def cmd_handler_device_key(args) -> int:
    """Returns path of the device private key file

    Arguments:
        args -- parsed command line arguments

    Returns:
        int -- 0 for success
    """
    api = moses_client.api.devices_api.DevicesApi(api_client)
    keypath = api.device_getprivatekey(args.device_id)
    logging.info(keypath)
    return 0


def cmd_handler_device_sync(args) -> int:
    """Sync a local folder with a folder on the device

    Arguments:
        args -- parsed command line arguments

    Returns:
        int -- 0 for success
    """
    api = moses_client.api.devices_api.DevicesApi(api_client)

    progress_id = handle_progress(args)

    device = api.device_syncfolders(
        args.device_id,
        os.path.abspath(args.source_folder),
        args.destination_folder,
        progress_id=progress_id,
    )
    return 0


def cmd_handler_device_ip(args) -> int:
    """Sync a local folder with a folder on the device

    Arguments:
        args -- parsed command line arguments

    Returns:
        int -- 0 for success
    """
    api = moses_client.api.devices_api.DevicesApi(api_client)
    ip = api.device_current_ip(args.device_id)
    logging.info(ip)
    return 0

def cmd_handler_device_validate(args) -> int:
    """Sync a local folder with a folder on the device

    Arguments:
        args -- parsed command line arguments

    Returns:
        int -- 0 for success
    """
    api = moses_client.api.devices_api.DevicesApi(api_client)
    result = api.device_validate_parameter(args.device_id,args.parameter,args.value)
    retcode = 0

    for warning in result.warnings:
        logging.warning(warning)
        retcode = 2
    for error in result.errors:
        logging.error(error)
        retcode = 1
    return retcode


def cmd_handler_application_info(args) -> int:
    """dumps application info

    Arguments:
        args {[type]} -- command line arguments

    Returns:
        int -- 0 for success
    """
    api = moses_client.api.applications_api.ApplicationsApi(api_client)

    application = api.application_get(args.application_id)
    logging.info(
        tabulate.tabulate(
            generate_prop_list(application),
            headers=["Property", "Value"],
            tablefmt="plain",
        )
    )
    return 0


def cmd_handler_application_build(args) -> int:
    """Build the container for a specific configuration of the app

    Arguments:
        args {[type]} -- command line arguments

    Returns:
        int -- 0 for success
    """
    api = moses_client.api.applications_api.ApplicationsApi(api_client)

    progress_id = handle_progress(args)

    logging.info("Building application, this may take a few minutes...")
    api.application_build(
        args.application_id, args.configuration, progress_id=progress_id
    )
    logging.info("Application %s successfully built.", args.application_id)
    return 0


def cmd_handler_application_deploy(args) -> int:
    """Deploy the container for a specific configuration of the app
    to a selected device

    Arguments:
        args {[type]} -- command line arguments

    Returns:
        int -- 0 for success
    """
    api = moses_client.api.applications_api.ApplicationsApi(api_client)
    progress_id = handle_progress(args)

    logging.info("Deploying application, this may take a few minutes...")
    api.application_deploy(
        args.application_id, args.configuration, args.device_id, progress_id=progress_id
    )
    logging.info("Application %s successfully deployed.", args.application_id)
    return 0


def cmd_handler_application_run(args) -> int:
    """Run the container for a specific configuration of the app
    on a selected device

    Arguments:
        args {[type]} -- command line arguments

    Returns:
        int -- 0 for success
    """
    api = moses_client.api.applications_api.ApplicationsApi(api_client)
    progress_id = handle_progress(args)

    logging.info("Starting application...")
    container = api.application_run(
        args.application_id, args.configuration, args.device_id, progress_id=progress_id
    )
    logging.info("Started container %s", container.id)
    return 0


def cmd_handler_application_stop(args) -> int:
    """Stops the container for a specific configuration of the app
    on a selected device

    Arguments:
        args {[type]} -- command line arguments

    Returns:
        int -- 0 for success
    """
    api = moses_client.api.applications_api.ApplicationsApi(api_client)

    container = api.application_stop(
        args.application_id, args.configuration, args.device_id
    )
    return 0


def cmd_handler_application_container(args) -> int:
    """Returns information about the application container running
    on a selected device

    Arguments:
        args {[type]} -- command line arguments

    Returns:
        int -- 0 for success
    """
    api = moses_client.api.applications_api.ApplicationsApi(api_client)

    container = api.application_getcontainer(
        args.application_id, args.configuration, args.device_id
    )

    logging.info(
        tabulate.tabulate(
            generate_prop_list(container),
            headers=["Property", "Value"],
            tablefmt="plain",
        )
    )
    return 0


def cmd_handler_application_logs(args) -> int:
    """Stops the container for a specific configuration of the app
    on a selected device

    Arguments:
        args {[type]} -- command line arguments

    Returns:
        int -- 0 for success
    """
    api = moses_client.api.applications_api.ApplicationsApi(api_client)

    restart = True

    while True:
        line = api.application_getcontainer_logs(
            args.application_id,
            args.configuration,
            args.device_id,
            restart=restart)
        restart = False

        if len(line) == 0:
            break
        logging.info(line)

    return 0


def cmd_handler_application_key(args) -> int:
    """prints path of private key file

    Arguments:
        args {[type]} -- command line arguments

    Returns:
        int -- 0 for success
    """
    api = moses_client.api.applications_api.ApplicationsApi(api_client)

    keypath = api.application_getprivatekey(args.application_id)
    logging.info(keypath)
    return 0


def cmd_handler_application_reseal(args) -> int:
    """removes keys and ids from configuration

    Arguments:
        args {[type]} -- command line arguments

    Returns:
        int -- 0 for success
    """
    api = moses_client.api.applications_api.ApplicationsApi(api_client)

    api.application_reseal(args.application_id)
    logging.warning(
        "Application has been resealed. It should not be used for any further operation, otherwise keys will be regenerated."
    )
    return 0


def cmd_handler_application_sync(args) -> int:
    """transfer files into the application container

    Arguments:
        args {[type]} -- command line arguments

    Returns:
        int -- 0 for success
    """
    api = moses_client.api.applications_api.ApplicationsApi(api_client)

    progress_id = handle_progress(args)

    api.application_syncfolders(
        args.application_id,
        args.source_folder,
        args.configuration,
        args.device_id,
        args.destination_folder,
        source_is_sdk=args.source_is_sdk,
        progress_id=progress_id,
    )
    return 0


def cmd_handler_application_cmdline(args) -> int:
    """Returns docker command line for a specific application configuration

    Arguments:
        args {[type]} -- command line arguments

    Returns:
        int -- 0 for success
    """
    api = moses_client.api.applications_api.ApplicationsApi(api_client)

    cmdline = api.application_getdocker_commandline(
        args.application_id, args.configuration
    )
    logging.info(cmdline)
    return 0


def cmd_handler_application_composefile(args) -> int:
    """Returns docker compose file for a specific application configuration

    Arguments:
        args {[type]} -- command line arguments

    Returns:
        int -- 0 for success
    """
    api = moses_client.api.applications_api.ApplicationsApi(api_client)

    composefile = api.application_getdocker_composefile(
        args.application_id, args.configuration
    )
    logging.info(composefile)
    return 0


def cmd_handler_application_push(args) -> int:
    """Pushes the required container to a docker registry

    Arguments:
        args {[type]} -- command line arguments

    Returns:
        int -- 0 for success
    """
    api = moses_client.api.applications_api.ApplicationsApi(api_client)

    progress_id = handle_progress(args)

    composefile = api.application_push_to_registry(
        args.application_id,
        args.configuration,
        args.username,
        args.password,
        progress_id=progress_id,
    )
    logging.info(composefile)
    return 0

def cmd_handler_application_setprop(args) -> int:
    """Set an application's property

    Arguments:
        args {[type]} -- command line arguments

    Returns:
        int -- 0 for success
    """
    api = moses_client.api.applications_api.ApplicationsApi(api_client)
    application = api.application_get(args.application_id)

    value=yaml.full_load(args.value)

    if args.property.startswith("props."):
        if args.configuration is None:
            raise argparse.ArgumentError(None,"Custom properties require configuration parameter.")

        propertyname=args.property[len("props."):]
        application.props[args.configuration][propertyname]="" if value is None else value
    else:
        if args.configuration is None:
            setattr(application,args.property,str(value))
        else:
            dictionary=getattr(application,args.property)
            dictionary[args.configuration]=value

    api.application_modify(args.application_id,application=application)
    return 0


def cmd_handler_application_publish(args) -> int:
    """Build the container for a specific configuration of the app

    Arguments:
        args {[type]} -- command line arguments

    Returns:
        int -- 0 for success
    """
    api = moses_client.api.applications_api.ApplicationsApi(api_client)

    progress_id = handle_progress(args)

    logging.info("Publishing application to Torizon OTA...")
    api.application_publish(
        args.application_id, args.credentials, args.username, args.password, progress_id=progress_id
    )
    return 0

def cmd_handler_application_validate_parameter(args) -> int:
    """Validate a simple parameter"""
    api = moses_client.api.applications_api.ApplicationsApi(api_client)

    result = api.application_validate_parameter(args.application_id, args.configuration, args.parameter, args.value)
    retcode = 0

    for warning in result.warnings:
        logging.warning(warning)
        retcode = 2
    for error in result.errors:
        logging.error(error)
        retcode = 1
    return retcode

def cmd_handler_application_validate_item(args) -> int:
    """Validate an array item"""
    api = moses_client.api.applications_api.ApplicationsApi(api_client)

    result = api.application_validate_array_item(args.application_id, args.configuration, args.array, args.value, args.index)
    retcode = 0

    for warning in result.warnings:
        logging.warning(warning)
        retcode = 2
    for error in result.errors:
        logging.error(error)
        retcode = 1
    return retcode

def cmd_handler_application_validate_entry(args) -> int:
    """Validate an array item"""
    api = moses_client.api.applications_api.ApplicationsApi(api_client)

    result = api.application_validate_dictionary_entry(args.application_id, args.configuration, args.dictionary, args.key, args.value, args.newitem)
    retcode = 0

    for warning in result.warnings:
        logging.warning(warning)
        retcode = 2
    for error in result.errors:
        logging.error(error)
        retcode = 1
    return retcode

def cmd_handler_detect(args) -> int:
    """Detects a new serial or network device

    Arguments:
        args -- parsed command line arguments

    Returns:
        int -- 0 for success
    """
    api = moses_client.api.devices_api.DevicesApi(api_client)

    device = None

    if args.network:
        logging.info(
            "Attepting to detect network device, this may take a couple of minutes."
        )
        logging.info(
            "Check that your device is turned on and connected to the network."
        )
        logging.info("At the end of detection your device will reboot.")
        device = api.devices_networkdetect(
            args.target, args.username, args.password)
    else:
        logging.info(
            "Attepting to detect serial device, this may take a couple of minutes, after detection the device will reboot."
        )
        logging.info(
            "Check that your device is powered on an connected to your PC via serial/USB cable."
        )
        logging.info("At the end of detection your device will reboot.")
        device = api.devices_serialdetect(
            args.target, args.username, args.password)

    logging.info("Device successfully detected.")
    logging.info(
        tabulate.tabulate(
            generate_prop_list(device), headers=["Property", "Value"], tablefmt="plain"
        )
    )

    return 0


def cmd_handler_create(args) -> int:
    """Creates a new application

    Arguments:
        args {[type]} -- command line arguments

    Returns:
        int -- 0 for success
    """
    api = moses_client.api.applications_api.ApplicationsApi(api_client)

    # the api requires absolute paths
    path = os.path.abspath(args.path)

    application = api.applications_create(
        args.platform_id, path, username=args.username
    )

    logging.info("%s", application.id)
    return 0


def cmd_handler_load(args) -> int:
    """Loads an existing application configuration

    Arguments:
        args {[type]} -- command line arguments

    Returns:
        int -- 0 for success
    """
    api = moses_client.api.applications_api.ApplicationsApi(api_client)

    # the api requires absolute paths
    path = os.path.abspath(args.path)

    application = api.applications_load(path)
    logging.info("%s", application.id)
    return 0


def cmd_handler_application_updatesdk(args) -> int:
    """Updates an application SDK

    Arguments:
        args {[type]} -- command line arguments

    Returns:
        int -- 0 for success
    """
    api = moses_client.api.applications_api.ApplicationsApi(api_client)

    progress_id = handle_progress(args)

    logging.info("Updating SDK, this may require a few minutes...")
    api.application_updatesdk(
        args.application_id, args.configuration, progress_id=progress_id
    )
    logging.info(
        "SDK for application %s successfully updated.",
        args.application_id)
    return 0


def cmd_handler_application_runsdk(args) -> int:
    """Runs the SDK container for an application

    Arguments:
        args {[type]} -- command line arguments

    Returns:
        int -- 0 for success
    """
    api = moses_client.api.applications_api.ApplicationsApi(api_client)

    progress_id = handle_progress(args)

    sdkaddress = api.application_runsdk(
        args.application_id, args.configuration, progress_id=progress_id
    )

    logging.info(
        tabulate.tabulate(
            generate_prop_list(sdkaddress),
            headers=["Property", "Value"],
            tablefmt="plain",
        )
    )
    return 0


def cmd_handler_pull(args) -> int:
    """Download base containers

    Arguments:
        args {[type]} -- command line arguments

    Returns:
        int -- 0 for success
    """
    api = moses_client.api.setup_api.SetupApi(api_client)

    progress_id = handle_progress(args)
    api.setup_pullcontainers(progress_id=progress_id)
    return 0


def cmd_handler_enableemulation(args) -> int:
    """Enables ARM emulation

    Arguments:
        args {[type]} -- command line arguments

    Returns:
        int -- 0 for success
    """
    api = moses_client.api.setup_api.SetupApi(api_client)

    progress_id = handle_progress(args)
    api.setup_enableemulation(progress_id=progress_id)
    return 0

def cmd_handler_version(args) -> int:
    """Return backend version

    Arguments:
        args {[type]} -- command line arguments

    Returns:
        int -- 0 for success
    """
    api = moses_client.api.version_api.VersionApi(api_client)
    backend_version = api.version_get()

    logging.info(
        tabulate.tabulate(
            generate_dict_list(backend_version), headers=["Property", "Value"], tablefmt="plain"
        )
    )
    return 0

def cmd_handler_dockerversion(args) -> int:
    """Return docker version

    Arguments:
        args {[type]} -- command line arguments

    Returns:
        int -- 0 for success
    """
    api = moses_client.api.version_api.VersionApi(api_client)
    docker_version = api.version_docker()

    logging.info(
        tabulate.tabulate(
            generate_prop_list(docker_version), headers=["Property", "Value"], tablefmt="plain"
        )
    )
    return 0

def create_parser() -> argparse.ArgumentParser:
    """Creates a parser for the command line arguments

    Returns:
        argparse.ArgumentParser -- parser

        Parser structure looks complex, with lots of sub-parsers, but basically
        it's splitted in 3 levels: topic, sub-topic, command
        Sub-topic is optional.
        This will allow usage of commands like:
        device image ls
        or
        application create
        each with its own set of arguments
    """

    parser = argparse.ArgumentParser(
        prog=os.path.basename(sys.argv[0]),
        description="Torizon Developer Swiss Knife Tool",
    )

    parser.add_argument(
        "-p", "--progress", action="store_true", dest="progress", default=False, help="provide progress information during the operation"
    )

    parser.add_argument(
        "-b", "----backend", dest="backend", default=None, help="<address>:<port> used to call backend REST api."
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    # add first level commands
    device_parser = subparsers.add_parser("devices")
    device_parser = subparsers.add_parser("device")
    eulas_parser = subparsers.add_parser("eulas")
    eula_parser = subparsers.add_parser("eula")
    platforms_parser = subparsers.add_parser("platforms")
    platform_parser = subparsers.add_parser("platform")
    application_parser = subparsers.add_parser("application")
    detect_parser = subparsers.add_parser("detect")
    create_parser = subparsers.add_parser("create")
    load_parser = subparsers.add_parser("load")
    pullcontainers_parser = subparsers.add_parser("pull")
    enableemulation_parser = subparsers.add_parser("enableemulation")
    version_parser = subparsers.add_parser("version")
    dockerversion_parser = subparsers.add_parser("dockerversion")
    device_parser.add_argument(
        "device_id", help="Device serial number", metavar="device-id"
    )

    # add sub-commands for device
    device_subparsers = device_parser.add_subparsers(dest="subcommand", required=True)

    device_subparsers.add_parser("images")
    device_subparsers.add_parser("containers")
    device_subparsers.add_parser("info")
    device_image_parser = device_subparsers.add_parser("image")
    device_container_parser = device_subparsers.add_parser("container")
    device_subparsers.add_parser("ps")
    device_subparsers.add_parser("mem")
    device_subparsers.add_parser("storage")
    device_subparsers.add_parser("key")
    device_sync_parser = device_subparsers.add_parser("sync")
    device_subparsers.add_parser("ip")
    device_validate_parser = device_subparsers.add_parser("validate")

    # add sub-commands for device image
    device_image_parser.add_argument(
        "image_id", help="Image SHA-id", metavar="image-id"
    )
    device_image_subparsers = device_image_parser.add_subparsers(
        dest="subsubcommand", required=True)

    device_image_subparsers.add_parser("info")
    device_image_subparsers.add_parser("delete")

    # add commands for device container
    device_container_parser.add_argument(
        "container_id", help="Container SHA-id", metavar="container-id"
    )
    device_container_subparsers = device_container_parser.add_subparsers(
        dest="subsubcommand", required=True
    )

    device_container_subparsers.add_parser("info")
    device_container_subparsers.add_parser("start")
    device_container_subparsers.add_parser("stop")
    device_container_subparsers.add_parser("ps")
    device_container_subparsers.add_parser("mem")
    device_container_subparsers.add_parser("storage")
    device_container_subparsers.add_parser("logs")

    device_sync_parser.add_argument(
        "source_folder", help="Source folder (host PC)", metavar="source-folder"
    )
    device_sync_parser.add_argument(
        "destination_folder",
        help="Destination folder (target device)",
        metavar="destination-folder",
    )

    device_validate_parser.add_argument(
        "parameter",
        help="Parameter being validated")

    device_validate_parser.add_argument(
        "value",
        help="Value for the parameter being validated")

    detect_parser.add_argument(
        "target", type=str, help="serial port or ip address/hostname"
    )
    detect_parser.add_argument(
        "username", type=str, help="username to be used for login"
    )
    detect_parser.add_argument("password", type=str, help="password")
    detect_parser.add_argument(
        "--network", dest="network", action="store_true", default=False
    )
    detect_parser.add_argument(
        "--uart", dest="network", action="store_false", default=False
    )
    detect_parser.set_defaults(network=False)

    # add commands for platform
    platform_parser.add_argument(
        "platform_id", help="Platform unique identifier", metavar="platform-id"
    )
    platform_subparsers = platform_parser.add_subparsers(dest="subcommand", required=True)

    platform_subparsers.add_parser("info")
    platform_subparsers.add_parser("compatible")

    application_parser.add_argument(
        "application_id", help="Application unique identifier", metavar="application-id"
    )
    application_subparsers = application_parser.add_subparsers(
        dest="subcommand", required=True)

    application_subparsers.add_parser("info")
    application_build_parser = application_subparsers.add_parser("build")
    application_deploy_parser = application_subparsers.add_parser("deploy")
    application_run_parser = application_subparsers.add_parser("run")
    application_stop_parser = application_subparsers.add_parser("stop")
    application_container_parser = application_subparsers.add_parser(
        "container")
    application_updatesdk_parser = application_subparsers.add_parser(
        "updatesdk")
    application_runsdk_parser = application_subparsers.add_parser("runsdk")
    application_key_parser = application_subparsers.add_parser("key")
    application_reseal_parser = application_subparsers.add_parser("reseal")
    application_sync_parser = application_subparsers.add_parser("sync")
    application_cmdline_parser = application_subparsers.add_parser("cmdline")
    application_composefile_parser = application_subparsers.add_parser(
        "composefile")
    application_push_parser = application_subparsers.add_parser("push")
    application_setprop_parser = application_subparsers.add_parser("setprop")
    application_logs_parser = application_subparsers.add_parser("logs")
    application_publish_parser = application_subparsers.add_parser("publish")
    application_validate_parser = application_subparsers.add_parser("validate")

    application_build_parser.add_argument(
        "configuration", help="debug/release or other app-specific configuration"
    )

    application_deploy_parser.add_argument(
        "configuration", help="debug/release or other app-specific configuration"
    )
    application_deploy_parser.add_argument(
        "device_id", help="Device serial number", metavar="device-id"
    )

    application_run_parser.add_argument(
        "configuration", help="debug/release or other app-specific configuration"
    )
    application_run_parser.add_argument(
        "device_id", help="Device serial number", metavar="device-id"
    )

    application_stop_parser.add_argument(
        "configuration", help="debug/release or other app-specific configuration"
    )
    application_stop_parser.add_argument(
        "device_id", help="Device serial number", metavar="device-id"
    )

    application_container_parser.add_argument(
        "configuration", help="debug/release or other app-specific configuration"
    )
    application_container_parser.add_argument(
        "device_id", help="Device serial number", metavar="device-id"
    )

    application_updatesdk_parser.add_argument(
        "configuration", help="debug/release or other app-specific configuration"
    )

    application_runsdk_parser.add_argument(
        "configuration", help="debug/release or other app-specific configuration"
    )

    application_sync_parser.add_argument(
        "source_folder", help="Source folder (host PC)", metavar="source-folder"
    )

    application_sync_parser.add_argument(
        "configuration", help="debug/release or other app-specific configuration"
    )
    application_sync_parser.add_argument(
        "device_id", help="Device serial number", metavar="device-id"
    )

    application_sync_parser.add_argument(
        "destination_folder",
        help="Destination folder (target device)",
        metavar="destination-folder",
    )
    application_sync_parser.add_argument(
        "--sdk",
        help="source folder is relative to sdk container",
        dest="source_is_sdk",
        action="store_true",
        default=False,
    )

    application_cmdline_parser.add_argument(
        "configuration", help="debug/release or other app-specific configuration"
    )

    application_composefile_parser.add_argument(
        "configuration", help="debug/release or other app-specific configuration"
    )

    application_push_parser.add_argument(
        "configuration", help="debug/release or other app-specific configuration"
    )
    application_push_parser.add_argument(
        "username", help="Username for docker registry login"
    )
    application_push_parser.add_argument(
        "password", help="password/token used for authentication"
    )

    application_setprop_parser.add_argument(
        "property", help="property name (use props.name for custom properties)"
    )

    application_setprop_parser.add_argument(
        "value", help="property value"
    )

    application_setprop_parser.add_argument(
        "configuration", help="debug/release/common or other app-specific configuration",
        nargs='?', default=None
    )

    application_logs_parser.add_argument(
        "configuration", help="debug/release or other app-specific configuration"
    )

    application_logs_parser.add_argument(
        "device_id", help="Device serial number", metavar="device-id"
    )

    application_publish_parser
    application_publish_parser.add_argument(
        "credentials", help="path to credentials.zip file"
    )
    application_publish_parser.add_argument(
        "username", help="Username for docker registry login"
    )
    application_publish_parser.add_argument(
        "password", help="password/token used for authentication"
    )

    application_validate_subparsers = application_validate_parser.add_subparsers(dest="subsubcommand", required=True)

    application_validate_parameter_parser = application_validate_subparsers.add_parser("parameter")
    application_validate_item_parser = application_validate_subparsers.add_parser("item")
    application_validate_entry_parser = application_validate_subparsers.add_parser("entry")

    application_validate_parameter_parser.add_argument(
        "configuration", help="debug/release/common"
    )
    application_validate_parameter_parser.add_argument(
        "parameter", help="parameter name"
    )
    application_validate_parameter_parser.add_argument(
        "value", help="parameter value"
    )

    application_validate_item_parser.add_argument(
        "configuration", help="debug/release/common"
    )
    application_validate_item_parser.add_argument(
        "array", help="array name"
    )
    application_validate_item_parser.add_argument(
        "value", help="item value"
    )

    application_validate_item_parser.add_argument(
        "index", help="item index (-1 for new item)",
        type=int, nargs="?", default=-1
    )
    application_validate_entry_parser.add_argument(
        "configuration", help="debug/release/common"
    )
    application_validate_entry_parser.add_argument(
        "dictionary", help="dictionary name"
    )
    application_validate_entry_parser.add_argument(
        "key", help="key value"
    )
    application_validate_entry_parser.add_argument(
        "value", help="entry value"
    )
    application_validate_entry_parser.add_argument(
        "--newitem", help="set if item is going to be added to dict",
        action="store_true", default=False
    )

    eula_parser.add_argument(
        "eula_id", help="Id of a specific eula", metavar="eula-id"
    )

    eula_subparsers = eula_parser.add_subparsers(
        dest="subcommand", required=True)
    eula_subparsers.add_parser("info")
    eula_setprop_parser=eula_subparsers.add_parser("setprop")

    eula_setprop_parser.add_argument(
        "property", help="property name"
    )

    eula_setprop_parser.add_argument(
        "value", help="property value"
    )

    # add command to create application
    create_parser.add_argument(
        "platform_id", help="Platform unique identifier", metavar="platform-id"
    )
    create_parser.add_argument(
        "path",
        help="Folder where application sub-folder will be created",
        metavar="path",
    )
    create_parser.add_argument(
        "username",
        help="Username that should be used to run the application inside the container",
        nargs="?",
        default="torizon",
        metavar="username",
    )

    load_parser.add_argument(
        "path", help="Folder from where application should be loaded", metavar="path"
    )

    return parser


def abort_handler(sig, frame):

    global progress

    if progress is not None:
        api = moses_client.api.progress_api.ProgressApi(api_client)

        api.progress_delete(progress_id=progress.id)

    logging.error("Operation aborted by user.")
    sys.exit(-1)


# If we're running in stand alone mode, run the application
if __name__ == "__main__":

    # configures logging: errors and warnings on stderr, regular messages on
    # stdout
    logger = logging.getLogger()

    logger.setLevel(logging.INFO)

    logstdout = logging.StreamHandler(sys.stdout)
    logstdout.setLevel(logging.INFO)
    logstdout.addFilter(lambda record: record.levelno <= logging.INFO)
    logstdout.setFormatter(logging.Formatter("%(message)s"))

    logstderr = logging.StreamHandler(sys.stderr)
    logstderr.setLevel(logging.WARNING)
    logstderr.setFormatter(logging.Formatter("%(message)s"))

    logger.addHandler(logstdout)
    logger.addHandler(logstderr)

    signal.signal(signal.SIGINT, abort_handler)

    parser = create_parser()

    args = parser.parse_args()

    if args.backend is not None:
        api_client=moses_client.ApiClient(moses_client.Configuration(host="http://"+args.backend+"/api"))

    function_name = "cmd_handler_"

    if not "command" in args or args.command is None:
        parser.print_usage()
        sys.exit(0)
    else:
        function_name += args.command

    if "subcommand" in args and args.subcommand is not None:
        function_name += "_" + args.subcommand

    if "subsubcommand" in args and args.subsubcommand is not None:
        function_name += "_" + args.subsubcommand

    try:
        sys.exit(getattr(sys.modules[__name__], function_name)(args))
    except Exception as e:
        code = -1
        if "body" in e.__dict__:

            try:
                ex = json.loads(e.__dict__["body"])
                if "description" in ex:
                    logging.error(ex["description"])
                if "message" in ex:
                    logging.error(ex["message"])
                if "code" in ex:
                    code = ex["code"]
            except BaseException:
                pass
            logging.error(e.__dict__["body"].strip('"\n'))

            if code == -1 and "status" in e.__dict__:
                code = e.status
        elif "args" in e.__dict__:
            logging.error(e.__dict__["args"])
        else:
            logging.error(e)

        if code == 404:
            code = 2  # not found
        elif code == 500:
            code = -1
        elif code > 500:
            code = code - 500
        sys.exit(code)
