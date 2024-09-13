<template>
    <h1>Usercenter</h1>
</template>

<script lang="ts" setup name="usercenterhomepage">
import { RouterView, RouterLink, useRoute } from "vue-router";

const route = useRoute();

</script>
<style scoped>
nav {
    box-sizing: border-box;
    width: 100%;
    padding-bottom: 2em;
    display: flex;
    justify-content: space-evenly;
}
nav a {
    height: 100%;
    padding: 1.5rem 4rem;
    font-size: 0.8rem;
    text-decoration: none;
    border: 1px solid black;
    color: black;
}
</style>
