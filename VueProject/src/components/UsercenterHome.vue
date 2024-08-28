<template>
    <div class="block">
        <div class="logout-button-block">
            <button @click="logoutUser">Logout</button>
        </div>
        <div class="title">나의 쇼핑 정보</div>
        <ul class="info-block">
            <li v-for="(value, key) in filteredUser">
                <div class="key-block">{{ key }}</div>
                <div class="value-block">
                    <span class="no-input" v-if="value === ''">기입 없음</span>
                    <span class="inputed" v-else>{{ value }}</span>
                </div>
            </li>
        </ul>
    </div>
</template>

<script lang="ts" setup name="usercenter">
import { ref, computed } from "vue";
import { useUserStore } from "@/stores";
import { onMounted } from "vue";
import router from "@/router";
import type { User } from "@/types";

// 检查是否登录
const userStore = useUserStore();
const isLoggedIn = ref<boolean>(
    userStore.user?.loginStatus === true ? true : false
);

const user = computed(() => {
    return userStore.user;
});

const fieldsToShow: Array<keyof User> = ["username", "tel", "email", "address"];
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

const token: string | any = user.value?.token;
async function logoutUser() {
    try {
        localStorage.clear();
        userStore.clearUser();
        if (token !== null) {
            fetch("/api/user/logout/", {
                method: "POST",
                headers: {
                    Authorization: `Token ${token}`,
                },
            }).then((response) => {
                if (response.ok) {
                    router.push({ name: "home" });
                } else {
                    throw new Error(`HTTP error! Status: ${response.status}`);
                }
            });
        } else {
            router.push({ name: "home" });
        }
    } catch (error) {
        console.error("Error logging out:", error);
    }
}

onMounted(() => {
    if (isLoggedIn.value === false) {
        router.push("/login");
    }
});
</script>
<style scoped>
.no-input {
    color: #666;
}

.block {
    display: flex;
    flex-direction: column;
    align-items: center;
    width: 100%;
    padding-bottom: 4em;
}

footer {
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: center;
    height: auto;
}

.block .title {
    font-size: 1.5em;
    font-weight: bold;
    padding: 2em 0;
}

.info-block {
    list-style: none;
    width: 100%;
}

.info-block li {
    box-sizing: border-box;
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: space-evenly;
    padding: 0.5em 1em;
}

.info-block li div {
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: space-around;
}

.info-block li .key-block {
    font-size: 1rem;
    width: 35%;
    padding: 0.4em 1.6em 0.4em 0;
}

.info-block li .value-block {
    font-size: 1rem;
    text-align: center;
    border: 0.1rem solid black;
    padding: 0.6em;
}

.logout-button-block {
    width: 100%;
    height: 4em;
    display: flex;
    flex-direction: row;
    justify-content: center;
    padding-top: 2em;
}
.logout-button-block button {
    padding: 1em 6em;
    font-size: 0.8em;
    color: black;
    border: 1px solid;
    background-color: white;
}
</style>
