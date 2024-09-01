<template>
    <OptionHeader />
    <div class="content-block">
        <ul v-if="cartItemsList.length > 0" class="item-list">
            <li v-for="item in cartItemsList">
                <div class="left-check-box-style">
                    <input
                        type="checkbox"
                        :value="item.id"
                        v-model="selectedItems"
                    />
                </div>
                <div class="right-info-box-style">
                    <div class="up-others-block">
                        <div class="left-item-img">
                            <img :src="`${item.imgLink}`" alt="" />
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
                        <span>Price:</span><span>{{ item.price }}</span>
                    </div>
                </div>
            </li>
        </ul>
        <div v-else class="empty-hint">쇼핑 카트가 비어 있습니다.</div>
    </div>
    <div class="bottom-block" ref="btmBlockDiv">
        <button @click="order">주문</button>
        <button @click="deleteHandle">삭제</button>
    </div>
    <footer class="footer-block" ref="footerBlock"><FooterBlock /></footer>
</template>

<script lang="ts" setup name="Cart">
import { useUserStore } from "@/stores/index";
import OptionHeader from "@/components/OptionHeader.vue";
import type { Item } from "@/types/index";
import { ref, onMounted, onUnmounted, computed } from "vue";
import FooterBlock from "@/components/FooterBlock.vue";

const selectedItems = ref<string[]>([]);
const selectedCartItems = computed(() => {
    return cartItemsList.value.filter((item) =>
        selectedItems.value.includes(item.id)
    );
});

const deleteHandle = () => {
    if (selectedItems.value.length === 0) {
        alert("No items selected to delete.");
        return;
    }

    // 过滤掉选中的项
    cartItemsList.value = cartItemsList.value.filter(
        (item) => !selectedItems.value.includes(item.id)
    );

    // 清空选中的复选框
    selectedItems.value = [];
};

const btmBlockDiv = ref<HTMLElement | null>(null);
const footerBlock = ref<HTMLElement | null>(null);
const cartItemsList = ref<Array<Item>>([]);
const userStore = useUserStore();

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
            (btmBlockDiv.value as HTMLDivElement).style.position = "relative";
        } else {
            (btmBlockDiv.value as HTMLDivElement).style.position = "fixed";
        }
    }
};

const fetchAllCartItems = (username: string) => {
    fetch(`api/items/cart/${username}`)
        .then((response) => {
            if (!response.ok) {
                throw new Error(`Error! HTTP status code ${response.status}`);
            }
            return response.json();
        })
        .then((data) => {
            cartItemsList.value = data;
            console.log(cartItemsList.value);
        });
};

onMounted(() => {
    window.addEventListener("scroll", handleScroll);
    handleScroll(); // 初始化时检查

    const username = userStore.user?.username;
    if (username !== null && username !== undefined && username !== "") {
        fetchAllCartItems(username);
    }
});

onUnmounted(() => {
    window.removeEventListener("scroll", handleScroll);
});

const order = () => {
    alert("No function");
};
</script>

<style scoped>
.empty-hint {
    box-sizing: border-box;
    text-align: center;
    padding: 33vh 5vh;
    width: 100%;
}

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
    background-color: white;
    border: 1px solid grey;
}

.left-item-img img {
    width: 100%;
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
    display: flex;
    flex-direction: row;
    justify-content: space-around;
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
    -webkit-appearance: none;
    -moz-appearance: none;
    appearance: none;
    box-sizing: border-box;
    width: 100%;
    height: 100%;
    background-color: white;
    padding: 0.8rem 0;
    border: 1px solid black;
    font-size: 1rem;
    color: black;
    cursor: pointer;
    text-align: center;
    outline: none;
    margin: 0.5rem 0;
}

.bottom-block button:active {
    background-color: #e0e0e0; /* 按钮点击时背景颜色变为更深的灰色 */
}
</style>
