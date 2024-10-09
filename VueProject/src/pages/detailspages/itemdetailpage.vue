<template>
    <ReturnBar />
    <div class="container" v-if="item">
        <div class="sub-container-1">
            <div class="img-block">
                <!-- 多个图片轮播显示 -->
                <ul>
                    <li v-for="i in item.images">
                        <img :src="i.image" alt="" />
                    </li>
                </ul>
            </div>
            <div class="info-block">
                <div class="item-title">{{ item.name }}</div>
                <h2>$ {{ item.price }}</h2>
                <div class="item-brand">{{ item.brand }}</div>
                <div class="item-desc">{{ item.desc }}</div>
            </div>
        </div>
        <div class="option-buttons">
            <button class="button-1" @click="addToFavorite">
                <img src="/src_img/heart2.png" alt="" />
            </button>
            <button class="button-2" @click="addToCart">
                <img src="/src_img/cart2.png" alt="" />
            </button>
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
import { useUserStore } from "@/stores/index";
import { useRoute, useRouter } from "vue-router";
const route = useRoute();
const router = useRouter();
const userStore = useUserStore();
const item = ref<Item | null>(null);
const isLoggedIn = ref<boolean>(
    userStore.user && userStore.user?.username !== "admin" ? true : false
);
const fetchItemDetails = (id: string) => {
    fetch(`/api/items/details/${id}/`)
        .then((response) => {
            if (!response.ok) {
                response.json().then((error) => {
                    console.log(error);
                    throw new Error(
                        `Error! HTTP status code ${response.status}`
                    );
                });
            }
            return response.json();
        })
        .then((data) => {
            item.value = data;
            console.log(item.value);
        });
};

const addToFavorite = () => {
    if (!isLoggedIn.value) {
        router.push({ name: "user" });
    }

    fetch(`/api/items/favorite_add/`, {
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
                    throw new Error(
                        `Error! HTTP status code ${response.status}`
                    );
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
        });
};

const addToCart = () => {
    if (!isLoggedIn.value) {
        router.push({ name: "user" });
    }
    fetch(`/api/items/cart_add/`, {
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
                    throw new Error(
                        `Error! HTTP status code ${response.status}`
                    );
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
    overflow: auto;
    height: calc(100% - 9.8rem);
}

.container::-webkit-scrollbar {
    display: none;
}

.sub-container-1 {
    box-sizing: border-box;
    padding-top: 2.6rem;
    height: 100%;
    width: 100%;
    overflow: auto;
    scrollbar-width: none; /* firefox */
    -ms-overflow-style: none; /* IE 10+ */
    scroll-snap-type: x mandatory;
    animation: 0.3s linear 0.1s slideIn1;
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

.img-block ul {
    display: flex;
    flex-direction: row;
    list-style: none;
    height: 100%;
    overflow-x: auto;
    scroll-snap-type: x mandatory;
    animation: 0.3s linear 0.1s slideIn1;
}

.img-block ul::-webkit-scrollbar {
    display: none; /* Chrome Safari */
}

.img-block > ul > li {
    scroll-snap-align: center;
}

.img-block > ul > li > img {
    height: 100%;
    width: 100vw;
    object-fit: contain;
}

.info-block {
    box-sizing: border-box;
    width: 100%;
    padding: 1rem;
}

.item-title {
    font-size: 1.2rem;
}

.item-brand,
.item-desc {
    padding: 0.5rem 0;
}
.option-buttons {
    box-sizing: border-box;
    position: absolute;
    height: 3rem;
    bottom: 4rem;
    width: 100vw;
    display: flex;
    flex-direction: row;
    border: 0.5rem solid black;
    z-index: 1000;
    animation: 0.3s linear 0.1s slideIn2;
}

.option-buttons .button-1 {
    box-sizing: border-box;
    border-right: 1px white solid;
    border-left: none;
    width: 50%;
    height: 100%;
    border-bottom: 2px solid black;
    border-top: 2px solid black;
    background-color: black;
    color: white;
}

.button-1 img {
    box-sizing: border-box;
    padding: 0.2rem;
    height: 100%;
    background-color: black;
}

.button-2 img {
    box-sizing: border-box;
    padding: 0.2rem;
    height: 100%;
    background-color: black;
}

.option-buttons .button-2 {
    border-left: 1px white solid;
    border-right: none;
    box-sizing: border-box;
    width: 50%;
    height: 100%;
    border-bottom: 2px solid black;
    border-top: 2px solid black;
    background-color: black;
    color: white;
}

/* animation */
@keyframes slideIn1 {
    from {
        opacity: 0;
        transform: translateX(-5rem);
    }
    to {
        opacity: 1;
        transform: translateX(0);
    }
}

@keyframes slideIn2 {
    from {
        opacity: 0;
        transform: translateY(5rem);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}
</style>
