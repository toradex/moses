"""Module with base class and functions used for validation."""
import inspect
import re
from typing import Any, Callable, Dict, List, Optional, Tuple
import yaml
import jsonschema
import tags

#pylint: disable=too-few-public-methods
class ValidationResult:
    """Stores results of validation."""

    def __init__(self) -> None:
        """Initialize the object."""
        self.errors : List[str] = []
        self.warnings : List[str] = []

    def to_json(self) -> Dict[str, Any]:
        """Convert object to an array of json-compatible key-value pairs.

        :return: properties as a dictionary
        :rtype: Dict[str, Any]

        """
        return self.__dict__

# pylint: disable=too-few-public-methods
class BasicValidation:
    """Support base validation via parameters table.

    To be used for object that support only simple parameters
    """

    def __init__(self,
                 validation_table: Dict[str,
                                        List[
                                            Tuple[
                                                bool,
                                                Callable[...,Optional[str]],
                                                Any]]],
                 skip_table: Optional[
                                Dict[
                                    str,
                                    List[Callable[...,bool]]]]) -> None:
        """Initialize the object.

        param validation_table: A dictionary with parameters and their validation functions.
        type validation_table: dictionary with string keys and callable values.
        parm skip_table: A dictionary with parameters for which validation can be skipped
        if value matches some conditions.
        type skip_table: dictionary with string keys and callable values.
        """
        self.validation_table = validation_table
        self.skip_table = skip_table if skip_table is not None else {}

    def _should_be_skipped(self, parameter: str, value: str) -> bool:
        """Check if validation should be skipped.

        :param parameter: parameter name
        :type parameter: str
        :param value: parameter value
        :type value: str
        :return: True if validation should be skipped
        :rtype: bool
        """
        if parameter in self.skip_table:
            for skip_fn in self.skip_table[parameter]:
                if skip_fn(self, value):
                    return True
        return False

    def validate(self,
                 parameter:str,
                 value: str)-> ValidationResult:
        """Validate a parameter.

        :param parameter: parameter name
        :type parameter: str
        :param value: value to be validated (always a string)
        :type value: str
        :return: list of errors and warming messages
        :rtype: Tuple[List[ValidationMessage],List[ValidationMessage]]
        """
        result = ValidationResult()

        if self._should_be_skipped(parameter, value):
            return result

        if parameter in self.validation_table:
            for error,validation_fn,userarg in self.validation_table[parameter]:
                message=validation_fn(self,value,userarg)
                if message is not None:
                    if error:
                        result.errors.append(message)
                        break
                    result.warnings.append(message)
        return result

