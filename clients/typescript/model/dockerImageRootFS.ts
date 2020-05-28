/**
 * Torizon Deployment API
 * Toradex Development API to build and deploy application on Torizon
 *
 * The version of the OpenAPI document: 1.0.4
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


export class DockerImageRootFS {
    'type': string;
    'layers'?: Array<string>;
    'baseLayer'?: string;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "type",
            "baseName": "Type",
            "type": "string"
        },
        {
            "name": "layers",
            "baseName": "Layers",
            "type": "Array<string>"
        },
        {
            "name": "baseLayer",
            "baseName": "BaseLayer",
            "type": "string"
        }    ];

    static getAttributeTypeMap() {
        return DockerImageRootFS.attributeTypeMap;
    }
}

