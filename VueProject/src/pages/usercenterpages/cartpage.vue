<template>
    <ReturnBar />
    <div class="container-block">
        <ul v-if="allCartItemsList.length !== 0">
            <li
                v-for="(cart_item, itemIndex) of allCartItemsList"
                class="item-container"
            >
                <div class="check-delete-block">
                    <div class="check-block">
                        <input
                            type="checkbox"
                            :value="cart_item"
                            v-model="selectedCartItems"
                        />
                    </div>
                    <!-- 删除单个item 按钮 -->
                    <button @click="deteleSingleItem(itemIndex)">delete</button>
                </div>
                <RouterLink
                    :to="{
                        name: 'itemdetail',
                        params: {
                            itemId: cart_item.item.id,
                            itemName: cart_item.item.name,
                            brand: cart_item.item.brand,
                            itemTitle: cart_item.item.title,
                        },
                    }"
                    class="item-link"
                    @click="toItemDetailPage(itemIndex)"
                >
                    <div class="img-container">
                        <img
                            v-if="
                                cart_item.item.images &&
                                cart_item.item.images.length > 0
                            "
                            :src="cart_item.item.images[0].image"
                            alt="/no"
                        />
                    </div>
                </RouterLink>
                <div class="info-container">
                    <div class="item-brand">[{{ cart_item.item.brand }}]</div>
                    <div class="item-title-block">
                        {{ cart_item.item.title }} / {{ cart_item.item.name }}
                    </div>
                    <div class="selected-options">
                        <div
                            v-for="option in cart_item.selected_options"
                            class="item-options-labels"
                        >
                            <span>[{{ option.option_key }}</span
                            ><span>{{ option.value }}]</span>
                        </div>
                    </div>
                    <div class="quantity-container">
                        <span>Quantity</span>
                        <input
                            type="text"
                            v-model="listOfQuatity[itemIndex]"
                            :placeholder="placeholderText"
                        />
                    </div>
                    <div class="price-block">$ {{ cart_item.item.price }}</div>
                </div>
                <div class="options-button">
                    <button @click="changeOptionsButton(itemIndex)">
                        Options Change
                    </button>
                    <button @click="buyButton(itemIndex)">Buy</button>
                </div>
                <teleport to="body">
                    <div class="item-option-view" v-if="showOptionsView">
                        <ul
                            v-if="
                                allCartItemsList[itemIndex]?.item !==
                                    undefined &&
                                allCartItemsList[itemIndex]?.item !==
                                    null
                            "
                        >
                            <li
                                v-for="(
                                    option, optionIndex
                                ) in allCartItemsList[itemIndex]?.item.options"
                            >
                                <h3 class="item-option-title">
                                    {{ option.name }}
                                </h3>
                                <div class="item-option-buttons">
                                    <button
                                        v-for="(
                                            value, valueIndex
                                        ) in option.values"
                                        @click="
                                            selectItemOption(
                                                itemIndex,
                                                optionIndex,
                                                valueIndex
                                            )
                                        "
                                        :style="
                                            getButtonStyle(
                                                itemIndex,
                                                optionIndex,
                                                valueIndex
                                            )
                                        "
                                        class="item-option-button"
                                    >
                                        {{ value }}
                                    </button>
                                </div>
                            </li>
                        </ul>
                        <div v-else>Empty options</div>
                        <button
                            @click="confirmChangeOptions(itemIndex)"
                            class="confirm-button"
                        >
                            CONFIRM
                        </button>
                    </div>
                </teleport>
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
        <button @click="addSeletedCartToOrder">
            <span
                ><strong
                    >Total {{ selectedCartItems.length }} Selected</strong
                ></span
            >
            <span
                ><strong>$ {{ totalPrice }}</strong></span
            >
        </button>
    </div>
</template>

<script lang="ts" setup name="CustomOrder">
import { ref, onMounted, computed } from "vue";
import type {
    Item,
    CartItem,
    SelectedOption,
    Option,
    Order,
    User,
    OptionValue,
} from "@/types/index";
import {
    useItemsListStore,
    useUserStore,
    useItemStore,
    useSelectedCartItemsStore,
    useOrdersListStore,
} from "@/stores/index";
import { useRouter, RouterLink } from "vue-router";
import ReturnBar from "@/components/ReturnBar.vue";

