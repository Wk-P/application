<template>
    <HomeHead1 />
    <HomeHead2 />
    <div class="page-view-container">
        <RouterView></RouterView>
        <BrandBar />
        <ItemsViewComponents />
    </div>
</template>

<script lang="ts" setup name="homepage">
import HomeHead1 from "@/components/HomeHead1.vue";
import HomeHead2 from "@/components/HomeHead2.vue";
import BrandBar from "@/components/BrandBar.vue";
import ItemsViewComponents from "@/components/ItemsViewComponents.vue";
import { RouterView } from "vue-router";
</script>

<style scoped>
.page-view-container {
    height: calc(100% - 11rem);
    box-sizing: border-box;
    width: 100%;
    padding-bottom: 4rem;
    overflow-x: hidden;
    overflow-y: auto;
    scrollbar-width: none; /* firefox */
    -ms-overflow-style: none; /* IE 10+ */
}

.page-view-container::-webkit-scrollbar {
    display: none;
}
</style>
