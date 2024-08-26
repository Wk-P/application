<template>
    <div class="containers-head" ref="containersHead">
        <OptionHeader />
    </div>
    <div class="block">
        <div><button @click="logoutUser">Logout</button></div>
        <div class="title">나의 쇼핑 정보</div>
        <ul class="info-block">
            <!-- <li v-for="(value, key) in userInfoObj" :key="key">
                <div class="key-block">{{ key }}</div>
                <div class="value-block">{{ value }}</div>
            </li> -->
        </ul>
    </div>
    <footer><FooterBlock /></footer>
</template>

<script lang="ts" setup name="usercenter">
import OptionHeader from "@/components/OptionHeader.vue";
import FooterBlock from "@/components/FooterBlock.vue";
import { ref } from "vue";
import { useUserStore } from "@/stores";
import { onMounted } from "vue";
import router from "@/router";

// 检查是否登录
const userStore = useUserStore();
const isLoggedIn = ref<boolean>(
    userStore.user?.loginStatus === true ? true : false
);
const user = JSON.parse(localStorage.getItem("user") as string);
const token: string | null = user?.token;
async function logoutUser() {
    try {
        // test
        localStorage.clear();
        if (token !== null) {
            fetch("/backend/api/user/logout/", {
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

.info-block li .key-block {
    font-size: 1rem;
    width: 20%;
    text-align: right;
    padding: 0.4em 1.6em 0.4em 0;
}

.info-block li .value-block {
    font-size: 1rem;
    width: 80%;
    text-align: center;
    border: 0.1rem solid black;
    padding: 0.4em 0;
}
</style>
