/**
 * Torizon IDE-backend API
 * Toradex API to build and deploy applications running as containers on Torizon
 *
 * The version of the OpenAPI document: 1.1.6
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { RequestFile } from './models';

/**
* The logging configuration for this container
*/
export class DockerHostConfigAllOfLogConfig {
    'type'?: DockerHostConfigAllOfLogConfig.TypeEnum;
    'config'?: { [key: string]: string; };

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "type",
            "baseName": "Type",
            "type": "DockerHostConfigAllOfLogConfig.TypeEnum"
        },
        {
            "name": "config",
            "baseName": "Config",
            "type": "{ [key: string]: string; }"
        }    ];

    static getAttributeTypeMap() {
        return DockerHostConfigAllOfLogConfig.attributeTypeMap;
    }
}

export namespace DockerHostConfigAllOfLogConfig {
    export enum TypeEnum {
        JsonFile = <any> 'json-file',
        Syslog = <any> 'syslog',
        Journald = <any> 'journald',
        Gelf = <any> 'gelf',
        Fluentd = <any> 'fluentd',
        Awslogs = <any> 'awslogs',
        Splunk = <any> 'splunk',
        Etwlogs = <any> 'etwlogs',
        None = <any> 'none'
    }
}
