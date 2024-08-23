<template>
    <HeadNav/>
    <div class="blocks">
        <div class="head-outer">
            <div class="head-left">
                <img src="" alt="avator" />
            </div>
            <ul class="inner-block">
                <li><RouterLink :to="{ name : 'orders' }">订单</RouterLink></li>
                <li><RouterLink :to="{ name : 'cart' }">购物车</RouterLink></li>
                <li><RouterLink :to="{ name : 'favorite' }">收藏</RouterLink></li>
            </ul>
        </div>
        <div class="top-line"></div>
        <div class="user-block">
            <div>{{ username }}</div>
        </div>
        <div class="container-block">
            <RouterView></RouterView>
        </div>
    </div>
</template>

<script lang="ts" setup name="usercenter">
import HeadNav from "@/components/HeadNav.vue";
import { RouterLink, RouterView } from "vue-router";
import { ref } from "vue";
import { userTokenStore } from "@/stores";

const tokenStore = userTokenStore();
const username = ref("");
if (tokenStore.username === null) {
    username.value = "";
} else {
    username.value = tokenStore.username;
}
</script>
<style scoped>
.blocks {
    display: flex;
    flex-direction: column;
    justify-content: start;
    align-items: center;
    width: 100%;
    box-sizing: border-box;
}

.head-outer {
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    height: 80px;
    box-sizing: border-box;
}

.head-outer img {
    border: 4px solid brown;
    height: 100%;
    aspect-ratio: 1;
    box-sizing: border-box;
}

.head-outer ul {
    display: flex;
    flex-direction: row;
    justify-content: end;
    list-style: none;
    box-sizing: border-box;
    background-color: rgba(244, 244, 244, 0.5);
}

.head-outer ul li {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    box-sizing: border-box;
    width: 100px;
}

.head-outer ul li a {
    cursor: pointer;
    color: #222;
    background-color: rgba(235, 235, 235, 1);
    transition: all 0.2s ease-out;
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    text-align: center;
    text-decoration: none;
}


.head-outer ul li a:hover {
    cursor: pointer;
    color: rgb(235, 235, 235);
    background-color: rgba(15, 15, 15, 0.5);
}

.head-left {
    height: 100%;
    display: flex;
    flex-direction: row;
}

/* .head-left div:last-child {
    box-sizing: border-box;
    text-align: center;
    width: 100px;
    font-size: large;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    border: 4px solid brown;
    border-left: none;
} */

.container-block {
    width: calc(100% - 100px);
    height: 100%;
    border: 4px solid brown;
    box-sizing: border-box;
    margin: 50px;
    padding: 30px;
    border-radius: 5px;
}

.top-line {
    display: flex;
    height: 5px;
    width: 100%;
    background: linear-gradient(
        to right,
        rgb(190, 226, 240),
        #fff,
        rgb(190, 226, 240)
    );
}

.user-block {
    width: calc(100% - 100px);
    box-sizing: border-box;
    border: 4px solid brown;
    margin: 50px;
    padding: 20px;
    border-radius: 5px;
}

</style>
