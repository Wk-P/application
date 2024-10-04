<template>
    <nav>
        <ul>
            <li v-for="(page, index) in pageLinks" :key="index">
                <RouterLink class="head2" :to="{ name: page.herfName }" :style="{
                    borderBottom:
                        activeIndex === index
                            ? page.style.activeBorderBottom
                            : page.style.initialBorderBottom,
                }" @click="changeLink(index, $event)">
                    {{ page.textContent }}
                </RouterLink>
            </li>
        </ul>
    </nav>
</template>

<script lang="ts" setup name="HomeHead2">
import { RouterLink, useRoute, useRouter } from "vue-router";
import { findChildrenRoutePath } from "@/utils/utils";
import { ref, nextTick, onUnmounted, watch, computed, onMounted } from "vue";
const activeIndex = ref<number>(0);
const route = useRoute();

const router = useRouter();
const childrenRoutePath = findChildrenRoutePath('home', router);

const ActiveLinkBorder = {
    weightNumber: 3,
    borderStyle: "solid",
    borderColor: "black",
    getStyle() {
        return `${this.weightNumber}px ${this.borderStyle} ${this.borderColor}`;
    },
};

const initialLinkBorder = {
    weightNumber: 3,
    borderStyle: "solid",
    borderColor: "white",
    getStyle() {
        return `${this.weightNumber}px ${this.borderStyle} ${this.borderColor}`;
    },
};

const linkStyle = {
    initialBorderBottom: initialLinkBorder.getStyle(),
    activeBorderBottom: ActiveLinkBorder.getStyle(),
};

const linksTextContent = [
    "BEST", "NEW", "HIQUAL", "VIP", "PAGE5", "PAGE6"
]

const pageLinks = ref(
    childrenRoutePath.map((child, index) => ({
        textContent: linksTextContent[index],
        herfName: child.name,
        style: linkStyle,
    }))
);

let timerId: number | undefined;
const changeLink = (index: number, event: Event) => {
    event.preventDefault();
    activeIndex.value = index;

    nextTick(() => {
        timerId = window.setTimeout(() => {
            const target = (event.target as HTMLElement).closest("a");
            if (target) {
                target.scrollIntoView({
                    behavior: "smooth",
                    inline: "center",
                    block: "nearest",
                });
            } else {
                console.error("Target element not found.");
            }
        }, 100); // 适当调整延迟时间
    });
};

const computeIndex = () => {
    const subLevelRoute = route.matched[1]?.name;
    const index = pageLinks.value.findIndex((link) => {
        return subLevelRoute === link.herfName;
    });
    return index !== -1 ? index : -1;
};

const scrollToElement = (target: HTMLElement) => {
    target.scrollIntoView({
        behavior: "smooth",
        inline: "center",
        block: "nearest",
    });
};

const initialScroll = () => {
    const index = computeIndex();
    activeIndex.value = index;

    nextTick(() => {
        // 找到目标元素并滚动到视图中
        const target = document.querySelectorAll(".head2")[
            index
        ] as HTMLElement;
        if (target) {
            scrollToElement(target);
        } else {
            console.error("Target element not found.");
        }
    });
};

onMounted(() => {
    initialScroll();
});

onUnmounted(() => {
    if (timerId) {
        clearTimeout(timerId); // 清除定时器，避免内存泄漏
    }
});
</script>

<style scoped>
nav {
    box-sizing: border-box;
    display: flex;
    flex-direction: row;
    height: 3rem;
    width: 100%;
    overflow-x: auto;
    scroll-snap-type: x mandatory;
    animation: 0.3s linear 0.1s slideIn;
}

nav::-webkit-scrollbar {
    display: none;
    /* Chrome Safari */
}

nav>ul {
    box-sizing: border-box;
    background-color: white;
    padding: 0 0.6rem;
    height: 100%;
    width: 1000vw;
    display: flex;
    list-style: none;
    flex-direction: row;
    justify-content: space-around;
}

nav>ul>li {
    box-sizing: border-box;
    height: 100%;
    width: 6rem;
    background-color: white;
    text-align: center;
    display: flex;
    flex-direction: column;
    justify-content: center;
    scroll-snap-align: center;
}

nav>ul>li>a {
    display: block;
    box-sizing: border-box;
    text-decoration: none;
    height: 100%;
    width: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    color: black;
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
