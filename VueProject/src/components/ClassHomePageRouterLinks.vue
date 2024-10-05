<template>
    <nav>
        <ul>
            <li
                v-for="(object, index) in linksList"
                :key="index"
                @click="changeHandle(index, $event)"
            >
                <RouterLink
                    :to="{ name: object.hrefName }"
                    :style="{
                        backgroundColor: getBackgroundColor(index),
                        color: getTextColor(index),
                    }"
                    >{{ object.textContent }}</RouterLink
                >
            </li>
        </ul>
    </nav>
</template>

<script lang="ts" setup name="ClassHomePageRouterLinks">
import SearchBar from "@/components/SearchBar.vue";
import { RouterLink, useRoute } from "vue-router";
import { ref, computed, onMounted, watch, onUnmounted, nextTick } from "vue";
const route = useRoute();
const activeIndex = ref<number>(0);
const linkStyle = {
    initialBackgroundColor: "#eee",
    activeBackgroundColor: "black",
    activeColor: "white",
    initialColor: "black",
};

const classNameTextList = [
    { korean: "목걸이", english: "Necklace", hrefName: "class_necklace" },
    { korean: "팔찌", english: "Bracelet", hrefName: "class_bracelet" },
    { korean: "반지", english: "Ring", hrefName: "class_ring" },
    { korean: "귀걸이", english: "Earrings", hrefName: "class_earrings" },
    { korean: "기타", english: "Others", hrefName: "class_others" },
    { korean: "남성", english: "Men", hrefName: "class_men" },
    { korean: "여성", english: "Women", hrefName: "class_women" },
    { korean: "커플", english: "Couple", hrefName: "class_couple" },
];

const linksList = ref(
    classNameTextList.map((textContent, index) => {
        return {
            hrefName: `${textContent.hrefName}`,
            style: linkStyle,
            textContent: textContent.korean,
        };
    })
);

console.log(linksList.value);

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
