<template>
    <div v-if="user" class="block">
        <ul>
            <li v-for="(value, key) in filteredUser">
                <label>{{ key }}</label>
                <div>
                    <input type="text" v-model="user[key]" />
                </div>
            </li>
        </ul>
        <div class="button-block"><button @click="save">저장</button></div>
    </div>
    <div v-else>
        <p>No user data available.</p>
    </div>
</template>

<script lang="ts" setup name="UsercenterModified">
import { useUserStore } from "@/stores";
import { computed } from "vue";
import type { User } from "@/types/index";
import { useRouter } from "vue-router";

const router = useRouter();
const userStore = useUserStore();
const user = computed(() => userStore.user as User);

const fieldsToShow: Array<keyof User> = [
    "username",
    "tel",
    "email",
    "name",
    "address",
];

const filteredUser = computed(() => {
    if (!userStore.user) return null;
    const filtered: Partial<User | any> = {};
    for (const key of fieldsToShow) {
        if (key in userStore.user) {
            filtered[key] = userStore.user[key];
        }
    }
    return filtered as User;
});

function save() {
    fetch("/api/user/modified/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ user: user.value }),
    })
        .then((response) => {
            if (response.ok) {
                alert(`사용자 정보 수정 완료!`);
                userStore.clearUser();
                router.push({ name: "login"});
            } else {
                throw Error(`HTTP error, status ${response.status}`);
            }
        })
        .catch((error) => console.error(error));
}
</script>

<style scoped>
.block {
    padding: 2rem;
}

.block ul {
    list-style: none;
}

.block ul label {
    display: block;
    font-size: 0.9rem;
    font-weight: bold;
    padding-bottom: 0.4rem;
}

.block ul input {
    box-sizing: border-box;
    outline: none;
    border: 1px solid black;
    padding: 0.5rem;
    width: 100%;
}

.block ul li {
    padding: 0.5rem;
}

.button-block {
    width: 100%;
    padding-top: 1rem;
    display: flex;
    flex-direction: row;
    justify-content: center;
}

.button-block button {
    width: 30%;
    font-size: 0.9rem;
    background-color: white;
    border: 1px solid black;
    padding: 1rem 0;
}
</style>
