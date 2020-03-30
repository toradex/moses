export * from './applicationsApi';
import { ApplicationsApi } from './applicationsApi';
export * from './devicesApi';
import { DevicesApi } from './devicesApi';
export * from './platformsApi';
import { PlatformsApi } from './platformsApi';
export * from './setupApi';
import { SetupApi } from './setupApi';
export * from './versionApi';
import { VersionApi } from './versionApi';
import * as fs from 'fs';
import * as http from 'http';

export class HttpError extends Error {
    constructor (public response: http.IncomingMessage, public body: any, public statusCode?: number) {
        super('HTTP request failed');
        this.name = 'HttpError';
    }
}

export interface RequestDetailedFile {
    value: Buffer;
    options?: {
        filename?: string;
        contentType?: string;
    }
}

export type RequestFile = string | Buffer | fs.ReadStream | RequestDetailedFile;

export const APIS = [ApplicationsApi, DevicesApi, PlatformsApi, SetupApi, VersionApi];
