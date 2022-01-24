/**
 * Torizon IDE-backend API
 * Toradex API to build and deploy applications running as containers on Torizon
 *
 * The version of the OpenAPI document: 1.1.5
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { RequestFile } from './models';

export class DockerResourcesBlkioWeightDevice {
    'path'?: string;
    'weight'?: number;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "path",
            "baseName": "Path",
            "type": "string"
        },
        {
            "name": "weight",
            "baseName": "Weight",
            "type": "number"
        }    ];

    static getAttributeTypeMap() {
        return DockerResourcesBlkioWeightDevice.attributeTypeMap;
    }
}

