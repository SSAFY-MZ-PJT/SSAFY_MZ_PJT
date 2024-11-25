<template>
  <div>
    <Search />
    <div class="mx-4">
      <!-- Section Title -->
      <div class="container mt-5">
        <h2 class="text-center fw-bold mb-4">{{ categoryName }}</h2>
        <p class="text-muted text-center">Explore all movies in this category</p>
      </div>

      <!-- Movie Cards Grid -->
      <div class="mt-5">
        <div v-if="movieStore.isLoading" class="text-center">
          <p>Loading movies...</p>
        </div>
        <div v-else-if="movieStore.error" class="text-center text-danger">
          <p>{{ movieStore.error }}</p>
        </div>
        <div v-else>
          <div class="container">
            <div class="movie-grid">
              <div
                class="movie-card"
                v-for="movie in paginatedMovies"
                :key="movie.id"
              >
                <!-- Card -->
                <div class="card h-100 mt-3 me-2">
                  <div class="position-relative">
                    <!-- Movie Poster -->
                    <router-link :to="{ name: 'MovieDetailView', params: { id: movie.id } }" class="card-link">
                      <img
                      :src="movie.poster_image_url"
                      class="card-img-top poster-image"
                      :alt="movie.title"
                      />
                    </router-link>
                      
                      <!-- Favorite Button -->
                      <button
                        class="bookmark-btn position-absolute top-0 end-0 btn btn-sm m-1"
                        @click="toggleFavorite(movie.id)"
                        :class="{ active: movie.isFavorite }"
                      >
                        <svg
                          xmlns="http://www.w3.org/2000/svg"
                          width="20"
                          height="20"
                          fill="currentColor"
                          class="bi bi-bookmark"
                          viewBox="0 0 16 16"
                        >
                          <path
                            d="M2 2v13.5l6-3.5 6 3.5V2a1 1 0 0 0-1-1H3a1 1 0 0 0-1 1z"
                            :fill="movie.isFavorite ? '#002C0C' : 'currentColor'"
                          />
                        </svg>
                      </button>
                    </div>
  
                    <!-- Card Body -->
                    <div class="card-body">
                      <h6 class="card-title text-truncate fw-bold">
                        {{ movie.title }}
                      </h6>
                      <p class="text-muted mb-1">
                        📅 {{ movie.release_date }} &nbsp;&nbsp;
                        <span class="text-warning fw-bold">★ {{ movie.rating.toFixed(1) }}</span>
                      </p>
                      <div class="d-flex align-items-center justify-content-between">
                        <!-- Trailer Button -->
                        <button
                          class="btn custom-button btn-sm"
                          @click="playTrailer(movie.trailer_url)"
                        >
                          ▶ Trailer
                        </button>
                      </div>
                    </div>
                  </div>
              </div>
            </div>
          </div>

          <!-- 페이지 이동 바 -->
          <div class="mt-5 pt-4">
            <nav aria-label="Page navigation">
              <ul class="pagination justify-content-center">
                <!-- 5개 이전으로 이동 -->
                <li class="page-item" :class="{ disabled: currentPage <= 5 }">
                  <a
                    class="page-link"
                    href="#"
                    @click.prevent="changePage(currentPage - 5)"
                  >
                    &laquo; Prev 5
                  </a>
                </li>

                <!-- 이전 페이지 -->
                <li class="page-item" :class="{ disabled: currentPage === 1 }">
                  <a
                    class="page-link"
                    href="#"
                    @click.prevent="changePage(currentPage - 1)"
                  >
                    &laquo;
                  </a>
                </li>

                <!-- 페이지 번호 -->
                <li
                  class="page-item"
                  v-for="page in visiblePages"
                  :key="page"
                  :class="{ active: page === currentPage }"
                >
                  <a
                    class="page-link"
                    href="#"
                    @click.prevent="changePage(page)"
                  >
                    {{ page }}
                  </a>
                </li>

                <!-- 다음 페이지 -->
                <li
                  class="page-item"
                  :class="{ disabled: currentPage === totalPages }"
                >
                  <a
                    class="page-link"
                    href="#"
                    @click.prevent="changePage(currentPage + 1)"
                  >
                    &raquo;
                  </a>
                </li>

                <!-- 5개 이후로 이동 -->
                <li
                  class="page-item"
                  :class="{ disabled: currentPage > totalPages - 5 }"
                >
                  <a
                    class="page-link"
                    href="#"
                    @click.prevent="changePage(currentPage + 5)"
                  >
                    Next 5 &raquo;
                  </a>
                </li>
              </ul>
            </nav>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import Search from "@/components/Search.vue";
