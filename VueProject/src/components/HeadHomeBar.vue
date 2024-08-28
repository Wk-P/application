<template>
    <ul class="head">
        <li @click="toHome">
            <div class="head-bar">
                <img src="/img/home.png" alt="home" />
            </div>
        </li>
        <li @click="usercenter">
            <div><img src="/img/user.png" alt="usercenter" /></div>
        </li>
        <li @click="search">
            <div><img src="/img/searchbutton.png" alt="search" /></div>
        </li>
        <li class="title"><p>ASLIN</p></li>
        <li @click="favorite">
            <div><img src="/img/heart.png" alt="favorite" /></div>
        </li>
        <li @click="cart">
            <div><img src="/img/cart.png" alt="cart" /></div>
        </li>
    </ul>
</template>

<script lang="ts" setup name="HeadHomeBar">
import { useRouter } from "vue-router";

const toHome = () => {
    router.push({ name: "home" }).catch((err) => {
        console.error(err.message);
    });
};
const router = useRouter();
function search() {
    alert("No function");
}
function usercenter() {
    router.push("/usercenter");
}

function favorite() {
    // router.push("/favorite");
    alert("No function");
}

function cart() {
    router.push("/cart");
}
</script>

<style scoped>
.head {
    padding: 0 5px;
    background-color: gray;
    height: 5vh;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
}

.head > li {
    box-sizing: border-box;
    height: 100%;
    width: auto;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.head > li > div {
    height: 35px;
    width: auto;
}

.head img {
    box-sizing: border-box;
    height: 100%;
    width: auto;
    padding: 0.3em;
}

.head .title {
    color: white;
    width: 50%;
    font-size: 1.3rem;
    font-weight: bold;
    text-align: center;
}
</style>
