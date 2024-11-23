<template>
  <div class="pt-5 mx-4"> 
    <!-- 내 프로필 -->
    <div class="pt-5">
      <div class="container mt-5 justify-content-center">
        <!-- 프로필 헤더 -->
        <div class="row mb-4">
          <!-- 왼쪽: 프로필 이미지 및 정보 -->
          <div class="col-md-6 d-flex align-items-center">
            <img src="@/assets/Navbaricons/user.png" alt="Profile Picture" class="rounded-circle me-5" width="120">
            <div>
              <h2 class="fw-bold">User Name</h2>
              <p class="text-muted">A short introduction about the user goes here.</p>
            </div>
          </div>
          <!-- 오른쪽: 작성글, 팔로워 수, 팔로잉 수 -->
          <div class="col-md-6">
            <div class="d-flex align-items-center justify-content-end h-100 border-separator">
              <div class="px-3 text-center border-end">
                <a class="text-decoration-none text-dark" @click="showPosts">
                  <p class="fw-bold fs-4">50</p>
                  <p class="text-muted">Posts</p>
                </a>
              </div>
              <div class="px-3 text-center border-start border-end">
                <a class="text-decoration-none text-dark" @click="showFollowersFollowing('followers')">
                  <p class="fw-bold fs-4">200</p>
                  <p class="text-muted">Followers</p>
                </a>
              </div>
              <div class="px-3 text-center border-start">
                <a class="text-decoration-none text-dark" @click="showFollowersFollowing('following')">
                  <p class="fw-bold fs-4">180</p>
                  <p class="text-muted">Following</p>
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    
    <hr class="responsive-hr mb-5 mt-5">
    
    <!-- FFS 컴포넌트 (팔로워/팔로잉) -->
    <FFS v-if="viewMode !== 'default'" :viewMode="viewMode" />
    
    <!-- 토론, 리뷰 섹션 -->
    <div v-if="viewMode === 'default'">
      <h1 class="text-center fw-bold mb-3">Recent Discussion</h1>
      <!-- 버튼 컨테이너 -->
      <div class="button-container mb-5 d-flex justify-content-center">
        <button class="btn">새로운 토론 생성</button>
      </div>
      <ul class="nav nav-underline justify-content-center custom-nav">
        <li class="nav-item">
          <a class="nav-link custom-link" href="#">최신순</a>
        </li>
        <li class="nav-item mx-2 text-muted">/</li>
        <li class="nav-item">
          <a class="nav-link custom-link" href="#">별점순</a>
        </li>
      </ul>

      <!-- 카드 -->
      <div class="container mt-4">
        <div class="row">
          <!-- 카드 1 -->
          <div class="col-md-3 mb-4">
            <div class="card h-100">
              <div class="card-header d-flex align-items-center">
                <!-- 프로필 이미지 -->
                <img src="@/assets/Reviewicons/user.png" alt="Profile Picture" class="rounded-circle me-3" width="35">
                <!-- 닉네임과 작성 일자 -->
                <div>
                  <h6 class="mb-0 fw-bold">User Name</h6>
                  <small class="text-muted">게시일: 2023-11-18</small>
                </div>
              </div>
              <img src="../icons/movie_p.webp" class="card-img-top no-rounded" alt="Card Image">
              <div class="card-body">
                <h5 class="fw-bold">Card Title 1</h5>
                <div class="d-flex align-items-center">
                  <img src="@/assets/Reviewicons/star.png" alt="star" width="20" class="me-2">
                  <p class="mb-0">수정 필요</p>
                </div>
                <div class="mt-3">
                  <img src="@/assets/Reviewicons/수정아이콘.png" alt="수정" width="20" class="me-2">
                  <img src="@/assets/Reviewicons/삭제아이콘.png" alt="delete" width="20">
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- 페이지 이동 바 -->
      <nav aria-label="Page navigation">
        <ul class="pagination justify-content-center">
          <!-- 이전 페이지 버튼 -->
          <li class="page-item disabled">
            <a class="page-link" href="#" aria-label="Previous">
              <span aria-hidden="true">&laquo;</span>
            </a>
          </li>
          <!-- 페이지 번호 -->
          <li class="page-item"><a class="page-link" href="#">1</a></li>
          <li class="page-item"><a class="page-link" href="#">2</a></li>
          <li class="page-item" aria-current="page">
            <a class="page-link" href="#">3</a>
          </li>
          <li class="page-item"><a class="page-link" href="#">4</a></li>
          <li class="page-item"><a class="page-link" href="#">5</a></li>
          <!-- 다음 페이지 버튼 -->
          <li class="page-item">
            <a class="page-link" href="#" aria-label="Next">
              <span aria-hidden="true">&raquo;</span>
            </a>
          </li>
        </ul>
      </nav>
    </div>
  </div>
</template>

<script setup>
import FFS from '@/components/FFS.vue'; // FFS 컴포넌트 가져오기
import { ref } from 'vue';
import { useRoute } from 'vue-router';

const route = useRoute();
const userId = route.params.userId; // URL에서 userId 추출

// viewMode 상태 관리
const viewMode = ref('default');

// 팔로워/팔로잉 보기 설정
const showFollowersFollowing = (mode) => {
  viewMode.value = mode; // 'followers' 또는 'following'으로 변경
};

// Posts 화면 전환
const showPosts = () => {
  viewMode.value = 'default'
}
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