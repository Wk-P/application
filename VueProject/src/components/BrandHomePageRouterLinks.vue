<template>
    <nav>
        <ul>
            <li
                v-for="(link, index) in linksList"
                :key="index"
                @click="changeHandle(index, $event)"
            >
                <RouterLink
                    :to="{ name: link.hrefName }"
                    :style="{
                        backgroundColor: getBackgroundColor(index),
                        color: getTextColor(index),
                    }"
                    >{{ link.textContent.en }}</RouterLink
                >
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
const childrenRoutePath = findChildrenRoutePath("brand", router);

const linksTextContent = [
    { en: "LV" },
    { en: "CHANEL" },
    { en: "HERMES" },
    { en: "CARTIER" },
    { en: "VANCLEEF" },
    { en: "DIOR" },
    { en: "BULAGLI" },
    { en: "TIFFANY" },
    { en: "OTHERS" },
];

const linksList = ref(
    childrenRoutePath.map((child, index) => ({
        hrefName: child.name,
        textContent: linksTextContent[index],
        style: linkStyle,
    }))
);

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

nav > ul {
    width: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
    list-style: none;
}

nav > ul > li {
    width: 100%;
    text-align: center;
}

nav > ul > li > a {
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    justify-content: center;
    text-align: center;
    height: 100%;
    width: 100%;
    color: black;
    padding: 1rem 0;
    text-decoration: none;
}
</style>
