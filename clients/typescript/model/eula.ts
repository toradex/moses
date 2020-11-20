/**
 * Torizon IDE-backend API
 * Toradex API to build and deploy applications running as containers on Torizon
 *
 * The version of the OpenAPI document: 1.0.12
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { RequestFile } from './models';

export class Eula {
    /**
    * Unique name (should be filesystem-compatible)
    */
    'id'?: string;
    /**
    * eula title
    */
    'title'?: string;
    /**
    * message shown to the user to accept/decline license
    */
    'question'?: string;
    /**
    * full path of the file containing the license text
    */
    'filepath'?: string;
    /**
    * true if license has been shown at least once to user
    */
    'visualized'?: boolean;
    /**
    * true if user accepted the license
    */
    'accepted'?: boolean;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "id",
            "baseName": "id",
            "type": "string"
        },
        {
            "name": "title",
            "baseName": "title",
            "type": "string"
        },
        {
            "name": "question",
            "baseName": "question",
            "type": "string"
        },
        {
            "name": "filepath",
            "baseName": "filepath",
            "type": "string"
        },
        {
            "name": "visualized",
            "baseName": "visualized",
            "type": "boolean"
        },
        {
            "name": "accepted",
            "baseName": "accepted",
            "type": "boolean"
        }    ];

    static getAttributeTypeMap() {
        return Eula.attributeTypeMap;
    }
}

