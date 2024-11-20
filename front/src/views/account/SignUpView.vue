<template>
  <div class="container mt-5">
    <h2 class="text-center mb-4">회원가입</h2>

    <form @submit.prevent="registerUser">
      <!-- Username -->
      <div class="row mb-3">
        <div class="col-md-12">
          <label for="username" class="form-label">사용자 이름</label>
          <input
            type="text"
            id="username"
            class="form-control"
            v-model="formData.username"
            placeholder="사용자 이름을 입력하세요"
            required
          />
        </div>
      </div>

      <!-- Email -->
      <div class="row mb-3">
      <div class="col-md-12">
        <label for="email" class="form-label">이메일</label>
        <div class="input-group">
          <input
            type="text"
            id="emailId"
            class="form-control"
            v-model="emailId"
            placeholder="이메일 아이디"
            required
          />
          <span class="input-group-text">@</span>
          <select
            class="form-select"
            v-model="selectedDomain"
            @change="updateEmailDomain"
          >
            <option value="">직접 입력</option>
            <option value="naver.com">naver.com</option>
            <option value="gmail.com">gmail.com</option>
            <option value="kakao.com">kakao.com</option>
            <option value="daum.net">daum.net</option>
            <option value="nate.com">nate.com</option>
          </select>
        </div>
      </div>
    </div>
    <div class="row mb-3" v-if="selectedDomain === ''">
      <div class="col-md-12">
        <input
          type="text"
          class="form-control"
          v-model="customDomain"
          placeholder="도메인 직접 입력"
          @input="updateEmail"
        />
      </div>
    </div>

      <!-- Email Verification -->
      <div class="row mb-3" v-show="emailVerificationSent">
        <div class="col-md-12">
          <label for="emailVerification" class="form-label">이메일 인증 코드</label>
          <input
            type="text"
            id="emailVerification"
            class="form-control"
            v-model="formData.emailVerificationCode"
            placeholder="이메일로 받은 인증 코드를 입력하세요"
            required
          />
          <button type="button" class="btn custom-button mt-2" @click="verifyEmail">
            인증 확인
          </button>
        </div>
      </div>

      <!-- 한줄 소개 -->
      <div class="row mb-3">
        <div class="col-md-12">
          <label for="aboutMe" class="form-label">한줄 소개 (선택사항)</label>
          <textarea
            id="aboutMe"
            class="form-control"
            v-model="formData.aboutMe"
            placeholder="한줄 소개를 작성하세요 (최대 50자)"
            maxlength="50"
            rows="3"
          ></textarea>
        </div>
      </div>

      <!-- 장르 선택 -->
      <div class="row mb-4">
      <div class="col-md-12">
        <label for="genres" class="form-label">선호 장르 (최소 2개 이상 선택)</label>
        <div class="d-flex flex-wrap">
          <button
            v-for="genre in genres"
            :key="genre.id"
            type="button"
            class="btn custom-button me-2 mb-2"
            @click="toggleGenre(genre.name)"
            :class="{ 'selected': formData.selectedGenres.includes(genre.name) }"
          >
            {{ genre.name }}
          </button>
        </div>
        <!-- 선택된 장르 -->
        <div v-if="formData.selectedGenres.length" class="mt-3">
          <h6>선택된 장르:</h6>
          <div class="selected-genres">
            <span
              v-for="(genre, index) in formData.selectedGenres"
              :key="index"
              class="selected-genre-badge me-2"
              @click="toggleGenre(genre)"
            >
              {{ genre }}
              <button
                type="button"
                class="btn-close btn-close-white ms-2"
                aria-label="Remove"
                @click.stop="toggleGenre(genre)"
              ></button>
            </span>
          </div>
        </div>
      </div>
    </div>

      <!-- 버튼 -->
      <div class="text-center">
        <button type="submit" class="btn custom-button" :disabled="!isFormValid">
          회원가입
        </button>
      </div>
    </form>
  </div>
</template>

<script setup>
import { reactive, computed, ref, onMounted, watch } from "vue";

const formData = reactive({
  username: "",
  email: "",
  emailVerificationCode: "",
  aboutMe: "",
  selectedGenres: [],
});