const router = useRouter();
const userStore = useUserStore();
const itemStore = useItemStore();
const ordersListStore = useOrdersListStore();
const cartItemsStore = useSelectedCartItemsStore();
const allCartItemsList = ref<Array<CartItem>>([]);
const placeholderText = "Quantity";
const listOfQuatity = ref<Array<number>>([]);
const showOptionsView = ref(false);

// 用于 记录 cartItem

const isLoggedIn = computed(() => (userStore.user ? true : false));

const selectedCartItems = ref<Array<CartItem>>([]); // 存储选中的订单项

const selectedItemOption = ref<Record<string, OptionValue | null>>({});

const createOrder = (cart_item: CartItem, quantity: number) => {
    // 强制转换 quantity
    const newOrder: Order = {
        orderId: "",
        user: userStore.user as User,
        item: cart_item.item,
        quantity: Number(quantity),
        totalPrice: Number(quantity) * cart_item.item.price,
        createdTime: "",
        updatedTime: "",
        status: undefined,
        tracking_number: undefined,
        selected_options: cart_item.selected_options,
    };
    return newOrder;
};

const postRequestOrders = (newOrders: Array<Order>) => {
    console.log(newOrders);
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
    try {
        for (let index = 0; index < selectedCartItems.value.length; index++) {
            const cart_item = selectedCartItems.value[index];
            console.log(listOfQuatity.value[index]);
            console.log(index);
            console.log(cart_item.selected_options);
            if (
                listOfQuatity.value[index] <= 0 ||
                listOfQuatity.value[index] === undefined
            ) {
                alert(`Please enter quantity more than 0!`);
                throw new Error("Invalid quantity");
            }
            if (
                cart_item.selected_options.length <= 0 ||
                cart_item.selected_options === undefined ||
                cart_item.selected_options === ([] as Array<SelectedOption>)
            ) {
                alert(`Please select options`);
                throw new Error("No options selected");
            }
            const newOrder = createOrder(cart_item, listOfQuatity.value[index]);
            console.log(typeof ordersListStore.ordersList);
            ordersListStore?.ordersList?.push(newOrder);
            console.log(typeof ordersListStore.ordersList);
        }
        console.log(
            `ordersListStore?.ordersList: ${ordersListStore.ordersList}`
        );
        console.assert(ordersListStore?.ordersList !== null);
        postRequestOrders(ordersListStore?.ordersList as Array<Order>);
        return true;
    } catch (error: any) {
        console.error(error);
        return false;
    }
};

const confirmChangeOptions = (itemIndex: number) => {
    showOptionsView.value = false;

    // patch 方式
    fetch(`/api/items/cart_add/`, {
        method: "PATCH",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            userId: userStore.user?.id,
            itemId: allCartItemsList.value[itemIndex].item.id,
            options: selectedItemOption.value,
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
            if (data.error) {
                alert(data.error);
                return;
            } else {
                alert("Change options success");
            }
            window.location.reload();
        });
};

const getButtonStyle = (
    itemIndex: number,
    optionIndex: number,
    valueIndex: number
) => {
    const optionKey =
        allCartItemsList.value[itemIndex].item.options[optionIndex].name;
    const selectedValue =
        allCartItemsList.value[itemIndex].item.options[optionIndex].values[
            valueIndex
        ];

    if (selectedItemOption.value[optionKey] === selectedValue) {
        // 检查 optionIndex 和 valueIndex 的匹配
        return {
            backgroundColor: "black",
            color: "white",
        };
    } else {
        return {
            backgroundColor: "#eee",
            color: "black",
        };
    }
};

// 累加所有选中的商品金额
const totalPrice = computed(() =>
    selectedCartItems.value.reduce((total, cart_item) => {
        console.log(`total: ${typeof total}`);
        console.log(`item.price: ${typeof cart_item.item.price}`);
        console.log(`item.price value: ${cart_item.item.price}`);
        console.log(`selectedCartItems: ${selectedCartItems.value}`);
        return total + Number(cart_item.item.price) || 0;
    }, 0)
);

