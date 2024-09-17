<template>
    <ReturnBar />
    <div class="container">
        <h2>Create Order page</h2>
        <ul class="order-items-list">
            <li v-for="(item, index) in itemsList">
                <div class="img-block">
                    <img :src="item.imgLink" alt="" />
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
                    <span><strong>{{ item.name }}</strong></span>
                    <span class="price"><strong>$ {{ item.price }}</strong></span>
                </div>
            </li>
        </ul>
        <div class="button-group">
            <button @click="createOrder">Create Order</button>
        </div>
    </div>
</template>

<script lang="ts" setup name="createorderpage">
import type { Order, Item } from "@/types/index";
import { useItemStore, useOrderStore, useItemsListStore, useOrdersListStore } from "@/stores/index";
import { ref, onMounted } from "vue";
import ReturnBar from "@/components/ReturnBar.vue";
const itemStore = useItemStore();
const orderStore = useOrderStore();
const ordersListStore = useOrdersListStore();
const itemsListStore = useItemsListStore();

const listOfQuatity = ref<Array<number>>([]);
const itemsList = ref<Array<Item>>(itemsListStore.itemsList as Array<Item>);

const addQuantity = (index: number) => {
    listOfQuatity.value[index] += 1;
};

const subQuantity = (index: number) => {
    if (listOfQuatity.value[index] >= 1) {
        listOfQuatity.value[index] -= 1;
    }
};

const createOrder = () => {
    const newOrders: Array<Order> = [];
    ordersListStore.setOrdersList(newOrders);
}

onMounted(() => {
    itemsList.value.forEach((item) => {
        listOfQuatity.value.push(0);
    });
});

</script>

<style scoped>
.container {
    padding-top: 2rem;
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
    border: 1px solid black;
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

.quantity-block

.quantity-container {
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
    box-sizing: border-box;
    position: fixed;
    width: 100%;
    left: 0;
    bottom: 4rem;
    z-index: 999;
    height: 3rem;
}

.button-group button {
    box-sizing: border-box;
    height: 100%;
    background-color: black;
    color: white;
    width: 100%;
}
</style>
