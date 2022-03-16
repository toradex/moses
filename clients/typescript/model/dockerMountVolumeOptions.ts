/**
 * Torizon IDE-backend API
 * Toradex API to build and deploy applications running as containers on Torizon
 *
 * The version of the OpenAPI document: 1.1.6
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { RequestFile } from './models';
import { DockerMountVolumeOptionsDriverConfig } from './dockerMountVolumeOptionsDriverConfig';

/**
* Optional configuration for the `volume` type.
*/
export class DockerMountVolumeOptions {
    /**
    * Populate volume with data from the target.
    */
    'noCopy'?: boolean = false;
    /**
    * User-defined key/value metadata.
    */
    'labels'?: { [key: string]: string; };
    'driverConfig'?: DockerMountVolumeOptionsDriverConfig;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "noCopy",
            "baseName": "NoCopy",
            "type": "boolean"
        },
        {
            "name": "labels",
            "baseName": "Labels",
            "type": "{ [key: string]: string; }"
        },
        {
            "name": "driverConfig",
            "baseName": "DriverConfig",
            "type": "DockerMountVolumeOptionsDriverConfig"
        }    ];

    static getAttributeTypeMap() {
        return DockerMountVolumeOptions.attributeTypeMap;
    }
}

