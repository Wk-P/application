<template>
    <ReturnBar />
    <div class="container-block">
        <h2 class="title">Cart</h2>
        <ul>
            <li
                v-for="(item, index) of allCartItemsList"
                class="cart-container"
            >
                <div class="check-block">
                    <input
                        type="checkbox"
                        :value="index"
                        v-model="selectedCartItems"
                    />
                </div>
                <RouterLink :to="{ name: 'itemdetail' }" class="cart-link" @click="toItemDetailPage(index)">
                    <div class="img-container">
                        <img src="/src_img/ring1.png" alt="/no" />
                    </div>
                    <div class="info-container">
                        <div class="item-name-block">{{ item.id }}</div>
                        <div class="time-block">2024-02-20</div>
                        <div class="price-quantity">
                            <div class="item-block">{{ item.name }}</div>
                            <div class="price-block">$ 20000</div>
                        </div>
                    </div>
                </RouterLink>
            </li>
        </ul>
    </div>
    <div class="button-group">
        <button @click="deleteSelectedOrders">Delete selected items</button>
        <button @click="addSeletedCartToOrder">Create order</button>
        <button @click="toHome">My Page</button>
    </div>
</template>

<script lang="ts" setup name="CustomOrder">
import { ref, onMounted } from "vue";
import type { Order, Item, User } from "@/types/index";
import { useItemsListStore, useUserStore, useItemStore } from "@/stores/index";
import { useRouter, RouterLink } from "vue-router";
import ReturnBar from "@/components/ReturnBar.vue";

const router = useRouter();
const userStore = useUserStore();
const itemStore = useItemStore();
const itemsListStore = useItemsListStore();
const allCartItemsList = ref<Array<Item>>([]);

const selectedCartItems = ref<Array<Item>>([]); // 存储选中的订单项
const toHome = () => {
    router.push({ name: "user" });
};

const deleteSelectedOrders = () => {
    if (selectedCartItems.value.length === 0) {
        alert("No orders selected for deletion.");
        return;
    }

    // 使用索引从 allOrdersList 过滤出选中的订单对象
    const deleteItems = selectedCartItems.value.map(
        (_, index) => allCartItemsList.value[index]
    );

    console.log(deleteItems);

    fetch("/api/items/delete/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            deleteItems: deleteItems,
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
            router.push({ name: "cart" });
        })
        .catch((error) => console.error(error));

    // 过滤出剩余订单列表（不包含已选中的订单）
    allCartItemsList.value = allCartItemsList.value.filter(
        (item) => !deleteItems.includes(item)
    );

    selectedCartItems.value = [];
};

const addSeletedCartToOrder = () => {
    if (selectedCartItems.value.length === 0) {
        alert("No orders selected for deletion.");
        return;
    }

    // 使用索引从 allOrdersList 过滤出选中的订单对象
    const addOrderItems = selectedCartItems.value.map(
        (_, index) => allCartItemsList.value[index]
    );

    console.log(addOrderItems);
    itemsListStore.setItemsList(addOrderItems);

    // fetch("/api/order/create/", {
    //     method: "POST",
    //     headers: {
    //         "Content-Type": "application/json",
    //     },
    //     body: JSON.stringify({
    //         addOrderItems: addOrderItems,
    //     }),
    // })
    //     .then((response) => {
    //         if (!response.ok) {
    //             throw new Error(`Error! HTTP status code ${response.status}`);
    //         }
    //         return response.json();
    //     })
    //     .then((data) => {
    //         console.log(data);
    //         alert("주문생선됐습니다!");
    //         router.push({ name: "order" });
    //     })
    //     .catch((error) => console.error(error));

    // 过滤出剩余订单列表（不包含已选中的订单）
    allCartItemsList.value = allCartItemsList.value.filter(
        (item) => !addOrderItems.includes(item)
    );

    selectedCartItems.value = [];

    router.push({ name: "createorder" });
};

const fetchAllOrders = () => {
    // 获取Orders
    const username = userStore.user?.username;
    fetch(`/api/items/cart/${username}/`)
        .then((response) => {
            if (!response.ok) {
                throw new Error(`Error! HTTP status code ${response.status}`);
            }
            return response.json();
        })
        .then((data) => {
            for (const d of data) {
                const _item: Item = d;
                allCartItemsList.value.push(_item);
            }
        })
        .catch((error) => console.error(error));
};

const toItemDetailPage = (index: number) => {
    const item = allCartItemsList.value[index];
    itemStore.setCustomItem(item);
}

onMounted(() => {
    fetchAllOrders();
    console.log(allCartItemsList.value);
});
</script>

<style scoped>
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

.cart-container {
    box-sizing: border-box;
    padding: 0.5rem;
    display: flex;
    flex-direction: row;
    border: 1px solid #ccc;
}

.check-block {
    padding: 0.5rem;
}

.cart-link {
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
    border: 1px solid black;
}
</style>
