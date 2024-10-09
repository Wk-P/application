<template>
    <ReturnBar />
    <div class="container">
        <div class="username-block">
            <div class="username-title">
                <span>{{ userStore.user?.username }}</span
                ><span>Welcome!</span>
            </div>
            <button @click="logout" class="logout-button">logout</button>
            <!-- <div class="ring-img"><img src="/src_img/ring1.png" alt="" /></div> -->
        </div>
        <div class="shopping-info">
            <h3 class="shopping-title">My Shopping</h3>
            <div class="links-block">
                <RouterLink :to="{ name: 'order' }" class="link-block">
                    <h4>Orders</h4>
                    <img src="/src_img/arrow-right.png" alt="" />
                </RouterLink>
                <RouterLink :to="{ name: 'cart' }" class="link-block">
                    <h4>Cart</h4>
                    <img src="/src_img/arrow-right.png" alt="" />
                </RouterLink>
                <RouterLink :to="{ name: 'favorite' }" class="link-block">
                    <h4>Favorite</h4>
                    <img src="/src_img/arrow-right.png" alt="" />
                </RouterLink>
            </div>
        </div>
        <div class="address-info">
            <h3 class="address-title">My Address & Receiver</h3>
            <div class="links-block">
                <RouterLink
                    :to="{ name: 'address_receiver' }"
                    class="link-block"
                >
                    <h4>Address & Receiver</h4>
                    <img src="/src_img/arrow-right.png" alt="" />
                </RouterLink>
            </div>
        </div>
        <div class="delivery-info">
            <h3 class="delivery-title">My Delivery</h3>
            <div class="links-block">
                <RouterLink
                    :to="{ name: 'address_receiver' }"
                    class="link-block"
                >
                    <h4>Delivery</h4>
                    <img src="/src_img/arrow-right.png" alt="" />
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
import ReturnBar from "@/components/ReturnBar.vue";
const router = useRouter();
const userStore = useUserStore();
</script>

<style scoped>
.logout-button {
    font-size: 1rem;
    color: white;
    background-color: black;
    border: none;
    padding: 0.5rem 1rem;
}

.container {
    box-sizing: border-box;
    height: calc(100% - 3rem);
    padding-top: 3rem;
    width: 100%;
    box-sizing: border-box;
    animation: 0.3s linear 0.1s slideIn;
    overflow-x: hidden;
    overflow-y: auto;
}

.username-block {
    box-sizing: border-box;
    height: 5rem;
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    padding: 0.5rem 1rem;
}

.username-title {
    box-sizing: border-box;
    height: 100%;
    flex: 1;
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
    font-size: 1.2rem;
    font-weight: bolder;
}

.username-title span {
    padding-right: 1rem;
}

.username-title span:nth-child(1) {
    flex: 1;
}

.shopping-info,
.delivery-info,
.address-info {
    box-sizing: border-box;
    width: 100%;
    padding: 1rem;
}

.shopping-title,
.delivery-title,
.address-title {
    padding-bottom: 1rem;
    border-bottom: 1px solid #eee;
}

.links-block {
    box-sizing: border-box;
    width: 100%;
    display: flex;
    flex-direction: column;
}

.link-block {
    box-sizing: border-box;
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
    box-sizing: border-box;
    padding: 0.2rem;
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
