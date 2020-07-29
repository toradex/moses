/**
 * Torizon IDE-backend API
 * Toradex API to build and deploy applications running as containers on Torizon
 *
 * The version of the OpenAPI document: 1.0.6
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { RequestFile } from '../api';

export class MountPoint {
    /**
    * mount point
    */
    'mountpoint'?: string;
    /**
    * file system
    */
    'filesystem'?: string;
    /**
    * total size in 1Kb blocks
    */
    'size'?: number;
    /**
    * available space in 1kb blocks
    */
    'available'?: number;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "mountpoint",
            "baseName": "mountpoint",
            "type": "string"
        },
        {
            "name": "filesystem",
            "baseName": "filesystem",
            "type": "string"
        },
        {
            "name": "size",
            "baseName": "size",
            "type": "number"
        },
        {
            "name": "available",
            "baseName": "available",
            "type": "number"
        }    ];

    static getAttributeTypeMap() {
        return MountPoint.attributeTypeMap;
    }
}

