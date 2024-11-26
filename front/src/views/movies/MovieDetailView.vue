<!-- MovieDetailView -->
<template>
  <div>
    <Search />
    <div class="container mt-5 pt-5">
      <!-- 로딩 및 에러 처리 -->
      <div v-if="movieStore.isLoading" class="text-center">
        <p>Loading movie details...</p>
      </div>
      <div v-else-if="movieStore.error" class="text-center text-danger">
        <p>{{ movieStore.error }}</p>
      </div>
      <div v-else-if="movieStore.movieDetails">
        <!-- Movie Title and Poster -->
        <div class="row">
          <div class="col-md-3">
            <img :src="movieStore.movieDetails.poster_image_url" alt="Movie Poster" class="img-fluid rounded shadow" />
          </div>
          <div class="col-md-9">
            <div class="d-flex justify-content-between align-items-start">
              <div>
                <h1 class="fw-bold">{{ movieStore.movieDetails.title }}</h1>
                <p class="text-muted">
                  {{ movieStore.movieDetails.release_date }} • Rating: {{ movieStore.movieDetails.rating }} • Runtime: {{ movieStore.movieDetails.runtime }} mins
                </p>
              </div>
              <!-- Watchlist Button -->
              <button
                class="btn custom-button"
                @click="toggleFavorite(movieStore.movieDetails.id)"
                :class="{ 'btn-success': movieStore.movieDetails.isFavorite, 'btn-outline-primary': !movieStore.movieDetails.isFavorite }"
              >
                <i :class="movieStore.movieDetails.isFavorite ? 'bi bi-bookmark-check-fill' : 'bi bi-bookmark'"></i>
                {{ movieStore.movieDetails.isFavorite ? 'Added to Watchlist' : 'Add to Watchlist' }}
              </button>
            </div>

            <!-- Genres -->
            <div class="mb-3">
              <span v-for="genre in movieStore.movieDetails.genres" :key="genre.id" class="badge bg-secondary me-2">
                {{ genre.name }}
              </span>
            </div>

            <!-- Plot -->
            <p class="lead">{{ movieStore.movieDetails.plot }}</p>
            
            <!-- Tagline -->
            <div v-if="movieStore.movieDetails.tagline" class="tagline mt-4">
              "{{ movieStore.movieDetails.tagline }}"
            </div>

          </div>
        </div>
        
        <!-- Director Section -->
        <div class="mt-5">
          <h3 class="fw-bold pt-5">Director</h3>
          <hr />
          <div class="d-flex align-items-start gap-3">
            <img
              :src="movieStore.movieDetails.director.photo_url ? movieStore.movieDetails.director.photo_url : '/src/assets/Movieicons/default_profile.png'"
              alt="Director Image"
              class="img-fluid rounded shadow"
              width="100"
              height="100"
            />
            <div>
          </div>
          </div>
          <h5 class="fw-bold mt-3">{{ movieStore.movieDetails.director.name }}</h5>
        </div>

        <!-- Cast Section -->
        <div class="mt-5">
          <h3 class="fw-bold pt-5">Cast</h3>
          <hr />
          <div class="d-flex flex-wrap gap-4">
            <div v-for="cast in movieStore.movieDetails.actors" 
            :key="cast.id" class="text-center">
              <img :src="cast.photo_url ? cast.photo_url : '/src/assets/Movieicons/default_profile.png'" 
              class="img-fluid shadow" width="100" />
              <p class="mt-2 mb-0 fw-bold" style="color: #002c0c;">{{ cast.name }}</p>
              <p class="text-muted small">{{ cast.role || 'Actor' }}</p>
            </div>
          </div>
        </div>


        <!-- Details Section -->
        <div class="mt-5">
        <h3 class="fw-bold pt-5">Details</h3>
        <hr />
        <ul class="list-unstyled">
          <li><strong>Budget:</strong> ${{ formatNumber(movieStore.movieDetails.budget) }}</li>
          <hr />
          <li><strong>Revenue:</strong> ${{ formatNumber(movieStore.movieDetails.revenue) }}</li>
          <hr />
          <li><strong>Popularity:</strong> {{ formatNumber(movieStore.movieDetails.popularity) }}</li>
          <hr />
          <li><strong>Vote Count:</strong> {{ formatNumber(movieStore.movieDetails.vote_count) }}</li>
          <hr />
          <li><strong>Is Now Playing:</strong> {{ movieStore.movieDetails.is_now_playing ? 'Yes' : 'No' }}</li>
          <hr />
          <li><strong>Is Popular:</strong> {{ movieStore.movieDetails.is_popular ? 'Yes' : 'No' }}</li>
        </ul>


            <!-- User Reviews Section -->
          <div class="mt-5">
            <div class="d-flex justify-content-between align-items-center pt-5">
              <!-- User Reviews Title and View All Button -->
              <div class="d-flex align-items-center">
                <h3 class="fw-bold me-3">User Reviews</h3>
                <!-- View All Reviews Button -->
                <button
                  class="btn see-all"
                  @click="goToBoardDetail(route.params.id)"
                >
                  See all
                  <i class="bi bi-chevron-right"></i>
                </button>
              </div>
              <!-- Create Review Button -->
              <button
                class="btn custom-button"
                @click="router.push({ name: 'ReviewCreateView', params: { id: route.params.id } })"
              >
                Create Review
              </button>
            </div>
            <hr />
            <div
              v-for="review in topReviews"
              :key="review.id"
              class="card mt-3 p-3"
            >
              <div class="d-flex justify-content-between align-items-center">
                <h5 class="card-title mb-0 fw-bold">{{ review.title }}</h5>
                <div class="d-flex align-items-center">
                  <i
                    :class="review.liked ? 'bi bi-hand-thumbs-up-fill like-icon' : 'bi bi-hand-thumbs-up like-icon'"
                    @click="toggleLike(review.id)"
                  ></i>
                  <span class="like-count ms-2">• {{ review.likes }} likes</span>
                </div>
              </div>
              <p class="text-muted small mb-1">
                By {{ review.author }} • {{ formatDate(review.created_at) }}
              </p>
              <p class="card-text">{{ review.content }}</p>
            </div>
          </div>
        </div>
      </div>


      <!-- Similar Movies Section -->
      <div class="section mt-5">
        <div class="section-header d-flex justify-content-between align-items-center">
          <h3 class="fw-bold">Similar Movies</h3>
          <hr>
          <div class="controls">
            <button class="circle-btn" @click="prevSlide">❮</button>
            <button class="circle-btn" @click="nextSlide">❯</button>
          </div>
        </div>
        <div class="carousel-container">
          <div class="carousel">
            <div
              class="carousel-slide"
              v-for="(chunk, index) in chunkedMovies(movieStore.similarMovies)"
              :key="index"
              :class="{ active: index === currentSlide }"
            >
              <div class="movie-grid">
                <MovieCard
                  v-for="movie in chunk"
                  :key="movie.id"
                  :movie="movie"
                />
              </div>
            </div>
          </div>
        </div>
      </div>

    </div>
  </div>
