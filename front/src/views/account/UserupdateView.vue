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

      <!-- 한줄소개 -->
      <div class="row mb-3">
        <div class="col-md-12">
          <label for="aboutMe" class="form-label">한줄 소개</label>
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
          <label for="genres" class="form-label">선호 장르</label>
          <div class="d-flex flex-wrap">
            <button
              v-for="genre in genres"
              :key="genre.id"
              type="button"
              class="btn custom-button me-2 mb-2"
              @click="addGenre(genre.name)"
              :disabled="formData.selectedGenres.includes(genre.name)"
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
              >
                {{ genre }}
                <button
                  type="button"
                  class="btn-close btn-close-white ms-2"
                  aria-label="Remove"
                  @click="removeGenre(genre)"
                ></button>
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
        <button type="submit" class="btn custom-button">
          저장
        </button>
      </div>
    </form>
  </div>
</template>

<script>
import { reactive } from "vue";

export default {
  name: "UserupdateView",
  setup() {
    const formData = reactive({
      username: "",
      email: "",
      aboutMe: "",
      selectedGenres: [],
      profileImage: null,
      profileImageUrl: null,
    });

    const defaultProfileImage =
      "/src/assets/Reviewicons/user.png"; // 기본 이미지 경로를 설정

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

    const addGenre = (genre) => {
      if (!formData.selectedGenres.includes(genre)) {
        formData.selectedGenres.push(genre);
      }
    };

    const removeGenre = (genre) => {
      formData.selectedGenres = formData.selectedGenres.filter(
        (g) => g !== genre
      );
    };

    const onFileChange = (event) => {
      const file = event.target.files[0];
      if (file) {
        formData.profileImage = file;
        formData.profileImageUrl = URL.createObjectURL(file);
      }
    };

    const updateProfile = () => {
      alert("프로필이 성공적으로 업데이트되었습니다!");
      console.log(formData);
    };

    const resetForm = () => {
      formData.username = "";
      formData.email = "";
      formData.aboutMe = "";
      formData.selectedGenres = [];
      formData.profileImage = null;
      formData.profileImageUrl = null;
    };

    return {
      formData,
      defaultProfileImage,
      genres,
      addGenre,
      removeGenre,
      onFileChange,
      updateProfile,
      resetForm,
    };
  },
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

/* 버튼 스타일 */
button {
  background-color: #ffffff;
  color: #254E01 !important;
  border: 2px solid #254E01 !important;
  transition: all 0.3s ease;
}

button:hover {
  background-color: #254E01 !important;
  color: #ffffff !important;
  border-color: #254E01 !important;
}

/* 선택된 장르 배지 스타일 */
.selected-genre-badge {
  display: inline-flex;
  align-items: center;
  background-color: #71994C;
  color: #ffffff;
  border-radius: 10px;
  padding: 4px 10px;
  font-size: 0.8rem;
  margin-bottom: 7px;
  transition: background-color 0.3s ease, transform 0.3s ease;
}

.selected-genre-badge .btn-close {
  margin-left: 10px;
  color: #ffffff;
}

.selected-genre-badge:hover {
  background-color: #1f3e01;
  transform: scale(1.05);
}

.custom-button {
  background-color: #ffffff;
  color: #254E01 !important;
  border: 1px solid #254E01 !important;
  transition: all 0.3s ease;
}

.custom-button :hover {
  background-color: #254E01 !important;
  color: #ffffff !important;
  border-color: #254E01 !important;
}
</style>
