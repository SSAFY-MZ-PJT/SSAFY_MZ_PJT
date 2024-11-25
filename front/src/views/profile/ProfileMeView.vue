<!-- views/profile/ProfileMeView.vue -->

<template>
  <div class="pt-5 mx-4">
    <!-- 프로필 섹션 -->
    <div class="pt-5">
      <div class="container mt-5 justify-content-center">
        <!-- 프로필 헤더 -->
        <div class="row mb-4">
          <!-- 왼쪽: 프로필 이미지 -->
          <div class="col-md-6 d-flex align-items-center">
            <img :src="profile.profile_image || defaultProfileImage" alt="Profile Picture" class="rounded-circle me-5" width="120" />
            <div>
              <h2 class="fw-bold">{{ profile.username }}</h2>
              <p class="text-muted">{{ profile.introduction || "No introduction provided." }}</p>
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

    <hr class="responsive-hr mb-5 mt-5">

    <!-- 팔로워/팔로잉 목록 -->
    <div v-if="viewMode !== 'default'" class="mt-5">
      <h3>{{ viewMode === 'followers' ? 'Followers' : 'Following' }}</h3>
      <ul v-if="followersFollowingList.length > 0" class="list-group">
        <li v-for="user in followersFollowingList" :key="user.id" class="list-group-item d-flex align-items-center">
          <img :src="user.profile_image || defaultProfileImage" alt="User Picture" class="rounded-circle me-3" width="50" />
          <p class="mb-0">{{ user.username }}</p>
        </li>
      </ul>
      <p v-else>No {{ viewMode === 'followers' ? 'followers' : 'following' }} found.</p>
    </div>

    
    <!-- 기본 뷰 -->
    <div class="container" v-else>
    
      <!-- 토론 섹션 -->
      <h1 class="text-center fw-bold mb-3">Discussion</h1>
      <!-- New Discussion Button -->
      <div class="button-container mb-5 d-flex justify-content-center">
        <button class="btn" @click="showCharacterSelection">새로운 토론 생성</button>
      </div>

      <!-- Character Selection -->
      <CharacterSelection
        v-if="isCharacterSelectionVisible"
        @characterSelected="handleCharacterSelected"
      />
      
      <!-- 좋아요한 영화 -->
      <div class="mt-5">
        <h3>Liked Movies</h3>
        <hr class=" mb-5 mt-5">

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
        <hr class=" mb-5 mt-5">
        <div v-if="profile.reviews.length > 0" class="container mt-4">
          <div class="row">
            <div v-for="review in profile.reviews" :key="review.id" class="col-md-3 mb-4">
              <div class="card h-100">
                <!-- 카드 헤더 -->
                <div class="card-header d-flex align-items-center">
                  <div>
                    <h6 class="mb-0 fw-bold">{{ profile.username }}</h6>
                    <small class="text-muted">Created At: {{ formatDate(review.created_at) }}</small>
                  </div>
                </div>
                <!-- 카드 본문 -->
                <div class="card-body">
                  <img :src="review.movie.poster_url || '@/assets/Reviewicons/default-movie.png'" alt="Movie Poster" class="card-img-top mb-3">
                  <h5 class="fw-bold">{{ review.title }}</h5>
                  <div class="d-flex align-items-center">
                    <img src="@/assets/Reviewicons/star.png" alt="star" width="20" class="me-2">
                    <p class="mb-0">Rating: {{ review.rating }}/5</p>
                  </div>
                  <div class="mt-3 d-flex">
                    <img src="@/assets/Reviewicons/수정아이콘.png" alt="edit" width="20" class="me-2" @click="editReview(review.id)">
                    <img src="@/assets/Reviewicons/삭제아이콘.png" alt="delete" width="20" @click="deleteReview(review.id)">
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <p v-else>No reviews written.</p>
      </div>
    </div>
  </div>
</template>


<script setup>
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";
import axios from "axios";
import CharacterSelection from "@/components/CharacterSelection.vue";

