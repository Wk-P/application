<template>
    <div class="nav-bar">
        <button @click="returnPrev">
            <div class="img-block">
                <img src="/src_img/backarrow.png" alt="" />
            </div>
        </button>
        <div><strong>{{ routePathTitle }}</strong></div>
        <button @click="toHome">
            <div class="img-block">
                <img src="/src_img/home1.png" alt="" />
            </div>
        </button>
    </div>
</template>

<script lang="ts" setup name="ReturnBar">
import { ref, onMounted } from "vue";
import { useRouter, useRoute } from "vue-router";
const router = useRouter();
const route = useRoute();
const returnPrev = () => {
    const routeName = route.matched[0]?.name;
    const routePath = route.path;
    if (routeName === "register") {
        router.push({ name: "user" });
    } else if (routePath === "class" && route.name === "class") {
        router.push({ name: "class" });
    } else if (routePath === "brand" && route.name === "brand") {
        router.push({ name: "brand" });
    } else if (routePath === "favorite" && route.name === "favorite") {
        router.push({ name: "favorite" });
    } else if (routePath == "user" && route.name === "user") {
        router.push({ name: "home" });
    } else {
        router.back();
    }
};

const toHome = () => {
    router.push({ name: "home" });
};

// 根据路径显示 title
const routePathTitle = ref<string | undefined>("");

onMounted(() => {
    if (route.name === 'favorite') {
        routePathTitle.value = route.name?.toString();
    } else if (route.name === 'usercenternav') {
        routePathTitle.value = "Usercenter";
    }
})

console.log(route.name);
console.log(routePathTitle.value);


</script>

<style scoped>
.nav-bar {
    position: fixed;
    left: 0;
    top: 0;
    width: 100%;
    height: 2.5rem;
    padding: 0.4rem;
    animation: 0.3s linear 0.1s slideIn1;
    background-color: white;
    display: flex;
    flex-direction: row;
    box-sizing: border-box;
    justify-content: space-between;
}

.nav-bar > div {
    flex: 1;
    text-align: center;
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
    background-color: white;
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
