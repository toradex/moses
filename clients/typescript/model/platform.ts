/**
 * Torizon Deployment API
 * Toradex Development API to build and deploy application on Torizon
 *
 * The version of the OpenAPI document: 1.0.4
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


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
    'runtimes'?: Array<string>;
    'sdkcontainerusername'?: string;
    'sdkcontainerpassword'?: string;
    'dockercomposefile'?: { [key: string]: string; };
    'startupscript'?: { [key: string]: string; };
    'shutdownscript'?: { [key: string]: string; };
    'ports'?: { [key: string]: { [key: string]: string; }; };
    'volumes'?: { [key: string]: { [key: string]: string; }; };
    'devices'?: { [key: string]: Array<string>; };
    'networks'?: { [key: string]: Array<string>; };
    'extraparms'?: { [key: string]: { [key: string]: object; }; };
    'props'?: { [key: string]: { [key: string]: string; }; };
    /**
    * Platform human-readable description
    */
    'description'?: string;

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
        }    ];

    static getAttributeTypeMap() {
        return Platform.attributeTypeMap;
    }
}

