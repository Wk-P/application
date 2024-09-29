<template>
    <ReturnBar />
    <div class="container">
        <h2 class="page-title">Address & Receiver Modify</h2>
        <div class="address-container">
            <h3>Address</h3>
            <input type="text" v-model="address" />
        </div>
        <div class="receiver-container">
            <h3>Receiver</h3>
            <input type="text" v-model="receiver" />
        </div>
        <div class="button-group">
            <button @click="modifyInfomation">Save</button>
            <button @click="toUsercenterHome">My Page</button>
        </div>
    </div>
</template>

<script lang="ts" setup name="addressmodifypage">
import ReturnBar from "@/components/ReturnBar.vue";
import { useRouter, useRoute } from "vue-router";
import { useUserStore } from "@/stores/index";
import { ref } from "vue";

const router = useRouter();
const route = useRoute();
console.log(route.params);
const address = ref<string>(route.params.addr as string);
const receiver = ref<string>(route.params.recv as string);

const user_id = useUserStore().user?.id;

const addrRecvId = route.params.addrRecvId as string;
const modifyInfomation = () => {
    fetch(`/api/user/address/modified/${user_id}/${addrRecvId}/`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            address: address.value,
            receiver: receiver.value,
        }),
    })
        .then((response) => {
            if (!response.ok) {
                response.json().then((error) => {
                    console.log(error);
                    throw new Error(error);
                });
            }
            return response.json();
        })
        .then((data) => {
            console.log(data);
            router.push({ name: "address_receiver" });
        });
};
const toUsercenterHome = () => {
    router.push({ name: "user" });
};
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
