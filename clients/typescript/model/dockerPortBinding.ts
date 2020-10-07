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

/**
* PortBinding represents a binding between a host IP address and a host port. 
*/
export class DockerPortBinding {
    /**
    * Host IP address that the container\'s port is mapped to.
    */
    'hostIp'?: string;
    /**
    * Host port number that the container\'s port is mapped to.
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
        return DockerPortBinding.attributeTypeMap;
    }
}

