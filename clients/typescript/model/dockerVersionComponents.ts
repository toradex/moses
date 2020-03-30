/**
 * Torizon Deployment API
 * Toradex Development API to build and deploy application on Torizon
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


export class DockerVersionComponents {
    'name': string;
    'version': string;
    'details'?: object;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "name",
            "baseName": "Name",
            "type": "string"
        },
        {
            "name": "version",
            "baseName": "Version",
            "type": "string"
        },
        {
            "name": "details",
            "baseName": "Details",
            "type": "object"
        }    ];

    static getAttributeTypeMap() {
        return DockerVersionComponents.attributeTypeMap;
    }
}