import defaultProfileImage from '@/assets/Navbaricons/user.png';

const router = useRouter(); // Vue Router 사용

// 캐릭터 선택 UI 표시 여부 상태
const isCharacterSelectionVisible = ref(false);

// 캐릭터 선택 UI 표시 함수
const showCharacterSelection = () => {
  isCharacterSelectionVisible.value = true;
};

// 캐릭터 선택 후 처리
const handleCharacterSelected = (character) => {
  console.log("Character selected:", character);

  console.log("Navigating with params:", {
  characterName: character.name,
  characterPersonality: character.personality,
});

  // TalkAiView로 이동 (백엔드 요청 없이 이동)
  router.push({
  name: "TalkAiView",
  params: {
    characterName: character.name,
    characterPersonality: character.personality,
  },
});
};

// 상태 관리
const viewMode = ref('default'); // 기본 viewMode 설정
const myName = ref("")
const profile = ref({
  username: "",
  profile_image: "",
  introduction: "",
  reviews: [],
  liked_movies: [],
  followers: [],
  followings: []
});
const followersFollowingList = ref([]);

// 포스터가 없는 경우 기본 포스터 경로
const defaultPosterUrl = '@/assets/Reviewicons/default-movie.png';

// 프로필 데이터 로드 함수
const fetchProfile = async () => {
  try {
    const response = await axios.get("http://localhost:8000/accounts/me/", {
      headers: { Authorization: `Token ${localStorage.getItem("accessToken")}` },
    });
    profile.value = response.data;
    myName.value = profile.value.username
    console.log(profile.value.followings)

    // 리뷰 데이터에 영화 포스터 추가
    profile.value.reviews = profile.value.reviews.map((review) => ({
      ...review,
      movie: { ...review.movie, poster_url: review.movie?.poster_url || defaultPosterUrl },
    }));
  } catch (error) {
    console.error("Error fetching profile data:", error);
  }
};

// followers 또는 followings 데이터 로드 함수
const fetchFollowersFollowing = async (type) => {
  try {
    // 올바른 API 경로로 요청
    const response = await axios.get(`http://localhost:8000/accounts/${myName.value}/follow/`, {
      headers: { Authorization: `Token ${localStorage.getItem("accessToken")}` },
    });

    // API 응답에서 followers 또는 followings 데이터 필터링
    followersFollowingList.value = response.data[type] || []; // 데이터 없으면 빈 배열로 대체
    console.log(`Fetched ${type}:`, followersFollowingList.value); // 디버깅 로그
  } catch (error) {
    console.error(`Error fetching ${type} list:`, error);
    followersFollowingList.value = [];
    alert(`Failed to load ${type} list.`);
  }
};

// 팔로워/팔로잉 보기 설정 함수
const showFollowersFollowing = (mode) => {
  viewMode.value = mode; // 'followers' 또는 'following'으로 전환
  fetchFollowersFollowing(mode); // 데이터 로드
};


// 포스트 보기 설정
const showPosts = () => {
  viewMode.value = 'default';
};

// 날짜 포맷 함수
const formatDate = (isoDate) => new Date(isoDate).toISOString().split("T")[0];

// 컴포넌트 마운트 시 데이터 로드
onMounted(() => fetchProfile());
</script>


    
<style scoped>
/* 클릭 가능한 텍스트 스타일 */
a.text-decoration-none.text-dark {
  cursor: pointer; /* 마우스를 가져가면 클릭 가능 표시 */
  transition: transform 0.5s ease, color 0.5s ease; /* 부드러운 전환 효과 */
}

a.text-decoration-none.text-dark:hover {
  font-size: 1.2rem !important; /* 글씨 크기 확대 */
  color: #084e0d; /* 색상 변경 */
}


.profile-header img {
border: 3px solid #ddd;
padding: 5px;
}

.card-header {
font-weight: bold;
}

