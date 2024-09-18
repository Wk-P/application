<template>
    <nav class="brand-bar">
        <ul>
            <li v-for="(brand, index) in brandList">
                {{ brand }}
            </li>
        </ul>
    </nav>
</template>

<script lang="ts" setup name="BrandBar">
import { ref } from "vue";
const brandList = ref<Array<string>>([
    "brand1",
    "brand2",
    "brand3",
    "brand4",
    "brand5",
    "brand6",
    "brand7",
    "brand8",
]);
</script>

<style scoped>
.brand-bar {
    width: 100%;
    display: flex;
    flex-direction: row;
    
}

.brand-bar ul {
    list-style: none;
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
}


.brand-bar ul li {
    width: 25%;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    height: 7rem;
}
</style>
