import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { createPinia } from 'pinia'
import { useAuthStore } from './store/index.js'
import './index.css'

const pinia = createPinia()
const app = createApp(App).use(router).use(pinia)

const authStore = useAuthStore()
authStore.restore()

app.mount('#app')


