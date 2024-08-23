import { createRouter, createWebHistory } from "vue-router";
import Login from "@/pages/login/App.vue";
import Register from "@/pages/register/App.vue";
import Product from "@/pages/product/App.vue";
import Comments from "@/pages/comments/App.vue";
import Details from "@/pages/details/App.vue";
import UserCenter from "@/pages/usercenter/App.vue"
import Orders from "@/pages/orders/App.vue";
import Cart from "@/pages/cart/App.vue";
import Favorite from "@/pages/favorite/App.vue";

import MobileHome from  "@/pages/mobilehome/App.vue";
import Start from "@/pages/start/App.vue";

const routes = [
    {
        path: "/",
        name: "home",
        component: MobileHome,
    },
    {
        path: "/start",
        name: "start",
        component: Start,
    },
    {
        path: "/login",
        name: "login",
        component: Login,
    },
    {
        path: "/register",
        name: "register",
        component: Register,
    }
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;
