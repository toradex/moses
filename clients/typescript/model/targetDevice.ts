/**
 * Torizon IDE-backend API
 * Toradex API to build and deploy applications running as containers on Torizon
 *
 * The version of the OpenAPI document: 1.0.9
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { RequestFile } from '../api';

export class TargetDevice {
    /**
    * Unique serial number
    */
    'id'?: string;
    /**
    * Device mnemnonic name
    */
    'name'?: string;
    /**
    * Device hardware ID
    */
    'model'?: string;
    /**
    * Device hardware revision
    */
    'hwrev'?: string;
    /**
    * Kernel name
    */
    'kernelversion'?: string;
    /**
    * Kernel release
    */
    'kernelrelease'?: string;
    /**
    * Torizon version (date)
    */
    'distroversion'?: string;
    /**
    * Device host name
    */
    'hostname'?: string;
    /**
    * User account used to connect to device via ssh
    */
    'username'?: string;
    /**
    * Home folder of ssh user (used to deploy files and apps, can be different from actual home)
    */
    'homefolder'?: string;
    /**
    * True for a target device that is a community device, false for default Toradex devices
    */
    'runningtorizon'?: boolean;

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
            "name": "model",
            "baseName": "model",
            "type": "string"
        },
        {
            "name": "hwrev",
            "baseName": "hwrev",
            "type": "string"
        },
        {
            "name": "kernelversion",
            "baseName": "kernelversion",
            "type": "string"
        },
        {
            "name": "kernelrelease",
            "baseName": "kernelrelease",
            "type": "string"
        },
        {
            "name": "distroversion",
            "baseName": "distroversion",
            "type": "string"
        },
        {
            "name": "hostname",
            "baseName": "hostname",
            "type": "string"
        },
        {
            "name": "username",
            "baseName": "username",
            "type": "string"
        },
        {
            "name": "homefolder",
            "baseName": "homefolder",
            "type": "string"
        },
        {
            "name": "runningtorizon",
            "baseName": "runningtorizon",
            "type": "boolean"
        }    ];

    static getAttributeTypeMap() {
        return TargetDevice.attributeTypeMap;
    }
}

