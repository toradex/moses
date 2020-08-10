/**
 * Torizon IDE-backend API
 * Toradex API to build and deploy applications running as containers on Torizon
 *
 * The version of the OpenAPI document: 1.0.7
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { RequestFile } from '../api';
import { DockerHealthConfig } from './dockerHealthConfig';

/**
* Configuration for a container that is portable between hosts
*/
export class DockerContainerConfig {
    /**
    * The hostname to use for the container, as a valid RFC 1123 hostname.
    */
    'hostname'?: string;
    /**
    * The domain name to use for the container.
    */
    'domainname'?: string;
    /**
    * The user that commands are run as inside the container.
    */
    'user'?: string;
    /**
    * Whether to attach to `stdin`.
    */
    'attachStdin'?: boolean;
    /**
    * Whether to attach to `stdout`.
    */
    'attachStdout'?: boolean;
    /**
    * Whether to attach to `stderr`.
    */
    'attachStderr'?: boolean;
    /**
    * An object mapping ports to an empty object in the form:  `{\"<port>/<tcp|udp|sctp>\": {}}` 
    */
    'exposedPorts'?: { [key: string]: object; };
    /**
    * Attach standard streams to a TTY, including `stdin` if it is not closed.
    */
    'tty'?: boolean;
    /**
    * Open `stdin`
    */
    'openStdin'?: boolean;
    /**
    * Close `stdin` after one attached client disconnects
    */
    'stdinOnce'?: boolean;
    /**
    * A list of environment variables to set inside the container in the form `[\"VAR=value\", ...]`. A variable without `=` is removed from the environment, rather than to have an empty value. 
    */
    'env'?: Array<string>;
    /**
    * Command to run specified as a string or an array of strings.
    */
    'cmd'?: Array<string>;
    'healthcheck'?: DockerHealthConfig;
    /**
    * Command is already escaped (Windows only)
    */
    'argsEscaped'?: boolean;
    /**
    * The name of the image to use when creating the container
    */
    'image'?: string;
    /**
    * An object mapping mount point paths inside the container to empty objects.
    */
    'volumes'?: { [key: string]: object; };
    /**
    * The working directory for commands to run in.
    */
    'workingDir'?: string;
    /**
    * The entry point for the container as a string or an array of strings.  If the array consists of exactly one empty string (`[\"\"]`) then the entry point is reset to system default (i.e., the entry point used by docker when there is no `ENTRYPOINT` instruction in the `Dockerfile`). 
    */
    'entrypoint'?: Array<string>;
    /**
    * Disable networking for the container.
    */
    'networkDisabled'?: boolean;
    /**
    * MAC address of the container.
    */
    'macAddress'?: string;
    /**
    * `ONBUILD` metadata that were defined in the image\'s `Dockerfile`.
    */
    'onBuild'?: Array<string>;
    /**
    * User-defined key/value metadata.
    */
    'labels'?: { [key: string]: string; };
    /**
    * Signal to stop a container as a string or unsigned integer.
    */
    'stopSignal'?: string;
    /**
    * Timeout to stop a container in seconds.
    */
    'stopTimeout'?: number;
    /**
    * Shell for when `RUN`, `CMD`, and `ENTRYPOINT` uses a shell.
    */
    'shell'?: Array<string>;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "hostname",
            "baseName": "Hostname",
            "type": "string"
        },
        {
            "name": "domainname",
            "baseName": "Domainname",
            "type": "string"
        },
        {
            "name": "user",
            "baseName": "User",
            "type": "string"
        },
        {
            "name": "attachStdin",
            "baseName": "AttachStdin",
            "type": "boolean"
        },
        {
            "name": "attachStdout",
            "baseName": "AttachStdout",
            "type": "boolean"
        },
        {
            "name": "attachStderr",
            "baseName": "AttachStderr",
            "type": "boolean"
        },
        {
            "name": "exposedPorts",
            "baseName": "ExposedPorts",
            "type": "{ [key: string]: object; }"
        },
        {
            "name": "tty",
            "baseName": "Tty",
            "type": "boolean"
        },
        {
            "name": "openStdin",
            "baseName": "OpenStdin",
            "type": "boolean"
        },
        {
            "name": "stdinOnce",
            "baseName": "StdinOnce",
            "type": "boolean"
        },
        {
            "name": "env",
            "baseName": "Env",
            "type": "Array<string>"
        },
        {
            "name": "cmd",
            "baseName": "Cmd",
            "type": "Array<string>"
        },
        {
            "name": "healthcheck",
            "baseName": "Healthcheck",
            "type": "DockerHealthConfig"
        },
        {
            "name": "argsEscaped",
            "baseName": "ArgsEscaped",
            "type": "boolean"
        },
        {
            "name": "image",
            "baseName": "Image",
            "type": "string"
        },
        {
            "name": "volumes",
            "baseName": "Volumes",
            "type": "{ [key: string]: object; }"
        },
        {
            "name": "workingDir",
            "baseName": "WorkingDir",
            "type": "string"
        },
        {
            "name": "entrypoint",
            "baseName": "Entrypoint",
            "type": "Array<string>"
        },
        {
            "name": "networkDisabled",
            "baseName": "NetworkDisabled",
            "type": "boolean"
        },
        {
            "name": "macAddress",
            "baseName": "MacAddress",
            "type": "string"
        },
        {
            "name": "onBuild",
            "baseName": "OnBuild",
            "type": "Array<string>"
        },
        {
            "name": "labels",
            "baseName": "Labels",
            "type": "{ [key: string]: string; }"
        },
        {
            "name": "stopSignal",
            "baseName": "StopSignal",
            "type": "string"
        },
        {
            "name": "stopTimeout",
            "baseName": "StopTimeout",
            "type": "number"
        },
        {
            "name": "shell",
            "baseName": "Shell",
            "type": "Array<string>"
        }    ];

    static getAttributeTypeMap() {
        return DockerContainerConfig.attributeTypeMap;
    }
}

