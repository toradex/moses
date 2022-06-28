/**
 * Torizon IDE-backend API
 * Toradex API to build and deploy applications running as containers on Torizon
 *
 * The version of the OpenAPI document: 1.1.7
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { RequestFile } from './models';
import { DockerVersionComponentsInner } from './dockerVersionComponentsInner';
import { DockerVersionPlatform } from './dockerVersionPlatform';

/**
* Information about docker version
*/
export class DockerVersion {
    'platform'?: DockerVersionPlatform;
    'components'?: Array<DockerVersionComponentsInner>;
    'version'?: string;
    'apiVersion'?: string;
    'minAPIVersion'?: string;
    'gitCommit'?: string;
    'goVersion'?: string;
    'os'?: string;
    'arch'?: string;
    'kernelVersion'?: string;
    'experimental'?: boolean;
    'buildTime'?: string;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "platform",
            "baseName": "Platform",
            "type": "DockerVersionPlatform"
        },
        {
            "name": "components",
            "baseName": "Components",
            "type": "Array<DockerVersionComponentsInner>"
        },
        {
            "name": "version",
            "baseName": "Version",
            "type": "string"
        },
        {
            "name": "apiVersion",
            "baseName": "ApiVersion",
            "type": "string"
        },
        {
            "name": "minAPIVersion",
            "baseName": "MinAPIVersion",
            "type": "string"
        },
        {
            "name": "gitCommit",
            "baseName": "GitCommit",
            "type": "string"
        },
        {
            "name": "goVersion",
            "baseName": "GoVersion",
            "type": "string"
        },
        {
            "name": "os",
            "baseName": "Os",
            "type": "string"
        },
        {
            "name": "arch",
            "baseName": "Arch",
            "type": "string"
        },
        {
            "name": "kernelVersion",
            "baseName": "KernelVersion",
            "type": "string"
        },
        {
            "name": "experimental",
            "baseName": "Experimental",
            "type": "boolean"
        },
        {
            "name": "buildTime",
            "baseName": "BuildTime",
            "type": "string"
        }    ];

    static getAttributeTypeMap() {
        return DockerVersion.attributeTypeMap;
    }
}

