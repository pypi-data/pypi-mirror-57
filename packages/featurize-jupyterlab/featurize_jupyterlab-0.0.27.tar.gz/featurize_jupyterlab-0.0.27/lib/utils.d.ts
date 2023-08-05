export declare function capitalize(s: string): string;
export declare function statusColor(status: string): string;
export declare function pendingStatus(status: string): boolean;
export declare function request(url: string, method: string, request?: {
    [key: string]: any;
} | null): Promise<Response>;
export declare function upload(url: string, request?: FormData | null): Promise<Response>;
export declare function getCookie(name: string): string | undefined;
export declare function requestData<Datatype>(url: string, method: string, data?: {
    [key: string]: any;
} | null): Promise<Datatype>;
export interface FeaturizeEvent {
    event: string;
    payload: any;
}
export declare class Subscribe {
    channel: string;
    onmessage: (message: FeaturizeEvent) => void;
    socket: WebSocket;
    constructor(onmessage: (event: FeaturizeEvent) => void, channel?: string);
    close(): void;
}
