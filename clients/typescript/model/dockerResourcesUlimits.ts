/**
 * Torizon IDE-backend API
 * Toradex API to build and deploy applications running as containers on Torizon
 *
 * The version of the OpenAPI document: 1.0.8
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { RequestFile } from './models';

export class DockerResourcesUlimits {
    /**
    * Name of ulimit
    */
    'name'?: string;
    /**
    * Soft limit
    */
    'soft'?: number;
    /**
    * Hard limit
    */
    'hard'?: number;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "name",
            "baseName": "Name",
            "type": "string"
        },
        {
            "name": "soft",
            "baseName": "Soft",
            "type": "number"
        },
        {
            "name": "hard",
            "baseName": "Hard",
            "type": "number"
        }    ];

    static getAttributeTypeMap() {
        return DockerResourcesUlimits.attributeTypeMap;
    }
}

