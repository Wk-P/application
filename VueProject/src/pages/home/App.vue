<template>
    <HeadNav />
    <div class="block">
        <nav class="support">
            <ul>
                <li>分区1</li>
                <li>分区2</li>
                <li>分区3</li>
            </ul>
        </nav>
        <div class="waterfall-flow" ref="waterfallContainer">
            <ul class="items">
                <li v-for="(item, index) in itemsList" :key="index">
                    <RouterLink
                        class="router-link-item-detail"
                        :to="{
                            path: `/product/${item.id}/details`,
                        }"
                        @click="storeProductObj(item)"
                    >
                        <div>{{ item.id }}</div>
                        <div>商品名: {{ item.name }}</div>
                        <div>描述: {{ item.desc }}</div>
                        <div>价格: {{ item.price }}</div>
                    </RouterLink>
                </li>
            </ul>
        </div>
    </div>
</template>

<script lang="ts" setup>
import { ref, computed, onMounted, watch } from "vue";
import type { Item } from "@/types/index";
import { RouterLink } from "vue-router";
import HeadNav from "@/components/HeadNav.vue";
import { useItemStore, useSearchStore } from "@/stores/index";

const itemStore = useItemStore();
const searchStore = useSearchStore();
const itemsList = ref<Item[]>([]);

// 获取商品列表数据
const fetchItems = async () => {
    const url = "/backend/api/items/all";
    let params = "";

    if (params == "") {
        params += "/";
    }

    try {
        // const response = await fetch(queryBaseURL);
        const response = await fetch(`${url}/${params}`);
        if (!response.ok) {
            throw new Error("Fetch failed");
        }
        const data = await response.json();
        itemsList.value = data; // 更新商品列表数据
    } catch (error) {
        console.error("Fetch Error:", error);
    }
};

const storeProductObj = (item: Item) => {
    itemStore.setItem(item);
};

// 在组件加载时获取商品列表数据
onMounted(() => {
    fetchItems();
});

window.onbeforeunload = function () {
    searchStore.clearResults();
};

// 重新获取search结果
const searchResultsComputed = computed(
    () => searchStore.searchResultsList || []
);

// 监听 searchResultsComputed 的变化
watch(searchResultsComputed, (newResults, oldResults) => {
    // 只在搜索结果发生变化时更新 itemsList
    if (newResults !== oldResults) {
        itemsList.value = newResults;
    }
});
</script>

<style scoped>
.block {
    width: 100%;
    height: auto;
}
.support {
    width: 100%;
    display: flex;
    flex-direction: row;
    align-items: center;
    text-align: center;
    height: 40px;
}

.support ul {
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: row;
    justify-content: start;
    align-items: center;
    list-style: none;
    background-color: rgb(34, 74, 134);
    border: 2px solid rgb(34, 74, 134);
}

.support ul li {
    height: 100%;
    padding: 0 20px;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    border: 2px solid rgb(34, 74, 134);
    color: white;
}

.support ul li:hover {
    border-radius: 3px;
    cursor: pointer;
    border: 2px solid #fff;
}

.items {
    margin: 25px;
    border-radius: 10px;

    display: grid;
    grid-template-columns: repeat(3, 1fr);
    list-style: none;

    height: auto;
}

.items li {
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    align-items: flex-start;
    padding: 15px;
    background-color: #fff;
    box-shadow: 0 0 15px #888;
    border-radius: 10px;
    margin: 20px;
    font-size: 1.3em;
    height: 200px;
}

.loading {
    padding: 20px;
    text-align: center;
}

.router-link-item-detail {
    text-align: center;
    width: 100%;
    height: 100%;

    display: flex;
    flex-direction: column;
    justify-content: space-evenly;

    text-decoration: none;

    color: black;
}

.router-link-item-detail div {
    height: auto;
}

.router-link-item-detail:hover {
    cursor: pointer;
    color: #00e3a3;
}

.img-display-block {
    width: 100%;
    box-sizing: border-box;
    padding: 20px;
    display: flex;
    flex-direction: row;
    justify-content: center;
    height: auto;
}

.img-display-block ul {
    list-style: none;
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    grid-gap: 40px;
    padding: 0;
    margin: 0;
    width: 80%;
}
.img-display-block ul li {
    box-sizing: border-box;
    box-shadow: 0 0 10px 4px #444;
    border-radius: 20px;
    overflow: hidden; /* 确保超出部分被裁剪 */
}

.img-display-block ul li img {
    display: block; /* 移除底部空白 */
    width: 100%; /* 确保图片占满整个容器 */
    height: 100%;
    object-fit: cover; /* 确保图片按比例裁剪以适应容器 */
}
</style>
