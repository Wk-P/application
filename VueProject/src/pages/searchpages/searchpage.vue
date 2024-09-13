<template>
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <div class="container">
        <div class="left">
            <button @click="backToPrev">
                <img src="/src_img/backarrow.png" alt="" />
            </button>
        </div>
        <div class="middle">
            <input type="text" ref="searchInput"/>
        </div>
        <div class="right">
            <button @click="search">
                <img src="/src_img/search1.png" alt="search_img"/>
            </button>
        </div>
    </div>
</template>

<script lang="ts" setup name="search">
import { onMounted, ref } from "vue";
import { useRouter } from "vue-router";

const router = useRouter();
const searchInput = ref<HTMLInputElement | null>(null);

const backToPrev = () => {
    router.back();
}

const search = () => {
    alert("search");
}

onMounted(() => {
    searchInput.value?.focus();
})

</script>

<style scoped>
.container {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    height: 2rem;
    padding: 0.7rem;
}

.container > div {
    height: 100%;
}

.middle {
    flex: 1;
    padding: 0 1rem;
}

input {
    display: block;
    box-sizing: border-box;
    height: 100%;
    width: 100%;
    background-color: #eee;
    border-radius: 1rem;
    padding: 0 1rem;
    border: none;
    outline: none;
}

button {
    display: block;
    height: 100%;
    border: none;
    background-color: white;
}

button img {
    box-sizing: border-box;
    height: 100%;
}

.right button img {
    padding: 0.25rem;
}

input {
    -webkit-user-select: none;
    user-select: none;
    -webkit-text-size-adjust: 100%; /* 防止 iOS 缩放 */
    -ms-text-size-adjust: 100%;
    text-size-adjust: 100%;
}
</style>
