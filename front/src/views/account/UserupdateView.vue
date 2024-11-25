<template>
  <div class="container mt-5">
    <h2 class="text-center mb-4">프로필 수정</h2>

    <!-- 프로필 이미지 -->
    <div class="text-center mb-4">
      <div class="profile-img-container">
        <img
          :src="formData.profileImageUrl || defaultProfileImage"
          alt="Profile"
          class="rounded-circle profile-img"
        />
      </div>
      <div>
        <label for="profileImage" class="btn custom-button mt-3">
          새로운 사진 업로드
        </label>
        <input
          type="file"
          id="profileImage"
          class="d-none"
          @change="onFileChange"
        />
      </div>
    </div>

    <!-- 회원정보 수정 폼 -->
    <form @submit.prevent="updateProfile">
      <h4 class="mb-3">기본 정보</h4>

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
      <div v-if="!passwordIsValid && formData.password" class="text-danger mb-3">
        비밀번호는 8자리 이상, 특수문자, 숫자를 포함해야 합니다.
      </div>

      <!-- Confirm Password -->
      <div class="row mb-3">
        <div class="col-md-12">
          <label for="confirmPassword" class="form-label">비밀번호 확인</label>
          <input
            type="password"
            id="confirmPassword"
            class="form-control"
            v-model="confirmPassword"
            placeholder="비밀번호를 다시 입력하세요"
            required
          />
        </div>
      </div>
      <div v-if="passwordMismatch" class="text-danger mb-3">
        비밀번호가 일치하지 않습니다.
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
              <option value="daum.net">daum.net</option>
              <option value="gmail.com">gmail.com</option>
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

      <!-- 한줄소개 -->
      <div class="row mb-3">
        <div class="col-md-12">
          <label for="introduction" class="form-label">한줄 소개</label>
          <textarea
            id="introduction"
            class="form-control"
            v-model="formData.introduction"
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
                :style="{
                  backgroundColor: genres.find(g => g.name === genre)?.color,
                  color: genres.find(g => g.name === genre)?.textColor
                }"
                @click="toggleGenre(genre)"
              >
                {{ genre }}
              </span>
            </div>
          </div>
        </div>
        </div>

      <!-- 버튼 -->
      <div class="text-center">
        <button type="button" class="btn custom-button me-3" @click="resetForm">
          취소
        </button>
        <button type="submit" class="btn custom-button" :disabled="!isFormValid">
          저장
        </button>
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref, reactive, computed, watch } from "vue";

// 폼 데이터
const formData = reactive({
  username: "",
  email: "",
  introduction: "",
  password: "",
  selectedGenres: [],
  profileImage: null,
  profileImageUrl: null,
});

const defaultProfileImage = "/src/assets/Reviewicons/user.png";

// 장르 데이터
const genres = [
  { id: 1, name: "액션", color: "#FFB3BA", textColor: "#8B0000" },
  { id: 2, name: "모험", color: "#FFDFBA", textColor: "#A84300" },
  { id: 3, name: "애니메이션", color: "#FFFFBA", textColor: "#8B8B00" },
  { id: 4, name: "코미디", color: "#BAFFC9", textColor: "#004C16" },
  { id: 5, name: "범죄", color: "#BAE1FF", textColor: "#003B6F" },
  { id: 6, name: "다큐멘터리", color: "#D5AAFF", textColor: "#350062" },
  { id: 7, name: "드라마", color: "#FFCCF9", textColor: "#8B003A" },
  { id: 8, name: "가족", color: "#F3FFE3", textColor: "#344C00" },
  { id: 9, name: "판타지", color: "#FFDEFA", textColor: "#7A3973" },
  { id: 10, name: "역사", color: "#E0BBE4", textColor: "#3C004C" },
  { id: 11, name: "공포", color: "#FFABAB", textColor: "#600000" },
  { id: 12, name: "음악", color: "#B2F4FF", textColor: "#004254" },
  { id: 13, name: "미스터리", color: "#D3F8E2", textColor: "#004025" },
  { id: 14, name: "로맨스", color: "#FFB7CE", textColor: "#72122E" },
  { id: 15, name: "SF", color: "#D4F1F4", textColor: "#00383F" },
  { id: 16, name: "TV 영화", color: "#FBE4FF", textColor: "#5D0074" },
  { id: 17, name: "스릴러", color: "#F8D4E4", textColor: "#3B0E22" },
  { id: 18, name: "전쟁", color: "#D5D8DC", textColor: "#303030" },
  { id: 19, name: "서부", color: "#F5E6CC", textColor: "#5C401F" },
];


// 랜덤 파스텔 색상 생성
const generatePastelColor = () => {
  const r = Math.floor((Math.random() * 127) + 127);
  const g = Math.floor((Math.random() * 127) + 127);
  const b = Math.floor((Math.random() * 127) + 127);
  return `rgb(${r}, ${g}, ${b})`;
};

// 장르별 색상 저장
const genreColors = reactive({});

const toggleGenre = (genre) => {
  const index = formData.selectedGenres.indexOf(genre);
  if (index === -1) {
    formData.selectedGenres.push(genre);
    if (!genreColors[genre]) {
      genreColors[genre] = generatePastelColor();
    }
  } else {
    formData.selectedGenres.splice(index, 1);
    delete genreColors[genre];
  }
};

const isFormValid = computed(() => {
  return formData.username && formData.email && formData.selectedGenres.length >= 2;
});

const passwordIsValid = computed(() => {
  const regex = /^(?=.*\d)(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,}$/;
  return regex.test(formData.password);
});

const passwordMismatch = computed(() => formData.password !== confirmPassword.value);

const confirmPassword = ref("");

const resetForm = () => {
  formData.username = "";
  formData.email = "";
  formData.password = "";
  formData.introduction = "";
  formData.selectedGenres = [];
  Object.keys(genreColors).forEach((key) => delete genreColors[key]);
};
</script>

<style scoped>
.container {
  max-width: 700px;
  margin: auto;
}

.profile-img-container {
  width: 150px;
  height: 150px;
  border-radius: 50%;
  overflow: hidden;
  border: 3px solid #ddd;
  display: inline-block;
}

.profile-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
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
  border-radius: 10px;
  padding: 4px 10px;
  font-size: 0.8rem;
  margin-bottom: 7px;
  cursor: pointer; /* 클릭 가능하다는 표시 */
  transition: background-color 0.3s ease;
}

</style>
