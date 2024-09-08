// src/stores/index.ts
import { defineStore } from "pinia";
import { ref } from "vue";
import type { User, Item, Order } from "@/types/index";


export const useUserStore = defineStore('user', () => {
    const user = ref<User | null>(null);
    const setUser = (newUser: User) => {
        user.value = newUser;
        localStorage.setItem("user", JSON.stringify(newUser));
    };

    const clearUser = () => {
        user.value = null;
        localStorage.removeItem("user");
    }

    const loadUser = () => {
        const storedUser = localStorage.getItem("user");
        if (storedUser) {
            try {
                user.value = JSON.parse(storedUser);
            } catch (error) {
                console.error("Failed to parse user from localStorage:", error);
                user.value = null;
                localStorage.removeItem("user");
            }
        }
    };
    

    const updateUserField = <KEY extends keyof User>(field: KEY, value: User[KEY]) => {
        if (user.value) {
            user.value[field] = value as User[typeof field];
            setUser(user.value);
        }
    };

    loadUser();

    return {
        user, setUser, clearUser, loadUser, updateUserField,
    }
});


export const useItemStore = defineStore('item', () => {
    const item = ref<Item | null>(null);
    const setCustomItem = (newItem: Item) => {
        item.value = newItem;
        localStorage.setItem("item", JSON.stringify(newItem));
    };

    const clearCustomItem = () => {
        item.value = null;
        localStorage.removeItem("item");
    }

    const loadCustomItem = () => {
        const storedItem = localStorage.getItem("item");
        if (storedItem) {
            item.value = JSON.parse(storedItem);
        }
    }

    const updateCustomItemField = <KEY extends keyof Item>(field: KEY, value: Item[KEY]) => {
        if (item.value) {
            item.value[field] = value as Item[typeof field];
        }
    };

    loadCustomItem();

    return {
        item, setCustomItem, clearCustomItem, loadCustomItem, updateCustomItemField,
    }
})

export const useItemsListStore = defineStore('items', () => {
    const itemsList = ref<Array<Item> | null>(null);
    const setItemsList = (newItemsList: Array<Item>) => {
        itemsList.value = newItemsList;
        localStorage.setItem("items", JSON.stringify(newItemsList));
    };

    const clearItemsList = () => {
        itemsList.value = null;
        localStorage.removeItem("items");
    }

    const loadItemsList = () => {
        const storedItemsList = localStorage.getItem("items");
        if (storedItemsList) {
            itemsList.value = JSON.parse(storedItemsList);
        }
    }

    const updateItemsList = (newItemsList: Array<Item>) => {
        itemsList.value = newItemsList;
    };

    loadItemsList();

    return {
        itemsList, setItemsList, clearItemsList, loadItemsList, updateItemsList,
    }
})


export const useOrderStore = defineStore('order', () => {
    const order = ref<Order | null>(null);
    const setOrder = (newOrder: Order) => {
        order.value = newOrder;
        localStorage.setItem("order", JSON.stringify(newOrder));
    };

    const clearOrder = () => {
        order.value = null;
        localStorage.removeItem("order");
    }

    const loadOrder = () => {
        const storedOrder = localStorage.getItem("order");
        if (storedOrder) {
            order.value = JSON.parse(storedOrder);
        }
    }

    const updateOrder = (newOrder: Order) => {
        order.value = newOrder;
    };

    loadOrder();

    return {
        order, setOrder, clearOrder, loadOrder, updateOrder,
    }
})


export const useOrdersListStore = defineStore('orders', () => {
    const ordersList = ref<Array<Order> | null>(null);
    const setOrdersList = (newOrdersList: Array<Order>) => {
        ordersList.value = newOrdersList;
        localStorage.setItem("orders", JSON.stringify(newOrdersList));
    };

    const clearOrdersList = () => {
        ordersList.value = null;
        localStorage.removeItem("orders");
    }

    const loadOrdersList = () => {
        const storedOrder = localStorage.getItem("orders");
        if (storedOrder) {
            ordersList.value = JSON.parse(storedOrder);
        }
    }

    const updateOrdersList = (newOrdersList: Array<Order>) => {
        ordersList.value = newOrdersList;
    };

    loadOrdersList();

    return {
        ordersList, setOrdersList, clearOrdersList, loadOrdersList, updateOrdersList,
    }
})

export const useQueryStore = defineStore('query', () => {
    const query = ref<string | null>(null);
    const setQuery = (newQuery: string) => {
        query.value = newQuery;
        localStorage.setItem("query", JSON.stringify(newQuery));
    };

    const clearQuery = () => {
        query.value = null;
        localStorage.removeItem("query");
    }

    const loadQuery = () => {
        const storedOrder = localStorage.getItem("query");
        if (storedOrder) {
            query.value = JSON.parse(storedOrder);
        }
    }

    const updateQuery = (newQuery: string) => {
        query.value = newQuery;
    };

    loadQuery();

    return {
        query, setQuery, clearQuery, loadQuery, updateQuery,
    }
})
