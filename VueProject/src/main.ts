// import './assets/main.css'

import { createApp, onMounted } from 'vue';
import App from '@/App.vue';
import router from './router'
import { createPinia } from 'pinia';

const app = createApp(App);

app.use(router);
app.use(createPinia());
app.mount('#app');

let fromStep1 = false;

router.beforeEach((to, from, next) => {
    if (to.matched.some(record => record.meta.requiresStep1)) {
        if (from.name === 'Step1Register' || fromStep1) {
            fromStep1 = true;
            next();
        } else {
            next('/register/step1');
        }
    } else {
        next();
    }
});