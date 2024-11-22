<!-- loginview -->
<template>
  <div>
    <DecoBox />
    <div class="container mt-5">
      <h2 class="text-center mb-4">로그인</h2>
  
      <form @submit.prevent="login">
        <!-- Email -->
        <div class="row mb-3">
          <div class="col-md-12">
            <label for="email" class="form-label">이메일</label>
            <input
              type="email"
              id="email"
              class="form-control"
              v-model="formData.email"
              placeholder="이메일 주소를 입력하세요"
              required
            />
          </div>
        </div>
  
        <!-- Password -->
        <div class="row mb-3">
          <div class="col-md-12">
            <label for="password" class="form-label">비밀번호</label>
            <input
              type="password"
              id="password"
              class="form-control"
              v-model="formData.password"
              placeholder="비밀번호를 입력하세요"
              required
            />
          </div>
        </div>
  
        <!-- 로그인 버튼 -->
        <div class="text-center">
          <button type="submit" class="btn custom-button">
            로그인
          </button>
        </div>
      </form>
  
      <!-- 회원가입 링크 -->
      <div class="text-center mt-3">
        <p class="small">
          계정이 없으신가요? 
          <router-link :to="{name:'SignUpView'}" class="signup-link">회원가입을 진행해주세요.</router-link>
        </p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { reactive } from 'vue';
import { useRouter } from 'vue-router';
import DecoBox from '@/components/DecoBox.vue';
import { useAuthStore } from '@/stores/auth';

const router = useRouter();
const authStore = useAuthStore();

const formData = reactive({
  email: '',
  password: '',
});

const login = async function () {
  try {
    await authStore.logIn({
      email: formData.email,
      password: formData.password,
    });
    router.push({ name: 'MainView' }); // 로그인 성공 시 리디렉션
  } catch {
    alert('로그인에 실패했습니다. 이메일과 비밀번호를 확인해주세요.');
  }
}
</script>

<style scoped>
.container {
  max-width: 400px;
  margin: auto;
}


/* 버튼 스타일 */
.custom-button {
  background-color: #ffffff;
  color: #254E01 !important;
  border: 1px solid #254E01 !important;
  transition: all 0.3s ease;
}

.custom-button:hover {
  background-color: #254E01 !important;
  color: #ffffff !important;
  border-color: #254E01 !important;
  transform: scale(1.05);
}


/* 링크 스타일 */
.signup-link {
  color: #254E01;
  text-decoration: none;
  font-weight: bold;
}

.signup-link:hover {
  text-decoration: underline;
}
</style>