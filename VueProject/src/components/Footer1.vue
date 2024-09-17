<template>
    <nav>
        <ul>
            <li v-for="(item, index) in navItems" :key="index">
                <RouterLink
                    :to="{ name: item.routeName }"
                    @click="changeImage(index)"
                >
                    <img :src="item.imgSrc" :alt="item.altText" />
                    <div>{{ item.label }}</div>
                </RouterLink>
            </li>
        </ul>
    </nav>
</template>

<script lang="ts" setup name="Footer1">
import { RouterLink, useRoute } from "vue-router";
import { ref, onMounted, computed, watch, onUnmounted } from "vue";

const route = useRoute();
const navItems = ref([
    {
        routeName: "class",
        imgSrc: "/src_img/lines1.png",
        altText: "class",
        label: "CLASS",
        imgSrcInitial: "/src_img/lines1.png",
        imgSrcActive: "/src_img/lines.png",
    },
    {
        routeName: "brand",
        imgSrc: "/src_img/brand1.png",
        altText: "brand",
        label: "BRAND",
        imgSrcInitial: "/src_img/brand1.png",
        imgSrcActive: "/src_img/brand.png",
    },
    {
        routeName: "home",
        imgSrc: "/src_img/home1.png",
        altText: "home",
        label: "HOME",
        imgSrcInitial: "/src_img/home1.png",
        imgSrcActive: "/src_img/home.png",
    },
    {
        routeName: "favorite",
        imgSrc: "/src_img/heart1.png",
        altText: "favorite",
        label: "FAVORITE",
        imgSrcInitial: "/src_img/heart1.png",
        imgSrcActive: "/src_img/heart.png",
    },
    {
        routeName: "user",
        imgSrc: "/src_img/user1.png",
        altText: "user",
        label: "USER",
        imgSrcInitial: "/src_img/user1.png",
        imgSrcActive: "/src_img/user.png",
    },
]);

// 切换图片的方法
const changeImage = (index: number) => {
    // 确保 index 有效
    if (index < 0 || index >= navItems.value.length) {
        return; // 或者其他处理逻辑
    }

    // 重置所有图片为初始状态
    navItems.value.forEach((item) => {
        item.imgSrc = item.imgSrcInitial;
    });

    // 切换当前点击项的图片为不带 '1' 的版本
    const item = navItems.value[index];
    item.imgSrc = item.imgSrcActive;
};

// 计算当前索引的方法
const computeIndex = () => {
    // 获取顶级路由名称
    const topLevelRoute = route.matched[0]?.name;

    // 查找匹配的索引
    const index = navItems.value.findIndex((item) => {
        return topLevelRoute === item.routeName;
    });

    // 返回索引，或者返回 -1 表示未找到
    return index !== -1 ? index : -1;
};

// 监听 route.matched 的变化
const imgSrcWatcher = watch(
    () => route.matched,
    (newMatched) => {
        // 确保 route.matched 有值
        if (newMatched.length > 0) {
            const index = computeIndex();
            if (index !== -1) {
                changeImage(index);
            }
        }
    },
    { immediate: true } // 立即执行一次 watch 回调
);

onMounted(() => {
    // 确保在挂载时进行图片切换
    if (route.matched.length > 0) {
        const index = computeIndex();
        if (index !== -1) {
            changeImage(index);
        }
    }
});

onUnmounted(() => {
    imgSrcWatcher();
});
</script>

<style scoped>
nav {
    position: fixed;
    bottom: 0;
    left: 0;
    box-sizing: border-box;
    display: flex;
    flex-direction: row;
    height: 4rem;
    width: 100%;
    animation: 0.3s linear 0.1s slideIn;
    box-shadow: 0 -2px 20px 1px rgba(0, 0, 0, 0.1);
    z-index: 1000;
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
}

nav > ul > li {
    box-sizing: border-box;
    height: 100%;
    width: 100%;
    margin: 0 0.4rem;
    text-align: center;
    scroll-snap-align: center;
}

nav > ul > li > a {
    display: flex;
    flex-direction: column;
    align-items: center;
    box-sizing: border-box;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    text-decoration: none;
    color: black;
    -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
}

nav > ul > li > a > img {
    box-sizing: border-box;
    display: flex;
    height: 60%;
    object-fit: fill;
    padding: 0.5rem;
    pointer-events: none;
}

nav > ul > li > a > div {
    font-size: 0.55rem;
    text-align: center;
}

@keyframes slideIn {
    from {
        opacity: 0;
        transform: translateY(5rem);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}
</style>