class ExtendedValidation(BasicValidation):
    """Extended validation class.

    Used for objects that must validate parameters inside arrays and dictionaries
    """

    def __init__(self,
                 validation_table: Dict[str,
                                        List[
                                            Tuple[
                                                bool,
                                                Callable[...,Optional[str]],
                                                Any]]],
                 skip_table: Optional[
                                Dict[
                                    str,
                                    List[Callable[...,bool]]]],
                 array_validation_table: Dict[str,
                                              List[
                                                  Tuple[
                                                      bool,
                                                      Callable[...,Optional[str]],
                                                      Any]]],
                dictionary_validation_table: Dict[str,
                                             List[
                                                 Tuple[
                                                     bool,
                                                     Callable[...,Optional[str]],
                                                     Any]]]) -> None:
        """Initialize the object.

        param validation_table: A dictionary with parameters and their validation functions.
        type validation_table: dictionary with string keys and callable values.
        parm skip_table: A dictionary with parameters for which validation can be skipped
        if value matches some conditions.
        type skip_table: dictionary with string keys and callable values.
        param array_validation_table: A dictionary with parameters and their validation functions.
        type array_validation_table: dictionary with string keys and callable values.
        param dictionary_validation_table: A dictionary with parameters
        and their validation functions.
        type dictionary_validation_table: dictionary with string keys and callable values.
        """
        super().__init__(validation_table, skip_table)
        self.array_validation_table = array_validation_table
        self.dictionary_validation_table = dictionary_validation_table

    def get_array(self, array_name: str) -> List[Any]:
        """Get array values.

        :param array_name: array name
        :type array_name: str
        :return: array value
        :rtype: List[Any]
        """
        raise NotImplementedError

    def get_dictionary(self, dictionary_name: str) -> Dict[str, Any]:
        """Get dictionary values.

        :param dictionary_name: dictionary name
        :type dictionary_name: str
        :return: dictionary value
        :rtype: Dict[str, Any]
        """
        raise NotImplementedError

    @staticmethod
    def is_single_parm_callable(function: Callable[...,Optional[str]]) -> bool:
        """Check if a function is a single parameter callable.

        :param function: function to be checked
        """
        signature = inspect.signature(function)

        if signature.return_annotation != Optional[str] \
            or len(signature.parameters) != 3:
            return False

        if (not "self" in signature.parameters) or \
           (not "value" in signature.parameters) or \
           (not "userarg" in signature.parameters):
            return False

        #pylint: disable=comparison-with-callable
        if signature.parameters["self"].annotation != Any \
            or signature.parameters["value"].annotation != str:
            return False

        return True


    def validate_array_item(self,
                            parameter: str,
                            value: str,
                            index: int,
                            ) -> ValidationResult:
        """Validate an array item.

        :param parameter: array name
        :type parameter: str
        :param value: value to be validated (always a string)
        :type value: str
        : parm index: index of the item or -1 for added item
        : type index: int
        """
        result = ValidationResult()

        if self._should_be_skipped(parameter, value):
            return result

        array = self.get_array(parameter)
        if parameter in self.array_validation_table:
            for error,validation_fn,userarg in self.array_validation_table[parameter]:
                if self.is_single_parm_callable(validation_fn):
                    message = validation_fn(self,value,userarg)
                else:
                    message = validation_fn(self, array, value, index, userarg)

                if message is not None:
                    if error:
                        result.errors.append(message)
                        break
                    result.warnings.append(message)
        return result

    def validate_dictionary_entry(self,
                            parameter: str,
                            key: str,
                            value: str,
                            newitem: bool) -> ValidationResult:
        """Validate a dictionary entry.

        :param parameter: dictionary name
        :type parameter: str
        :param key: key
        :type parameter: str
        :param value: value to be validated (always a string)
        :type value: str
        :param newitem: True if the entry is new
        :type newitem: bool
        """
        result = ValidationResult()

        if self._should_be_skipped(parameter, value):
            return result

        dictionary = self.get_dictionary(parameter)
        if parameter in self.dictionary_validation_table:
            for error,validation_fn,userarg in self.dictionary_validation_table[parameter]:
                if self.is_single_parm_callable(validation_fn):
                    message = validation_fn(self,value,userarg)
                else:
                    message = validation_fn(self, dictionary, key, value, newitem, userarg)

                if message is not None:
                    if error:
                        result.errors.append(message)
                        break
                    result.warnings.append(message)
        return result

# validate functions

# pylint: disable=unused-argument
def validate_regexp(self: Any,
                    value: str,
                    userarg: re.Pattern) -> Optional[str]:
    """Validate a value using a regular expression.

    :param self: not used
    :type self: Any
    :param value: value to be validated
    :type value: str
    :return: true when the value is valid
    :rtype: bool
    :param userarg: regular expression that should match the value
    :type userarg: re.Pattern
    """
    if userarg.match(value) is None:
        return f"Value does not match regex {userarg.pattern}"
    return None

# pylint: disable=unused-argument
def validate_empty_string(self: Any,
                          value: str,
                          userarg: Any) -> Optional[str]:
    """Check that string is empty.

    :param self: not used
    :type self: Any
    :param value: value to be validated
    :type value: str
    :param userarg: not used
    :type userarg: Any
    """
    if len(value) != 0:
        return "Empty string is a valid value"
    return None

# pylint: disable=unused-argument
def validate_non_empty_string(self: Any,
                              value: str,
                              userarg: Any) -> Optional[str]:
    """Check that string is not empty.

    :param self: not used
    :type self: Any
    :param value: value to be validated
    :type value: str
    :param userarg: not used
    :type userarg: Any
    """
    if len(value) == 0:
        return "Value can't be an empty string"
    return None

USERNAME_REGEXP = re.compile(r"^[a-z_]([a-z0-9_-]{0,31}|[a-z0-9_-]{0,30}\$)$")

# pylint: disable=unused-argument
def validate_username(self: Any,
                      value: str,
                      userarg: Any) -> Optional[str]:
    """Check that parameter is a valid Linux username.

    :param self: not used
    :type self: Any
    :param value: value to be validated
    :type value: str
    :param userarg: not used
    :type userarg: Any
    """
    if not validate_regexp(self, value, USERNAME_REGEXP) is None:
        return "Value is not a valid Linux username"
    return None

