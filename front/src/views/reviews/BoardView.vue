<template>
    <div class="container mt-5">
      <!-- 상단 정보 -->
      <div class="movie-info d-flex justify-content-between align-items-center mb-4">
        <div>
          <h1 class="fw-bold">{{ movie.title }}</h1>
          <p class="text-muted">
            {{ movie.year }} • {{ movie.rating }} • {{ movie.runtime }}
          </p>
        </div>
        <div class="d-flex align-items-center">
          <span class="badge bg-warning text-dark me-3">
            ★ {{ movie.avgRating }} / 10 <small>({{ movie.ratingCount }}K)</small>
          </span>
          <button class="btn btn-success">+ Add to Watchlist</button>
        </div>
      </div>
  
      <!-- 중앙 포스터 및 리뷰 -->
      <div class="row">
        <!-- 영화 포스터 -->
        <div class="col-md-4">
          <img
            :src="movie.poster"
            alt="Movie Poster"
            class="img-fluid rounded shadow"
          />
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
              <span class="badge bg-warning text-dark me-2">
                ★ {{ review.rating }}/10
              </span>
              <h5 class="mb-0">{{ review.title }}</h5>
            </div>
            <p class="text-muted mb-1">Date: {{ review.date }}</p>
            <p>{{ review.content }}</p>
            <div class="d-flex align-items-center">
              <span class="me-2">{{ review.likes }}</span>
              <button class="btn btn-outline-primary btn-sm">
                <i class="bi bi-hand-thumbs-up"></i> Helpful
              </button>
            </div>
          </div>
        </div>
      </div>
  
      <!-- 하단 화살표 -->
      <div class="text-center mt-4">
        <button class="btn btn-outline-secondary" @click="goToAllReviews">
          <i class="bi bi-chevron-down"></i>
        </button>
      </div>
    </div>
  </template>
  
<script setup>
  import { reactive } from "vue";
  
    //  더미데이터
  const movie = reactive({
    title: "Dune: Part Two",
    year: 2024,
    runtime: "2h 46m",
    rating: "PG-13",
    avgRating: 8.9,
    ratingCount: 200,
    poster: "https://via.placeholder.com/300x400",
    reviews: [
      {
        rating: 10,
        title: "One Of The Greatest Sequel Ever Made",
        date: "20 Feb 2024",
        content:
          "In the quiet embrace of ink and page, a story unfolded, timeless and sage, through the lens of a filmmaker's artistry...",
        likes: 210,
      },
      {
        rating: 5,
        title: "A Good Watch, but Not Without Flaws",
        date: "15 Feb 2024",
        content:
          "While visually stunning, the pacing of the movie felt uneven. Still, the acting and direction made up for some of its shortcomings.",
        likes: 87,
      },
      {
        rating: 1,
        title: "Disappointing and Overhyped",
        date: "10 Feb 2024",
        content:
          "Unfortunately, the movie failed to deliver on the promise set by its predecessor. A major letdown in many aspects.",
        likes: 50,
      },
    ],
  });
  
  const getReviewBgColor = (rating) => {
    if (rating >= 8) return "#E3E8DE"; // 10점 색상
    if (rating >= 5) return "#F2F4F0"; // 5점 색상
    return "#FAFAFA"; // 1점 색상
  };
  
  const goToAllReviews = () => {
    // 이동할 페이지 URL (예: 리뷰 페이지)
    window.location.href = "/reviews";
  };
</script>
  
<style scoped>
/* 이 개못생긴 버튼 빨리 고치기 */
  .container {
    max-width: 1200px;
  }
  
  /* 리뷰 카드 스타일 */
  .review-card {
    border-radius: 10px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  }
  
  /* 포스터 이미지 */
  img {
    border-radius: 10px;
  }
  
  /* 하단 화살표 버튼 */
  .btn-outline-secondary {
    font-size: 1.5rem;
    border-radius: 50%;
    width: 50px;
    height: 50px;
  }

</style>
  