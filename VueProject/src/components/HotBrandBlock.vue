<template>
    <ul>
        <li v-for="brand in hotBrandsList">
            <RouterLink :to="{ name: '' }" class="brand-link">
                <img src="" alt="brand-img">
                <p>{{ brand.className }}</p>
            </RouterLink>
        </li>
    </ul>
</template>

<script lang="ts" setup name="HotBrandBlock">
import { ref } from "vue";
import { RouterLink, RouterView } from "vue-router";

// 从后端获取热门品牌
const hotBrandsList = ref([
    {
        className: "class1",
        image: "",
    },
    {
        className: "class2",
        image: "",
    },
    {
        className: "class3",
        image: "",
    },
]);

</script>

<style scoped>
ul {
    box-sizing: border-box;
    display: grid;
    grid-template-columns: repeat(2, 50%);
    padding: 0 1rem;
    list-style: none;
    width: 100%;
    column-gap: 1rem;
    justify-content: center;
    align-items: center;
}



ul li img {
    display: block;
    width: 100%;
    height: 5rem;
    object-fit: contain;
    border: 1px solid black;
}

ul li p {
    text-align: center;
}

.brand-link {
    color: black;
    text-decoration: none;
}
</style>