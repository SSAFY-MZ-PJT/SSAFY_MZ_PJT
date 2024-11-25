// src/main.js

import { createApp } from 'vue';
import { createPinia } from 'pinia';
import { useAuthStore } from '@/stores/auth';
import piniaPluginPersistedState from 'pinia-plugin-persistedstate'; // 플러그인 추가
import "bootstrap-icons/font/bootstrap-icons.css";

import App from './App.vue';
import router from './router';

const app = createApp(App);

const pinia = createPinia();
pinia.use(piniaPluginPersistedState); // 플러그인 적용

app.use(pinia); // Pinia를 Vue 애플리케이션에 연결
app.use(router);

// Pinia를 연결한 후 authStore를 가져와 상태 복원
const authStore = useAuthStore();
authStore.restoreAuthState(); // 앱 초기화 시 인증 상태 복원

app.mount('#app');