import { useRoute } from "vue-router";
import { onMounted, computed, ref } from "vue";
import { useMovieStore } from "@/stores/movie";

const route = useRoute();
const movieStore = useMovieStore();

// 현재 카테고리 가져오기
const category = computed(() => route.params.category);

// 카테고리 이름 정의
const categoryName = computed(() => {
  if (category.value === "nowPlaying") return "Now Playing Movies";
  if (category.value === "popular") return "Popular Movies";
  if (category.value === "recommended") return "Recommended Movies";
  return "Movies";
});

// Pagination 관련 상태
const currentPage = ref(1); // 현재 페이지
const itemsPerPage = 15; // 페이지당 영화 수

// 현재 페이지의 영화 계산
const paginatedMovies = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage;
  const end = start + itemsPerPage;
  return movieStore.currentMovies.slice(start, end);
});

// 총 페이지 수 계산
const totalPages = computed(() =>
  Math.ceil(movieStore.currentMovies.length / itemsPerPage)
);

// 5개씩 보이는 페이지 목록
const visiblePages = computed(() => {
  const start = Math.floor((currentPage.value - 1) / 5) * 5 + 1;
  const end = Math.min(start + 4, totalPages.value);
  const pages = [];
  for (let i = start; i <= end; i++) {
    pages.push(i);
  }
  return pages;
});

// 페이지 변경 핸들러
const changePage = (page) => {
  if (page >= 1 && page <= totalPages.value) {
    currentPage.value = page;
    window.scrollTo(0, 0); // 페이지 전환 시 화면 맨 위로 스크롤
  }
};

// 영화 데이터 가져오기
onMounted(() => {
  movieStore.fetchMoviesByCategory(category.value);
});

// 즐겨찾기 토글
const toggleFavorite = (id) => {
  console.log(`Toggled favorite for movie with id: ${id}`);
};

// 트레일러 열기
const playTrailer = (url) => {
  window.open(url, "_blank");
};
</script>

<style scoped>
/* Bookmark Button */
.bookmark-btn {
  background-color: rgba(0, 0, 0, 0.3);
  border: none;
  border-radius: 50%;
  padding: 0.5rem;
  color: white;
  transition: all 0.3s ease;
}

.bookmark-btn:hover {
  background-color: rgba(0, 0, 0, 0.6);
}

.bookmark-btn.active {
  background-color: rgba(255, 255, 255, 0.8);
}

/* 카드 디자인 */
.movie-grid {
  display: grid;
  gap: 1.5rem;
  grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
}

.movie-card {
  display: flex;
  flex-direction: column;
}

.card {
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  border-radius: 10px;
  overflow: hidden;
  background-color: #ffffff;
  height: 100%;
  transition: transform 0.3s ease;
}

.card:hover {
  transform: scale(1.05);
  z-index: 2;
}

.poster-image {
  width: 100%;
  height: 375px;
  object-fit: cover;
}

/* Trailer Button */
.custom-button {
  width: 100%;
  background-color: #f3f3f3;
  color: #686868 !important;
  border: 1px solid #f3f3f3 !important;
  transition: all 0.3s ease;
}

.custom-button:hover:not(:disabled) {
  background-color: #c4302b !important;
  color: #ffffff !important;
  border-color: #c4302b !important;
}

/* Pagination */
.pagination .page-link {
  color: #254E01;
  transition: background-color 0.3s ease, color 0.3s ease;
}

.pagination .page-link:hover {
  background-color: #254E01;
  color: #ffffff;
}

.pagination .page-item.active .page-link {
  background-color: #254E01;
  color: #ffffff;
  border: none;
}

.card-link {
  text-decoration: none; /* 밑줄 제거 */
  }

  .card-link:hover {
    text-decoration: none; /* 호버 상태에서도 밑줄 제거 */
  }
</style>
