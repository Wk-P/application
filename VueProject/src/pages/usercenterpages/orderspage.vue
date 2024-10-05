<template>
    <ReturnBar />
    <div class="container-block">
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
                        <img v-if="order.item?.images && order.item?.images.length > 0" :src="order.item?.images[0].image" alt="/no" />
                    </div>
                    <div class="info-container">
                        <div class="item-name-block">{{ order.orderId }}</div>
                        <div class="time-block">{{ order.createdTime }}</div>
                        <div class="price-quantity">
                            <div class="quantity-block">
                                x{{ order.quantity }}
                            </div>
                            <div class="price-block">
                                $ {{ order.totalPrice }}
                            </div>
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
            alert("삭제돴습니다!");
            router.push({ name: "order" });
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
            allOrdersList.value = [];
            data.forEach((element: any) => {
                const o: Order = {
                    orderId: element.order_id,
                    user: element.user,
                    item: element.item,
                    quantity: element.quantity,
                    totalPrice: element.total_price,
                    createdTime: element.created_at,
                    updatedTime: element.updated_at,
                    status: element.status,
                    tracking_number: element.tracking_number,
                };
                allOrdersList.value.push(o);
            });
        })
        .catch((error) => console.error(error));
};

const storeOrder = (index: number) => {
    const storedOrder = allOrdersList.value[index];
    orderStore.setOrder(storedOrder);
};

onMounted(() => {
    fetchAllOrders();
});
</script>

<style scoped>
.empty-block {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100%;
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
    max-width: 100vw;
}

.order-container {
    box-sizing: border-box;
    display: flex;
    flex-direction: row;
    border: 1px solid #ccc;
    flex-shrink: 1; /* 确保子元素不会超出父容器 */
    min-width: 0; /* 防止子元素过度撑开 */
    max-width: 100%; /* 限制最大宽度为父元素宽度 */
}
.check-block {
    padding: 0.5rem;
}

.order-link {
    display: flex;
    flex-direction: row;
    align-items: center;
    padding: 0.4rem;
    color: black;
    font-size: 0.9rem;
    text-decoration: none;
    flex: 1; /* 让 order-link 占满剩余空间 */
    min-width: 0; /* 防止 order-link 过度撑开 */
    max-width: 100%; /* 确保 order-link 不会超出父元素 */
    white-space: normal; /* 允许内容换行 */
    word-wrap: break-word; /* 换行以适应内容 */
    overflow-wrap: break-word; /* 强制换行以避免溢出 */
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
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    height: 100%;
    padding: 0 0.5rem;
    min-width: 0; /* 防止信息块过度撑开 */
    max-width: 100%; /* 防止信息块超出父元素 */
    white-space: normal; /* 允许内容换行 */
    word-wrap: break-word; /* 长单词换行 */
    overflow-wrap: break-word; /* 适应长单词 */
}

.price-quantity {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
}

.item-name-block {
    word-wrap: break-word; /* 或者使用 word-break: break-all; */
    overflow-wrap: break-word; /* 让长单词换行 */
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
    color: black;
    margin: 0 0.5rem;
    border: 1px solid black;
    flex: 1;
}
</style>
