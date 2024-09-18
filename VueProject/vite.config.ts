import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueJsx from '@vitejs/plugin-vue-jsx'
import os from 'node:os'; // 引入 os 模块

const currentPlatform = os.platform(); // 获取当前平台
const serverHost = currentPlatform === 'win32' ? '192.168.1.6' : 'localhost';

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
