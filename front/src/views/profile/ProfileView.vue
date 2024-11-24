<template>
  <div class="pt-5 mx-4">
    <!-- 프로필 섹션 -->
    <div class="pt-5">
      <div class="container mt-5 justify-content-center">
        <div class="row mb-4">
          <!-- 왼쪽: 프로필 이미지 및 정보 -->
          <div class="col-md-6 d-flex align-items-center">
            <img :src="profile.profile_image || defaultProfileImage" alt="Profile Picture" class="rounded-circle me-5" width="120" />
            <div>
              <h2 class="fw-bold">{{ profile.username }}</h2>
              <p class="text-muted">{{ profile.introduce || "No introduction provided." }}</p>
            </div>
          </div>
          <!-- 오른쪽: 작성글, 팔로워 수, 팔로잉 수 -->
          <div class="col-md-6">
            <div class="d-flex align-items-center justify-content-end h-100 border-separator">
              <div class="px-3 text-center border-end">
                <a class="text-decoration-none text-dark" @click="showPosts">
                  <p class="fw-bold fs-4">{{ profile.reviews.length }}</p>
                  <p class="text-muted">Posts</p>
                </a>
              </div>
              <div class="px-3 text-center border-start border-end">
                <a class="text-decoration-none text-dark" @click="showFollowersFollowing('followers')">
                  <p class="fw-bold fs-4">{{ profile.followers.length }}</p>
                  <p class="text-muted">Followers</p>
                </a>
              </div>
              <div class="px-3 text-center border-start">
                <a class="text-decoration-none text-dark" @click="showFollowersFollowing('following')">
                  <p class="fw-bold fs-4">{{ profile.followings.length }}</p>
                  <p class="text-muted">Following</p>
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <hr class="responsive-hr mb-5 mt-5" />

    <!-- 좋아요한 영화 -->
    <div class="mt-5">
      <h3>Liked Movies</h3>
      <div v-if="profile.liked_movies.length > 0" class="d-flex flex-wrap">
        <div v-for="movie in profile.liked_movies" :key="movie.id" class="card m-2" style="width: 18rem;">
          <img :src="movie.poster_image_url" class="card-img-top" alt="Movie Poster" />
          <div class="card-body">
            <h5 class="card-title">{{ movie.title }}</h5>
            <p class="card-text">Release Date: {{ movie.release_date }}</p>
          </div>
        </div>
      </div>
      <p v-else>No liked movies.</p>
    </div>

    <!-- 작성한 리뷰 -->
    <div class="mt-5">
      <h3>Written Reviews</h3>
      <div v-if="profile.reviews.length > 0" class="d-flex flex-wrap">
        <div v-for="review in profile.reviews" :key="review.id" class="card m-2" style="width: 18rem;">
          <div class="card-body">
            <h5 class="card-title">{{ review.title }}</h5>
            <p class="card-text">Rating: {{ review.rating }}/5</p>
            <p class="card-text"><small class="text-muted">Created At: {{ review.created_at }}</small></p>
          </div>
        </div>
      </div>
      <p v-else>No reviews written.</p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";

// 기본 프로필 이미지 경로
import defaultProfileImage from '@/assets/Navbaricons/user.png';

// 상태 관리
const profile = ref({
  username: "",
  profile_image: "",
  introduce: "",
  reviews: [],
  liked_movies: [],
  followers: [],
  followings: []
});

// 데이터 로드 함수
const fetchProfile = async () => {
  try {
    const response = await axios.get("http://localhost:8000/accounts/me/", {
      headers: {
        Authorization: `Token ${localStorage.getItem("accessToken")}`,
      },
    });
    profile.value = response.data;
  } catch (error) {
    console.error("Error fetching profile data:", error);
    alert("Failed to fetch profile data. Please try again later.");
  }
};

// 컴포넌트 마운트 시 데이터 로드
onMounted(() => {
  fetchProfile();
});
</script>