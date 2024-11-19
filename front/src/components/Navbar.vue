<template>

<!-- 조건문으로 로그인 안한 유저면 다르게 보여줘야함. -->
<nav class="navbar navbar-expand-lg navbar-light bg-white">
    <div class="container">
        <!-- 로고 -->
        <a class="" href="#">
        <img src="../assets/Navbaricons/Logo.png" alt="Logo" width="120" class="d-inline-block align-text-top">
        </a>
        <!-- 햄버거 버튼 -->
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
        </button>
        <!-- 드롭다운 메뉴 -->
        <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav ms-auto">
            
            <li class="nav-item">
            <a class="nav-link" href="#">Watch</a>
            </li>
            <li class="nav-item">
            <a class="nav-link" href="#">Community</a>
            </li>
            <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="/profile" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                <img src="../assets/Navbaricons/user.png" alt="User" width="30" height="30">
                User
            </a>
            <ul class="dropdown-menu">
                <li class="dropdown-item">
                    <a class="nav-link" href="/profile">Profile</a>
                </li>
                <li class="dropdown-item">
                    <a class="nav-link" href="/userupdate">Upate</a>
                </li>
                <li><hr class="dropdown-divider"></li>
                <li class="dropdown-item">
                    <a class="nav-link" href="/profileother">Logout</a>
                </li>
            </ul>
            </li>
        </ul>
        </div>
    </div>
</nav>
   
</template>

<script setup>

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