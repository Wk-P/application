<template>
    <ReturnBar />
    <div class="container">
        <ul v-if="addressReceiverList.length > 0" class="address-ul">
            <li v-for="addr_recv in addressReceiverList">
                <RouterLink :to="{name: 'address_modify', params: {'addrRecvId': addr_recv.id, 'addr': addr_recv.address, 'recv': addr_recv.receiver}}">
                    <span>{{ addr_recv.address }}</span>
                    <span>{{ addr_recv.receiver }}</span>
                </RouterLink>
            </li>
        </ul>
        <div v-else class="add-new-address-link">
            <RouterLink :to="{ name: 'address_add'}">Add new address</RouterLink>
        </div>
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
    width: 100%;
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

.add-new-address-link {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 60%;
    width: 100%;
}

.add-new-address-link a {
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 2rem;
    padding: 1rem;
    text-decoration: none;
    border: 2px solid black;
    color: black;
}

.address-ul {
    display: flex;
    flex-direction: column;
    height: 100%;
    width: 100%;
    list-style: none;
}

.address-ul li {
    width: 100%;
    display: flex;
    flex-direction: row;
}

.address-ul li a {
    box-sizing: border-box;
    padding: 1rem 1rem;
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: space-between;
    text-decoration: none;
    color: white;
    background-color: black;
    margin: 1rem;
    height: 3.6rem;
    border-radius: 1.5rem;
}
</style>
