<template>
    <div class="app-container">
        <RouterView></RouterView>
    </div>
    <Footer1 />
</template>

<script lang="ts" setup>
import { RouterView } from "vue-router";
import Footer1 from "@/components/Footer1.vue";
</script>

<style scoped>
.app-container {
    padding-bottom: 4rem;
}
</style>
