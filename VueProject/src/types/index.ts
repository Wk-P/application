export interface User {
    id: string,
    uid: string,
    tel: string,
    name: string,
    email: string,
    username: string,
    loginStatus: boolean,
    token: string | null,
    cookies: string | null,
    address: string | null,
}