<template>
    <ReturnBar />
    <div class="container">
        <div class="nav-link">
            <BrandHomePageRouterLinks />
        </div>
        <div class="page-view">
            <RouterView></RouterView>
        </div>
    </div>
</template>

<script lang="ts" setup name="ClassHomePage">
import { RouterView } from "vue-router";
import BrandHomePageRouterLinks from "@/components/BrandHomePageRouterLinks.vue";
import ReturnBar from "@/components/ReturnBar.vue";

</script>

<style scoped>
.container {
    padding-top: 3rem;
    height: calc(100% - 4rem);
    width: 100%;
    box-sizing: border-box;
    display: flex;
    flex-direction: row;
    animation: 0.3s linear 0.1s slideIn;
    overflow: hidden;
}

.nav-link {
    background-color: #eee;
    box-sizing: border-box;
    height: 100%;
    width: 30vw;
    flex-shrink: 0; /* 防止因内容过多导致 nav-link 缩小 */
    overflow-y: auto; /* Allow vertical scroll */
    overflow-x: hidden; /* Prevent horizontal scroll */
    scrollbar-width: none; /* firefox */
    -ms-overflow-style: none; /* IE 10+ */
}

.nav-link::-webkit-scrollbar {
    display: none; /* Chrome Safari */
}

.page-view {
    box-sizing: border-box;
    padding: 1.5rem;
    flex: 1;
    height: 100%; /* 高度为父容器的 100% */
    overflow-y: auto; /* Allow vertical scroll */
    overflow-x: hidden; /* Prevent horizontal scroll */
    scrollbar-width: none; /* firefox */
    -ms-overflow-style: none; /* IE 10+ */
}

.page-view::-webkit-scrollbar {
    display: none; /* Chrome Safari */
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
