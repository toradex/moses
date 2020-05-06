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

import { DockerContainerConfig } from './dockerContainerConfig';
import { DockerContainerState } from './dockerContainerState';
import { DockerGraphDriverData } from './dockerGraphDriverData';
import { DockerHostConfig } from './dockerHostConfig';
import { DockerMountPoint } from './dockerMountPoint';
import { DockerNetworkSettings } from './dockerNetworkSettings';

export class DockerContainer {
    /**
    * The ID of the container
    */
    'id'?: string;
    /**
    * The time the container was created
    */
    'created'?: string;
    /**
    * The path to the command being run
    */
    'path'?: string;
    /**
    * The arguments to the command being run
    */
    'args'?: Array<string>;
    'state'?: DockerContainerState;
    /**
    * The container\'s image
    */
    'image'?: string;
    'resolvConfPath'?: string;
    'hostnamePath'?: string;
    'hostsPath'?: string;
    'logPath'?: string;
    /**
    * TODO
    */
    'node'?: object;
    'name'?: string;
    'restartCount'?: number;
    'driver'?: string;
    'mountLabel'?: string;
    'processLabel'?: string;
    'appArmorProfile'?: string;
    'execIDs'?: Array<string>;
    'hostConfig'?: DockerHostConfig;
    'graphDriver'?: DockerGraphDriverData;
    /**
    * The size of files that have been created or changed by this container.
    */
    'sizeRw'?: number;
    /**
    * The total size of all the files in this container.
    */
    'sizeRootFs'?: number;
    'mounts'?: Array<DockerMountPoint>;
    'config'?: DockerContainerConfig;
    'networkSettings'?: DockerNetworkSettings;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "id",
            "baseName": "Id",
            "type": "string"
        },
        {
            "name": "created",
            "baseName": "Created",
            "type": "string"
        },
        {
            "name": "path",
            "baseName": "Path",
            "type": "string"
        },
        {
            "name": "args",
            "baseName": "Args",
            "type": "Array<string>"
        },
        {
            "name": "state",
            "baseName": "State",
            "type": "DockerContainerState"
        },
        {
            "name": "image",
            "baseName": "Image",
            "type": "string"
        },
        {
            "name": "resolvConfPath",
            "baseName": "ResolvConfPath",
            "type": "string"
        },
        {
            "name": "hostnamePath",
            "baseName": "HostnamePath",
            "type": "string"
        },
        {
            "name": "hostsPath",
            "baseName": "HostsPath",
            "type": "string"
        },
        {
            "name": "logPath",
            "baseName": "LogPath",
            "type": "string"
        },
        {
            "name": "node",
            "baseName": "Node",
            "type": "object"
        },
        {
            "name": "name",
            "baseName": "Name",
            "type": "string"
        },
        {
            "name": "restartCount",
            "baseName": "RestartCount",
            "type": "number"
        },
        {
            "name": "driver",
            "baseName": "Driver",
            "type": "string"
        },
        {
            "name": "mountLabel",
            "baseName": "MountLabel",
            "type": "string"
        },
        {
            "name": "processLabel",
            "baseName": "ProcessLabel",
            "type": "string"
        },
        {
            "name": "appArmorProfile",
            "baseName": "AppArmorProfile",
            "type": "string"
        },
        {
            "name": "execIDs",
            "baseName": "ExecIDs",
            "type": "Array<string>"
        },
        {
            "name": "hostConfig",
            "baseName": "HostConfig",
            "type": "DockerHostConfig"
        },
        {
            "name": "graphDriver",
            "baseName": "GraphDriver",
            "type": "DockerGraphDriverData"
        },
        {
            "name": "sizeRw",
            "baseName": "SizeRw",
            "type": "number"
        },
        {
            "name": "sizeRootFs",
            "baseName": "SizeRootFs",
            "type": "number"
        },
        {
            "name": "mounts",
            "baseName": "Mounts",
            "type": "Array<DockerMountPoint>"
        },
        {
            "name": "config",
            "baseName": "Config",
            "type": "DockerContainerConfig"
        },
        {
            "name": "networkSettings",
            "baseName": "NetworkSettings",
            "type": "DockerNetworkSettings"
        }    ];

    static getAttributeTypeMap() {
        return DockerContainer.attributeTypeMap;
    }
}

