"""Define base class for objects that have custom properties stored in dictionaries."""
from typing import Optional, Dict, Any, List


# pylint: disable = too-many-instance-attributes
# pylint: disable = too-few-public-methods
class PropertiesObject:
    """Base class implementing properties shared between application and platform."""

    def __init__(self) -> None:
        """Initialize common properties."""
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
        self.devices: Dict[str, List[str]] = {
            "common": [], "debug": [], "release": []}

        self.networks: Dict[str, List[str]] = {
            "common": [], "debug": [], "release": []}

        self.extraparms: Dict[str, Dict[str, Any]] = {
            "common": {},
            "debug": {},
            "release": {},
        }

        self.dockercomposefile: Dict[str, Optional[str]] = {
            "common": None,
            "debug": None,
            "release": None,
        }

        self.startupscript: Dict[str, Optional[str]] = {
            "common": None,
            "debug": None,
            "release": None,
        }

        self.shutdownscript: Dict[str, Optional[str]] = {
            "common": None,
            "debug": None,
            "release": None,
        }

        self.props: Dict[str, Dict[str, str]] = {
            "common": {},
            "debug": {},
            "release": {},
        }

    def get_custom_prop(self, configuration: str,
                        prop: str) -> Optional[str]:
        """Return value for a custom property.

        If there is a configuration-specific value, it's returned, otherwise the function
        checks for a common value, if even this one has not been configured, then it will
        return None.

        :param configuration: debug/release
        :type configuration: str
        :param prop: property name
        :type prop: str
        :returns: property value or None
        :rtype: str | None

        """
        if prop in self.props[configuration]:
            return str(self.props[configuration][prop])
        if prop in self.props["common"]:
            return str(self.props["common"][prop])
        return None
