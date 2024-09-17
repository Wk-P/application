<template>
    <HomeHead1 />
    <HomeHead2 />
    <RouterView></RouterView>
</template>

<script lang="ts" setup name="homepage">
import HomeHead1 from "@/components/HomeHead1.vue";
import HomeHead2 from "@/components/HomeHead2.vue";
import { RouterView } from "vue-router";
</script>

<style scoped>

</style>