<template>
  <div class="guide-page">
    <!-- Section 1 -->
    <header class="header section" ref="sections">
      <div class="container text-center">
        <h1 class="logo">C:nerium</h1>
        <h2 class="main-title">영화를 보고, 의견을 나누고, 성장하다.</h2>
        <h3>영화와 토론, 새로운 방식으로 즐기세요.</h3>
        <p class="sub-title">
          Cinerium은 영화와 토론을 함께할 수 있는 새로운 플랫폼입니다.
          영화에 대한 정보부터 다른 사람들의 리뷰, 그리고 당신만의 깊이 있는 토론까지.
          편리함과 내적 성장을 위한 여정을 지금 시작하세요.
        </p>
        <div class="custom-width">
          <h3>생각의 나무를 키워보세요.</h3>
          <p class="sub-title">
            단순히 영화를 보는 것에서 끝나지 마세요.
            Cinerium은 질문하고, 배우고, 성장할 수 있는 기회를 제공합니다.
            당신의 의견을 나누고, 새로운 시각을 얻으며 내면의 깊이를 더하세요.
          </p>
        </div>
      </div>
    </header>

    <main>
      <!-- Section 2 -->
      <section class="content container section" ref="sections">
        <div class="row align-items-center my-5 topdiv text-center">
          <div class="text-section">
            <h5 class="small-title">영화 정보를 한눈에</h5>
            <h3 style="color: #5B7C3C;">한 곳에서 영화 정보를 모두 확인하세요</h3>
            <p>
              Cinerium은 영화에 대한 정보를 간편하게 확인할 수 있는 플랫폼입니다.  
              당신이 좋아하는 영화의 리뷰와 평점을 한눈에 살펴보세요.
            </p>
          </div>
        </div>
      </section>

      <!-- Section 3 -->
      <section class="content container section" ref="sections">
        <div class="my-5 topdiv justify-content-center text-center">
          <div class="col-md-12 text-section">
            <h5 class="small-title">나만의 토론 공간</h5>
            <h3>개인적인 토론으로 내 생각을 확장하세요</h3>
            <p>
              혼자만 볼 수 있는 개인 토론 기능으로 몰랐던 것을 질문하고  
              영화의 깊은 의미를 탐구하며 더 나은 시각을 얻어보세요.
            </p>
          </div>
        </div>
      </section>

      <!-- Section 4 -->
      <section class="content container section" ref="sections">
        <div class="row align-items-center my-5 topdiv">
          <div class="col-md-12 text-section text-center">
            <h5 class="small-title">다양한 리뷰와 의견</h5>
            <h3>다른 사람들의 리뷰를 확인하고 소통하세요</h3>
            <p>
              리뷰가 마음에 드는 사람을 팔로우하고 그들의 새로운 글을 확인할 수 있습니다.  
              서로의 의견을 통해 다양한 시각을 경험해 보세요.
            </p>
          </div>
        </div>
      </section>

      <!-- Section 5 -->
      <section class="content container section" ref="sections">
        <div class="row align-items-center my-5 topdiv text-center">
          <div class="col-md-6 mx-auto">
            <img src="../assets/Guideicons/person3.png" alt="Illustration 3" class="img-fluid" width="300">
          </div>
          <div class="col-md-6 text-section">
            <h5 class="small-title">성장을 위한 첫걸음</h5>
            <h3>영화와 토론으로 새로운 길을 만들어보세요</h3>
            <p>
              Cinerium은 단순한 영화 감상을 넘어,  
              함께 느끼고 질문하며 성장할 수 있는 공간입니다.  
              지금 당신의 영화 여정을 시작하세요.
            </p>
          </div>
          <div class="text-center py-5 mt-5">
            <button @click="goToSignUp" class="btn btn-outline-success btn-lg">회원가입하기</button>
          </div>
        </div>
      </section>
    </main>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter();
const sections = ref([]);

const goToSignUp = () => {
  router.push({ name: 'SignUpView' });
};

onMounted(() => {
  const observerOptions = {
    root: null,
    threshold: 0.1, // 섹션의 10%가 보일 때 애니메이션 트리거
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible'); // 섹션이 보이면 visible 클래스 추가
      }
    });
  }, observerOptions);

  sections.value = document.querySelectorAll('.section');
  sections.value.forEach((section) => observer.observe(section));
});
</script>

<style scoped>
/* 전체 배경 스타일 */
.guide-page {
  position: relative;
  width: 100%;
  min-height: 100vh;
  background-image: url('../assets/Guideicons/background.png');
  background-size: cover;
  background-repeat: no-repeat;
  background-position: center;
  overflow: hidden;
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
  font-size: 1.2rem;
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
  font-size: 1.5rem;
  color: #00380C;
  font-weight: bold;
}

.content .text-section h3 {
  font-size: 2.5rem;
  margin-top: 10px;
  color: #333;
  font-weight: bold;
}

.content .text-section p {
  margin-top: 10px;
  font-size: 1.2rem;
  color: #555;
}

/* Row styling */
.topdiv {
  padding-bottom: 15rem;
  padding-top: 15rem;
}

.custom-width {
  width: 50%;
  max-width: 600px;
  margin: 0 auto;
}

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

/* Section animation */
.section {
  opacity: 0;
  transform: translateY(50px);
  transition: all 0.8s ease-out;
}

.section.visible {
  opacity: 1;
  transform: translateY(0);
}

/* Section 5 이미지 가운데 정렬 */
.img3 {
  transform: scale(1.3);
  transition: transform 0.3s ease;
  margin: 0 auto;
  display: block;
}
</style>
