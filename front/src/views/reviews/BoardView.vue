<template>
  <div>
    <Search />
    <div class="mx-4">
      <!-- v-for로 영화 표시 -->
      <div class="container mt-5">
        <ul class="nav nav-underline justify-content-end custom-nav mt-5 pb-4">
          <li class="nav-item">
            <a class="nav-link custom-link" href="#">최신순</a>
          </li>
          <li class="nav-item mx-2 text-muted">/</li>
          <li class="nav-item">
            <a class="nav-link custom-link" href="#">별점순</a>
          </li>
        </ul>
        <div
          v-for="movie in paginatedMovies"
          :key="movie.id"
          class="mb-5"
        >
          <!-- 상단 정보 -->
          <div class="movie-info d-flex justify-content-between align-items-center mb-4">
            <div>
              <h1 class="fw-bold">{{ movie.title }}</h1>
              <p class="text-muted">
                {{ movie.year }} • {{ movie.rating }} • {{ movie.runtime }}
              </p>
            </div>
            <div class="d-flex align-items-center">
              <button class="btn custom-button">+ Add to Watchlist</button>
            </div>
          </div>
  
          <!-- 중앙 포스터 및 리뷰 -->
          <div class="row">
            <!-- 영화 포스터 -->
            <div class="col-md-4">
              <img :src="movie.poster" alt="Movie Poster" class="img-fluid rounded shadow" />
            </div>
            <!-- 리뷰 리스트 -->
            <div class="col-md-8">
              <div
                class="review-card p-3 mb-4"
                v-for="(review, index) in movie.reviews.slice(0, 2)"
                :key="index"
                :style="{ backgroundColor: getReviewBgColor(review.rating) }"
              >
                <div class="d-flex align-items-center mb-2">
                  <span class="rating-badge">
                    <span>★</span> {{ review.rating }}/10
                  </span>
                  <h5 class="mb-0 ms-3">{{ review.title }}</h5>
                </div>
                <p class="text-muted mb-1">Date: {{ review.date }}</p>
                <p>{{ review.content }}</p>
                <div class="d-flex align-items-center">
                  <i
                    :class="review.liked ? 'bi bi-hand-thumbs-up-fill like-icon' : 'bi bi-hand-thumbs-up like-icon'"
                    @click="toggleLike(movie.id, review.id)"
                  ></i>
                  <span class="like-count ms-2">• {{ review.likes }} likes</span>
                </div>
              </div>
              <!-- 하단 화살표 -->
              <div class="text-center mt-4">
                <button class="btn btn-outline-secondary" @click="goToAllReviews">
                  <i class="bi bi-chevron-down"></i>
                </button>
              </div>
            </div>
          </div>
        </div>
  
  
  
        <!-- 페이지 이동 바 -->
        <nav aria-label="Page navigation">
          <ul class="pagination justify-content-center">
            <!-- 이전 페이지 버튼 -->
            <li class="page-item" :class="{ disabled: currentPage === 1 }">
              <a class="page-link" href="#" aria-label="Previous" @click.prevent="changePage(currentPage - 1)">
                <span aria-hidden="true">&laquo;</span>
              </a>
            </li>
            <!-- 페이지 번호 -->
            <li
              class="page-item"
              v-for="page in totalPages"
              :key="page"
              :class="{ active: currentPage === page }"
            >
              <a class="page-link" href="#" @click.prevent="changePage(page)">{{ page }}</a>
            </li>
            <!-- 다음 페이지 버튼 -->
            <li class="page-item" :class="{ disabled: currentPage === totalPages }">
              <a class="page-link" href="#" aria-label="Next" @click.prevent="changePage(currentPage + 1)">
                <span aria-hidden="true">&raquo;</span>
              </a>
            </li>
          </ul>
        </nav>
      </div>
    </div>
  </div>
</template>

<script setup>
import { reactive, computed } from "vue";
import Search from "@/components/Search.vue";

