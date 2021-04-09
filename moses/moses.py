#!python3
"""Main entry point and initialization of all global objects."""
import sys
import os
import argparse
import logging
import logging.handlers
from typing import Any
import requests
import connexion
import waitress
import yaml
from connexion.json_schema import Draft4RequestValidator
from flask import request
import api
import moses_exceptions
import targetdevice
import applicationconfig
import eula
import platformconfig

if getattr(sys, "frozen", False):
    options = {"swagger_path": os.path.dirname(sys.executable) + "/api/ui"}
else:
    from swagger_ui_bundle import swagger_ui_3_path
    options = {'swagger_path': swagger_ui_3_path}

app = connexion.App("moses", options=options)


@app.app.before_request
def log_rest_in() -> None:
    """Log API request."""
    logging.info("REST -> %s", request.path)


@app.app.after_request
def log_rest_out(response: Any) -> Any:
    """Log API request and its result.

    :param response: Flask response object

    """
    logging.info("REST <- %s - %d", request.path, response.status_code)
    return response


# If we're running in stand alone mode, run the application
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="backend for Toradex IDEs support")
    parser.add_argument(
        "--port",
        type=int,
        default=5000,
        choices=range(1, 65535),
        metavar="port used for REST server, range is 1..65535",
    )
    parser.add_argument("--logfile", type=str, default=None)
    parser.add_argument("--debug", action="store_true")

    args = parser.parse_args()

    if not args.debug:
        logging.basicConfig(level=logging.INFO)
        logging.getLogger("paramiko").setLevel(logging.WARNING)
    else:
        logging.basicConfig(level=logging.DEBUG)
        logging.getLogger("paramiko").setLevel(logging.DEBUG)

    if args.logfile is not None:
        logging.getLogger().addHandler(
            logging.handlers.RotatingFileHandler(
                args.logfile, "a", 1024 * 1024, 4)
        )

    # pylint: disable = broad-except
    try:
        proxies = {
            "http": None,
            "https": None,
        }

        r = requests.get(
            "http://localhost:" + str(args.port) + "/api/version", proxies=proxies
        )

        if r.status_code != 200:
            logging.error(
                f"Port {args.port} already used by an incompatible REST server."
            )
            sys.exit(-1)

        version = r.json()

        if (
            version["app_version"] != api.API_VERSION
            or version["api_version"] != api.API_VERSION
        ):
            logging.warning(
                "Running version does not match current version, this may be an issue."
            )
        else:
            logging.warning("back-end server already running.")

        sys.exit(0)
    except requests.exceptions.ConnectionError as exception:
        pass
    except Exception as exception:
        logging.exception(exception)

    with open("swagger.yaml", "r") as inp:
        schema = yaml.full_load(inp)

    targetdevice.TargetDevice.parse_schema(
        schema["definitions"]["TargetDevice"])
    applicationconfig.ApplicationConfig.parse_schema(
        schema["definitions"]["Application"]
    )
    eula.EULA.parse_schema(schema["definitions"]["Eula"])
    platformconfig.PlatformConfig.parse_schema(schema["definitions"]["Platform"])

    app.app.json_encoder = api.CustomJSONEncoder
    api.init_api()

    with open("swagger.yaml") as swagger_file:
        swagger_yaml = yaml.load(swagger_file, Loader=yaml.FullLoader)
        swagger_yaml["host"] = "localhost:" + str(args.port)

    app.add_api(swagger_yaml, resolver=api.ApiResolver())
    app.add_error_handler(
        moses_exceptions.MosesError,
        moses_exceptions.encode_error)
    app.add_error_handler(Exception, moses_exceptions.encode_exception)

    Draft4RequestValidator.VALIDATORS["readOnly"] = api.remove_readonly

    waitress.serve(app, host="127.0.0.1", port=args.port)
