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
                                <li class="option-style" @click="optionSelect">
                                    option
                                </li>
                            </ul>
                            <teleport to="body">
                                <div
                                    v-if="showPopup"
                                    class="popup-overlay"
                                    @click="closePopup"
                                >
                                    <div class="popup-content" @click.stop>
                                        <h3>Option</h3>
                                        <div>
                                            <h4>수량</h4>
                                            <div class="content">
                                                <button
                                                    class="sub"
                                                    @click="
                                                        subQuantity(
                                                            cartItemsList.indexOf(
                                                                item
                                                            )
                                                        )
                                                    "
                                                >
                                                    -
                                                </button>
                                                <div class="number-content">
                                                    <input
                                                        type="text"
                                                        v-model="optionQuantity"
                                                    />
                                                </div>
                                                <button
                                                    class="add"
                                                    @click="
                                                        addQuantity(
                                                            cartItemsList.indexOf(
                                                                item
                                                            )
                                                        )
                                                    "
                                                >
                                                    +
                                                </button>
                                            </div>
                                        </div>
                                        <button @click="closePopup">
                                            확인
                                        </button>
                                    </div>
                                </div>
                            </teleport>
                        </div>
                    </div>
                    <div class="down-price-block">
                        <span>Quantity:</span><span>{{ optionQuantity }}</span>
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
import {
    useUserStore,
    useOrderStore,
    useOrdersListStore,
} from "@/stores/index";
import OptionHeader from "@/components/OptionHeader.vue";
import FooterBlock from "@/components/FooterBlock.vue";
import type { Item, Order } from "@/types/index";
import { ref, onMounted, onUnmounted } from "vue";
import { useRouter } from "vue-router";

// 直接生成 order 变量管理多个 item
// cartItem 类要有 quantity
const ordersListStore = useOrdersListStore();
const orderStore = useOrderStore();
const optionQuantity = ref<number>(0);
const subQuantity = (index: number) => {
    optionQuantity.value -= 1;
    if (optionQuantity.value < 0) {
        optionQuantity.value = 0;
    }
    // 获取到 item 信息
    let itemsOption = JSON.parse(localStorage.getItem("item-option") as string);
    itemsOption[index] = optionQuantity.value;
};

const addQuantity = (index: number) => {
    optionQuantity.value += 1;
    if (optionQuantity.value < 0) {
        optionQuantity.value = 0;
    }
};

// 创建一个响应式的变量来控制悬浮层的显示
const showPopup = ref<boolean>(false);

// 关闭悬浮层的函数
const closePopup = () => {
    showPopup.value = false;
};

const selectedItems = ref<string[]>([]);
const deleteHandle = () => {
    if (!confirm(`선택하는 것을 삭제하겠습니까?`)) {
        return;
    }

    if (selectedItems.value.length === 0) {
        alert("삭제할 항목이 선택되지 않았습니다.");
        return;
    }

    // 过滤掉选中的项
    cartItemsList.value = cartItemsList.value.filter(
        (item) => !selectedItems.value.includes(item.id)
    );

    // 清空选中的复选框
    selectedItems.value = [];
};

const orderCartItems = ref<Array<Item>>([]);
const btmBlockDiv = ref<HTMLElement | null>(null);
const footerBlock = ref<HTMLElement | null>(null);
const cartItemsList = ref<Array<Item>>([]);
const userStore = useUserStore();
const router = useRouter();

const optionSelect = () => {
    showPopup.value = true;
};

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
    fetch(`/api/items/cart/${username}`)
        .then((response) => {
            if (!response.ok) {
                throw new Error(`Error! HTTP status code ${response.status}`);
            }
            return response.json();
        })
        .then((data) => {
            for (const d of data) {
                const newItem: Item = {
                    id: d.item.id,
                    name: d.item.name,
                    desc: d.item.desc,
                    title: d.item.title,
                    price: d.item.price,
                    imgLink: `/item_img/${d.item.filename}`,
                };
                cartItemsList.value.push(newItem);
            }
            localStorage.setItem(
                "item-option",
                JSON.stringify({
                    items: cartItemsList.value,
                    options: Array.from(
                        { length: cartItemsList.value.length },
                        () => 0
                    ),
                })
            );
        });
};

onMounted(() => {
    if (userStore.user === null) {
        router.push({ name: "login" });
    }

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
    orderCartItems.value = cartItemsList.value.filter((item) =>
        selectedItems.value.includes(item.id)
    );

    if (orderCartItems.value.length == 0) {
        return;
    }

    let orderedItems: Array<Order> = [];

    // 向后端传输 order 信息
    for (const i of orderCartItems.value) {
        if (optionQuantity.value == 0) {
            alert("Error quantity");
            return;
        }

        const newOrder: Order = {
            orderId: undefined,
            user: undefined,
            item: undefined,
            quantity: undefined,
            totalPrice: undefined,
            createdTime: undefined,
            updatedTime: undefined,
        };
        orderedItems.push(newOrder);
    }

    fetch("/api/orders/create/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            newOrders: orderedItems,
        }),
    })
        .then((response) => {
            if (!response.ok) {
                throw new Error(`Error! HTTP status code ${response.status}`);
            }
            return response.json();
        })
        .then((data) => {
            alert(JSON.stringify(data));
            cartItemsList.value = cartItemsList.value.filter(
                (item) => !selectedItems.value.includes(item.id)
            );
        })
        .catch((error) => console.error(error));
};
</script>

<style scoped>
.popup-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.5);
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 5;
}

.popup-content {
    background: white;
    width: 80%;
    height: 50%;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.popup-content > button {
    background-color: black;
    color: white;
    border: none;
    padding: 0.5rem 0.6rem;
}

.popup-content > h3 {
    display: block;
    padding: 0.3rem;
}

.popup-content h4 {
    display: block;
    width: 100%;
    text-align: center;
    padding-bottom: 0.7rem;
}

.content {
    display: flex;
    flex-direction: row;
    justify-content: space-evenly;
    box-sizing: border-box;
    height: 10vh;
    padding: 0.3rem;
    height: 6vh;
}

.content .sub,
.content .add {
    background-color: black;
    color: white;
    font-size: 2rem;
    text-align: center;
    height: 100%;
    width: 20vw;
}

.content .number-content {
    height: 100%;
    appearance: none;
    box-sizing: border-box;
    margin: 0 1rem;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.content .number-content input {
    box-sizing: border-box;
    height: 100%;
    border: 2px solid black;
    text-align: center;
    outline: none;
    font-size: 1.12rem;
}

.option-style {
    border: 1px solid grey;
    text-align: center;
    font-size: 0.8rem;
}
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
    padding: 0 0.4rem;
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
