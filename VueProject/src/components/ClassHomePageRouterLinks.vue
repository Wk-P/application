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
                        color: getTextColor(index)
                    }"
                    >{{ object.textContent }}</RouterLink
                >
            </li>
        </ul>
    </nav>
</template>

<script lang="ts" setup name="ClassHomePageRouterLinks">
import { RouterLink } from "vue-router";
import { ref } from "vue";
const activeIndex = ref<number>(0);
const linkStyle = {
    initialBackgroundColor: "#eee",
    activeBackgroundColor: "black",
    activeColor: "white",
    initialColor: "black",
};

const linksList = ref([
    {
        hrefName: "classpage1",
        textContent: "page1",
        style: linkStyle,
    },
    {
        hrefName: "classpage2",
        textContent: "page2",
        style: linkStyle,
    },
    {
        hrefName: "classpage2",
        textContent: "page2",
        style: linkStyle,
    },
    {
        hrefName: "classpage3",
        textContent: "page3",
        style: linkStyle,
    },
    {
        hrefName: "classpage4",
        textContent: "page4",
        style: linkStyle,
    },
    {
        hrefName: "classpage5",
        textContent: "page5",
        style: linkStyle,
    },
    {
        hrefName: "classpage5",
        textContent: "page5",
        style: linkStyle,
    },
    {
        hrefName: "classpage5",
        textContent: "page5",
        style: linkStyle,
    },
    {
        hrefName: "classpage5",
        textContent: "page5",
        style: linkStyle,
    },
    {
        hrefName: "classpage5",
        textContent: "page5",
        style: linkStyle,
    },
    {
        hrefName: "classpage5",
        textContent: "page5",
        style: linkStyle,
    },
]);

const changeHandle = (index: number, event: Event) => {
    event.preventDefault();
    activeIndex.value = index;
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
    return activeIndex.value === index
        ? style.activeColor
        : style.initialColor;
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
    padding: 1.5rem 2.25rem;
    text-decoration: none;
}
</style>
