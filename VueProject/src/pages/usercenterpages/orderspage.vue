<template>
    <ReturnBar />
    <div class="container-block">
        <h2 class="title">Orders</h2>
        <ul v-if="allOrdersList.length > 0">
            <li v-for="(order, index) of allOrdersList" class="order-container">
                <div class="check-block">
                    <input
                        type="checkbox"
                        :value="index"
                        v-model="selectedOrders"
                    />
                </div>
                <RouterLink
                    :to="{ name: 'orderdetail' }"
                    class="order-link"
                    @click="storeOrder(index)"
                >
                    <div class="img-container">
                        <img src="/src_img/ring1.png" alt="/no" />
                    </div>
                    <div class="info-container">
                        <div class="item-name-block">{{ order.orderId }}</div>
                        <div class="time-block">2024-02-20</div>
                        <div class="price-quantity">
                            <div class="quantity-block">
                                {{ order.quantity }}
                            </div>
                            <div class="price-block">$ 20000</div>
                        </div>
                    </div>
                </RouterLink>
            </li>
        </ul>
        <div v-else class="empty-block">
            <strong> - No Orders - </strong>
            <RouterLink :to="{ name: 'home' }" class="link"
                >Go to shopping</RouterLink
            >
        </div>
    </div>
    <div class="button-group">
        <button @click="deleteSelectedOrders">Cancel selected orders</button>
        <button @click="toHome">My Page</button>
    </div>
</template>

<script lang="ts" setup name="CustomOrder">
import { ref, onMounted } from "vue";
import type { Order, Item, User } from "@/types/index";
import { useOrderStore, useUserStore } from "@/stores/index";
import { useRouter, RouterLink } from "vue-router";
import ReturnBar from "@/components/ReturnBar.vue";

const router = useRouter();
const userStore = useUserStore();
const orderStore = useOrderStore();
const allOrdersList = ref<Array<Order>>([]);

const selectedOrders = ref<Array<Order>>([]); // 存储选中的订单项

const toHome = () => {
    router.push({ name: "user" });
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
                const _item = d.item;
                const _user = d.user;
                const _order: Order = {
                    orderId: d.order_id,
                    item: _item,
                    user: _user,
                    quantity: d.quantity,
                    totalPrice: d.total_price,
                    createdTime: d.created_at,
                    updatedTime: d.updated_at,
                };
                allOrdersList.value.push(_order);
            }
        })
        .catch((error) => console.error(error));
};

const storeOrder = (index: number) => {
    const storedOrder = allOrdersList.value[index];
    orderStore.setOrder(storedOrder);
};

onMounted(() => {
    fetchAllOrders();
    console.log(allOrdersList.value);
});
</script>

<style scoped>
.empty-block {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 10rem;
}

.link {
    display: flex;
    align-items: center;
    justify-content: center;
    margin: 1rem 0;
    padding: 0.6rem 3rem;
    text-decoration: none;
    color: black;
    border: 2px solid black;
    font-size: 0.88rem;
    font-weight: bold;
}
.container-block > h2 {
    margin: 2rem 1rem;
    padding-bottom: 1rem;
    border-bottom: 2px solid black;
}

.container-block {
    padding-top: 2.8rem;
    height: calc(100% - 11rem);
    overflow: auto;
}

.order-container {
    box-sizing: border-box;
    padding: 0.5rem;
    display: flex;
    flex-direction: row;
    border: 1px solid #ccc;
}

.check-block {
    padding: 0.5rem;
}

.order-link {
    box-sizing: border-box;
    display: flex;
    flex: 1;
    padding: 0.4rem;
    color: black;
    font-size: 0.9rem;
    text-decoration: none;
}

.img-container {
    box-sizing: border-box;
    height: 8rem;
}

.img-container img {
    box-sizing: border-box;
    height: 100%;
    padding: 0.5rem;
    border: 1px solid #ccc;
}

.info-container {
    width: 100%;
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    padding: 0 0.5rem;
}

.price-quantity {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
}

.button-group {
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: space-evenly;
    padding-top: 1rem;
    box-shadow: 0 -2px 2px rgba(0, 0, 0, 0.1);
    height: 3rem;
}

.button-group button {
    padding: 1rem 2rem;
    background-color: white;
    color: black;
    border: 1px solid black;
}
</style>
