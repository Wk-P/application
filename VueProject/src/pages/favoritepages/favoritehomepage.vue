<template>
    <ReturnBar />
    <div class="container-block">
        <h2 class="title">Favorite</h2>
        <ul v-if="allFavoriteItemsList.length !== 0">
            <li
                v-for="(item, index) of allFavoriteItemsList"
                class="cart-container"
            >
                <div class="check-block">
                    <input
                        type="checkbox"
                        :value="index"
                        v-model="selectedFavoriteItems"
                    />
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
                    class="cart-link"
                    @click="toItemDetailPage(index)"
                >
                    <div class="img-container">
                        <img v-if="item.images && item.images.length > 0" :src="item.images[0].image" alt="/no" />
                    </div>
                    <div class="info-container">
                        <div class="item-title-block">{{ item.title }}</div>
                        <div class="item-block">{{ item.name }}</div>
                        <div class="price-block">$ {{ item.price }}</div>
                    </div>
                </RouterLink>
            </li>
        </ul>
        <div v-else class="empty-block">
            <strong> - No Items - </strong>
            <RouterLink :to="{ name: 'home' }" class="link"
                >Go to shopping</RouterLink
            >
        </div>
    </div>
    <div class="button-group">
        <button @click="deleteSelectedItems">Delete selected items</button>
        <button @click="addSeletedToCart">Add to cart</button>
        <button @click="toHome">My Page</button>
    </div>
</template>

<script lang="ts" setup name="favoritepage">
import { ref, onMounted, computed } from "vue";
import type { Item } from "@/types/index";
import { useFavoriteItemsListStore, useUserStore, useItemStore, useItemsListStore } from "@/stores/index";
import { useRouter, RouterLink } from "vue-router";
import ReturnBar from "@/components/ReturnBar.vue";

const router = useRouter();
const userStore = useUserStore();
const itemStore = useItemStore();
const favoritesStore = useFavoriteItemsListStore();
const itemsListStore = useItemsListStore();
const allFavoriteItemsList = ref<Array<Item>>([]); // 在界面中现实的 所有 favorite 商品

const isLoggedIn = computed(() => (userStore.user ? true : false));

const selectedFavoriteItems = ref<Array<Item>>([]); // 存储选中的喜欢项
const toHome = () => {
    router.push({ name: "user" });
};

const deleteSelectedItems = () => {
    if (selectedFavoriteItems.value.length === 0) {
        alert("No orders selected for deletion.");
        return;
    }

    // 使用索引从 allFavorites 过滤出选中的订单对象
    const deleteItems = selectedFavoriteItems.value.map(
        (_, index) => allFavoriteItemsList.value[index]
    );

    console.log(deleteItems);

    fetch("/api/items/favorite/delete/", {
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
    allFavoriteItemsList.value = allFavoriteItemsList.value.filter(
        (item) => !deleteItems.includes(item)
    );

    selectedFavoriteItems.value = [];
};

const addSeletedToCart = () => {
    if (selectedFavoriteItems.value.length === 0) {
        alert("No orders selected for deletion.");
        return;
    }

    // 使用索引从 allOrdersList 过滤出选中的订单对象
    const addCartItems = selectedFavoriteItems.value.map(
        (_, index) => allFavoriteItemsList.value[index]
    );

    fetch('/api/items/cart_add/', {
        method: "POST",
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            userId: userStore.user?.id,
            items: addCartItems 
        })
    })

    console.log(addCartItems);
    itemsListStore.setItemsList(addCartItems);

    // 过滤出剩余订单列表（不包含已选中的订单）
    allFavoriteItemsList.value = allFavoriteItemsList.value.filter(
        (item) => !addCartItems.includes(item)
    );

    selectedFavoriteItems.value = [];
};

const fetchAllFavoriteItems = () => {
    // 获取本用户所有 Favorite 商品
    const username = userStore.user?.username;
    fetch(`/api/items/favorite/${username}/`)
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
            allFavoriteItemsList.value = data.items;
        })
        .catch((error) => console.error(error));
};

const toItemDetailPage = (index: number) => {
    const item = allFavoriteItemsList.value[index];
    itemStore.setCustomItem(item);
};

onMounted(() => {
    console.log(isLoggedIn.value);
    if (!isLoggedIn.value) {
        router.push({ name: "user" });
    } else {
        fetchAllFavoriteItems();
        console.log(allFavoriteItemsList.value);
    }
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

.item-block,
.item-title-block {
    display: flex;
    flex-direction: row;
    justify-content: left;
}
.price-block {
    display: flex;
    flex-direction: row;
    justify-content: right;
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
