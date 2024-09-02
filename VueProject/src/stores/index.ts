// src/stores/index.ts
import { defineStore } from "pinia";
import { ref } from "vue";
import type { User, Item } from "@/types/index";


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
            user.value = JSON.parse(storedUser);
        }
    }

    const updateUserField = <KEY extends keyof User>(field: KEY, value: User[KEY]) => {
        if (user.value) {
            user.value[field] = value as User[typeof field];
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