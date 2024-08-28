import { createRouter, createWebHistory } from "vue-router";
import Login from "@/pages/login/App.vue";
import Register from "@/pages/register/App.vue";
import Step1Register from "@/components/Step1Register.vue";
import Step2Register from "@/components/Step2Register.vue";
import UserCenter from "@/pages/usercenter/App.vue"
import MobileHome from "@/pages/mobilehome/App.vue";
import Start from "@/pages/start/App.vue";
import Favorite from "@/pages/favorite/App.vue";
import Cart from "@/pages/cart/App.vue";
import NotFoundPage from "@/pages/404page/App.vue";
import UsercenterHome from "@/components/UsercenterHome.vue";
import UsercenterModified from "@/components/UsercenterModified.vue";

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
        redirect: "/register/step1",
        children: [
            { path: "step1", name: "Step1Register", component: Step1Register },
            { path: "step2", name: "Step2Register", component: Step2Register, meta: { requiresStep1: true } },
        ]
    },
    {
        path: "/usercenter",
        name: "usercenter",
        component: UserCenter,
        redirect: "/usercenter/home",
        children: [
            { path: "home", name: "usercenterhome", component: UsercenterHome },
            { path: "modified", name: "usercentermodified", component: UsercenterModified },
        ]
    },
    {
        path: "/favorite",
        name: "favorite",
        component: Favorite,
    },
    {
        path: "/cart",
        name: "cart",
        component: Cart,
    },
    {
        path: "/404",
        name: "404page",
        component: NotFoundPage,
    },
    {
        path: "/:pathMatch(.*)",
        redirect: "/404",
        hidden: true,
    },
    // {
    //     path: '/admin',
    //     redirect: () => {
    //         window.location.href = '/api/admin/';
    //         return '/';
    //     }
    // },
    // {
    //     path: '/admin/logout',
    //     redirect: () => {
    //         window.location.href = '/api/admin/logout';
    //         return '/';
    //     }
    // },
];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;
