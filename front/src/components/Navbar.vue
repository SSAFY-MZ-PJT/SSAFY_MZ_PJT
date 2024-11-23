<!-- navbar -->

<template>
    <!-- 회원용 네비게이션 -->
    <nav class="navbar navbar-expand-lg navbar-light bg-white" v-if="authStore.isAuthenticated">
      <div class="container">
        <!-- 로고 -->
        <router-link :to="{ name: 'GuidepageView' }">
          <img src="../assets/Navbaricons/Logo.png" alt="Logo" width="120" class="d-inline-block align-text-top">
        </router-link>
        <!-- 햄버거 버튼 -->
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <!-- 회원용 메뉴 -->
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav ms-auto">
            <li class="nav-item">
              <router-link class="nav-link" :to="{ name: 'MainView' }">Watch</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" :to="{ name: 'BoardView' }">Reviews</router-link>
            </li>
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                <img src="../assets/Navbaricons/user.png" alt="User" width="30" height="30"> User
              </a>
              <ul class="dropdown-menu">
                <li class="dropdown-item">
                  <router-link class="nav-link" :to="{ name: 'ProfileMeView'}">Profile</router-link>
                </li>
                <li class="dropdown-item">
                  <router-link class="nav-link" :to="{ name: 'UserupdateView' }">Update</router-link>
                </li>
                <li><hr class="dropdown-divider"></li>
                <li class="dropdown-item">
                  <a href="#" class="nav-link" @click="authStore.logout">Logout</a>
                </li>
              </ul>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  
    <!-- 비회원용 네비게이션 -->
    <nav class="navbar navbar-expand-lg navbar-light bg-white" v-else>
      <div class="container">
        <!-- 로고 -->
        <router-link :to="{ name: 'GuidepageView' }">
          <img src="../assets/Navbaricons/Logo.png" alt="Logo" width="120" class="d-inline-block align-text-top">
        </router-link>
        <!-- 햄버거 버튼 -->
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <!-- 비회원용 메뉴 -->
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav ms-auto">
            <li class="nav-item">
              <router-link class="nav-link" :to="{ name: 'LogInView' }">로그인</router-link>
            </li>
            <li class="nav-item">
              <router-link class="nav-link" :to="{ name: 'SignUpView' }">회원가입</router-link>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </template>
  
  <script setup>
  import { useAuthStore } from '@/stores/auth'; // 올바른 경로 확인
  const authStore = useAuthStore();
  // consloe.log(authStore.username)
  </script>

<style scoped>
/* nav */
.nav-link {
    margin-right: 15px; /* 네비게이션 링크 간격 */
    font-weight: bold; /* 글자 굵게 */
    color: #6c757d; /* 기본 글자색 회색 */
    transition: color 0.3s ease, font-size 0.3s ease; /* 부드러운 전환 효과 */
}

.nav-link:hover {
    color: #084e0d; /* 마우스를 올렸을 때 색상 */
}

.nav-link:hover {
    color: #084e0d; /* 마우스를 올렸을 때 색상 변경 */
    transform: scale(1.1); /* 마우스를 올렸을 때 글자 확대 */
}

.navbar .btn {
    margin-left: 10px; /* 버튼과 링크 간격 */
    font-weight: bold; /* 버튼 글자도 굵게 */
    background-color: #084e0d; /* 버튼 배경색 */
    color: #ffffff; /* 버튼 글자색 */
    border-radius: 20px; /* 둥근 버튼 스타일 */
    padding: 5px 15px; /* 버튼 내부 여백 */
    transition: background-color 0.3s ease, transform 0.3s ease;
}

.navbar .btn:hover {
    background-color: #063808; /* 버튼 호버 시 배경색 */
    transform: scale(1.05); /* 버튼 호버 시 약간 커짐 */
}

.navbar {
    background-color: #ffffff !important; /* 하얀색 배경 설정 */
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* 가벼운 그림자 효과 */
}

/* 드롭다운 포커스 및 활성화 상태 커스텀 */
.dropdown-menu .dropdown-item:focus, 
.dropdown-menu .dropdown-item:hover, 
.dropdown-menu .dropdown-item.active {
    background-color: #084e0d15; /* 커스텀 배경색 */
    color: #ffffff; /* 커스텀 텍스트 색상 */
    outline: none; /* 기본 아웃라인 제거 */
    box-shadow: none; /* 기본 그림자 제거 */
}
</style>