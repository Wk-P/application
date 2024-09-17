<template>
    <nav class="head-bar">
        <button @click="returnPrev">
            <img src="/src_img/backarrow.png" alt=""/>
        </button>
        <h2>Class</h2>
    </nav>
    <div class="container">
        <div class="nav-link">
            <ClassHomePageRouterLinks />
        </div>
        <div class="page-view">
            <RouterView></RouterView>
        </div>
    </div>
</template>

<script lang="ts" setup name="ClassHomePage">
import { RouterView, useRouter } from "vue-router";
import ClassHomePageRouterLinks from "@/components/ClassHomePageRouterLinks.vue";
const router = useRouter();
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

.head-bar button img {
    box-sizing: border-box;
    height: 100%;
}

.container {
    padding-top: 4rem;
    height: calc(100vh - 4rem);
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
    width: fit-content;
    flex-shrink: 0; /* 防止因内容过多导致 nav-link 缩小 */
    overflow-y: auto; /* Allow vertical scroll */
    overflow-x: hidden; /* Prevent horizontal scroll */
    scrollbar-width: none; /* firefox */
    -ms-overflow-style: none; /* IE 10+ */
    border-top: 1px solid #333;
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
    border-top: 1px solid #333;
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
