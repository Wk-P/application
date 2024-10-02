<template>
    <div class="search-container">
        <input type="text" ref="searchInput" v-model="searchInputTextValue" />
        <div class="search-block">
            <button @click="search">
                <img src="/src_img/search1.png" alt="search_img" />
            </button>
        </div>
    </div>
</template>

<script lang="ts" setup name="SearchBar">
import { onMounted, ref } from "vue";

// 根据路由判断需要查询什么
const search = () => {
    // 收集路由
    // TODO
    let queryKeyword = "";
    alert("search");
};

const searchInputTextValue = ref<string | undefined>("");
const searchInput = ref<HTMLInputElement | null>(null);
</script>

<style scoped>
.search-container {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    padding: 0.7rem;
}

.search-container input {
    display: block;
    box-sizing: border-box;
    height: 100%;
    width: 100%;
    background-color: #eee;
    border-radius: 1rem;
    padding: 0 1rem;
    border: none;
    outline: none;
    height: 2rem;
}

.search-container button {
    display: block;
    height: 100%;
    border: none;
    background-color: white;
}

.search-container button img {
    box-sizing: border-box;
    height: 2rem;
    padding: 0.25rem 0rem 0.25rem 1.5rem;
}
</style>
