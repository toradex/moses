export * from './application';
export * from './dockerAddress';
export * from './dockerContainer';
export * from './dockerContainerConfig';
export * from './dockerContainerState';
export * from './dockerDeviceMapping';
export * from './dockerEndpointIPAMConfig';
export * from './dockerEndpointSettings';
export * from './dockerGraphDriverData';
export * from './dockerHealthConfig';
export * from './dockerHostConfig';
export * from './dockerHostConfigAllOf';
export * from './dockerHostConfigAllOfLogConfig';
export * from './dockerImage';
export * from './dockerImageMetadata';
export * from './dockerImageRootFS';
export * from './dockerMount';
export * from './dockerMountBindOptions';
export * from './dockerMountPoint';
export * from './dockerMountTmpfsOptions';
export * from './dockerMountVolumeOptions';
export * from './dockerMountVolumeOptionsDriverConfig';
export * from './dockerNetworkSettings';
export * from './dockerPortBinding';
export * from './dockerResources';
export * from './dockerResourcesBlkioWeightDevice';
export * from './dockerResourcesUlimits';
export * from './dockerRestartPolicy';
export * from './dockerThrottleDevice';
export * from './dockerVersion';
export * from './dockerVersionComponents';
export * from './dockerVersionPlatform';
export * from './errorInfo';
export * from './inlineResponse200';
export * from './memInfo';
export * from './mountPoint';
export * from './platform';
export * from './process';
export * from './targetDevice';

import localVarRequest = require('request');

import { Application } from './application';
import { DockerAddress } from './dockerAddress';
import { DockerContainer } from './dockerContainer';
import { DockerContainerConfig } from './dockerContainerConfig';
import { DockerContainerState } from './dockerContainerState';
import { DockerDeviceMapping } from './dockerDeviceMapping';
import { DockerEndpointIPAMConfig } from './dockerEndpointIPAMConfig';
import { DockerEndpointSettings } from './dockerEndpointSettings';
import { DockerGraphDriverData } from './dockerGraphDriverData';
import { DockerHealthConfig } from './dockerHealthConfig';
import { DockerHostConfig } from './dockerHostConfig';
import { DockerHostConfigAllOf } from './dockerHostConfigAllOf';
import { DockerHostConfigAllOfLogConfig } from './dockerHostConfigAllOfLogConfig';
import { DockerImage } from './dockerImage';
import { DockerImageMetadata } from './dockerImageMetadata';
import { DockerImageRootFS } from './dockerImageRootFS';
import { DockerMount } from './dockerMount';
import { DockerMountBindOptions } from './dockerMountBindOptions';
import { DockerMountPoint } from './dockerMountPoint';
import { DockerMountTmpfsOptions } from './dockerMountTmpfsOptions';
import { DockerMountVolumeOptions } from './dockerMountVolumeOptions';
import { DockerMountVolumeOptionsDriverConfig } from './dockerMountVolumeOptionsDriverConfig';
import { DockerNetworkSettings } from './dockerNetworkSettings';
import { DockerPortBinding } from './dockerPortBinding';
import { DockerResources } from './dockerResources';
import { DockerResourcesBlkioWeightDevice } from './dockerResourcesBlkioWeightDevice';
import { DockerResourcesUlimits } from './dockerResourcesUlimits';
import { DockerRestartPolicy } from './dockerRestartPolicy';
import { DockerThrottleDevice } from './dockerThrottleDevice';
import { DockerVersion } from './dockerVersion';
import { DockerVersionComponents } from './dockerVersionComponents';
import { DockerVersionPlatform } from './dockerVersionPlatform';
import { ErrorInfo } from './errorInfo';
import { InlineResponse200 } from './inlineResponse200';
import { MemInfo } from './memInfo';
import { MountPoint } from './mountPoint';
import { Platform } from './platform';
import { Process } from './process';
import { TargetDevice } from './targetDevice';

/* tslint:disable:no-unused-variable */
let primitives = [
                    "string",
                    "boolean",
                    "double",
                    "integer",
                    "long",
                    "float",
                    "number",
                    "any"
                 ];

