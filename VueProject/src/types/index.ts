export interface Item {
    id: number;
    title: string;
    name: string;
    desc: string;
    price: number;
}

export interface Order {
    orderId: string,
    username: string | null,
    itemName: string,
    userId: number,
    createdTime: string,
    updatedTime: string,
    quantity: number,
    totalPrice: number,
    price: number,
}