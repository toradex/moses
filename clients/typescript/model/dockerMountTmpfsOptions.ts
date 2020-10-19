/**
 * Torizon IDE-backend API
 * Toradex API to build and deploy applications running as containers on Torizon
 *
 * The version of the OpenAPI document: 1.0.10
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { RequestFile } from './models';

/**
* Optional configuration for the `tmpfs` type.
*/
export class DockerMountTmpfsOptions {
    /**
    * The size for the tmpfs mount in bytes.
    */
    'sizeBytes'?: number;
    /**
    * The permission mode for the tmpfs mount in an integer.
    */
    'mode'?: number;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "sizeBytes",
            "baseName": "SizeBytes",
            "type": "number"
        },
        {
            "name": "mode",
            "baseName": "Mode",
            "type": "number"
        }    ];

    static getAttributeTypeMap() {
        return DockerMountTmpfsOptions.attributeTypeMap;
    }
}

