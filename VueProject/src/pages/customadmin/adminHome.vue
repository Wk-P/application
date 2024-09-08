<template>
    <div class="wel">
        Welcome to Custom Admin System
        <a :href="adminUrl" target="_blank">to Django Admin System</a>
    </div>
</template>

<script lang="ts" setup name="adminHome">
import { computed } from "vue";

// 这里可以从环境变量中读取当前环境
const isProduction = import.meta.env.MODE === "production";

const adminUrl = computed(() => {
    return isProduction
        ? "https://cskbusiness.com/admin"
        : "http://localhost:8000/admin";
});
</script>

<style>
.wel {
    height: 60vh;
    width: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}
</style>
