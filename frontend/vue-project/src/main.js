import { createApp } from 'vue';
import { createPinia } from 'pinia';
import piniaPluginPersistedState from 'pinia-plugin-persistedstate';
import axios from 'axios';
import App from './App.vue';
import router from './router/index.js';


// 全局配置 Axios
axios.defaults.withCredentials = true; // 启用跨域携带 Cookie


// 创建应用实例
const app = createApp(App);
const pinia=createPinia()
pinia.use(piniaPluginPersistedState);

app.use(pinia)
app.use(router)
app.mount('#app');