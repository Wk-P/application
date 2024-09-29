<template>
    <ReturnBar />
    <h1 class="top-title">ordertails page</h1>
    <div class="container-block">
        <div class="img-block"><img v-if="order.item?.images && order.item?.images.length > 0" :src="order.item?.images[0].image" alt="" /></div>
        <div class="info-block">
            <div><span>ORDER ID</span><span>{{ order.orderId }}</span></div>
            <div><span>NAME</span><span>{{ order.item?.name }}</span></div>
            <div><span>PRICE</span><span>{{ order.item?.price }}</span></div>
            <div><span>QUANTITY</span><span>{{ order.quantity }}</span></div>
            <div><span>TOTAL PRICE</span><span>{{ order.totalPrice }}</span></div>
        </div>
        <div class="delivery-block">
            <div><span>STATUS</span><span>{{ order.status }}</span></div>
            <div><span>TRACKING NUMBER</span><span>{{ order.tracking_number }}</span></div>
        </div>
    </div>
</template>

<script lang="ts" setup name="orderdetailpage">
import type { Order } from "@/types/index";
import { useOrderStore } from "@/stores/index";
import { onMounted, ref } from "vue";
import ReturnBar from "@/components/ReturnBar.vue";
const order = ref<Order>(useOrderStore().order as Order);

onMounted(() => {
    console.log(order.value);
});
</script>

<style scoped>
.container-block {
    box-sizing: border-box;
    height: calc(100% - 8rem);
    overflow-y: auto;
    padding-bottom: 4rem;
}

.top-title {
    margin-top: 2.8rem;
    margin: 2.8rem 0.5rem 1rem 0.5rem;
    padding-bottom: 1rem;
    border-bottom: 2px solid black;
}

.img-block {
    box-sizing: border-box;
    width: 100vw;
}

.img-block img {
    box-sizing: border-box;
    padding: 0.5rem;
    width: 100%;
}

.info-block, .delivery-block {
    display: flex;
    flex-direction: column;
    border: 1px solid #ddd;
}

.info-block div, .delivery-block div {
    padding: 0.5rem 1rem;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
}
</style>
