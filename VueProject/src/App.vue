<template>
    <div class="container">
        <RouterView></RouterView>
    </div>
    <Footer1 />
</template>

<script lang="ts" setup>
import { RouterView } from "vue-router";
import Footer1 from "@/components/Footer1.vue";
</script>

<style scoped>
.container {
    height: 100%;
    padding-bottom: 4rem;
}
</style>
