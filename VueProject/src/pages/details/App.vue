<template>
    <div>
        <h1>Product Details</h1>
        <p>Product ID: {{ id }}</p>
        <!-- 你可以添加更多的商品详细信息展示 -->
    </div>
</template>

<script lang="ts" setup name="Details">
import { useRoute } from "vue-router";
import { ref } from "vue";
const route = useRoute();
const id = route.params.id as string;
</script>

<style scoped></style>
