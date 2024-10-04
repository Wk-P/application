<template>
    <h3>Earrings</h3>
    <div class="head-img">
        <img src="" alt="head image">
    </div>
    <RouterLink :to="{ name: 'earrings' }" class="link">
        <div>전채 보시</div>
        <img src="/arrow-right.png" alt="">
    </RouterLink>
    <HotBrandBlock />
</template>

<script lang="ts" setup name="earringspage">
import HotBrandBlock from "@/components/HotBrandBlock.vue";
import { RouterLink } from "vue-router";



</script>

<style scoped>
h3 {
    padding: 0 1rem;
}

.link {
    box-sizing: border-box;
    display: flex;
    text-decoration: none;
    color: black;
    flex-direction: row;
    width: 100%;
    height: 3rem;
    align-items: center;
    justify-content: space-between;
    padding: 0 1rem;
    margin: 1rem 0;
}

.link div {
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    flex: 1;
}

.head-img {
    height: 6rem;
    width: 100%;
    box-sizing: border-box;
    padding: .5rem;
}

.head-img img {
    border: 1px solid black;
    height: 100%;
    width: 100%;
}
</style>