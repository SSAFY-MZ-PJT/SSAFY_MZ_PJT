<!-- src/views/account/EmailVerificationView.vue -->

<template>
    <div class="flex min-h-[50vh] items-center justify-center bg-gray-50 py-8 px-4">
      <div class="w-full max-w-sm">
        <div class="bg-white px-6 py-5 shadow-sm rounded-lg">
          <!-- 로딩 상태 -->
          <div v-if="isLoading" class="text-center">
            <div class="mx-auto h-8 w-8 animate-spin rounded-full border-2 border-gray-200 border-t-blue-500"></div>
            <h2 class="mt-3 text-lg font-semibold text-gray-900">
              이메일 인증 진행 중...
            </h2>
            <p class="mt-1 text-sm text-gray-500">
              잠시만 기다려주세요.
            </p>
          </div>
  
          <!-- 성공 상태 -->
          <div v-else-if="verificationStatus === 'success'" class="text-center">
            <h2 class="mt-3 text-lg font-semibold text-gray-900">
              인증 완료!
            </h2>
            <p class="mt-1 text-sm text-gray-500">
              이메일 인증이 성공적으로 완료되었습니다.
              <br/>
              <span class="text-xs text-gray-400">3초 후 로그인 페이지로 이동합니다...</span>
            </p>
          </div>
  
          <!-- 에러 상태 -->
          <div v-else class="text-center">
            <h2 class="mt-3 text-lg font-semibold text-gray-900">
              인증 실패
            </h2>
            <p class="mt-1 text-sm text-red-500">
              {{ errorMessage }}
            </p>
            <button
              @click="router.push({ name: 'LogInView' })"
              class="mt-3 w-full rounded-md bg-blue-600 px-3 py-1.5 text-sm font-medium text-white hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-1"
            >
              로그인 페이지로 이동
            </button>
          </div>
        </div>
      </div>
    </div>
  </template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import axios from 'axios'

const route = useRoute()
const router = useRouter()
const isLoading = ref(true)
const verificationStatus = ref('pending')
const errorMessage = ref('')

// axios 인스턴스 생성
const api = axios.create({
  baseURL: 'http://localhost:8000',
  withCredentials: true,
  headers: {
    'Content-Type': 'application/json',
  }
})

// CSRF 토큰 추출 함수
const getCsrfToken = () => {
  return document.cookie
    .split('; ')
    .find(row => row.startsWith('csrftoken='))
    ?.split('=')[1];
};

// CSRF 토큰 요청 함수
const fetchCsrfToken = async () => {
  try {
    // CSRF 토큰을 요청 (GET 요청)
    const response = await api.get('/csrf/');
    const token = getCsrfToken();
    api.defaults.headers.common['X-CSRFToken'] = token;
    return token;
  } catch (error) {
    console.error('CSRF 토큰 얻기 실패:', error);
    throw error;
  }
};

const verifyEmail = async (key) => {
  try {
    console.log('이메일 인증 요청 데이터:', { key });

    const response = await api.post('/confirm-email/', { key });
    console.log('이메일 인증 응답 데이터:', response.data);

    if (response.status === 200 || response.status === 201) {
      verificationStatus.value = 'success';
      setTimeout(() => {
        router.push({ name: 'LogInView' });
      }, 3000);
    }
  } catch (error) {
    console.error('이메일 인증 실패:', error);
    verificationStatus.value = 'error';
    errorMessage.value = error.response?.data?.message || '이메일 인증에 실패했습니다.';
  } finally {
    isLoading.value = false;
  }
};



onMounted(async () => {
  const key = route.query.key
  if (key) {
    await verifyEmail(key)
  } else {
    verificationStatus.value = 'error'
    errorMessage.value = '유효하지 않은 인증 링크입니다.'
    isLoading.value = false
  }
})
</script>


<style scoped>
.animate-spin {
  animation: spin 1s linear infinite;
}

@keyframes spin {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}
</style>