// 删除单个商品
const deteleSingleItem = (index: number) => {
    console.log("deleteSingleItem");

    const deleteItem = allCartItemsList.value[index];

    fetch("/api/items/cart/delete/", {
        method: "DELETE",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            deleteItem: deleteItem,
            user: userStore.user,
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
            // router.push({ name: "cart" });
            window.location.reload();
        })
        .catch((error) => console.error(error));

    allCartItemsList.value.filter((item) => item !== deleteItem);
};

const selectItemOption = (
    itemIndex: number,
    optionIndex: number,
    valueIndex: number
) => {
    const optionKey =
        allCartItemsList.value[itemIndex].item.options[optionIndex].name;
    selectedItemOption.value[optionKey] =
        allCartItemsList.value[itemIndex].item.options[optionIndex].values[
            valueIndex
        ];
};

const changeOptionsButton = (itemIndex: number) => {
    // 改变当前item options 选项
    showOptionsView.value = true;
    const changeOptionItem = allCartItemsList.value[itemIndex];
    console.log(changeOptionItem);
};

const buyButton = (index: number) => {
    // 直接购买 跳转至订单界面
};

// 购买以上用品
const addSeletedCartToOrder = () => {
    if (selectedCartItems.value.length === 0) {
        alert("No orders selected for deletion.");
        return;
    }

    // 使用索引从 allOrdersList 过滤出选中的订单对象
    const addOrderItems = selectedCartItems.value.map(
        (_, index) => allCartItemsList.value[index]
    );

    cartItemsStore.setSeletedCartItems(addOrderItems);

    if (createOrders() === false) {
        return;
    }

    // 过滤出剩余订单列表（不包含已选中的订单）
    allCartItemsList.value = allCartItemsList.value.filter(
        (item) => !addOrderItems.includes(item)
    );

    selectedCartItems.value = [];

    router.push({ name: "createorder" });
};

const fetchAllCartItems = () => {
    // 所有CartItems
    const username = userStore.user?.username;
    fetch(`/api/items/cart/${username}/`)
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
            allCartItemsList.value = data.map(
                (element: {
                    item: CartItem;
                    options: Array<Option>;
                    selected_options: Array<SelectedOption>;
                }) => {
                    const cart_item: CartItem = {
                        item: element.item.item,
                        user: element.item.user,
                        selected_options: element.selected_options
                    }

                    cart_item.item.options = element.options;
                    return cart_item;
                });
            console.log(allCartItemsList.value);
        })
        .catch((error) => console.error(error));
};

const toItemDetailPage = (index: number) => {
    const item = allCartItemsList.value[index];
    itemStore.setCustomItem(item.item);
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

.info-container > div {
    margin-top: 0.2rem;
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

.selected-options {
    box-sizing: border-box;
    display: flex;
    height: 3rem;
    flex-direction: column;
    justify-content: center;
    overflow-x: hidden;
    overflow-y: auto;
}

.item-options-labels {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
}

.item-option-view {
    position: absolute;
    top: calc((100vh - 40vh) * 0.4);
    left: calc((100vw - 60vw) * 0.5);
    height: 40vh;
    width: 60vw;
    z-index: 1000;
    background-color: white;
    display: flex;
    flex-direction: column;
    align-items: center;
}

.item-option-view ul {
    box-sizing: border-box;
    height: 100%;
    width: 100%;
    overflow-y: auto;
    overflow-x: hidden;
}

.item-option-view ul li {
    height: 4rem;
    width: 100%;
}

.item-option-view > div {
    width: 100%;
    height: 4rem;
}

.confirm-button {
    display: block;
    box-sizing: border-box;
    width: 80%;
    padding: 0.5rem 1rem;
    height: 2rem;
    background-color: white;
}

.item-option-buttons {
    box-sizing: border-box;
    display: flex;
    flex-direction: row;
    justify-content: space-evenly;
    margin: 0.4rem;
}

.item-option-button {
    box-sizing: border-box;
    padding: 0.2rem 0.5rem;
    border: 1px solid #eee;
    width: 100%;
}

.item-option-title {
    padding: 0.4rem 0.5rem;
}

.quantity-container {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
}

.quantity-container input {
    box-sizing: border-box;
    outline: none;
    text-align: center;
}
</style>
