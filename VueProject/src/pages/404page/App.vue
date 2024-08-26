<template>
    <HeadHomeBar />
    <div class="block">
        <p>404</p>
        <p>Sorry, not found page.</p>
    </div>
    <FooterBlock />
</template>

<script lang="ts" setup name="NotFoundPage">
import FooterBlock from "@/components/FooterBlock.vue";
import HeadHomeBar from "@/components/HeadHomeBar.vue"
</script>

<style scoped>
.block {
    display: flex;
    flex-direction: column;
    justify-content: center;
    text-align: center;
    height: 80%;
}
</style>