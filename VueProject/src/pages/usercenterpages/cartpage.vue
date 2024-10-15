<template>
    <ReturnBar />
    <div class="container-block">
        <ul v-if="allCartItemsList.length !== 0">
            <li
                v-for="(item, index) of allCartItemsList"
                class="item-container">
                <div class="check-delete-block">
                    <div class="check-block">
                        <input
                            type="checkbox"
                            :value="item"
                            v-model="selectedCartItems" />
                    </div>
                    <!-- 删除单个item 按钮 -->
                    <button @click="deteleSingleItem(index)">delete</button>
                </div>
                <RouterLink
                    :to="{
                        name: 'itemdetail',
                        params: {
                            itemId: item.id,
                            itemName: item.name,
                            brand: item.brand,
                            itemTitle: item.title,
                        },
                    }"
                    class="item-link"
                    @click="toItemDetailPage(index)">
                    <div class="img-container">
                        <img
                            v-if="item.images && item.images.length > 0"
                            :src="item.images[0].image"
                            alt="/no" />
                    </div>
                    <div class="info-container">
                        <div class="item-brand">[{{ item.brand }}]</div>
                        <div class="item-title-block">{{ item.title }} / Name</div>
                        <div class="options">[ options ]</div>  
                        <div class="price-block">$ {{ item.price }}</div>
                    </div>
                </RouterLink>
                <div class="options-button">
                    <button @click="changeOptionsButton">Options Change</button>
                    <button @click="buyButton">Buy</button>
                </div>
            </li>
        </ul>
        <div
            v-else
            class="empty-block">
            <strong> - No Items - </strong>
            <RouterLink
                :to="{ name: 'home' }"
                class="link"
                >Go to shopping</RouterLink
            >
        </div>
    </div>
    <div class="button-group">
        <button @click="addSeletedCartToOrder">
            <span
                ><strong>Total {{ selectedCartItems.length }} Selected</strong></span
            >
            <span
                ><strong>$ {{ totalPrice }}</strong></span
            >
        </button>
    </div>
</template>

<script lang="ts" setup name="CustomOrder">
import { ref, onMounted, computed } from "vue";
import type { Item } from "@/types/index";
import { useItemsListStore, useUserStore, useItemStore } from "@/stores/index";
import { useRouter, RouterLink } from "vue-router";
import ReturnBar from "@/components/ReturnBar.vue";

const router = useRouter();
const userStore = useUserStore();
const itemStore = useItemStore();
const itemsListStore = useItemsListStore();
const allCartItemsList = ref<Array<Item>>([]);

const isLoggedIn = computed(() => (userStore.user ? true : false));

const selectedCartItems = ref<Array<Item>>([]); // 存储选中的订单项

// 累加所有选中的商品金额
const totalPrice = computed(() =>
    selectedCartItems.value.reduce((total, item) => {
        console.log(`total: ${typeof total}`);
        console.log(`item.price: ${typeof item.price}`);
        console.log(`item.price value: ${item.price}`);
        console.log(`selectedCartItems: ${selectedCartItems.value}`);
        return total + Number(item.price) || 0;
    }, 0)
);

const deteleSingleItem = (index: number) => {
    console.log("deleteSingleItem");
};

const changeOptionsButton = () => {
    // 改变当前item options 选项
};

const buyButton = () => {
    // 直接购买 跳转至订单界面
    
};

const deleteSelectedItems = () => {
    if (selectedCartItems.value.length === 0) {
        alert("No orders selected for deletion.");
        return;
    }

    // 使用索引从 allOrdersList 过滤出选中的订单对象
    const deleteItems = selectedCartItems.value.map((_, index) => allCartItemsList.value[index]);

    console.log(deleteItems);

    fetch("/api/items/cart/delete/", {
        method: "DELETE",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            deleteItems: deleteItems,
            user: userStore.user,
        }),
    })
        .then((response) => {
            if (!response.ok) {
                response.json().then((error) => {
                    console.log(error);
                    throw new Error(`Error! HTTP status code ${response.status}`);
                });
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
    allCartItemsList.value = allCartItemsList.value.filter((item) => !deleteItems.includes(item));

    selectedCartItems.value = [];
};

const addSeletedCartToOrder = () => {
    if (selectedCartItems.value.length === 0) {
        alert("No orders selected for deletion.");
        return;
    }

    // 使用索引从 allOrdersList 过滤出选中的订单对象
    const addOrderItems = selectedCartItems.value.map((_, index) => allCartItemsList.value[index]);

    console.log(addOrderItems);
    itemsListStore.setItemsList(addOrderItems);

    // 过滤出剩余订单列表（不包含已选中的订单）
    allCartItemsList.value = allCartItemsList.value.filter((item) => !addOrderItems.includes(item));

    selectedCartItems.value = [];

    router.push({ name: "createorder" });
};

const fetchAllCartItems = () => {
    // 获取Orders
    const username = userStore.user?.username;
    fetch(`/api/items/cart/${username}/`)
        .then((response) => {
            if (!response.ok) {
                response.json().then((error) => {
                    console.log(error);
                    throw new Error(`Error! HTTP status code ${response.status}`);
                });
            }
            return response.json();
        })
        .then((data) => {
            allCartItemsList.value = data.map((cartItem: { item: Item }) => cartItem.item);
            console.log(allCartItemsList.value);
        })
        .catch((error) => console.error(error));
};

const toItemDetailPage = (index: number) => {
    const item = allCartItemsList.value[index];
    itemStore.setCustomItem(item);
};

onMounted(() => {
    console.log(isLoggedIn.value);
    if (!isLoggedIn.value) {
        router.push({ name: "user" });
    } else {
        fetchAllCartItems();
        console.log(allCartItemsList.value);
    }
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
}

.item-container {
    box-sizing: border-box;
    padding: 0.5rem;
    display: flex;
    flex-direction: column;
    border-bottom: 1px solid #ccc;
}

.check-delete-block {
    padding: 0.5rem;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
}

.check-delete-block button {
    color: white;
    background-color: black;
    border: none;
    padding: 0.3rem 0.5rem;
}

.check-delete-block .check-block input {
    box-sizing: border-box;
}

.item-link {
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
    padding: 0.1rem;
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

.item-block,
.item-title-block {
    display: flex;
    flex-direction: row;
    justify-content: left;
}
.price-block {
    display: flex;
    flex-direction: row;
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
    background-color: black;
    color: white;
    font-size: 1rem;
    margin: 0 0.5rem;
    border: 1px solid black;
    flex: 1;
}

.button-group button span:nth-child(1) {
    padding-right: 0.5rem;
    border-right: 2px solid white;
}

.button-group button span:nth-child(2) {
    padding-left: 0.5rem;
}

.options-button {
    width: 100%;
    height: 3.5rem;
    display: flex;
    flex-direction: row;
    justify-content: space-evenly;
}

.options-button button {
    box-sizing: border-box;
    width: 50%;
    border: 1px solid #ccc;
    outline: none;
    margin: 0.4rem;
    padding: 0.5rem 1rem;
    background-color: white;
    color: black;
}
</style>
