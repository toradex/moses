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


export class DockerImageMetadata {
    'lastTagTime'?: string;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "lastTagTime",
            "baseName": "LastTagTime",
            "type": "string"
        }    ];

    static getAttributeTypeMap() {
        return DockerImageMetadata.attributeTypeMap;
    }
}

