<!-- BoardView -->
<template>
  <div>
    <Search />
    <div class="mx-4">
      <!-- 로딩 및 에러 처리 -->
      <div v-if="isLoading" class="text-center my-5 fs-2 fs-bold">
        <p>Loading movies and reviews...</p>
      </div>
      <div v-else-if="error" class="text-center my-5 text-danger">
        <p>{{ error }}</p>
      </div>
      <div v-else>
        <!-- 영화 리스트 -->
        <div class="container mt-5">
          <div v-for="movie in movies.slice(0, 50)" :key="movie.id" class="mb-5">
            <!-- 영화 정보 -->
            <div class="movie-info d-flex justify-content-between align-items-center mb-4">
              <div>
                <router-link
                  :to="{ name: 'BoardDetailView', params: { movieId: movie.id } }"
                  class="styled-link"
                >
                  <p class="fw-bold">{{ movie.title }}</p>
                </router-link>
                  <p class="text-muted">
                    {{ movie.release_date }} • {{ movie.rating.toFixed(1) }} • {{ movie.runtime }} mins
                  </p>
                </div>
                <div class="d-flex align-items-center">
                  <button
                  class="btn custom-button"
                  @click="toggleFavorite(movieStore.movieDetails.id)"
                  :class="{ 'btn-success': movieStore.movieDetails.isFavorite, 'btn-outline-primary': !movieStore.movieDetails.isFavorite }"
                >
                  <i :class="movieStore.movieDetails.isFavorite ? 'bi bi-bookmark-check-fill' : 'bi bi-bookmark'"></i>
                  {{ movieStore.movieDetails.isFavorite ? 'Added to Watchlist' : 'Add to Watchlist' }}
                </button>
                </div>
              </div>
              
              <!-- 영화 포스터와 리뷰 -->
              <div class="row align-items-stretch">
                <div class="col-md-4">
                  <img
                    :src="movie.poster_image_url"
                    alt="Movie Poster"
                    class="img-fluid rounded shadow h-100 clickable-poster"
                    @click="navigateToMovie(movie.id)"
                  />
                </div>
                <div class="col-md-8 d-flex flex-column">
                  <div
                    v-for="(review, index) in movie.representativeReviews"
                    :key="index"
                    class="review-card flex-grow-1 mb-2 d-flex flex-column justify-content-between"
                    :style="{ backgroundColor: getReviewBgColor(review.rating) }"
                    @click="navigateToReview(review.id, movie.id)"
                    >
                    <div>
                      <div class="d-flex align-items-center mb-2">
                        <span class="rating-badge">
                          <span>★</span>
                          {{ review.rating ? `${review.rating}/10` : "N/A" }}
                        </span>
                        <h5 class="mb-0 ms-3">{{ review.title }}</h5>
                      </div>
                      <p class="text-muted mb-1">Date • {{ formatDate(review.created_at) }}</p>
                      <p>{{ review.content }}</p>
                    </div>
                    <div class="d-flex align-items-center mt-auto">
                      <i
                        :class="review.liked ? 'bi bi-hand-thumbs-up-fill like-icon' : 'bi bi-hand-thumbs-up like-icon'"
                        @click="toggleLike(movie.id, review.id)"
                      ></i>
                      <span class="like-count ms-2">• {{ review.likes.length }} likes</span>
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

              <!-- 현재 보이는 페이지 그룹 -->
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
              <li class="page-item" :class="{ disabled: currentPage === totalPages }">
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
</template>

<script setup>
import { ref, computed, onMounted } from "vue";
import Search from "@/components/Search.vue";
import { useReviewStore } from "@/stores/review";
import { useRouter } from "vue-router"
import { useMovieStore } from "@/stores/movie";

const movieStore = useMovieStore();
const router = useRouter()
const reviewStore = useReviewStore();
const isLoading = ref(true);
const error = ref(null);
const movies = ref([]);
const currentPage = ref(1);
const itemsPerPage = 3;

// 평점에 따라 배경 색깔 변화
const getReviewBgColor = (rating) => {
  if (rating >= 8) return "#E3E8DE";
  if (rating >= 5) return "#F2F4F0";
  return "#FAFAFA";
};

// 대표 리뷰 계산
const calculateRepresentativeReviews = (reviews) => {
  if (!reviews || reviews.length === 0) return [];
  const highestRated = [...reviews].sort((a, b) => b.rating - a.rating)[0];
  const lowestRated = [...reviews].sort((a, b) => a.rating - b.rating)[0];
  return [highestRated, lowestRated];
};

// 페이지네이션 처리
const totalPages = computed(() => Math.ceil(movies.value.length / itemsPerPage));
const paginatedMovies = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage;
  const end = start + itemsPerPage;
  return movies.value.slice(start, end);
});

const visiblePages = computed(() => {
  const start = Math.floor((currentPage.value - 1) / 5) * 5 + 1;
  const end = Math.min(start + 4, totalPages.value);
  return Array.from({ length: end - start + 1 }, (_, i) => start + i);
});


const changePage = (page) => {
  if (page >= 1 && page <= totalPages.value) {
    currentPage.value = page;
  }
};

// 날짜 포맷 함수
const formatDate = (isoDate) => {
  const date = new Date(isoDate);
  return date.toISOString().split("T")[0]; // "YYYY-MM-DD" 포맷
};

