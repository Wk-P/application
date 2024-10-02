<template>
    <ul>
        <li v-for="brand in hotBrandsList">
            <img src="" alt="brand-img">
            <p>{{ brand.className }}</p>
        </li>
    </ul>
</template>

<script lang="ts" setup name="HotBrandBlock">
import { ref } from "vue";

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
    width: 100%;
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    list-style: none;
}

ul li {
    width: 50%;
}

ul li img {
    display: block;
    height: 5rem;
    object-fit: contain;
    border: 1px solid black;
    margin: 0.5rem;
}

ul li p {
    text-align: center;
}

</style>