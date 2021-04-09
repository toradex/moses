/**
 * Torizon IDE-backend API
 * Toradex API to build and deploy applications running as containers on Torizon
 *
 * The version of the OpenAPI document: 1.1.1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { RequestFile } from './models';

export class Application {
    /**
    * Unique id
    */
    'id'?: string;
    /**
    * id of the platform used to generate this application configuration
    */
    'platformid'?: string;
    /**
    * folder where application configuration and extra files are stored
    */
    'folder'?: string;
    /**
    * Custom application properties
    */
    'props'?: { [key: string]: { [key: string]: string; }; };
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
    * Local folders to be mounted \"A mount points inside a container
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
    'extraparms'?: { [key: string]: { [key: string]: string; }; };
    /**
    * user account used to run the application inside the container
    */
    'username'?: string;
    /**
    * SHA-ids of the debug and release images
    */
    'images'?: { [key: string]: string; };
    /**
    * SHA-ids of the debug and release SDK images
    */
    'sdkimages'?: { [key: string]: string; };
    /**
    * unique tag used for the images
    */
    'imagetags'?: { [key: string]: string; };
    /**
    * unique tag used for the SDK images (if application uses an SDK)
    */
    'sdkimagetags'?: { [key: string]: string; };

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "id",
            "baseName": "id",
            "type": "string"
        },
        {
            "name": "platformid",
            "baseName": "platformid",
            "type": "string"
        },
        {
            "name": "folder",
            "baseName": "folder",
            "type": "string"
        },
        {
            "name": "props",
            "baseName": "props",
            "type": "{ [key: string]: { [key: string]: string; }; }"
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
            "type": "{ [key: string]: { [key: string]: string; }; }"
        },
        {
            "name": "username",
            "baseName": "username",
            "type": "string"
        },
        {
            "name": "images",
            "baseName": "images",
            "type": "{ [key: string]: string; }"
        },
        {
            "name": "sdkimages",
            "baseName": "sdkimages",
            "type": "{ [key: string]: string; }"
        },
        {
            "name": "imagetags",
            "baseName": "imagetags",
            "type": "{ [key: string]: string; }"
        },
        {
            "name": "sdkimagetags",
            "baseName": "sdkimagetags",
            "type": "{ [key: string]: string; }"
        }    ];

    static getAttributeTypeMap() {
        return Application.attributeTypeMap;
    }
}