</template>

<script setup>
import { ref, watch, onMounted, computed } from "vue";
import { useRoute, useRouter } from "vue-router";
import { useMovieStore } from "@/stores/movie";
import { useReviewStore } from "@/stores/review";
import Search from "@/components/Search.vue";
import MovieCard from "@/components/MovieCard.vue";

// 상태 및 라우트 설정
const route = useRoute()
const router = useRouter()
const movieStore = useMovieStore();
const reviewStore = useReviewStore();
const currentSlide = ref(0);

// 리뷰 데이터를 저장할 상태
const reviews = ref([]);

// 대표 리뷰 2개 계산
const topReviews = computed(() => {
  const sortedReviews = [...reviews.value].sort((a, b) => {
    if (b.likes === a.likes) {
      return new Date(b.created_at) - new Date(a.created_at); // 최신 순
    }
    return b.likes - a.likes; // 좋아요 순
  });
  return sortedReviews.slice(0, 2);
});

// 리뷰 데이터 가져오기
const fetchReviews = async () => {
  try {
    const { reviews: fetchedReviews } = await reviewStore.fetchMovieDetails(route.params.id);
    reviews.value = fetchedReviews; // 리뷰 상태 업데이트
  } catch (error) {
    console.error("Error fetching reviews:", error);
  }
};

// 날짜 포맷 함수
const formatDate = (isoDate) => {
  const date = new Date(isoDate);
  return date.toISOString().split("T")[0]; // "YYYY-MM-DD" 포맷
};

// 좋아요 토글 (movieStore.movieDetails.reviews용)
const toggleMovieDetailReviewLike = (id) => {
  const review = movieStore.movieDetails.reviews.find((r) => r.id === id);
  if (review) {
    review.liked = !review.liked;
    review.likes += review.liked ? 1 : -1;
  }
};

