<template>
    <ReturnBar />
    <div class="container" v-if="item">
        <div class="img-block">
            <img :src="item.imgLink" alt="item img" />
        </div>
        <div class="info-block">
            <div class="item-title">{{ item.name }}</div>
            <h2>$ 20,000</h2>
        </div>
        <div class="option-buttons">
            <button class="button-1">Favorite</button>
            <button class="button-2" @click="addToCart">Add to cart</button>
        </div>
    </div>
    <div class="container" v-else>
        <div class="error-block"><h3 class="error-hint">Item does not exist</h3></div>
    </div>
</template>

<script lang="ts" setup name="detailpage">
import ReturnBar from "@/components/ReturnBar.vue";
import { ref, onMounted } from "vue";
import type { Item } from "@/types/index";
import { useItemStore } from "@/stores/index";
const itemStore = useItemStore();
const addToCart = () => {
    fetch(`/api/items/cart/`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({item}),
    });
};
const item = ref<Item | null | undefined>(itemStore.item as Item | undefined);
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
