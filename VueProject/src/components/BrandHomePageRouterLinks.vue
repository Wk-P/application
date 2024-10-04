<template>
    <nav>
        <ul>
            <li v-for="(object, index) in linksList" :key="index" @click="changeHandle(index, $event)">
                <RouterLink :to="{ name: object.hrefName }" :style="{
                    backgroundColor: getBackgroundColor(index),
                    color: getTextColor(index),
                }">{{ object.textContent }}</RouterLink>
            </li>
        </ul>
    </nav>
</template>

<script lang="ts" setup name="BrandHomePageRouterLinks">
import { RouterLink, useRouter } from "vue-router";
import { findChildrenRoutePath } from "@/utils/utils";
import { ref, computed, onMounted, watch, onUnmounted, nextTick } from "vue";
const activeIndex = ref<number>(0);
const linkStyle = {
    initialBackgroundColor: "#eee",
    activeBackgroundColor: "black",
    activeColor: "white",
    initialColor: "black",
};

const router = useRouter();
const childrenRoutePath = findChildrenRoutePath('brand', router);

const linksTextContent = [
    "LV", "CHANEL", "HERMES", "CARTIER", "VANCLEEF", "DIOR", "BULAGLI", "TIFFANY"
]

const linksList = ref(
    childrenRoutePath.map((child, index) => ({
        hrefName: child.name,
        textContent: linksTextContent[index],
        style: linkStyle,
    }))
)

const linksListss = ref([
    {
        hrefName: "brandpage1",
        textContent: "brand1",
        style: linkStyle,
    },
    {
        hrefName: "brandpage2",
        textContent: "brand2",
        style: linkStyle,
    },
    {
        hrefName: "brandpage3",
        textContent: "brand3",
        style: linkStyle,
    },
    {
        hrefName: "brandpage4",
        textContent: "brand4",
        style: linkStyle,
    },
    {
        hrefName: "brandpage5",
        textContent: "brand5",
        style: linkStyle,
    },
]);

let timerId: number | undefined;
const changeHandle = (index: number, event: Event) => {
    event.preventDefault();
    activeIndex.value = index;
    nextTick(() => {
        timerId = window.setTimeout(() => {
            const target = (event.target as HTMLElement).closest("a");
            if (target) {
                target.scrollIntoView({
                    behavior: "smooth",
                    inline: "start",
                    block: "nearest",
                });
            } else {
                console.error("Target element not found.");
            }
        }, 100); // 适当调整延迟时间
    });
};

// 获取背景颜色
const getBackgroundColor = (index: number) => {
    const style = linksList.value[index]?.style || linkStyle;
    return activeIndex.value === index
        ? style.activeBackgroundColor
        : style.initialBackgroundColor;
};

// 获取文本颜色
const getTextColor = (index: number) => {
    const style = linksList.value[index]?.style || linkStyle;
    return activeIndex.value === index ? style.activeColor : style.initialColor;
};

</script>

<style scoped>
nav {
    width: 100%;
}

nav>ul {
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    list-style: none;
}

nav>ul>li {
    width: 100%;
    text-align: center;
}

nav>ul>li>a {
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    justify-content: center;
    text-align: center;
    height: 100%;
    width: 100%;
    color: black;
    padding: 1.5rem 2.25rem;
    text-decoration: none;
}
</style>
