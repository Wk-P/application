<template>
    <ReturnBar />
    <div class="container" v-if="item">
        <div class="img-block">
            <img :src="item.image" alt="item img" />
        </div>
        <div class="info-block">
            <div class="item-title">{{ item.name }}</div>
            <div class="item-brand">{{ item.brand }}</div>
            <h2>$ {{ item.price }}</h2>
        </div>
        <div class="option-buttons">
            <button class="button-1">Favorite</button>
            <button class="button-2" @click="addToCart">Add to cart</button>
        </div>
    </div>
    <div class="container" v-else>
        <div class="error-block">
            <h3 class="error-hint">Item does not exist</h3>
        </div>
    </div>
</template>

<script lang="ts" setup name="detailpage">
import ReturnBar from "@/components/ReturnBar.vue";
import { ref, onMounted, computed } from "vue";
import type { Item } from "@/types/index";
import { useItemStore, useUserStore } from "@/stores/index";
import { useRoute, useRouter } from "vue-router";
const route = useRoute();
const router = useRouter();
const userStore = useUserStore();
const item = ref<Item | null>(null);
const isLoggedIn = computed(() => userStore.user ? true : false);

const fetchItemDetails = (id: string) => {
    if (userStore.user?.username === "admin") {
        router.push({ name: "user" });
    }
    if (!isLoggedIn.value) {
        router.push({ name: "user" });
    }
    fetch(`/api/items/details/${id}/`)
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
            item.value = data;
        });
};

const addToCart = () => {
    fetch(`/api/items/cart/`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            userId: userStore.user?.id,
            itemId: item.value?.id,
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
            if (data.error) {
                alert(data.error);
                return;
            } else {
                alert("Add item success");
            }
            window.location.reload();
        });
};

onMounted(() => {
    const item_params = route.params;
    fetchItemDetails(item_params.itemId as string);
});
</script>

<style scoped>
.error-block {
    display: flex;
    flex-direction: column;
    justify-content: center;
    height: 100%;
}

.error-hint {
    text-align: center;
}

.container {
    box-sizing: border-box;
    padding-top: 2.8rem;
    height: calc(100% - 9.8rem);
    width: 100%;
    overflow: auto;
    animation: 0.3s linear 0.1s slideIn;
    overflow-y: auto;
    scrollbar-width: none; /* firefox */
    -ms-overflow-style: none; /* IE 10+ */
    scroll-snap-type: x mandatory;
}

.container::-webkit-scrollbar {
    display: none;
}

.img-block {
    box-sizing: border-box;
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    flex: 0 0 100vw;
    background-color: rgba(0, 0, 0, 0.06);
    height: 60%;
    scroll-snap-align: center;
}

.img-block img {
    box-sizing: border-box;
    width: auto;
    height: 100%;
    object-fit: cover;
}

.info-block {
    box-sizing: border-box;
    width: 100%;
    padding: 1rem;
}

.item-title {
    font-size: 1.2rem;
}
.option-buttons {
    box-sizing: border-box;
    position: fixed;
    z-index: 1000;
    bottom: 4rem;
    left: 0;
    height: 3rem;
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: space-evenly;
    border: 0.5rem solid black;
}

.option-buttons .button-1 {
    box-sizing: border-box;
    border-right: 1px white solid;
    border-left: none;
    width: 50%;
    border-bottom: 1px solid black;
    border-top: 1px solid black;
    background-color: black;
    color: white;
}

.option-buttons .button-2 {
    border-left: 1px white solid;
    border-right: none;
    box-sizing: border-box;
    width: 50%;
    border-bottom: 1px solid black;
    border-top: 1px solid black;
    background-color: black;
    color: white;
}

/* animation */
@keyframes slideIn {
    from {
        opacity: 0;
        transform: translateX(-5rem);
    }
    to {
        opacity: 1;
        transform: translateX(0);
    }
}
</style>
