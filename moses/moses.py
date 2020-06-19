#!python3

import sys
import os
import logging
import logging.handlers
import connexion
import api
import exceptions
import waitress
from flask import request
from connexion.json_schema import Draft4RequestValidator
import yaml
import targetdevice
import applicationconfig
import argparse
import requests
import paramiko

if getattr(sys, 'frozen', False):
    options = {'swagger_path': os.path.dirname(sys.executable) + '/api/ui'}
else:
    options = {}

app = connexion.App("moses", options=options)


@app.app.before_request
def log_rest_in():
    logging.info("REST -> %s", request.path)


@app.app.after_request
def log_rest_out(response):
    logging.info("REST <- %s - %d", request.path, response.status_code)
    return response


# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="backend for Toradex IDEs support")
    parser.add_argument("--port", type=int, default=5000,
                        choices=range(1, 65535), metavar="port used for REST server, range is 1..65535")
    parser.add_argument(
        "--logfile", type=str, default=None)
    parser.add_argument(
        "--debug", action="store_true")

    args = parser.parse_args()

    if not args.debug:
        logging.basicConfig(level=logging.INFO)
        logging.getLogger("paramiko").setLevel(logging.WARNING)
    else:
        logging.basicConfig(level=logging.DEBUG)
        logging.getLogger("paramiko").setLevel(logging.DEBUG)

    if args.logfile is not None:
        logging.getLogger().addHandler(
            logging.handlers.RotatingFileHandler(args.logfile, "a", 1024*1024, 4))

    try:
        proxies = {
            "http": None,
            "https": None,
        }

        r = requests.get("http://localhost:"+str(args.port) +
                         "/api/version", proxies=proxies)

        if r.status_code != 200:
            logging.error(
                "Port " + args.port + " already used by an incompatible REST server.")
            sys.exit(-1)

        version = r.json()

        if version["app_version"] != api.API_VERSION or version["api_version"] != api.API_VERSION:
            logging.warning(
                "Running version does not match current version, this may be an issue.")
        else:
            logging.warning(
                "back-end server already running.")

        sys.exit(0)

    except requests.exceptions.ConnectionError as e:
        pass
    except Exception as e:
        logging.exception()

    with open("swagger.yaml", "r") as inp:
        schema = yaml.full_load(inp)

    targetdevice.TargetDevice.parse_schema(
        schema["definitions"]["TargetDevice"])
    applicationconfig.ApplicationConfig.parse_schema(
        schema["definitions"]["Application"])

    app.app.json_encoder = api.CustomJSONEncoder
    api.init_api()
    app.add_api("swagger.yaml", resolver=api.ApiResolver())
    app.add_error_handler(exceptions.MosesError, exceptions.encode_error)
    app.add_error_handler(Exception, exceptions.encode_exception)

    Draft4RequestValidator.VALIDATORS["readOnly"] = api.remove_readonly

    waitress.serve(app, host='127.0.0.1', port=args.port)
