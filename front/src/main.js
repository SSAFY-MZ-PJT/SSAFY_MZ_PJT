import { createApp } from 'vue';
import { createPinia } from 'pinia';
import piniaPluginPersistedState from 'pinia-plugin-persistedstate'; // 플러그인 추가
import "bootstrap-icons/font/bootstrap-icons.css";

import App from './App.vue';
import router from './router';

const app = createApp(App);

const pinia = createPinia();
pinia.use(piniaPluginPersistedState); // 플러그인 적용

app.use(pinia);
app.use(router);

app.mount('#app');
