/**
 * Torizon IDE-backend API
 * Toradex API to build and deploy applications running as containers on Torizon
 *
 * The version of the OpenAPI document: 1.1.5
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { RequestFile } from './models';
import { ErrorInfo } from './errorInfo';

export class Progress {
    /**
    * cookie
    */
    'id'?: string;
    /**
    * 0%-100%
    */
    'progress'?: number;
    'messages'?: Array<string>;
    /**
    * true as long as operation is pending
    */
    'pending'?: boolean;
    'result'?: ErrorInfo;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "id",
            "baseName": "id",
            "type": "string"
        },
        {
            "name": "progress",
            "baseName": "progress",
            "type": "number"
        },
        {
            "name": "messages",
            "baseName": "messages",
            "type": "Array<string>"
        },
        {
            "name": "pending",
            "baseName": "pending",
            "type": "boolean"
        },
        {
            "name": "result",
            "baseName": "result",
            "type": "ErrorInfo"
        }    ];

    static getAttributeTypeMap() {
        return Progress.attributeTypeMap;
    }
}

