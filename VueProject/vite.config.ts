import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import vueJsx from '@vitejs/plugin-vue-jsx'

// https://vitejs.dev/config/
export default defineConfig({
    plugins: [
        vue(),
        vueJsx(),
    ],
    server: {
        host: "192.168.1.6",
        port: 3000,
        proxy: {
            "/backend": {
                target: "http://localhost:8000",
                changeOrigin: true,
                rewrite: (path) => path.replace(/^\/backend/, ''),
            }
        }
    },
    resolve: {
        alias: {
            '@': fileURLToPath(new URL('./src', import.meta.url))
        }
    }
})
