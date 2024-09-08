<template>
    <div class="nav-bar">
        <button @click="returnStart">
            <div class="img-block"><img src="/arrow-left.png" alt="" /></div>
        </button>
    </div>
</template>

<script lang="ts" setup name="ReturnBar">
import { useRouter } from "vue-router";
const router = useRouter();
const returnStart = () => {
    router.push({ name: "start" });
};
</script>

<style scoped>
.nav-bar {
    width: 100%;
    background-color: gray;
    height: 5vh;
}

.nav-bar button {
    height: 100%;
    background-color: gray;
    border: none;
}

.img-block {
    height: 100%;
}

.img-block img {
    height: 100%;
}
</style>
