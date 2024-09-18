import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueJsx from '@vitejs/plugin-vue-jsx'
import os from 'node:os'; // 引入 os 模块


// 获取本地网络接口中的私有 IP 地址
function getLocalIPAddress(): string {
    const nets = os.networkInterfaces();
    for (const name of Object.keys(nets)) {
        const netInterfaces = nets[name];
        if (netInterfaces) {
            for (const net of netInterfaces) {
                // 过滤出 IPv4 地址，并且是私有地址（192.x.x.x）
                if (net.family === 'IPv4' && net.address.startsWith('192.')) {
                    return net.address;
                }
            }
        }
    }
    return 'localhost'; // 默认值
}

const currentPlatform = os.platform(); // 获取当前平台
let serverHost = getLocalIPAddress();

if (currentPlatform === 'linux') {
    serverHost = '127.0.0.1';
}


// https://vitejs.dev/config/
export default defineConfig({
    plugins: [
        vue(),
        vueJsx(),
    ],
    server: {
        host: serverHost,
        port: 3000,
        proxy: {
            "/api": {
                target: "http://127.0.0.1:8000",
                changeOrigin: true,
            }
        }
    },
    resolve: {
        alias: {
            '@': fileURLToPath(new URL('./src', import.meta.url))
        }
    },
    cacheDir: 'node_modules/.vite',
})