# pylint: disable=unused-argument
def validate_hostname(self: Any,
                      value: str,
                      userarg: Any) -> Optional[str]:
    """Check that parameter is a valid hostname.

    :param self: not used
    :type self: Any
    :param value: value to be validated
    :type value: str
    :param userarg: not used
    :type userarg: Any
    """
    hostname = value.encode("idna").decode().split(":")[0]
    if len(hostname) > 255:
        return "Hostname is too long."
    hostname = hostname.rstrip(".")
    allowed = re.compile(r"(?!-)[A-Z\d\-\_]{1,63}(?<!-)$", re.IGNORECASE)
    if all(allowed.match(x) for x in hostname.split(".")):
        return None
    return "Value does not appear to be a valid hostname or IP address."

REMOTE_PATH_REGEXP = re.compile(r"^(\/[\w^ ]+)+\/?([\w.])+[^.]$")

def validate_remote_path(self: Any,
                             value: str,
                             userarg: Any) -> Optional[str]:
    """Check that parameter is a valid file name.

    :param self: not used
    :type self: Any
    :param value: value to be validated
    :type value: str
    :param userarg: not used
    :type userarg: Any
    """
    if not validate_regexp(self, value, REMOTE_PATH_REGEXP) is None:
        return "Value does not appear to be a valid path."
    return None


RELATIVE_OR_ABSOLUTE_PATH_REGEXP = re.compile(
    r"([a-z0-9_\-\.]+/)+[a-z0-9_\-\.]*$|^[a-z0-9_\-\.]*$|^/([a-z0-9_\-\.]+/)+[a-z0-9_\-\.]*$")

def validate_path(self: Any,
                                value: str,
                                userarg: Any) -> Optional[str]:
    """Check that parameter is a valid path (dir or file).

    :param self: not used
    :type self: Any
    :param value: value to be validated
    :type value: str
    :param userarg: not used
    :type userarg: Any
    """
    if not validate_regexp(self, value, RELATIVE_FILE_REGEXP) is None:
        return "Value does not appear to be a valid relative file path."
    return None

FILENAME_REGEXP = re.compile(r"[a-z0-9_\-\.]*$")

def validate_filename(self: Any,
                      value: str,
                      userarg: Any) -> Optional[str]:
    """Check that parameter is a valid file or dir name (no additional paths).

    :param self: not used
    :type self: Any
    :param value: value to be validated
    :type value: str
    :param userarg: not used
    :type userarg: Any
    """
    if not validate_regexp(self, value, FILENAME_REGEXP) is None:
        return "Value does not appear to be a valid relative file path."
    return None


RELATIVE_FILE_REGEXP = re.compile(r"^([a-z0-9_\-\.]+/)+[a-z0-9_\-\.]*$|^[a-z0-9_\-\.]*$")

def validate_relative_file_path(self: Any,
                                value: str,
                                userarg: Any) -> Optional[str]:
    """Check that parameter is a valid relative path.

    :param self: not used
    :type self: Any
    :param value: value to be validated
    :type value: str
    :param userarg: not used
    :type userarg: Any
    """
    if not validate_regexp(self, value, RELATIVE_FILE_REGEXP) is None:
        return "Value does not appear to be a valid relative file path."
    return None

DOCKER_NAME_REGEXP = re.compile(
    r"^/?[a-zA-Z0-9][a-zA-Z0-9_.-]+$")

def validate_docker_name(self: Any,
                         value: str,
                         userarg: Any) -> Optional[str]:
    """Check that parameter is a valid directory name.

    :param self: not used
    :type self: Any
    :param value: value to be validated
    :type value: str
    :param userarg: not used
    :type userarg: Any
    """
    if not validate_regexp(self, value, DOCKER_NAME_REGEXP) is None:
        return "Value does not appear to be a valid docker object name."
    return None

SEMANTIC_VERSION_REGEXP = re.compile(
    r"^(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)"\
    r"(?:-((?:0|[1-9][0-9]*|[0-9]*[a-zA-Z-][0-9a-zA-Z-]*)"\
    r"(?:\.(?:0|[1-9][0-9]*|[0-9]*[a-zA-Z-][0-9a-zA-Z-]*))*))?"\
    r"(?:\+([0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$")