const goToBoardDetail = (movieId) => {
  router.push({ name: 'BoardDetailView', params: { movieId } });
};

// 데이터 로딩 로직
const loadMovieData = async (movieId) => {
  try {
    await movieStore.fetchMovieDetails(movieId); // 영화 세부 정보 로드
    const genres = movieStore.movieDetails.genres.map((genre) => genre.name);
    await movieStore.fetchSimilarMovies(genres); // 비슷한 영화 로드
  } catch (error) {
    console.error("Error loading movie data:", error);
  }
};

// 캐러셀 동작
const chunkedMovies = (movies, chunkSize = 4) =>
  movies.reduce((result, _, index) => {
    if (index % chunkSize === 0) result.push(movies.slice(index, index + chunkSize));
    return result;
  }, []);

const nextSlide = () => {
  const totalSlides = chunkedMovies(movieStore.similarMovies).length;
  currentSlide.value = (currentSlide.value + 1) % totalSlides;
};

const prevSlide = () => {
  const totalSlides = chunkedMovies(movieStore.similarMovies).length;
  currentSlide.value = (currentSlide.value - 1 + totalSlides) % totalSlides;
};


// 좋아요 토글 함수
const toggleFavorite = async (movieId) => {
  try {
    await movieStore.toggleFavorite(movieId);
  } catch (error) {
    console.error("Failed to toggle favorite:", error);
  }
};


// 숫자 형식 변환
const formatNumber = (number) => 
  new Intl.NumberFormat("en-US", { maximumFractionDigits: 0 }).format(number);

// 초기 데이터 로드
onMounted(() => loadMovieData(route.params.id));
onMounted(fetchReviews);

// 라우트 변경 시 데이터 로드
watch(
  () => route.params.id,
  (newId) => loadMovieData(newId)
);
</script>


<style scoped>
.carousel-container {
  position: relative;
}

.carousel-slide {
  display: none;
}

.carousel-slide.active {
  display: block;
}

.movie-grid {
  display: grid;
  gap: 1rem;
}

/* 큰 화면: 4개 */
@media (min-width: 1200px) {
  .movie-grid {
    grid-template-columns: repeat(4, 1fr);
  }
}

/* 중간 화면: 2개 */
@media (max-width: 1199px) and (min-width: 768px) {
  .movie-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

/* 작은 화면: 1개 */
@media (max-width: 767px) {
  .movie-grid {
    grid-template-columns: repeat(1, 1fr);
  }
}

.controls {
  display: flex;
  gap: 10px;
}

.section-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
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

.container {
  max-width: 1200px;
}
.img-fluid {
  max-width: 100%;
  height: auto;
  border-radius: 12px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}
.badge {
  font-size: 0.9rem;
  padding: 0.5rem;
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
.tagline {
  font-size: 1.5rem;
  font-style: italic;
  color: #4a4a4a;
  border-left: 5px solid #254e01;
  padding-left: 15px;
  margin-top: 20px;
}
.custom-link {
  color: #254e01;
  text-decoration: none;
  transition: color 0.3s ease;
}
.custom-link:hover {
  color: #1a3a00;
  text-decoration: underline;
}

hr {
  border: none;
  border-top: 2px solid #ddd;
  margin: 2rem 0;
}

/* 카드 디자인 */
.card {
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  border-radius: 10px;
  overflow: hidden;
  background-color: #ffffff;
  height: 100%; /* Ensure card height is consistent */
  transition: transform 0.3s ease;
}

.card:hover {
  transform: scale(1.05);
  z-index: 2;
}

.poster-image {
  width: 100%;
  height: 375px; /* Adjust for 2:3 aspect ratio */
  object-fit: cover;
}

.see-all:hover {
  background-color: #dddddd;
  color: #242424;
  text-decoration: none;
}

.see-all {
  margin-left: 0.5rem; /* 아이콘과 텍스트 사이 간격 */
  font-size: 1.2rem;
  color: #888888;
  background-color: #f0f0f0;
}

.btn-success {
  background-color: #28a745;
  border-color: #28a745;
  color: #fff;
}

.btn-outline-primary {
  border-color: #007bff;
  color: #007bff;
}

.btn-outline-primary:hover {
  background-color: #007bff;
  color: #fff;
}
</style>
