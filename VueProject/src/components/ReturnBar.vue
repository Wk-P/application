<template>
    <div class="nav-bar">
        <button @click="returnPrev">
            <div class="img-block">
                <img src="/src_img/backarrow.png" alt="" />
            </div>
        </button>
    </div>
</template>

<script lang="ts" setup name="ReturnBar">
import { useRouter, useRoute } from "vue-router";
const router = useRouter();
const route = useRoute();
const returnPrev = () => {
    const routeName = route.matched[0]?.name;
    if (routeName === "register") {
        router.push({ name: "user" });
    } else if (routeName === 'class' || routeName === 'brand' || routeName === 'favorite') {
        router.push({ name: "home" });
    } else {
        router.back();
    }
};
</script>

<style scoped>
.nav-bar {
    position: fixed;
    left: 0;
    top: 0;
    width: 100%;
    height: 2rem;
    padding: 0.4rem;
    animation: 0.3s linear 0.1s slideIn1;
    background-color: white;
}

.nav-bar button {
    height: 100%;
    border: none;
}

.img-block {
    height: 100%;
}

.img-block img {
    box-sizing: border-box;
    height: 100%;
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
