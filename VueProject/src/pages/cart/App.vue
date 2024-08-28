<template>
    <OptionHeader />
    <div class="content-block">
        <ul class="item-list">
            <li v-for="item in itemList">
                <div class="left-check-box-style">
                    <input type="checkbox" />
                </div>
                <div class="right-info-box-style">
                    <div class="up-others-block">
                        <div class="left-item-img">
                            <img src="" alt="" />
                        </div>
                        <div class="right-label">
                            <ul>
                                <li class="title">{{ item.title }}</li>
                                <li>
                                    <span>{{ item.desc }}</span>
                                </li>
                                <li>{{ item.name }}</li>
                                <li>option</li>
                            </ul>
                        </div>
                    </div>
                    <div class="down-price-block">
                        {{ item.price }}
                    </div>
                </div>
            </li>
        </ul>
    </div>
    <div class="bottom-block" ref="btmBlockDiv">
        <button @click="order">주문함</button>
    </div>
    <footer class="footer-block" ref="footerBlock"><FooterBlock /></footer>
</template>

<script lang="ts" setup name="Cart">
import OptionHeader from "@/components/OptionHeader.vue";
import type { Item } from "@/types/index";
import { ref, onMounted, onUnmounted } from "vue";
import FooterBlock from "@/components/FooterBlock.vue";

const btmBlockDiv = ref<HTMLElement | null>(null);
const footerBlock = ref<HTMLElement | null>(null);

const handleScroll = () => {
    if (footerBlock.value) {
        const footerRect = footerBlock.value.getBoundingClientRect();
        const windowHeight = window.innerHeight;
        const distanceFromBottom =
            document.documentElement.scrollHeight -
            windowHeight -
            window.scrollY;

        const targetValue = footerRect.height;
        if (distanceFromBottom <= targetValue) {
            (btmBlockDiv.value as HTMLDivElement).style.position = 'relative';
        } else {
            (btmBlockDiv.value as HTMLDivElement).style.position = 'fixed';
        }
    }
};

onMounted(() => {
    window.addEventListener("scroll", handleScroll);
    handleScroll(); // 初始化时检查
});

onUnmounted(() => {
    window.removeEventListener("scroll", handleScroll);
});

const order = () => {
    alert("No function");
};

const itemList = ref<Array<Item>>([]);
const item = ref<Item>({
    id: "001",
    name: "item1",
    title: "가방1",
    desc: "가방, ㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎㅎ",
    price: 10,
});

for (let i = 0; i < 5; i++) {
    itemList.value.push(item.value);
}
</script>

<style scoped>
footer {
    width: 100%;
}
.content-block {
    box-sizing: border-box;
    width: 100%;
    padding: 0.5rem;
}
.item-list {
    box-sizing: border-box;
    width: 100%;
    padding: 0.5rem;
    box-sizing: border-box;
    list-style: none;
}
.item-list > li {
    display: flex;
    flex-direction: row;
    justify-content: center;
    box-sizing: border-box;
    padding: 0.5rem;
    border-bottom: 1px solid grey;
}

.left-check-box-style {
    box-sizing: border-box;
    padding: 0.5rem 1rem 0.5rem 0.1rem;
}

.left-check-box-style input {
    box-sizing: border-box;
    height: 20px;
    width: 20px;
}

.right-info-box-style {
    box-sizing: border-box;
    flex: 13;
}

.up-others-block {
    display: flex;
    flex-direction: row;
    width: 100%;
}

.left-item-img {
    width: 48%;
    background-color: gray;
}

.right-label {
    width: 70%;
}

.right-label ul {
    box-sizing: border-box;
    list-style: none;
    padding: 0.4rem;
    display: flex;
    flex-direction: column;
    justify-content: space-around;
}

.right-label ul li {
    padding: 0.5rem;
}

.right-label ul li span {
    display: block;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}
.right-label ul .title {
    font-size: 1.1rem;
    font-weight: bold;
}

.down-price-block {
    box-sizing: border-box;
    padding: 0.2rem;
    text-align: center;
    border: 1px solid grey;
    margin: 0.3rem 0;
}

.bottom-block {
    position: fixed;
    box-sizing: border-box;
    width: 100%;
    padding: 1rem;
    z-index: 2;
    bottom: 0;
    left: 0;
}

.bottom-block button {
    box-sizing: border-box;
    width: 100%;
    height: 100%;
    background-color: white;
    padding: 0.8rem 0;
}
</style>
