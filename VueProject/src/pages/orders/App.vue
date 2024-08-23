<template>
    这是订单
    <ul class="order-block">
        <li v-for="(o, i) in ordersList" :key="i">
            <div>{{ o.itemName }}</div>
            <div>{{ o.orderId }}</div>
            <div>{{ o.username }}</div>
            <div>{{ o.userId }}</div>
            <div>{{ o.price }}</div>
            <div>{{ o.quantity }}</div>
            <div>{{ o.totalPrice }}</div>
            <div>{{ o.createdTime }}</div>
        </li>
    </ul>
</template>

<script setup lang="ts" name="orders">
import { getCSRFToken } from '@/utils/validate';
import { ref } from 'vue';
import { userTokenStore } from '@/stores';
import type { Order } from '@/types';

// fetch user orders
const ordersList = ref<Array<Order>>([]);
const tokenStore = userTokenStore();

const username: string | null = tokenStore.username;

// backend
const url = '/backend/api/orders/search'
let params = username || '';


params += '/';

if (username !== null) {
    getOrdersList();
}

function getOrdersList() {
    getCSRFToken().then((csrftoken) => {
        fetch(`${url}/${params}`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": csrftoken,
            }
        }).then((response) => {
            if (!response.ok) {
                throw new Error("Network Invalid");
            }
            return response.json();
        }).then((data) => {
            for (let i = 0;i < data.orders.length;i++) {
                const o = data.orders[i];
                ordersList.value.push({
                    orderId: o['order-id'],
                    // username: username,
                    userId: o['userId'],
                    createdTime: o['created-time'],
                    updatedTime: o['updated-time'],
                    quantity: o['quantity'],
                    totalPrice: o['total-price'],
                    price: o['price'],
                    username: username,
                    itemName: o['item-name']
                });
            }
        }).catch(error => console.error(error.message));
    })
}

</script>
<style scoped>
.order-block {
    list-style: none;
    display: flex;
    flex-direction: column;
    width: 100%;
    box-sizing: border-box;
}

.order-block li {
    border: 3px solid #999;
    margin: 20px 0;
}
</style>
