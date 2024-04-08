import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import Lara from '@/presets/lara';
import App from './App.vue'
import router from './router'
import axios from 'axios'
import './assets/main.css'
import VuePagination from "vue3-tailwind-pagination";
import "vue3-tailwind-pagination/dist/style.css";
import '@imengyu/vue3-context-menu/lib/vue3-context-menu.css'
import ContextMenu from '@imengyu/vue3-context-menu'
import PrimeVue from 'primevue/config';
import Checkbox from 'primevue/checkbox';
axios.defaults.baseURL = 'http://localhost:8000'

const app = createApp(App)
app.use(createPinia())
app.use(VuePagination);
app.use(ContextMenu)
app.use(PrimeVue, {
    pt: Lara//apply preset
});
app.component('Checkbox', Checkbox);
app.use(router, axios)
app.mount('#app')
