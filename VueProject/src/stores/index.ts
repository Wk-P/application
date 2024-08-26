// src/stores/index.ts
import { defineStore } from "pinia";
import { ref } from "vue";
import type { User } from "@/types/index";

export const useUserStore = defineStore('user', () => {
    const user = ref<User | null>();
    const setUser = (newUser: User) => {
        user.value = newUser;
        localStorage.setItem("user", JSON.stringify(newUser));
    };

    const clearUser = () => {
        user.value = null;
        localStorage.clear();
    }

    const loadUser = () => {
        const storedUser = localStorage.getItem("user");
        if (storedUser) {
            user.value = JSON.parse(storedUser);
        }
    }

    loadUser();

    return {
        user, setUser, clearUser, loadUser,
    }
});
