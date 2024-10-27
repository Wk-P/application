<template>
    <ReturnBar />
    <div class="container">
        <!-- 信息管理 -->
        <div class="address-block">
            <span><strong>배송지</strong></span>
            <RouterLink :to="{ name: 'address_receiver' }" class="link"
                >배송지 관리</RouterLink
            >
        </div>
        <!-- 订单地址 -->
        <div class="address-block-1">
            <ul
                class="address-first-content"
                v-if="addressInformationList.length > 0"
            >
                <!-- <div>{{ addressInformationList[0]?.address }}</div> -->
                <li
                    v-for="(address, index) in addressInformationList"
                    @click="selectAddress(index)"
                    :style="isSelectedAddress(index) ? selectedAddressStyle : unSelectedAddressStyle"
                >
                    {{ address.receiver }}
                </li>
            </ul>
            <div v-else>Please add new address and receiver</div>
        </div>
        <!-- 付款信息 -->
        <div class="send-money-info">
            <h4>结算方式</h4>
            <div>$ {{ orderStore?.order?.totalPrice }} 请转账至下列账户</div>
            <div>NH 1234-5678-9999</div>
        </div>
        <!-- 订单商品展示区 -->
        <ul class="order-items-list">
            <li v-for="(cart_item, item_index) in fromCartItems">
                <div class="img-block">
                    <img
                        v-if="
                            cart_item?.item.images &&
                            cart_item?.item.images.length > 0
                        "
                        :src="cart_item?.item.images[0].image"
                        alt=""
                    />
                </div>
                <div class="quantity-block">
                    <span>Quantity</span>
                    <span> </span>
                </div>
                <div class="info-block">
                    <div class="block-1">
                        <span>{{ cart_item?.item.name }}</span>
                        <span>$ {{ cart_item?.item.price }}</span>
                    </div>
                    <div
                        class="options-block"
                        v-for="option in cart_item?.selected_options"
                    >
                        <span>{{ option.option_key }}</span>
                        <span>{{ option.value }}</span>
                    </div>
                </div>
            </li>
        </ul>
        <div class="button-group">
            <button @click="toOrderDetail">Send money confirm</button>
            <button @click="kakaoInfo">Contact us</button>
        </div>
    </div>
    <!-- kakao信息 -->
    <teleport to="body">
        <div v-if="showModal" class="modal">
            <div class="head">
                <span><strong>Pay</strong></span
                ><button @click="showModal = false">X</button>
            </div>
            <p>Kakao Information</p>
            <button @click="closeModal()" class="close-button">
                Close Modal
            </button>
        </div>
    </teleport>
</template>

<script lang="ts" setup name="createorderpage">
import type { Order, Item, User, AddressReceiver } from "@/types/index";
import { useRouter, useRoute } from "vue-router";
import {
    useItemStore,
    useOrderStore,
    useItemsListStore,
    useOrdersListStore,
    useUserStore,
    useSelectedCartItemsStore,
} from "@/stores/index";
import { ref, onMounted } from "vue";
import ReturnBar from "@/components/ReturnBar.vue";
const itemStore = useItemStore();
const orderStore = useOrderStore();
const router = useRouter();
const userStore = useUserStore();
const ordersListStore = useOrdersListStore();
const fromCartItemsStore = useSelectedCartItemsStore();

// const itemsList = ref<Array<Item>>(itemsListStore.itemsList as Array<Item>);

// 地址信息
const addressInformationList = ref<Array<AddressReceiver>>([]);

// 当前选中的地址
const selectedAddressInfo = ref<AddressReceiver>();

// 检查是否为当前选中地址
const isSelectedAddress = (index: number) => {
    return addressInformationList.value[index] === selectedAddressInfo.value;
}

// 未选择的地址css
const unSelectedAddressStyle = {
    backgroundColor: 'white',
    color: 'black',
}

// 选择的地址css
const selectedAddressStyle = {
    backgroundColor: 'black',
    color: 'white'
}

const selectAddress = (index: number) => {
    selectedAddressInfo.value = addressInformationList.value[index];
};

// 从 cartItems 获取 items
const fromCartItems = fromCartItemsStore.selectedItems;

// kakao 信息展示控制
const showModal = ref(false);


// 关闭浮窗
const closeModal = () => {
    showModal.value =  false;
}


// 跳转用户 Order details 界面展示订单详情
const toOrderDetail = () => {
    if (confirm(`Did you pay for this order?`) === true) {
        router.push({ name: "orderdetail"});
    } 
    return;
}

const fetchAddressInformation = async () => {
    fetch(`/api/user/address/${userStore?.user?.id}`)
        .then((response) => {
            if (!response.ok) {
                response.json().then((error) => {
                    console.log(error);
                    throw new Error(
                        `Error! HTTP status code ${response.status}`
                    );
                });
            } else {
                return response.json();
            }
        })
        .then((data) => {
            console.log(data);
            addressInformationList.value = data;
            // 设置默认地址
            selectedAddressInfo.value = addressInformationList.value[0];
        });

    
};

const kakaoInfo = () => {
    showModal.value = true;
};

onMounted(() => {
    fetchAddressInformation();
});
</script>

<style scoped>
ul {
    list-style: none;
}

.address-block {
    box-sizing: border-box;
    padding: 0 1rem;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
}

.address-block .link {
    display: block;
    color: #aaa;
    text-decoration: none;
    border: 1px solid #aaa;
    padding: 0 0.5rem;
    font-size: 0.8rem;
}

.modal {
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    background-color: white;
    padding: 20px;
    border: 1px solid #ccc;
    z-index: 1000;
    width: 50%;
}

.modal .head {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
}

.modal .head button {
    width: 2rem;
    height: 2rem;
    border: 1px solid border;
    background-color: white;
    border-radius: 0.3rem;
}

.modal .close-button {
    width: 100%;
    height: 3rem;
    margin-top: 2rem;
    border: 1px solid border;
    background-color: white;
    border-radius: 0.3rem;
}

.container {
    padding-top: 3rem;
    overflow-y: auto;
    overflow-x: hidden;
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

.quantity-block .quantity-container {
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
    background-color: black;
    border: none;
    color: white;
    width: 1.5rem;
    font-size: 1.1rem;
}

.quantity-container input {
    box-sizing: border-box;
    height: 100%;
    padding: 0.2rem;
    width: 7rem;
    outline: none;
    border: 1px solid black;
    text-align: center;
    border-radius: 0.3rem;
}

.info-block {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    width: 100%;
}

.info-block .block-1 {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    border-bottom: 0.1rem solid #ccc;
    padding-bottom: 0.3rem;
    height: auto;
}

.info-block .options-block {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
}

.options-block:nth-child(2) {
    padding-top: 0.3rem;
}

.options-block:last-child {
    border-bottom: 0.1rem solid #ccc;
    padding-bottom: 0.3rem;
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
    margin: 0 0.5rem;
    color: black;
    border: 1px solid black;
    flex: 1;
}

.address-first-content {
    list-style: none;
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    width: 100%;
    border-bottom: 1px solid #ccc;
    padding: 0.5rem 1rem;
}

.address-first-content li {
    list-style: none;
    padding: 0.4rem 0.8rem;
    border-radius: 0.5rem;
    margin-right: 1rem;
    border: 2px solid black,
}


.send-money-info {
    width: 100%;
    padding: 1rem;
    border-bottom: 1px solid #ccc;
}
</style>