/* 그 페이지 넘기는거 */
  /* 페이지 이동 기본 스타일 */
  .pagination .page-link {
    color: #254E01; /* 페이지 링크 기본 색상 */
    transition: background-color 0.3s ease, color 0.3s ease; /* 부드러운 전환 효과 */
  }

  /* 포커스 및 클릭 상태 수정 */
  .pagination .page-link:focus,
  .pagination .page-link:active {
    outline: none; /* 포커스 테두리 제거 */
    box-shadow: none; /* 기본 그림자 제거 */
    background-color: #ffffff; /* 클릭 시 배경색 회색 대신 연한 초록색 */
    color: #254E01; /* 클릭 시 글자색 초록색 */
    font-weight: bold;
  }

  /* 호버 상태 */
  .pagination .page-link:hover {
    background-color: #254E01; /* 호버 시 배경색 */
    color: #ffffff; /* 호버 시 텍스트 색상 */
  }

  /* 활성화된 페이지 */
  .pagination .page-item.active .page-link {
    background-color: #254E01; /* 활성 페이지 배경색 */
    color: #ffffff; /* 활성 페이지 텍스트 색상 */
    border: none; /* 테두리 제거 */
  }


/* 리뷰, 토론 카드 컴포 */
.card {
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* 부드러운 그림자 효과 */
    overflow: hidden; /* 내용이 카드 영역을 넘지 않도록 */
  }
  
  .card-img-top {
    object-fit: cover; /* 이미지를 카드 영역에 맞게 조정 */
  }
  
  
  .card-title {
    font-weight: bold; /* 제목 굵게 */
    color: #084e0d; /* 제목 색상 */
  }
  

  /* 카드 이미지 둥글게 깎이는 것 방지 */
.no-rounded {
    border-top-left-radius: 0 !important; /* 좌상단 둥근 모서리 제거 */
    border-top-right-radius: 0 !important; /* 우상단 둥근 모서리 제거 */
  }

.card-header {
    background-color: rgb(255, 255, 255) !important;
}


/* 최신순, 평점순 */
.custom-nav {
    font-size: 1rem; /* 글씨 크기 */
  }
  
  /* 링크 스타일 */
  .custom-link {
    color: #084e0d !important; /* 기본 링크 색상 */
    transition: color 0.3s ease; /* 색상 전환 효과 */
  }
  
  .custom-link:hover {
    color: #5f9c63 !important; /* 호버 시 링크 색상 */
  }
  
  /* 구분자 스타일 */
  .custom-nav .text-muted {
    font-size: 1.2rem; /* 구분자 크기 */
    color: #6c757d; /* 구분자 색상 */
  }
  

/* 구분선 */
.responsive-hr {
    border: 0; /* 기본 테두리 제거 */
    border-top: 2px solid #969696; /* 위쪽 선으로 구분선 설정 */
    margin: 10px auto; /* 수직 여백 및 중앙 정렬 */
    width: 80%; /* 기본 너비 */
    transition: width 0.3s ease; /* 너비 전환 효과 */
  }
  
  /* 반응형 너비 조정 */
  @media (max-width: 1200px) {
    .responsive-hr {
      width: 60%; /* 큰 화면에서 더 작은 너비 */
    }
  }
  
  @media (max-width: 992px) {
    .responsive-hr {
      width: 60%; /* 중간 화면에서 너비 감소 */
    }
  }
  
  @media (max-width: 768px) {
    .responsive-hr {
      width: 50%; /* 작은 화면에서 너비 감소 */
    }
  }
  
  @media (max-width: 576px) {
    .responsive-hr {
      width: 50%; /* 가장 작은 화면에서 너비 감소 */
    }
  }


button {
  background-color: #ffffff;
  color: #254E01 !important; /* 버튼 글자 색상 */
  border: 1px solid #254E01 !important; /* 테두리 색상 */
  transition: all 0.3s ease;
}

button:hover {
  background-color: #254E01 !important;
  color: #ffffff !important;
  border-color: #254E01 !important;
  transform: scale(1.05);
}

  
</style>