/**
 * Torizon IDE-backend API
 * Toradex API to build and deploy applications running as containers on Torizon
 *
 * The version of the OpenAPI document: 1.1.1
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { RequestFile } from './models';

/**
* Optional configuration for the `bind` type.
*/
export class DockerMountBindOptions {
    /**
    * A propagation mode with the value `[r]private`, `[r]shared`, or `[r]slave`.
    */
    'propagation'?: DockerMountBindOptions.PropagationEnum;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "propagation",
            "baseName": "Propagation",
            "type": "DockerMountBindOptions.PropagationEnum"
        }    ];

    static getAttributeTypeMap() {
        return DockerMountBindOptions.attributeTypeMap;
    }
}

export namespace DockerMountBindOptions {
    export enum PropagationEnum {
        Private = <any> 'private',
        Rprivate = <any> 'rprivate',
        Shared = <any> 'shared',
        Rshared = <any> 'rshared',
        Slave = <any> 'slave',
        Rslave = <any> 'rslave'
    }
}
