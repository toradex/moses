"""Additional validation routines useful for platform-specific validation files."""
from typing import Any, Callable, Optional
import validation

def add_prop_validation_entry(
    application: validation.ExtendedValidation,
    prop_name: str,
    fatal: bool,
    validation_function: Callable[...,Optional[str]],
    userarg: Any) -> None:
    """Add a validation entry for a property."""
    application.dictionary_validation_table["props"].append(
        (fatal, validation.validate_entry,
            (prop_name, validation_function, userarg)),
    )

def add_base_container_props_validation(
    application: validation.ExtendedValidation) -> None:
    """Add validation entries for containers using standard templates.

    :param application: application object
    :type application: validation.ExtendedValidation
    """
    add_prop_validation_entry(application, "expose",
        False, validation.validate_docker_command, None)
    add_prop_validation_entry(application, "arg",
        False, validation.validate_docker_command, None)
    add_prop_validation_entry(application, "env",
        False, validation.validate_docker_command, None)
    add_prop_validation_entry(application, "preinstallcommands",
        False, validation.validate_docker_command, None)
    add_prop_validation_entry(application, "buildfiles",
        False, validation.validate_docker_command, None)
    add_prop_validation_entry(application, "buildcommands",
        False, validation.validate_docker_command, None)
    add_prop_validation_entry(application, "targetfiles",
        False, validation.validate_docker_command, None)
    add_prop_validation_entry(application, "username",
        False, validation.validate_username, None)
    add_prop_validation_entry(application, "appname",
        False, validation.validate_filename, None)
    add_prop_validation_entry(application, "exename",
        False, validation.validate_relative_file_path, None)
    add_prop_validation_entry(application, "targetcommands",
        False, validation.validate_docker_command, None)

def add_debian_container_props_validation(
    application: validation.ExtendedValidation) -> None:
    """Add validation entries for debian-based containers.

    :param application: application object
    :type application: validation.ExtendedValidation
    """
    add_prop_validation_entry(application, "extrapackages",
        False, validation.validate_debian_package_list, None)

def add_debian_sdk_container_props_validation(
    application: validation.ExtendedValidation) -> None:
    """Add validation entries for debian-based containers.

    :param application: application object
    :type application: validation.ExtendedValidation
    """
    add_prop_validation_entry(application, "sdkpreinstallcommands",
        False, validation.validate_docker_command, None)
    add_prop_validation_entry(application, "sdkpostinstallcommands",
        False, validation.validate_docker_command, None)
    add_prop_validation_entry(application, "devpackages",
        False, validation.validate_debian_package_list, None)
    add_prop_validation_entry(application, "sdkpackages",
        False, validation.validate_debian_package_list, None)
