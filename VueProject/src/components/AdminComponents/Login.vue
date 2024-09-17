<template>
    <div class="login-container">
        <h2>Admin Login page</h2>
        <div>
            <h3>Username</h3>
            <input type="text" v-model="adminUsername" readonly>
        </div>
        <div>
            <h3>Password</h3>
            <input type="password" v-model="adminPassword" autocomplete="on">
        </div>
        <div class="button-group">
            <button @click="handleLogin($event, adminUsername, adminPassword)">Login</button>
        </div>
    </div>
</template>

<script lang="ts" setup name="AdminLogin">
import { ref } from "vue";
import { login } from "@/utils/utils";
import { useRoute, useRouter } from "vue-router";
import { useAdminStore } from "@/stores/index";

const router = useRouter();
const route = useRoute();
const adminuserStore = useAdminStore();
const adminUsername = ref<string>("admin");
const adminPassword = ref<string>("");


const handleLogin = async (
    event: Event,
    username: string,
    password: string
) => {
    const result = await login(event, username, password, route);
    if (result.success && result.user) {
        adminuserStore.setAdminUser(result.user);
        router.push({ name: "admin" });
    } else {
        console.log(`${result.success}`);
    }
};

</script>

<style scoped>
.login-container {
    height: 100%;
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
}

.login-container input {
    width: 100%;
    outline: none;
    box-sizing: border-box;
    border: 2px solid black;
    padding: 0.5rem 1rem;
    text-align: center;
}

.button-group {
    padding: 2rem;
}

.button-group button {
    padding: 1rem 4rem;
    background-color: black;
    color: white;
    border: none;
}

</style>