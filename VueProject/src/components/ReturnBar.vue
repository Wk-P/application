<template>
    <div class="nav-bar">
        <button @click="returnPrev">
            <div class="img-block">
                <img
                    src="/src_img/backarrow.png"
                    alt="" />
            </div>
        </button>
        <div>
            <strong>{{ routePathTitle }}</strong>
        </div>
        <button @click="toHome">
            <div class="img-block">
                <img
                    src="/src_img/home1.png"
                    alt=""
                    class="home-img" />
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
    const routeName = route.name;
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
    const parentPathMatched0 = route.matched[0]?.path;
    const parentPathMatched1 = route.matched[1]?.path;

    console.log(parentPathMatched0, parentPathMatched1);
    console.log(parentPathMatched1 === '/user/createorder');

    if (parentPathMatched0 === "/favorite") {
        routePathTitle.value = parentPathMatched0.split("/")[1];
    } else if (parentPathMatched0 === "/user") {
        if (parentPathMatched1 === "/user/order") {
            routePathTitle.value = parentPathMatched1.split("/")[2];
        } else if (parentPathMatched1 === "/user/cart") {
            routePathTitle.value = parentPathMatched1.split("/")[2];
        }  else if (parentPathMatched1 === '/user/createorder') {
            routePathTitle.value = "주문/결제";
        } else {
            // login
            routePathTitle.value = parentPathMatched0.split("/")[1];
        }
    } else if (parentPathMatched0 === "/brand") {
        // brand
        routePathTitle.value = parentPathMatched0.split("/")[1];
    } else if (parentPathMatched0 === "/class") {
        // class
        routePathTitle.value = parentPathMatched0.split("/")[1];
    } else if (parentPathMatched0 === "/address/info") {
        // address info
        routePathTitle.value = parentPathMatched0.split("/")[1];
    }
});

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
    padding-right: 0.8rem;
    border-bottom: 1px solid #eee;
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

.home-img {
    padding: 0.2rem;
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
