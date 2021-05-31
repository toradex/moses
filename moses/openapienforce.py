"""Functions used to clean object that should be returned via openapi REST calls."""
import copy
from typing import Any, Dict

# pylint: disable=global-statement

_API_SCHEMA : Dict[str,Any] = {}

def _deref_schema_element(element: dict, schema: dict) -> bool:
    """Replace the $ref entries with actual content.

    :param element: element that need to be "dereferenced"
    :type element: dict
    :param schema: whole schema
    :type schema: dict
    :return: true if the object has been changed
    :rtype: bool
    """
    for key,value in element.items():
        if key=="$ref":
            path=value.split("/")
            obj=schema
            for level in path[1:]:
                obj=obj[level]
            del element[key]
            element.update(copy.deepcopy(obj))
            return True
        if isinstance(value,dict):
            if _deref_schema_element(value,schema):
                return True
        if isinstance(value,list):
            for item in value:
                if isinstance(item,dict):
                    if _deref_schema_element(item,schema):
                        return True
    return False

def _deref_schema(schema: dict) -> None:
    """Replace $ref entries in the schema to make it usable directly.

    :param schema: schema from swagger.yaml
    :type schema: dict
    """
    while _deref_schema_element(schema,schema):
        pass

def denullify(obj: dict) -> dict :
    """Convert null values into empty strings since openAPI does not support nulls.

    replacement is done in-place, object is returned just for convenience

    :param obj: object to be processed
    :type obj: dict
    :return: object with all None values replaced with empty strings
    :rtype: dict
    """
    for key, value in obj.items():
        if value is None:
            obj[key]=""
        if isinstance(value,dict):
            denullify(value)
    return obj

def _null_value(typename: str) -> Any:
    """Return empty/null value depending on data type.

    :param typename: type as defined in openAPI
    :type typename: str
    :rtype: Any
    """
    if typename == "string":
        return ""
    if typename == "array":
        return []
    if typename == "object":
        return {}
    if typename == "boolean":
        return False
    if typename == "integer":
        return 0
    raise Exception("Object value can't be null")

def normalize_value(value: Any, typeinfo: dict) -> Any:
    """Check if value is openAPI complaint and replaces it if it isn't.

    :param value: initial value
    :type value: Any
    :param typeinfo: schema node that describes the expected object
    :type typeinfo: dict
    :return: object compatible with openAPI definition
    :rtype: Any
    """
    typestr=typeinfo["type"]
    if value is None and ("x-nullable" not in typeinfo or not typeinfo["x-nullable"]):
        return _null_value(typestr)
    if typestr == "object":
        return normalize_object(value,typeinfo)
    if typestr == "array":
        if typeinfo["items"]["type"] == "object":
            return _normalize_object_array(value,typeinfo["items"])
        return value
    return value


def normalize_object(obj: dict, typedef: dict) -> dict :
    """Replace all non-nullable fields with empty values.

    Remove also all fields not explicitely defined in the openAPI definition file.

    :param value: initial value
    :type value: Any
    :param typeinfo: schema node that describes the expected object
    :type typeinfo: dict
    :return: object compatible with openAPI definition
    :rtype: Any
    """
    if obj is None:
        return {}

    retval : Dict[str, Any]={}

    if "additionalProperties" in typedef:
        for key, value in obj.items():
            typeinfo=typedef["additionalProperties"]
            retval[key] = normalize_value(value,typeinfo)
    else:
        if not "properties" in typedef:
            return retval

        for key, value in obj.items():

            if not key in typedef["properties"]:
                continue

            typeinfo=typedef["properties"][key]

            # we have to merge all the properties into a single typeinfo object
            if "allOf" in typeinfo:
                typeinfo["properties"] = {}
                typeinfo["type"] = "object"

                for subtype in typeinfo["allOf"]:
                    typeinfo["properties"].update(subtype["properties"])

            retval[key]=normalize_value(value,typeinfo)

        for key,typeinfo in typedef["properties"].items():
            if key in retval:
                continue

            retval[key]=normalize_value(None,typeinfo)

    return retval

def _normalize_object_array(array:list,typedef:dict) -> list:
    if array is None:
        return []

    retval:list=[]

    for item in array:
        if isinstance(item,dict):
            retval.append(normalize_object(item,typedef))
        else:
            retval.append(normalize_object(vars(item),typedef))

    return retval

def normalize_object_from_type(obj: Any, typename:str) -> dict:
    """Conforms an object to its openAPI definition.

    :param obj: object to be checked
    :type obj: Any
    :param typename: type of the object in the openAPI schema
    :type typename: str
    :return: openAPI compliant version of the object
    :rtype: dict
    """
    global _API_SCHEMA
    if isinstance(obj,dict):
        return normalize_object(obj,_API_SCHEMA["definitions"][typename])
    return normalize_object(vars(obj),_API_SCHEMA["definitions"][typename])

def normalize_array_from_type(array: list, typename:str) -> list:
    """Conform all the elements of the array to the specified openAPI type.

    :param array: object array
    :type array: list
    :param typename: type of the object in the openAPI schema
    :type typename: str
    :return: array with openAPI compliant objects
    :rtype: list
    """
    global _API_SCHEMA
    return _normalize_object_array(array,_API_SCHEMA["definitions"][typename])

def init_openapi_enforce(schema: Dict[str,Any]) -> None:
    """Initialize the functions used to enforce openAPI compliance.

    :param schema: contents of swagger.YAML
    :type schema: Any
    """
    global _API_SCHEMA

    _API_SCHEMA = copy.deepcopy(schema)
    _deref_schema(_API_SCHEMA)
