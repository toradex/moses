/**
 * Torizon IDE-backend API
 * Toradex API to build and deploy applications running as containers on Torizon
 *
 * The version of the OpenAPI document: 1.0.13
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { RequestFile } from './models';

export class Platform {
    /**
    * Unique name (should be filesystem-compatible)
    */
    'id'?: string;
    /**
    * Platform mnemnonic name
    */
    'name'?: string;
    /**
    * true if the platform is provided by Toradex and can\'t be modified
    */
    'standard'?: boolean;
    /**
    * Version of the image (not related to distro version)
    */
    'version'?: string;
    /**
    * runtimes/languages supported by the container
    */
    'runtimes'?: Array<string>;
    /**
    * ssh user supported by the SDK container
    */
    'sdkcontainerusername'?: string;
    /**
    * password used to ssh inside the SDK container
    */
    'sdkcontainerpassword'?: string;
    /**
    * path of docker-compose file to be used to start additional containers needed by the app
    */
    'dockercomposefile'?: { [key: string]: string; };
    /**
    * path of script to be run when application debugging starts
    */
    'startupscript'?: { [key: string]: string; };
    /**
    * path of script to be run when application debugging stops
    */
    'shutdownscript'?: { [key: string]: string; };
    /**
    * ports to be exposed from the container
    */
    'ports'?: { [key: string]: { [key: string]: string; }; };
    /**
    * Local folders to be mounted as mount points inside a container
    */
    'volumes'?: { [key: string]: { [key: string]: string; }; };
    /**
    * Additional devices to be shared inside container
    */
    'devices'?: { [key: string]: Array<string>; };
    /**
    * Networks used by container (in debug it will always be also on bridge)
    */
    'networks'?: { [key: string]: Array<string>; };
    /**
    * Additional parameter passed to the run call (check docker SDK for python for reference, value is YAML)
    */
    'extraparms'?: { [key: string]: { [key: string]: object; }; };
    /**
    * Custom properties (may be used in dockerfile or by extensions)
    */
    'props'?: { [key: string]: { [key: string]: string; }; };
    /**
    * Platform human-readable description
    */
    'description'?: string;
    /**
    * strings used to identify specific properties of the platform
    */
    'tags'?: Array<string>;
    /**
    * architecture as defined by docker
    */
    'architecture'?: string;
    /**
    * true for platforms that are no longer supported
    */
    'deprecated'?: boolean;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "id",
            "baseName": "id",
            "type": "string"
        },
        {
            "name": "name",
            "baseName": "name",
            "type": "string"
        },
        {
            "name": "standard",
            "baseName": "standard",
            "type": "boolean"
        },
        {
            "name": "version",
            "baseName": "version",
            "type": "string"
        },
        {
            "name": "runtimes",
            "baseName": "runtimes",
            "type": "Array<string>"
        },
        {
            "name": "sdkcontainerusername",
            "baseName": "sdkcontainerusername",
            "type": "string"
        },
        {
            "name": "sdkcontainerpassword",
            "baseName": "sdkcontainerpassword",
            "type": "string"
        },
        {
            "name": "dockercomposefile",
            "baseName": "dockercomposefile",
            "type": "{ [key: string]: string; }"
        },
        {
            "name": "startupscript",
            "baseName": "startupscript",
            "type": "{ [key: string]: string; }"
        },
        {
            "name": "shutdownscript",
            "baseName": "shutdownscript",
            "type": "{ [key: string]: string; }"
        },
        {
            "name": "ports",
            "baseName": "ports",
            "type": "{ [key: string]: { [key: string]: string; }; }"
        },
        {
            "name": "volumes",
            "baseName": "volumes",
            "type": "{ [key: string]: { [key: string]: string; }; }"
        },
        {
            "name": "devices",
            "baseName": "devices",
            "type": "{ [key: string]: Array<string>; }"
        },
        {
            "name": "networks",
            "baseName": "networks",
            "type": "{ [key: string]: Array<string>; }"
        },
        {
            "name": "extraparms",
            "baseName": "extraparms",
            "type": "{ [key: string]: { [key: string]: object; }; }"
        },
        {
            "name": "props",
            "baseName": "props",
            "type": "{ [key: string]: { [key: string]: string; }; }"
        },
        {
            "name": "description",
            "baseName": "description",
            "type": "string"
        },
        {
            "name": "tags",
            "baseName": "tags",
            "type": "Array<string>"
        },
        {
            "name": "architecture",
            "baseName": "architecture",
            "type": "string"
        },
        {
            "name": "deprecated",
            "baseName": "deprecated",
            "type": "boolean"
        }    ];

    static getAttributeTypeMap() {
        return Platform.attributeTypeMap;
    }
}

