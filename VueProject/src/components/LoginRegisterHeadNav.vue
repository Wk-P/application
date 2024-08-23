<template>
    <nav>
        <ul class="login-register-head-nav">
            <li><RouterLink to="/">主页</RouterLink></li>
            <li v-if="isLogin"><RouterLink to="/register">注册</RouterLink></li>
            <li v-if="isRegister"><RouterLink to="/login">登录</RouterLink></li>
        </ul>
    </nav>
</template>

<script lang="ts" setup>
import { ref } from "vue";
import { RouterLink, useRoute } from "vue-router";
const isLogin = ref(true);
const isRegister = ref(false);

const route = useRoute();

if (route.path.split("/")[-1] == "register") {
    isLogin.value = false;
    isRegister.value = true;
} else {
    isLogin.value = true;
    isRegister.value = false;
}
</script>

<style scoped>
.login-register-head-nav {
    display: flex;
    flex-direction: row;
    list-style: none;
    background-color: rgb(34, 74, 134);
    height: 60px;
    border: 2px solid rgb(34, 74, 134);
}

.login-register-head-nav li {
    background-color: rgb(34, 74, 134);
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    height: 100%;
    width: 5%;
}

.login-register-head-nav li a {
    height: 100%;
    width: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    text-align: center;
    text-decoration: none;
    color: white;
}

.login-register-head-nav li a:hover {
    cursor: pointer;
    border: 2px solid rgb(255, 255, 255);
    border-radius: 5px;
}
</style>
