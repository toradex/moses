/**
 * Torizon Deployment API
 * Toradex Development API to build and deploy application on Torizon
 *
 * The version of the OpenAPI document: 1.0.2
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


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

