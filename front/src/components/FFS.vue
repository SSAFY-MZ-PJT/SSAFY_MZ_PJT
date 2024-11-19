<template>
    <div class="container mt-5">
        <div class="row">
            <!-- Followers -->
            <div class="col-md-6">
            <h3 class="fw-bold">followers</h3>
            <ul class="list-unstyled mt-4">
                <li class="d-flex align-items-center mb-3">
                <img src="../icons/user.png" alt="Profile Picture" class="rounded-circle me-3" width="50">
                <div>
                    <h6 class="mb-0 fw-bold">Jung</h6>
                    <small class="text-muted">삶은 계란이다.</small>
                </div>
                </li>
                <li class="d-flex align-items-center mb-3">
                <img src="../icons/user.png" alt="Profile Picture" class="rounded-circle me-3" width="50">
                <div>
                    <h6 class="mb-0 fw-bold">송후엽</h6>
                    <small class="text-muted">삶은 계란이다....그렇다.. 삶은 계란...</small>
                </div>
                </li>
                <!-- 추가 항목은 동일한 형식으로 추가 -->
            </ul>
            </div>
        
            <!-- Following -->
            <div class="col-md-6">
            <h3 class="fw-bold">following</h3>
            <ul class="list-unstyled mt-4">
                <li class="d-flex align-items-center justify-content-between mb-3">
                <div class="d-flex align-items-center">
                    <img src="../icons/user.png" alt="Profile Picture" class="rounded-circle me-3" width="50">
                    <div>
                    <h6 class="mb-0 fw-bold">jung</h6>
                    <small class="text-muted">삶은 계란이다.</small>
                    </div>
                </div>
                <button class="btn btn-success btn-sm">following</button>
                </li>
                <li class="d-flex align-items-center justify-content-between mb-3">
                <div class="d-flex align-items-center">
                    <img src="../icons/user.png" alt="Profile Picture" class="rounded-circle me-3" width="50">
                    <div>
                    <h6 class="mb-0 fw-bold">kinf</h6>
                    <small class="text-muted">cineruimyn</small>
                    </div>
                </div>
                <button class="btn btn-outline-success btn-sm">follow</button>
                </li>
                <!-- 추가 항목은 동일한 형식으로 추가 -->
            </ul>
            </div>
        </div>
    </div>
</template>

<script setup>

</script>

<style scoped>
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
  

</style>