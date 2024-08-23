<template>
    <HeadNav />
    <div class="head-on">
        <RouterLink to="/">
            <img src="/arrow-left.png" alt="turn back" />
            <div>返回</div>
        </RouterLink>
    </div>
    <div class="outer">
        <div class="product-detail-block">
            <h2 class="title">{{ item?.name }}</h2>
            <div class="product-img">
                <img src="/lv.png" alt="item-img" />
            </div>
            <div class="button-group">
                <div class="add-order-button">
                    <ul>
                        <li class="number-button">
                            <button @click="subSum">-</button>
                        </li>
                        <li class="number-block">
                            <input type="text" v-model="orderSum" />
                        </li>
                        <li class="number-button">
                            <button @click="addSum">+</button>
                        </li>
                    </ul>
                    <button @click="createOrder">Order</button>
                </div>
                <div class="add-favorite-button">
                    <button @click="addFavorite">Favorite</button>
                </div>
                <div class="add-cart-button">
                    <button @click="addToCart">Add to cart</button>
                </div>
                <div class="add-comments-button">
                    <button @click="addComment">Comments</button>
                </div>
            </div>

            <div class="details">
                <ul class="details-list">
                    <li>
                        <RouterLink :to="{ name: 'details' }" class="item-link">详情</RouterLink>
                    </li>
                    <li>
                        <RouterLink :to="{ name: 'comments' }" class="item-link">评论</RouterLink>
                    </li>
                </ul>
            </div>
            <RouterView></RouterView>
        </div>
    </div>
</template>

<script lang="ts" setup name="product">
import HeadNav from "@/components/HeadNav.vue";
import router from "@/router";
import { useItemStore, userTokenStore } from "@/stores";
import { getCSRFToken } from "@/utils/validate";
import { ref, watch, computed } from "vue";
import { RouterLink, RouterView, useRoute } from "vue-router";
const store = useItemStore();

// 动态计算 item 属性
const item = computed(() => store.item);
const currentComponent = ref("details");

// 获取路由信息
const route = useRoute();

const tokenStore = userTokenStore();

const orderSum = ref<number>(1);

function addSum() {
    orderSum.value = Number(orderSum.value) + 1;
}

function subSum() {
    if (orderSum.value <= 1) {
        return;
    }
    orderSum.value = Number(orderSum.value) - 1;
}

async function addToCart() {
    let username = tokenStore.username;
    
    const csrftoken = await getCSRFToken();
    const url = "/backend/api/user/";
    let params = "";

    if (username !== null) {
        params == username;
        params += "/";
    }

    fetch(`${url}/${params}`)
    .then((response) => {
        if (!response.ok) {
            throw new Error(`Network Invalid`);
        }
    }).then((data) => {
        alert("Add to cart");
    }).catch((error) => {
        console.error(error.message);
    })
}


function createOrder() {
    const itemId = item.value?.id;
    if (itemId === null) {
        alert("Item id wrong!");
        return;
    }

    if (orderSum.value < 1) {
        orderSum.value = 1;
        alert("Wrong sum of order");
        return;
    }

    // login check
    if (tokenStore.username === null) {
        alert("Please login!");
        router.push("/login");
        return;
    }

    const message = `Order:\n Item name: ${item.value?.name}\nUser: ${tokenStore.username}\nSum of items: ${orderSum.value}\nConfirm your order and continue?`

    if (!confirm(message)) {
        return;
    }


    const url = "/backend/api/orders/create";
    let params = "";

    getCSRFToken().then((csrftoken) => {
        fetch(`${url}/${params}`,
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    'X-CSRFToken': csrftoken || "",
                },
                body: JSON.stringify({
                    itemId: itemId,
                    username: tokenStore.username,
                    orderSum: orderSum.value,
                }),
            }
        )
            .then((response) => {
                if (!response.ok) {
                    throw new Error("Network invalid Invalid");
                }
                return response.json();
            })
            .then((data) => {
                alert(`Order has been submitted\nOrder id: ${data.order_id}\n`);
            })
            .catch((error) => {
                console.error(error.message);
            });
    }).catch(error => console.error(error.message));
}

function addFavorite() { }

function addComment() { }

// 监听路由变化
watch(
    () => route.name,
    (to) => {
        if (to) {
            currentComponent.value = to.toString(); // Ensure to convert to string
        }
    }
);
</script>

<style scoped>
.outer {
    height: auto;
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    padding-top: 40px;
    padding-bottom: 40px;
}

.product-detail-block {
    width: 50%;
    border-radius: 4px;
    box-shadow: 0 0 10px 2px #eee;
    border: 3px solid rgb(255, 200, 0);
    display: flex;
    flex-direction: column;
    align-items: center;
}

