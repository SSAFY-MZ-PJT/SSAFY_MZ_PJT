<!-- MainView -->
<template>
  <div>
    <Search />
    <div class="mx-4">
      <div class="container mt-5">
        <h1 class="text-center fw-bold mb-5">Movie Recommendations</h1>

        <!-- 로딩 및 에러 처리 -->
        <div v-if="movieStore.isLoading" class="text-center">
          <p>Loading movies...</p>
        </div>
        <div v-else-if="movieStore.error" class="text-center text-danger">
          <p>{{ movieStore.error }}</p>
        </div>
        <div v-else>
          <!-- 현재 상영 중 -->
          <div class="section">
            <div class="section-header">
              <router-link
                :to="{ name: 'RecommendDetailView', params: { category: 'nowPlaying' } }"
                class="fw-bold h3-link styled-link"
              >
              • Now Playing ▶
              </router-link>
              <div class="controls">
                <button class="circle-btn" @click="prevSlide('nowPlaying')">❮</button>
                <button class="circle-btn" @click="nextSlide('nowPlaying')">❯</button>
              </div>
            </div>
            <div class="carousel-container">
              <div class="carousel">
                <div
                  class="carousel-slide"
                  v-for="(chunk, index) in chunkedMovies(movieStore.nowPlaying)"
                  :key="index"
                  :class="{ active: index === currentSlide.nowPlaying }"
                >
                  <div class="row justify-content-center">
                    <div
                      class="col-lg-3 col-md-4 col-sm-6 mb-4"
                      v-for="movie in chunk"
                      :key="movie.id"
                    >
                      <MovieCard :movie="movie" />
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- 인기 영화 -->
          <div class="section">
            <div class="section-header">
              <router-link
                :to="{ name: 'RecommendDetailView', params: { category: 'popular' } }"
                class="fw-bold h3-link styled-link"
              >
              • Popular Movies ▶
              </router-link>
              <div class="controls">
                <button class="circle-btn" @click="prevSlide('popular')">❮</button>
                <button class="circle-btn" @click="nextSlide('popular')">❯</button>
              </div>
            </div>
            <div class="carousel-container">
              <div class="carousel">
                <div
                  class="carousel-slide"
                  v-for="(chunk, index) in chunkedMovies(movieStore.popular)"
                  :key="index"
                  :class="{ active: index === currentSlide.popular }"
                >
                  <div class="row justify-content-center">
                    <div
                      class="col-lg-3 col-md-4 col-sm-6 mb-4"
                      v-for="movie in chunk"
                      :key="movie.id"
                    >
                      <MovieCard :movie="movie" />
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- 추천 영화 -->
          <div class="section">
            <div class="section-header">
              <router-link
                :to="{ name: 'RecommendDetailView', params: { category: 'recommended' } }"
                class="fw-bold h3-link styled-link"
              >
              • Recommended Movies ▶
              </router-link>
              <div class="controls">
                <button class="circle-btn" @click="prevSlide('recommended')">❮</button>
                <button class="circle-btn" @click="nextSlide('recommended')">❯</button>
              </div>
            </div>
            <div class="carousel-container">
              <div class="carousel">
                <div
                  class="carousel-slide"
                  v-for="(chunk, index) in chunkedMovies(movieStore.recommended)"
                  :key="index"
                  :class="{ active: index === currentSlide.recommended }"
                >
                  <div class="row justify-content-center">
                    <div
                      class="col-lg-3 col-md-4 col-sm-6 mb-4"
                      v-for="movie in chunk"
                      :key="movie.id"
                    >
                      <MovieCard :movie="movie" />
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useMovieStore } from "@/stores/movie";
import { onMounted, reactive } from "vue";
import Search from "@/components/Search.vue";
import MovieCard from "@/components/MovieCard.vue";

const movieStore = useMovieStore();

const currentSlide = reactive({
  nowPlaying: 0,
  popular: 0,
  recommended: 0,
});

const chunkedMovies = (movies, chunkSize = 4) => {
  const chunks = [];
  for (let i = 0; i < movies.length; i += chunkSize) {
    chunks.push(movies.slice(i, i + chunkSize));
  }
  return chunks;
};

const nextSlide = (section) => {
  const totalSlides = chunkedMovies(movieStore[section]).length;
  currentSlide[section] = (currentSlide[section] + 1) % totalSlides;
};

const prevSlide = (section) => {
  const totalSlides = chunkedMovies(movieStore[section]).length;
  currentSlide[section] =
    (currentSlide[section] - 1 + totalSlides) % totalSlides;
};

onMounted(() => {
  movieStore.fetchMainPageMovies();
});
</script>

<style scoped>
.container {
  max-width: 1200px;
}

.section {
  margin-bottom: 50px;
}

/* 제목과 버튼을 같은 줄에 배치 */
.section-header {
  display: flex;
  justify-content: space-between; /* 제목은 왼쪽, 버튼은 오른쪽 */
  align-items: center;
  margin-bottom: 20px;
}

/* 라우터 링크 스타일 */
.styled-link {
  font-size: 25px;
  text-decoration: none;
  color: #1b3a00;
  transition: color 0.3s ease, font-size 0.3s ease;
}

.styled-link:hover {
  color: #436b02;
  font-size: 1.8rem;
}

/* 동그란 버튼 스타일 */
.controls {
  display: flex;
  gap: 10px; /* 버튼 간격 */
}

.circle-btn {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  border: none;
  background: rgba(0, 0, 0, 0.3);
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 18px;
  cursor: pointer;
  transition: background 0.3s ease;
}

.circle-btn:hover {
  background: rgba(0, 0, 0, 0.6);
}

/* 캐러셀 관련 스타일 */
.carousel-container {
  position: relative;
}

.carousel {
  overflow: hidden;
  display: flex;
  position: relative;
}

.carousel-slide {
  flex: 0 0 100%;
  display: none;
}

.carousel-slide.active {
  display: block;
}

.poster-image {
  width: 100%;
  aspect-ratio: 2 / 3; /* 2:3 비율 유지 */
  object-fit: cover;
  max-height: 375px; /* 최대 높이 제한 */
}
@media (min-width: 1200px) {
  .row .col-lg-3 {
    flex: 0 0 25%; /* 한 줄에 4개 */
    max-width: 25%;
  }
}

@media (min-width: 992px) and (max-width: 1199px) {
  .row .col-lg-3 {
    flex: 0 0 50%; /* 한 줄에 2개 */
    max-width: 50%;
  }
}

@media (min-width: 768px) and (max-width: 991px) {
  .row .col-lg-3 {
    flex: 0 0 50%; /* 한 줄에 2개 */
    max-width: 50%;
  }
}

@media (max-width: 767px) {
  .row .col-lg-3 {
    flex: 0 0 100%; /* 한 줄에 1개 */
    max-width: 100%;
  }
}

.styled-link {
  font-size: 25px;
  background-position: 100% 0; /* 그라데이션 이동 효과 */
  transition: background-position 0.5s ease, font-size 0.3s ease;
}

/* 호버 효과 */
.styled-link:hover {
  text-decoration: none;
  color: transparent; /* 텍스트 색상을 투명으로 설정 */
  background-image: linear-gradient(90deg, #254e01, #8bc34a); /* 그라데이션 */
  background-clip: text; /* 배경 이미지를 텍스트에만 클립 */
  -webkit-background-clip: text; /* 웹킷 브라우저 호환 */
  font-size: 27px; /* 글씨 크기 증가 */
}

</style>
