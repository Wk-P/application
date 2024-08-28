<template>
    <ul class="waterfall-ul">
        <li v-for="(url, index) in imgUrlList" :key="index">
            <img :src="url" alt="" />
            <div class="name-block">itemname</div>
            <div class="tool-block">
                <span>heart | </span>
                <span>cart</span>
            </div>
        </li>
    </ul>
    <p ref="loader" class="loader-text">{{ loaderText }}</p>
    <div class="to-top"><button v-if="loaderText != initLoadText" @click="scrollToTop" >Back to Top</button></div>
</template>

<script lang="ts" setup name="waterfallflow">
import { nextTick, onMounted, ref, onUnmounted } from "vue";

const imgUrlList = ref<Array<string>>([]);
const waitingImgUrlList = ref<Array<string>>([]);
// 像后端索要，（隐式）查询本地



imgUrlList.value = [
    "/img/image10.png",
    "/img/image12.png",
    "/img/image9.png",
    "/img/image11.png",
];
waitingImgUrlList.value = [
    "/img/image10.png",
    "/img/image12.png",
    "/img/image9.png",
    "/img/image11.png",

    "/img/image10.png",
    "/img/image12.png",
    "/img/image9.png",
    "/img/image11.png",

    "/img/image10.png",
    "/img/image12.png",
    "/img/image9.png",
    "/img/image11.png",
];

// to Top
const scrollToTop = () => {
    window.scrollTo({
        top: 0,
        behavior: "smooth", // smooth scrolling
    });
};

let waitingIndex = 0;

const loader = ref(null);
const isLoading = ref(false);
const initLoadText = "Loading...";
const loaderText = ref(initLoadText);

// simulate data loading
const loadMore = () => {
    if (isLoading.value) return;
    isLoading.value = true;

    if (waitingIndex >= waitingImgUrlList.value.length) {
        isLoading.value = false;
        loaderText.value = "- End -";
        return;
    }

    // simulate http request
    imgUrlList.value.push(waitingImgUrlList.value[waitingIndex]);
    waitingIndex += 1;
    imgUrlList.value.push(waitingImgUrlList.value[waitingIndex]);
    waitingIndex += 1;
    isLoading.value = false;
};

let observer: IntersectionObserver | null = null;

onMounted(() => {
    // 监视器对象
    // observer object
    observer = new IntersectionObserver(
        ([entry]) => {
            if (entry.isIntersecting) {
                loadMore();
            }
        },
        { threshold: 0.6 }
    );

    // bind target DOM element to observer （绑定监视对象）
    nextTick(() => {
        if (loader.value && observer) {
            observer.observe(loader.value);
        }
    });
});

onUnmounted(() => {
    // bind target 
    if (loader.value && observer) {
        observer.unobserve(loader.value);
    }
});
</script>

<style scoped>
.loader-text {
    text-align: center;
    font-size: 0.8rem;
    padding: 20px 0;
}

.to-top {
    text-align: center;
    font-size: 0.8rem;
    padding: 20px 0;
}

.to-top button {
    padding: 15px 20px;
    border: 1px solid #999;
    background-color: white;
    border-radius: 5px;
}

.name-block,
.tool-block {
    font-size: 0.8rem;
    padding-left: 20px;
}

.waterfall-ul {
    margin: 0 auto;
    height: auto;
    width: 85%;
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    list-style: none;
    padding: 50px 0;
}

.waterfall-ul li {
    border: 1px solid #888;
    display: flex;
    flex-direction: column;
}

.waterfall-ul li:nth-child(n + 2) {
    margin-top: -1px;
}

.waterfall-ul li:nth-child(odd) {
    box-sizing: border-box;
    width: 100%;
    grid-column: 1;
    grid-row: auto;
    transform: translateY(-25px);
}

.waterfall-ul li:nth-child(even) {
    box-sizing: border-box;
    margin-left: -1px;
    grid-column: 2;
    grid-row: auto;
    transform: translateY(15px);
}

.waterfall-ul li img {
    box-sizing: border-box;
    height: auto;
    width: 100%;
    height: 100%;
}
</style>
