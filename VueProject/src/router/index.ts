import { createRouter, createWebHistory } from "vue-router";
import Register from "@/pages/registerpages/registerpage.vue";
import Step1Register from "@/pages/registerpages/registerstep1.vue";
import Step2Register from "@/pages/registerpages/registerstep2.vue";
import NotFoundPage from "@/pages/404page/App.vue";

import Home1 from "@/pages/homepages/homepage.vue";
import homepage1 from "@/pages/homepages/page1.vue";
import homepage2 from "@/pages/homepages/page2.vue";
import homepage3 from "@/pages/homepages/page3.vue";
import homepage4 from "@/pages/homepages/page4.vue";
import homepage5 from "@/pages/homepages/page5.vue";
import homepage6 from "@/pages/homepages/page6.vue";

import classhomepage from "@/pages/classpages/classhomepage.vue";
import necklacepage from "@/pages/classpages/necklacepage.vue";
import earringspage from "@/pages/classpages/earringspage.vue";
import braceletpage from "@/pages/classpages/braceletpage.vue";
import ringpage from "@/pages/classpages/ringpage.vue";
import otherspage from "@/pages/classpages/otherspage.vue";
import menpage from "@/pages/classpages/menpage.vue";
import womenpage from "@/pages/classpages/womenpage.vue";
import couplepage from "@/pages/classpages/couplepage.vue";

import brandhomepage from "@/pages/brandpages/brandhomepage.vue";
import brandpage1 from "@/pages/brandpages/brandpage1.vue";
import brandpage2 from "@/pages/brandpages/brandpage2.vue";
import brandpage3 from "@/pages/brandpages/brandpage3.vue";
import brandpage4 from "@/pages/brandpages/brandpage4.vue";
import brandpage5 from "@/pages/brandpages/brandpage5.vue";


import favoritehomepage from "@/pages/favoritepages/favoritehomepage.vue";

import usercenternav from "@/pages/usercenterpages/usercenternav.vue";
import orderspage from "@/pages/usercenterpages/orderspage.vue";
import cartpage from "@/pages/usercenterpages/cartpage.vue";
import createorderpage from "@/pages/usercenterpages/createorderpage.vue";
import orderdetailpage from "@/pages/usercenterpages/orderdetailpage.vue";
import addressinfopage from "@/pages/usercenterpages/addressinfopage.vue";
import addressmodifypage from "@/pages/usercenterpages/addressmodifypage.vue";
import addressaddpage from "@/pages/usercenterpages/addressaddpage.vue";


import searchpage from "@/pages/searchpages/searchpage.vue";
import itemdetailpage from "@/pages/detailspages/itemdetailpage.vue";


import annoucementpage from "@/pages/bulletinboardpages/announcementpage.vue";
import noticedetails from "@/pages/bulletinboardpages/noticedetails.vue";



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
        redirect: { name: "necklace" },
        children: [
            { path: "necklace", name: 'necklace', component: necklacepage },
            { path: "earrings", name: 'earrings', component: earringspage },
            { path: "bracelet", name: 'bracelet', component: braceletpage },
            { path: "ring", name: 'ring', component: ringpage },
            { path: "others", name: 'others', component: otherspage },
            { path: "men", name: 'men', component: menpage },
            { path: "women", name: 'women', component: womenpage },
            { path: "couple", name: 'couple', component: couplepage },
        ]
    },
    {
        path: "/brand",
        name: "brand",
        component: brandhomepage,
        redirect: { name: "brandpage1" },
        children: [
            { path: "brandpage1", name: 'brandpage1', component: brandpage1 },
            { path: "brandpage2", name: 'brandpage2', component: brandpage2 },
            { path: "brandpage3", name: 'brandpage3', component: brandpage3 },
            { path: "brandpage4", name: 'brandpage4', component: brandpage4 },
            { path: "brandpage5", name: 'brandpage5', component: brandpage5 },
        ]
    },
    {
        path: "/favorite",
        name: "favorite",
        component: favoritehomepage,
    },
    {
        path: "/user",
        name: "user",
        redirect: { name: "usercenternav" },
        children: [
            { path: "home", name: "usercenternav", component: usercenternav },
            { path: "order", name: 'order', component: orderspage },
            { path: "cart", name: 'cart', component: cartpage },
            { path: 'createorder', name: 'createorder', component: createorderpage },
            { path: 'orderdetail', name: 'orderdetail', component: orderdetailpage },
        ]
    },
    {
        path: "/search",
        name: "search",
        component: searchpage,
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
        path: "/404",
        name: "404page",
        component: NotFoundPage,
    },
    {
        path: "/:pathMatch(.*)",
        redirect: "/404",
        hidden: true,
    },
    {
        path: '/details/:itemId/:brand/:itemTitle/:itemName',
        name: 'itemdetail',
        component: itemdetailpage,
    },
    {
        path: '/address/info',
        name: 'address_receiver',
        component: addressinfopage,
    },
    {
        path: '/address/info/modify/:addrRecvId/:addr/:recv',
        name: 'address_modify',
        component: addressmodifypage,
    },
    {
        path: '/address/info/add',
        name: 'address_add',
        component: addressaddpage,
    },
    {
        path: '/notice/:noticeId',
        name: 'noticepage',
        component: noticedetails,
    },
    {
        path: '/announcement',
        name: 'annoucementpage',
        component: annoucementpage,
    }
];

const router = createRouter({
    history: createWebHistory(),
    routes: routes,
});

export default router;