.details {
    width: 100%;
}

.details-list {
    list-style: none;
    display: flex;
    flex-direction: row;
    justify-content: space-evenly;
    align-items: center;
    width: 100%;
    height: 50px;
}

.details-list li {
    border-top: 2px solid rgb(255, 200, 0);
    text-align: center;
    background-color: rgba(255, 200, 0, 0.5);
    height: 100%;
    width: 100%;
}

.details-list li:hover {
    background-color: rgba(255, 200, 0, 1);
    cursor: pointer;
}

.item-link {
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    text-decoration: none;
    color: black;
    box-sizing: border-box;
}

.title {
    padding: 20px 0;
}

.product-img {
    display: flex;
    flex-direction: row;
    justify-content: center;
    padding: 10px 20px 40px 20px;
    width: 100%;
    height: 500px;
    box-sizing: border-box;
}

.product-img img {
    border: 4px solid rgba(255, 200, 0, 1);
    box-sizing: border-box;
    background-color: #eee;
    height: 100%;
}

.inner-details {
    box-sizing: border-box;
    width: 100%;
    border: 3px solid black;
    height: 200px;
}

.head-on {
    height: 50px;
    display: flex;
    flex-direction: row;
    align-items: center;
    background-color: rgb(244, 244, 244);
}

.head-on a {
    height: 100%;
    width: auto;
    display: flex;
    flex-direction: row;
    text-decoration: none;
    box-sizing: border-box;
    border: 2px solid rgb(244, 244, 244);
}

.head-on a div {
    height: 100%;
    width: auto;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    color: black;
    padding-right: 20px;
    padding-left: 5px;
}

.head-on img {
    box-sizing: border-box;
    height: 100%;
    width: auto;
}

.head-on a:hover {
    cursor: pointer;
    border: 2px solid #ccc;
}

.button-group {
    width: 100%;
    margin-bottom: 20px;
}

.add-order-button {
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    height: 50px;
    padding: 20px;
}

.add-order-button ul {
    display: flex;
    flex-direction: row;
    justify-content: center;
    list-style: none;
    height: 100%;
    width: 60%;
    box-sizing: border-box;
}

.add-order-button ul li {
    width: 100%;
    box-sizing: border-box;
    height: 100%;
    display: flex;
    flex-direction: row;
    justify-content: center;
}

.add-order-button ul li:first-child {
    display: flex;
    flex-direction: row;
    justify-content: end;
    margin-right: 5px;
}

.add-order-button ul li:last-child {
    display: flex;
    flex-direction: row;
    justify-content: start;
    margin-left: 5px;
}

.add-order-button .number-button {
    box-sizing: border-box;
    height: 100%;
    width: 25%;
}

.add-order-button ul .number-button button {
    box-sizing: border-box;
    height: 100%;
    width: 100%;
    font-size: 1rem;
    border-radius: 4px;
    border: 2px solid #eee;
    box-shadow: 0 0 10px 2px #444;
    background-color: #ddd;
    transition: all 0.2s ease-in-out;
    font-size: 1.2rem;
}

.add-order-button ul .number-block input {
    box-sizing: border-box;
    width: 100%;
    height: 100%;
    outline: none;
    box-shadow: 0 0 10px 2px #444;
    border: 2px solid #eee;
    border-radius: 4px;
    text-align: center;
    font-size: 1.2rem;
}

.add-order-button .number-button button:hover {
    cursor: pointer;
    background-color: #444;
    color: white;
}

.add-order-button>button:last-child {
    box-sizing: border-box;
    height: 100%;
    width: 28%;
    font-size: 1rem;
    border-radius: 4px;
    border: 2px solid #eee;
    box-shadow: 0 0 10px 2px #444;
    background-color: #ddd;
    transition: all 0.2s ease-in-out;
    padding: 0 20px;
}

.add-order-button button:hover {
    cursor: pointer;
    background-color: #fff;
}

.add-favorite-button,
.add-comments-button,
.add-cart-button {
    width: 100%;
    height: 50px;
    padding: 20px 0;
    display: flex;
    flex-direction: row;
    justify-content: center;
}

.add-favorite-button button,
.add-comments-button button,
.add-cart-button button {
    width: 40%;
    font-size: 1rem;
    border-radius: 4px;
    border: 2px solid #eee;
    box-shadow: 0 0 10px 2px #444;
    background-color: #ddd;
    transition: all 0.2s ease-in-out;
}

.add-favorite-button button:hover,
.add-comments-button button:hover,
.add-cart-button button:hover {
    cursor: pointer;
    background-color: #fff;
}
</style>