const emailId = ref("");
const selectedDomain = ref("");
const customDomain = ref("");
const updateEmailDomain = () => {
  if (selectedDomain.value) {
    formData.email = `${emailId.value}@${selectedDomain.value}`;
  } else {
    formData.email = `${emailId.value}@${customDomain.value}`;
  }
};

const updateEmail = () => {
  formData.email = `${emailId.value}@${customDomain.value}`;
};

watch(emailId, updateEmailDomain);
watch(customDomain, updateEmail);

const genres = [
  { id: 28, name: "액션" },
  { id: 12, name: "모험" },
  { id: 16, name: "애니메이션" },
  { id: 35, name: "코미디" },
  { id: 80, name: "범죄" },
  { id: 99, name: "다큐멘터리" },
  { id: 18, name: "드라마" },
  { id: 10751, name: "가족" },
  { id: 14, name: "판타지" },
  { id: 36, name: "역사" },
  { id: 27, name: "공포" },
  { id: 10402, name: "음악" },
  { id: 9648, name: "미스터리" },
  { id: 10749, name: "로맨스" },
  { id: 878, name: "SF" },
  { id: 10770, name: "TV 영화" },
  { id: 53, name: "스릴러" },
  { id: 10752, name: "전쟁" },
  { id: 37, name: "서부" },
];

const toggleGenre = (genre) => {
  const index = formData.selectedGenres.indexOf(genre);
  if (index === -1) {
    formData.selectedGenres.push(genre);
  } else {
    formData.selectedGenres.splice(index, 1);
  }
};

const isFormValid = computed(() => {
  return (
    formData.username &&
    formData.email &&
    formData.email.includes('@') &&
    (!emailVerificationSent.value || formData.emailVerificationCode) &&
    formData.selectedGenres.length >= 2
  );
});

const registerUser = async () => {
  if (isFormValid.value) {
    try {
      // Django 백엔드로 회원가입 요청을 보내는 로직
      const response = await fetch('/api/register/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });

      if (response.ok) {
        alert("회원가입이 완료되었습니다!");
        // 회원가입 성공 후 처리 (예: 로그인 페이지로 리다이렉트)
      } else {
        const errorData = await response.json();
        alert(`회원가입 실패: ${errorData.message}`);
      }
    } catch (error) {
      console.error("회원가입 중 오류 발생:", error);
      alert("회원가입 중 오류가 발생했습니다. 다시 시도해주세요.");
    }
  }
};

const verifyEmail = async () => {
  try {
    // Django 백엔드로 이메일 인증 요청을 보내는 로직
    const response = await fetch('/api/verify-email/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        email: formData.email,
        verificationCode: formData.emailVerificationCode,
      }),
    });

    if (response.ok) {
      alert("이메일이 성공적으로 인증되었습니다.");
      emailVerificationSent.value = false;
    } else {
      alert("이메일 인증에 실패했습니다. 다시 시도해주세요.");
    }
  } catch (error) {
    console.error("이메일 인증 중 오류 발생:", error);
    alert("이메일 인증 중 오류가 발생했습니다. 다시 시도해주세요.");
  }
};

onMounted(() => {
  console.log('Component mounted');
});
</script>

<style scoped>
.input-group-text {
  background-color: #f8f9fa;
  border-color: #ced4da;
}

.form-select {
  border-top-left-radius: 0;
  border-bottom-left-radius: 0;
}
.container {
  max-width: 700px;
  margin: auto;
}

textarea {
  resize: none;
}

.custom-button {
  background-color: #ffffff;
  color: #254E01 !important;
  border: 1px solid #254E01 !important;
  transition: all 0.3s ease;
}

.custom-button:hover:not(:disabled) {
  background-color: #254E01 !important;
  color: #ffffff !important;
  border-color: #254E01 !important;
}

.custom-button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

.selected-genre-badge {
  display: inline-flex;
  align-items: center;
  background-color: #95b973;
  color: #ffffff;
  border-radius: 10px;
  padding: 4px 10px;
  font-size: 0.8rem;
  margin-bottom: 7px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.selected-genre-badge:hover {
  background-color: #7a9c5c;
}

.btn-close {
  font-size: 0.5rem;
  padding: 0.25rem;
}

.btn-close:focus {
  box-shadow: none;
}
</style>