def validate_semantic_version(self: Any,
                         value: str,
                         userarg: Any) -> Optional[str]:
    """Check that parameter is a valid version number.

    :param self: not used
    :type self: Any
    :param value: value to be validated
    :type value: str
    :param userarg: not used
    :type userarg: Any
    """
    if not validate_regexp(self, value, SEMANTIC_VERSION_REGEXP) is None:
        return "Value does not appear to be a valid version number in the format maj.min.build."
    return None

def validate_number(self: Any,
                    value: str,
                    userarg: Any) -> Optional[str]:
    """Check that parameter is a valid number.

    :param self: not used
    :type self: Any
    :param value: value to be validated
    :type value: str
    :param userarg: can be a tuple of (min, max) or None
    :type userarg: Any
    """
    try:
        intvalue=int(value)
    except ValueError:
        return "Value does not appear to be a valid number."

    if userarg is not None:
        if isinstance(userarg, tuple):
            range_min, range_max = userarg

            if intvalue<range_min or intvalue>range_max:
                return f"Value is not in the allowed range ({range_min}-{range_max})."
    return None

def validate_unique_items(self: Any,
                          array: List[str],
                          value: str,
                          index: int,
                          userarg: Any) -> Optional[str]:
    """Check that parameter is not already in a list of unique items.

    :param self: not used
    :type self: Any
    :param array: list of unique items
    :type array: List[str]
    :param value: value to be validated
    :type value: List[str]
    :param index: index of value in array (or -1 for added item)
    :type index: int
    :param userarg: not used
    :type userarg: Any
    """
    if not value in array:
        return None
    if array.index(value) == index:
        return None
    return "Duplicated value."

# pylint: disable=too-many-arguments
def validate_non_empty_key(self:Any,
                         dictionary: Dict[str,str],
                         key: str,
                         value: str,
                         newitem: bool,
                         userarg: Any) -> Optional[str]:
    """Check that the key is valid.

    :param self: not used
    :type self: Any
    :param dictionary: dictionary of unique keys
    :type dictionary: Dict[str,str]
    :param key: key to be validated
    :type key: str
    :param value: value to be validated
    :type value: str
    :param newitem: True if the key is new, False if it is an existing key
    :type newitem: bool
    :param userarg: not used
    :type userarg: Any
    """
    if len(key) == 0:
        return "Key can't be an empty string."
    return None

# pylint: disable=too-many-arguments
def validate_unique_keys(self:Any,
                         dictionary: Dict[str,str],
                         key: str,
                         value: str,
                         newitem: bool,
                         userarg: Any) -> Optional[str]:
    """Check that parameter is not already in a dictionary of unique keys.

    :param self: not used
    :type self: Any
    :param dictionary: dictionary of unique keys
    :type dictionary: Dict[str,str]
    :param key: key to be validated
    :type key: str
    :param value: value to be validated
    :type value: str
    :param newitem: True if the item is new, False if it is being updated
    :type newitem: bool
    :param userarg: not used
    :type userarg: Any
    """
    if newitem and key in dictionary:
        return "Duplicated key."
    return None

# pylint: disable=too-many-arguments
def validate_key(self:Any,
                 dictionary: Dict[str,str],
                 key: str,
                 value: str,
                 newitem: bool,
                 userarg: Tuple[Callable[...,Optional[str]],Any]) -> Optional[str]:
    """Apply a validation function to the key.

    :param self: not used
    :type self: Any
    :param dictionary: dictionary of unique keys
    :type dictionary: Dict[str,str]
    :param key: key to be validated
    :type key: str
    :param value: not used
    :type value: str
    :param newitem: True if the key is new, False if it is an existing key
    :type newitem: bool
    :param userarg: function to be applied to the key and its argument
    :type userarg: Tuple[Callable[...,Optional[str]],Any]
    """
    validation_fn, fn_arg = userarg

    return validation_fn(self, key, fn_arg)


def validate_device_name(self:Any,
                         value: str,
                         userarg: Any) -> Optional[str]:
    """Validate device name.

    :param self: not used
    :type self: Any
    :param value: value to be validated
    :type value: str
    :param userarg: not used
    :type userarg: Any
    """
    if not value.startswith("/dev/"):
        return "Device name should start with /dev"
    return None

