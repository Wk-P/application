export interface User {
    id: string,
    uid: string,
    tel: string,
    name: string,
    email: string,
    username: string,
    token: string | null,
    cookies: string | null,
    address: string | null,
}

export interface Item {
    id: string,
    name: string,
    desc: string,
    brand: string,
    title: string,
    price: number,
    image: string,
}

export interface Order {
    orderId: string | undefined,
    user: User | undefined,
    item: Item | undefined,
    quantity: number | undefined,
    totalPrice: number | undefined,
    createdTime: string | undefined,
    updatedTime: string | undefined,
}

export interface AdminUser {
    username: string,
    token: string | null,
}