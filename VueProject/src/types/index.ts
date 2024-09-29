export interface User {
    id: string,
    uid: string,
    tel: string,
    name: string,
    email: string,
    username: string,
    token: string | null,
}

export interface Item {
    id: string,
    name: string,
    desc: string,
    brand: string,
    class: string,
    title: string,
    price: number,
    images: Array<Image> | null | undefined,
}

export interface Order {
    orderId: string | undefined,
    user: User | undefined,
    item: Item | undefined,
    quantity: number | undefined,
    totalPrice: number | undefined,
    createdTime: string | undefined,
    updatedTime: string | undefined,
    status: string | undefined,
    tracking_number: string | undefined,
}

export interface AdminUser {
    username: string,
    token: string | null,
}

export interface Image {
    image: string
}

export interface Notice {
    id: string,
    title: string,
    content: string,
    created_at: string,
    updated_at: string,
}

export interface Comment {
    id: string,
    content: string,
    created_at: string,
    updated_at: string,
    author: User | null,
}

export interface AddressReceiver {
    id: string | null,
    address: string | null,
    receiver: string | null,
    user: User | null,
}