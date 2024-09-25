export interface User {
    id: string,
    uid: string,
    tel: string,
    name: string,
    email: string,
    username: string,
    token: string | null,
    address: string | null,
}

export interface Item {
    id: string,
    name: string,
    desc: string,
    brand: string,
    class: string,
    title: string,
    price: number,
    images: Array<Image>,
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

export interface Image {
    image: string
}