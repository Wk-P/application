import { createRouter, createWebHistory } from "vue-router";
import Register from "@/pages/registerpages/registerpage.vue";
import Step1Register from "@/pages/registerpages/registerstep1.vue";
import Step2Register from "@/pages/registerpages/registerstep2.vue";
import NotFoundPage from "@/pages/404page/App.vue";

import Home1 from "@/pages/homepages/homepage.vue";
import bestpage from "@/pages/homepages/bestpage.vue";
import newpage from "@/pages/homepages/newpage.vue";
import hiqualpage from "@/pages/homepages/hiqualpage.vue";
import VIPpage from "@/pages/homepages/VIPpage.vue";
import homepage5 from "@/pages/homepages/page5.vue";
import homepage6 from "@/pages/homepages/page6.vue";

// class 总览
import classhomepage from "@/pages/classpages/prevpages/classhomepage.vue";
import prev_necklacepage from "@/pages/classpages/prevpages/necklacepage.vue";
import prev_earringspage from "@/pages/classpages/prevpages/earringspage.vue";
import prev_braceletpage from "@/pages/classpages/prevpages/braceletpage.vue";
import prev_ringpage from "@/pages/classpages/prevpages/ringpage.vue";
import prev_class_otherspage from "@/pages/classpages/prevpages/otherspage.vue";
import prev_menpage from "@/pages/classpages/prevpages/menpage.vue";
import prev_womenpage from "@/pages/classpages/prevpages/womenpage.vue";
import prev_couplepage from "@/pages/classpages/prevpages/couplepage.vue";

// class 分类单页
import necklacepage from "@/pages/classpages/classfiedpages/braceletpage.vue";
import earringspage from "@/pages/classpages/classfiedpages/earringspage.vue";
import barceletpage from "@/pages/classpages/classfiedpages/braceletpage.vue";
import ringpage from "@/pages/classpages/classfiedpages/ringpage.vue";
import otherspage from "@/pages/classpages/classfiedpages/otherspage.vue";
import menpage from "@/pages/classpages/classfiedpages/menpage.vue";
import womenpage from "@/pages/classpages/classfiedpages/womenpage.vue";
import couplepage from "@/pages/classpages/classfiedpages/couplepage.vue";


// brand 总览
import brandhomepage from "@/pages/brandpages/prevpages/brandhomepage.vue";
import prev_LVpage from "@/pages/brandpages/prevpages/LVpage.vue";
import prev_chanelpage from "@/pages/brandpages/prevpages/chanelpage.vue";
import prev_diorpage from "@/pages/brandpages/prevpages/diorpage.vue";
import prev_hermespage from "@/pages/brandpages/prevpages/hermespage.vue";
import prev_tiffanypage from "@/pages/brandpages/prevpages/tiffanypage.vue";
import prev_vancleefpage from "@/pages/brandpages/prevpages/vancleefpage.vue";
import prev_cartierpage from "@/pages/brandpages/prevpages/cartierpage.vue";
import prev_bulgalipage from "@/pages/brandpages/prevpages/bulgalipage.vue";
import prev_brand_otherspage from "@/pages/brandpages/prevpages/otherspage.vue";


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
    // 主页
    {
        path: "/",
        name: "home",
        component: Home1,
        redirect: { name: "bestpage" },
        children: [
            { path: "bestpage", name: 'bestpage', component: bestpage },
            { path: "newpage", name: 'newpage', component: newpage },
            { path: "hiqualpage", name: 'hiqualpage', component: hiqualpage },
            { path: "VIPpage", name: 'VIPpage', component: VIPpage },
            { path: "homepage5", name: 'homepage5', component: homepage5 },
            { path: "homepage6", name: 'homepage6', component: homepage6 },
        ]
    },

    // 类型总览界面
    {
        path: "/class",
        name: "class",
        component: classhomepage,
        redirect: { name: "class_necklace" },
        children: [
            { path: "class_necklace", name: 'class_necklace', component: prev_necklacepage },
            { path: "class_earrings", name: 'class_earrings', component: prev_earringspage },
            { path: "class_bracelet", name: 'class_bracelet', component: prev_braceletpage },
            { path: "class_ring", name: 'class_ring', component: prev_ringpage },
            { path: "class_others", name: 'class_others', component: prev_class_otherspage },
            { path: "class_men", name: 'class_men', component: prev_menpage },
            { path: "class_women", name: 'class_women', component: prev_womenpage },
            { path: "class_couple", name: 'class_couple', component: prev_couplepage },
            { path: "/necklace", // 项链
                name: "necklace",
                component: necklacepage,
            },
            {
                path: "/earrings", // 耳环
                name: "earrings",
                component: earringspage,
            },
            {
                path: "/bracelet", // 手镯
                name: "bracelet",
                component: barceletpage,
            },
            {
                path: "/ring",     // 戒指
                name: "ring",
                component: ringpage,
            },
            {
                path: "/others",     // 其他
                name: "others",
                component: otherspage,
            },
            {
                path: "/men",     // 男
                name: "men",
                component: menpage,
            },
            {
                path: "/women",     // 女
                name: "women",
                component: womenpage,
            },
            {
                path: "/couple",     // 情侣
                name: "couple",
                component: couplepage,
            },
        ]
    },

    // brand 总览
    {
        path: "/brand",
        name: "brand",
        component: brandhomepage,
        redirect: { name: "brand_LV" },
        children: [
            { path: "brand_LV", name: 'brand_LV', component: prev_LVpage },
            { path: "brand_chanel", name: 'brand_chanel', component: prev_chanelpage },
            { path: "brand_hermes", name: 'brand_hermes', component: prev_hermespage },
            { path: "brand_cartier", name: 'brand_cartier', component: prev_cartierpage },
            { path: "brand_tiffany", name: 'brand_tiffany', component: prev_tiffanypage },
            { path: "brand_dior", name: 'brand_dior', component: prev_diorpage },
            { path: "brand_bulgali", name: 'brand_bulgali', component: prev_bulgalipage },
            { path: "brand_vancleef", name: 'brand_vancleef', component: prev_vancleefpage },
            { path: "brand_others", name: 'brand_others', component: prev_brand_otherspage },
        ]
    },

    // 用户的喜欢
    {
        path: "/favorite",
        name: "favorite",
        component: favoritehomepage,
    },

    // 用户中心
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

    // 搜索页 （可能要删除）
    {
        path: "/search",
        name: "search",
        component: searchpage,
    },

    // 用户注册页
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

    // 错误页匹配
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


    // 商品详情页
    {
        path: '/details/:itemId/:brand/:itemTitle/:itemName',
        name: 'itemdetail',
        component: itemdetailpage,
    },


    // 用户地址及功能界面
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

    // 网站公告页
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
