import { createRouter, createWebHistory } from "vue-router";
import { useUserStore } from '@/stores/index';
import Login from "@/pages/login/App.vue";
import Register from "@/pages/register/App.vue";
import Step1Register from "@/components/Step1Register.vue";
import Step2Register from "@/components/Step2Register.vue";
import Start from "@/pages/start/App.vue";
import Cart from "@/pages/cart/App.vue";
import NotFoundPage from "@/pages/404page/App.vue";
import UploadItems from "@/pages/upload/uploadItems.vue";
import CustomAdmin from "@/pages/customadmin/App.vue";
import CustomAdminHome from "@/pages/customadmin/adminHome.vue";
import Details from "@/pages/details/App.vue";

import Home1 from "@/pages/homepages/homepage.vue";
import homepage1 from "@/pages/homepages/page1.vue";
import homepage2 from "@/pages/homepages/page2.vue";
import homepage3 from "@/pages/homepages/page3.vue";
import homepage4 from "@/pages/homepages/page4.vue";
import homepage5 from "@/pages/homepages/page5.vue";
import homepage6 from "@/pages/homepages/page6.vue";

import classhomepage from "@/pages/classpages/classhomepage.vue";
import classpage1 from "@/pages/classpages/classpage1.vue";
import classpage2 from "@/pages/classpages/classpage2.vue";
import classpage3 from "@/pages/classpages/classpage3.vue";
import classpage4 from "@/pages/classpages/classpage4.vue";
import classpage5 from "@/pages/classpages/classpage5.vue";

import brandhomepage from "@/pages/brandpages/brandhomepage.vue";

import favoritehomepage from "@/pages/favoritepages/favoritehomepage.vue";

import usercenterpage from "@/pages/usercenterpages/usercenterhome.vue";

import searchpage from "@/pages/searchpages/searchpage.vue";

const routes = [
    {
        path: "/",
        name: "home",
        component: Home1,
        redirect: { name: "homepage1" },
        children: [
            { path: "homepage1", name: 'homepage1', component: homepage1 },
            { path: "homepage2", name: 'homepage2', component: homepage2 },
            { path: "homepage3", name: 'homepage3', component: homepage3 },
            { path: "homepage4", name: 'homepage4', component: homepage4 },
            { path: "homepage5", name: 'homepage5', component: homepage5 },
            { path: "homepage6", name: 'homepage6', component: homepage6 },
        ]
    },
    {
        path: "/class",
        name: "class",
        component: classhomepage,
        redirect: { name: "classpage1" },
        children: [
            { path: "classpage1", name: 'classpage1', component: classpage1 },
            { path: "classpage2", name: 'classpage2', component: classpage2 },
            { path: "classpage3", name: 'classpage3', component: classpage3 },
            { path: "classpage4", name: 'classpage4', component: classpage4 },
            { path: "classpage5", name: 'classpage5', component: classpage5 },
        ]
    },
    {
        path: "/brand",
        name: "brand",
        component: brandhomepage,
    },
    {
        path: "/favorite",
        name: "favorite",
        component: favoritehomepage,
    },
    {
        path: "/user",
        name: "user",
        component: usercenterpage,
    },
    {
        path: "/search",
        name: "search",
        component: searchpage,
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
        children: [
            {
                path: "home",
                name: "adminHome",
                component: CustomAdminHome,
                beforeEnter: (_to: any, _from: any, next: any) => {
                    const userStore = useUserStore();
                    if (userStore.user?.loginStatus) {
                        next();
                    } else {
                        next({ name: 'customadmin' }); // 未登录，重定向到登录页
                    }
                },
            },
            {
                path: "uploaditems",
                name: "uploaditems",
                component: UploadItems,
                beforeEnter: (_to: any, _from: any, next: any) => {
                    const userStore = useUserStore();
                    if (userStore.user?.loginStatus) {
                        next();
                    } else {
                        next({ name: 'customadmin' });
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
