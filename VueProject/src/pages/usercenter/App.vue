<template>
    <div class="containers-head" ref="containersHead">
        <OptionHeader />
    </div>
    <div>
        <RouterView />
    </div>
    <nav>
        <RouterLink to="/usercenter/home" class="nav-link" v-if="route.path === '/usercenter/modified'">Home</RouterLink>
        <RouterLink to="/usercenter/modified" class="nav-link" v-if="route.path === '/usercenter/home'">Modifed</RouterLink>
        <RouterLink to="/usercenter/orders" class="nav-link" v-if="route.path === '/usercenter/home'">Orders</RouterLink>
    </nav>
    <FooterBlock />
</template>

<script lang="ts" setup name="usercenter">
import { RouterView, RouterLink, useRoute } from "vue-router";
import OptionHeader from "@/components/OptionHeader.vue";
import FooterBlock from "@/components/FooterBlock.vue";
import ReturnBar from "@/components/ReturnBar.vue";

const route = useRoute();

</script>
<style scoped>
nav {
    box-sizing: border-box;
    width: 100%;
    padding-bottom: 2em;
    display: flex;
    justify-content: space-evenly;
}
nav a {
    height: 100%;
    padding: 1.5rem 4rem;
    font-size: 0.8rem;
    text-decoration: none;
    border: 1px solid black;
    color: black;
}
</style>
