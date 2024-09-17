<template>
    <h2>ordertails page</h2>
    <div>
        <h3>order info</h3>
        <strong><i>{{ order }}</i></strong>
    </div>
</template>

<script lang="ts" setup name="orderdetailpage">
import type { Order } from "@/types/index";
import { useOrderStore } from "@/stores/index";
import { onMounted, ref } from "vue";
const order = ref<Order>(useOrderStore().order as Order);

onMounted(() => {
    console.log(order.value);
});
</script>

<style scoped></style>
