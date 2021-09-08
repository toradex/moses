/**
 * Torizon IDE-backend API
 * Toradex API to build and deploy applications running as containers on Torizon
 *
 * The version of the OpenAPI document: 1.1.3
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { RequestFile } from './models';

/**
* Map of driver specific options
*/
export class DockerMountVolumeOptionsDriverConfig {
    /**
    * Name of the driver to use to create the volume.
    */
    'name'?: string;
    /**
    * key/value map of driver specific options.
    */
    'options'?: { [key: string]: string; };

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "name",
            "baseName": "Name",
            "type": "string"
        },
        {
            "name": "options",
            "baseName": "Options",
            "type": "{ [key: string]: string; }"
        }    ];

    static getAttributeTypeMap() {
        return DockerMountVolumeOptionsDriverConfig.attributeTypeMap;
    }
}

