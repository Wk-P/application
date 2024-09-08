import { createRouter, createWebHistory, type RouteLocationNormalized, type NavigationGuardNext } from "vue-router";
import { useUserStore } from '@/stores/index';
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
import UploadItems from "@/pages/upload/uploadItems.vue";
import CustomAdmin from "@/pages/customadmin/App.vue";
import CustomAdminHome from "@/pages/customadmin/adminHome.vue";
import Details from "@/pages/details/App.vue";
import CustomOrder from "@/pages/usercenter/Order.vue";

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
            { path: "orders", name: "orders", component: CustomOrder },
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
        path: "/customadmin",
        name: "customadmin",
        component: CustomAdmin,
    },
    {
        path: "/customadmin",
        name: "customadmin",
        component: CustomAdmin,
        redirect: "/customadmin/home",
        children: [
            {
                path: "home",
                name: "adminHome",
                component: CustomAdminHome,
                beforeEnter: (_to: RouteLocationNormalized, _from: RouteLocationNormalized, next: NavigationGuardNext) => {
                    const userStore = useUserStore();
                    if (userStore.user?.loginStatus) {
                        next(); // 已登录，继续访问
                    } else {
                        next({ name: 'customadmin' }); // 未登录，重定向到登录页
                    }
                },
            },
            {
                path: "uploaditems",
                name: "uploaditems",
                component: UploadItems,
                beforeEnter: (_to: RouteLocationNormalized, _from: RouteLocationNormalized, next: NavigationGuardNext) => {
                    const userStore = useUserStore();
                    if (userStore.user?.loginStatus) {
                        next(); // 已登录，继续访问
                    } else {
                        next({ name: 'customadmin' }); // 未登录，重定向到登录页
                    }
                },
            },
        ]
    },
    {
        path: "/:pathMatch(.*)",
        redirect: "/404",
        hidden: true,
    },
    {
        path: '/details/:id',
        name: 'Details',
        component: Details,
    },
];

const router = createRouter({
    history: createWebHistory(),
    routes: routes,
});

export default router;
