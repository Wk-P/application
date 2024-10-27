export interface User {
    id: string,
    uid: string,
    tel: string,
    name: string,
    email: string,
    username: string,
    token: string | null,
}

export interface OptionValue {
    value: string
}

export interface Option {
    name: string;
    values: Array<OptionValue>;
}

export interface SelectedOption {
    option_key: string,
    value: string,
}

export interface Item {
    id: string,
    name: string,
    desc: string,
    brand: string,
    class: string,
    title: string,
    price: number,
    options: Array<Option>,
    images: Array<Image> | null | undefined,
}

export interface CartItem {
    item: Item,
    user: User,
    selected_options: Array<SelectedOption>,
}

export interface Order {
    orderId: string | undefined,
    user: User | undefined,
    item: Item | undefined,
    quantity: number | undefined,
    selected_options: Array<SelectedOption>,
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