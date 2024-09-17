<template>
    <ReturnBar />
    <div v-if="isAdminLoggedIn" class="container">
        <adminhome />
    </div>
    <div v-else class="container">
        <AdminLogin />
    </div>
</template>

<script lang="ts" setup name="adminnav">
import { ref, computed } from "vue";
import { useAdminStore } from "@/stores/index";
import AdminLogin from "@/components/AdminComponents/Login.vue";
import ReturnBar from "@/components/ReturnBar.vue";
import adminhome from "@/pages/adminpages/adminhome.vue";

const adminStore = useAdminStore();
const isAdminLoggedIn = computed(() => {
    return adminStore.adminuser?.loginStatus && adminStore.adminuser?.username === 'admin';
});

</script>

<style scoped>
.container {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding-top: 2.8rem;
    padding-bottom: 4rem;
    height: calc(100% - 6.8rem);
}
</style>
