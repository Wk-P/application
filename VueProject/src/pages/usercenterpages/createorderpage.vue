<template>
    <ReturnBar />
    <div class="container">
        <div class="address-block">
            <span><strong>배송지</strong></span>
            <RouterLink :to="{ name: ''}" class="link">배송지 관리</RouterLink>
        </div>
        <div class="address-block-1">
            <div></div>
        </div>
        <ul class="order-items-list">
            <li v-for="(item, index) in itemsList">
                <div class="img-block">
                    <img
                        v-if="item.images && item.images.length > 0"
                        :src="item.images[0].image"
                        alt=""
                    />
                </div>
                <div class="quantity-block">
                    <h3>Quantity</h3>
                    <div class="quantity-container">
                        <button @click="subQuantity(index)">-</button>
                        <input type="text" v-model="listOfQuatity[index]" />
                        <button @click="addQuantity(index)">+</button>
                    </div>
                </div>
                <div class="info-block">
                    <span
                        ><strong>{{ item.name }}</strong></span
                    >
                    <span class="price"
                        ><strong>$ {{ item.price }}</strong></span
                    >
                </div>
            </li>
        </ul>
        <div class="button-group">
            <button @click="createOrders">Create Order</button>
        </div>
    </div>
    <!-- 付款信息 -->
    <teleport to="body">
        <div v-if="showModal" class="modal">
            <div class="head">
                <span><strong>Pay</strong></span
                ><button @click="showModal = false">X</button>
            </div>
            <p>Way of pay</p>
            <button @click="closeModal(newOrders)" class="close-button">
                Close Modal
            </button>
        </div>
    </teleport>
</template>

<script lang="ts" setup name="createorderpage">
import type { Order, Item, User } from "@/types/index";
import { useRouter, useRoute } from "vue-router";
import {
    useItemStore,
    useOrderStore,
    useItemsListStore,
    useOrdersListStore,
    useUserStore,
} from "@/stores/index";
import { ref, onMounted } from "vue";
import ReturnBar from "@/components/ReturnBar.vue";
const itemStore = useItemStore();
const orderStore = useOrderStore();
const router = useRouter();
const userStore = useUserStore();
const ordersListStore = useOrdersListStore();
const itemsListStore = useItemsListStore();

const listOfQuatity = ref<Array<number>>([]);
const itemsList = ref<Array<Item>>(itemsListStore.itemsList as Array<Item>);

let newOrders = Array<Order>();

const addQuantity = (index: number) => {
    listOfQuatity.value[index] += 1;
};

const subQuantity = (index: number) => {
    if (listOfQuatity.value[index] >= 1) {
        listOfQuatity.value[index] -= 1;
    }
};

const createOrder = (item: Item, quantity: number) => {
    const newOrder: Order = {
        orderId: "",
        user: userStore.user as User,
        item: item,
        quantity: quantity,
        totalPrice: quantity * item.price,
        createdTime: "",
        updatedTime: "",
        status: undefined,
        tracking_number: undefined,
    };
    return newOrder;
};

const showModal = ref(false);

const closeModal = (newOrders: Array<Order>) => {
    showModal.value = false;
    postRequestOrders(newOrders);
};

const postRequestOrders = (newOrders: Array<Order>) => {
    fetch(`/api/orders/create/`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            newOrders: newOrders,
        }),
    })
        .then((response) => {
            console.log(response);
            if (!response.ok) {
                response.json().then((error) => {
                    console.log(error);
                    throw new Error(
                        `Error! HTTP status code ${response.status}`
                    );
                });
            }
            return response.json();
        })
        .then((data) => {
            console.log(data);
            alert("주문생선됐습니다!");
            router.push({ name: "order" });
        })
        .catch((error) => console.log(error.message));
};

const createOrders = () => {
    itemsList.value.forEach((item) => {
        const quantityIndex = itemsList.value.findIndex(
            (i) => i.id === item.id
        );
        newOrders.push(createOrder(item, listOfQuatity.value[quantityIndex]));
    });
    ordersListStore.setOrdersList(newOrders);
    // 显示付款信息
    showModal.value = true;
};

onMounted(() => {
    itemsList.value = useItemsListStore().itemsList as Array<Item>;
    listOfQuatity.value = Array<number>(itemsList.value.length).fill(0);
});
</script>

<style scoped>
.address-block {
    box-sizing: border-box;
    padding: 0 1rem;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
}

.address-block .link {
    display: block;
    color: #aaa;
    text-decoration: none;
    border: 1px solid #aaa;
    padding: 0 0.5rem;
}

.modal {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background-color: white;
    padding: 20px;
    border: 1px solid #ccc;
    z-index: 1000;
    width: 50%;
}
.modal .head {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
}

.modal .head button {
    width: 2rem;
    height: 2rem;
    border: 1px solid border;
    background-color: white;
    border-radius: 0.3rem;
}

.modal .close-button {
    width: 100%;
    height: 3rem;
    margin-top: 2rem;
    border: 1px solid border;
    background-color: white;
    border-radius: 0.3rem;
}
.container {
    padding-top: 3rem;
    overflow-y: auto;
    height: calc(100% - 4rem);
}

.container > h2 {
    box-sizing: border-box;
    padding: 1rem;
    text-align: center;
}
.order-items-list {
    box-sizing: border-box;
    list-style: none;
    width: 100%;
    padding: 0.5rem 0.5rem 7rem 0.5rem;
    height: calc(100% - 4rem);
    overflow-y: auto;
    overflow-x: hidden;
}

.order-items-list > li {
    margin: 0.4rem 0;
    box-sizing: border-box;
    height: auto;
    padding: 0.4rem;
}

.img-block {
    height: 7rem;
    width: 100%;
}

.img-block img {
    height: 100%;
}

.quantity-block {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    text-align: center;
    align-items: center;
}

.quantity-block .quantity-container {
    display: flex;
    flex-direction: row;
    justify-content: center;
    padding: 0.3rem 0;
    box-sizing: border-box;
    height: 5vh;
}

.quantity-container button {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    height: 100%;
    box-sizing: border-box;
    border: black 1px solid;
    background-color: black;
    color: white;
    width: 2rem;
    font-size: 1.1rem;
}

.quantity-container input {
    box-sizing: border-box;
    height: 100%;
    padding: 0.2rem;
    width: 7rem;
    outline: none;
    border: 2px solid black;
    text-align: center;
}

.info-block {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
    width: 100%;
}

.price {
    font-size: 1.5rem;
    text-align: right;
}

.button-group {
    position: fixed;
    left: 0;
    bottom: 4rem;
    padding: 0.8rem 0;
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: space-evenly;
    box-shadow: 0 -4px 10px rgba(0, 0, 0, 0.1);
    height: 3rem;
}

.button-group button {
    padding: 0 0.5rem;
    background-color: white;
    margin: 0 0.5rem;
    color: black;
    border: 1px solid black;
    flex: 1;
}
</style>