def validate_or(self:Any,
                                 value: str,
                                 userarg: List[
                                            Tuple[
                                                Callable[...,Optional[str]],
                                                Any]]) -> Optional[str]:
    """Validate multiple conditions and return no error if at least one is satisfied.

    :param self: not used
    :type self: Any
    :param value: value to be validated
    :type value: str
    :param userarg: list of validation functions and their own user arguments
    :type userarg: List[Tuple[Callable[...,Optional[str]],Any]
    """
    total_message = []

    for validate_fn,fn_userarg in userarg:
        message = validate_fn(self, value, fn_userarg)
        if message is None:
            return None
        total_message.append(message)
    return " - ".join(total_message)

def validate_and(self:Any,
                                 value: str,
                                 userarg: List[
                                            Tuple[
                                                Callable[...,Optional[str]],
                                                Any]]) -> Optional[str]:
    """Validate multiple conditions and return no error if all of them are satisfied.

    :param self: not used
    :type self: Any
    :param value: value to be validated
    :type value: str
    :param userarg: list of validation functions and their own user arguments
    :type userarg: List[Tuple[Callable[...,Optional[str]],Any]
    """
    for validate_fn,fn_userarg in userarg:
        message = validate_fn(self, value, fn_userarg)
        if message is not None:
            return message
    return None

# pylint: disable=unused-argument
def validate_port(self: Any,
                       value: str,
                       userarg: Any) -> Optional[str]:
    """Check that value is a valid port name.

    :param self: not used
    :type self: Any
    :param value: value to be validated
    :type value: str
    :param userarg: not used
    :type userarg: Any
    """
    try:
        # number is a valid port entry
        portnumber=int(value)
    except ValueError:
        elements = value.split("/")

        if len(elements)==2:
            port,protocol=elements

            if protocol not in ["tcp","udp","sctp"]:
                return "Protocol should be tcp, udp or sctp."
            try:
                # number is a valid port entry
                portnumber=int(port)
            except ValueError:
                return "Invalid port number"
        else:
            return "Invalid port name, must be a port number or number/protocol(tcp,udp,sctp)."

    if portnumber < 0 or portnumber > 65535:
        return "Port number should be between 0 and 65535"
    return None

# pylint: disable=unused-argument
def validate_mount_info(self: Any,
                       value: str,
                       userarg: Any) -> Optional[str]:
    """Check that value is a mount point.

    Format for mount points is folder[,ro/rw]

    :param self: not used
    :type self: Any
    :param value: value to be validated
    :type value: str
    :param userarg: not used
    :type userarg: Any
    """
    path=value

    if "," in path:
        parts=path.split(",")
        if parts[-1] in ["ro","rw"]:
            path=",".join(parts[:-1])

    if validate_remote_path(self, path, userarg) is not None:
        return "Invalid mount point"

    return None

YAML_STRING = "{ type: string }"
YAML_BOOLEAN = "{ type: boolean }"
YAML_INTEGER = "{ type: integer }"
YAML_DICT = "{ type: object , additionalProperties: true }"

YAML_STRING_OR_LIST = "\
    oneOf:\n\
      - type: string\n\
      - type: array\n\
        items:\n\
            type: string\n\
        uniqueItems: true\n\
    "

YAML_LIST_OF_STRINGS = "\
    type: array\n\
    items:\n\
        type: string\n\
    uniqueItems: true\n\
    "

YAML_LIST_OR_DICT = "\
    oneOf:\n\
      - type: object\n\
        patternProperties:\n\
          .+:\n\
            type:\n\
              - string\n\
              - number\n\
              - 'null'\n\
        additionalProperties: false\n\
      - type: array\n\
        items:\n\
          type: string\n\
        uniqueItems: true\n\
    "

# pylint: disable=unused-argument
def validate_yaml(self: Any,
                       value: str,
                       userarg: Any) -> Optional[str]:
    """Check that value is a valid yaml string.

    :param self: not used
    :type self: Any
    :param value: value to be validated
    :type value: str
    :param userarg: not used
    :type userarg: Any
    """
    try:
        _ = yaml.full_load(value)
    except yaml.YAMLError as ex:
        return f"YAML parsing error: {str(ex)}"
    return None

# pylint: disable=unused-argument
def validate_yaml_schema(self: Any,
                       value: str,
                       userarg: Any) -> Optional[str]:
    """Check that value matches a schema.

    :param self: not used
    :type self: Any
    :param value: value to be validated
    :type value: str
    :param userarg: schema to be used for validation
    :type userarg: Any
    """
    try:
        document = yaml.full_load(value)
        schema = yaml.full_load(userarg)

        jsonschema.validate(document, schema)
    except yaml.YAMLError as ex:
        return f"YAML parsing error: {str(ex)}"
    except (jsonschema.ValidationError, jsonschema.SchemaError) as ex:
        return f"YAML validation error: {str(ex)}"
    return None

