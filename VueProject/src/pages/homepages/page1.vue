<template>
    <nav>
        <ul>
            <li v-for="item in recommendItemsList">
                <RouterLink
                    :to="{
                        name: 'itemdetail',
                        params: {
                            itemId: item.id,
                            brand: item.brand,
                            itemTitle: item.title,
                            itemName: item.name,
                        },
                    }"
                    ><img :src="item.images[0].image" alt="img1"
                /></RouterLink>
            </li>
        </ul>
    </nav>
</template>

<script lang="ts" setup name="Page1">
import { RouterLink } from "vue-router";
import { ref, onMounted } from "vue";
import type { Item } from "@/types/index";
const recommendItemsList = ref<Array<Item>>([]);

const fetchRecommend = () => {
    fetch(`/api/items/recommend/`)
        .then((response) => {
            if (!response.ok) {
                response.json().then((error) => {
                    console.log(error);
                    throw new Error(
                        `Error! HTTP status code ${response.status}`
                    );
                });
            }
            return response.json();
        })
        .then((data) => {
            recommendItemsList.value = data;
        });
};

onMounted(() => {
    fetchRecommend();
})

</script>

<style scoped>
nav {
    box-sizing: border-box;
    display: flex;
    flex-direction: row;
    height: 50vh;
    width: 100%;
    overflow-x: auto;
    scrollbar-width: none; /* firefox */
    -ms-overflow-style: none; /* IE 10+ */
    scroll-snap-type: x mandatory;
    animation: 0.3s linear 0.1s slideIn;
}

nav::-webkit-scrollbar {
    display: none;
}

nav > ul {
    box-sizing: border-box;
    height: 100%;
    display: flex;
    list-style: none;
    white-space: nowrap;
    margin: 0;
    padding: 0;
}

nav > ul > li {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100vw;
    height: 100%;
    background-color: #eee;
    scroll-snap-align: center;
}

nav > ul > li > img {
    max-width: 100%;
    max-height: 100%;
    object-fit: cover;
}

@keyframes slideIn {
    from {
        opacity: 0;
        transform: translateX(-5rem);
    }
    to {
        opacity: 1;
        transform: translateX(0);
    }
}
</style>
