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


/**
* The behavior to apply when the container exits. The default is not to restart.  An ever increasing delay (double the previous delay, starting at 100ms) is added before each restart to prevent flooding the server. 
*/
export class DockerRestartPolicy {
    /**
    * - Empty string means not to restart - `always` Always restart - `unless-stopped` Restart always except when the user has manually stopped the container - `on-failure` Restart only when the container exit code is non-zero 
    */
    'name'?: DockerRestartPolicy.NameEnum;
    /**
    * If `on-failure` is used, the number of times to retry before giving up
    */
    'maximumRetryCount'?: number;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "name",
            "baseName": "Name",
            "type": "DockerRestartPolicy.NameEnum"
        },
        {
            "name": "maximumRetryCount",
            "baseName": "MaximumRetryCount",
            "type": "number"
        }    ];

    static getAttributeTypeMap() {
        return DockerRestartPolicy.attributeTypeMap;
    }
}

export namespace DockerRestartPolicy {
    export enum NameEnum {
        Empty = <any> '',
        Always = <any> 'always',
        UnlessStopped = <any> 'unless-stopped',
        OnFailure = <any> 'on-failure'
    }
}
