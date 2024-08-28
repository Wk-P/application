<template>
    <div class="head-bar" @click="toHome"><img src="/img/home.png" alt="home"></div>
</template>

<script lang="ts" setup name="HomeBar">
import router from '@/router';

const toHome = () => {
    router.push({name: "home"}).catch((err) => {
        console.error(err.message);
    })
}

</script>

<style scoped>
.head-bar {
    height: 5vh;
    width: 100%;
    background-color: grey;
    padding: 0 0.3em;
    display: flex;
    flex-direction: row;
    justify-content: center;
}

.head-bar img {
    box-sizing: border-box;
    padding: 0.6em;
    height: 100%;
}
</style>