let enumsMap: {[index: string]: any} = {
        "DockerContainerState.StatusEnum": DockerContainerState.StatusEnum,
        "DockerHostConfigAllOfLogConfig.TypeEnum": DockerHostConfigAllOfLogConfig.TypeEnum,
        "DockerMount.TypeEnum": DockerMount.TypeEnum,
        "DockerMountBindOptions.PropagationEnum": DockerMountBindOptions.PropagationEnum,
        "DockerRestartPolicy.NameEnum": DockerRestartPolicy.NameEnum,
}

let typeMap: {[index: string]: any} = {
    "Application": Application,
    "DockerAddress": DockerAddress,
    "DockerContainer": DockerContainer,
    "DockerContainerConfig": DockerContainerConfig,
    "DockerContainerState": DockerContainerState,
    "DockerDeviceMapping": DockerDeviceMapping,
    "DockerEndpointIPAMConfig": DockerEndpointIPAMConfig,
    "DockerEndpointSettings": DockerEndpointSettings,
    "DockerGraphDriverData": DockerGraphDriverData,
    "DockerHealthConfig": DockerHealthConfig,
    "DockerHostConfig": DockerHostConfig,
    "DockerHostConfigAllOf": DockerHostConfigAllOf,
    "DockerHostConfigAllOfLogConfig": DockerHostConfigAllOfLogConfig,
    "DockerImage": DockerImage,
    "DockerImageMetadata": DockerImageMetadata,
    "DockerImageRootFS": DockerImageRootFS,
    "DockerMount": DockerMount,
    "DockerMountBindOptions": DockerMountBindOptions,
    "DockerMountPoint": DockerMountPoint,
    "DockerMountTmpfsOptions": DockerMountTmpfsOptions,
    "DockerMountVolumeOptions": DockerMountVolumeOptions,
    "DockerMountVolumeOptionsDriverConfig": DockerMountVolumeOptionsDriverConfig,
    "DockerNetworkSettings": DockerNetworkSettings,
    "DockerPortBinding": DockerPortBinding,
    "DockerResources": DockerResources,
    "DockerResourcesBlkioWeightDevice": DockerResourcesBlkioWeightDevice,
    "DockerResourcesUlimits": DockerResourcesUlimits,
    "DockerRestartPolicy": DockerRestartPolicy,
    "DockerThrottleDevice": DockerThrottleDevice,
    "DockerVersion": DockerVersion,
    "DockerVersionComponents": DockerVersionComponents,
    "DockerVersionPlatform": DockerVersionPlatform,
    "ErrorInfo": ErrorInfo,
    "InlineResponse200": InlineResponse200,
    "MemInfo": MemInfo,
    "MountPoint": MountPoint,
    "Platform": Platform,
    "Process": Process,
    "TargetDevice": TargetDevice,
}

export class ObjectSerializer {
    public static findCorrectType(data: any, expectedType: string) {
        if (data == undefined) {
            return expectedType;
        } else if (primitives.indexOf(expectedType.toLowerCase()) !== -1) {
            return expectedType;
        } else if (expectedType === "Date") {
            return expectedType;
        } else {
            if (enumsMap[expectedType]) {
                return expectedType;
            }

            if (!typeMap[expectedType]) {
                return expectedType; // w/e we don't know the type
            }

            // Check the discriminator
            let discriminatorProperty = typeMap[expectedType].discriminator;
            if (discriminatorProperty == null) {
                return expectedType; // the type does not have a discriminator. use it.
            } else {
                if (data[discriminatorProperty]) {
                    var discriminatorType = data[discriminatorProperty];
                    if(typeMap[discriminatorType]){
                        return discriminatorType; // use the type given in the discriminator
                    } else {
                        return expectedType; // discriminator did not map to a type
                    }
                } else {
                    return expectedType; // discriminator was not present (or an empty string)
                }
            }
        }
    }

