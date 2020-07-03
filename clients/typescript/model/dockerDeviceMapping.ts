/**
 * Torizon IDE-backend API
 * Toradex API to build and deploy applications running as containers on Torizon
 *
 * The version of the OpenAPI document: 1.0.5
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


/**
* A device mapping between the host and container
*/
export class DockerDeviceMapping {
    'pathOnHost'?: string;
    'pathInContainer'?: string;
    'cgroupPermissions'?: string;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "pathOnHost",
            "baseName": "PathOnHost",
            "type": "string"
        },
        {
            "name": "pathInContainer",
            "baseName": "PathInContainer",
            "type": "string"
        },
        {
            "name": "cgroupPermissions",
            "baseName": "CgroupPermissions",
            "type": "string"
        }    ];

    static getAttributeTypeMap() {
        return DockerDeviceMapping.attributeTypeMap;
    }
}

