<template>
    <div class="home-container">
        <div class="links">
            <RouterLink :to="{ name: 'adminitems' }">Items</RouterLink>
            <RouterLink :to="{ name: 'adminusers' }">User</RouterLink>
            <RouterLink :to="{ name: 'adminorders' }">Orders</RouterLink>
            <RouterLink :to="{ name: 'admincarts' }">Cart</RouterLink>
        </div>
        <div class="page-container">
            <RouterView />
        </div>
    </div>
</template>

<script lang="ts" setup name="adminhome">
import { RouterLink, RouterView } from "vue-router";
</script>

<style scoped>
.home-container {
    width: 100%;
    display: flex;
    flex-direction: column;
}

.home-container h3 {
    width: 100%;
    text-align: center;
}

.links {
    width: 100%;
    height: 3rem;
    display: flex;
    flex-direction: row;
    justify-content: space-around;
}

.links > a {
    height: 100%;
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    text-decoration: none;
    color: white;
    background-color: black;
}

.page-container {
    padding: 1rem;
    border: 2px solid black;
}
</style>