    public static serialize(data: any, type: string) {
        if (data == undefined) {
            return data;
        } else if (primitives.indexOf(type.toLowerCase()) !== -1) {
            return data;
        } else if (type.lastIndexOf("Array<", 0) === 0) { // string.startsWith pre es6
            let subType: string = type.replace("Array<", ""); // Array<Type> => Type>
            subType = subType.substring(0, subType.length - 1); // Type> => Type
            let transformedData: any[] = [];
            for (let index in data) {
                let date = data[index];
                transformedData.push(ObjectSerializer.serialize(date, subType));
            }
            return transformedData;
        } else if (type === "Date") {
            return data.toISOString();
        } else {
            if (enumsMap[type]) {
                return data;
            }
            if (!typeMap[type]) { // in case we dont know the type
                return data;
            }

            // Get the actual type of this object
            type = this.findCorrectType(data, type);

            // get the map for the correct type.
            let attributeTypes = typeMap[type].getAttributeTypeMap();
            let instance: {[index: string]: any} = {};
            for (let index in attributeTypes) {
                let attributeType = attributeTypes[index];
                instance[attributeType.baseName] = ObjectSerializer.serialize(data[attributeType.name], attributeType.type);
            }
            return instance;
        }
    }

    public static deserialize(data: any, type: string) {
        // polymorphism may change the actual type.
        type = ObjectSerializer.findCorrectType(data, type);
        if (data == undefined) {
            return data;
        } else if (primitives.indexOf(type.toLowerCase()) !== -1) {
            return data;
        } else if (type.lastIndexOf("Array<", 0) === 0) { // string.startsWith pre es6
            let subType: string = type.replace("Array<", ""); // Array<Type> => Type>
            subType = subType.substring(0, subType.length - 1); // Type> => Type
            let transformedData: any[] = [];
            for (let index in data) {
                let date = data[index];
                transformedData.push(ObjectSerializer.deserialize(date, subType));
            }
            return transformedData;
        } else if (type === "Date") {
            return new Date(data);
        } else {
            if (enumsMap[type]) {// is Enum
                return data;
            }

            if (!typeMap[type]) { // dont know the type
                return data;
            }
            let instance = new typeMap[type]();
            let attributeTypes = typeMap[type].getAttributeTypeMap();
            for (let index in attributeTypes) {
                let attributeType = attributeTypes[index];
                instance[attributeType.name] = ObjectSerializer.deserialize(data[attributeType.baseName], attributeType.type);
            }
            return instance;
        }
    }
}

export interface Authentication {
    /**
    * Apply authentication settings to header and query params.
    */
    applyToRequest(requestOptions: localVarRequest.Options): Promise<void> | void;
}

export class HttpBasicAuth implements Authentication {
    public username: string = '';
    public password: string = '';

    applyToRequest(requestOptions: localVarRequest.Options): void {
        requestOptions.auth = {
            username: this.username, password: this.password
        }
    }
}

export class HttpBearerAuth implements Authentication {
    public accessToken: string | (() => string) = '';

    applyToRequest(requestOptions: localVarRequest.Options): void {
        if (requestOptions && requestOptions.headers) {
            const accessToken = typeof this.accessToken === 'function'
                            ? this.accessToken()
                            : this.accessToken;
            requestOptions.headers["Authorization"] = "Bearer " + accessToken;
        }
    }
}

export class ApiKeyAuth implements Authentication {
    public apiKey: string = '';

    constructor(private location: string, private paramName: string) {
    }

    applyToRequest(requestOptions: localVarRequest.Options): void {
        if (this.location == "query") {
            (<any>requestOptions.qs)[this.paramName] = this.apiKey;
        } else if (this.location == "header" && requestOptions && requestOptions.headers) {
            requestOptions.headers[this.paramName] = this.apiKey;
        } else if (this.location == 'cookie' && requestOptions && requestOptions.headers) {
            if (requestOptions.headers['Cookie']) {
                requestOptions.headers['Cookie'] += '; ' + this.paramName + '=' + encodeURIComponent(this.apiKey);
            }
            else {
                requestOptions.headers['Cookie'] = this.paramName + '=' + encodeURIComponent(this.apiKey);
            }
        }
    }
}

export class OAuth implements Authentication {
    public accessToken: string = '';

    applyToRequest(requestOptions: localVarRequest.Options): void {
        if (requestOptions && requestOptions.headers) {
            requestOptions.headers["Authorization"] = "Bearer " + this.accessToken;
        }
    }
}

export class VoidAuth implements Authentication {
    public username: string = '';
    public password: string = '';

    applyToRequest(_: localVarRequest.Options): void {
        // Do nothing
    }
}

export type Interceptor = (requestOptions: localVarRequest.Options) => (Promise<void> | void);
