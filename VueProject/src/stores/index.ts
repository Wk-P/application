// src/stores/index.ts
import { defineStore } from "pinia";
import { ref } from "vue";
import type { User } from "@/types/index";

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
