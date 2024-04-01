import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'
import axios from 'axios'
import './assets/main.css'
import VuePagination from "vue3-tailwind-pagination";
import "vue3-tailwind-pagination/dist/style.css";
axios.defaults.baseURL = 'http://localhost:8000'

const app = createApp(App)
app.use(createPinia())
app.use(VuePagination);
app.use(router, axios)
app.mount('#app')
