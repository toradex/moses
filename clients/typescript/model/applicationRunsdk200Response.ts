/**
 * Torizon IDE-backend API
 * Toradex API to build and deploy applications running as containers on Torizon
 *
 * The version of the OpenAPI document: 1.1.7
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { RequestFile } from './models';

export class ApplicationRunsdk200Response {
    /**
    * The IP address for local container instance
    */
    'hostIp'?: string;
    /**
    * port used for SSH
    */
    'hostPort'?: string;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "hostIp",
            "baseName": "HostIp",
            "type": "string"
        },
        {
            "name": "hostPort",
            "baseName": "HostPort",
            "type": "string"
        }    ];

    static getAttributeTypeMap() {
        return ApplicationRunsdk200Response.attributeTypeMap;
    }
}

