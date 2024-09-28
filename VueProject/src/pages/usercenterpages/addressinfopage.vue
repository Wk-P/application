<template>
    <ReturnBar />
    <div class="container">
        <h2 class="page-title">Address & Receiver Info</h2>
        <ul>
            <li v-for="addr_recv in addressReceiverList">
                <RouterLink :to="{name: 'address_modify', params: {'addrRecvId': addr_recv.id, 'addr': addr_recv.address, 'recv': addr_recv.receiver}}">
                    <span>{{ addr_recv.address }}</span>
                    <span>{{ addr_recv.receiver }}</span>
                </RouterLink>
            </li>
        </ul>
        <div class="button-group">
            <button @click="toAddInfomation">Add</button>
            <button @click="toUsercenterHome">My Page</button>
        </div>
    </div>
</template>

<script lang="ts" setup name="addressinfopage">
import ReturnBar from "@/components/ReturnBar.vue";
import type { AddressReceiver } from "@/types/index";
import { useRouter, RouterLink } from "vue-router";
import { useUserStore } from "@/stores/index";
import { ref, onMounted } from "vue";

const router = useRouter();
const userStore = useUserStore();
const addressReceiverList = ref<Array<AddressReceiver>>([]);

const getAllAddressReceiver = () => {
    const user_id = userStore.user?.id;
    fetch(`/api/user/address/${user_id}/`)
        .then((response) => {
            if (!response.ok) {
                response.json().then((error) => {
                    console.log(error);
                    throw new Error(error);
                });
            } else {
                return response.json();
            }
        })
        .then((data) => {
            addressReceiverList.value = data;
        });
};

const toAddInfomation = () => {
    router.push({ name: "address_add" });
};

const toUsercenterHome = () => {
    router.push({ name: "user" });
};

onMounted(() => {
    getAllAddressReceiver();
});
</script>

<style scoped>
.container {
    height: calc(100% - 6.8rem);
    padding-top: 2.8rem;
    padding-bottom: 4rem;
    overflow-y: auto;
}

.page-title {
    margin: 0 3rem;
    padding-bottom: 0.5rem;
    text-align: center;
    border-bottom: 2px solid black;
}

.address-container,
.receiver-container,
.tel-container,
.email-container {
    box-sizing: border-box;
    width: 100%;
    padding: 1rem 4rem;
    display: flex;
    flex-direction: column;
}

.address-container input,
.receiver-container input,
.tel-container input,
.email-container input {
    margin-top: 0.4rem;
    border: 2px solid black;
    outline: none;
    padding: 0.5rem 1rem;
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
    margin: 0 0.5rem;
    flex: 1;
}
</style>
