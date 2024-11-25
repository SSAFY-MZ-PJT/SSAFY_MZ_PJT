<template>
  <div class="guide-page">
    <!-- Section 1 -->
    <header class="header">
      <div class="container text-center">
        <h1 class="logo">C:nerium</h1>
        <h2 class="main-title">영화로 시작하고, 토론으로 성장하다.</h2>
        <h3>영화는 단순히 즐기기 위해 있는 것이 아닙니다. </h3>
        <p class="sub-title">
          우리의 시야를 넓히고, 내면을 성장시키는 도구가 될 수 있습니다.
          영화와 토론을 하나의 플랫폼에서 만나보세요. 
          당신의 성장을 돕는 새로운 여정을 지금 시작하세요.
          저희 cinerium이 당신의 성장을 돕겠습니다.
        </p>
        <div class="custom-width">
          <h3>내면의 숲을 꾸며나가 보세요.</h3>
          <p class="sub-title">
            우리의 시야를 넓히고, 내면을 성장시키는 도구가 될 수 있습니다.
            영화와 토론을 하나의 플랫폼에서 만나보세요. 
            당신의 성장을 돕는 새로운 여정을 지금 시작하세요.
            저희 cinerium이 당신의 성장을 돕겠습니다.
          </p>
        </div>
      </div>
    </header>

    <main>
      <section class="content container">
        <!-- Section 2 -->
        <div class="row align-items-center my-5 topdiv">
          <div class="col-md-6">
            <img src="../assets/Guideicons/guideicons1.png" alt="Illustration 1" class="img-fluid">
          </div>
          <div class="col-md-6 text-section">
            <h5 class="small-title">Small title</h5>
            <h3>Create illustration groups perfect for your product</h3>
            <p>You can use this illustration group for your website...</p>
          </div>
        </div>

        <!-- Section 3 -->
        <div class="row align-items-center my-5 flex-row-reverse topdiv">
          <div class="col-md-6 text-end">
            <img src="../assets/Guideicons/person1.png" alt="Illustration 2" class="img-fluid" width="250">
          </div>
          <div class="col-md-6 text-section">
            <h5 class="small-title">Small title</h5>
            <h3>Create illustration groups perfect for your product</h3>
            <p>You can use this illustration group for your website...</p>
          </div>
        </div>

        <!-- Section 4 -->
        <div class="row align-items-center my-5 topdiv">
          <div class="col-md-6">
            <img src="../assets/Guideicons/person2.png" alt="Illustration 1" class="img-fluid" width="310">
          </div>
          <div class="col-md-6 text-section">
            <h5 class="small-title">Small title</h5>
            <h3>Create illustration groups perfect for your product</h3>
            <p>You can use this illustration group for your website...</p>
          </div>
        </div>

        <!-- Section 5 -->
        <div class="row align-items-center my-5 topdiv">
          <div class="col-md-6">
            <img src="../assets/Guideicons/person3.png" alt="Illustration 3" class="img-fluid" width="300">
          </div>
          <div class="col-md-6 text-section">
            <h5 class="small-title">Small title</h5>
            <h3>Create illustration groups perfect for your product</h3>
            <p>
              영화는 즐기는 것이 아니라, 함께 느끼고 성장하는 것입니다.
              Cinerium에서 영화를 다시 발견하고, 당신의 생각을 확장하세요.
            </p>
          </div>
          <div class="text-center py-5">
            <button @click="goToSignUp" class="btn btn-outline-success btn-lg">Create an account</button>
          </div>
        </div>

      </section>
    </main>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router';

const router = useRouter();

const goToSignUp = () => {
  router.push({ name: 'SignUpView' });
};

</script>

<style scoped>
/* 전체 배경 스타일 */
.guide-page {
  position: relative;
  width: 100%;
  min-height: 100vh; /* 전체 화면 높이 */
  background-image: url('../assets/Guideicons/background.png'); /* 배경 이미지 경로 */
  background-size: cover; /* 배경 이미지 크기 설정 */
  background-repeat: no-repeat; /* 배경 이미지 반복 방지 */
  background-position: center; /* 배경 위치 중앙 정렬 */
  overflow: hidden; /* 초과된 부분 숨김 */
}

/* Global Styles */
h1.logo {
  font-size: 5.5rem;
  font-weight: bold;
  color: #fff;
}

h3 {
  color: #fff;
}

p {
  padding-top: 1rem;
  line-height: 2.5;
}

/* Header Section */
.header {
  padding: 350px 20px;
  text-align: center;
}

.main-title {
  font-size: 2.5rem;
  padding-top: 1.5rem;
  padding-bottom: 3rem;
  color: #fff;
  margin-top: 10px;
  font-weight: bold;
}

.sub-title {
  font-size: 1rem;
  color: #d9f0e0;
}

/* Content Section */
.content .text-section h5 {
  font-size: 1rem;
  color: #00380C;
  font-weight: bold;
}

.content .text-section h3 {
  font-size: 1.8rem;
  margin-top: 10px;
  color: #333;
  font-weight: bold;
}

.content .text-section p {
  margin-top: 10px;
  font-size: 1rem;
  color: #555;
}

.topdiv {
  padding-bottom: 9rem;
  padding-top: 5rem;
}

.custom-width {
  width: 50%; /* 전체 화면의 50% 너비 */
  max-width: 600px; /* 최대 너비 600px */
  margin: 0 auto; /* 가운데 정렬 */
}

button {
  background-color: #ffffff;
  color: #254E01 !important; /* 버튼 글자 색상 */
  border: 2px solid #254E01 !important; /* 테두리 색상 */
  transition: all 0.3s ease;
}

button:hover {
  background-color: #254E01 !important;
  color: #ffffff !important;
  border-color: #254E01 !important;
}
</style>