// 좋아요 토글
const toggleLike = async (movieId, reviewId) => {
  try {
    await reviewStore.toggleLike(reviewId);
    const movie = movies.value.find((m) => m.id === movieId);
    const review = movie.representativeReviews.find((r) => r.id === reviewId);
    if (review) {
      review.liked = !review.liked;
      review.likes += review.liked ? 1 : -1;
    }
  } catch (err) {
    console.error("Failed to toggle like:", err);
  }
};

// 데이터 로드
const loadMoviesAndReviews = async () => {
  try {
    isLoading.value = true;
    error.value = null;

    // 페이지 번호와 한 번에 가져올 데이터 개수를 요청
    const fetchedMovies = await reviewStore.fetchMoviesWithReviews({
      page: currentPage.value,
      limit: itemsPerPage,
    });

    // 데이터 제한을 프론트엔드에서 적용 시간 남을 때 ㄱㄱ
    movies.value = fetchedMovies.map((movie) => ({
      ...movie,
      representativeReviews: calculateRepresentativeReviews(movie.reviews),
    }));
  } catch (err) {
    error.value = "Failed to load movies or reviews.";
    console.error(err);
  } finally {
    isLoading.value = false;
  }
};

const navigateToReview = (reviewId, movieId) => {
  console.log('Navigating to ReviewDetailView:', { reviewId, movieId });
  router.push({ name: 'ReviewDetailView', params: { id: reviewId, movieId } });
};

const navigateToMovie = (movieId) => {
  router.push({ name: 'BoardDetailView', params: { movieId } });
};

// 좋아요 토글 함수
const toggleFavorite = async (movieId) => {
  try {
    await movieStore.toggleFavorite(movieId);
  } catch (error) {
    console.error("Failed to toggle favorite:", error);
  }
};

onMounted(loadMoviesAndReviews);
</script>

<style scoped>
/* 하단 화살표 */
.btn-outline-secondary {
  font-size: 1.5rem;
  border-radius: 50%;
  width: 50px;
  height: 50px;
}

/* 최신순, 평점순 */
.custom-nav {
  font-size: 1rem;
}

.custom-link {
  color: #084e0d !important;
  transition: color 0.3s ease;
}

.custom-link:hover {
  color: #5f9c63 !important;
}

.custom-nav .text-muted {
  font-size: 1.2rem;
  color: #6c757d;
}

.container {
  max-width: 1200px;
  padding-left: 15px;
  padding-right: 15px;
}

img {
  border-radius: 10px;
}

.custom-button {
  background-color: #ffffff;
  color: #254e01 !important;
  border: 1px solid #254e01 !important;
  transition: all 0.3s ease;
}

.custom-button:hover:not(:disabled) {
  background-color: #254e01 !important;
  color: #ffffff !important;
  border-color: #254e01 !important;
}

.custom-button:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

button:hover {
  transform: scale(1.05);
}

.rating-badge {
  background-color: transparent;
  color: #000;
  font-weight: bold;
  border: none;
  padding: 5px 10px;
}

.rating-badge span {
  color: #ffd700;
}

.like-icon {
  font-size: 1.5rem;
  color: #797979;
  cursor: pointer;
  transition: color 0.3s ease;
}

.like-icon:hover {
  color: #545454;
  
}

.like-count {
  font-size: 1rem;
  color: #545454;
}

.pagination .page-link {
  color: #254e01;
  transition: background-color 0.3s ease, color 0.3s ease;
}

.pagination .page-link:focus,
.pagination .page-link:active {
  outline: none;
  box-shadow: none;
  background-color: #ffffff;
  color: #254e01;
  font-weight: bold;
}

.pagination .page-link:hover {
  background-color: #254e01;
  color: #ffffff;
}

.pagination .page-item.active .page-link {
  background-color: #254e01;
  color: #ffffff;
  border: none;
}

/* 라우터 링크 스타일 */
.styled-link {
  font-size: 30px;
  text-decoration: none;
  color: #000000; /* 기본 텍스트 색상 */
  background-clip: text; /* 배경 이미지를 텍스트에만 클립 */
  -webkit-background-clip: text; /* 웹킷 브라우저 호환 */
  transition: background-position 0.5s ease, font-size 0.3s ease, color 0.3s ease;
}

/* 호버 효과 */
.styled-link:hover {
  text-decoration: none;
  background-position: 100% 0; /* 배경 위치 변경 효과 */
  font-size: 2rem; /* 글씨 크기 증가 */
  background-image: linear-gradient(90deg, #254e01, #8bc34a); /* 그라데이션 */
}


.row.align-items-stretch {
  display: flex;
  align-items: stretch;
}

.col-md-4 img {
  object-fit: cover;
  height: 100%; /* 포스터가 항상 세로를 꽉 채우도록 */
}

.col-md-8 {
  display: flex;
  flex-direction: column;
  justify-content: space-between; /* 리뷰가 고르게 분배되도록 */
}

.review-card {
  flex: 1;
  margin-bottom: 10px;
  padding: 15px;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease; 
  cursor: pointer;
}

.review-card:hover {
  transform: scale(1.05); 
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15); 
}


.clickable-poster {
  cursor: pointer;
}


</style>

