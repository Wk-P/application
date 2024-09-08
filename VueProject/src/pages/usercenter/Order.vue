<template>
    <div class="container-block">
        <div class="order-container">
            <div class="select-title">Select</div>
            <div class="orderId-title">Order id</div>
            <div class="user-title">User name</div>
            <div class="item-title">User</div>
            <div class="quantity-title">quantity</div>
        </div>
        <ul>
            <li v-for="(value, index) of allOrdersList" class="order-container">
                <div class="check-block">
                    <input
                        type="checkbox"
                        :value="index"
                        v-model="selectedOrders"
                    />
                </div>
                <div class="orderId-block">{{ value.orderId }}</div>
                <div class="user-block">{{ username }}</div>
                <div class="item-block">{{ value.item.name }}</div>
                <div class="quantity-block">{{ value.totalQuantity }}</div>
            </li>
        </ul>
    </div>
    <div class="button-group">
        <button @click="deleteSelectedOrders">Delete Selected</button>
        <button @click="toHome">Home</button>
    </div>
</template>

<script lang="ts" setup name="CustomOrder">
import { ref, onMounted } from "vue";
import type { Order, Item, User } from "@/types/index";
import { useUserStore } from "@/stores/index";
import { useRouter } from "vue-router";

const router = useRouter();
const userStore = useUserStore();
const username = ref<string | undefined>(userStore.user?.username);
const allOrdersList = ref<Array<Order>>([]);
const selectedOrders = ref<Array<Order>>([]); // 存储选中的订单项

const toHome = () => {
    router.push({ name: "usercenter" });
};

const deleteSelectedOrders = () => {
    if (selectedOrders.value.length === 0) {
        alert("No orders selected for deletion.");
        return;
    }

    // 使用索引从 allOrdersList 过滤出选中的订单对象
    const deleteOrders = selectedOrders.value.map(
        (_, index) => allOrdersList.value[index]
    );

    console.log(deleteOrders);

    fetch("/api/orders/delete/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            deleteOrders: deleteOrders,
        }),
    })
        .then((response) => {
            if (!response.ok) {
                throw new Error(`Error! HTTP status code ${response.status}`);
            }
            return response.json();
        })
        .then((data) => {
            console.log(data);
            alert("삭제돴습니다!");
            router.push({ name: "orders" });
        })
        .catch((error) => console.error(error));

    // 过滤出剩余订单列表（不包含已选中的订单）
    allOrdersList.value = allOrdersList.value.filter(
        (order) => !deleteOrders.includes(order)
    );

    selectedOrders.value = [];
};

const fetchAllOrders = () => {
    // 获取Orders
    fetch("/api/orders/all/")
        .then((response) => {
            if (!response.ok) {
                throw new Error(`Error! HTTP status code ${response.status}`);
            }
            return response.json();
        })
        .then((data) => {
            for (const d of data) {
                console.log(d);
                const _item: Item = d.item_info;
                const _userId: string = d.user_info.id;
                const _order: Order = {
                    orderId: d.order_id,
                    item: _item,
                    userId: _userId,
                    totalQuantity: d.totalQuantity,
                };
                allOrdersList.value.push(_order);
            }
        })
        .catch((error) => console.error(error));
};

onMounted(() => {
    fetchAllOrders();
    console.log(allOrdersList.value);
});
</script>

<style scoped>
.order-container {
    padding: 0.2rem;
    display: flex;
    flex-direction: row;
    justify-content: space-around;
}

.order-container div {
    flex: 1;
    text-align: center;
}

.button-group {
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: space-evenly;
    padding-top: 1rem;
}
.button-group button {
    padding: 1rem 3rem;
    background-color: white;
    color: black;
    border: 1px solid black;
}

.orderId-block {
    overflow: hidden;
    white-space: nowrap;
    text-overflow: ellipsis;
}
</style>
