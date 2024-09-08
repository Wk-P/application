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
        <li v-if="route.path.startsWith('/start')" @click="search">
            <div><img src="/img/searchbutton.png" alt="search" /></div>
        </li>
        <li class="title"><p>ASLIN</p></li>
        <!-- <li @click="favorite">
            <div><img src="/img/heart.png" alt="favorite" /></div>
        </li> -->
        <li @click="cart">
            <div><img src="/img/cart.png" alt="cart" /></div>
        </li>
    </ul>
    <teleport to="body">
        <div v-if="showSearchModal" class="search-modal">
            <div class="modal-content">
                <span class="close" @click="closeModal">&times;</span>
                <h2>Search</h2>
                <input
                    type="text"
                    v-model="searchQuery"
                    placeholder="Enter your query"
                />
                <button @click="saveSearchQuery">Save</button>
            </div>
        </div>
    </teleport>
</template>

<script lang="ts" setup name="HeadHomeBar">
import { useRouter, useRoute } from "vue-router";
import { ref } from "vue";
import { useQueryStore } from "@/stores/index";


const queryStore = useQueryStore();
const router = useRouter();
const route = useRoute();
const showSearchModal = ref(false);
const searchQuery = ref("");

const toHome = () => {
    router.push({ name: "home" }).catch((err) => {
        console.error(err.message);
    });
};

function search() {
    showSearchModal.value = true;
}

const closeModal = () => {
    showSearchModal.value = false;
};

// 保存搜索查询到 sessionStorage
const saveSearchQuery = () => {
    sessionStorage.setItem("searchQuery", searchQuery.value);
    closeModal(); // 关闭二级界面
    queryStore.setQuery(searchQuery.value);
    router.push({ name: "start" });
    window.location.reload();
};

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
.search-modal {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.5);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 1000;
}

.modal-content {
    background: white;
    padding: 20px;
    border-radius: 8px;
    width: 80%;
    max-width: 500px;
    position: relative;
}

.modal-content input {
    box-sizing: border-box;
    border-radius: 6px;
    border: 1px solid black;
    padding: 0.7rem;
    margin: 0.5rem;
    font-size: 1.04rem;
    height: 6vh;
}
.modal-content button {
    padding: 0.7rem;
    height: 6vh;
    border: 1px solid #111;
    background-color: white;
    border-radius: 6px;
    margin-left: 1rem;
}

.close {
    position: absolute;
    top: 10px;
    right: 20px;
    font-size: 24px;
    cursor: pointer;
}
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
