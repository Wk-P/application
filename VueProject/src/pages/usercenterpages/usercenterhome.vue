<template>
    <nav class="head-bar">
        <button @click="returnPrev">
            <img src="/src_img/backarrow.png" alt="" />
        </button>
        <h2>My Page</h2>
        <button @click="logout" class="logout-button"><strong>logout</strong></button>
    </nav>
    <div class="container">
        <div class="username-block">
            <div class="username-title">
                <span>{{ userStore.user?.username }}</span
                ><span>Welcome!</span>
            </div>
            <div class="ring-img"><img src="/src_img/ring1.png" alt="" /></div>
        </div>
        <div class="shopping-info">
            <h3 class="shopping-title">My Shopping</h3>
            <div class="links-block">
                <RouterLink :to="{ name: 'order' }" class="link-block">
                    <h4>Orders</h4>
                    <img src="/src_img/rightarrow.png" alt="" />
                </RouterLink>
                <RouterLink :to="{ name: 'cart' }" class="link-block">
                    <h4>Cart</h4>
                    <img src="/src_img/rightarrow.png" alt="" />
                </RouterLink>
                <RouterLink :to="{ name: 'user' }" class="link-block">
                    <h4>Favorite</h4>
                    <img src="/src_img/rightarrow.png" alt="" />
                </RouterLink>
            </div>
        </div>
        <div class="delivery-info">
            <h3 class="delivery-title">My Delivery</h3>
            <div class="links-block">
                <RouterLink :to="{ name: 'order' }" class="link-block">
                    <h4>Address & Receiver</h4>
                    <img src="/src_img/rightarrow.png" alt="" />
                </RouterLink>
            </div>
        </div>
    </div>
</template>

<script lang="ts" setup name="usercenterhome">
import { ref } from "vue";
import { useUserStore } from "@/stores/index";
import { useRouter, RouterLink } from "vue-router";
import { logout } from "@/utils/utils";
const router = useRouter();
const userStore = useUserStore();
const returnPrev = () => {
    router.push({ name: "home" });
};
</script>

<style scoped>
.head-bar {
    box-sizing: border-box;
    display: flex;
    flex-direction: row;
    height: 4rem;
    position: fixed;
    left: 0;
    top: 0;
    width: 100%;
    animation: 0.3s linear 0.1s slideIn1;
}
.head-bar h2 {
    display: flex;
    flex-direction: column;
    justify-content: center;
    text-align: center;
    box-sizing: border-box;
    padding: 1rem;
    height: 100%;
    width: 100%;
    background-color: white;
}

.head-bar button {
    box-sizing: border-box;
    height: 100%;
    padding: 1rem;
    background-color: white;
    border: none;
}

.logout-button {
    font-size: 1.2rem;
}

.head-bar button img {
    box-sizing: border-box;
    height: 100%;
}

.container {
    box-sizing: border-box;
    padding-top: 4rem;
    width: 100%;
    box-sizing: border-box;
    animation: 0.3s linear 0.1s slideIn;
    overflow: hidden;
}

.username-block {
    box-sizing: border-box;
    height: 5rem;
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    border-top: 1px solid #333;
    padding: 0 2rem;
}

.username-title {
    box-sizing: border-box;
    height: 100%;
    flex: 1;
    display: flex;
    flex-direction: row;
    align-items: center;
    font-size: 1.5rem;
    font-weight: bolder;
}

.username-title span:nth-child(1) {
    padding-right: 0.5rem;
}

.username-title span:nth-child(2) {
    padding: 0 1rem;
}

.ring-img {
    box-sizing: border-box;
    height: 100%;
}

.ring-img img {
    box-sizing: border-box;
    padding: 1.6rem 1rem 1.6rem 1.6rem;
    height: 100%;
}

.shopping-info,
.delivery-info {
    box-sizing: border-box;
    width: 100%;
    padding: 2rem;
}

.shopping-title, .delivery-title {
    padding-bottom: 1rem;
    border-bottom: 1px solid black;
}

.links-block {
    padding-top: 0.5rem;
    box-sizing: border-box;
    width: 100%;
    display: flex;
    flex-direction: column;
}

.link-block {
    box-sizing: border-box;
    padding: 0.3rem 0;
    color: black;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    text-decoration: none;
}

.link-block h4 {
    display: flex;
    flex-direction: column;
    justify-content: center;
    height: 100%;
    flex: 1;
}

.link-block img {
    height: 2rem;
}

@keyframes slideIn {
    from {
        transform: translateX(-2rem);
        opacity: 0;
    }
    to {
        transform: translateX(0);
        opacity: 1;
    }
}

@keyframes slideIn1 {
    from {
        transform: translateY(-2rem);
        opacity: 0;
    }
    to {
        transform: translateY(0);
        opacity: 1;
    }
}
</style>
