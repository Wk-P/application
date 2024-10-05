<template>
    <div
        v-if="isLoggedIn"
        class="container">
        <usercenterhome />
    </div>
    <div
        v-else
        class="container">
        <LoginComponent />
    </div>
</template>

<script lang="ts" setup name="usercenternav">
    import { ref, computed } from "vue";
    import { RouterView, RouterLink, useRoute } from "vue-router";
    import { useUserStore } from "@/stores/index";
    import LoginComponent from "@/components/LoginComponent.vue";
    import usercenterhome from "@/pages/usercenterpages/usercenterhome.vue";
    const route = useRoute();
    const userStore = useUserStore();
    const isLoggedIn = computed(() => (userStore.user ? true : false));
</script>
<style scoped>
    .container {
        height: 100%;
        width: 100%;
        display: flex;
        flex-direction: column;
        overflow: auto;
    }

    form {
        box-sizing: border-box;
        padding: 0 5rem;
    }
</style>
