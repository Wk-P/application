<template>
    <nav class="brand-bar">
        <ul>
            <li v-for="(brand, index) in brandList">
                <div>{{ brand }}</div>
            </li>
        </ul>
    </nav>
</template>

<script lang="ts" setup name="BrandBar">
import { ref } from "vue";
const brandList = ref<Array<string>>(["brand1", "brand2", "brand3", "brand4", "brand5", "brand6", "brand7", "brand8"]);
</script>

<style scoped>
.brand-bar {
    box-sizing: border-box;
    padding: 1rem;
    width: 100%;
    display: flex;
    flex-direction: row;
}

.brand-bar > ul {
    width: 100%;
    list-style: none;
    display: flex;
    flex-direction: row;
    justify-content: space-evenly;
    align-content: space-evenly;
    flex-wrap: wrap;
}

.brand-bar > ul > li {
    box-sizing: border-box;
    width: 25%;
    height: auto;
    aspect-ratio: 1 / 1;
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    align-content: center;
    justify-content: center;
    padding: 0.5rem;
}

.brand-bar > ul > li > div {
    box-sizing: border-box;
    width: 100%;
    height: auto;
    aspect-ratio: 1 / 1;
    background-color: rgba(155, 200, 50, 0.3);
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
}
</style>