VALIDID_REGEXP = re.compile(r"^[a-zA-Z0-9_]+$")

# pylint: disable=unused-argument
def validate_id(self: Any,
                       value: str,
                       userarg: Any) -> Optional[str]:
    """Check that value is a string with only valid characters.

    :param self: not used
    :type self: Any
    :param value: value to be validated
    :type value: str
    :param userarg: not used
    :type userarg: Any
    """
    if not VALIDID_REGEXP.match(value):
        return "Value must use only alphanumerical characters and the underscore."
    return None

# pylint: disable=too-many-arguments
def validate_entry(self:Any,
                 dictionary: Dict[str,str],
                 key: str,
                 value: str,
                 newitem: bool,
                 userarg: Tuple[str, Callable[...,Optional[str]],Any]) -> Optional[str]:
    """Apply a validation function to a specific entry.

    :param self: not used
    :type self: Any
    :param dictionary: dictionary of unique keys
    :type dictionary: Dict[str,str]
    :param key: key to be validated
    :type key: str
    :param value: not used
    :type value: str
    :param newitem: True if the key is new, False if it is an existing key
    :type newitem: bool
    :param userarg: key name, function to be applied to the key and its argument
    :type userarg: Tuple[str, Callable[...,Optional[str]],Any]
    """
    keymatch, validation_fn, fn_arg = userarg

    if keymatch != key:
        return None

    return validation_fn(self, value, fn_arg)

DOCKER_COMMANDS = {
    "FROM",
    "RUN",
    "CMD",
    "LABEL",
    "EXPOSE",
    "ENV",
    "ADD",
    "COPY",
    "ENTRYPOINT",
    "VOLUME",
    "USER",
    "WORKDIR",
    "ARG",
    "ONBUILD",
    "STOPSIGNAL",
    "HEALTHCHECK",
    "SHELL"
}

def validate_docker_command(self: Any,
                            value: str,
                            userarg: Any) -> Optional[str]:
    """Check that value is a valid sequence of docker commands.

    :param self: not used
    :type self: Any
    :param value: value to be validated
    :type value: str
    :param userarg: not used
    :type userarg: Any
    """
    for line in value.splitlines():
        line=line.strip()
        if line.startswith("#"):
            continue

        if line.split(" ")[0].upper() not in DOCKER_COMMANDS:
            return "Not a valid docker command."

    return None

DEBIAN_PACKAGE_NAME_REGEXP = re.compile(r"^[a-z0-9][a-z0-9+-.]*$")

DEBIAN_ARCHITECTURES = {
    "amd64", "arm64", "armel", "armhf", "i386", "mips64el", "mipsel", "ppc64el", "s390x"
}

def validate_debian_package_list(self: Any,
                                 value: str,
                                 userarg: Any) -> Optional[str]:
    """Check that value is a valid list of debian packages.

    :param self: not used
    :type self: Any
    :param value: value to be validated
    :type value: str
    :param userarg: not used
    :type userarg: Any
    """
    for package in value.split(" "):
        package.strip()

        if len(package) == 0:
            continue

        packagename = package

        if ":" in package:
            parts = package.split(":")

            if len(parts) != 2:
                return f"{package} is not a valid package name (invalid characters)."

            packagename = parts[0]
            arch = parts[1]

            if not arch in DEBIAN_ARCHITECTURES:
                return f"{package} is not a valid package name (invalid architecture)."

        if not DEBIAN_PACKAGE_NAME_REGEXP.match(packagename):
            return f"{package} is not a valid package name (invalid characters)."

    return None


# skip functions

def skip_if_empty(self:Any,
                  value: str) -> bool:
    """Skip validation when value is empty.

    :param self: not used
    :type self: Any
    :param value: value to be validated
    :type value: str
    :param userarg: not used
    :type userarg: Any
    """
    if len(value) == 0:
        return True
    return False

def skip_if_contains_tags(self:Any,
                  value: str) -> bool:
    """Skip validation when value is empty.

    :param self: not used
    :type self: Any
    :param value: value to be validated
    :type value: str
    :param userarg: not used
    :type userarg: Any
    """
    if tags.TAG.match(value) is not None:
        return True
    return False
