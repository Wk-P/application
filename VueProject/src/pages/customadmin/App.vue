<template>
    <div v-if="!isLoggedIn" class="login-block">
        <div>
            <span>Username</span><input type="text" v-model="adminUsername" />
        </div>
        <div>
            <span>Password</span
            ><input type="password" v-model="adminPassword" />
        </div>
        <div class="button-block">
            <button @click="handleLogin($event, adminUsername, adminPassword)">
                Login
            </button>
        </div>
    </div>
    <div v-else>
        <nav class="link-block">
            <RouterLink :to="{ name: 'adminHome' }" class="link"
                >Admin</RouterLink
            >
            <RouterLink :to="{ name: 'uploaditems' }" class="link"
                >Img Upload</RouterLink
            >
        </nav>
        <div>
            <RouterView></RouterView>
        </div>
    </div>
</template>

<script lang="ts" setup name="CustomAdmin">
import { ref, onMounted, computed } from "vue";
import { login } from "@/utils/utils";
import { useUserStore } from "@/stores/index";
import { useRouter, useRoute } from "vue-router";

const route = useRoute();
const router = useRouter();
const adminUsername = ref<string>("");
const adminPassword = ref<string>("");
const userStore = useUserStore();
const isLoggedIn = computed(() => userStore.user?.loginStatus === true);

onMounted(() => {
    if (userStore.user) {
        router.push(route.path);
    }
});

const handleLogin = (event: Event, username: string, password: string) => {
    login(event, username, password, route)
        .then((result) => {
            console.log(result);
            if (result.success && result.user) {
                userStore.setUser(result.user);
                router.push({ name: "adminHome" });
            } else {
                alert("Login failed");
            }
        })
        .catch((error) => console.error(error));
};
</script>

<style scoped>
.link-block {
    height: 5vh;
    color: white;
    background-color: black;
    display: flex;
    flex-direction: row;
    align-items: center;
}
.link {
    height: 100%;
    display: block;
    box-sizing: border-box;
    text-decoration: none;
    color: white;
    padding: 0 1rem;
    border-left: 1px solid white;
    border-right: 1px solid white;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.login-block > div {
    display: flex;
    flex-direction: row;
    justify-content: space-evenly;
    padding: 2rem;
}

.login-block span {
    box-sizing: border-box;
    padding: 0.2rem;
    width: 30vw;
}

.login-block input {
    box-sizing: border-box;
    padding: 0.4rem;
    border: 0.15em solid black;
}

.button-block {
    box-sizing: border-box;
    width: 100%;
    padding: 0.2rem;
}

.button-block button {
    box-sizing: border-box;
    padding: 0.5rem;
    width: 50%;
    font-size: 1.05rem;
    border: 2px black solid;
    background-color: white;
}
</style>
