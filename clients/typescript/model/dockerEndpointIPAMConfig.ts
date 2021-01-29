/**
 * Torizon IDE-backend API
 * Toradex API to build and deploy applications running as containers on Torizon
 *
 * The version of the OpenAPI document: 1.1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { RequestFile } from './models';

/**
* EndpointIPAMConfig represents an endpoint\'s IPAM configuration. 
*/
export class DockerEndpointIPAMConfig {
    'iPv4Address'?: string;
    'iPv6Address'?: string;
    'linkLocalIPs'?: Array<string>;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "iPv4Address",
            "baseName": "IPv4Address",
            "type": "string"
        },
        {
            "name": "iPv6Address",
            "baseName": "IPv6Address",
            "type": "string"
        },
        {
            "name": "linkLocalIPs",
            "baseName": "LinkLocalIPs",
            "type": "Array<string>"
        }    ];

    static getAttributeTypeMap() {
        return DockerEndpointIPAMConfig.attributeTypeMap;
    }
}

