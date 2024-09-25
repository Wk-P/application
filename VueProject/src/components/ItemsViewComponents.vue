<template>
    <ul class="item-view-list">
        <li v-for="(item, index) in itemsList">
            <RouterLink
                :to="{
                    name: 'itemdetail',
                    params: { itemId: item.id, itemName: item.name, brand: item.brand, itemTitle: item.title },
                }"
            >
                <div class="li-img">
                    <img :src="item.images[0].image" alt="" />
                </div>
                <div class="text-block">
                    <div class="name-block">{{ item.name }}</div>
                    <div class="price-block">$ <strong>{{ item.price }}</strong></div>
                </div>
            </RouterLink>
        </li>
    </ul>
</template>

<script lang="ts" setup name="ItemsViewComponents">
import { ref, onMounted } from "vue";
import type { Item } from "@/types/index";
import { RouterLink } from "vue-router";
const itemsList = ref<Array<Item>>([]);

const fetchAllViewItems = () => {
    fetch(`/api/items/all/`)
        .then((response) => {
            if (!response.ok) {
                throw new Error(`Error! HTTP status code ${response.status}`);
            }
            return response.json();
        })
        .then((data) => {
            itemsList.value = data;
            console.log(itemsList.value);
        });
};

onMounted(() => {
    fetchAllViewItems();
    console.log(itemsList.value);
});
</script>

<style scoped>
.item-view-list {
    list-style: none;
    box-sizing: border-box;
    width: 100%;
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
}

.item-view-list li {
    box-sizing: border-box;
    padding: .5rem;
    width: 33vw;
}

.item-view-list li a {
    width: 100%;
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    text-decoration: none;
    color: black;
}

.li-img {
    height: 15vh;
    width: auto;
}

.li-img img {
    box-sizing: border-box;
    height: 100%;
}

.text-block {
    display: flex;
    flex-direction: column;
}
</style>
