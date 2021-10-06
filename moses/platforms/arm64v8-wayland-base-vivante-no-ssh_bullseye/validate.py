"""Platform-specific validation."""
import validation
import validation_utils

def init_app_tables(
    application: validation.ExtendedValidation) -> None:
    """Add platform-specific validation to application object."""
    validation_utils.add_base_container_props_validation(application)
    validation_utils.add_debian_container_props_validation(application)
    validation_utils.add_debian_sdk_container_props_validation(application)
