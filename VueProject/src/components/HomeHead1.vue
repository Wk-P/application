<template>
    <nav>
        <ul>
            <li v-for="(item, index) in navItems" :key="index">
                <RouterLink v-if="index !== 1" :to="{ name: item.routeName }">
                    <img :src="item.imgSrc" :alt="item.altText" />
                </RouterLink>
                <RouterLink
                    v-else
                    :to="{}"
                    @click="$event.preventDefault()"
                >
                    <img :src="item.imgSrc" :alt="item.altText" />
                </RouterLink>
            </li>
        </ul>
    </nav>
</template>

<script lang="ts" setup name="HomeHead1">
import { RouterLink } from "vue-router";
import { ref, onMounted } from "vue";

const navItems = ref([
    {
        routeName: "home",
        imgSrc: "/src_img/ring1.png",
        altText: "ring",
        imgSrcInitial: "/src_img/ring1.png",
        imgSrcActive: "/src_img/ring.png",
    },
    {
        routeName: "home",
        imgSrc: "/src_img/title.png",
        altText: "brand",
        imgSrcInitial: "/src_img/title.png",
        imgSrcActive: "/src_img/title.png",
    },
    {
        routeName: "search",
        imgSrc: "/src_img/search1.png",
        altText: "search",
        imgSrcInitial: "/src_img/search1.png",
        imgSrcActive: "/src_img/search.png",
    },
    {
        routeName: "cart",
        imgSrc: "/src_img/cart1.png",
        altText: "cart",
        imgSrcInitial: "/src_img/cart1.png",
        imgSrcActive: "/src_img/cart.png",
    },
]);
</script>

<style scoped>
nav {
    box-sizing: border-box;
    display: flex;
    flex-direction: row;
    height: 3rem;
    width: 100%;
    overflow: auto;
    animation: 0.3s linear 0.1s slideIn;
}

nav > ul {
    box-sizing: border-box;
    background-color: white;
    height: 100%;
    width: 100vw;
    display: flex;
    list-style: none;
    flex-direction: row;
    justify-content: space-around;
    padding: 0 0.7rem;
}

nav > ul > li {
    box-sizing: border-box;
    height: 100%;
    width: 100%;
    text-align: center;
    scroll-snap-align: center;
    flex: 1;
}

nav > ul > li:nth-child(2) {
    flex: 8;
}

nav > ul > li > a {
    display: flex;
    align-items: center;
    box-sizing: border-box;
    height: 100%;
    flex-direction: column;
    justify-content: center;
    text-decoration: none;
    color: black;
    -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
}

nav > ul > li > a > img {
    box-sizing: border-box;
    display: flex;
    height: 100%;
    object-fit: fill;
    padding: 0.8rem;
    pointer-events: none; /* 避免图片本身的点击事件 */
}

@keyframes slideIn {
    from {
        opacity: 0;
        transform: translateY(-5rem);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}
</style>