// 더미 데이터
const movies = reactive([
  {
    id: 1,
    title: "Spider-Man: Across the Spider-Verse",
    year: 2024,
    runtime: "2h 10m",
    rating: "PG-13",
    poster: "https://via.placeholder.com/300x400",
    reviews: [
      {
        id: 1,
        rating: 10,
        title: "Amazing Sequel!",
        date: "20 Feb 2024",
        content: "A truly groundbreaking movie that redefines animation.",
        likes: 320,
        liked: false,
      },
      {
        id: 3,
        rating: 1,
        title: "Amazing Sequel!",
        date: "20 Feb 2024",
        content: "A truly groundbreaking movie that redefines animation.",
        likes: 320,
        liked: false,
      },
    ],
  },
  {
    id: 2,
    title: "Interstellar",
    year: 2014,
    runtime: "2h 49m",
    rating: "PG-13",
    poster: "https://via.placeholder.com/300x400",
    reviews: [
      {
        id: 1,
        rating: 9,
        title: "A Sci-Fi Masterpiece",
        date: "15 Feb 2014",
        content: "Christopher Nolan at his best.",
        likes: 540,
        liked: false,
      },
      {
        id: 4,
        rating: 5,
        title: "A Sci-Fi Masterpiece",
        date: "15 Feb 2014",
        content: "Christopher Nolan at his best.",
        likes: 540,
        liked: false,
      },
    ],
  },
  {
    id: 2,
    title: "Interstellar",
    year: 2014,
    runtime: "2h 49m",
    rating: "PG-13",
    poster: "https://via.placeholder.com/300x400",
    reviews: [
      {
        id: 1,
        rating: 9,
        title: "A Sci-Fi Masterpiece",
        date: "15 Feb 2014",
        content: "Christopher Nolan at his best.",
        likes: 540,
        liked: false,
      },
      {
        id: 4,
        rating: 5,
        title: "A Sci-Fi Masterpiece",
        date: "15 Feb 2014",
        content: "Christopher Nolan at his best.",
        likes: 540,
        liked: false,
      },
    ],
  },
  {
    id: 2,
    title: "Interstellar",
    year: 2014,
    runtime: "2h 49m",
    rating: "PG-13",
    poster: "https://via.placeholder.com/300x400",
    reviews: [
      {
        id: 1,
        rating: 9,
        title: "A Sci-Fi Masterpiece",
        date: "15 Feb 2014",
        content: "Christopher Nolan at his best.",
        likes: 540,
        liked: false,
      },
      {
        id: 4,
        rating: 5,
        title: "A Sci-Fi Masterpiece",
        date: "15 Feb 2014",
        content: "Christopher Nolan at his best.",
        likes: 540,
        liked: false,
      },
    ],
  },
  // Add more movie objects as needed
]);

// 페이지네이션 데이터
const currentPage = reactive({ value: 1 });
const itemsPerPage = 3;

const totalPages = computed(() => Math.ceil(movies.length / itemsPerPage));

const paginatedMovies = computed(() => {
  const start = (currentPage.value - 1) * itemsPerPage;
  const end = start + itemsPerPage;
  return movies.slice(start, end);
});

const changePage = (page) => {
  if (page >= 1 && page <= totalPages.value) {
    currentPage.value = page;
  }
};

const getReviewBgColor = (rating) => {
  if (rating >= 8) return "#E3E8DE";
  if (rating >= 5) return "#F2F4F0";
  return "#FAFAFA";
};

const toggleLike = (movieId, reviewId) => {
  const movie = movies.find((m) => m.id === movieId);
  const review = movie.reviews.find((r) => r.id === reviewId);
  if (review) {
    review.liked = !review.liked;
    review.likes += review.liked ? 1 : -1;
  }
};

const goToAllReviews = (movieId) => {
  window.location.href = `/movies/${movieId}/reviews`;
};
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

.review-card {
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
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
</style>
