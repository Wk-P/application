<template>
    <div class="container">
        <RouterView></RouterView>
    </div>
    <FooterBlock />
</template>

<script lang="ts" setup>
import { RouterView } from "vue-router";
import FooterBlock from "@/components/FooterBlock.vue";
</script>

<style scoped>
.container {
    height: 100%;
    padding-bottom: 4rem;
}
</style>
