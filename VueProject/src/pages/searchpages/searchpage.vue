<template>
    <div class="container">
        <div class="left">
            <button @click="backToPrev">
                <img src="/src_img/backarrow.png" alt="" />
            </button>
        </div>
        <div class="middle">
            <input type="text" ref="searchInput" v-model="searchInputTextValue"/>
        </div>
        <div class="right">
            <button @click="search">
                <img src="/src_img/search1.png" alt="search_img"/>
            </button>
        </div>
    </div>
</template>

<script lang="ts" setup name="searchpage">
import { onMounted, ref } from "vue";
import { useRouter } from "vue-router";

const router = useRouter();

const searchInputTextValue = ref<string | undefined>("");
const searchInput = ref<HTMLInputElement | null>(null);

const backToPrev = () => {
    router.back();
}

const search = () => {
    alert("search");
}

</script>

<style scoped>
.container {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    height: 2rem;
    padding: 1rem;
}

.left, .right, .middle {
    box-sizing: border-box;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.left button, .right button {
    box-sizing: border-box;
    appearance: none;
    height: 100%;
    display: block;
    border: none;
    outline: none;
    background: none;
}

img {
    box-sizing: border-box;
    height: 100%;
    padding: 0.25rem;
}

.middle {
    box-sizing: border-box;
    flex: 1;
    padding: 0 1rem;
}

.middle input {
    width: 100%;
    box-sizing: border-box;
    border-radius: 2rem;
    padding: 0.5rem 1rem;
    outline: none;
    background-color: #eee;
    border: 1px solid #eee;
}
</style>