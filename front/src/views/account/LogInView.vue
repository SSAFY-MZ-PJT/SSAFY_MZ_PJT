<template>
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
    <div class="text-center mt-5">
      <p class="small">
        계정이 없으신가요? 
        <router-link to="/signup" class="signup-link">회원가입을 진행해주세요.</router-link>
      </p>
    </div>
  </div>
</template>

<script setup>
import { reactive } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();

const formData = reactive({
  email: '',
  password: '',
});

const login = async () => {
  try {
    // 여기에 실제 로그인 로직을 구현합니다.
    // 예를 들어, API 호출을 통해 서버에 로그인 요청을 보냅니다.
    console.log('로그인 시도:', formData);
    
    // 로그인 성공 시 처리
    // 예: 홈 페이지로 리다이렉트
    router.push('/');
  } catch (error) {
    console.error('로그인 실패:', error);
    alert('로그인에 실패했습니다. 이메일과 비밀번호를 확인해주세요.');
  }
};
</script>

<style scoped>
.container {
  max-width: 400px;
  margin: auto;
}

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
}

.signup-link {
  color: #254E01;
  text-decoration: none;
  font-weight: bold;
}

.signup-link:hover {
  text-decoration: underline;
}
</style>