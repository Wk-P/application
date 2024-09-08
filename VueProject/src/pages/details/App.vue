<template>
    <OptionHeader />
    <ReturnBar />
    <div class="block">
        <div class="img-block">
            <img :src="item?.imgLink" alt="" />
        </div>
        <div class="title">{{ item?.title }}</div>
        <div class="description">{{ item?.desc }}</div>
        <div class="name">{{ item?.name }}</div>
    </div>
    <div class="button-group">
        <button class="cart-button" @click="addToCart">장바구니 담기</button>
    </div>
    <FooterBlock />
</template>

<script lang="ts" setup name="Details">
import OptionHeader from "@/components/OptionHeader.vue";
import FooterBlock from "@/components/FooterBlock.vue";
import ReturnBar from "@/components/ReturnBar.vue";
import { useItemStore, useUserStore } from "@/stores";
import type { Item, User } from "@/types/index";
import { ref, onMounted, computed } from "vue";
import { useRouter } from "vue-router";

const itemStore = useItemStore();
const userStore = useUserStore();
const item = ref<Item | null>(null);
const user = ref<User | null>(null);
const isLoggedIn = computed(() => userStore.user?.loginStatus);
const router = useRouter();

const addToCart = () => {
    if (!isLoggedIn.value) {
        if (!confirm("로그인 먼저 해주세요!")) {
            return;
        }
        router.push({ name: "login" });
        return;
    }

    if (!confirm(`Add to your cart?`)) {
        return;
    }

    fetch(`/api/items/cart/`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            username: user.value?.username,
            item_id: item.value?.id,
        }),
    })
        .then((response) => {
            if (response.ok) {
                alert(`장바구니에 가입 완료됐습니다!`);
            } else {
                throw Error(`HTTP error, status ${response.status}`);
            }
        })
        .catch((error) => {
            console.log(error);
        });
};

onMounted(() => {
    item.value = itemStore.item;
    user.value = userStore.user;
});
</script>

<style scoped>
.button-group {
    box-sizing: border-box;
    width: 100%;
    padding: 0.5rem;
}

.button-group button {
    box-sizing: border-box;
    width: 100%;
    padding: 1.5rem;
    font-size: 0.9rem;
    background-color: white;
    border: 1px solid black;
}

.block {
    display: flex;
    flex-direction: column;
    justify-content: start;
    box-sizing: border-box;
    width: 100%;
    padding: 0.2rem;
}

.img-block {
    box-sizing: border-box;
    width: 100%;
}

.img-block img {
    box-sizing: border-box;
    width: 100%;
    height: auto;
}

.title,
.name,
.description {
    box-sizing: border-box;
    padding: 1rem 2rem;
}
</style>
