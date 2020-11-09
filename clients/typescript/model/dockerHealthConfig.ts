/**
 * Torizon IDE-backend API
 * Toradex API to build and deploy applications running as containers on Torizon
 *
 * The version of the OpenAPI document: 1.0.11
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { RequestFile } from './models';

/**
* A test to perform to check that the container is healthy.
*/
export class DockerHealthConfig {
    /**
    * The test to perform. Possible values are:  - `[]` inherit healthcheck from image or parent image - `[\"NONE\"]` disable healthcheck - `[\"CMD\", args...]` exec arguments directly - `[\"CMD-SHELL\", command]` run command with system\'s default shell 
    */
    'test'?: Array<string>;
    /**
    * The time to wait between checks in nanoseconds. It should be 0 or at least 1000000 (1 ms). 0 means inherit.
    */
    'interval'?: number;
    /**
    * The time to wait before considering the check to have hung. It should be 0 or at least 1000000 (1 ms). 0 means inherit.
    */
    'timeout'?: number;
    /**
    * The number of consecutive failures needed to consider a container as unhealthy. 0 means inherit.
    */
    'retries'?: number;
    /**
    * Start period for the container to initialize before starting health-retries countdown in nanoseconds. It should be 0 or at least 1000000 (1 ms). 0 means inherit.
    */
    'startPeriod'?: number;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "test",
            "baseName": "Test",
            "type": "Array<string>"
        },
        {
            "name": "interval",
            "baseName": "Interval",
            "type": "number"
        },
        {
            "name": "timeout",
            "baseName": "Timeout",
            "type": "number"
        },
        {
            "name": "retries",
            "baseName": "Retries",
            "type": "number"
        },
        {
            "name": "startPeriod",
            "baseName": "StartPeriod",
            "type": "number"
        }    ];

    static getAttributeTypeMap() {
        return DockerHealthConfig.attributeTypeMap;
    }
}

